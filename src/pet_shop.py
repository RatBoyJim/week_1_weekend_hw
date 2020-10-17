# WRITE YOUR FUNCTIONS HERE
def get_pet_shop_name(pet_shop):
    return pet_shop["name"]
    
def get_total_cash(pet_shop):
    return pet_shop["admin"]["total_cash"]

def add_or_remove_cash(pet_shop, amount):
    pet_shop["admin"]["total_cash"] += amount
    
def get_pets_sold(pet_shop):
    return pet_shop["admin"]["pets_sold"]

def increase_pets_sold(pet_shop, num_pets):
    pet_shop["admin"]["pets_sold"] += num_pets
    
def get_stock_count(pet_shop):
    stock_count = 0
    for pet in pet_shop["pets"]:
        stock_count += 1
    return stock_count

def get_pets_by_breed(pet_shop, breed):
    pets = []
    for pet in pet_shop["pets"]:
        if pet["breed"] == breed:
            pets.append(pet["name"])
    return pets

def find_pet_by_name(pet_shop, name):
    for pet in pet_shop["pets"]:
        if pet["name"] == name:
            return pet

def remove_pet_by_name(pet_shop, name):
    for pet in pet_shop["pets"]:
        if pet["name"] == name:
            pet_shop["pets"].remove(pet)