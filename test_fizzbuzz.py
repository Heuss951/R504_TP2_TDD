from fizzbuzz import affiche

def test_affiche_sans_param():
    result = affiche()
    assert "Fizz" in result
    assert "Buzz" in result
    assert "FrisBee" in result
    assert result.startswith("1")
