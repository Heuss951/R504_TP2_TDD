from fizzbuzz import affiche   # vérifie que cette ligne est bien présente tout en haut

def test_affiche_sans_param():
    result = affiche()
    assert "Fizz" in result
    assert "Buzz" in result
    assert "FrisBee" in result
    assert result.startswith("1")

def test_affiche_avec_param():
    result = affiche(15)
    assert result.endswith("FrisBee")  # 15 est un multiple de 15
