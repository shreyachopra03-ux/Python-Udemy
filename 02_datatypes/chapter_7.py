# Tuples

masala_spices = ("cardamom", "ajwain", "cloves")

(spice1, spice2, spice3) = masala_spices

print(f"Main masala spices: {spice1}, {spice2}, {spice3}")

ginger_ratio , cardamom_ratio = 2, 1
print(f"Ratio of G is : {ginger_ratio} and C is : {cardamom_ratio}")

ginger_ratio , cardamom_ratio = cardamom_ratio, ginger_ratio
print(f"Ratio of G is : {ginger_ratio} and C is : {cardamom_ratio}")


#membership testing

print(f"Is cloves in masala spices ? {'cloves' in masala_spices}")