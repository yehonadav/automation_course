def test_address_book__str__(book):
    assert book.__str__() == '[Name: {} | Address: {} | Email: {} | Phone: {}]'.format(
        book.expected_name, book.expected_address, book.expected_email, book.expected_phone)
