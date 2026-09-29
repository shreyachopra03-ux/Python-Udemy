# Dictionary

chai_order = dict(type="masala chai", sugar=2, size="large cup")
print(f"Chai order is: {chai_order}")

chai_recipe = {}
chai_recipe["base"] = "black tea"
chai_recipe["liquid"] = "milk"

print(f"Chai recipe is: {chai_recipe}")
del chai_recipe["base"]
print(f"Chai recipe is: {chai_recipe}")

print(f"Is there sugar in chai_order ? {'sugar' in chai_order}")

chai_order = {"type" : "black chai", "value": "3", "size" : "small"}
print(f"Order details (keys) : {chai_order.keys()}")
print(f"Order details (values) : {chai_order.values()}")
print(f"Order details (items) : {chai_order.items()}")

last_item = chai_order.popitem()
print(f"remove last item: {last_item}")

extra_spices = {"cardmom": "crushed", "ginger": "sliced"}
chai_recipe.update(extra_spices)
print(f"Updated chai recipe: {chai_recipe}")

customer_note = chai_order.get("note", "NO NOTE FOUND")
print(f"Customer note is: {customer_note}")

