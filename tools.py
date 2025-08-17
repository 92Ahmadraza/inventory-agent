import json

INVENTORY_FILE = "inventory_agent/inventory.json"

def load_inventory():
    with open(INVENTORY_FILE, "r") as f:
        return json.load(f)

def save_inventory(data):
    with open(INVENTORY_FILE, "w") as f:
        json.dump(data, f, indent=2)

def list_items():
    return load_inventory()

def add_item(name, quantity):
    data = load_inventory()
    new_id = str(len(data) + 1)
    new_item = {"id": new_id, "name": name, "quantity": quantity}
    data.append(new_item)
    save_inventory(data)
    return new_item

def get_item_by_name(name):
    data = load_inventory()
    for item in data:
        if item["name"].lower() == name.lower():
            return item
    return None
