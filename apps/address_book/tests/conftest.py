import pytest
from apps.address_book.tests.services.address_book import AddressBook
from apps.address_book.tests.config import parameters as p


@pytest.fixture(scope='session')
def parameters():
    return p


@pytest.fixture(scope='session')
def book(request, parameters):
    """fixture for cross-platform model-based application
    always use session scope for this type of fixture
    :rtype: AddressBook
    """
    book = AddressBook(
        name=parameters.name,
        address=parameters.address,
        email=parameters.email,
        phone=parameters.phone
    )
    book.create()
    request.addfinalizer(book.delete)
    return book


@pytest.fixture(scope='session')
def empty_book():
    """fixture for cross-platform model-based application
    always use session scope for this type of fixture
    :rtype: AddressBook
    """
    book = AddressBook(None, None, None, None)
    return book


@pytest.fixture(scope='session')
def add_contact(book, parameters):
    printed_msgs, input_msgs = book.display_contacts_interface()
    assert printed_msgs == ['No Records in database.']

    return book.add_contacts_interface(
        name=parameters.name,
        address=parameters.address,
        email=parameters.email,
        phone=parameters.phone
    )
