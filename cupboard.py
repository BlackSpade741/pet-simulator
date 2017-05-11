"""
Cupboard in PetSim.
Written by Ellen Yufei Chen (BlackSpade741) 2016-2017

"""

import constants
from items import Item


class Cupboard:
    """
    A cupboard containing Items.
    """
    def __init__(self):
        """ Initialize this cupboard object.
        """
        self.items = []

    def __iter__(self):
        """ Allows iteration over Cupboard, which is iteration over self.items
        """
        return self.items.__iter__()

    def get(self, name):
        """ Return an Item object of name in self.items, if it exists.
        @param name:
        @rtype:
        """
        for stage in self:
            for item in stage:
                if item.name == name:
                    return item

        raise NoItemError

    def fill_cupboard(self, itms):
        """ Fill this cupboard with items from itms.

        @param list[list[Item]] itms:
        @rtype:
        """
        for stage in range(len(itms)):
            self.items.append([])
            for item in itms[stage]:
                self.items[stage].append(item)

    def use(self, name, pet):
        """ Use item with name. Might raise NoItemError.

        @param name:
        @param pet:
        @rtype:
        """
        item = self.get(name)
        pet.use(item)

    def add_item(self, name, type_, attr, react, dur, stage):
        """ Add a new item to the cupboard, with {name} name, {attr} attributes,
        {react} reactions, and {dur} durability.

        @param Cupboard self: This cupboard
        @param str name: The name of the item to add
        @param str type_: The type of the item to add
        @param dict attr: The attributes of the item to add
        @param dict react: The reactions from each pet to the item to add
        @param int dur: The starting durability of the item to add
        @param int stage: The minimum stage a pet has to be in order to use the
        item to add
        @rtype: None
        """
        assert type(name) == str and type(attr) == dict and type(react) == dict\
            and type(dur) == int and type(type_) in constants.TYPES

        new_item = Item(name, type_, attr, react, dur)
        self.items[stage].append(new_item)

    def file_output(self):
        """

        @return:
        @rtype:
        """
        s = ''
        for i in range(len(self.items)):
            s += int(i), '\n'
            for item in self.items[i]:
                s += item.file_output()
            s += '\n'


class NoItemError(Exception):
    """ Exception raise when a particular item doesn't exist.
    """
    pass
