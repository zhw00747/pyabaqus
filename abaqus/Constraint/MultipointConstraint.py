from abaqusConstants import *
from .Constraint import Constraint
from ..Region.Region import Region


class MultipointConstraint(Constraint):

    """The MultipointConstraint object defines a constraint between a group of 
    MultipointConstraint nodes located on a region and a reference point. 
    The MultipointConstraint object is derived from the Constraint object. 

    Access
    ------
        - import interaction
        - mdb.models[name].constraints[name]

    Table Data
    ----------

    Corresponding analysis keywords
    -------------------------------
        - MPC

    """

    # A Boolean specifying whether the constraint is suppressed or not. The default value is 
    # OFF. 
    suppressed: Boolean = OFF

    def __init__(self, name: str, surface: Region, controlPoint: Region, mpcType: SymbolicConstant, 
                 csys: str = None, userType: int = 0, userMode: SymbolicConstant = DOF_MODE_MPC):
        """This method creates a MultipointConstraint object.

        Path
        ----
            - mdb.models[name].MultipointConstraint

        Parameters
        ----------
        name
            A String specifying the constraint repository key. 
        surface
            A Region object specifying the surface on which the MultipointConstraint nodes are 
            located. 
        controlPoint
            A Region object specifying the constraint control point. 
        mpcType
            A SymbolicConstant specifying the MPC type of the constraint. Possible values are 
            BEAM_MPC, ELBOW_MPC, PIN_MPC, LINK_MPC, TIE_MPC, and USER_MPC. 
        csys
            None or a DatumCsys object specifying the initial orientation of the local coordinate 
            system for the MultipointConstraint's degrees of freedom. If *localCsys*=None, the 
            MultipointConstraint is defined in the global coordinate system. The default value is 
            None. 
        userType
            An Int specifying to differentiate between different constraint types in a user-defined 
            MultipointConstraint. The default value is 0.The *userType* argument applies only when 
            *mpcType*=USER_MPC. 
        userMode
            A SymbolicConstant specifying the mode of the constraint when it is user-defined. 
            Possible values are DOF_MODE_MPC and NODE_MODE_MPC. The default value is 
            DOF_MODE_MPC.The *userMode* argument applies only when *mpcType*=USER_MPC. 

        Returns
        -------
            A MultipointConstraint object. 

        Exceptions
        ----------
            None. 
        """
        super().__init__()
        pass

    def setValues(self, csys: str = None, userType: int = 0, userMode: SymbolicConstant = DOF_MODE_MPC):
        """This method modifies the MultipointConstraint object.

        Parameters
        ----------
        csys
            None or a DatumCsys object specifying the initial orientation of the local coordinate 
            system for the MultipointConstraint's degrees of freedom. If *localCsys*=None, the 
            MultipointConstraint is defined in the global coordinate system. The default value is 
            None. 
        userType
            An Int specifying to differentiate between different constraint types in a user-defined 
            MultipointConstraint. The default value is 0.The *userType* argument applies only when 
            *mpcType*=USER_MPC. 
        userMode
            A SymbolicConstant specifying the mode of the constraint when it is user-defined. 
            Possible values are DOF_MODE_MPC and NODE_MODE_MPC. The default value is 
            DOF_MODE_MPC.The *userMode* argument applies only when *mpcType*=USER_MPC. 

        Returns
        -------
            None. 

        Exceptions
        ----------
            None. 
        """
        pass

