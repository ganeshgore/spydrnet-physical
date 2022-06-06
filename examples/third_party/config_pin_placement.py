"""
"""
import numpy as np
import pandas as pd
import create_config_chain_eco as eco

TOTAL_WL = 10
TOTAL_BL = 10


def get_first_neighbour(matrix, index):
    '''
    '''
    padded_matrix = np.pad(matrix, [(1, 1), (1, 1)],
                           mode='constant', constant_values=0)
    index = index[0]+1, index[1]+1
    value = sum(padded_matrix[index[0]-1][index[1]-1:index[0]+2]) + \
        sum(padded_matrix[index[0]+0][index[1]-1:index[0]+2]) + \
        sum(padded_matrix[index[0]+1][index[1]-1:index[0]+2])
    return value-padded_matrix[index[0]][index[1]]


def get_second_neighbour(matrix, index):
    '''
    '''
    padded_matrix = np.pad(matrix, [(2, 2), (2, 2)],
                           mode='constant', constant_values=0)
    indx = index[0]+2, index[1]+2
    value = \
        sum(padded_matrix[indx[0]-2][indx[1]-2:indx[0]+3]) + \
        sum(padded_matrix[indx[0]-1][indx[1]-2:indx[0]+3]) + \
        sum(padded_matrix[indx[0]+0][indx[1]-2:indx[0]+3]) + \
        sum(padded_matrix[indx[0]+1][indx[1]-2:indx[0]+3]) + \
        sum(padded_matrix[indx[0]+2][indx[1]-2:indx[0]+3])
    return value - get_first_neighbour(matrix, index) - \
        padded_matrix[indx[0]][indx[1]]


def cost_function(matrix, wl_lines, bl_lines):
    matrix = matrix.copy()
    capacity = wl_lines*bl_lines
    difference = capacity-matrix
    for idx, value in np.ndenumerate(difference):
        if value < 0:
            # Check first neighbour
            l1_capacity = get_first_neighbour(matrix, idx)
            l2_capacity = get_second_neighbour(matrix, idx)
            print(value, l1_capacity, l2_capacity)

            matrix[idx[0]][idx[1]] = ((value-l1_capacity-l2_capacity)*10) + \
                min(abs(value), l1_capacity)*2 + \
                min(abs(value)-l1_capacity, l2_capacity+l1_capacity)*8
    return sum(sum(abs(difference)))


def main():
    '''
    Main Function
    '''
    grid = np.array([[4, 4, 4, 4, 4],
                     [4, 4, 4, 4, 4],
                     [4, 4, 4, 4, 4],
                     [4, 4, 4, 4, 4],
                     [4, 4, 4, 4, 4]], np.int8)
    wl_lines = np.array([[1, 2, 3, 1, 2]]).T
    bl_lines = [3, 2, 1, 4, 1]

    capacity = wl_lines*bl_lines
    print(capacity)
    #  3  2  1  4  1
    #  6  4  2  8  2
    #  9  6  3 12  3
    #  3  2  1  4  1
    #  6  4  2  8  2
    assert get_first_neighbour(capacity, (2, 2)) == (4+2+8+6+12+2+1+4), \
        "First neighbour calculation wrong"
    assert get_second_neighbour(capacity, (2, 2)) == (3+2+1+4+1+6+4+2+8+2+6+9+3+2+3+1), \
        "Second neighbour calculation wrong"

    # =====================
    # ======  Case 0 ======
    # =====================
    wl_lines = np.array([[2, 2, 3, 2, 2]]).T
    bl_lines = [3, 2, 2, 4, 2]
    capacity = wl_lines*bl_lines
    print(capacity-grid)
    # 2 0 0 4 0
    # 2 0 0 4 0
    # 5 2 2 8 2
    # 2 0 0 4 0
    # 2 0 0 4 0
    assert cost_function(grid, wl_lines, bl_lines) == 43, \
        "Wrong cost funcion calculation"

    # =====================
    # ======  Case 1 ======
    # =====================
    grid = np.array([[4, 4, 4, 4, 4],
                     [4, 4, 4, 4, 4],
                     [4, 4, 8, 4, 4],
                     [4, 4, 4, 4, 4],
                     [4, 4, 4, 4, 4]], np.int8)
    print(capacity-grid)
    #  2  0  0  4  0
    #  2  0  0  4  0
    #  5  2 -2  8  2
    #  2  0  0  4  0
    #  2  0  0  4  0
    assert cost_function(grid, wl_lines, bl_lines) == 43, \
        "Wrong cost funcion calculation"


if __name__ == "__main__":
    main()
