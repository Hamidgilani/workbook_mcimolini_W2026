burger = {
    "patties": 1,
    "patty_type": "whale",
    "cheese": True,
    "toppings": ["lettuce", "tomato", "onion", "pickles"],
    "bun_type": "brioche"
}

burger["patties"] = 2 
burger["patty_type"] = "beef"
burger["cheese"] = False
burger["toppings"].pop(1)

print ("Here's what's in the burger:")
print(f"{burger['patties']} {burger['patty_type']} patties on your burger")

print(f"Your burger has {burger["bun_type"]} bun.")

if burger["cheese"]:
    print("Cheese is on your burger.")
else:
    print("No cheese on your burger.")

print("Toppings:")
for topping in burger["toppings"]:
    print(f"- {topping}")


# as "gluten_allergy doesn't exist, we get a KeyError"
#if burger["gluten_allergy"]:
if burger.get("gluten_allergy", False): # no key error as we have default if our key doesn't exist
    print("We will remove the gluten from the burger.")

if "tomato allergy " in burger:
    print("We have removed the tomatoes from the burger. ")
else:
    print("We have added tomatoes to the burger. ")


