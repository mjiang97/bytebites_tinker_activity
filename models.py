"""
ByteBites Backend Models

Four core classes for the ByteBites food ordering system:

1. Customer: Manages customer data including name and purchase history
2. MenuItem: Represents individual food items with price, category, and popularity rating
3. Menu: Maintains a collection of menu items and provides filtering/search functionality
4. Order: Groups selected items together and calculates total transaction cost
"""

from datetime import datetime
from typing import List, Optional


class Customer:
    """Represents a ByteBites customer with purchase history."""
    
    def __init__(self, name: str):
        self.name = name
        self.purchase_history: List['Order'] = []
    
    def __str__(self) -> str:
        return f"Customer(name={self.name}, purchases={len(self.purchase_history)})"
    
    def get_name(self) -> str:
        """Returns the customer's name."""
        return self.name
    
    def get_purchase_history(self) -> List['Order']:
        """Returns the list of all past orders."""
        return self.purchase_history
    
    def add_purchase(self, order: 'Order') -> None:
        """Adds an order to the customer's purchase history."""
        self.purchase_history.append(order)
    
    def is_valid_user(self) -> bool:
        """Returns True if customer has at least one purchase."""
        return len(self.purchase_history) > 0


class MenuItem:
    """Represents a food item on the menu."""
    
    def __init__(self, name: str, price: float, category: str, popularity_rating: float = 0.0):
        self.name = name
        self.price = price
        self.category = category
        self.popularity_rating = popularity_rating
    
    def __str__(self) -> str:
        return f"MenuItem(name={self.name}, price=${self.price:.2f}, category={self.category}, rating={self.popularity_rating})"
    
    def get_name(self) -> str:
        """Returns the item's name."""
        return self.name
    
    def get_price(self) -> float:
        """Returns the item's price."""
        return self.price
    
    def get_category(self) -> str:
        """Returns the item's category."""
        return self.category
    
    def get_popularity_rating(self) -> float:
        """Returns the item's popularity rating."""
        return self.popularity_rating
    
    def set_popularity_rating(self, rating: float) -> None:
        """Sets the item's popularity rating."""
        self.popularity_rating = rating


class Menu:
    """Manages a collection of menu items with filtering and sorting capabilities."""
    
    def __init__(self):
        self.items: List[MenuItem] = []
    
    def __str__(self) -> str:
        return f"Menu(items={len(self.items)})"
    
    def add_item(self, item: MenuItem) -> None:
        """Adds an item to the menu."""
        self.items.append(item)
    
    def remove_item(self, item: MenuItem) -> None:
        """Removes an item from the menu."""
        if item in self.items:
            self.items.remove(item)
    
    def get_items(self) -> List[MenuItem]:
        """Returns all items in the menu."""
        return self.items
    
    def get_items_by_category(self, category: str) -> List[MenuItem]:
        """Returns all items matching the specified category."""
        return [item for item in self.items if item.get_category() == category]
    
    def search_item(self, name: str) -> Optional[MenuItem]:
        """Searches for an item by name. Returns None if not found."""
        for item in self.items:
            if item.get_name().lower() == name.lower():
                return item
        return None
    
    def get_items_sorted_by_price(self, ascending: bool = True) -> List[MenuItem]:
        """Returns items sorted by price."""
        return sorted(self.items, key=lambda item: item.get_price(), reverse=not ascending)
    
    def get_items_sorted_by_popularity(self, ascending: bool = False) -> List[MenuItem]:
        """Returns items sorted by popularity rating."""
        return sorted(self.items, key=lambda item: item.get_popularity_rating(), reverse=not ascending)
    
    def get_items_sorted_by_name(self) -> List[MenuItem]:
        """Returns items sorted alphabetically by name."""
        return sorted(self.items, key=lambda item: item.get_name())
    
    def get_total_items(self) -> int:
        """Returns the total number of items in the menu."""
        return len(self.items)


class Order:
    """Represents a customer's transaction containing selected menu items."""
    
    def __init__(self, customer: Customer):
        self.customer = customer
        self.items: List[MenuItem] = []
        self.order_date = datetime.now()
    
    def __str__(self) -> str:
        return f"Order(customer={self.customer.get_name()}, items={len(self.items)}, total=${self.get_total_cost():.2f})"
    
    def add_item(self, item: MenuItem) -> None:
        """Adds an item to the order."""
        self.items.append(item)
    
    def remove_item(self, item: MenuItem) -> None:
        """Removes an item from the order."""
        if item in self.items:
            self.items.remove(item)
    
    def get_items(self) -> List[MenuItem]:
        """Returns all items in the order."""
        return self.items
    
    def get_total_cost(self) -> float:
        """Calculates and returns the total cost of the order."""
        return sum(item.get_price() for item in self.items)
    
    def get_order_date(self) -> datetime:
        """Returns the date and time the order was created."""
        return self.order_date
    
    def get_customer(self) -> Customer:
        """Returns the customer who placed the order."""
        return self.customer
    
    def get_item_count(self) -> int:
        """Returns the total number of items in the order."""
        return len(self.items)
    
    def get_average_item_price(self) -> float:
        """Returns the average price of items in the order."""
        if self.is_empty():
            return 0.0
        return self.get_total_cost() / self.get_item_count()
    
    def is_empty(self) -> bool:
        """Returns True if the order contains no items."""
        return len(self.items) == 0