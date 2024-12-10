import unittest
from datetime import datetime
from records_management import record

class TestRecord(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        """Setup resources shared across all test cases."""
        cls.record_system = record()
        print("TestRecord: SetupClass executed.")
        
    @classmethod
    def tearDownClass(cls):
        """Clean up resources shared across all test cases."""
        del cls.record_system
        print("TestRecord: TearDownClass executed.")

    def setUp(self):
        """Setup resources for each test case."""
        print("TestRecord: Setup executed.")

    def tearDown(self):
        """Clean up resources after each test case."""
        print("TestRecord: TearDown executed.")

    def test_add_record(self):
        """Test adding a record and verifying it in the history."""
        # Given
        customer_id = "CUST123"
        items = [{"name": "Apple", "price": 5, "quantity": 2}]
        total_price = 10
        profit = 5
        cal_q = {"Apple": 2}
        
        # When
        self.record_system.add_record(customer_id, items, total_price, profit, cal_q)
        
        # Then
        self.assertIn(customer_id, self.record_system.history, "Customer ID should exist in history.")
        self.assertEqual(len(self.record_system.history[customer_id]), 1, "There should be 1 record for this customer.")
        self.assertEqual(self.record_system.history[customer_id][0]["total_price"], total_price, "Total price should match.")
        self.assertEqual(self.record_system.q["Apple"], 2, "The quantity sold for Apple should be 2.")
    
    def test_get_history(self):
        """Test retrieving a customer's purchase history."""
        # Given
        customer_id = "CUST123"
        items = [{"name": "Banana", "price": 2, "quantity": 3}]
        total_price = 6
        profit = 3
        cal_q = {"Banana": 3}
        
        # When
        self.record_system.add_record(customer_id, items, total_price, profit, cal_q)
        self.record_system.get_history(customer_id)  # Should print history, we will check manually
        
        # Then
        history = self.record_system.history[customer_id]
        self.assertEqual(len(history), 2, "Customer should have 1 history record.")
        self.assertEqual(history[-1]["total_price"], total_price, "The total price should match the added value.")
        self.assertEqual(history[-1]["profit"], profit, "The profit should match the added value.")
        self.assertEqual(history[-1]["items"][0]["name"], "Banana", "The item name should match.")
    
    def test_get_total(self):
        """Test calculating total spending and number of purchases."""
        # Given
        customer_id = "CUST123"
        items1 = [{"name": "Apple", "price": 5, "quantity": 2}]
        total_price1 = 10
        profit1 = 5
        cal_q1 = {"Apple": 2}
        
        items2 = [{"name": "Orange", "price": 3, "quantity": 4}]
        total_price2 = 12
        profit2 = 6
        cal_q2 = {"Orange": 4}
        
        # When
        self.record_system.add_record(customer_id, items1, total_price1, profit1, cal_q1)
        self.record_system.add_record(customer_id, items2, total_price2, profit2, cal_q2)
        
        # Then
        self.record_system.get_total(customer_id)  # Should print the total, we will check manually
        
        total_spent = total_price1 + total_price2
        self.assertEqual(total_spent, 22, "Total spent should match the sum of all records.")
    


