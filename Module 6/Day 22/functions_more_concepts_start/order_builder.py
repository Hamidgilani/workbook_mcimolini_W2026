from pizza import make_pizza_with_toppings
if __name__ == "__main__":
    is_ordering_pizza = True

    while is_ordering_pizza:
        ordering = input("Would you like to order a pizaa? (y/n): ")
        if ordering == "n":
            is_ordering_pizza = False
            continue
        size =int(input("What size pizza would you like?  "))
        crust = input("What type of crust would you like? ")

        # here's where our variable input comes in 
        toppings = []
        topping = "" 
        while topping != "done":
            topping = input("What topping would you like? ('done to finish): ")
            toppings.append(topping)
            
        
        special_requests = {}
        special_requests_topping = input("What modification to toppings? ('done to finish'): ") 

        while special_requests_topping != "done":
            amount = input("How much? (light,extra,double): ")
            special_requests[special_requests_topping] = amount
            special_requests_topping = input("what modification to toppings ('done to finish'): ")   

        # this is variable unpacking. use * to unpack *args and ** to unpack *kwargs
        # unpacking just means taking each item out of the collection and passing thrm in separetely
        make_pizza_with_toppings(*toppings,size=size,crust=crust,**special_requests)   