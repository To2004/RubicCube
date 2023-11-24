class Cube:
    def __init__(self, cubearr):
        self._cubearr = cubearr
    def cubearr(self, new_cubearr):
        # Add any validation logic if needed
        self._cubearr = new_cubearr
    @property
    def cubearr(self):
        return self._cubearr