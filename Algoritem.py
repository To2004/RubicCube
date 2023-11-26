class Algoritem ():
def transform_cube_to_custom_shape(cube_arr):
    return [
        [
            [cube_arr[j][b][i] for b in range(3)] for i in range(3)
        ] for j in range(6)
    ]