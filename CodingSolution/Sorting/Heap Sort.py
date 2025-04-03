# Space -> o(1) || Time -> O(nlog(n))

def heapSort(array):
    array = build_max_heap(array)
    right = len(array) - 1
    while right > 0:
        array[0], array[right] = array[right], array[0]
        max_heapify(array, right, 0)
        right -= 1
    
    return array
    
def max_heapify(array, heap_size, i):
    left = 2 * i
    right = 2 * i + 1
    largest = i
    
    if left < heap_size and array[left] > array[i]:
        largest = left
    if right < heap_size and array[right] > array[largest]:
        largest = right
    if largest != i:
        array[i], array[largest] = array[largest], array[i]
        max_heapify(array, heap_size, largest)

def build_max_heap(array):
    heap_size = len(array)
    for i in range(heap_size // 2, -1, -1):
        # print(array[i])
        max_heapify(array, heap_size, i)
    return array
    
    