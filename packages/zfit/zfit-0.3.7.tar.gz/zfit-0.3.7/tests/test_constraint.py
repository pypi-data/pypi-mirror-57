#  Copyright (c) 2019 zfit
import pytest
import numpy as np
import scipy.stats

import zfit
from zfit import ztf
from zfit.core.testing import setup_function, teardown_function, tester
from zfit.util.exception import ShapeIncompatibleError
from zfit.core.constraint import BaseConstraint, SimpleConstraint, GaussianConstraint
from zfit.util.container import convert_to_container


def true_nll_gaussian(params, mu, sigma):
    params = convert_to_container(params, container=tuple)
    mu = convert_to_container(mu, container=tuple)
    sigma = convert_to_container(sigma, container=tuple)
    constraint = ztf.constant(0.)
    if not len(params) == len(mu) == len(sigma):
        raise ValueError("params, mu and sigma have to have the same length.")
    for param, mean, sig in zip(params, mu, sigma):
        constraint += ztf.reduce_sum(ztf.square(param - mean) / (2. * ztf.square(sig)))

    return constraint


def test_base_constraint():  # TODO(Mayou36): upgrade to tf2, use ABC again
    # with pytest.raises(TypeError):
    #     _ = BaseConstraint()
    pass


def test_gaussian_constraint_shape_errors():
    param1 = zfit.Parameter("Param1", 5)
    param2 = zfit.Parameter("Param2", 6)

    with pytest.raises(ShapeIncompatibleError):
        GaussianConstraint([param1, param2], mu=[4, 2, 3], sigma=5)
    with pytest.raises(ShapeIncompatibleError):
        GaussianConstraint([param1, param2], mu=[4, 2], sigma=5)
    with pytest.raises(ShapeIncompatibleError):
        GaussianConstraint([param1, param2], mu=2, sigma=[1, 4])
    with pytest.raises(ShapeIncompatibleError):
        GaussianConstraint(param1, mu=[4, 2], sigma=[2, 3])


def test_gaussian_constraint_matrix():
    param1 = zfit.Parameter("Param1", 5)
    param2 = zfit.Parameter("Param2", 6)
    params = [param1, param2]

    mu = [3., 6.1]
    sigma = np.array([[1, 0.3],
                      [0.3, 0.5]])
    constr = GaussianConstraint(params=params, mu=mu, sigma=sigma)
    constr_np = zfit.run(constr.value())
    assert constr_np == pytest.approx(3.989638)

    assert constr.get_dependents() == set(params)


def test_gaussian_constraint():
    param_vals = [5, 6, 3]
    mu = [3, 6.1, 4.3]
    sigma = [1, 0.3, 0.7]
    true_val = true_gauss_constr_value(param_vals, mu, sigma)
    params = [zfit.Parameter(f"Param{i}", val) for i, val in enumerate(param_vals)]

    constr = GaussianConstraint(params=params, mu=mu, sigma=sigma)
    value_tensor = constr.value()
    constr_np = zfit.run(value_tensor)
    assert constr_np == pytest.approx(true_val)
    assert constr.get_dependents() == set(params)

    param_vals[0] = 2
    params[0].set_value(param_vals[0])

    constr2_np = zfit.run(value_tensor)
    constr2_newtensor_np = zfit.run(constr.value())
    assert constr2_newtensor_np == pytest.approx(constr2_np)

    true_val2 = true_gauss_constr_value(param_vals, mu, sigma)
    assert constr2_np == pytest.approx(true_val2)


def test_gaussian_constraint_orderbug():  # as raised in #162
    param_vals = [1500, 1.0, 1.0, 1.0, 0.5]
    params = [zfit.Parameter(f"param{i}", val) for i, val in enumerate(param_vals)]

    mu = param_vals
    sigma = [0.05 * 1500, 0.001, 0.01, 0.1, 0.05 * 0.5]
    true_val = true_gauss_constr_value(params=param_vals, mu=mu, sigma=sigma)

    constr1 = zfit.constraint.GaussianConstraint(params=params, mu=mu, sigma=sigma)

    value_tensor = constr1.value()
    constr_np = zfit.run(value_tensor)
    assert constr_np == pytest.approx(true_val)
    assert true_val < 10000


def test_gaussian_constraint_orderbug2():  # as raised in #162, failed before fixing
    param1 = zfit.Parameter("param1", 1500)
    param5 = zfit.Parameter("param2", 0.5)

    param2 = zfit.Parameter("param3", 1.0)
    param3 = zfit.Parameter("param4", 1.0)
    param4 = zfit.Parameter("param5", 1.0)

    constraint = {"params": [param1, param2, param3, param4, param5],
                  "mu": [1500, 1.0, 1.0, 1.0, 0.5],
                  "sigma": [0.05 * 1500, 0.001, 0.01, 0.1, 0.05 * 0.5]}

    constr1 = zfit.constraint.GaussianConstraint(**constraint)
    # param_vals = [1500, 1.0, 1.0, 1.0, 0.5]
    constraint['params'] = zfit.run(constraint['params'])

    true_val = true_gauss_constr_value(**constraint)

    value_tensor = constr1.value()
    constr_np = zfit.run(value_tensor)
    assert constr_np == pytest.approx(true_val)
    assert true_val < 1000
    assert true_val == pytest.approx(-8.592, abs=0.1)  # if failing, change value. Hardcoded for additional layer


def true_gauss_constr_value(params, mu, sigma):
    return -np.sum(np.log(scipy.stats.norm.pdf(x, loc=mu, scale=sigma)) for x, mu, sigma in zip(params,
                                                                                                mu,
                                                                                                sigma))


@pytest.mark.flaky(3)
def test_gaussian_constraint_sampling():
    param1 = zfit.Parameter("Param1", 5)
    params = [param1]

    mu = [5]
    sigma = [1]
    constr = GaussianConstraint(params=params, mu=mu, sigma=sigma)

    sample = constr.sample(15000)

    assert np.mean(sample[param1]) == pytest.approx(mu[0], rel=0.01)
    assert np.std(sample[param1]) == pytest.approx(sigma[0], rel=0.01)


def test_simple_constraint():
    param1 = zfit.Parameter("Param1", 5)
    param2 = zfit.Parameter("Param2", 6)
    params = [param1, param2]

    mu = [3., 6.1]
    sigma = [1., 0.5]

    def func():
        return true_nll_gaussian(params=params, mu=mu, sigma=sigma)

    constr = SimpleConstraint(func=func)

    constr_np = zfit.run(constr.value())
    assert constr_np == pytest.approx(2.02)

    assert constr.get_dependents() == set(params)
