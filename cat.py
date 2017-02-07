from pet import Pet
from pet_status import PetStatus


class Cat(Pet):
    """ A Cat-type pet.

    === Attributes ===
    @type name: str
        The name of the Cat.
    @type gender: char
        The gender of the Cat
    @type stats: PetStatus
        The status of the Cat, containing level information and status information.
    @type evol_path: list of str
        The evolution pathway of all Cats.
    """
    evol_path = ['Kitten', 'Catling', 'Cat', 'Nekomo', 'Nekohito']

    def __init__(self, name, gender):
        """ Initialize the Cat.

        @type self: Cat
        @type name: str
            The name of the Cat.
        @rtype: None

        >>> cat = Cat('Bob', 'M')
        >>> cat.name
        'Bob'
        >>> cat.gender
        'M'
        >>> cat2 = Cat('Judy', 'F')
        >>> cat.name
        'Judy'
        >>> cat.gender
        'F'
        """

        super().__init__(name, gender)
        self.stats = PetStatus(self)

    def get_response_n(self, a):
        """ Return a neutral response to action a.

        @type self: Cat
        @type a: Action
            An action performed onto the cat.
        @rtype: str
        """

        if isinstance(a, Food):
            return '{} tasted the {} thoughtfully. '.format(self.name, a.name)
        if isinstance(a, Play):
            return '{} pawed at the {} thoughtfully. '.format(self.name, a.name)
        if isinstance(a, Washroom):
            return '{} cleaned with the {} thoughtfully. '.format(self.name,
                                                                  a.name)
        if isinstance(a, Rest):
            return '{} rested on the {} thoughtlessly. '.format(self.name,
                                                                a.name)

    def get_response_d(self, a):
        """ Return a disgust response to action a.

        @type self: Cat
        @type a: Action
            An action performed onto the cat.
        @rtype: str
        """

        if isinstance(a, Food):
            return '{} spat the {} out in an instant. '.format(self.name,
                                                               a.name)
        if isinstance(a, Play):
            return '{} touched the {}, but did not seem to want to play it. '.\
                format(self.name, a.name)
        if isinstance(a, Washroom):
            return '{} stayed away from the {} and did not want to get near it.\
             '.format(self.name, a.name)
        if isinstance(a, Rest):
            return '{} did not even want to see the {} and ran away. '.\
                format(self.name, a.name)

    def get_response_f(self, a):
        """ Return a favour response to action a.

        @type self: Cat
        @type a: Action
            An action performed onto the cat.
        @rtype: str
        """

        if isinstance(a, Food):
            return '{} buried {} whiskers into the bowl of {}, finished it, and\
            is meowing for more. '.format(self.name,
                                          self.pronouns['poss_lower'], a.name)
        if isinstance(a, Play):
            return "{} couldn't get {} paws off the {}. {} loved it. ".\
                format(self.name, self.pronouns['poss_lower'], a.name,
                       self.pronouns['subject_upper'])
        if isinstance(a, Washroom):
            return '{} washed {} thoroughly with the {} and meowed at the \
            comfort.'.format(self.name, self.pronouns['reflexive'], a.name)
        if isinstance(a, Rest):
            return '{} closed {} eyes and slept on the {} happily. '.\
                format(self.name, self.pronouns['reflexive'], a.name)

    def evolve(self):
        """ Evolve the Cat and return a message.

        @type self: Cat
        @rtype: str
        """

        new_lvl = self.stats.evolve()
        return 'A bright light fill the room... When the light subsides, you \
        see that {0} has evolved! {0} is now a {1}! '.format(self.name, self.
                                                             evol_path[new_lvl])

    def level_up(self):
        """ Level up the cat and return a message.

        @type self: Cat
        @rtype: str
        """

        new_lvl = self.stats.level_up()
        return '{0} has leveled up! {0} is now level {1}'.format(self.name,
                                                                 new_lvl)