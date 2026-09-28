# Strings

customer_name = "shreya"
chai_type = "saunf"

print(f"Order for {customer_name} : {chai_type} tea please !!")

chai_description = "Aromatic and bold"
print(f"Fisrt word : {chai_description[:8]}")
print(f"Last word : {chai_description[12:]}")
print(f"Whole sentence reversed : {chai_description[::-1]}")

label_text = "Chai Spécial"
encoded_label = label_text.encode("utf-8")
print(f"Non encoded label: {label_text}")
print(f"encoded label: {encoded_label}")

decoded_label = encoded_label.decode("utf-8")
print(f"decoded label: {decoded_label}")
