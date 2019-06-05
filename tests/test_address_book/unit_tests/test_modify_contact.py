from tests.test_address_book.config import parameters
from qaviton.utils.random_util import create_random
from qaviton.utils.random_util import fake


def assert_name_modification(book):
    new_name = fake.name()
    while new_name == parameters.name:
        new_name = fake.name()

    printed_msgs, input_msgs = book.modify_contact_interface(
        name=parameters.name,
        modify='1',
        new_value=new_name
    )
    assert len(input_msgs) == 3
    assert input_msgs[0] == 'Enter the full name of the contact to modify: '
    assert input_msgs[1] == 'Modify:\n(1) name\n(2) address\n(3) email\n(4) phone\n'
    assert input_msgs[2] == 'Enter New Name: '
    assert printed_msgs == ['Successful']
    return new_name


def assert_address_modification(book, name):
    new_address = fake.address()
    while new_address == parameters.address:
        new_address = fake.address()

    printed_msgs, input_msgs = book.modify_contact_interface(
        name=name,
        modify='2',
        new_value=new_address
    )
    assert len(input_msgs) == 3
    assert input_msgs[0] == 'Enter the full name of the contact to modify: '
    assert input_msgs[1] == 'Modify:\n(1) name\n(2) address\n(3) email\n(4) phone\n'
    assert input_msgs[2] == 'Enter New Address: '
    assert printed_msgs == ['Successful']


def assert_email_modification(book, name):
    new_email = name + '@gmail.com'
    printed_msgs, input_msgs = book.modify_contact_interface(
        name=name,
        modify='3',
        new_value=new_email
    )
    assert len(input_msgs) == 3
    assert input_msgs[0] == 'Enter the full name of the contact to modify: '
    assert input_msgs[1] == 'Modify:\n(1) name\n(2) address\n(3) email\n(4) phone\n'
    assert input_msgs[2] == 'Enter New Email: '
    assert printed_msgs == ['Successful']


def assert_phone_modification(book, name):
    new_phone = create_random.numbers(length=10)
    while new_phone == parameters.phone:
        new_phone = create_random.numbers(length=10)

    printed_msgs, input_msgs = book.modify_contact_interface(
        name=name,
        modify='4',
        new_value=new_phone
    )
    assert len(input_msgs) == 3
    assert input_msgs[0] == 'Enter the full name of the contact to modify: '
    assert input_msgs[1] == 'Modify:\n(1) name\n(2) address\n(3) email\n(4) phone\n'
    assert input_msgs[2] == 'Enter New Phone: '
    assert printed_msgs == ['Successful']


def test_address_book_modify_contact(book):
    book.add_contacts_interface(
        name=parameters.name,
        address=parameters.address,
        email=parameters.email,
        phone=parameters.phone
    )

    new_name = assert_name_modification(book)
    assert_address_modification(book, new_name)
    assert_email_modification(book, new_name)
    assert_phone_modification(book, new_name)
