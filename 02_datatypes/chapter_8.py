# List

chai_ingredients = ["water", "milk", "black tea"]
chai_ingredients.append("sugar")

print(f"Ingredients are: {chai_ingredients}")

chai_ingredients.remove("water")
print(f"Ingredients are: {chai_ingredients}")

spice_options = ["cardomom", "ginger"]
chai_ingredients.extend(spice_options)
print(f"Ingredients are: {chai_ingredients}")

chai_ingredients.insert(3, "saunf")
print(f"Ingredients are: {chai_ingredients}")

last_added = chai_ingredients.pop()
print(f"{last_added}")
print(f"Ingredients are: {chai_ingredients}")

chai_ingredients.reverse()
print(f"Ingredients are: {chai_ingredients}")

chai_ingredients.sort()
print(f"Ingredients are: {chai_ingredients}")

sugar_levels = [1,2,3,4,5,6]
print(f"Maximum sugar level is: {max(sugar_levels)}")
print(f"Minimum sugar level is: {min(sugar_levels)}")