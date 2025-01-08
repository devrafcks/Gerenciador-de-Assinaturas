import sys
import os
# Ajustando o caminho para importar os módulos
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from datetime import datetime, date
from decimal import Decimal
from models.database import engine
from views.view import SubscriptionService
from models.model import Subscription, Payments


class UI:
    def __init__(self):
        self.subscription_service = SubscriptionService(engine)
        
    def start(self):
        while True:
            print(''' 
            [1] -> Adicionar assinatura
            [2] -> Remover assinatura
            [3] -> Valor total
            [4] -> Gastos últimos 12 meses
            [5] -> Pagar assinatura
            [6] -> Sair
            ''')
            choice = input('Escolha uma opção: ')
            if not choice.isdigit() or int(choice) not in [1, 2, 3, 4, 5, 6]:
                print("Opção inválida. Tente novamente.")
                continue

            choice = int(choice)
            if choice == 1:
                self.add_subscription()
            elif choice == 2:
                self.delete_subscription()
            elif choice == 3:
                self.total_value()
            elif choice == 4:
                self.subscription_service.gen_chart()
            elif choice == 5:
                self.pay_subscription()  
            else:
                break
    
    def add_subscription(self):
        empresa = input('Empresa: ')
        site = input('Site: ')
        data_assinatura = input('Data de assinatura (dd/mm/aaaa): ')
        
        # Validação da data
        try:
            data_assinatura = datetime.strptime(data_assinatura, '%d/%m/%Y')
        except ValueError:
            print("Data inválida. O formato correto é dd/mm/aaaa.")
            return
        
        valor = input('Valor: ')
        try:
            valor = Decimal(valor)
        except ValueError:
            print("Valor inválido. Insira um número válido.")
            return
        
        # Criação da assinatura
        subscription = Subscription(empresa=empresa, site=site, data_assinatura=data_assinatura, valor_assinatura=valor)
        self.subscription_service.create(subscription)
        print('Assinatura adicionada com sucesso.')
        self.wait_for_input()
        
    def delete_subscription(self):
        subscriptions = self.subscription_service.list_all()
        print('Escolha qual assinatura deseja excluir')
        for i in subscriptions:
            print(f'[{i.id}] -> {i.empresa}')
        
        choice = input('Escolha a assinatura: ')
        try:
            choice = int(choice)
        except ValueError:
            print("Opção inválida. Tente novamente.")
            return

        subscription = self.subscription_service.get_by_id(choice)
        
        if subscription:
            # Exclui os pagamentos associados antes de excluir a assinatura
            self.subscription_service.delete_payments(subscription)
            self.subscription_service.delete(choice)
            print('Assinatura e pagamentos excluídos com sucesso.')
        else:
            print("Assinatura não encontrada.")
        self.wait_for_input()
                
    def total_value(self):
        total = self.subscription_service.total_value()
        print(f'Seu valor total mensal em assinaturas: {total:.2f}')  # Exibe o valor formatado com 2 casas decimais
        self.wait_for_input()

    def pay_subscription(self):
        subscriptions = self.subscription_service.list_all()  # Lista as assinaturas
        print('Escolha a assinatura que deseja pagar:')
        for i in subscriptions:
            print(f'[{i.id}] -> {i.empresa}')

        choice = input('Escolha a assinatura: ')
        try:
            choice = int(choice)
        except ValueError:
            print("Opção inválida. Tente novamente.")
            return

        subscription = self.subscription_service.get_by_id(choice)
        
        if subscription:
            # Checando se o pagamento já foi feito para o mês atual
            payments = self.subscription_service.get_payments(subscription)  # Chama get_payments agora
            if self._has_payment_for_this_month(payments):
                print(f"Já existe um pagamento registrado para o mês atual para a assinatura {subscription.empresa}.")
                return

            # Passa o engine diretamente para o método pay
            self.pay(subscription)
        else:
            print("Assinatura não encontrada.")
        self.wait_for_input()
    
    def pay(self, subscription):
        """
        Registra o pagamento da assinatura.
        """
        print(f"Pagando a assinatura {subscription.empresa}")
        self.subscription_service.record_payment(subscription)  
        
    def _has_payment_for_this_month(self, payments):
        """
        Verifica se já existe um pagamento realizado para o mês atual.
        """
        today = date.today()
        return any(payment.date.month == today.month and payment.date.year == today.year for payment in payments)
        
    def wait_for_input(self):
        input("Pressione Enter para voltar ao menu principal...")

if __name__ == '__main__':
    UI().start()
