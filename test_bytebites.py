"""
Test suite for ByteBites food ordering system.

Tests cover core functionality:
- Order total calculations
- Empty order handling
- Menu filtering and sorting
- Customer purchase history
"""

import pytest
from models import Customer, MenuItem, Menu, Order


class TestOrder:
    """Tests for Order class - transaction and cost calculations."""
    
    def test_calculate_total_with_multiple_items(self):
        """Verify that order total equals sum of all item prices."""
        customer = Customer("Alice")
        order = Order(customer)
        
        burger = MenuItem("Spicy Burger", 12.50, "Main")
        soda = MenuItem("Large Soda", 5.00, "Drinks")
        fries = MenuItem("Fries", 3.50, "Sides")
        
        order.add_item(burger)
        order.add_item(soda)
        order.add_item(fries)
        
        assert order.get_total_cost() == 21.00
    
    def test_order_total_is_zero_when_empty(self):
        """Verify that an empty order has total cost of zero."""
        customer = Customer("Bob")
        order = Order(customer)
        
        assert order.get_total_cost() == 0.0
        assert order.is_empty() is True
    
    def test_order_item_count(self):
        """Verify that item count matches number of added items."""
        customer = Customer("Charlie")
        order = Order(customer)
        
        pizza = MenuItem("Pepperoni Pizza", 15.00, "Main")
        order.add_item(pizza)
        order.add_item(pizza)
        
        assert order.get_item_count() == 2
    
    def test_average_item_price(self):
        """Verify that average item price is calculated correctly."""
        customer = Customer("Diana")
        order = Order(customer)
        
        cheap = MenuItem("Water", 2.00, "Drinks")
        expensive = MenuItem("Lobster", 28.00, "Main")
        
        order.add_item(cheap)
        order.add_item(expensive)
        
        assert order.get_average_item_price() == 15.00
    
    def test_remove_item_from_order(self):
        """Verify that items can be removed and total updates correctly."""
        customer = Customer("Eve")
        order = Order(customer)
        
        burger = MenuItem("Burger", 10.00, "Main")
        order.add_item(burger)
        
        assert order.get_total_cost() == 10.00
        
        order.remove_item(burger)
        
        assert order.get_total_cost() == 0.0
        assert order.is_empty() is True


class TestMenu:
    """Tests for Menu class - filtering and sorting functionality."""
    
    def setup_method(self):
        """Set up a menu with sample items for each test."""
        self.menu = Menu()
        
        self.menu.add_item(MenuItem("Spicy Burger", 12.50, "Main", 4.8))
        self.menu.add_item(MenuItem("Veggie Burger", 11.00, "Main", 4.5))
        self.menu.add_item(MenuItem("Large Soda", 5.00, "Drinks", 4.2))
        self.menu.add_item(MenuItem("Iced Tea", 4.50, "Drinks", 3.9))
        self.menu.add_item(MenuItem("Chocolate Cake", 8.00, "Desserts", 4.9))
        self.menu.add_item(MenuItem("Ice Cream", 6.50, "Desserts", 4.7))
    
    def test_filter_items_by_category(self):
        """Verify that filtering 'Drinks' category only returns liquid items."""
        drinks = self.menu.get_items_by_category("Drinks")
        
        assert len(drinks) == 2
        assert all(item.get_category() == "Drinks" for item in drinks)
        assert any(item.get_name() == "Large Soda" for item in drinks)
    
    def test_filter_main_dishes(self):
        """Verify that filtering 'Main' category returns main courses only."""
        mains = self.menu.get_items_by_category("Main")
        
        assert len(mains) == 2
        assert "Spicy Burger" in [item.get_name() for item in mains]
        assert "Veggie Burger" in [item.get_name() for item in mains]
    
    def test_filter_empty_category(self):
        """Verify that filtering non-existent category returns empty list."""
        sides = self.menu.get_items_by_category("Sides")
        
        assert len(sides) == 0
    
    def test_search_item_by_name(self):
        """Verify that searching finds the correct item."""
        item = self.menu.search_item("Spicy Burger")
        
        assert item is not None
        assert item.get_name() == "Spicy Burger"
        assert item.get_price() == 12.50
    
    def test_search_item_case_insensitive(self):
        """Verify that item search is case-insensitive."""
        item = self.menu.search_item("spicy burger")
        
        assert item is not None
        assert item.get_name() == "Spicy Burger"
    
    def test_search_nonexistent_item(self):
        """Verify that searching for non-existent item returns None."""
        item = self.menu.search_item("Nonexistent Dish")
        
        assert item is None
    
    def test_sort_items_by_price_ascending(self):
        """Verify that items are sorted by price from lowest to highest."""
        sorted_items = self.menu.get_items_sorted_by_price(ascending=True)
        prices = [item.get_price() for item in sorted_items]
        
        assert prices == sorted(prices)
        assert prices[0] == 4.50  # Iced Tea
        assert prices[-1] == 12.50  # Spicy Burger
    
    def test_sort_items_by_price_descending(self):
        """Verify that items are sorted by price from highest to lowest."""
        sorted_items = self.menu.get_items_sorted_by_price(ascending=False)
        prices = [item.get_price() for item in sorted_items]
        
        assert prices == sorted(prices, reverse=True)
        assert prices[0] == 12.50  # Spicy Burger
        assert prices[-1] == 4.50  # Iced Tea
    
    def test_sort_items_by_popularity(self):
        """Verify that items are sorted by popularity rating (highest first)."""
        sorted_items = self.menu.get_items_sorted_by_popularity(ascending=False)
        ratings = [item.get_popularity_rating() for item in sorted_items]
        
        assert ratings == sorted(ratings, reverse=True)
        assert sorted_items[0].get_name() == "Chocolate Cake"  # 4.9
        assert sorted_items[-1].get_name() == "Iced Tea"  # 3.9
    
    def test_sort_items_by_name(self):
        """Verify that items are sorted alphabetically by name."""
        sorted_items = self.menu.get_items_sorted_by_name()
        names = [item.get_name() for item in sorted_items]
        
        assert names == sorted(names)
        assert names[0] == "Chocolate Cake"
        assert names[-1] == "Veggie Burger"
    
    def test_total_items_in_menu(self):
        """Verify that menu correctly counts total items."""
        assert self.menu.get_total_items() == 6
    
    def test_remove_item_from_menu(self):
        """Verify that items can be removed from menu."""
        burger = self.menu.search_item("Spicy Burger")
        self.menu.remove_item(burger)
        
        assert self.menu.get_total_items() == 5
        assert self.menu.search_item("Spicy Burger") is None


class TestCustomer:
    """Tests for Customer class - user validation and purchase history."""
    
    def test_valid_user_with_purchases(self):
        """Verify that customer with purchases is a valid user."""
        customer = Customer("Frank")
        order = Order(customer)
        
        order.add_item(MenuItem("Burger", 10.00, "Main"))
        customer.add_purchase(order)
        
        assert customer.is_valid_user() is True
    
    def test_invalid_user_without_purchases(self):
        """Verify that customer without purchases is not a valid user."""
        customer = Customer("Grace")
        
        assert customer.is_valid_user() is False
    
    def test_purchase_history_tracking(self):
        """Verify that all customer purchases are tracked in history."""
        customer = Customer("Henry")
        
        order1 = Order(customer)
        order1.add_item(MenuItem("Burger", 10.00, "Main"))
        customer.add_purchase(order1)
        
        order2 = Order(customer)
        order2.add_item(MenuItem("Pizza", 15.00, "Main"))
        customer.add_purchase(order2)
        
        history = customer.get_purchase_history()
        assert len(history) == 2
        assert order1 in history
        assert order2 in history


class TestIntegration:
    """Integration tests combining multiple components."""
    
    def test_complete_ordering_flow(self):
        """Test a complete flow: create menu, filter items, create order, place order."""
        # Set up menu
        menu = Menu()
        menu.add_item(MenuItem("Spicy Burger", 12.50, "Main", 4.8))
        menu.add_item(MenuItem("Large Soda", 5.00, "Drinks", 4.2))
        menu.add_item(MenuItem("Chocolate Cake", 8.00, "Desserts", 4.9))
        
        # Customer browses and creates order
        customer = Customer("Isabella")
        order = Order(customer)
        
        # Add items from menu
        burger = menu.search_item("Spicy Burger")
        soda = menu.search_item("Large Soda")
        cake = menu.search_item("Chocolate Cake")
        
        order.add_item(burger)
        order.add_item(soda)
        order.add_item(cake)
        
        # Complete order
        customer.add_purchase(order)
        
        # Verify final state
        assert order.get_total_cost() == 25.50
        assert customer.is_valid_user() is True
        assert len(customer.get_purchase_history()) == 1
