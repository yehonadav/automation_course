import pytest
from qaviton.utils.random_util import fake
from qaviton.utils.random_util import create_random
from tests.test_address_book.services.address_book import AddressBook


@pytest.fixture(scope='session')
def book(request):
    """fixture for cross-platform model-based application
    always use session scope for this type of fixture
    :rtype: AddressBook
    """
    expected_name = fake.name().replace(' ', '_')
    expected_address = fake.address()
    expected_email = expected_name + '@gmail.com'
    expected_phone = create_random.numbers(length=10)

    book = AddressBook(
        name=expected_name,
        address=expected_address,
        email=expected_email,
        phone=expected_phone
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
