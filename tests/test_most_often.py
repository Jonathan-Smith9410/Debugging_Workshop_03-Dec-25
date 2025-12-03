from lib.most_often import MostOften

def test_most_often_instantiates():
    mo = MostOften(['a', 'b'])

    assert mo.starting_list == ['a', 'b']

def test_most_often_can_add_new():
    mo = MostOften(['a', 'b'])

    mo.add_new('c')

    assert mo.starting_list == ['a', 'b', 'c']

def test_most_often_can_get_most_often_element():
    mo = MostOften(['a', 'b', 'a'])

    assert mo.get_most_often() == 'a'

def test_most_often_can_get_most_often_element_no_clear_winner():
    mo = MostOften(['a', 'b'])

    assert mo.get_most_often() == 'no clear winner'