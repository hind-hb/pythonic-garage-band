import pytest
from pythonic_garage_band.Band import (
    Band,
    Musician,
    Guitarist,
    Bassist,
    Drummer
)

def test_guitarist_str():
    na = Guitarist( "Stel Andre" )
    actual = str(na)
    expected = "My name is: Stel Andre"
    assert actual == expected


def test_guitarist_repr():
    na = Guitarist("Stel Andre")
    actual = repr(na)
    expected = "Guitarist instance. Name = Stel Andre"
    assert actual == expected


def test_bassist_str():
    na = Bassist("Wajtek pilioch")
    actual = str(na)
    expected = "My name is: Wajtek pilioch"
    assert actual == expected

def test_bassist_repr():
    na = Bassist("Wajtek pilioch")
    actual = repr(na)
    expected = "Bassist instance. Name = Wajtek pilioch"
    assert actual == expected




def test_drummer_str():
    na = Drummer("Meinal")
    actual = str(na)
    expected = "My name is: Meinal"
    assert actual == expected


def test_drummer_repr():
    na = Drummer("Meinal")
    actual = repr(na)
    expected = "Drummer instance. Name = Meinal"
    assert actual == expected

@pytest.fixture
def test_band_mem(Bandaa):

    assert len(Bandaa.members) == 3

    assert isinstance(Bandaa.members[0], Musician)
    assert isinstance(Bandaa.members[0], Guitarist)
    assert Bandaa.members[0].name == "Stel Andre"

    assert isinstance(Bandaa.members[1], Musician)
    assert isinstance(Bandaa.members[1], Bassist)
    assert Bandaa.members[1].name == "Wajtek pilioch"

    assert isinstance(Bandaa.members[2], Musician)
    assert isinstance(Bandaa.members[2], Drummer)
    assert Bandaa.members[2].name == "Meinal"