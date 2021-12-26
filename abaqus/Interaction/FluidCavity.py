from abaqusConstants import *
from .Interaction import Interaction
from ..Region.Region import Region


class FluidCavity(Interaction):

    """The FluidCavity object defines a surface-based cavity. 
    The FluidCavity object is derived from the Interaction object. 

    Access
    ------
        - import interaction
        - mdb.models[name].interactions[name]

    Table Data
    ----------

    Corresponding analysis keywords
    -------------------------------
        - FLUID CAVITY

    """

    def __init__(self, name: str, createStepName: str, cavityPoint: Region, cavitySurface: Region, 
                 interactionProperty: str, ambientPressure: float = 0, thickness: float = 1, 
                 useAdiabatic: Boolean = OFF, checkNormals: Boolean = ON):
        """This method creates an FluidCavity object.

        Path
        ----
            - mdb.models[name].FluidCavity

        Parameters
        ----------
        name
            A String specifying the repository key. 
        createStepName
            A String specifying the name of the step in which the FluidCavity object is created. 
        cavityPoint
            A Region object specifying the fluid cavity reference point. 
        cavitySurface
            A Region object specifying the surface forming the boundary of the fluid cavity. 
        interactionProperty
            A String specifying the FluidCavityProperty object associated with this interaction. 
        ambientPressure
            A Float specifying the magnitude of the ambient pressure. The default value is 0.0. 
        thickness
            A Float specifying the out-of-plane thickness of the surface for two-dimensional models. 
            This argument is valid only when using two-dimensional models. The default value is 1.0. 
        useAdiabatic
            A Boolean specifying whether adiabatic behavior is assumed for the ideal gas. This 
            argument is valid only when *interactionProperty* specifies a pneumatic definition. The 
            default value is OFF. 
        checkNormals
            A Boolean specifying whether the analysis will check the consistency of the surface 
            normals. The default value is ON. 

        Returns
        -------
            A FluidCavity object. 

        Exceptions
        ----------
            None. 
        """
        super().__init__()
        pass

    def setValues(self, ambientPressure: float = 0, thickness: float = 1, useAdiabatic: Boolean = OFF, 
                  checkNormals: Boolean = ON):
        """This method modifies the FluidCavity object.

        Parameters
        ----------
        ambientPressure
            A Float specifying the magnitude of the ambient pressure. The default value is 0.0. 
        thickness
            A Float specifying the out-of-plane thickness of the surface for two-dimensional models. 
            This argument is valid only when using two-dimensional models. The default value is 1.0. 
        useAdiabatic
            A Boolean specifying whether adiabatic behavior is assumed for the ideal gas. This 
            argument is valid only when *interactionProperty* specifies a pneumatic definition. The 
            default value is OFF. 
        checkNormals
            A Boolean specifying whether the analysis will check the consistency of the surface 
            normals. The default value is ON. 

        Returns
        -------
            None. 

        Exceptions
        ----------
            None. 
        """
        pass

