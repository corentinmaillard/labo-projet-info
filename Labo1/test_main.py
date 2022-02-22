import main
import pytest

def test_roots():
    assert main.roots(1, 2, 1)==-1
    assert main.roots(1, 0, 1)=="Racine non réelle"
    assert main.roots(1, -3, 2)==[2.0, 1.0]

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