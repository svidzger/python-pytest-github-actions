from postinumerot import main, smartpost_problem


def test_postinumerot_one_postcode():
    assert main('juupajoki')


def test_postinumerot_many_postcodes():
    assert main('helsinki')


def test_postinumerot_city_not_in_finland():
    assert not main('stockholm')


def test_postinumerot_not_a_city():
    assert not main('kissa')


def test_postinumerot_smart_post():
    assert main('smart post')


def test_postinumerot_smartpost():
    assert main('smartpost')


def test_smartpost_problem_combined():
    assert smartpost_problem('SMARTPOST') == 'SMART POST'


def test_smartpost_problem_separated():
    assert smartpost_problem('SMART POST') == 'SMARTPOST'
