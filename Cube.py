class Cube:
    # try to do the arr like this cube_array =    [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
    #     [[10, 11, 12], [13, 14, 15], [16, 17, 18]],
    #     [[19, 20, 21], [22, 23, 24], [25, 26, 27]],
    #     [[28, 29, 30], [31, 32, 33], [34, 35, 36]],
    #     [[37, 38, 39], [40, 41, 42], [43, 44, 45]],
    #     [[46, 47, 48], [49, 50, 51], [52, 53, 54]] it will be easier to do class faces and action it is really good
    def __init__(self, cubearr):
        self._cubearr = cubearr
    def cubearr(self, new_cubearr):
        # Add any validation logic if needed
        self._cubearr = new_cubearr
    @property
    def cubearr(self):
        return self._cubearr