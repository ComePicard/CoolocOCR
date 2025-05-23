from datetime import datetime

from pydantic import BaseModel, Field


class Article(BaseModel):
    name: str = Field(..., title="Name", max_length=250, description="Name of the article",)
    unit_price: float = Field(..., title="Unit Price", ge=0, description="Unit price of the article",)
    quantity: int = Field(..., title="Quantity", ge=1, description="Quantity of the article",)
    total_price: float = Field(..., title="Total Price", ge=0, description="Total price of the article",)


class Receipt(BaseModel):
    name: str = Field(..., title="Name", max_length=250, description="Name of the OCR",)
    date: str = Field(..., title="Date", description="Date of the OCR",)
    articles: list[Article]
    total_price: float = Field(..., title="Total Price", ge=0, description="Total price of the OCR",)
