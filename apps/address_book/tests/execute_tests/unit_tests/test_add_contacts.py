def test_address_book_add_contacts(book, add_contact):
    printed_msgs, input_msgs = add_contact
    assert len(input_msgs) == 4
    assert input_msgs[0] == 'Enter Contact\'s Full Name: '
    assert input_msgs[1] == 'Enter Contact\'s Address: '
    assert input_msgs[2] == 'Enter Contact\'s Email Address: '
    assert input_msgs[3] == 'Enter Contact\'s Phone Number: '
    assert printed_msgs == ['Contact Added Successfully!']
