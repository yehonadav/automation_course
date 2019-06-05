from tests.test_address_book.config import parameters


def test_display_contacts(book):
    printed_msgs, input_msgs = book.display_contacts_interface()
    assert printed_msgs == ['No Records in database.']

    book.add_contacts_interface(
        name=parameters.name,
        address=parameters.address,
        email=parameters.email,
        phone=parameters.phone
    )

    printed_msgs, input_msgs = book.display_contacts_interface()
    assert len(printed_msgs) == 1
    assert printed_msgs[0]['Name'] == parameters.name
    assert printed_msgs[0]['Address'] == parameters.address
    assert printed_msgs[0]['Email'] == parameters.email
    assert printed_msgs[0]['Phone'] == int(parameters.phone)
