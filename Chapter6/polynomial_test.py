# Testing script for linked list implementation of polynomial ADT

from polynomial import Polynomial

def main():
    print("Testing class constructor: ")
    eq1 = Polynomial() # Create empty polynomial object
    eq2 = Polynomial(2, 5) # Create polynomial object with degree 2 coefficient 5

    print("Testing degree method: ")
    print("Should be -1: ", eq1.degree())
    print("Should be 2: ", eq2.degree())

    print("Testing getitem method: ")
    # REVIEW: Not really sure how the getitem for this class works??
    print(eq2[2])

    print("Testing evaluate method: ")
    print(eq2.evaluate(4))

    print("Testing simple_add method: ")
    eq2.simple_add(eq1)

    print("Testing add method: ")
    new_eq = eq1 + eq2
    print(new_eq)

    print("Testing sub method: ")
    # This method is not finished yet
    new_eq = eq1 - eq2
    print(new_eq)

    print("Testing mul method: ")
    # This method is not finished yet
    new_eq = eq1 * eq2
    print(new_eq)

    print("Testing multiply method: ")
    print(eq2.multiply(eq1))


if __name__ == '__main__':
    main()
