def make_pizza(size, crust):
    print("Summarize the pizza we are about to make:")
    print("Making a " + str(size) + "-inch pizza with " + crust + " crust.")

# this function will have default values
def make_pizza_with_toppings(size=8, crust="traditional", *toppings): # * is the part that makes this flexible, not args
    print("Summarize the pizza we are about to make:")
    print("Making a " + str(size) + "-inch pizza with " + crust + " crust.")

    for topping in toppings:
        print("- " + topping)
    
    print()

# this function will have everything
def make_pizza_with_toppings_and_mods(*toppings, size=8, crust="traditional", **modifications): # ** is the part that makes this flexible, not kwargs
    print("Summarize the pizza we are about to make:")
    print("Making a " + str(size) + "-inch pizza with " + crust + " crust.")

    for topping in toppings:
        print("- " + topping)
    
    print()
    
    if modifications:
        print("Special instructions:")
        for key, value in modifications.items():
            print(f"- {key}: {value}")

    print()