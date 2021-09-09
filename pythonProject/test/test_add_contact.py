# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_phone(prefix, maxlen):
    phone_numbers = string.digits
    return prefix + "".join([random.choice(phone_numbers) for i in range(random.randrange(maxlen))])


months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November",
          "December"]

testdata = [Contact(firstname=random_string("firstname: ", 8), middlename=random_string("middlename: ", 8),
                    lastname=random_string("lastname: ", 12), nickname=random_string("nickname: ", 8),
                    title=random_string("title: ", 6), company=random_string("company: ", 20),
                    address1=random_string("address1: ", 12), home_phonenumber=random_phone("home_phonenumber: ", 12),
                    mobile_phonenumber=random_phone("mobile_phonenumber: ", 12),
                    work_phonenumber=random_phone("work_phonenumber: ", 12), fax=random_phone("fax: ", 12),
                    email1=random_string("email1: ", 16), email2=random_string("email2: ", 16),
                    email3=random_string("email3: ", 16), homepage=random_string("homepage: ", 20),
                    bday=str(random.randint(1, 29)),
                    bmonth=random.choice(months),
                    byear=str(random.randint(1950, 2016)),
                    aday=str(random.randint(1, 29)),
                    amonth=random.choice(months),
                    ayear=str(random.randint(1950, 2016)),
                    address2=random_string("address2: ", 16), phone2=random_phone("phone2: ", 12),
                    notes=random_string("notes: ", 50))
            for i in range(5)]


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.add(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
