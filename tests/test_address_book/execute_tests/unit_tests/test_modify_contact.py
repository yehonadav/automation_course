from qaviton.utils.random_util import create_random
from qaviton.utils.random_util import fake


def test_address_book_modify_contact_name(book, add_contact, parameters):
    new_value = fake.name()
    while new_value == parameters.name:
        new_value = fake.name()

    printed_msgs, input_msgs = book.modify_contact_interface(
        name=parameters.name,
        modify='1',
        new_value=new_value)

    try:
        assert len(input_msgs) == 3
        assert input_msgs[0] == 'Enter the full name of the contact to modify: '
        assert input_msgs[1] == 'Modify:\n(1) name\n(2) address\n(3) email\n(4) phone\n'
        assert input_msgs[2] == 'Enter New Name: '
        assert printed_msgs == ['Successful']
    finally:
        book.modify_contact_interface(name=new_value, modify='1', new_value=parameters.name)
        book.assert_contact_exist(parameters)


def test_address_book_modify_contact_address(book, add_contact, parameters):
    new_value = fake.name()
    while new_value == parameters.address:
        new_value = fake.name()

    printed_msgs, input_msgs = book.modify_contact_interface(
        name=parameters.name,
        modify='2',
        new_value=new_value)

    try:
        assert len(input_msgs) == 3
        assert input_msgs[0] == 'Enter the full name of the contact to modify: '
        assert input_msgs[1] == 'Modify:\n(1) name\n(2) address\n(3) email\n(4) phone\n'
        assert input_msgs[2] == 'Enter New Address: '
        assert printed_msgs == ['Successful']
    finally:
        book.modify_contact_interface(name=parameters.name, modify='2', new_value=parameters.address)


def test_address_book_modify_contact_email(book, add_contact, parameters):
    new_value = fake.name()
    while new_value == parameters.name:
        new_value = fake.name()
    new_value = new_value + '@gmail.com'

    printed_msgs, input_msgs = book.modify_contact_interface(
        name=parameters.name,
        modify='3',
        new_value=new_value)

    try:
        assert len(input_msgs) == 3
        assert input_msgs[0] == 'Enter the full name of the contact to modify: '
        assert input_msgs[1] == 'Modify:\n(1) name\n(2) address\n(3) email\n(4) phone\n'
        assert input_msgs[2] == 'Enter New Email: '
        assert printed_msgs == ['Successful']
    finally:
        book.modify_contact_interface(name=parameters.name, modify='3', new_value=parameters.email)


def test_address_book_modify_contact_phone(book, add_contact, parameters):
    new_value = create_random.numbers(length=10)
    while new_value == parameters.phone:
        new_value = create_random.numbers(length=10)

    printed_msgs, input_msgs = book.modify_contact_interface(
        name=parameters.name,
        modify='4',
        new_value=new_value)

    try:
        assert len(input_msgs) == 3
        assert input_msgs[0] == 'Enter the full name of the contact to modify: '
        assert input_msgs[1] == 'Modify:\n(1) name\n(2) address\n(3) email\n(4) phone\n'
        assert input_msgs[2] == 'Enter New Phone: '
        assert printed_msgs == ['Successful']
    finally:
        book.modify_contact_interface(name=parameters.name, modify='4', new_value=int(parameters.phone))
