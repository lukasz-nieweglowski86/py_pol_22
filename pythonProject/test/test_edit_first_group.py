from model.group import Group


def test_edit_first_group_name(app):
    if app.group.count() == 0:
        app.group.add(Group(name="added group", header_name="test header", footer_name="test footer"))
    app.group.edit_first_group(Group(name="name edited"))


def test_edit_first_group_header(app):
    if app.group.count() == 0:
        app.group.add(Group(name="added group", header_name="test header", footer_name="test footer"))
    app.group.edit_first_group(Group(header_name="header edited"))
