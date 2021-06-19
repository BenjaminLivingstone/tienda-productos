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
        return self