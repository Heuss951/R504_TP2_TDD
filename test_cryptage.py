from cryptage import crypt

def test_crypt_simple():
    result = crypt("abc")
    assert result == "bcd"
