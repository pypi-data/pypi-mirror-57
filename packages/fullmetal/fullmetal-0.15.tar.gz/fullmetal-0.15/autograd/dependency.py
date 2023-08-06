
from typing import List, NamedTuple, Callable, Optional, Union
import numpy as np
import weakref

class Dependency(object):

    def __init__(self, node, grad_fn):
        self.Node = weakref.proxy(node)
        self.grad_fn = grad_fn

    def __repr__(self) -> str:
        return f"Dependency(Node{self.Node}, grad_fn{self.grad_fn})"
