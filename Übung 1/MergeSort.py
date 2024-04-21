import random


def SplitArrayIntoEvenParts (a, n):
    """
        Teilt einen Array a in n ca. gleich große Teile auf
        * Hab ich so von StackOverflow, kann man evtl. noch durch eigenen Code ersetzen
    """
    k, m = divmod(len(a), n)
    return list(a[i*k+min(i, m):(i+1)*k+min(i+1, m)] for i in range(n))

def MergeTwoArrays (arr1, arr2):
    """
        Zusammenführen und Sortieren von zwei Arrays.
        Gleicher Aufbau wie in der Vorlesung.
    """
    mergedArr = []
    pos = 0
    i = 0
    j = 0
    len1 = len(arr1)
    len2 = len(arr2)

    while pos < len1 + len2:
        if i < len1 and (j >= len2 or arr1[i] < arr2[j]):
            mergedArr.append (arr1[i])
            pos += 1
            i += 1
        else:
            mergedArr.append (arr2[j])
            pos += 1
            j += 1
    
    return mergedArr

def MergeSortRecursive (arr, k):
    """
       Perform merge sort on a list, splitting it into k parts.

       Args:
           arr (list): The list to be sorted.
           k (int): The number of parts to split the list into.

       Returns:
           list: The sorted list.

       Examples:
           >>> MergeSortRecursive([12, 11, 13, 5, 6, 7], 3)
           [5, 6, 7, 11, 12, 13]
           >>> MergeSortRecursive([], 10)
           []
           >>> MergeSortRecursive([9], 10)
           [9]
    """
    n = len(arr)
    if n <= 1:
        return arr
    
    splitArr = SplitArrayIntoEvenParts(arr, k)
    sortedArr = []

    # Iterration durch die k Teile des Arrays um
    # * Rekursivität zu ermöglichen und
    # * den sortedArray immer im direkten Vergleich mit dem nächsten Split vom Array zu mergen und sortieren.
    for elem in splitArr:
        elem = MergeSortRecursive(elem, k)
        sortedArr = MergeTwoArrays(sortedArr, elem)
    
    return sortedArr


# testing some random arrays to help you check correctness
if __name__ == "__main__":
    n = 1000
    k_limit = 20
    for k in range(2, k_limit):
        arr = [random.randint(0, 10000) for i in range(n)]
        sorted_arr = MergeSortRecursive(arr, k)
        if not sorted_arr == sorted(arr):
            raise Exception("Didn't Sort Correctly!")
    print("seems to work")