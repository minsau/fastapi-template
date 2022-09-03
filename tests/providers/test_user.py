from sqlalchemy.orm import Session

from app.models.user import User
from app.providers.user import user as user_provider
from app.schemas.user import UserCreate
from tests.factories.user import UserFactory
from tests.utils.random import random_email, random_lower_string


class TestUserBaseProvider:
    def create_user(self, db: Session) -> User:
        email = random_email()
        user = UserFactory.create(email=email)
        db.commit()

        return user

    def test_should_create_user_from_user_create(self, db: Session) -> None:
        email = random_email()
        password = random_lower_string()
        user_in = UserCreate(username=email, email=email, password=password, is_superuser=False)
        user = user_provider.create(db=db, obj_in=user_in)
        assert user.email == email
        assert user.is_superuser is False

    def test_should_get_user_by_email(self, db: Session) -> None:
        user_created = self.create_user(db=db)
        user = user_provider.get_by_email(db=db, email=user_created.email)
        assert user.email == user_created.email
        assert user.is_superuser is False
