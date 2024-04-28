"""
    Ayiza Muzaffar - am819 - 5136283
    Berthold Dominique Buri - bb268 - 4744252
    Henry Juncker - hj84 - 5605330

    falls der Plot neu erstellt werden soll,
    entkommentieren sie Zeile 125
"""


import random
import math
import numpy as np
import time
from matplotlib import pyplot as plt


def split_array_into_even_parts(a, n):
    """
        Teilt einen Array a in n ca. gleich große Teile auf
    """
    k, m = divmod(len(a), n)
    return list(a[i*k+min(i, m):(i+1)*k+min(i+1, m)] for i in range(n))


def merge_two_arrays(arr1, arr2):
    """
        Zusammenführen und Sortieren von zwei Arrays.
        Gleicher Aufbau wie in der Vorlesung.
    """
    merged_arr = []
    pos = 0
    i = 0
    j = 0
    len1 = len(arr1)
    len2 = len(arr2)

    while pos < len1 + len2:
        if i < len1 and (j >= len2 or arr1[i] < arr2[j]):
            merged_arr.append(arr1[i])
            pos += 1
            i += 1
        else:
            merged_arr.append(arr2[j])
            pos += 1
            j += 1

    return merged_arr


def merge_sort_recursive(arr, k):
    """
       Perform merge sort on a list, splitting it into k parts.

       Args:
           arr (list): The list to be sorted.
           k (int): The number of parts to split the list into.

       Returns:
           list: The sorted list.

       Examples:
           >>> merge_sort_recursive([12, 11, 13, 5, 6, 7], 3)
           [5, 6, 7, 11, 12, 13]
           >>> merge_sort_recursive([], 10)
           []
           >>> merge_sort_recursive([9], 10)
           [9]
    """
    n = len(arr)
    if n <= 1:
        return arr

    split_arr = split_array_into_even_parts(arr, k)
    sorted_arr = []

    # Iterration durch die k Teile des Arrays um
    # * Rekursivität zu ermöglichen und
    # * den sortedArray immer im direkten Vergleich
    #   mit dem nächsten Split vom Array zu mergen und sortieren.
    for elem in split_arr:
        elem = merge_sort_recursive(elem, k)
        sorted_arr = merge_two_arrays(sorted_arr, elem)

    return sorted_arr


def create_plot():
    list_n = np.arange(100, 10001, 1000)
    values_k = {}

    for n in list_n:
        print(n)
        list_k = [2, 3, int(math.log2(n)), n//4]
        arr = [random.randint(0, 10000) for i in range(n)]

        for idx, k in enumerate(list_k):
            anfang = time.perf_counter()
            merge_sort_recursive(arr, k)
            if idx not in values_k:
                values_k[idx] = []
            values_k[idx].append(time.perf_counter() - anfang)

    list_label = ["k=2", "k=3", "k=log2(n)", "k=n/4"]
    for k in values_k:
        plt.plot(list_n, values_k[k], label=list_label[k])
    plt.legend()
    plt.show()
    print("fertig")


# testing some random arrays to help you check correctness
if __name__ == "__main__":
    n = 1000
    k_limit = 20
    for k in range(2, k_limit):
        arr = [random.randint(0, 10000) for i in range(n)]
        sorted_arr = merge_sort_recursive(arr, k)
        if not sorted_arr == sorted(arr):
            raise Exception("Didn't Sort Correctly!")
    print("seems to work")

    # falls der Plot neu erstellt werden soll,
    # entkommentieren sie die nächste Zeile
    # create_plot()
