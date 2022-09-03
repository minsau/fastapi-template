from sqlalchemy.orm import Session

from app.providers.user import user as user_provider
from app.tasks import send_user_invitation
from tests.factories.user import UserFactory


class TestSendInvitationTask:
    def test_should_update_invitation_sent_flag(self, db: Session) -> None:
        # Given
        user_created = UserFactory.create(is_active=False, invitation_sent=False)
        db.commit()
        # When
        send_user_invitation.apply()
        # Then
        user = user_provider.get(db=db, id=user_created.id)
        assert user.invitation_sent is True
