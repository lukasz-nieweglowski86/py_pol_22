from model.contact import Contact


def test_edit_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first_contact(Contact(firstname="edited", middlename="edited",
                                           lastname="edited", nickname="edited", title="edited",
                                           company="edited", address1="edited",
                                           home_phonenumber="111111111", mobile_phonenumber="222222222",
                                           work_phonenumber="333333333", fax="444444444", email1="edited1@test.com",
                                           email2="edited2@test.com", email3="edited3@test.com",
                                           homepage="www.edited.com", bday="12", bmonth="June", byear="1886", aday="1",
                                           amonth="January", ayear="2022", address2="edited2", phone2="555555555",
                                           notes="edited"))
    app.session.logout()
