import os
import mock
import builtins
from apps.address_book import address_book


def interface(f):
    def decorator(self, *args, **kw):
        with mock.patch.object(builtins, 'print', self.catch_print):
            with mock.patch.object(builtins, 'input', self.catch_input):
                res = f(self, *args, **kw)

        printed_msgs = self.printed_msgs
        input_msgs = self.input_msgs

        self.printed_msgs = []
        self.inputs = []
        self.input_msgs = []

        if res: return res, printed_msgs, input_msgs
        return printed_msgs, input_msgs

    return decorator


class AddressBook(address_book.AddressBook):
    printed_msgs = []
    inputs = []
    input_msgs = []

    filename = 'mock_address_book'

    def __init__(self, name: str, address: str, email: str, phone: str):
        address_book.AddressBook.__init__(self, name, address, email, phone)
        self.expected_name = name
        self.expected_address = address
        self.expected_email = email
        self.expected_phone = phone

    @interface
    def modify_contact_interface(self, name: str, modify: str, new_value: str):
        self.inputs = [name, modify, new_value]
        address_book.AddressBook.modify_contact(self)

    @interface
    def search_contact_interface(self, name: str):
        self.inputs = [name]
        address_book.AddressBook.search_contact(self)

    @interface
    def display_contacts_interface(self):
        address_book.AddressBook.display_contacts(self)

    @interface
    def get_user_details_interface(self, name: str, address: str, email: str, phone: str):
        self.inputs = [name, address, email, phone]
        return address_book.AddressBook.get_user_details(self)

    @interface
    def add_contacts_interface(self, name: str, address: str, email: str, phone: str):
        self.inputs = [name, address, email, phone]
        address_book.AddressBook.add_contacts(self)

    def create(self):
        """setup interface"""
        open(self.filename, 'wb').close()

    def delete(self):
        """teardown interface"""
        os.remove(self.filename)

    def catch_print(self, *msgs):
        """mock interface to obtain print messages"""
        for msg in msgs:
            self.printed_msgs.append(msg)

    def catch_input(self, msg):
        """mock interface to obtain input messages and return mocked input"""
        self.input_msgs.append(msg)
        return self.inputs.pop(0)

    def assert_attributes(self):
        """assertion function"""
        # assert attributes exist
        assert hasattr(self, 'name')
        assert hasattr(self, 'address')
        assert hasattr(self, 'email')
        assert hasattr(self, 'phone')
        assert hasattr(self, '__str__')
        assert hasattr(self, '__repr__')
        assert hasattr(self, 'add_contacts')
        assert hasattr(self, 'display_contacts')
        assert hasattr(self, 'get_user_details')
        assert hasattr(self, 'modify_contact')
        assert hasattr(self, 'search_contact')

        # assert attribute values are correct
        assert self.name == self.expected_name
        assert self.address == self.expected_address
        assert self.email == self.expected_email
        assert self.phone == self.expected_phone

        # assert methods
        assert callable(self.__str__)
        assert callable(self.__repr__)
        assert callable(self.add_contacts)
        assert callable(self.display_contacts)
        assert callable(self.get_user_details)
        assert callable(self.modify_contact)
        assert callable(self.search_contact)


