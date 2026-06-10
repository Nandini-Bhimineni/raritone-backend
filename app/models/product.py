from datetime import datetime

from sqlalchemy import (
    Column,
    Integer,
    String,
    Float,
    ForeignKey,
    DateTime
)
from sqlalchemy.orm import relationship

from app.database.base import Base


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String(255), nullable=False)
    description = Column(String(500))

    price = Column(Float, nullable=False)
    stock = Column(Integer, default=0)

    image_url = Column(String(500))

    category_id = Column(
        Integer,
        ForeignKey("categories.id")
    )

    variant = Column(String(100))
    sku=Column(String(100),unique=True)
    brand=Column(String(100))

    status = Column(
        String(20),
        default="active"
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )

    updated_at = Column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )

    category = relationship("Category")