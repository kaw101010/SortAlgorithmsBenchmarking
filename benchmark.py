import random
import timeit
from copy import deepcopy

def merge_sort(arr):
    """
    Sorts an array using the merge sort algorithm.
    The merge sort algorithm is a divide-and-conquer 
    algorithm that splits the array into two halves,
    recursively sorts each half, and then merges the 
    two sorted halves into a single sorted array.

    arr (list): The list of elements to be sorted.
    @return A new list containing all elements from 
            the input list, sorted in ascending order.
    """
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    """
    Merges two sorted lists into a single sorted list.
    
    left (list): The first sorted list.
    right (list): The second sorted list.
    @return A single sorted list containing 
            all elements from both input lists.
    """
    i, j = 0, 0
    result = []
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def insertion_sort(arr):
    """
    Sorts an array using the insertion sort algorithm.
    The insertion sort algorithm builds the final 
    sorted array one item at a time.
    
    arr (list): The list of elements to be sorted.
    @return The same list, sorted in ascending order.
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def benchmark_sorting(sizes, loops):
    """
    Benchmark Insertion Sort and Merge Sort on 
    arrays of various sizes using timeit.
    
    sizes: A list of input sizes to test.
    loops: Number of times to run each algorithm for averaging.
    @return: A list of (n, insertion_avg_time, merge_avg_time).
    """
    results = []
    for n in sizes:
        base_array = [random.randint(0, 1000000) for _ in range(n)]
        arr = deepcopy(base_array)

        # insertion sort test
        insert_time = timeit.timeit(
            stmt="insertion_sort(base_array)",
            setup="from __main__ import insertion_sort",
            globals={"insertion_sort": insertion_sort, "arr": base_array},
            number=loops
        ) / loops

        # merge sort test
        merge_time = timeit.timeit(
            stmt="merge_sort(arr)",
            setup="from __main__ import merge_sort",
            globals={"merge_sort": merge_sort, "arr": arr},
            number=loops
        ) / loops

        results.append((n, insert_time, merge_time))

    return results

if __name__ == "__main__":
    sizes = [10, 20, 50, 100, 200, 500, 1000, 2000, 5000]
    loops = 100
    timings = benchmark_sorting(sizes, loops)

    # Print the results
    for size, i_time, m_time in timings:
        print(f"n={size}, Insertion={i_time:.6}s, Merge={m_time:.6}s")
