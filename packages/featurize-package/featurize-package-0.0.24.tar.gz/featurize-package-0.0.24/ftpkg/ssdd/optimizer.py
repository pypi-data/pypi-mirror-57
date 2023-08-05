from featurize_jupyterlab.core import Optimizer, Option
from torch.optim import SGD


class PyTorchSGD(Optimizer):
    """Simple wrap of the SGD optimizer of PyTorch
    """
    learning_rate = Option(name="Learning Ratel", default=0.1, type='number')
    model = Option(type='hardcode')

    def __call__(self):
        return SGD(self.model.parameters(), float(self.learning_rate))
