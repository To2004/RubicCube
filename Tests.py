import copy

cube_arr = [
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
    [[10, 11, 12], [13, 14, 15], [16, 17, 18]],
    [[19, 20, 21], [22, 23, 24], [25, 26, 27]],
    [[28, 29, 30], [31, 32, 33], [34, 35, 36]],
    [[37, 38, 39], [40, 41, 42], [43, 44, 45]],
    [[46, 47, 48], [49, 50, 51], [52, 53, 54]]
]




def transform_cube_to_custom_shape(cube_arr):
    return [
        [
            [cube_arr[j][b][i] for b in range(3)] for i in range(3)
        ] for j in range(6)
    ]
def F (cube_arr):
        # Add any validation logic if needed
        custom_cube=transform_cube_to_custom_shape(cube_arr)
        copycubearr=copy.deepcopy(cube_arr)
        custom_cube[1][0], custom_cube[2][0], custom_cube[0][2], custom_cube[3][2] = (
            custom_cube[2][0], custom_cube[0][2], custom_cube[3][2], custom_cube[1][0]
        )

        copyrow=custom_cube[5][0]
        copyrow2 = custom_cube[5][2]
        custom_cube[5][2] = copycubearr[5][0]
        custom_cube[5][0] = copycubearr[5][2]
        copycubearr=transform_cube_to_custom_shape(custom_cube)
        copycubearr[5][2] =  copyrow2
        copycubearr[5][0] =  copyrow
        cubearr=copycubearr
        print( cubearr)


def rotate_front_clockwise(cube_arr):
    # Perform a 90-degree clockwise rotation of the front face
    rotated_face = list(zip(*reversed(cube_arr[1])))
    cube_arr[1] = rotated_face


F(cube_arr)
rotate_front_clockwise(cube_arr)
print(cube_arr)