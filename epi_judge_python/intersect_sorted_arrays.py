from test_framework import generic_test


def intersect_two_sorted_arrays(A, B):
    # O (n) time O (N) space
    i_A = 0
    i_B = 0

    intersection = []
    while i_A < len(A) and i_B < len(B):
        if A[i_A] > B[i_B]:
            # increment B pointer

            i_B += 1
        elif A[i_A] < B[i_B]:
            # increment A pointer

            i_A += 1
        else:
            # values are equal to each other can use either A or B

            if A[i_A] not in intersection:
                intersection.append(A[i_A])

            # increment both counters
            i_A += 1
            i_B += 1

    return intersection


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("intersect_sorted_arrays.py",
                                       'intersect_sorted_arrays.tsv',
                                       intersect_two_sorted_arrays))
