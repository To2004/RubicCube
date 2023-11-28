class Algoritem ():
    def transform_cube_to_custom_shape(cube_arr):
        """
        Transforms a 3x3 Rubik's Cube into a custom shape.

        Parameters:
        - cube_arr (list): A 3D list representing the initial Rubik's Cube.

        Returns:
        - list: A 3D list representing the transformed Rubik's Cube with the desired shape(up to down).
        """

        return [
            [
                [cube_arr[j][b][i] for b in range(3)] for i in range(3)
            ] for j in range(6)
        ]

    def spinrightmatrix(matrix):
        rotated_matrix = [list(row) for row in zip(*reversed(matrix))]
        return  rotated_matrix
    def spinleftmatrix(matrix):
        rotated_matrix = [list(row) for row in reversed(list(zip(*matrix)))]
        return  rotated_matrix

