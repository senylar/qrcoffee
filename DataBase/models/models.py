from typing import Optional, List
from datetime import datetime
from sqlmodel import Field, SQLModel, Relationship, Column, JSON
from pydantic import field_validator
import re
from DataBase.methods.baseMethods import BaseDbMethods


class Users(SQLModel, BaseDbMethods, table=True):
    id: int = Field(default=None, primary_key=True)
    telegram_id: int = Field(index=True, unique=True, nullable=False)
    name: Optional[str] = None
    phone: Optional[str] = Field(index=True, unique=True, nullable=True)
    email: Optional[str] = Field(index=True, unique=True, nullable=True)
    registration_date: datetime = Field(default_factory=datetime.utcnow)
    status: str = Field(default="active")  # active/blocked
    balance: float = Field(default=0.0)
    qrcodes: List["QRCode"] = Relationship(back_populates="user")
    operations: List["Operations"] = Relationship(back_populates="user")
    staff: Optional["Staff"] = Relationship()

    @field_validator("phone")
    def validate_phone(cls, v):
        if v and not re.match(r'^\+?[1-9]\d{1,14}$', v):
            raise ValueError("Invalid phone number format")
        return v


class QRCode(SQLModel,BaseDbMethods, table=True):
    id: int = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="users.id")
    code: str = Field(unique=True, nullable=False)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
    active: bool = Field(default=True)
    user: Optional[Users] = Relationship(back_populates="qrcodes")


class Staff(SQLModel, BaseDbMethods, table=True):
    id: int = Field(default=None, primary_key=True)
    role: str = Field(nullable=False)  # barista/admin
    token: str = Field(nullable=False, unique=True)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    operations: List["Operations"] = Relationship(back_populates="staff")


class Operations(SQLModel,BaseDbMethods, table=True):
    id: int = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="users.id")
    staff_id: Optional[int] = Field(foreign_key="staff.id", default=None)
    operation_type: str = Field(nullable=False)  # purchase/bonus_accrual/bonus_spending/qrcode_scan/participation_in_promo
    amount: Optional[float] = None
    operation_datetime: datetime = Field(default_factory=datetime.utcnow)
    details: Optional[dict] = Field(default=None, sa_column=Column(JSON))
    user: Optional[Users] = Relationship(back_populates="operations")
    staff: Optional["Staff"] = Relationship(back_populates="operations")


class Promo(SQLModel,BaseDbMethods, table=True):
    id: int = Field(default=None, primary_key=True)
    title: str = Field(nullable=False)
    description: Optional[str] = None
    photo: Optional[str] = None  # ссылка/имя файла
    start_date: datetime = Field(nullable=False)
    end_date: datetime = Field(nullable=False)
    active: bool = Field(default=True)


Users.model_rebuild()
QRCode.model_rebuild()
Operations.model_rebuild()
Staff.model_rebuild()
