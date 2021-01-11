from typing import List

def dutch_flag_partition(pivot_index: int, A: List[int]) -> None:
    pivot = A[pivot_index]

    # Two pass implementation:
    # next_idx = 0
    # for i in range(len(A)):
    #     if A[i] < pivot:
    #         A[next_idx], A[i] = A[i], A[next_idx]
    #         next_idx += 1
    # 
    # next_idx = -1
    # for i in range(len(A) - 1, -1, -1):
    #     if A[i] < pivot:
    #         break
    #     elif A[i] > pivot:
    #         A[next_idx], A[i] = A[i], A[next_idx]
    #         next_idx -= 1

    # Single pass implementation
    lt_idx = 0
    gt_idx = len(A)
    curr_idx = 0

    while curr_idx < gt_idx:
        if A[curr_idx] < pivot:
            A[lt_idx], A[curr_idx] = A[curr_idx], A[lt_idx]
            lt_idx += 1
            curr_idx += 1
        elif A[curr_idx] == pivot:
            curr_idx += 1
        else:
            gt_idx -= 1
            A[gt_idx], A[curr_idx] = A[curr_idx], A[gt_idx]
