def make_pizza(size,crust):
    """Summarize the pizza we are about to make """ # """ does a newline and print a newline without calling newline
    print("\nMaking a " + str(size) + " -inch pizza with " + crust + " crust. ")

def make_pizza_with_default(size=12,crust="thin"):
    """Summarize the pizza we are about to make """ # """ does a newline and print a newline without calling newline
    print("\nMaking a " + str(size) + " -inch pizza with " + crust + " crust. ")

def make_pizza_with_toppings(*toppings,size=12,crust="thin",**comments): 
    print("Summarize the pizza we are about to make") # """ does a newline and print a newline without calling newline
    print("\nMaking a " + str(size) + " -inch pizza with " + crust + " crust. ") 
    print("The toppings added are: ")

    for topping in toppings:
        print("- " + topping)
    print()  

    if comments: 
        print("\n Special Instructions: ")
        for key, value in comments.items():
            print(f"- {key}: {value}")
    print()        

#make_pizza(16, "thin") # positional parameter passing 
   # make_pizza(size = 12,crust = "thick") # keyword parameter passing 
    #make_pizza(crust= "medium",size= 18) # keyword parameter order doesn't matter 
 
# order is important for this as if we change the order we experience type error as int can't be concatenated with string variable. 

    #make_pizza_with_default() # uses both defaults 
    #make_pizza_with_default(22) #uses default for crust 
    #make_pizza_with_default("thin") # still only uses default or crust. Output is odd
    #make_pizza_with_default(crust="medium") # need to pass by keyword if we're skip 
    # make_pizza_with_toppings(size=16,crust="thin")
    #make_pizza_with_toppings("cheese","pepperoni","banana peppers",size = 16,crust="thin")


    #make_pizza_with_toppings("cheese", size=8, crust="thin", cheese="dairy free", crust_type ="gluten free")