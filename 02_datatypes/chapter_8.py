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

# operator overloading

base_flavour = ["water", "soda"]
extra_flavor = ["strawberry"]
full_liquid_mix = base_flavour + extra_flavor
print(f"Full liquid mix: {full_liquid_mix }")

strong_brew = ["black coffee", "H20"] * 3
print(f"Strong brew: {strong_brew}")

# bytearray
raw_spice_data = bytearray(b"CINNAMON")
new_raw_spice_data = raw_spice_data.replace(b"CINN", b"CARD")
print(f"New raw data is: {new_raw_spice_data}")



