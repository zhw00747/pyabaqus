from abaqusConstants import *
from .BoundaryConditionState import BoundaryConditionState


class TemperatureBCState(BoundaryConditionState):

    """The TemperatureBCState object stores the propagating data for a temperature boundary 
    condition in a step. One instance of this object is created internally by the 
    TemperatureBC object for each step. The instance is also deleted internally by the 
    TemperatureBC object. 
    The TemperatureBCState object has no constructor or methods. 
    The TemperatureBCState object is derived from the BoundaryConditionState object. 

    Access
    ------
        - import load
        - mdb.models[name].steps[name].boundaryConditionStates[name]

    Table Data
    ----------

    Corresponding analysis keywords
    -------------------------------
        - BOUNDARY

    """

    # A Float specifying the temperature magnitude. 
    magnitude: float = None

    # A SymbolicConstant specifying the propagation state of the temperature magnitude. 
    # Possible values are UNSET, SET, UNCHANGED, FREED, and MODIFIED. 
    magnitudeState: SymbolicConstant = None

    # A SymbolicConstant specifying the propagation state of the *dof* member. Possible values 
    # are SET and UNCHANGED. 
    dofState: SymbolicConstant = None

    # A tuple of Ints specifying the degrees of freedom to which the boundary condition is 
    # applied. 
    dof: int = None

    # A SymbolicConstant specifying the propagation state of the amplitude reference. Possible 
    # values are UNSET, SET, UNCHANGED, FREED, and MODIFIED. 
    amplitudeState: SymbolicConstant = None

    # A SymbolicConstant specifying the propagation state of the BoundaryConditionState 
    # object. Possible values 
    # are:NOT_YET_ACTIVECREATEDPROPAGATEDMODIFIEDDEACTIVATEDNO_LONGER_ACTIVETYPE_NOT_APPLICABLEINSTANCE_NOT_APPLICABLEPROPAGATED_FROM_BASE_STATEMODIFIED_FROM_BASE_STATEDEACTIVATED_FROM_BASE_STATEBUILT_INTO_MODES 
    status: SymbolicConstant = None

    # A String specifying the name of the amplitude reference. The String is empty if the 
    # boundary condition has no amplitude reference. 
    amplitude: str = ''

