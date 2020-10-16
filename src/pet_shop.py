# WRITE YOUR FUNCTIONS HERE
def get_pet_shop_name(dict):
    return dict["name"]

def get_total_cash(dict):
    return dict["admin"]["total_cash"]

def add_or_remove_cash(dict, amount):
    if amount >= 0:
        dict["admin"]["total_cash"] += amount
    elif amount < 0:
        dict["admin"]["total_cash"] -= amount  