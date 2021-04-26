from collections import defaultdict
from dataclasses import dataclass


DEFAULT_RULE = 'B3/S23'


@dataclass(frozen=True)
class Rule:
    """Model to hold a ruleset for the game of life."""
    birth: frozenset[int]
    survival: frozenset[int]

    def __init__(self, rulestring: str):
        """Create the rule.
        :param rulestring: the rulestring to generate the model from
        """
        accumulator: dict[str, list[int]] = defaultdict(list)
        for rule in rulestring.upper().split('/'):
            accumulator[rule[0]] += [int(n) for n in rule[1:]]
        object.__setattr__(self, 'birth', frozenset(accumulator['B']))
        object.__setattr__(self, 'survival', frozenset(accumulator['S']))
