"""
Constants to be used in PetSim.
Written by Ellen Yufei Chen (BlackSpade741) 2016-2017.
"""

# pet class
PRONOUNS = {'m': {'subject_upper': 'He', 'object': 'him', 'poss_upper': 'His',
                  'poss_lower': 'his', 'subject_lower': 'he',
                  'reflexive': 'himself'},
            'f': {'subject_upper': 'She', 'object': 'her', 'poss_upper': 'Her',
                  'poss_lower': 'her', 'subject_lower': 'she',
                  'poss_noun_lower': 'hers', 'poss_noun_upper': 'Hers',
                  'reflexive': 'herself'},
            'n': {'subject_upper': 'They', 'object': 'them',
                  'poss_upper': 'Their', 'poss_lower': 'their',
                  'subject_lower': 'they', 'poss_noun_lower': 'theirs',
                  'poss_noun_upper': 'Theirs', 'reflexive': 'themselves'}}

EVOL_PATH = {'cat': ['Kitten', 'Catling', 'Cat', 'Nekomo', 'Nekohito'],
             'dog': ['Pupper', 'Dogling', 'Dog', 'Inumo', 'Inuhito']}

MAX_ATTR = {'cat': {'hunger': 30, 'fun': 20, 'clean': 50, 'stamina': 30},
            'dog': {'hunger': 40, 'fun': 40, 'clean': 20, 'stamina': 30}}

EVOL_LEVELS = [5, 10, 25, 50]

REACTION_MULT = {'n': 0.75, 'f': 1.0, 'd': 0.0}

TYPES = ['food', 'play', 'clean', 'rest']

EXP_MULTIPLIER = 1.5

EXP_START_CAP = 20
