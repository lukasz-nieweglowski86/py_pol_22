# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contacts_list()
    contact = Contact(firstname="Test_firstname", middlename="Test_middlename",
                      lastname="Test_lastname", nickname="Test_nickname", title="Test_title",
                      company="Test_company", address1="Test_address1", home_phonenumber="123123123",
                      mobile_phonenumber="321321321", work_phonenumber="135135135", fax="123456789",
                      email1="test_email1@test.com", email2="test_email2@test.com",
                      email3="test_email3@test.com", homepage="www.google.com", bday="11",
                      bmonth="March", byear="1986", aday="7", amonth="July", ayear="2020",
                      address2="Test_address2", phone2="909808707", notes="Lorem ipsum...")
    app.contact.add(contact)
    new_contacts = app.contact.get_contacts_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
