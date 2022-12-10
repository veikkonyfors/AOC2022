import sys
import re


# Voi Voi
# Oli oletuksena että näkyy.
#
# Eka yritys kävi riveittäin läpi puut, että onko vasemmalla puolella korkeampia tai yhtä korkeita.
# Jos ei ollut, niin kasvatettiin näkyvien määrää.
# Jos oli, niin sitten katsottiin oikealta puolelta sama ja kasvatettiin näkyvien määrää tarvittaessa.
# Vielä sama kierros sarakkeittain, ylä ja alapuoli kerrallaan.
# Ongelma on, että sivuilta ja pystystä katsottuna osa puista lasketaan kahteen kertaan näkyviksi.
#
# Sitten luokka tree, jossa height ja visibility. __str__ ei oikein toiminut niin kun halusin.

# Muutin sen [height, vis]
#
# Edelleen ongelmana se, että jos ei näy sivusta, niin voi näkyä pystystä.
# Jos rivin jälkeen on true, niin voi sarake laittaa False.
#
# Eli pitäisi olla oletus False.
# Riveittäin katsoa, että jos vasemmalla puolella kaikki matalampia, niin sitten True.
# Oikealla puolella sama, jos vasemmalta ei näkynyt.
# Ja lopulta samat sarakkeittain. Jos puu on jo näkyvissä, niin skipataan puun tarkistus sarakkeessa.
#
# Sitten käydään rivi riviltä läpi, että onko vasemmalla puolella
# korkeampia. Jos on niin näkyvyys laitetaan Falseksi.
# Ja sama per sarake.


class tree():
    def __init__(self, height, visibility):
        self.height = height
        self.visibility = visibility

    def __str__(self):
        return (self.height, self.visibility)


def getcol(columnNumber):
    print("Kukkuu")
    column = []
    for idx, row in enumerate(intrees):
        column.append(row[columnNumber])
    return column

def num_visible(rowOrCol):
    #print("Kotkot", rowOrCol)
    visible = 0

    #print("row:", rowOrCol)
    for idxc, col in enumerate(rowOrCol):
        # print("col, idxc", col, idxc)

        if rowOrCol[idxc][1] == True: continue  # Already visible from somewhere, e.g. row-wise left or right
        show = True

        # From left
        for idxl, val in enumerate(rowOrCol):
            if idxl < idxc:
                if rowOrCol[idxl][0] >= rowOrCol[idxc][0]:
                    # print("ei nay: ",idxl, idxc, val, row)
                    rowOrCol[idxc][1] = False
                    show = False
                    break
            else:
                break  # Only from left side
        if show == True: rowOrCol[idxc][1] = True  # If all on left were lower, or idxc==0, nothing on left
        # print(show)

        # The rowwise right
        # From right, if wasn't visible from left
        if rowOrCol[idxc][1] == False:  # If wasn't visible from left, Look from the right
            # Assume show
            show = True
            for idxr, val in enumerate(rowOrCol):
                if idxc < idxr:
                    if rowOrCol[idxr][0] >= rowOrCol[idxc][0]:
                        # print("ei nay: ",idxr, idxc, val, row)
                        rowOrCol[idxc][1] = False
                        show = False
                        break
                else:
                    continue  # Only from right
            if show == True: rowOrCol[idxc][1] = True  # If all on left were lower, or idxc==0, nothing on left

            # print(show)
        if show: visible += 1
    print("Visible in ", rowOrCol, ": ", visible)
    return visible
def getCountVisible():
    count=0
    for i in range(len(intrees)):
        for j in range(len(intrees[i])):
            if intrees[i][j][1]: count += 1

    return count

intrees = []
linenumber = 0

for line in sys.stdin:
    # if linenumber == 0:
    #    linenumber += 1
    #   continue

    if line.startswith("#"): continue
    line = line.strip()
    print(line)

    for idx, height in enumerate(line):
        if idx == 0:
            intrees.append([[height, False]])
        else:
            intrees[linenumber].append([height, False])
        # print(linenumber, idx, height)
    linenumber += 1

print(intrees)

visible = 0
dummy = 0

# Iterate through the tree
# First rows
for idx, row in enumerate(intrees):
    # Row by row
    # First rowwise
    visible += num_visible(row)

print("Visible in rows: ", visible)
# Then columns
for idx, row in enumerate(intrees):
    # Skip first and last columns, they've been counted already
    if idx <= 0 or idx >= len(row) - 1: continue
    column = getcol(idx)
    visible += num_visible(column)
    visible -= 2  # top and bottom ones already counted with rows

print(intrees)
print("Visible in all: ", getCountVisible())

# print(getcol(0))
# print(num_visible(getcol(3)))

# 2022 first guess incorrect too high
# 1822 guess incorrect too high. Try binary search
# 1022 is too low
# 1422 didn't say was it too high or low. wait increased to 5 minutes
"""
That's not the right answer. Curiously, it's the right answer for someone else; 
you might be logged in to the wrong account or just unlucky. 
In any case, you need to be using your puzzle input. If you're stuck, make sure you're using the full input data; 
there are also some general tips on the about page, or you can ask for hints on the subreddit. 
Because you have guessed incorrectly 5 times on this puzzle, please wait 5 minutes before trying again. 
(You guessed 1805.) [Return to Day 8]
"""
