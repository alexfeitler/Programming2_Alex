# Universal Gravity Calculator (15pts)
# In physics, the force of gravity between two objects can be calculated using the equation:
# F = G * (m1 * m2) / r**2
# F is the force of gravity in Newtons
# G is the universal gravity constant (6.67e-11)
# m1 is the mass of first object in kg
# m2 is the mass of the second object in kg
# r is the center to center distance between the objects in meters


# Make a calculator that does all of the following 
# (3pts) takes the inputs for mass 1, mass 2.and distance between the two objects (m1, m2, and r) 
# (4pts) contains exceptions for any potential errors (value and dividebyzero).
# (3pts) keeps asking for inputs until they are valid (see while loop from notes)
# (4pts) calculate the force of gravity in Newtons and print the result to the user in scientific notation to two decimals.



def force():
    done = False
    while not done:
        try:
            m1 = float(input("Enter the mass of the first object: "))
            m2 = float(input("Enter the mass of the second object: "))
            r = float(input("Enter the center distance between the objects in meters: "))
            G = (6.67e-11)
            F = (G * m1 * m2) / (r ** 2)
            done = True
        except ValueError:
            print("You entered an invalid number")
        except ZeroDivisionError:
            print("You can't divide by zero because it will make a black hole.")




    return (F)

print("The Gravitational Force is: {:.2e}".format(force()), "newton")
