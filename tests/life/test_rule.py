import pytest

from life.rule import DEFAULT_RULE, Rule


@pytest.mark.parametrize('rulestring, exp_birth, exp_survival', (
    (DEFAULT_RULE, (3,), (2, 3)),
    ('B0123456789/S0123456789', (0, 1, 2, 3, 4, 5, 6, 7, 8, 9), (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)),
    ('b1/s', (1,), ()),
    ('b1', (1,), ()),
))
def test_rule_init(rulestring, exp_birth, exp_survival):
    rule = Rule(rulestring)
    assert rule.birth == exp_birth
    assert rule.survival == exp_survival
