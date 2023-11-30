import copy

from Algoritem import Algoritem
from Faces import Faces


class Action (Faces,Algoritem):
    def __init__(self, cubearr):
        # Call the constructor of the base class (Faces)
        super().__init__(cubearr)
    def F (self,line):
        # Add any validation logic if needed
        cubearr= Algoritem.spin_somthing_right(copy.deepcopy(self.cubearr),line)
        if line!=1:
            cubearr[5 - line // 2]=Algoritem.spinrightmatrix( copy.deepcopy(  cubearr[5 - line // 2]))

        self.cubearr=cubearr

    def Fleft (self,line):
        # Add any validation logic if needed
        cubearr= Algoritem.spin_somthing_left(copy.deepcopy(self.cubearr),line)
        if line!=1:
            cubearr[5 - line // 2]=Algoritem.spinleftmatrix( copy.deepcopy(cubearr[5 - line // 2]))

        self.cubearr=cubearr

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
