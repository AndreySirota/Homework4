"""Homework 21: test_bank_deposit"""


import pytest
from source.bank_deposit import Bank


@pytest.fixture
def bank():
    """Creating a new bank for each test."""
    return Bank()


@pytest.fixture
def client_id():
    """Creating a client id for each test."""
    return 1


@pytest.fixture
def name():
    """Creating a client's name for each test."""
    return "Ivan"


@pytest.fixture
def registered_bank(bank, client_id, name):
    """A bank with an already registered client."""
    bank.register_client(client_id, name)
    return bank


class TestRegisterClient:
    """Client registration tests."""

    def test_register_new_client(self, bank,
                                 client_id, name, loguru_logger):
        """Positive test: new client registration."""
        loguru_logger.info("New client registration")
        bank.register_client(client_id, name)
        assert client_id in bank.clients
        assert bank.clients[client_id]["name"] == name
        assert bank.clients[client_id]["start_balance"] == 0
        assert bank.clients[client_id]["years"] == 0
        assert bank.clients[client_id]["sum"] == 0

    def test_register_existing_client_overwrites(
            self, bank, client_id, name, loguru_logger):
        """Negative test: re-registration overwrites data."""
        loguru_logger.warning("Overwriting an existing client")
        bank.register_client(client_id, "Old")
        bank.register_client(client_id, name)
        assert bank.clients[client_id]["name"] == name
        assert bank.clients[client_id]["start_balance"] == 0


class TestOpenDepositAccount:
    """Tests for opening a deposit account."""

    def test_open_for_existing_client(self, registered_bank,
                                      client_id, loguru_logger):
        """Positive test: opening a deposit for an existing client."""
        loguru_logger.info("Opening a deposit for an existing client")
        registered_bank.open_deposit_account(client_id, 1000, 2)
        client = registered_bank.clients[client_id]
        assert client["start_balance"] == 1000
        assert client["years"] == 2
        assert client["sum"] == 0

    def test_open_for_unregistered_client_no_error(self, bank,
                                                   loguru_logger):
        """Negative test: trying to open
        an account for an unregistered client"""
        loguru_logger.info("Attempt to open a "
                           "deposit for an unregistered client")
        bank.open_deposit_account(999, 500, 1)
        assert 999 not in bank.clients


class TestCalcDepositInterestRate:
    """Interest rate calculation tests."""

    def test_calc_for_valid_deposit(self, registered_bank,
                                    client_id, loguru_logger):
        """Positive test: calculation for an open deposit."""
        loguru_logger.info("Calculation of interest on a deposit")
        registered_bank.open_deposit_account(client_id, 1000, 2)
        result = registered_bank.calc_deposit_interest_rate(client_id)
        expected = 1000 * (1 + 0.1 / 12) ** (2 * 12)
        assert abs(result - expected) < 0.01

    def test_calc_unregistered_client(self, bank, loguru_logger):
        """Negative test: calculation for an
         unregistered client returns False."""
        loguru_logger.warning("Calculation for an unregistered client")
        assert bank.calc_deposit_interest_rate(123) is False

    def test_calc_with_zero_balance_or_years(self, registered_bank,
                                             client_id, loguru_logger):
        """Negative test: deposit isn't open"""
        loguru_logger.info("Payment without an open deposit")
        result = registered_bank.calc_deposit_interest_rate(client_id)
        assert result is False


class TestCloseDeposit:
    """Deposit closing tests."""

    def test_close_valid_deposit(self, registered_bank,
                                 client_id, loguru_logger):
        """Positive test: closing an open deposit
        returns the final amount."""
        loguru_logger.info("Closing the deposit")
        registered_bank.open_deposit_account(client_id, 2000, 1)
        expected = 2000 * (1 + 0.1 / 12) ** 12
        final = registered_bank.close_deposit(client_id)
        assert abs(final - expected) < 0.01
        client = registered_bank.clients[client_id]
        assert client["start_balance"] == 0
        assert client["years"] == 0
        assert client["sum"] == 0

    def test_close_unregistered_client(self, bank, loguru_logger):
        """Negative test: close for an unregistered client"""
        loguru_logger.warning("Closing a deposit "
                              "for an unregistered client")
        assert bank.close_deposit(42) is False

    def test_close_without_open_deposit(self, registered_bank,
                                        client_id, loguru_logger):
        """Negative test: closing without open deposit"""
        loguru_logger.info("Closing an unopened deposit")
        assert registered_bank.close_deposit(client_id) is False
