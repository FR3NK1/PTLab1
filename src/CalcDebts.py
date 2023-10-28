# -*- coding: utf-8 -*-
from Types import DataType


class CalcDebts:
    def __init__(self, data: DataType) -> None:
        self.data: DataType = data
        self.students_with_debts: int = 0

    def calc(self) -> int:
        for subjects in self.data.values():
            count_bad_scores = sum(1 for _, score in subjects if score < 61)
            if count_bad_scores == 2:
                self.students_with_debts += 1
        return self.students_with_debts
