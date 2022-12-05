"""_summary_
"""


class EnergyCalculator:
    """
    Общий класс для калькуляторов,
    возможно использовать не только для калькулятора природного газа
    """

    # цена топлива
    price: float
    # КПД
    efficiency: float
    # мощность
    power: float
    # удельная теплота сгорания (МДж/м3)
    heating_value: float
    v_max: float  # м3/час - максимальный расход газа
    v_avg: float  # м3/час - средний расход газа


class GasCalculator(EnergyCalculator):
    """
    Класс для вычисления
    """

    def __init__(
        self,
        power: float,
        price: float,
        # для плит КПД составляет 30-60%, поэтому среднее 45%
        efficiency: float = 0.45,
        # табличное значение согласно справочнику по физике Х.Кухлинга
        heating_value: float = 35.9,  # (МДж/м3)
    ):
        """конструктор класса"""

        self.power = power
        self.price = price
        self.efficiency = efficiency
        self.heating_value = heating_value

        # вычислить максимальный расход газа
        self.calc_max_v()

    def calc_max_v(self):
        """вычисляет максимальный расход"""
        self.v_max = self.power / (self.heating_value * 0.278 * self.efficiency)
        self.v_avg = self.v_max / 2

    def price_per_hour(self):
        """вычисляет стоимость за часовой расход топлива"""
        price_per_hour = round(self.v_max * self.price, 2)
        print("цена в час:", price_per_hour, "руб")
        return price_per_hour

    def v_per_day(self):
        """вычисляет максимальный расход топлива в день"""
        return (
            self.v_max * 8
        )  # 8, потому что редко когда печь используется более 8 часов

    def v_per_month(self):
        """вычисляет максимальный расход топлива в месяц"""
        return self.v_per_day() * 30

    def v_per_year(self):
        """вычисляет максимальный расход топлива в год"""
        return self.v_per_month() * 12

    def price_per_day(self):
        """вычисляет стоимость топлива в день"""
        price_per_day = round(self.v_per_day() * self.price, 2)
        print("цена в день:", price_per_day / 2, "-", price_per_day, "руб")
        return price_per_day

    def price_per_month(self):
        """вычисляет расход в месяц"""
        price_per_month = round(self.v_per_month() * self.price, 2)
        print("цена в день:", price_per_month / 2, "-", price_per_month, "руб")
        return price_per_month

    def per_year(self):
        """вычисляет расход в год"""
        price_per_year = round(self.v_per_year() * self.price, 2)
        print("цена в год:", price_per_year / 2, "-", price_per_year, "руб")
        return price_per_year
