import numpy as np
from autograd.tensor import Tensor
from autograd.parameter import Parameter
from metal.module import Module
from autograd.dependency import Dependency
import math
import copy
from metal.layers.layer import Layer

class Flatten(Layer):
    __slots__ =( 'prev_shape', 'trainable','type' )

    """ Turns a multidimensional matrix into two-dimensional """
    def __init__(self, input_shape=None):
        self.prev_shape = None
        self.trainable = True
        self.input_shape = input_shape

    def forward_pass(self, x_, training=True):
        self.x = x_
        self.prev_shape = x_.shape
        self.type = type(x_)
        requires_grad = x_.requires_grad

        if requires_grad:
            depends_on = [Dependency(self.x, self.gardflatten)]
        else:
            depends_on = []
        return self.type(data=self.x.data.reshape((self.x.shape[0], -1)),requires_grad=requires_grad,depends_on=depends_on)

    def gardflatten(self, accum_grad):
        return accum_grad.reshape(self.prev_shape)

    def update_pass(self):
        self.np_del()


    def output_shape(self):
        return (np.prod(self.input_shape),)
