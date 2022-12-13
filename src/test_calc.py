"""Тестирует калькулятор"""

from calc import GasCalculator


def test_calc_has_methods():
    """Тестирует что в классе calc все методы определены"""
    calc = GasCalculator(power=10, price=10)
    assert calc.max_gas_usage is not None
    assert calc.price_per_day is not None
    assert calc.price_per_month is not None
    assert calc.price_per_year is not None


def test_calc_max_gas_usage_formula():
    """Тестирует, что функция соответствует формуле"""
    calc = GasCalculator(power=10, price=10)
    formula = 10 / (34.02 * 0.278 * 0.476)
    assert calc.max_gas_usage() == formula
    assert calc.max_gas_usage() == 2.221334399289514
