def make_pizza(size, crust):
    """Summarize the pizza we are about to make:""" # """ does a newline and print without calling print
    print("\nMaking a " + str(size) + "-inch pizza with " + crust + " crust.")

def make_pizza_with_default(size=12, crust="thin"):
    """Summarize the pizza we are about to make:""" # """ does a newline and print without calling print
    print("\nMaking a " + str(size) + "-inch pizza with " + crust + " crust.")

def make_pizza_with_toppings(*toppings, size=12, crust="thin", **comments): # the * makes this a *args, not the name. ** makes this a **kwargs
    print("Summarize the pizza we are about to make:")
    print("Making a " + str(size) + "-inch pizza with " + crust + " crust.")
    print("The toppings added are:")
    for topping in toppings:
        print("- " + topping)
    
    if comments:
        print("\nSpecial Instructions:")
        for key, value in comments.items():
            print(f"- {key}: {value}")
    print()