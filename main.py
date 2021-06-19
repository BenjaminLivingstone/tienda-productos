from packages.products import Product  #* agrega todas las classes dentre del archivo.
from packages.store import Store


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

# while True:
#     print()
#     if

# # Asignatura: Tienda y Productos
# # Objetivos:
# # Practica creando clases
# # Practicar asociaciones entre clases
# # Practica el código de modularización
# # Comienza creando una clase de Tienda que tenga 2 atributos: un nombre y una lista de productos. El nombre debe proporcionarse en el momento de la creación, pero la lista de productos debe estar vacía.

# class Store():
#     def __init__(self,name="",products=[]):
#         self.name=name
#         self.products=products
    
#     def add_product (self, new_product):
        
#         self.products.append(new_product)
#         return self

#     def sell_product (self, id):
#         self.products.pop(id)    
#         return self

# # A continuación, crea una clase de Producto que tenga 3 atributos: un nombre, un precio y una categoría. Todo esto debe proporcionarse en el momento de la creación.

# class Product():
#     def __init__(self,name="",price=0,category=""):
#         self.name = name
#         self.price = price
#         self.category= category

# # Veamos algunos métodos para nuestra clase de producto:

# # update_price(self, percent_change, is_increased) : actualiza el precio del producto. Si is_increased es True, el precio debería aumentar en el porcentaje de cambio proporcionado. Si es False, el precio debe disminuir en el cambio porcentual proporcionado.
# # print_info (self) : imprime el nombre del producto, su categoría y su precio.

#     def update_price(self,percent_change=0, is_increased=False):
#         if is_increased==True:
#             self.price=self.price+(self.price*percent_change)
#             return self
#         else :
#             self.price=self.price+(self.price*percent_change)
#             return self

#     def print_info (self):
#         print(f"""
#                 Name: {self.name}
#                 Price: {self.price}
#                 Category: {self.category}
#                 """)
#         return self        

# store1=Store("My first store")
# product1=Product("Jalapeño",100,"Food")

# store1.add_product ("Beef Jerky")
# store1.add_product ("Soy Sauce") 
# store1.sell_product (0)
# print(store1.products)

# product1.print_info()

# product1.update_price(0.07,True)
# product1.print_info()



# # También demos algunos métodos a nuestra clase Store:

# # add_product (self, new_product) : toma un producto y lo agrega a la tienda
# # sell_product (self, id) : elimina el producto de la lista de productos de la tienda dada la identificación (suponga que id es el índice del producto en la lista) e imprima su información.
# # inflation(self, percent_increase) : aumenta el precio de cada producto por el percent_increase dado (¡use el método que escribió en la clase Product!)
# # set_clearance (self, category, percent_discount) : actualiza todos los productos que coinciden con la categoría dada reduciendo el precio en el percent_discount dado (¡use el método que escribió en la clase Product!)
# #  Crear una clase de tienda con 2 atributos
# #  Crear una clase de producto con 3 atributos
# #  Agrega el método print_info a la clase de Producto
# #  Agrega el método update_price a la clase Product
# #  Agrega el método add_product a la clase Store
# #  Agrega el método sell_product a la clase Store
# #  Prueba tus clases creando una instancia de la Tienda y algunas instancias de la clase Producto, agrega esas instancias a la instancia de la tienda y luego prueba los métodos.
# #  NINJA BONUS: Agregue el método de inflación a la clase Store
# #  NINJA BONUS: Agregue el método set_clearance a la clase Store
# #  NINJA BONUS: modularice su código en 3 archivos separados
# #  SENSEI BONUS: actualice la clase de producto para dar a cada producto una identificación única. Actualice el método sell_product para aceptar la identificación única.