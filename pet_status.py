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
    @type exp_cap: int
        The experience cap at the current level.
    @type level: int
        The level the Pet is at.
    @type stage: int
        The stage the Pet is at.
    @type attr: dict{str: int}
        The attributes of the pet. Includes hunger, fun, clean, and stamina.
    """

    def __init__(self, pet):
        """ Initialize this PetStatus.

        @type self: PetStatus
        @type pet: pets.Pet

        """
        self.pet = pet
        self.exp = 0
        self.exp_cap = constants.EXP_START_CAP
        self.level = 0
        self.stage = 0
        if isinstance(pet, pets.Cat):
            self.attr = constants.MAX_ATTR['cat'].copy()
        elif isinstance(pet, pets.Dog):
            self.attr = constants.MAX_ATTR['dog'].copy()

    def use(self, item):
        """ Apply Item a to self.pet.

        @type self: PetStatus
        @type item: Item
        @rtype: None
        """
        change = item.use(self.pet)

        for key in constants.TYPES:
            self.attr[key] += change[key]

    def evolve(self):
        """ Evolve a pet, returning the new stage.

        @type self: PetStatus
        @rtype: int
        """
        assert self.check_evolve()
        self.stage += 1
        return self.stage

    def level_up(self):
        """ Level up a pet, returning the new level.

        @type self: PetStatus
        @rtype: int
        """
        assert self.check_level_up()
        self.level += 1
        self.exp = 0
        self.exp_cap **= constants.EXP_MULTIPLIER

    def check_level_up(self):
        """ Return whether this pet has reached the level cap or not.

        @type self: PetStatus
        @rtype: bool
        """
        return self.exp >= self.exp_cap

    def check_evolve(self):
        """ Return whether this pet is ready to evolve or not.

        @type self: PetStatus
        @rtype: bool
        """
        return self.level in constants.EVOL_LEVELS
