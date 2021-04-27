from collections import defaultdict
from dataclasses import dataclass


NAMED_RULES = {
    'seeds': 'B2',
    'life-without-death': 'B3/S012345678',
    'flock': 'B3/S12',
    'mazectric': 'B3/S1234',
    'maze': 'B3/S12345',
    'original': 'B3/S23',
    'highlife': 'B36/S23',
    'move': 'B368/S245',
}
DEFAULT_RULE = NAMED_RULES['original']


@dataclass(frozen=True)
class Rule:
    """Model to hold a ruleset for the game of life."""
    birth: frozenset[int]
    survival: frozenset[int]

    def __init__(self, rulestring: str):
        """Create the rule.
        :param rulestring: the rulestring to generate the model from
        """
        rulestring = NAMED_RULES.get(rulestring, rulestring)
        accumulator: dict[str, list[int]] = defaultdict(list)
        for rule in rulestring.upper().split('/'):
            accumulator[rule[0]] += [int(n) for n in rule[1:]]
        object.__setattr__(self, 'birth', frozenset(accumulator['B']))
        object.__setattr__(self, 'survival', frozenset(accumulator['S']))
