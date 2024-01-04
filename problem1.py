def read_market_data(filename):
    """
    Read in the farmers market data from the given filename and return
    a tuple of two objects:
    1) A dictionary mapping zip codes to lists of farmers market tuples.
    2) A dictionary mapping towns to sets of zip codes.
    listings: state, market name, street address, city, zip code, longitude, latitude.
    """

    zip_c = {}
    towns = {}

    with open(filename, 'r') as file:
        for line in file:
            data = (line.strip()).split('@')[:-2]
            if len(data) == 5 and isValid(data):
                beep = data[4]  # beep are zips
                bing = data[3].lower()  # bings are town names
                if beep in zip_c:
                    zip_c[beep] = zip_c[beep] + [data]
                else:
                    zip_c[beep] = [data]
                if bing in towns and beep.isnumeric():
                    towns[bing].add(beep)
                else:
                    towns[bing] = {beep}  # make into sets of zipcodes,
    file.close()
    return zip_c, towns  # replace this line


def isValid(t):
    if len(t) == 5:
        for i in t:
            if len(i) < 1:
                return False
    return True


def format_market_data(market):
    """
    Return a human-readable string representing the farmers market tuple
    passed to the function in the market parameter.
    """
    list = []
    if len(market) == 5:
        list = ["\n", market[1], "\n", market[2], "\n", market[0], ", ", market[3], " ", market[4]]
    ret = ''.join(str(item) for item in list)
    return ret  # replace this line


if __name__ == "__main__":

    FILENAME = "markets.txt"

    """
    Create a main program that first reads in the markets.txt file once using the function from (1), 
    then asks the user repeatedly for a zip code or a town name in a while loop until the user types “quit”.
    For each input, the program shows all farmers markets for the town or zip code using the function from (2).
    If the user enters a zip code, the program looks up the farmers markets in the zip code using the first 
    dictionary returned by read_market_data(). 

    If the user enters a town name, the program first translates the 
    town to a set of zip codes using the second dictionary returned by read_market_data(). It then looks up all 
    farmers markets for each zip code and prints them all. If a town or zip code does not exist, the program prints 
    'Not found.'"""

    try:
        zip_to_market, town_to_zips = read_market_data(FILENAME)  ## zip to market includes zipcodes for some reason
        on = True
        while (on):
            inp = input("\nPlease type a zip code or town name, or 'quit' to end:\n")
            if (type(inp) == str and inp != "quit") or type(inp) == int:
                strt = ""
                b = False
                if inp.isnumeric():
                    if inp in zip_to_market:
                        for zipc in zip_to_market[inp]:
                            print(format_market_data(zipc))
                            b = True
                elif type(inp) == str:
                    s = inp.lower()
                    if s in town_to_zips:
                        for t in town_to_zips[s]:
                            for z in zip_to_market[t]:
                                print(format_market_data(z))
                                b = True
                if b == False:
                    print("Not found.")
            elif inp == "quit":
                on = False

    except(FileNotFoundError, IOError):
        print("Error reading {}".format(FILENAME))