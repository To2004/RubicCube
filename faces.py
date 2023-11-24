class faces (Cube):

    def __init__(self, cubearr):
        super().__init__(cubearr)
        self._L = cubearr[0:5]
        self._R = cubearr[6:11]
        self._U = cubearr[12:17]
        self._D = cubearr[18:23]
        self._B = cubearr[24:29]
        self._F= cubearr[30:35]

    @property
    def name(self):
        return self._name