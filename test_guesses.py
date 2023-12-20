from guesses import guesses


def test_binary_search_guesses():
    assert guesses(50, 1, 100) == 50
    assert guesses(100, 1, 100) == 100
    assert guesses(1, 1, 100) == 1
    assert guesses(101, 1, 100) == -1
