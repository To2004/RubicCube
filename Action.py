import copy

from Algoritem import Algoritem
from Faces import Faces


class Action (Faces,Algoritem):
    def __init__(self, cubearr):
        # Call the constructor of the base class (Faces)
        super().__init__(cubearr)
    def F (self):
        # Add any validation logic if needed
        custom_cube=Algoritem.transform_cube_to_custom_shape(self.cubearr())
        copycubearr=copy.deepcopy(self.cubearr())
        custom_cube[1][0], custom_cube[2][0], custom_cube[0][2], custom_cube[3][2] = (
            custom_cube[2][0], custom_cube[0][2], custom_cube[3][2], custom_cube[1][0]
        )

        copyrow=custom_cube[5][0]
        copyrow2 = custom_cube[5][2]
        custom_cube[5][2] = copycubearr[5][0]
        custom_cube[5][0] = copycubearr[5][2]
        copycubearr=Algoritem.transform_cube_to_custom_shape(custom_cube)
        copycubearr[5][2] =  copyrow2
        copycubearr[5][0] =  copyrow
        self.cubearr=copycubearr
        print( self.cubearr)





    #def R(self):
            # Add any validation logic if needed

    #def U(self):
            # Add any validation logic if needed

    #def cubearr(self):
            # Add any validation logic if needed

    #def cubearr(self):
            # Add any validation logic if needed

    #def cubearr(self):
            # Add any validation logic if needed
