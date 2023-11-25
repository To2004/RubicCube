class Rows (Cube):

    def __init__(self, cubearr):
        # Call the constructor of the base class (Cube)
        super().__init__(cubearr)

        # Assuming cubearr is a 3D array, you might want to initialize faces based on the structure
        self._U = cubearr[0]
        self._L = cubearr[1]
        self._F = cubearr[2]
        self._R = cubearr[3]
        self._B = cubearr[4]
        self._D = cubearr[5]
