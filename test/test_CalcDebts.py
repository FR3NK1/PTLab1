# -*- coding: utf-8 -*-
from src.Types import DataType
from src.CalcDebts import CalcDebts
import pytest

RatingsType = dict[str, float]


class TestCalcDebts:
    @pytest.fixture()
    def input_data(self) -> tuple[DataType, int]:
        data: DataType = {
            "Абрамов Петр Сергеевич": [
                ("математика", 55),
                ("русский язык", 65),
                ("программирование", 58)
            ],
            "Петров Игорь Владимирович": [
                ("математика", 59),
                ("русский язык", 60),
                ("программирование", 95),
                ("литература", 97)
            ],
            "Сидоров Илья Алексеевич": [
                ("математика", 70),
                ("русский язык", 80),
                ("программирование", 78)
            ],
        }

        students_with_debts = 2  # Исходя из данных, только Абрамов и Петров имеют задолженности по двум предметам.

        return data, students_with_debts

    def test_init_calc_rating(self, input_data: tuple[DataType,
                                                      int]) -> None:
        calc_rating = CalcDebts(input_data[0])
        assert input_data[0] == calc_rating.data

    def test_calc(self, input_data: tuple[DataType, int]) -> None:
        number_of_students = CalcDebts(input_data[0]).calc()
        assert number_of_students == input_data[1]