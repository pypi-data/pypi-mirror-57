import numpy as np

from tests.wrappers.uber import backprop_test_factory, fwdprop_test_factory
from mynn.activations import (
    elu,
    glu,
    hard_tanh,
    leaky_relu,
    log_softmax,
    relu,
    selu,
    sigmoid,
    softmax,
    soft_sign,
)


def _away_from_zero(*args, **kwargs):
    x = args[0]
    return np.all(np.abs(x.data) > 1e-08)


def test_elu_fwd():
    pass


def test_elu_bkwd():
    pass


def test_glu_fwd():
    pass


def test_glu_bkwd():
    pass


def test_hard_tanh_fwd():
    pass


def test_hard_tanh_bkwd():
    pass


def _np_leaky_relu(x, slope):
    return np.maximum(x, 0) + slope * np.minimum(x, 0)


@fwdprop_test_factory(mygrad_func=leaky_relu, true_func=_np_leaky_relu, num_arrays=1)
def leaky_relu_fwd():
    pass


@backprop_test_factory(mygrad_func=leaky_relu, true_func=_np_leaky_relu, num_arrays=1)
def leaky_relu_bkwd():
    pass


# @fwdprop_test_factory(
#     mygrad_func=log_softmax,
#     true_func=lambda x: np.log(np.exp(x) / np.exp(x).sum()),
#     num_arrays=1,
#     assumptions=_away_from_zero,
# )
# def test_log_softmax_fwd():
#     pass


def _np_log_softmax(x):
    x = x - x.max()
    x = np.exp(x)
    return np.log(x / x.sum())

# @backprop_test_factory(
#     mygrad_func=log_softmax,
#     true_func=_np_log_softmax,
#     num_arrays=1,
#     assumptions=_away_from_zero,
# )
# def test_log_softmax_bkwd():
#     pass


@fwdprop_test_factory(
    mygrad_func=relu, true_func=lambda x: np.maximum(x, 0), num_arrays=1
)
def test_relu_fwd():
    pass


@backprop_test_factory(
    mygrad_func=relu,
    true_func=lambda x: np.maximum(x, 0),
    num_arrays=1,
    assumptions=_away_from_zero,
)
def test_relu_bkwd():
    pass


def test_selu_fwd():
    pass


def test_selu_bkwd():
    pass


def test_sigmoid_fwd():
    pass


def test_sigmoid_bkwd():
    pass


def test_softmax_fwd():
    pass


def test_softmax_bkwd():
    pass


def test_soft_sign_fwd():
    pass


def test_soft_sign_bkwd():
    pass
