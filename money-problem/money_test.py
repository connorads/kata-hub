
import pytest

from money import Money


def test_create_money():
    m = Money(10, 'USD')
    assert m.amount == 10
    assert m.currency == 'USD'

def test_create_money_with_euros():
    m = Money(10, 'EUR')
    assert m.amount == 10
    assert m.currency == 'EUR'

def test_add_two_money_objects():
    m1 = Money(10, 'USD')
    m2 = Money(20, 'USD')
    m3 = m1 + m2
    assert m3.amount == 30
    assert m3.currency == 'USD'

def test_add_two_money_objects_with_different_currencies_should_throw():
    m1 = Money(10, 'USD')
    m2 = Money(20, 'EUR')
    with pytest.raises(ValueError):
        m1 + m2

def test_subtract_two_money_objects():
    m1 = Money(20, 'USD')
    m2 = Money(50, 'USD')
    m3 = m2 - m1
    assert m3.amount == 30
    assert m3.currency == 'USD'

def test_subtract_two_money_objects_with_different_currencies_should_throw():
    m1 = Money(20, 'USD')
    m2 = Money(50, 'EUR')
    with pytest.raises(ValueError):
        m2 - m1

def test_multuply_money_by_number():
    m1 = Money(20, 'USD')
    m2 = m1 * 2
    assert m2.amount == 40
    assert m2.currency == 'USD'

def test_convert_currency():
    m1 = Money(20, 'USD')
    m2 = m1.convert('EUR', 0.85)
    assert m2.amount == 17
    assert m2.currency == 'EUR'