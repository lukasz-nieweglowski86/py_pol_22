from model.group import Group


def test_edit_first_group_name(app):
    if app.group.count() == 0:
        app.group.add(Group(name="added group", header_name="test header", footer_name="test footer"))
    old_groups = app.group.get_group_list()
    group = Group(name="name edited")
    group.id = old_groups[0].id
    app.group.edit_first_group(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[0] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


#def test_edit_first_group_header(app):
#    if app.group.count() == 0:
#        app.group.add(Group(name="added group", header_name="test header", footer_name="test footer"))
#    old_groups = app.group.get_group_list()
#    app.group.edit_first_group(Group(header_name="header edited"))
#    new_groups = app.group.get_group_list()
#    assert len(old_groups) == len(new_groups)
