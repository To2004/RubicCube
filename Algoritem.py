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
        """
        Rotate the matrix to the right.

        Parameters:
        - matrix (list): The input matrix to be rotated.

        Returns:
        - list: The rotated matrix.
        """
        rotated_matrix = [list(row) for row in zip(*reversed(matrix))]
        return rotated_matrix

    def spinleftmatrix(matrix):
        """
        Rotate the matrix to the left.

        Parameters:
        - matrix (list): The input matrix to be rotated.

        Returns:
        - list: The rotated matrix.
        """
        rotated_matrix = [list(row) for row in reversed(list(zip(*matrix)))]
        return rotated_matrix
    def spin_backside_right(cube_arr,line):
        """
           Spin the backside of the cube to the right.

           Parameters:
           - cube_arr (list): The 2D array representing the cube.
           - line (int): The line to spin.

           Returns:
           - list: The modified cube array after the spin.
           """
        custom_cube = Algoritem.transform_cube_to_custom_shape(cube_arr)
        custom_cube[1][0+line], custom_cube[0][2-line], = (
            cube_arr[2][2-line], cube_arr[3][0+line]
        )

        copycubearr = Algoritem.transform_cube_to_custom_shape(custom_cube)
        copycubearr[2][2-line],  copycubearr[3][0+line], = (
            custom_cube[1][0 + line], custom_cube[0][2 - line]
        )
        return  copycubearr
    def spin_backside_left(cube_arr,line):
        """
           Spin the backside of the cube to the left.

           Parameters:
           - cube_arr (list): The 2D array representing the cube.
           - line (int): The line to spin.

           Returns:
           - list: The modified cube array after the spin.
           """
        custom_cube = Algoritem.transform_cube_to_custom_shape(cube_arr)
        custom_cube[0][2-line], custom_cube[1][0+line] = (
            cube_arr[2][2-line], cube_arr[3][0+line],
        )

        copycubearr = Algoritem.transform_cube_to_custom_shape(custom_cube)
        copycubearr[2][2-line],  copycubearr[3][0+line], = (
            custom_cube[1][0+line], custom_cube[0][2-line],
        )
        return copycubearr
    def spin_sideways_right(cube_arr,line):
        """
           Spin the cube sideways to the right.

           Parameters:
           - cube_arr (list): The 2D array representing the cube.
           - line (int): The line to spin.

           Returns:
           - list: The modified cube array after the spin.
           """
        cube_arr[0][0+line], cube_arr[1][0+line], cube_arr[5][0+line], cube_arr[4][0+line], = (
           cube_arr[4][0+line], cube_arr[5][0+line], cube_arr[0][0+line], cube_arr[1][0+line],
        )
        return  cube_arr


    def spin_sideways_left(cube_arr,line):
        """
            Spin the cube sideways to the left.

            Parameters:
            - cube_arr (list): The 2D array representing the cube.
            - line (int): The line to spin.

            Returns:
            - list: The modified cube array after the spin.
            """
        cube_arr[4][0+line], cube_arr[5][0+line], cube_arr[0][0+line], cube_arr[1][0+line], = (
            cube_arr[0][0+line], cube_arr[1][0+line], cube_arr[5][0+line], cube_arr[4][0+line],
        )
        return cube_arr