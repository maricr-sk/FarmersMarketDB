# FarmerMarketDB

Parses through a farmers market database and prints the values in an organized way, providing a lookup function. Also implements the game Hangman using a random word from the dictionary. 

Directions: 

Problem 1: Farmers Market Database (60 pts)

In this assignment, you will implement a simple database that lets the user discover farmers markets in their town or zip code. The database prompts the user for a town or zip code. It then outputs all farmers markets in the town or zip code. The database prompts the user repeatedly until they enter "quit".

Download the file markets.txt. The file contains geographic information for more than 7000 farmers markets in the U.S. (source: https://catalog.data.gov/dataset/farmers-markets-directory-and-geographic-dataLinks to an external site.). Each line contains information about one farmers market. Data fields are separated by a single "@" character. The fields are in the following order: state, market name, street address, city, zip code, longitude, latitude.

Columbia University Greenmarket
E. Side of Broadway between 114th & 115th Streets
New York, New York 10027

(3) Create a main program that first reads in the markets.txt file once using the function from (1), then asks the user repeatedly for a zip code or a town name in a while loop until the user types “quit”.

For each input, the program shows all farmers markets for the town or zip code using the function from (2). If the user enters a zip code, the program looks up the farmers markets in the zip code using the first dictionary returned by read_market_data(). If the user enters a town name, the program first translates the town to a set of zip codes using the second dictionary returned by read_market_data(). It then looks up all farmers markets for each zip code and prints them all.

If a town or zip code does not exist, the program prints "Not found."


Problem 2: Hangman (40 pts)

In this assignment, you will implement the classic word-guessing game HangmanLinks to an external site.. The computer selects a random word that the player must guess. Instead of guessing the entire word at once, the player guesses individual letters. If the user guesses a letter that appears in the word, the computer reveals where in the word the guessed letter appears. If the user guesses a letter that does not appear in the word, the computer increases a variable value that keeps track of the number of incorrect guesses. If the player gets more than five guesses wrong, they loose. If the player uncovers the entire word, they win.

Write a Python program that plays Hangman:

(1) Download file dictionary.txt. Save it in the same folder as your program (problem2.py).

(2) At the start, your program reads all the words from the file and stores them in a list. Then it randomly selects one word from the list.

(3) The program prints '_' (underscore) for each letter in the word. Separate underscores with a space. For example, if the word is "college", the program prints:

_ _ _ _ _ _ _
(4) The main loop lets the player make repeated letter guesses. If the guessed letter appears in the word, the program uncovers the letter. If the letter appears multiple times, all occurrences are uncovered. For example, if the word is "college" and the user guesses "e", the output should be:

_ _ _ _ e _ e
I If the user guesses "l" in the next turn, the output should be:

_ _ l l e _ e
and so on. If the players guesses a letter that does NOT appear in the word, the program simply prints the previous output. For example, if the player guesses "k" next, the program outputs:

_ _ l l e _ e
(5) If the player guesses the entire word, the program prints a winning message and terminates. If the user makes more than five incorrect guesses, the program prints a losing message and terminates.
