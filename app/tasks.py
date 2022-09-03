import logging

from app.core.celery_app import app
from app.core.session import SessionLocal
from app.providers.user import user as user_provider
from app.schemas.user import UserUpdate

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@app.task
def test_celery(word: str) -> str:
    return f"test task return {word}"


@app.task
def send_user_invitation():
    """Send user invitation."""
    logger.info("Sending invitations for all non active users")
    with SessionLocal() as db:
        users = user_provider.filter(db=db, is_active=False)
        logger.info(f"Found {len(users)} users to send invitations to")

        for user in users:
            user_update = UserUpdate(invitation_sent=True, password=None)
            user_provider.update(db=db, db_obj=user, obj_in=user_update)
