import sys
import os
# Ajustando o caminho para importar os módulos
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from sqlmodel import Field, SQLModel, Relationship
from typing import Optional
from datetime import date, datetime
from decimal import Decimal

# Modelando BD
class Subscription(SQLModel, table=True):
    __tablename__ = 'subscription'  
    __table_args__ = {'extend_existing': True}  
    id: int = Field(default=None, primary_key=True)
    empresa: str
    site: str
    data_assinatura: datetime
    valor_assinatura: Decimal

class Payments(SQLModel, table=True):
    id: int = Field(primary_key=True)
    subscription_id: int = Field(foreign_key='subscription.id')
    subscription: Subscription = Relationship()
    date: date
    amount: Decimal