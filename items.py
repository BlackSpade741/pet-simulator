"""
Items in PetSim.
Written by Ellen Yufei Chen (BlackSpade741) 2016-2017.
"""

types = ['food', 'play', 'clean', 'rest']


class Item:
    """ An item in PetSim.

    === Attributes ===
    @type name: str
        The name of this Item.
    @type type: str
        The type of this Item.
    @type attributes: dict{str: int}
        The attribute changes with the usage of this Item.
    @type durability: int
        The durability of this Item. Decreases after being used.
    """

    def __init__(self, name, type, attributes, durability):
        """

        @type self: Item
            This Item.
        @type name: str
            The name of this Item.
        @type type: str
            The type of this Item.
            Precondition: type in types
        @type attributes: dict{str: int}
            The attribute changes with the usage of this Item.
        @type durability: int
            The starting durability of this Item.
            Precondition: durability > 0
        @rtype: None
        """
        assert type in types
        assert durability > 0

        self.name = name
        self.type = type
        self.attributes = attributes
        self.durability = durability
