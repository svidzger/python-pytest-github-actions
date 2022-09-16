from postinumerot import main, smartpost_problem


def test_postinumerot_one_postalcode_juupajoki():

    assert main('juupajoki') == '35540'


def test_postinumerot_many_postcodes_karkkila():
    assert main('karkkila') == '03600, 03601, 03620'


def test_postinumerot_city_not_in_finland():
    assert not main('stockholm')


def test_postinumerot_not_a_city():
    assert not main('kissa')


def test_postinumerot_smart_post_contains_smartpost():
    assert not len(main('smart post')) < 1
    assert len(main('smart post')) > 5870


def test_postinumerot_smartpost_contains_smartpost():
    assert not len(main('smartpost')) < 1
    assert len(main('smartpost')) > 5870


def test_smartpost_problem_combined():
    assert smartpost_problem('SMARTPOST') == 'SMART POST'


def test_smartpost_problem_separated():
    assert smartpost_problem('SMART POST') == 'SMARTPOST'
