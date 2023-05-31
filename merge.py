from multiprocessing import Process, Manager

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)

def merge(left, right):
    merged = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    while i < len(left):
        merged.append(left[i])
        i += 1

    while j < len(right):
        merged.append(right[j])
        j += 1

    return merged

def parallel_merge_sort(arr, shared_list):
    sorted_arr = merge_sort(arr)
    shared_list[:] = sorted_arr

if __name__ == '__main__':
    input_list = [64, 34, 25, 12, 22, 11, 90]

    with Manager() as manager:
        shared_list = manager.list(input_list)
        process_list = []

        merge_sort_process = Process(target=parallel_merge_sort, args=(shared_list, shared_list))
        merge_sort_process.start()
        process_list.append(merge_sort_process)

        for process in process_list:
            process.join()

        sorted_list = list(shared_list)
        print("Sorted list (Merge Sort):", sorted_list)
