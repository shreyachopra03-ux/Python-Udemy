# Boolean

is_boiling = True
stir_count = 5
total_actions = is_boiling + stir_count   # upcasting

print(f"Total actions are : {total_actions}")

milk_present = 0 # no milk
print(f"Is milk present ? {bool(milk_present)}")

# AND OPERATOR
water_hot = True
tea_added = True

tea_serve = water_hot and tea_added
print(f"Is tea served ? {tea_serve}")
