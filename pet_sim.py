"""
Pet_Sim class for PetSim.
"""


from cupboard import Cupboard
from pets import Cat, Dog


class PetSim:
    """
    A pet simulator.
    """

    def __init__(self):
        """

        """
        self.pet = None
        self.cupboard = Cupboard()

    def init_pet(self, type_, name, gender):
        """

        @return:
        @rtype:
        """
        if type_.lower() == 'cat':
            self.pet = Cat(name, gender)
        else:
            self.pet = Dog(name, gender)

    def use(self, name):
        """ Use an item called name on self.pet.

        @param name:
        @type name:
        @return:
        @rtype:
        """

