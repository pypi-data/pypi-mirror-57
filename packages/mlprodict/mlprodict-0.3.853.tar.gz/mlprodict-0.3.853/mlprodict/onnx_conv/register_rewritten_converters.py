"""
@file
@brief Rewrites some of the converters implemented in
:epkg:`sklearn-onnx`.
"""
from skl2onnx.common._registration import _converter_pool
from .sklconv.ada_boost import convert_sklearn_ada_boost_regressor
from .sklconv.tree_converters import (
    convert_sklearn_decision_tree_regressor,
    convert_sklearn_gradient_boosting_regressor,
    convert_sklearn_random_forest_regressor_converter,
)
from .sklconv.svm_converters import convert_sklearn_svm


_overwritten_operators = {
    'SklearnAdaBoostRegressor': convert_sklearn_ada_boost_regressor,
    'SklearnDecisionTreeRegressor': convert_sklearn_decision_tree_regressor,
    'SklearnExtraTreesRegressor': convert_sklearn_random_forest_regressor_converter,
    'SklearnGradientBoostingRegressor': convert_sklearn_gradient_boosting_regressor,
    'SklearnHistGradientBoostingRegressor': convert_sklearn_random_forest_regressor_converter,
    'SklearnOneClassSVM': convert_sklearn_svm,
    'SklearnRandomForestRegressor': convert_sklearn_random_forest_regressor_converter,
    'SklearnSVC': convert_sklearn_svm,
    'SklearnSVR': convert_sklearn_svm,
}


def register_rewritten_operators(new_values=None):
    """
    Registers modified operators and returns the old values.

    @param      new_values      operators to rewrite or None
                                to rewrite default ones
    @return                      old values
    """
    if new_values is None:
        for rew in _overwritten_operators:
            if rew not in _converter_pool:
                raise KeyError(
                    "skl2onnx was not imported and '{}' was not registered.".format(rew))
        old_values = {k: _converter_pool[k] for k in _overwritten_operators}
        _converter_pool.update(_overwritten_operators)
        return old_values
    else:
        for rew in new_values:
            if rew not in _converter_pool:
                raise KeyError(
                    "skl2onnx was not imported and '{}' was not registered.".format(rew))
        old_values = {k: _converter_pool[k] for k in new_values}
        _converter_pool.update(new_values)
        return old_values
