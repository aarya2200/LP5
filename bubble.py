from multiprocessing import Process, Manager

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def parallel_bubble_sort(arr, shared_list):
    bubble_sort(arr)
    shared_list[:] = arr

if __name__ == '__main__':
    input_list = [64, 34, 25, 12, 22, 11, 90]

    with Manager() as manager:
        shared_list = manager.list(input_list)
        process_list = []

        bubble_sort_process = Process(target=parallel_bubble_sort, args=(shared_list, shared_list))
        bubble_sort_process.start()
        process_list.append(bubble_sort_process)

        for process in process_list:
            process.join()

        sorted_list = list(shared_list)
        print("Sorted list (Bubble Sort):", sorted_list)
