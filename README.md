# About the app

This is a command line application written in python. It is a battleship game with a single player. The program starts by positioning the ships in a 10X10 coordinate grid based on the "board.txt" files. The player enters
the any coordinate on the grid in the format "XX", where the first character is a number from 0 to 9 and second character is an alphabet from a to j. If the input coordinate matches the ships coordinate, it is a hit and marked with "X". If the input coordinate does not match any of the ships coordinates, it is a miss and marked with "*". If all the coordinates of a ship are hit, the ship sinks. Finally, when all the ships sink, the game is over.

