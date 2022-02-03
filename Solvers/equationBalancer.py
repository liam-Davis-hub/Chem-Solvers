import sys
import numpy as np


def main():
    eqn = input('Enter Equation')

    # break if no equal sign
    equals = 0
    for char in eqn:
        if char == '=':
            equals += 1

    if equals != 1:
        print('invalid equation')
        sys.exit

    reactants = fillReactants(eqn)
    products = fillProducts(eqn)

    matrix = np.matrix

    # append elements into matrix
    for index, element in enumerate(reactants):
        if element.isalpha() & element.isupper():
            if reactants[index + 1].islower():
                matrix.append(element + reactants[index + 1])
            else:
                matrix.append(element)

    # fill values into matrix


# create list of reactants
def fillReactants(eqn):
    reactants = []
    i = 0

    while eqn[i] != '=':
        if eqn[i] != '+':
            reactants.append(eqn[i])
        i += 1

    return reactants


# create list of products
def fillProducts(eqn):
    products = []
    i = len(eqn) - 1

    while eqn[i] != '=':
        if eqn[i] != '+':
            products.append(eqn[i])
        i += 1

    return products


main()
