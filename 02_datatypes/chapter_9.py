# Set

essential_spices = {"ginger", "cloves", "black pepper"}
optional_spices = {"ginger", "ajwain"}

all_spices = essential_spices | optional_spices
print(f"All spices: {all_spices}")

common_spices = essential_spices & optional_spices
print(f"Common spices: {common_spices}")

only_in_essential = essential_spices - optional_spices
print(f"Only in essential spices: {only_in_essential}")

print(f"Is cloves in essential spices ? {'cloves' in essential_spices}")