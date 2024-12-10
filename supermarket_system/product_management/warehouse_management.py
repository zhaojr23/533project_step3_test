class warehouse():
    """
    A class to represent a warehouse and manage its inventory.

    Attributes:
    ----------
    products: dict
        A dictionary containing product details such as ID, name, category, purchase price, entry date, and quantity.
    
    Methods:
    ---------
    add_product(self, productId, productname, category, purchaseprice, entrydate, quantity):
        Adds a product to the warehouse or updates the quantity if the product already exists.
    remove_product(self, productId, quantity):
        Removes a specified quantity of a product from the warehouse. If the quantity becomes zero, 
        the product is removed from the inventory.
    display(self):
        Displays the details of all products currently in the warehouse.

    """
    def __init__(self):
        self.products={}
    def add_product(self,productId, productname, category, purchaseprice, entrydate, quantity):
        if productId in self.products:
            self.products[productId]["quantity"] += quantity
        else:
            self.products[productId]={
                "name": productname,
                "category": category,
                "pprice" : purchaseprice,
                "edate" : entrydate,
                "quantity" : quantity
            }
    def remove_product(self, productId, quantity):
        if productId in self.products and self.products[productId]["quantity"] >= quantity:
            self.products[productId]["quantity"] -= quantity
            if self.products[productId]["quantity"] == 0:
                del self.products[productId]
        else:
            print("There is no this product or the quantity is greater than the quantity in warehouse")
    def display(self):
        for id, product in self.products.items():
            print(id, product['name'], product['category'], product['pprice'], product['edate'], product['quantity'])

        
            