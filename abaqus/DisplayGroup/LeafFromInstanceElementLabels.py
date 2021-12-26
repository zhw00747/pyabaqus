from abaqusConstants import *
from .Leaf import Leaf


class LeafFromInstanceElementLabels(Leaf):

    """The LeafFromInstanceElementLabels object can be used whenever a Leaf object is expected 
    as an argument. Leaf objects are used to specify the items in a display group. Leaf 
    objects are constructed as temporary objects, which are then used as arguments to 
    DisplayGroup commands. 
    The LeafFromInstanceElementLabels object is derived from the Leaf object. 

    Access
    ------
        - import displayGroupMdbToolset

    Table Data
    ----------

    Corresponding analysis keywords
    -------------------------------

    """

    # A SymbolicConstant specifying the leaf type. Possible values are EMPTY_LEAF, 
    # DEFAULT_MODEL, ALL_ELEMENTS, ALL_NODES, and ALL_SURFACES. 
    leafType: SymbolicConstant = None

    def __init__(self, elementLabels: tuple):
        """This method creates a Leaf object from a sequence of Strings specifying the element
        labels. Leaf objects specify the items in a display group.

        Path
        ----
            - LeafFromInstanceElementLabels

        Parameters
        ----------
        elementLabels
            A sequence of sequences specifying element labels. Each inner sequence consists of a 
            PartInstance object followed by a sequence of Strings specifying element labels. 

        Returns
        -------
            A LeafFromInstanceElementLabels object. 

        Exceptions
        ----------
            None. 
        """
        super().__init__()
        pass

