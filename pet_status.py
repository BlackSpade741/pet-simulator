"""
A pet's status in PetSim.
Written by Ellen Yufei Chen (BlackSpade741) 2016-2017
"""

import pets


class PetStatus:
    """ A class containing the status of a Pet.

    === Attributes ===
    @type pet: pets.Pet
        The Pet this PetStatus is of.
    @type exp: int
        The experience the Pet has.
    @type level: int
        The level the Pet is at.
    @type stage: str
        The stage the Pet is at.
    @type hunger: int
        The hunger level of the Pet.
    @type stamina: int
        The stamina level of the Pet.
    @type clean: int
        The cleanliness level of the Pet.
    @type fun: int
        The fun level of the Pet.
    """

    def __init__(self, pet):
        """

        @type pet: pets.Pet

        """
        self.pet = pet

    def stat_change_n(self, a):
        """

        @type a: Item
        """
        pass

    def stat_change_d(self, a):
        """
        @type a: Item
        """
        pass

    def stat_change_f(self, a):
        """

        @type a: Item
        """
        pass

    def evolve(self):
        """

        @rtype:
        """
        pass

    def level_up(self):
        """

        @return:
        @rtype:
        """
        pass
