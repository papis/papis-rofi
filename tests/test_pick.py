from papis_rofi.main import pick


def test_simple():
    assert(pick([]) == [])
    assert(pick(['test']) == ['test'])
