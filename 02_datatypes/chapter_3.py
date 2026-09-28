# Integer

black_tea_grams = 14
ginger_tea_grams = 3

total_tea_grams = black_tea_grams + ginger_tea_grams
print(f"Total tea grams are: {total_tea_grams}")

remanining_tea_grams = black_tea_grams - ginger_tea_grams
print(f"Remaining tea grams are: {remanining_tea_grams}")

milk_litres = 7
servings = 4

milk_per_serving = milk_litres / servings
print(f"Milk per serving would be: {milk_per_serving}")

total_tea_bags = 7
pots = 4

bags_per_pot = total_tea_bags // pots
print(f"Tea bags per pot: {bags_per_pot}")

cardomom_pods = 10
pods_per_cup = 3
leftover_pods = cardomom_pods % pods_per_cup

print(f"Leftover C pods are: {leftover_pods}")

# 2 * 2 * 2
base_flavour_strength = 2
scale_factor = 3
powerful_flavour = base_flavour_strength ** scale_factor

print(f"Scaled flavour strength: {powerful_flavour}")

total_tea_leaves_harvested = 1_000_000_000
print(f"Total tea leaves harvested are: {total_tea_leaves_harvested}")
