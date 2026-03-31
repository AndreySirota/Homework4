"""Homework 12: bank_deposit"""


class Bank:
    """class Bank."""

    def __init__(self):
        """Сlass constructor."""
        self.clients = {}

    def register_client(self, client_id, name):
        """Register client with bank."""
        self.clients[client_id] = {
            "name": name,
            "start_balance": 0,
            "years": 0,
            "sum": 0
        }

    def open_deposit_account(self, client_id, start_balance, years):
        """Open deposit account."""
        if client_id not in self.clients:
            return
        self.clients[client_id]["start_balance"] = start_balance
        self.clients[client_id]["years"] = years
        self.clients[client_id]["sum"] = 0

    def calc_deposit_interest_rate(self, client_id):
        """calculate deposit interest rate."""
        if client_id not in self.clients:
            return False
        client = self.clients[client_id]
        if client["start_balance"] == 0 or client["years"] == 0:
            return False
        amount = client["start_balance"]
        months = 12
        for _ in range(client["years"]):
            for _ in range(months):
                amount += amount * 0.1 / 12
        return amount

    def close_deposit(self, client_id):
        """close deposit account."""
        if client_id not in self.clients:
            return False
        client = self.clients[client_id]
        if client["start_balance"] == 0 or client["years"] == 0:
            return False
        final_sum = self.calc_deposit_interest_rate(client_id)
        client["start_balance"] = 0
        client["years"] = 0
        client["sum"] = 0
        return final_sum


CLIENT_ID = "0000001"
CLIENT_ID2 = "0000002"
bank1 = Bank()
bank2 = Bank()
bank1.register_client(CLIENT_ID, "Andrey")
bank2.register_client(CLIENT_ID2, "Roman")
bank1.open_deposit_account(CLIENT_ID, 1000, 2)
bank2.open_deposit_account(CLIENT_ID2, 5000, 6)
final_amount1 = bank1.calc_deposit_interest_rate(CLIENT_ID)
final_amount2 = bank2.calc_deposit_interest_rate(CLIENT_ID2)
print(final_amount1)
print(final_amount2)
close_sum1 = bank1.close_deposit(CLIENT_ID)
close_sum2 = bank2.close_deposit(CLIENT_ID2)
print(close_sum1)
print(close_sum2)
