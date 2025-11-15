from sqlalchemy.orm import session, Session

from app.schemas.user import User

def create_user(db: Session, user: User):
    # Create a new User instance
    new_user = User(
        username=user.username,
        email=user.email,
        password=user.password,
        is_active=user.is_active
    )

    # Add the new user to the database
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user