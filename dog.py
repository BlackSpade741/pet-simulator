from pet import Pet
from pet_status import PetStatus


class Dog(Pet):
    """ A Dog-type pet.

    === Attributes ===
    @type name: str
        The name of the Dog.
    @type gender: char
        The gender of the Dog
    @type stats: PetStatus
        The status of the Dog, containing level information and status
        information.
    @type evol_path: list of str
        The evolution pathway of all Dogs.
    """
    evol_path = ['Pupper', 'Dogling', 'Dog', 'Inumo', 'Inuhito']

    def __init__(self, name, gender):
        """ Initialize the Dog.

        @type self: Dog
        @type name: str
            The name of the Dog.
        @rtype: None

        >>> dog = Dog('Bob', 'M')
        >>> dog.name
        'Bob'
        >>> dog.gender
        'M'
        >>> dog2 = Dog('Judy', 'F')
        >>> dog2.name
        'Judy'
        >>> dog2.gender
        'F'
        """

        super().__init__(name, gender)
        self.stats = PetStatus(self)

    def get_response_n(self, a):
        """ Return a neutral response to action a.

        @type self: Dog
        @type a: Action
            An action performed onto the Dog.
        @rtype: str
        """

        if isinstance(a, Food):
            return '{} tasted the {} slobberily. '.format(self.name, a.name)
        if isinstance(a, Play):
            return '{} pawed at the {} slobberily. '.format(self.name, a.name)
        if isinstance(a, Washroom):
            return '{} cleaned with the {} slobberily. '.format(self.name,
                                                                  a.name)
        if isinstance(a, Rest):
            return '{} rested on the {} slobberily. '.format(self.name,
                                                                a.name)

    def get_response_d(self, a):
        """ Return a disgust response to action a.

        @type self: Dog
        @type a: Action
            An action performed onto the Dog.
        @rtype: str
        """

        if isinstance(a, Food):
            return "{} didn't seem to like the {}, but swallowed it anyway. ".\
                format(self.name, a.name)
        if isinstance(a, Play):
            return '{} touched the {}, but did not seem to want to play it. '.\
                format(self.name, a.name)
        if isinstance(a, Washroom):
            return '{} pawed at the {} disappointingly.'.format(self.name,
                                                                a.name)
        if isinstance(a, Rest):
            return '{} laid on the {}, then flopped up again, still excited. '.\
                format(self.name, a.name)

    def get_response_f(self, a):
        """ Return a favour response to action a.

        @type self: Dog
        @type a: Action
            An action performed onto the Dog.
        @rtype: str
        """

        if isinstance(a, Food):
            return '{} devoured the {} in an instant, and hastily pushed {} \
                   {} bowl up to you for more'.format(self.name,
                                                      self.pronouns['poss_'
                                                                    'lower'],
                                                      a.name)
        if isinstance(a, Play):
            return "{} couldn't get {} paws off the {}. {} loved it. ".\
                format(self.name, self.pronouns['poss_lower'], a.name,
                       self.pronouns['subject_upper'])
        if isinstance(a, Washroom):
            return '{} washed {} thoroughly with the {} and woofed at the \
            comfort.'.format(self.name, self.pronouns['reflexive'], a.name)
        if isinstance(a, Rest):
            return '{} closed {} eyes and slept on the {} happily. '.\
                format(self.name, self.pronouns['reflexive'], a.name)

    def evolve(self):
        """ Evolve the Dog and return a message.

        @type self: Dog
        @rtype: str
        """

        new_lvl = self.stats.evolve()
        return 'A bright light fill the room... When the light subsides, you \
        see that {0} has evolved! {0} is now a {1}! '.format(self.name, self.
                                                             evol_path[new_lvl])

    def level_up(self):
        """ Level up the Dog and return a message.

        @type self: Dog
        @rtype: str
        """

        new_lvl = self.stats.level_up()
        return '{0} has leveled up! {0} is now level {1}'.format(self.name,
                                                                 new_lvl)
