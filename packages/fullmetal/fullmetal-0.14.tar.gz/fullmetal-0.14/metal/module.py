from typing import Iterator
import inspect
from autograd.tensor import Tensor
from autograd.parameter import Parameter
import numpy as np

class Module:
    def parameters(self) -> Iterator[Parameter]:
        for name, value in inspect.getmembers(self):
            if isinstance(value, Parameter):
                yield value
            if isinstance(value, Tensor):
                yield value
            elif isinstance(value, Module):
                yield from value.parameters()

    def zero_grad(self):
        for parameter in self.parameters():
            parameter.zero_grad()
            del parameter.depends_on[:]

    def _np(self):
        for name, value in inspect.getmembers(self):
            if isinstance(value, np.ndarray):
                yield value
            elif isinstance(value, Module):
                yield from value._np()

    def del_numpy(self):
        for i in self._np():
            del i
            
