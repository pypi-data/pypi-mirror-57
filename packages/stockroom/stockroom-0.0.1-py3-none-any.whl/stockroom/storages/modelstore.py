import numpy as np

from .storagebase import StorageBase
from ..utils import get_current_head, get_stock_root
from .. import parser


class ModelStore(StorageBase):
    """
    ModelStore class utilizes hangar arraysets to store the pieces of a model and
    use hangar metadata to store the information required to collate it back to
    a model. It right now supports ``keras.Model`` and ``torch.nn.Module`` models.
    ModelStore instance, on :meth:`storages.ModelStore.save` creates few arraysets
    to store the weights and create one arrayset specifically to store the shape
    of each layer. This shape arrayset is needed because the weights of each
    layer would be flattened before saving. This is essential since handling variable
    shapes and variable ranks are more complex than flattening and reshaping-back the
    weights.
    """

    def __init__(self, write):
        super().__init__()
        self.write = write
        self.opened_aset = []

    def save(self, name, model):
        if not self.write:
            raise RuntimeError("ModelStore instance is not write-enabled")
        if hasattr(model, 'state_dict'):
            state = model.state_dict()
            weights = [x.numpy() for x in state.values()]
            layers = state.keys()
            library = 'torch'
        elif hasattr(model, 'get_weights'):
            library = 'tf'
            layers = None
            weights = model.get_weights()
        else:
            raise TypeError("Unknown model type. StockRoom can work with only "
                            "``Keras.Model`` or ``torch.nn.Module`` modules")
        # TODO: make sure the longest becoming longer is not an issue: add test
        longest = str(max([len(x.reshape(-1)) for x in weights]))
        dtypes = [w.dtype.name for w in weights]

        co = self.repo.checkout(write=True)
        self.store_metadata(co, name,
                            library=library,
                            longest=longest,
                            dtypes=dtypes,
                            numLayers=str(len(weights)),
                            layers=layers)
        shapeKey = parser.shapekey(name, longest)
        shape_aset = self.get_arrayset(co, shapeKey)
        if shape_aset is None:
            shape_aset = self.create_arrayset(co, shapeKey, 10, 'int64', variable_shape=True)
        for i, w in enumerate(weights):
            modelKey = parser.modelkey(name, longest, dtypes[i])
            model_aset = self.get_arrayset(co, modelKey)
            if model_aset is None:
                model_aset = self.create_arrayset(
                    co, modelKey, int(longest), dtypes[i], variable_shape=True)
            model_aset[i] = w.reshape(-1)
            if w.shape:
                shape_aset[i] = np.array(w.shape)
            else:
                shape_aset[i] = np.array(()).astype('int64')
        self.close_arraysets()
        co.close()

    def load(self, name, model):
        root = get_stock_root()
        head_commit = get_current_head(root)
        co = self.repo.checkout(commit=head_commit)
        library, longest, dtypes, numLayers, layers = self.get_metadata(co, name)
        shapeKey = parser.shapekey(name, longest)
        shape_aset = self.get_arrayset(co, shapeKey)
        weights = []
        for i in range(numLayers):
            modelKey = parser.modelkey(name, longest, dtypes[i])
            aset = self.get_arrayset(co, modelKey)
            w = aset[i].reshape(np.array(shape_aset[i]))
            weights.append(w)
        if len(weights) != numLayers:
            raise RuntimeError(
                "Critical: Discrepancy in the stored data: numLayers != len(weights)")
        if library == 'torch':
            import torch
            state = {layers[i]: torch.from_numpy(weights[i]) for i in range(numLayers)}
            model.load_state_dict(state)
        else:
            model.set_weights(weights)

    @staticmethod
    def store_metadata(co, name, library, longest, dtypes, numLayers, layers=None):
        co.metadata[parser.metakey(name, 'library')] = library
        if library == 'torch':
            if layers is None:
                raise ValueError("Could not fetch layer information for the torch model")
            co.metadata[parser.metakey(name, 'layers')] = parser.encode(layers)
        co.metadata[parser.metakey(name, 'library')] = library
        co.metadata[parser.metakey(name, 'longest')] = longest
        co.metadata[parser.metakey(name, 'numLayers')] = numLayers
        co.metadata[parser.metakey(name, 'dtypes')] = parser.encode(dtypes)

    @staticmethod
    def get_metadata(co, name):
        library = co.metadata[parser.metakey(name, 'library')]
        if library == 'torch':
            layers = co.metadata[parser.metakey(name, 'layers')]
            layers = parser.decode(layers)
        else:
            layers = None
        library = co.metadata[parser.metakey(name, 'library')]
        longest = co.metadata[parser.metakey(name, 'longest')]
        numLayers = co.metadata[parser.metakey(name, 'numLayers')]
        dtypes = co.metadata[parser.metakey(name, 'dtypes')]
        dtypes = parser.decode(dtypes)
        return library, longest, dtypes, int(numLayers), layers

    def get_arrayset(self, co, name):
        try:
            aset = co.arraysets[name]
            aset.__enter__()
            self.opened_aset.append(aset)
            return aset
        except KeyError:
            return None

    def create_arrayset(self, co, name, longest=None, dtype=None, variable_shape=False):
        self.close_arraysets()
        aset = co.arraysets.init_arrayset(
            name, dtype=np.dtype(dtype), shape=(longest,), variable_shape=variable_shape)
        self.opened_aset.append(aset)

        # open all the closed arraysets
        for val in self.opened_aset:
            val.__enter__()
        return aset

    def close_arraysets(self):
        for aset in self.opened_aset:
            aset.__exit__()


def modelstore(write=False):
    return ModelStore(write=write)
