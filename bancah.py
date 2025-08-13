class ContaBancaria:
    """Classe que rmostra uma conta bancária, com historico de depósito, saque e consulta de saldo."""
    
    def __init__(self, titular, saldo=0):
        """
        Nova conta bancária.
        
        Parâmetros:
        titular (str): Nome do titular da conta.
        saldo (float): Saldo inicial da conta. Padrão é 0.
        """
        self.__titular = titular  # Nome do titular (privado)
        self.__saldo = saldo      # Saldo atual da conta (privado)

    def depositar(self, valor):
        """
        Realiza depósito na conta.

        Parâmetros:
        valor (float): Valor a ser depositado. Deve ser positivo.

        Retorno:
        Nenhum retorno, apenas exibe uma mensagem de confirmação.
        """
        if valor > 0:
            self.__saldo += valor  # Adiciona o valor ao saldo atual
            print(f"Deposito de R${valor} realizado! Novo Saldo: R${self.__saldo}")

    def sacar(self, valor):
        """
        Realiza saque na conta, se houver saldo suficiente.

        Parâmetros:
        valor (float): Valor a ser sacado. Deve ser positivo e menor ou igual o saldo.

        Retorno:
        Nenhum retorno, mostra uma mensagem de confirmação.
        """
        if 0 < valor <= self.__saldo:
            self.__saldo -= valor  # Subtrai o valor do saldo atual
            print(f"Saque de R${valor} realizado! Novo Saldo: R${self.__saldo}, Saldo atual da conta {self.__titular}: R${self.__saldo}")

    def get_saldo(self):
        """
        Exibe o saldo atual da conta.

        Retorno:
        Nenhum. Apenas imprime o saldo no console.
        """
        print(f"Seu saldo é: R${self.__saldo}")


# Criação de uma instância da ContaBancaria com titular 'Nicole' e saldo inicial de R$1000
Nicole = ContaBancaria("Nicole", 1000)

# Depósito de R$500 na conta de Nicole
Nicole.depositar(500)

# Saque de R$200 da conta de Nicole
Nicole.sacar(200)