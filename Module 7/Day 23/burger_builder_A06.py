burger = {
    "patties": 1,
    "patty_type": "whale",
    "cheese": True,
    "toppings": ["lettuce", "tomato", "onion", "pickles"],
    "bun": "brioche"
}

burger["patties"] = 2
burger["patty_type"] = "beef"
burger["cheese"] = False
burger["toppings"].pop(1)

print("Here's what's in your burger:")
print(f"{burger['patties']} {burger['patty_type']} patties on your burger.")

print(f"Your burger has {burger["bun"]} bun.")
if burger["cheese"]:
    print("Cheese is on your burger.")
else:
    print("No cheese is on your burger.")

print("Toppings:")
for topping in burger["toppings"]:
    print(f"- {topping}")

# this will fail with KeyError
# if burger["gluten_allergy"]: - Will throw a KeyError as gluten_allergy doesn't exist in burger
burger["gluten_allergy"] = True # adds a new Key/Value pair to our dictionary.

if burger.get("gluten_allergy", False):
    print("We will remove the gluten from the burger.")

if "tomato_allergy" in burger:
    print("We have removed the tomatoes from the burger.")
else:
    print("We have added tomatoes to the burger.")