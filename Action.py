import copy

from Algoritem import Algoritem
from Faces import Faces


class Action (Faces,Algoritem):
    def __init__(self, cubearr):
        # Call the constructor of the base class (Faces)
        super().__init__(cubearr)
    def F (self,line):
        # Add any validation logic if needed
        cubearr= Algoritem.spin_backside_right(copy.deepcopy(self.cubearr),line)
        if line!=1:
            cubearr[5 - line // 2]=Algoritem.spinrightmatrix( copy.deepcopy(  cubearr[5 - line // 2]))

        self.cubearr=cubearr

    def Fleft (self,line):
        # Add any validation logic if needed
        cubearr= Algoritem. spin_backside_left(copy.deepcopy(self.cubearr),line)
        if line!=1:
            cubearr[5 - line // 2]=Algoritem.spinleftmatrix( copy.deepcopy(cubearr[5 - line // 2]))

        self.cubearr=cubearr

    def U(self, line):
        # Add any validation logic if needed
        cubearr = Algoritem.spin_sideways_right(copy.deepcopy(self.cubearr), line)
        if line != 1:
            cubearr[2 + line // 2] = Algoritem.spinrightmatrix(copy.deepcopy(cubearr[2 + line // 2]))

        self.cubearr = cubearr

    def Uleft(self, line):
        # Add any validation logic if needed
        cubearr = Algoritem.spin_sideways_left(copy.deepcopy(self.cubearr), line)
        if line != 1:
            cubearr[2 + line // 2] = Algoritem.spinleftmatrix(copy.deepcopy(cubearr[2 + line // 2]))

        self.cubearr = cubearr

    def D(self, line):
        # Add any validation logic if needed
      Action.U(line)

    def Dleft(self, line):
        # Add any validation logic if needed
        Action.Uleft(line)

    #def R(self):
            # Add any validation logic if needed


