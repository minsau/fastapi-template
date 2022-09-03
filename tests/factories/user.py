import factory
from faker import Faker

from app.models.user import User

fake = Faker()


class UserFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = User

    full_name = factory.LazyFunction(fake.name)
    email = factory.LazyFunction(fake.email)
    hashed_password = factory.LazyFunction(fake.password)
    is_active = True
    is_superuser = False
