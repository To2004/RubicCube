
    # try to do the arr like this cube_array =    [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
    #     [[10, 11, 12], [13, 14, 15], [16, 17, 18]],
    #     [[19, 20, 21], [22, 23, 24], [25, 26, 27]],
    #     [[28, 29, 30], [31, 32, 33], [34, 35, 36]],
    #     [[37, 38, 39], [40, 41, 42], [43, 44, 45]],
    #     [[46, 47, 48], [49, 50, 51], [52, 53, 54]] it will be easier to do class faces and action it is really good
class Cube:
        def __init__(self, cubetext):
            self.cubearr = []
            for i in range(0, len(cubetext), 6):
                self.cubearr.append(cubetext[i:i + 6])
            self.cubearr = []  # Initialize as an empty list
            for i in range(0, 6):
                self.cubearr.append(cubetext[i * 9:(i + 1) * 9])

        def get_cubearr(self):
            return self.cubearr






   # text = "w r g g r g o w o r r b y o r r o b o r r b y w w y g w o b b w w g g y w g g y b w o o y r b y y g o b b y"
    #stripped_text = "".join(text.split())
   # print(stripped_text)
    #my_cube = Cube(stripped_text)
    #my_cube.print_cube()