#!/usr/bin/env python
# coding: utf-8

# In[4]:


import time

class Product:
    def __init__(self, ID, name, price, category):
        self.ID = ID
        self.name = name
        self.price = price
        self.category = category

def load_data(file_name):
    products = []
    with open(file_name, 'r') as file:
        for line in file:
            data = line.strip().split(',')
            product = Product(data[0], data[1], float(data[2]), data[3])
            products.append(product)
    print("Loaded data:")
    for product in products:
        print(f"ID: {product.ID}, Name: {product.name}, Price: {product.price}, Category: {product.category}")
    
    return products

def insert_product(products, new_product):
    products.append(new_product)
    print("New product inserted \n")

def update_product(products, product_id, new_price):
    for product in products:
        if product.ID == product_id:
            product.price = new_price
            print("Product price updated \n")

def delete_product(products, product_id):
    products[:] = [product for product in products if product.ID != product_id]
    print("Product deleted \n")
    
def bubble_sort_by_price(products):
    n = len(products)
    for i in range(n):
        for j in range(0, n-i-1):
            if products[j].price > products[j+1].price:
                products[j], products[j+1] = products[j+1], products[j]

def search_product_by_id(products, product_id):
    for product in products:
        if product.ID == product_id:
            return product
    return None

def main():
    # Load data from file
    products = load_data("product_data.txt")
    

    # Perform sorting and measure time
    start_time = time.time()
    bubble_sort_by_price(products)
    end_time = time.time()
    print("\nTime taken to sort:", end_time - start_time, "seconds \n")
    
    # Perform sorting on reverse sorted data and measure time
    products.reverse()
    start_time = time.time()
    bubble_sort_by_price(products)
    end_time = time.time()
    print("Time taken to sort reverse sorted data:", end_time - start_time, "seconds \n")
    
    # Perform sorting on already sorted data and measure time
    start_time = time.time()
    bubble_sort_by_price(products)
    end_time = time.time()
    print("Time taken to sort already sorted data:", end_time - start_time, "seconds \n")

    # Perform search
    product_id_to_search = "57353"
    found_product = search_product_by_id(products, product_id_to_search)
    if found_product:
        print("Product found:", found_product.name, "\n")
    else:
        print("Product not found \n")

    # Perform insert
    new_product = Product("89456", "Twilight", 17.99, "Books")
    insert_product(products, new_product)

    # Perform update
    product_id_to_update = "34863"
    new_price = 15.99
    update_product(products, product_id_to_update, new_price)

    # Perform delete
    product_id_to_delete = "97895"
    delete_product(products, product_id_to_delete)
    

if __name__ == "__main__":
    main()


# In[ ]:





# In[ ]:




