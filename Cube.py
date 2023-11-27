
    # try to do the arr like this cube_array =    [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
    #     [[10, 11, 12], [13, 14, 15], [16, 17, 18]],
    #     [[19, 20, 21], [22, 23, 24], [25, 26, 27]],
    #     [[28, 29, 30], [31, 32, 33], [34, 35, 36]],
    #     [[37, 38, 39], [40, 41, 42], [43, 44, 45]],
    #     [[46, 47, 48], [49, 50, 51], [52, 53, 54]] it will be easier to do class faces and action it is really good
class Cube:
    def __init__(self, cubetext):
        rows = 6
        cols = 3
        depth = 3

        self.cubearr = [[[cubetext[i * cols * depth + j * depth + k] for k in range(depth)]
                         for j in range(cols)]
                        for i in range(rows)]

    def get_cubearr(self):
        return self.cubearr

    def print_cube(self):
        for layer in self.cubearr:
            for row in layer:
                print(row)
            print()

# Input text
text = "w r g g r g o w o r r b y o r r o b o r r b y w w y g w o b b w w g g y w g g y b w o o y r b y y g o b b y"

# Remove spaces from the input text
stripped_text = "".join(text.split())

# Create an instance of the Cube class
my_cube = Cube(stripped_text)

# Print the cube array
my_cube.print_cube()