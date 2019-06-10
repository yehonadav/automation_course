def test_address_book_search_contact(book, add_contact, parameters):
    book.assert_contact_exist(parameters)
