from account import Account

class CurrentAccount(Account):
    def __init__(self):
        Account.__init__(self)

current = CurrentAccount()
current.deposit(500)
current.withdrawal(1000)
