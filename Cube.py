class Cube:
    # try to do the arr like this cube_array = [[[1, 2], [3, 4]], [[5, 6], [7, 8]], [[9, 10], [11, 12]]] it will be easier to do class faces
    def __init__(self, cubearr):
        self._cubearr = cubearr
    def cubearr(self, new_cubearr):
        # Add any validation logic if needed
        self._cubearr = new_cubearr
    @property
    def cubearr(self):
        return self._cubearr