from abaqusConstants import *
from .Leaf import Leaf


class LeafFromElementLabels(Leaf):

    """The LeafFromElementLabels object can be used whenever a Leaf object is expected as an 
    argument. Leaf objects are used to specify the items in a display group. Leaf objects 
    are constructed as temporary objects, which are then used as arguments to DisplayGroup 
    commands. 
    The LeafFromElementLabels object is derived from the Leaf object. 
    This page discusses: 

    Access
    ------
        - import displayGroupOdbToolset

    Table Data
    ----------

    Corresponding analysis keywords
    -------------------------------

    """

    # A SymbolicConstant specifying the leaf type. Possible values are EMPTY_LEAF, 
    # DEFAULT_MODEL, ALL_ELEMENTS, ALL_NODES, and ALL_SURFACES. 
    leafType: SymbolicConstant = None

    def __init__(self, partInstanceName: str, elementLabels: tuple):
        """This method creates a Leaf object from a sequence of element labels that belong to a
        single part instance.

        Path
        ----
            - LeafFromElementLabels

        Parameters
        ----------
        partInstanceName
            A String specifying the name of the part instance to which *elementLabels* refers. 
        elementLabels
            A sequence of Strings specifying expressions that denote element labels. The expression 
            can be any of the following:An Int specifying a single element label; for example, `1`.A 
            String specifying a single element label; for example, `'7'`.A String specifying a 
            sequence of element labels; for example, `'3:5'` and `'3:15:3'`. 

        Returns
        -------
            A LeafFromElementLabels object. 

        Exceptions
        ----------
            None. 
        """
        super().__init__()
        pass

