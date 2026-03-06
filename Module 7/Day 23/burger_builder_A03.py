burger = {
    "patties": 1,
    "patty_type": "chicken",
    "cheese": True,
    "toppings": ["lettuce", "tomato", "bacon", "spicy mayo"],
    "bun_type": "brioche"
}

burger["patties"] = 13
burger["patty_type"] = "beyond meat"
burger["cheese"] = False
burger["bun_type"] = "lettuce wrap"
burger["gluten_allergy"] = True # we can add new keys to our dictionary

new_toppings = burger["toppings"]
new_toppings.pop(2)
burger["toppings"] = new_toppings

# """ prints will print the text as present in the file. Be careful.
print(f"""
Here's what's in your burger: 
{burger["patties"]} {burger["patty_type"]} patties on your burger.""")

print(f"Your burger has {burger["bun_type"]} bun.")

if burger["cheese"]:
    print("Cheese is on your burger.")
else:
    print("No cheese on your burger.")

print("It has the following toppings:")
for topping in burger["toppings"]: # we can access individual items in our toppings via burger["toppings"][index]
    print(f"- {topping}")

# as "gluten_allergy doesn't exist, we get a KeyError"
#if burger["gluten_allergy"]:
if burger.get("gluten_allergy", False): # no key error as we have default if our key doesn't exist
    print("We have removed the gluten from your burger.")

# we can also check if a key exists with 'in'
if "tomato_allergy" in burger:
    if burger["tomato_allergy"]:
        print("We have removed the tomatoes from the burger.")
    else:
        print("We have added tomoates to your burger.")

try:
    if burger["onion_allergy"]:
        print("We have removed onions from your burger.")
    else:
        print("We have added onions to your burger.")
except KeyError:
    print("Sorry, we can't accomodate onion allergies.")