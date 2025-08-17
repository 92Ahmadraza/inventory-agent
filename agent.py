from openai import AssistantAgent, tool
import inventory_agent.tools as tools

@tool
def list_inventory_items():
    """List all items in the inventory."""
    return tools.list_items()

@tool
def add_inventory_item(name: str, quantity: int):
    """Add a new item to the inventory with given name and quantity."""
    return tools.add_item(name, quantity)

@tool
def find_item(name: str):
    """Find and return details of an item by name."""
    return tools.get_item_by_name(name)

agent = AssistantAgent(
    name="InventoryManager",
    instructions="You are an assistant that manages inventory items. Use the tools to interact with the inventory.",
    tools=[list_inventory_items, add_inventory_item, find_item],
)
