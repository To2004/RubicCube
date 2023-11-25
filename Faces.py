from Cube import Cube


class Faces (Cube):

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

    @property
    def left_face(self):
        return self._L

    @left_face.setter
    def left_face(self, new_left_face):
        # Add any validation logic if needed
        self._L = new_left_face

    @property
    def right_face(self):
        return self._R

    @right_face.setter
    def right_face(self, new_right_face):
        # Add any validation logic if needed
        self._R = new_right_face

    @property
    def upper_face(self):
        return self._U

    @upper_face.setter
    def upper_face(self, new_upper_face):
        # Add any validation logic if needed
        self._U = new_upper_face

    @property
    def lower_face(self):
        return self._D

    @lower_face.setter
    def lower_face(self, new_lower_face):
        # Add any validation logic if needed
        self._D = new_lower_face

    @property
    def back_face(self):
        return self._B

    @back_face.setter
    def back_face(self, new_back_face):
        # Add any validation logic if needed
        self._B = new_back_face

    @property
    def front_face(self):
        return self._F

    @front_face.setter
    def front_face(self, new_front_face):
        # Add any validation logic if needed
        self._F = new_front_face