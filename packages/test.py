class Store():
    def __init__(self,name="",products=[]):
        self.name=name
        self.products=products
    
    def add_product (self, new_product):
        # for product in self.products:
        self.products.append(new_product)
        return self

    def sell_product (self, id):
        self.products.pop(id)    
        return self
    
    def show_all(self):
        for product in self.products:
            product.print_info()

class Product():
    def __init__(self,name="",price=0,category=""):
        self.name = name
        self.price = price
        self.category= category

    def update_price(self,percent_change=0, is_increased=False):
        if is_increased==True:
            self.price=self.price+(self.price*percent_change)
            return self
        else :
            self.price=self.price+(self.price*percent_change)
            return self

    def print_info (self):
        print(f"""
                Name: {self.name}
                Price: {self.price}
                Category: {self.category}
                """)
        return self        

store1=Store("My first store")
product1=Product("Jalapeño",100,"Comida Mexicana")
product2=Product("Tortillas",100,"Comida Mexicana")
product3=Product("Tabasco",100,"Comida Mexicana")
product4=Product("Lechuga",100,"Verduras")
product5=Product("Tomate",100,"Verduras")

store1.add_product(product1).add_product(product2).add_product(product3).add_product(product4).add_product(product5)
# store1.sell_product (0)
store1.show_all()

product1.print_info()
product1.update_price(0.07,True)
product1.print_info()
