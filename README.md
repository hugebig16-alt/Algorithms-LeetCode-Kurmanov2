def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        swapped = False

        # Проходим по неотсортированной части массива
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        # Если обменов не было, массив уже отсортирован
        if not swapped:
            break
