from pyprimesieve import primes
primeList = []


with open('listfile.txt', 'w') as filehandle:
    for listitem in (primes(0, 179424674)):
        filehandle.write('%s\n' % listitem)


#It is for reading from file
# places = []
#
# # open file and read the content in a list
# with open('listfile.txt', 'r') as filehandle:
#     for line in filehandle:
#         # remove linebreak which is the last character of the string
#         currentPlace = line[:-1]
#
#         # add item to the list
#         places.append(currentPlace)