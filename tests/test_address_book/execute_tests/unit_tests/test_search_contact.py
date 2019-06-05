def test_address_book_search_contact(book, add_contact, parameters):
    printed_msgs, input_msgs = book.search_contact_interface(name=parameters.name)
    assert input_msgs == ['Enter the name of the contact to search: ']
    assert len(printed_msgs) == 1
    assert printed_msgs[0]['Name'] == parameters.name
    assert printed_msgs[0]['Address'] == parameters.address
    assert printed_msgs[0]['Email'] == parameters.email
    assert printed_msgs[0]['Phone'] == int(parameters.phone)
