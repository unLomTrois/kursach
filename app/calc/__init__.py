"""_summary_
"""


from typing import Optional


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

    # табличное значение согласно справочнику по физике Х.Кухлинга
    heating_value = 35.9
    # для плит КПД составляет 30-60%, поэтому среднее 45%
    efficiency = 0.45

    def __init__(
        self,
        power: Optional[float] = None,
        price: Optional[float] = None,
        efficiency: Optional[float] = None,
    ):
        """конструктор класса"""
        # если power или price не указаны, то спросить пользователя о них
        self.power = power if power is not None else self.ask_for_power()
        self.price = (
            price
            if price is not None
            else float(input("введите цену на топливо (руб/м3)"))
        )
        if efficiency is not None:
            self.efficiency = efficiency
        # вычислить максимальный расход газа
        self.calc_max_v()

    def calc_max_v(self):
        """вычисляет максимальный расход"""
        self.v_max = self.power / (self.heating_value * 0.278 * self.efficiency)
        self.v_avg = self.v_max / 2

    def ask_for_power(self):
        """функция просит пользователя указать мощность устройства"""

        burner_count = int(input("введите количество конфорок"))
        power = 0
        for n in range(burner_count):
            power += float(input(f"введите мощность {n+1}-й конфорки (кВт)"))
        print("номинальная мощность плиты:", power, "(кВт)")
        return power

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
