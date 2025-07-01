class BankAccount:
    def __init__(self, owner: str, balance: float = 0.0):
        self._owner = owner
        self._balance = balance

    def deposit(self, amt: float) -> None:
        if amt <= 0:
            raise ValueError("Deposit must be positive")
        self._balance += amt

    def withdraw(self, amt: float) -> float:
        if amt <= 0:
            raise ValueError("Withdraw must be positive")
        if amt > self._balance:
            raise ValueError("Insufficient funds")
        self._balance -= amt
        return amt

    def balance(self) -> float:
        return self._balance