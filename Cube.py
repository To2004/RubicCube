

class Cube:
    def __init__(self, cubetext):
        rows = 6
        cols = 3
        depth = 3
        cubetext = "".join( cubetext.split())

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


# Create an instance of the Cube class
my_cube = Cube(text)

# Print the cube array
my_cube.print_cube()