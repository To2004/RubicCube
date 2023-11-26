from Cube import Cube


class Rows (Cube):

    def __init__(self, cubearr):
        # Call the constructor of the base class (Cube)
        super().__init__(cubearr)
        # I will edit this
        self._L = cubearr[0]
        self._R = cubearr[1]
        self._U = cubearr[2]
        self._D = cubearr[3]
        self._B = cubearr[4]
        self._F = cubearr[5]
