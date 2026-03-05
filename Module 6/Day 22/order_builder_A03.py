from pizza_A03 import * # * imports all functions from the given file

if __name__ == "__main__":

    is_still_ordering = True

    while is_still_ordering:
        user_input = input("Did you want to order a pizza? (y/n): ")

        if user_input == "n":
            is_still_ordering = False
            continue

        size = int(input("What size pizza would you like? (in inches): "))
        crust = input("What type of crust would you like: ")

        toppings = [] # list of toppings

        topping = input("What topping would you like? ('done' to finish): ")
        while topping != "done":
            toppings.append(topping)
            topping = input("What topping would you like? ('done' to finish): ")

        modifications = {}
        modification = input("What modification to toppings? ('done' to finish): ") # our key
        while modification != "done":
            modification_amount = input("How much? (light, extra, double): ") # our value
            modifications[modification] = modification_amount

            modification = input("What modification to toppings? ('done' to finish): ")

        # we need to unpack our list (toppings) and dictionary (modifications) to work with flex args
        make_pizza_with_toppings_and_mods(*toppings, size=size, crust=crust, **modifications)

    # Fixed examples:

    make_pizza(16, 'thin')
    make_pizza(12, "stuffed")

    # This won't work
    #make_pizza("gluten-free", 8)

    # This will work
    make_pizza(crust="gluten-free", size=8)

    make_pizza_with_toppings(12, "deep-dish", "pepperoni", "black olives")

    # This skips our default values
    make_pizza_with_toppings("ham", "pineapple")

    # Flexible arguments as the last parameter must be passed into our function last.
    # If we want to use flexible arguments with other parameters having defaults, the defaults should come last.
    #make_pizza_with_toppings("ham", "pineapple", size=12, crust="thin")

    make_pizza_with_toppings_and_mods("cheese", cheese="extra") #can skip my default values and they work
    make_pizza_with_toppings_and_mods("cheese", cheese="extra", size=24, crust="stuffed")
    make_pizza_with_toppings_and_mods("cheese", "mandarin orange", "bannana", "tobasco", size=6, crust="thin")