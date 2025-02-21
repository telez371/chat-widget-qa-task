from faker import Faker

from e2e_tests.data.data import Person

faker_en = Faker('en_US')


def generated_person():
    return Person(
        first_name=faker_en.first_name(),
        email=faker_en.email(),
    )
