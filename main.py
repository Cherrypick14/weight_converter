#temperature = 25
#if temperature >35:
 #  print("You have normal temperature")
#elif temperature >20: # (btwn 20 and 35)
 #  print("You actually need to see a doctor")
#elif temperature <20: # (btwn 10 and 20)
   #print("Woooh! we're really freezing outta here!")
#else:
 #   print("We're definiteley gonna have to do something bout this")
#print("We're done for the day")

#creating lists in python
#fruits =["mango","apples","tomatoes"]
#favorite =fruits[1]
#print("My most liked fruit is:"+ favorite)
#appending lists
#cars =["BMW", "Volvo", "Limo","Mercedes"]
#cars.append("Bugatti")
#print(cars)

# A weight converter program
name = input("What's your name: ")
weight= float(input("Enter your weight: "))
unit= input("K(gs) or L(bs)")
if unit.upper() == "l":
    converter =weight * 0.56
    print("Your weight in Kgs: " + converter)
else:
    converter = weight / 0.56
    print("Your weight in l(bs) is: " + str(converter))





