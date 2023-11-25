class Cube:
    def __init__(self, cubetext):
        self.cubearr = []  # Initialize as an empty list
        for i in range(0, 6):
            self.cubearr.append(cubetext[i * 9:(i + 1) * 9])

    def get_cubearr(self):
        return self.cubearr

    def print_cube(self):
        for item in self.get_cubearr():
            print(item)

        print(len(self.get_cubearr()))

text = "w r g g r g o w o r r b y o r r o b o r r b y w w y g w o b b w w g g y w g g y b w o o y r b y y g o b b y"
stripped_text = "".join(text.split())
my_cube = Cube(stripped_text)
my_cube.print_cube()