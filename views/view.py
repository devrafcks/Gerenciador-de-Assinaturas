import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from sqlmodel import Session, select
from datetime import datetime
from models.model import Subscription, Payments
import matplotlib.pyplot as plt


# Serviço de Assinaturas
class SubscriptionService:
    def __init__(self, engine):
        self.engine = engine

    # Método que registra o pagamento
    def record_payment(self, subscription):
        # Cria um novo pagamento com dados de subscription
        payment = Payments(
            subscription_id=subscription.id,
            date=datetime.today(),
            amount=subscription.valor_assinatura
        )
        # Registra o pagamento no banco de dados
        with Session(self.engine) as session:
            session.add(payment)
            session.commit()
        print(f"Pagamento para a assinatura {subscription.empresa} registrado com sucesso.")
    
    def create(self, subscription: Subscription):
        with Session(self.engine) as session:
            session.add(subscription)
            session.commit()
            session.refresh(subscription)
            return subscription

    def get_by_id(self, subscription_id: int):
        with Session(self.engine) as session:
            return session.get(Subscription, subscription_id)

    def list_all(self):
        with Session(self.engine) as session:
            statement = select(Subscription)
            results = session.exec(statement).all()
        return results
    
    def delete(self, id):
        with Session(self.engine) as session:
            statement = select(Subscription).where(Subscription.id == id)
            result = session.exec(statement).one()
            session.delete(result)
            session.commit()
    
    def delete_payments(self, subscription):
        with Session(self.engine) as session:
            statement = select(Payments).where(Payments.subscription_id == subscription.id)
            payments = session.exec(statement).all()
            for payment in payments:
                session.delete(payment)
            session.commit()

    # Método para obter pagamentos de uma assinatura
    def get_payments(self, subscription: Subscription):
        with Session(self.engine) as session:
            statement = select(Payments).where(Payments.subscription_id == subscription.id)
            payments = session.exec(statement).all()
        return payments

    def pay(self, subscription: Subscription):
        with Session(self.engine) as session:
            statement = select(Payments).where(Payments.subscription_id == subscription.id)
            results = session.exec(statement).all()

            if self._has_payment_for_this_month(results):
                question = input('Essa conta já foi paga esse mês, deseja pagar novamente? Y ou N: ')
                if question.upper() != 'Y':
                    return
            
            payment = Payments(subscription_id=subscription.id, date=datetime.today(), amount=subscription.valor_assinatura)
            session.add(payment)
            session.commit()

    def total_value(self):
        with Session(self.engine) as session:
            statement = select(Subscription)
            results = session.exec(statement).all()
        return sum(result.valor_assinatura for result in results)

    def _get_last_12_months_native(self):
        today = datetime.now()
        return [(today.month - i - 1) % 12 + 1 for i in range(12)]

    def _get_values_for_months(self, last_12_months):
        with Session(self.engine) as session:
            statement = select(Payments)
            results = session.exec(statement).all()
            value_for_months = []
            for month in last_12_months:
                value = sum(float(payment.amount) for payment in results if payment.date.month == month)
                value_for_months.append(value)
        return value_for_months

    def gen_chart(self):
        last_12_months = self._get_last_12_months_native()
        values_for_months = self._get_values_for_months(last_12_months)

        plt.plot(last_12_months, values_for_months)
        plt.xlabel('Meses')
        plt.ylabel('Total Pago')
        plt.title('Total de Pagamentos por Mês nos Últimos 12 Meses')
        plt.show()

    def _has_payment_for_this_month(self, results):
        for result in results:
            if result.date.month == datetime.today().month:
                return True
        return False
