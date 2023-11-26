from Algoritem import Algoritem
from Faces import Faces


class Action (Faces,Algoritem):
    def __init__(self, cubearr):
        # Call the constructor of the base class (Faces)
        super().__init__(cubearr)
    def F (self):
        # Add any validation logic if needed
        custom_cube=Algoritem.transform_cube_to_custom_shape(self.cubearr())
        copycubearr=self.cubearr()
        custom_cube[1][0], custom_cube[2][0], custom_cube[0][2], custom_cube[3][2] = (
            custom_cube[2][0], custom_cube[0][2], custom_cube[3][2], custom_cube[1][0]
        )

        copyrow=custom_cube[5][0]
        custom_cube[5][2]=copycubearr[5][0]
        copycubearr[5][2]= custom_cube[5][2]
        custom_cube[5][0]=copycubearr[5][2]
        copycubearr[5][0]=  copyrow




    def R(self):
        # Add any validation logic if needed

    def U(self):
        # Add any validation logic if needed

    def cubearr(self):
        # Add any validation logic if needed

    def cubearr(self):
        # Add any validation logic if needed

    def cubearr(self):
        # Add any validation logic if needed
