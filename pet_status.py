"""
A pet's status in PetSim.
Written by Ellen Yufei Chen (BlackSpade741) 2016-2017
"""

import pets
import constants


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
    @type attr: dict{str: int}
        The attributes of the pet. Includes hunger, fun, clean, and stamina.
    """

    def __init__(self, pet):
        """

        @type pet: pets.Pet

        """
        self.pet = pet
        self.exp = 0
        self.level = 0
        if isinstance(pet, pets.Cat):
            self.stage = constants.EVOL_PATH['cat']
            self.attr = constants.MAX_ATTR['cat'].copy()
        elif isinstance(pet, pets.Dog):
            self.stage = constants.EVOL_PATH['dog']
            self.attr = constants.MAX_ATTR['dog'].copy()

    def use(self, item):
        """ Apply Item a to self.pet.

        @type item: Item
        """
        change = item.use(self.pet)

        for key in constants.TYPES:
            self.attr[key] += change[key]

    def evolve(self):
        """

        @rtype:
        """
        pass

    def level_up(self):
        """

        @rtype:
        """
        pass
