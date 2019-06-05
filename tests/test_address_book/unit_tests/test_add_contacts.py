from tests.test_address_book.config import parameters


def test_address_book_add_contacts(book):
    printed_msgs, input_msgs = book.add_contacts_interface(
        name=parameters.name,
        address=parameters.address,
        email=parameters.email,
        phone=parameters.phone
    )
    assert len(input_msgs) == 4
    assert input_msgs[0] == 'Enter Contact\'s Full Name: '
    assert input_msgs[1] == 'Enter Contact\'s Address: '
    assert input_msgs[2] == 'Enter Contact\'s Email Address: '
    assert input_msgs[3] == 'Enter Contact\'s Phone Number: '
    assert printed_msgs == ['Contact Added Successfully!']
