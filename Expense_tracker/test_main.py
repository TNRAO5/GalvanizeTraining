import unittest
from datetime import datetime
from main import viewAllExpenses

class TestExpenseTrackerController(unittest.TestCase):

    def setUp(self):
        # Initialize Expense_Tracker instance
        self.main = viewAllExpenses()

    def test_viewAllExpenses(self):

        try:
            self.main.viewAllExpenses()
            # self.main.addAnotherExpense()
        except Exception as e:
            self.fail(f"Unexpected exception occurred: {e}")

        # Optionally, you can add assertions here to verify the result if needed
        # For example:
        # expenses = self.controller.get_expenses()
        # self.assertEqual(len(expenses), 1, "Expense was not added correctly")

    # def test_add_another_expense_missing_fields(self):
    #     # Test with missing required fields  
    #     dateField = ""
    #     payee = ""
    #     description = ""
    #     amount = 0
    #     modeOfPayment = "Test"

    #     with self.assertRaises(ValueError):
    #         self.controller.add_another_expense(dateField,payee,description,amount,modeOfPayment)

    # def test_add_expense_invalid_date_format(self):
    #     # Test with invalid date format
    #     dateField = "2024-06-30" #Invalid Date 
    #     payee = ""
    #     description = ""
    #     amount = 0
    #     modeOfPayment = "Test"

    #     with self.assertRaises(ValueError):
    #         self.controller.add_another_expense(dateField,payee,description,amount,modeOfPayment)

    # def test_add_expense_unexpected_error(self):
    #     # Test unexpected error handling
    #     amount = "invalid_amount"  # Invalid amount type
    #     payee = "Miscellaneous"
    #     dateField = datetime.now().date()
    #     description = "Test"
    #     modeOfPayment = "Test"

    #     with self.assertRaises(Exception):
    #         self.controller.add_another_expense(dateField,payee,description,amount,modeOfPayment)

if __name__ == '__main__':
    unittest.main()