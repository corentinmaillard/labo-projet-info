import main
import pytest

def test_fact():
    # À compléter...
    pass

def test_roots():
    # À compléter...
    pass

def test_integrate():
    # À compléter...
    pass

def test_add():
    assert main.add(3, 4)==7
    assert main.add(3, 5)==8
    assert main.add(2, 4)==6

def test_fact():
    assert main.fact(5)==120
    assert main.fact(3)==6
    assert main.fact(4)==24