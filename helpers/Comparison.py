from typing import Any
import itertools
import pandas as pd
import math

# from sklearn.metrics import accuracy_score


def comparison_table(data: pd.DataFrame) -> pd.DataFrame:
    """This function will calculate the accuracy of each prediction with the others."""

    listOfColumns = list(data.columns)
    # remove text from column list
    listOfColumns.pop(listOfColumns.index("normalized tweet"))
    # create the possible combinations each two
    possibleCombination = list(itertools.combinations(listOfColumns, 2))

    # calculate the accuracy of each part
    # final_list = [accuracy_score(data[el[0]], data[el[1]]) for el in possibleCombination]

    final_list: list[Any] = [
        [
            el,
            manhattan_distance(data[el[0]], data[el[1]]),
            euclidean_distance(data[el[0]], data[el[1]]),
        ]
        for el in possibleCombination
    ]

    return pd.DataFrame(data=final_list, columns=["Pairs", "Manhattan", "Euclidean"])


def manhattan_distance(list1, list2):
    """To calculate Manhattan distance."""
    return sum(abs(x1 - x2) for x1, x2 in zip(list1, list2))


def euclidean_distance(list1, list2):
    """To calculate Euclidean distance."""
    return math.sqrt(sum((x - y) ** 2 for x, y in zip(list1, list2)))
