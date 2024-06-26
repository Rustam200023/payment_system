from pydantic import BaseModel


# Класс для валидации добавления карты
class CardAddModel(BaseModel):
    user_id: int
    card_number: int
    balance: float
    card_name: str
    exp_date: int
    cvv: int