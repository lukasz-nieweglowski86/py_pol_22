# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    app.group.add(Group(name="test group", header_name="group header", footer_name="group footer"))


def test_add_empty_group(app):
    app.group.add(Group(name="", header_name="", footer_name=""))
