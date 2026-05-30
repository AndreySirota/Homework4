"""Homework 20: bank_deposit"""
import unittest
from bank_deposit import Bank
from logger_config import get_logger

logger = get_logger(__name__)


class TestBankInit(unittest.TestCase):
    """Creation of a bank"""

    def test_create_bank(self):
        """Create a bank instance"""
        logger.info("Test: creating a bank instance")
        bank = Bank()
        self.assertEqual(bank.clients, {})
        logger.debug("The bank has been successfully created: %s",
                     bank.clients)


class TestRegisterClient(unittest.TestCase):
    """Client registration"""

    def setUp(self):
        logger.info("=== Preparing registration tests ===")
        self.bank = Bank()
        logger.debug("Bank '%s' is created", self.bank)

    def test_register_client_adds_client(self):
        """Register a client and check fields"""
        logger.debug("Test: Register and add client")
        self.bank.register_client("001", "Alice")
        self.assertEqual(self.bank.clients["001"], {
            "name": "Alice",
            "start_balance": 0,
            "years": 0,
            "sum": 0
        })

    def test_register_multiple_clients(self):
        """Register several clients and verify them separately"""
        logger.debug("Test: Register multiple clients")
        self.bank.register_client("001", "Alice")
        self.bank.register_client("002", "Bob")
        self.assertEqual(self.bank.clients["001"], {
            "name": "Alice",
            "start_balance": 0,
            "years": 0,
            "sum": 0
        })
        self.assertEqual(self.bank.clients["002"], {
            "name": "Bob",
            "start_balance": 0,
            "years": 0,
            "sum": 0
        })


class TestOpenDepositAccount(unittest.TestCase):
    """Opening a deposit account tests"""

    def setUp(self):
        logger.info("=== Preparing opening a deposit account tests ===")
        self.bank = Bank()
        self.bank.register_client("001", "Test")
        logger.debug("Bank and client ready")

    def test_open_deposit_for_existing_client(self):
        """Opening deposit for existing client updates fields"""
        logger.debug("Test: Opening deposit for existing client")
        self.bank.open_deposit_account("001", 5000, 3)
        self.assertEqual(self.bank.clients["001"], {
            "name": "Test",
            "start_balance": 5000,
            "years": 3,
            "sum": 0
        })

    def test_open_deposit_for_nonexistent_client(self):
        """Opening deposit for nonexistent client does nothing"""
        logger.debug("Test: Opening deposit for nonexisting client")
        clients_before = self.bank.clients.copy()
        self.assertIsNone(self.bank.open_deposit_account("999", 5000, 3))
        self.assertEqual(self.bank.clients, clients_before)
        logger.debug("Clients unchanged: %s", self.bank.clients)


class TestCalcDepositInterestRate(unittest.TestCase):
    """Interest calculation tests"""

    def setUp(self):
        logger.info("=== Preparing interest calculation tests ===")
        self.bank = Bank()
        self.bank.register_client("001", "Test")
        logger.debug("Bank and client ready")

    def test_calc_returns_correct_amount(self):
        """Calculation for 1 year gives ~1104.71"""
        logger.debug("Test: Calc returns correct amount")
        self.bank.open_deposit_account("001", 1000, 1)
        result = self.bank.calc_deposit_interest_rate("001")
        logger.debug("Result: %s", result)
        self.assertAlmostEqual(result, 1104.71, places=2)

    def test_calc_for_nonexistent_client(self):
        """Nonexistent client returns False"""
        logger.debug("Test: Calc with nonexistent client")
        result = self.bank.calc_deposit_interest_rate("999")
        logger.debug("Result: %s", result)
        self.assertFalse(result)

    def test_calc_with_zero_balance(self):
        """Zero balance leads to False"""
        logger.debug("Test: Calc with zero balance")
        self.bank.open_deposit_account("001", 0, 1)
        result = self.bank.calc_deposit_interest_rate("001")
        logger.debug("Result: %s", result)
        self.assertFalse(result)

    def test_calc_with_zero_years(self):
        """Zero years leads to False"""
        logger.debug("Test: Calc with zero years")
        self.bank.open_deposit_account("001", 1000, 0)
        result = self.bank.calc_deposit_interest_rate("001")
        logger.debug("Result: %s", result)
        self.assertFalse(result)

    def test_calc_different_period(self):
        """Calculation for 2 years gives ~1220.39"""
        logger.debug("Test: Calc different period")
        self.bank.open_deposit_account("001", 1000, 2)
        result = self.bank.calc_deposit_interest_rate("001")
        logger.debug("Result: %s", result)
        self.assertAlmostEqual(result, 1220.39, places=2)


class TestCloseDeposit(unittest.TestCase):
    """Closing the deposit"""

    def setUp(self):
        logger.info("=== Preparing close deposit tests ===")
        self.bank = Bank()
        self.bank.register_client("001", "Test")
        self.bank.open_deposit_account("001", 2000, 2)
        logger.debug("Client 001 ready with deposit 2000 for 2 years")

    def test_close_deposit_returns_sum_and_clears(self):
        """Close returns correct sum and zeroes the fields"""
        logger.debug("Test: Close deposit returns sum and clears")
        expect = self.bank.calc_deposit_interest_rate("001")
        result = self.bank.close_deposit("001")
        logger.debug("Expected %s, Got %s", expect, result)
        self.assertEqual(result, expect)
        self.assertEqual(self.bank.clients["001"], {
            "name": "Test",
            "start_balance": 0,
            "years": 0,
            "sum": 0
        })

    def test_close_deposit_nonexistent_client(self):
        """Nonexistent client returns False"""
        logger.debug("Test: Close deposit nonexistent client")
        result = self.bank.close_deposit("999")
        logger.debug("Result: %s", result)
        self.assertFalse(result)

    def test_close_deposit_already_closed(self):
        """Second close returns False"""
        logger.debug("Test: Close deposit already closed")
        result = self.bank.close_deposit("001")
        logger.debug("Result: %s", result)
        self.assertNotEqual(result, False)
        result2 = self.bank.close_deposit("001")
        logger.debug("Result2: %s", result2)
        self.assertFalse(result2)

    def test_close_deposit_without_open_deposit(self):
        """Client without opened deposit returns False"""
        logger.debug("Test: Close deposit without open deposit")
        self.bank.register_client("002", "Alex")
        result = self.bank.close_deposit("002")
        logger.debug("Result: %s", result)
        self.assertFalse(result)


class TestBankIntegration(unittest.TestCase):
    """Integration tests"""

    def setUp(self):
        logger.info("=== Preparing bank integration tests ===")
        self.bank = Bank()
        self.bank.register_client("001", "Test")
        self.bank.register_client("002", "Alex")
        logger.debug("Two clients registered")

    def test_full_lifecycle(self):
        """Complete flow: open, calculate, close, repeated operations"""
        logger.debug("Test: Full lifecycle")
        self.bank.open_deposit_account("001", 1000, 1)
        result = self.bank.calc_deposit_interest_rate("001")
        logger.debug("Calculated result: %s", result)
        self.assertAlmostEqual(result, 1104.71, places=2)

        result2 = self.bank.close_deposit("001")
        logger.debug("Close result2: %s", result2)
        self.assertEqual(result2, result)
        self.assertEqual(self.bank.clients["001"], {
            "name": "Test",
            "start_balance": 0,
            "years": 0,
            "sum": 0
        })

        self.assertFalse(self.bank.calc_deposit_interest_rate("001"))
        self.assertFalse(self.bank.close_deposit("001"))

    def test_multiple_clients_independence(self):
        """Closing one deposit does not affect another client"""
        logger.debug("Test: Multiple clients independence")
        self.bank.open_deposit_account("001", 2000, 3)
        self.bank.open_deposit_account("002", 5000, 1)

        result = self.bank.calc_deposit_interest_rate("002")
        logger.debug("Result: %s", result)
        self.bank.close_deposit("001")

        self.assertEqual(self.bank.clients["002"]["start_balance"], 5000)
        self.assertEqual(self.bank.clients["002"]["years"], 1)
        self.assertEqual(self.bank.clients["002"]["sum"], 0)

        result2 = self.bank.calc_deposit_interest_rate("002")
        logger.debug("Result2: %s", result2)
        self.assertAlmostEqual(result2, result, places=2)


if __name__ == '__main__':
    unittest.main()
