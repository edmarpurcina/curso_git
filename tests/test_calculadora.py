from app.calculadora import soma

def test_soma():
    assert soma(2, 4) == 6

def test_soma_positivos():
    assert soma(2,2) == 4

def test_soma_negativos():
    assert soma(2,-2) == 0
    assert soma(-1,-1) == -2

def test_soma_zero():
    assert soma(0,0) == 0