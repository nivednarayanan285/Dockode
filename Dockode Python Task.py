
def draw_hexagon(rows, columns):
    
    if columns % 2 != 0:
        columns='odd'
    else:
        columns='even'

    for i in range(rows):
        for j in range(columns // 2):
            print(" ---    ", end="")
            if columns == "odd" and j == ((columns // 2) - 1):
                print(" ---    ", end="")
        print()

        for j in range(columns // 2):
            print("/   \___", end="")
            if columns == 'odd' and j == ((columns // 2) - 1):
                print("/   \ ", end="")
            elif columns == 'even' and i != 0 and j == ((columns // 2) - 1):
                print("/ ", end="")
        print()

        for j in range(columns // 2):
            print("\   /   ", end="")
            if columns == 'odd' and j == ((columns // 2) - 1):
                print("\   /   ", end="")
            elif columns == 'even' and i != (rows - 1) and j == ((columns // 2) - 1):
                print("\ ", end="")
        print()


    for j in range(columns // 2):
        print(" ---    ", end="")
        if columns == 'odd' and j == (columns // 2) - 1:
            print(" ---    ", end="")


# Getting the user input for number of rows and columns
rows = int(input('No of rows'))
columns = int(input('No of columns'))

# Calling the function to draw the hexagon based on the user input
draw_hexagon(rows, columns)
