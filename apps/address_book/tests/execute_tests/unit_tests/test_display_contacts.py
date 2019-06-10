def test_display_contacts(book, add_contact, parameters):
    printed_msgs, input_msgs = book.display_contacts_interface()
    assert len(printed_msgs) == 1
    assert printed_msgs[0]['Name'] == parameters.name
    assert printed_msgs[0]['Address'] == parameters.address
    assert printed_msgs[0]['Email'] == parameters.email
    assert printed_msgs[0]['Phone'] == int(parameters.phone)
