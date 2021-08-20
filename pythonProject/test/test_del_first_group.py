from model.group import Group


def test_delete_first_group(app):
    if app.group.count() == 0:
        app.group.add(Group(name="added group", header_name="test header", footer_name="test footer"))
    app.group.delete_first_group()
