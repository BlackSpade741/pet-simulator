"""
Items in PetSim.
Written by Ellen Yufei Chen (BlackSpade741) 2016-2017.
"""

import constants


class Item:
    """ An item in PetSim.

    === Attributes ===
    @type name: str
        The name of this Item.
    @type type_: str
        The type of this Item.
    @type attributes: dict{str: int}
        The attribute changes with the usage of this Item.
    @type pet_reaction: dict{str: char}
        The reaction of each kind of pet to this Item.
    @type durability: int
        The durability of this Item. Decreases after being used.
    """

    def __init__(self, name, type_, attributes, pet_reaction, durability):
        """

        @type self: Item
            This Item.
        @type name: str
            The name of this Item.
        @type type_: str
            The type of this Item.
            Precondition: type in types
        @type attributes: dict{str: int}
            The attribute changes with the usage of this Item.
        @type pet_reaction: dict{str: float}
            The reaction of each kind of pet to this Item, in the form of a
            decimal multiplier to attributes.
        @type durability: int
            The starting durability of this Item.
            Precondition: durability > 0
        """
        assert type in constants.TYPES
        assert durability > 0

        self.name = name
        self.type_ = type_
        self.attributes = attributes
        self.pet_reaction = pet_reaction
        self.durability = durability
        self._or_durability = durability

    def get_reaction(self, pet):
        """ Return whether pet will react in favour, dislike, or neutral to this
        item.

        @type pet: Pet
        @rtype: char
        """
        return self.pet_reaction[pet.get_type()]

    def use(self, pet):
        """ Return the appropriate pet attribute changes that this Item has
        on pet, and decrease durability by 1.

        @type self: Item
        @type pet: Pet
        @rtype: dict{str: int}
        """
        keys = constants.TYPES
        react = self.get_reaction(pet)
        self.durability -= 1

        return {key: int(self.attributes[key] * constants.REACTION_MULT[react])
                for key in keys}

    def file_output(self):
        """ Return a string version of self for file i/o.

        format:
        name, type, durability
        hunger_value, food_value, clean_value, stamina_value
        dog_reaction, cat_reaction

        @rtype: str
        """
        s = '{0}, {1}, {2} \n'.format(self.name, self.type_, self.durability)
        s += '{0}, {1}, {2}, {3} \n'.format(self.attributes['hunger'],
                                            self.attributes['food'],
                                            self.attributes['clean'],
                                            self.attributes['stamina'])
        s += '{0}, {1} \n'.format(self.pet_reaction['dog'],
                                  self.pet_reaction['cat'])
        return s
