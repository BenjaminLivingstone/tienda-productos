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
        print(f"Product: {self.name}, Price: {self.price}, Category: {self.category}")
        return self        

