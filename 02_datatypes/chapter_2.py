# Example of mutable data type

spice_mix = set()
print(f"Initial spice mix id: {id(spice_mix)}")
print(f"Initial spice mix: {spice_mix}")

spice_mix.add("Ginger")
spice_mix.add("Cardomom")

print(f"Final spice mix: {spice_mix}")
print(f"Final spice mix id: {id(spice_mix)}")

 