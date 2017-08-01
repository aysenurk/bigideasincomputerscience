# coding=utf-8
import random

# Point out the function that we are going to use.

listOfMoves = ["A", "B", "C", "D", "E", "F", "G", "H"]
hugo = ["A", "A", "A", "B", "B", "B", "C", "C"]
michelle = ["D", "D", "D", "E", "E", "E", "F", "F"]


def reproduce(self, partner=None):
    '''If the individual list doesn’t have a partner, create the partner, that will be the child of current list.
    If the individual list has a partner, cross over the partner, that will be the child of current list. Moreover, “self” is our current list.'''

    if partner is None:
        child = self.__reproduce_clone()
    else:
        child = self.__repdroduce_crossover()
    return child


def __reproduce_clone(chromosome):
    ''' Define a function to change some elements of the individual list into random sequence.'''

    percentage = 0.2
    # Define the length of the list that we choose is 0.2*initial list.

    chromosome = list(chromosome)
    # To create a list with the elements from “chromosome”.

    mutationArray = random.sample(range(0, len(chromosome)), int(percentage * len(chromosome)))
    # To create an array whose length is percentage*length of chromosome. Moreover, it is in random order.

    for index in mutationArray:
        # Create a loop from the first element of MutationArray to the last element of MutationArray.
        chromosome[index] = random.choice(listOfMoves)
        # As for every position of the array, we choose an element from list “ListOfMoves” to be make the change randomly.
    return chromosome


def __reproduce_crossover(chromosome1, chromosome2):
    ''' them “chromosome1” and “chromosome2”.'''

    child = []
    # To create an empty list --“child”.

    cross = sorted(random.sample(range(0, len(chromosome2)), int(0.2 * len(chromosome1))))
    # To sort the list whose length is 0.2*length of chromosome1.

    parents = (chromosome1, chromosome2)
    # Define a word "parent" that is chromosome1 or chromosome2.

    chosenParent = 0
    prevIndex = 0

    for index in cross + [len(chromosome1)]:
        # To create a loop to make every element of list child sources from list chromosome1 or list chromosome2.
        child[prevIndex:index] = parents[chosenParent][prevIndex:index]
        prevIndex = index
        chosenParent = 1 - chosenParent

    return child


def main():
    print __reproduce_crossover(hugo, michelle)


if __name__ == '__main__':
    main()
