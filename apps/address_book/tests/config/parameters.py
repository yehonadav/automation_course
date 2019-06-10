from qaviton.utils.random_util import fake
from qaviton.utils.random_util import create_random


name = fake.name().replace(' ', '_')
address = fake.address()
email = name + '@gmail.com'
phone = create_random.numbers(length=10)
