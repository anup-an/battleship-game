"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Writer: Anup Poudel
"""


class Player:
    """
    Class Player: Implements a player with some targets to shoot at.
    """

    def __init__(self, targets):
        """
        Constructor, initializes the newly created object.

        :param targets: list, list of targets to be shot by the user
        """
        # __hits denotes array of coordinates that are hit by the player
        self.__hits = []
        # __hits denotes array of coordinates that are misfired by the player
        self.__misses = []
        self.__targets = targets
        hits_Array = []

        for i in range(0, len(targets)):
            for target in targets[i]:
                hits_Array.append({target: []})

        self.__hits_array = hits_Array

    def shoot(self, coordinate):
        """
        Adds  or removes coordinates from the defined data structures.


        :param coordinate: str, the coordinate fired by the player 
        """
        hit = False
        isEnemyDefeated = False
        for target in self.__targets:

            for x in target:
                hit_Coordinates = []

                if coordinate in target[x]:
                    hit_Coordinates.append(coordinate)
                    hit = True
                    self.__hits.append(coordinate)
                    new_Array = []
                    hit_Array = []

                    for i in range(0, len(target[x])):
                        if target[x][i] != coordinate:
                            new_Array.append(target[x][i])
                        else:
                            for j in range(0, len(self.__hits_array)):
                                for hit_target in self.__hits_array[j]:
                                    if hit_target == x:
                                        self.__hits_array[j][hit_target].append(
                                            target[x][i])
                    target[x] = new_Array
                    if new_Array == []:
                        print(f"You sank a {x.lower()}!")
        if hit == False:
            if len(self.__misses) == 0:
                self.__misses.append(coordinate)
            elif coordinate in self.__hits or coordinate in self.__misses:
                print("Location has already been shot at!")
            else:
                self.__misses.append(coordinate)

        for i in range(0, len(self.__targets)):
            for target in self.__targets[i]:
                if self.__targets[i][target] == []:
                    isEnemyDefeated = True
                else:
                    isEnemyDefeated = False

        return (isEnemyDefeated, create_grid(self.__hits, self.__misses, self.__targets, self.__hits_array))

    def check_coordinate(self, coordinate):
        """
        Checks if coordinates are valid.

        :param: coordinate: str
        """
        xaxis = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
        yaxis = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        if not coordinate or coordinate[0] not in xaxis or coordinate[1:] not in yaxis:
            print("Invalid command!")
            print_grid(create_grid(self.__hits, self.__misses,
                       self.__targets, self.__hits_array))
            return False
        else:
            return True


def convert_to_alphabet(numeral):
    """
    Converts number to alphabets.
    :param numeral: number
    """
    alphabets = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
    numerals = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in range(0, len(numerals)):
        if numerals[i] == numeral:
            return alphabets[i]


def create_grid(hits=[], misses=[], targets=[], hits_array=[]):
    """
    Creates a grid representing the player screen which is printed in the command line
    :param hits: list, misses: list, targets: list
    """
    i = 0
    loop1 = True

    board_array = []

    while(loop1):
        if i < 10:
            array = []
            j = 0
            loop2 = True
            while(loop2):
                if j < 10:
                    found = False
                    for k in misses:
                        if k[0] == convert_to_alphabet(j) and int(k[1]) == i:
                            array.append("* ")
                            found = True
                    for m in range(0, len(hits_array)):
                        for hit in hits_array[m]:
                            for n in range(0, len(hits_array[m][hit])):
                                if hits_array[m][hit][n][0] == convert_to_alphabet(j) and int(hits_array[m][hit][n][1]) == i:
                                    if targets[m][hit] == []:
                                        string = hit[0].upper() + " "
                                        array.append(string)
                                        found = True
                                    else:
                                        array.append("X ")
                                        found = True
                    if not found:
                        array.append("  ")

                    j += 1
                else:
                    loop2 = False
            board_array.append(array)
            i += 1
        else:
            loop1 = False
    return board_array


def print_grid(grid):
    """
    Prints the grid in the command line
    :parameter grid: list
    """
    print()
    print(" ", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J")
    for i in range(0, len(grid)):
        print(i, end=" ")
        for j in range(0, len(grid[i])):
            print(grid[i][j], end="")
        print(i, end=" ")
        print()
    print(" ", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J")
    print()


def read_file():
    """
    Reads the input file and created the data structure
    """
    try:
        filename = input('Enter file name: ')

        file = open(filename, mode="r")
        targets = []
        for line in file:
            x = list(line.split(";"))
            target_coordinates = x[1:]
            for i in range(0, len(target_coordinates)):
                target_coordinates[i] = (target_coordinates[i][0].lower(
                ) + target_coordinates[i][1:]).strip()

            target = {
                x[0]: target_coordinates
            }
            targets.append(target)
        print_grid(create_grid())
        file.close()
        return targets

    except OSError:
        print("File can not be read!")

    # -------------------------------------------------------------------------------------------


def check_ship_coordinates(targets):
    """
    Checks if the ships have overlapping coordinates. Returns a boolean
    :param :targets: dict
    """
    target_coordinates = []
    for i in range(0, len(targets)):
        for target in targets[i]:
            for j in range(0, len(targets[i][target])):
                if targets[i][target][j] in target_coordinates:
                    return True
                else:
                    target_coordinates.append(targets[i][target][j])
    return False


def check_invalid_coordinates(targets):
    """
    Checks if the ships have overlapping coordinates. Returns a boolean
    :param :targets: dict
    """
    xaxis = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
    yaxis = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    isValid = False
    for i in range(0, len(targets)):
        for target in targets[i]:
            for j in range(0, len(targets[i][target])):
                if targets[i][target][j][0] in xaxis and targets[i][target][j][1:] in yaxis:
                    isValid = True
                else:
                    isValid = False
    return isValid


def main():
    targets = read_file()
    if targets:
        isSharing = check_ship_coordinates(targets)
        isValid = check_invalid_coordinates(targets)
        if isValid == True:
            if isSharing == False:

                # ------------------------Creating the grid and printing it----------------------------------
                player1 = Player(targets)
                while True:
                    # -------------------------------------------------------------------------------------------
                    coordinate = input('Enter place to shoot (q to quit): ')
                    if coordinate == "q":
                        print("Aborting game!")
                        return
                    else:
                        if player1.check_coordinate(coordinate.lower()):
                            isEnemyDefeated, grid = player1.shoot(
                                coordinate.lower())
                            if isEnemyDefeated == True:
                                print_grid(grid)
                                print('Congratulations! You sank all enemy ships.')
                                return
                            else:
                                print_grid(grid)

            else:
                print("There are overlapping ships in the input file!")
        else:
            print("Error in ship coordinates!")


if __name__ == "__main__":
    main()
