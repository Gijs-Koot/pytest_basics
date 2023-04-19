from ptb import impl

def test_group_summer():

    things = [('A', 1), ('B', 2), ('C', 4), ('B', 4)]

    summer = impl.GroupSummer(things)

    assert len(summer._groups) == 3
    assert summer.groupsum('B') == 6