from model.group import Group
import random
import string


constant = [
    Group(name="name1", header_name="header1", footer_name="footer1"),
    Group(name="name2", header_name="header2", footer_name="footer2"),
]


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Group(name="", header_name="", footer_name="")] + [
    Group(name=random_string("name: ", 10), header_name=random_string("header: ", 20),
          footer_name=random_string("footer: ", 20))
    for i in range(5)
]
