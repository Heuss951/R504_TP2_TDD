from cryptage import crypt

def test_crypt_simple():
    result = crypt("abc")
    assert result == "bcd1"   

def test_crypt_avec_pas():
    result = crypt("abc", 3)
    assert result == "def3"  
