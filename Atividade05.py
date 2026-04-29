def quicksort(arr):
    """
    Função principal que inicia o QuickSort.
    """
    _quicksort(arr, 0, len(arr) - 1)

def _quicksort(arr, left, right):
    """
    Função recursiva do QuickSort.
    """
    if left < right:
        pi = partition(arr, left, right)
        _quicksort(arr, left, pi - 1)
        _quicksort(arr, pi + 1, right)

def partition(arr, left, right):
    """
    Particionamento usando Lomuto.
    """
    pivot = arr[right]
    i = left - 1

    for j in range(left, right):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    # coloca o pivô na posição correta
    arr[i + 1], arr[right] = arr[right], arr[i + 1]

    return i + 1


# teste
nums = [2, 0, 3, 1, 1, 0]
quicksort(nums)
print(nums)