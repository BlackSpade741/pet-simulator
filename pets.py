"""
Pets in PetSim.
Written by Ellen Yufei Chen (BlackSpade741) 2016-2017
"""

from pet_status import PetStatus


class Pet:
    """ A pet from PetSim.

    === Attributes ===
    @type name: str
        The name of the pet.
    @type gender: char
        The gender of the pet. 'M' is male, and 'F' is female.
        Precondition: gender == 'M' or gender == 'F'
    @type stats: PetStatus
        The status of the pet, includes exp, level, stage, and status levels.

    """
    # === Private Attributes ===
    # @type pronouns: dict{str: str}
    # The pronouns of a pet, given the gender. The keys of the dictionary are
    # the type of pronouns, and the values the corresponding pronouns.

    def __init__(self, name, gender):
        """Initialize this Pet

        @type self: Pet
        @type name: str
            The name of this Pet.
        @type gender: char
            The gender of this Pet. 'M' is male, 'F' is female, and 'N' is
            neutral.
            Precondition: gender == 'M' or gender == 'F' or gender == 'N'
        @rtype: None

        >>> cat = Pet('boo', 'F')
        >>> cat.name
        'boo'
        >>> cat.gender
        'F'
        >>> dog = Pet('Fido', 'M')
        >>> dog.name
        'Fido'
        >>> dog.gender
        'M'
        """

        self.name = name
        self.gender = gender
        self.stats = None

        if gender == 'M':
            self.pronouns = {'subject_upper': 'He', 'object': 'him',
                             'poss_upper': 'His',
                             'poss_lower': 'his', 'subject_lower': 'he',
                             'reflexive': 'himself'}
        elif gender == 'F':
            self.pronouns = {'subject_upper': 'She', 'object': 'her',
                             'poss_upper': 'Her',
                             'poss_lower': 'her', 'subject_lower': 'she',
                             'poss_noun_lower': 'hers',
                             'poss_noun_upper': 'Hers', 'reflexive': 'herself'}
        elif gender == 'N':
            self.pronouns = {'subject_upper': 'They', 'object': 'them',
                             'poss_upper': 'Their', 'poss_lower': 'their',
                             'subject_lower': 'they',
                             'poss_noun_lower': 'theirs',
                             'poss_noun_upper': 'Theirs',
                             'reflexive': 'themselves'}

    def act(self, a):
        """Return the outcome of a on Pet.

        @type self: Pet
        @type a: Action
            An action to be done on the pet.
        @rtype: str
            A string describing the outcome of a.
        """

        reaction = a.type_to_reaction[str(type(self))]
        response = ''

        if reaction == 'n':
            response = self.get_response_n(a) + self.stats.stat_change_n(a)
        elif reaction == 'd':
            response = self.get_response_d(a) + self.stats.stat_change_d(a)
        elif reaction == 'f':
            response = self.get_response_f(a) + self.stats.stat_change_f(a)

        return response

    def get_response_n(self, a):
        """ Returns a neutral response of the pet to Action a.

        @type self: Pet
        @type a: Action
            An action done on the pet.
        @rtype: str
            A string describing a response to a.
        """

        raise NotImplementedError("Cannot use Pet instance!"
                                  "Please use a subclass instance.")

    def get_response_d(self, a):
        """ Returns a disgust response of the pet to Action a.

        @type self: Pet
        @type a: Action
            An action done on the pet.
        @rtype: str
            A string describing a response to a.
        """
        raise NotImplementedError("Cannot use Pet instance!"
                                  "Please use a subclass instance.")

    def get_response_f(self, a):
        """ Returns a favoured response of the pet to Action a.

        @type self: Pet
        @type a: Action
            An action done on the pet.
        @rtype: str
            A string describing a response to a.
        """
        raise NotImplementedError("Cannot use Pet instance!"
                                  "Please use a subclass instance.")

    def evolve(self):
        """ Evolve the pet to the next stage and return a message.

        @type self: Pet
        @rtype: str
        """
        raise NotImplementedError("Cannot use Pet instance!"
                                  "Please use a subclass instance.")

    def level_up(self):
        """ Level up the pet, and return a message.

        @type self: Pet
        @rtype: str
        """
        raise NotImplementedError("Cannot use Pet instance!"
                                  "Please use a subclass instance.")


class Cat(Pet):
    """ A Cat-type pet.

    === Attributes ===
    @type name: str
        The name of the Cat.
    @type gender: char
        The gender of the Cat
    @type stats: PetStatus
        The status of the Cat, containing level information and status
        information.
    @type EVOL_PATH: list of str
        The evolution pathway of all Cats.
    @type MAX_ATTR: dict{str: int}
        The maximum level of attributes this Cat can have.
    """
    EVOL_PATH = ['Kitten', 'Catling', 'Cat', 'Nekomo', 'Nekohito']
    MAX_ATTR = {'hunger': 30, 'fun': 20, 'clean': 50, 'stamina': 30}

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

        if a.type == 'food':
            return '{} tasted the {} thoughtfully. '.format(self.name, a.name)
        if a.type == 'play':
            return '{} pawed at the {} thoughtfully. '.format(self.name, a.name)
        if a.type == 'clean':
            return '{} cleaned with the {} thoughtfully. '.format(self.name,
                                                                  a.name)
        if a.type == 'rest':
            return '{} rested on the {} thoughtlessly. '.format(self.name,
                                                                a.name)

    def get_response_d(self, a):
        """ Return a disgust response to action a.

        @type self: Cat
        @type a: Action
            An action performed onto the cat.
        @rtype: str
        """

        if a.type == 'food':
            return '{} spat the {} out in an instant. '.format(self.name,
                                                               a.name)
        if a.type == 'play':
            return '{} touched the {}, but did not seem to want to play it. '.\
                format(self.name, a.name)
        if a.type == 'clean':
            return '{} stayed away from the {} and did not want to get near it.\
             '.format(self.name, a.name)
        if a.type == 'rest':
            return '{} did not even want to see the {} and ran away. '.\
                format(self.name, a.name)

    def get_response_f(self, a):
        """ Return a favour response to action a.

        @type self: Cat
        @type a: Action
            An action performed onto the cat.
        @rtype: str
        """

        if a.type == 'food':
            return '{} buried {} whiskers into the bowl of {}, finished it, and\
            is meowing for more. '.format(self.name,
                                          self.pronouns['poss_lower'], a.name)
        if a.type == 'play':
            return "{} couldn't get {} paws off the {}. {} loved it. ".\
                format(self.name, self.pronouns['poss_lower'], a.name,
                       self.pronouns['subject_upper'])
        if a.type == 'clean':
            return '{} washed {} thoroughly with the {} and meowed at the \
            comfort.'.format(self.name, self.pronouns['reflexive'], a.name)
        if a.type == 'rest':
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

        if a.type == 'food':
            return '{} tasted the {} slobberily. '.format(self.name, a.name)
        if a.type == 'play':
            return '{} pawed at the {} slobberily. '.format(self.name, a.name)
        if a.type == 'clean':
            return '{} cleaned with the {} slobberily. '.format(self.name,
                                                                a.name)
        if a.type == 'rest':
            return '{} rested on the {} slobberily. '.format(self.name,
                                                             a.name)

    def get_response_d(self, a):
        """ Return a disgust response to action a.

        @type self: Dog
        @type a: Action
            An action performed onto the Dog.
        @rtype: str
        """

        if a.type == 'food':
            return "{} didn't seem to like the {}, but swallowed it anyway. ".\
                format(self.name, a.name)
        if a.type == 'play':
            return '{} touched the {}, but did not seem to want to play it. '.\
                format(self.name, a.name)
        if a.type == 'clean':
            return '{} pawed at the {} disappointingly.'.format(self.name,
                                                                a.name)
        if a.type == 'rest':
            return '{} laid on the {}, then flopped up again, still excited. '.\
                format(self.name, a.name)

    def get_response_f(self, a):
        """ Return a favour response to action a.

        @type self: Dog
        @type a: Action
            An action performed onto the Dog.
        @rtype: str
        """

        if a.type == 'food':
            return '{} devoured the {} in an instant, and hastily pushed {} \
                   bowl up to you for more'.format(self.name,
                                                   self.pronouns['poss_'
                                                                 'lower'],
                                                   a.name)
        if a.type == 'play':
            return "{} couldn't get {} paws off the {}. {} loved it. ".\
                format(self.name, self.pronouns['poss_lower'], a.name,
                       self.pronouns['subject_upper'])
        if a.type == 'clean':
            return '{} washed {} thoroughly with the {} and woofed at the \
            comfort.'.format(self.name, self.pronouns['reflexive'], a.name)
        if a.type == 'rest':
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
