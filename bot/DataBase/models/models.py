
from sqlmodel import Field, SQLModel
from pydantic import field_validator
import re
from DataBase.methods.user import UserMethods
from DataBase.methods.baseMethods import BaseDbMethods


class User(SQLModel, BaseDbMethods, table=True,):
    id: int = Field(default=None, primary_key=True)
    username: str = Field(index=True, unique=True, nullable=False)
    email: str = Field(index=True, unique=True, nullable=True)
    phone: str = Field(index=True, unique=True, nullable=True)
    full_name: str = None
    disabled: bool = False

    @field_validator("email")
    def validate_email(cls, v):
        if v and not re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', v):
            raise ValueError("Invalid email format")
        return v

    @field_validator("phone")
    def validate_phone(cls, v):
        if v and not re.match(r'^\+?[1-9]\d{1,14}$', v):
            raise ValueError("Invalid phone number format")
        return v




