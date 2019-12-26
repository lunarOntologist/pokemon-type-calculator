import calc as calc
from operator import and_
from functools import reduce

def test_get_starting_vals():
    vals = calc.get_starting_vals()
    assert len(vals) == 18
    assert reduce(and_, [v == 1 for v in vals.values() ])
