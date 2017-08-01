import random

listOfMoves = ["A", "B", "C", "D", "E", "F", "G", "H"]
hugo = ["A", "B", "C", "D", "E", "F", "G", "H", "A", "B", "C", "D", "E", "F", "G", "H"]
michelle = ["D", "D", "D", "E", "E", "E", "F", "F", "D", "D", "D", "E", "E", "E", "F", "F"]

def reproduce(self, partner=None):
    if partner is None:
        child = self.__reproduce_clone()
    else:
        child = self.__repdroduce_crossover()
    return child


def __reproduce_clone(chromosome):
    percentage = 0.2
    chromosome = list(chromosome)

    mutationArray = random.sample(range(0,len(chromosome)), int(percentage*len(chromosome)))
    for index in mutationArray:
        chromosome[index] = random.choice(listOfMoves)

    return chromosome


def __reproduce_crossover(chromosome1, chromosome2):
        child = []
        cross = sorted(random.sample(range(0, len(chromosome2)), int(0.2*len(chromosome1))))

        parents = (chromosome1, chromosome2)
        chosenParent = 0
        prevIndex = 0

        for index in cross + [len(chromosome1)]:
            child[prevIndex:index] = parents[chosenParent][prevIndex:index]

            prevIndex = index
            chosenParent = 1 - chosenParent

        return child


def main():
    print  __reproduce_clone(hugo)


if __name__ == '__main__':
    main()