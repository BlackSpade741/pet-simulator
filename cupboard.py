"""
Cupboard in PetSim.
Written by Ellen Yufei Chen (BlackSpade741) 2016-2017

"""

import items


class Cupboard:
    """
    A cupboard containing Items.
    """
    def __init__(self):
        """
        Initialize this cupboard object.
        """
        self.items = {}

    def __str__(self):
        """

        @return:
        @rtype:
        """
        pass

    def get(self, name):
        """ Return an Item object of name in self.items, if it exists.
        @param name:
        @type name:
        @return:
        @rtype:
        """
        pass

    def fill_cupboard(self, itms):
        """ Fill this cupboard with items from itms.

        @param itms:
        @rtype:
        """
        pass

    def use(self, name, pet):
        """ Use item with name. Might raise NoItemError.

        @param name:
        @param pet:
        @rtype:
        """
        pass

    def restock(self, name, quantity):
        """

        @param name:
        @param quantity:
        @rtype:
        """
        pass

    def add_item(self, name, attr, react, dur, num):
        """

        @param name:
        @type name:
        @param attr:
        @type attr:
        @param react:
        @type react:
        @param dur:
        @type dur:
        @param num:
        @type num:
        @return:
        @rtype:
        """
        pass




class NoItemError(Exception):
    """ Exception raise when a particular item doesn't exist.
    """
    pass
