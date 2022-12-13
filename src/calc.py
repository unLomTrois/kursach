"""Модуль калькулятора расхода газа"""


class GasCalculator:
    """
    Класс калькулятора расхода газа
    """

    # мощность
    power: float
    # цена топлива
    price: float
    # КПД
    efficiency: float = 0.476
    # удельная теплота сгорания (МДж/м3)
    heating_value: float = 34.02

    def __init__(self, power: float, price: float):
        """конструктор класса"""

        self.power = power
        self.price = price

        # вычислить максимальный расход газа
        self.max_gas_usage()

    def max_gas_usage(self):
        """вычисляет максимальный расход газа в час"""
        return self.power / (self.heating_value * 0.278 * self.efficiency)

    def price_per_day(self):
        """вычисляет максимальную стоимость топлива в день"""
        return round(self.max_gas_usage() * 8 * self.price, 2)

    def price_per_month(self):
        """вычисляет максимальную стоимость топлива в месяц"""
        return round(self.max_gas_usage() * 8 * 30 * self.price, 2)

    def price_per_year(self):
        """вычисляет максимальную стоимость топлива в год"""
        return round(self.max_gas_usage() * 8 * 365 * self.price, 2)
