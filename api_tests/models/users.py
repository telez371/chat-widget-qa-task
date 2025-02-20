from pydantic import BaseModel, EmailStr, UUID4
from typing import Dict, Any
from faker import Faker
import uuid

fake = Faker()


class UserPayload(BaseModel):
    id: UUID4
    login: UUID4
    email: EmailStr
    fullName: str
    payload: Dict[str, Any]

    @classmethod
    def generate_fake(cls) -> "UserPayload":
        return cls(
            id=uuid.uuid4(),
            login=uuid.uuid4(),
            email=fake.email(),
            fullName=fake.name(),
            payload={}
        )
