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


c=transform_cube_to_custom_shape(cube_arr)
c=transform_cube_to_custom_shape(c)

print(c)
