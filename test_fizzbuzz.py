from fizzbuzz import affiche   

def test_affiche_sans_param():
    result = affiche()
    assert "Fizz" in result
    assert "Buzz" in result
    assert "FrisBee" in result
    assert result.startswith("1")

def test_affiche_avec_param():
    result = affiche(15)
    assert "FrisBee" in result          # doit contenir FrisBee au moins une fois
    assert result[0].isdigit() or result.startswith("F")  # doit commencer par un chiffre ou Fizz  

def test_affiche_intervalle():
    result = affiche(5, 10)
    assert result == "BuzzFizz78FizzBuzz"
