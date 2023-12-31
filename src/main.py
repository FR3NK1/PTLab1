# -*- coding: utf-8 -*-
import argparse
import sys

from DataReader import DataReader

from CalcRating import CalcRating
from CalcDebts import CalcDebts
from TextDataReader import TextDataReader
from XmlDataReader import XmlDataReader


def get_path_from_arguments(args) -> str:
    parser = argparse.ArgumentParser(description="Path to datafile")
    parser.add_argument(
        "-p", dest="path", type=str, required=True, help="Path to datafile"
    )
    args = parser.parse_args(args)
    return args.path


def get_reader(path: str) -> DataReader:
    file_extension = path.split(".")[-1]
    print(file_extension)
    if file_extension == "txt":
        return TextDataReader()
    elif file_extension == "xml":
        return XmlDataReader()
    else:
        raise ValueError("Расширение файла не поддерживается")


def main():
    path = get_path_from_arguments(sys.argv[1:])

    reader = get_reader(path)
    students = reader.read(path)
    print("Students: ", students)

    rating = CalcRating(students).calc()
    print("Rating: ", rating)

    debts = CalcDebts(students).calc()
    print("Debts:", debts)


if __name__ == "__main__":
    main()
