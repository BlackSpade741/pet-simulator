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
        
        pass
    
    def get_response_d(self, a):
        """ Returns a disgust response of the pet to Action a.
        
        @type self: Pet
        @type a: Action
            An action done on the pet.
        @rtype: str
            A string describing a response to a.
        """
        pass
    
    def get_response_f(self, a):
        """ Returns a favoured response of the pet to Action a.
            
        @type self: Pet
        @type a: Action
            An action done on the pet.
        @rtype: str
            A string describing a response to a.
        """
        pass

    def evolve(self):
        """ Evolve the pet to the next stage and return a message.
        
        @type self: Pet
        @rtype: str
        """
        pass

    def level_up(self):
        """ Level up the pet, and return a message.
        
        @type self: Pet
        @rtype: str
        """
        pass
