"""
loss function to optimizer functions
"""
import numpy as np
from nn_numpy.tensor import Tensor

class Loss:
    def loss(self, predicted: Tensor, actual: Tensor) -> float:
        raise NotImplementedError

    def grad(self, predicted: Tensor, actual: Tensor) -> Tensor:
        raise NotImplementedError

class MSE(Loss):
    """
    MSE is mean square error
    """
    def loss(self, predicted: Tensor, actual: Tensor) -> float:
        return np.sum((predicted-actual)**2)

    def grad(self, predicted: Tensor, actual: Tensor) -> Tensor:
        return 2*(predicted-actual)