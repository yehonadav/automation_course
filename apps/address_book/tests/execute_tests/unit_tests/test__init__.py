def test_address_book_with_required_attributes(book):
    book.assert_attributes()


def test_empty_address_book(empty_book):
    empty_book.assert_attributes()
