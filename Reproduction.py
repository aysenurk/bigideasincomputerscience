# coding=utf-8
import random

# Point out the function that we are going to use.

def reproduce(individuals, total):
    remaining = [None] * (total - len(individuals))

    for i in range(0, len(remaining)):
        doMutation = random.choice([True, False])
        if doMutation:
            remaining[i] = __reproduce_clone(random.choice(individuals))
        else:
            remaining[i] = __reproduce_crossover(random.choice(individuals), random.choice(individuals))

    mergedlist = individuals + remaining
    return mergedlist

def __reproduce_clone(chromosome):
    ''' Define a function to change some elements of the individual list into random sequence.'''

    percentage = 0.2
    # Define the length of the list that we choose is 0.2*initial list.

    chromosome = list(chromosome)
    # To create a list with the elements from “chromosome”.

    mutationArray = random.sample(range(0,len(chromosome)), int(percentage*len(chromosome)))
    # To create an array whose length is percentage*length of chromosome. Moreover, it is in random order.

    for index in mutationArray:
        # Create a loop from the first element of MutationArray to the last element of MutationArray.
        from driver import constants
        chromosome[index] = random.choice(constants)
        # As for every position of the array, we choose an element from list “constants” to be make the change randomly.
    return chromosome


def __reproduce_crossover(chromosome1, chromosome2):
    ''' them “chromosome1” and “chromosome2”.'''

    child = []
    # To create an empty list --“child”.

    cross = sorted(random.sample(range(0, len(chromosome2)), int(0.2*len(chromosome1))))
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
