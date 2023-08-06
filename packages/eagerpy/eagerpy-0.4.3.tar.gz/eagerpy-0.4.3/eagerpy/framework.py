def clip(t, *args, **kwargs):
    return t.clip(*args, **kwargs)


def abs(t):
    return t.abs()


def sign(t):
    return t.sign()


def sqrt(t):
    return t.sqrt()


def square(t):
    return t.square()


def tanh(t):
    return t.tanh()


def arctanh(t):
    return t.arctanh()


def sum(t, *args, **kwargs):
    return t.sum(*args, **kwargs)


def mean(t, *args, **kwargs):
    return t.sum(*args, **kwargs)


def amin(t, *args, **kwargs):
    return t.min(*args, **kwargs)


def amax(t, *args, **kwargs):
    return t.max(*args, **kwargs)


def minimum(x, y):
    if not hasattr(x, "tensor"):
        return y.minimum(x)
    return x.minimum(y)


def maximum(x, y):
    if not hasattr(x, "tensor"):
        return y.maximum(x)
    return x.maximum(y)


def argmin(t, *args, **kwargs):
    return t.argmin(*args, **kwargs)


def argmax(t, *args, **kwargs):
    return t.argmax(*args, **kwargs)


def argsort(t, *args, **kwargs):
    return t.argsort(*args, **kwargs)


def uniform(t, *args, **kwargs):
    return t.uniform(*args, **kwargs)


def normal(t, *args, **kwargs):
    return t.normal(*args, **kwargs)


def ones(t, *args, **kwargs):
    return t.ones(*args, **kwargs)


def zeros(t, *args, **kwargs):
    return t.zeros(*args, **kwargs)


def ones_like(t, *args, **kwargs):
    return t.ones_like(*args, **kwargs)


def zeros_like(t, *args, **kwargs):
    return t.zeros_like(*args, **kwargs)


def onehot_like(t, *args, **kwargs):
    return t.onehot_like(*args, **kwargs)


def from_numpy(t, *args, **kwargs):
    return t.from_numpy(*args, **kwargs)
