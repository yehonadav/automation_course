def test_address_book__repr__(book):
    assert book.__repr__() == '[Name: {} | Address: {} | Email: {} | Phone: {}]'.format(
        book.expected_name, book.expected_address, book.expected_email, book.expected_phone)
