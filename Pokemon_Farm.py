

import numpy as np


def read_file(s):

    '''
    read the file and make a list of data inside it.
    s: file to be read
    return: list containing properly arranged data of the file
    '''

    f=open(s,'r')

    l = []
    for line in f:
        for value in line:
            if value == ' ':
                line = line.replace(' ', ',')
        l.append(line.rstrip().split(','))

    for list in l:
        for items in list:
            index = list.index(items)
            list[index] = int(items)

    return l



file_list=read_file('pokefruit_viridianfarm.txt')



def tuple_making(file_list):

    '''
    make tuple pair of the data in the list
    file_list: list in which data is present
    return: list of list containing tuples
    '''

    improved_list = []
    improved_list.append(file_list[0])
    del file_list[0]

    for sub_list in file_list:
        i = 0
        new = []

        while i < len(sub_list):
            tuple = (sub_list[i], sub_list[i + 1])
            i += 2
            new.append(tuple)
        improved_list.append(new)

    return improved_list



improved_list=tuple_making(file_list)




N=improved_list[0][0]          # specify the size of the grid

# differentiate data of the each tree
F=improved_list[1]
W=improved_list[2]
G=improved_list[3]
J=improved_list[4]



# make an blue print array of appropriate size
f=[]
for i in range(N):
    new='_'
    f.append(new)
    basic=f
new_f=[]
for i in range(N):
    new_f.append(basic)
new_f=np.array(new_f)



def basic_entry(s,letter):

    '''
    fill up the basic entries in the array
    s: blue print array
    letter: letter that has to be placed there (which tree)
    return: array containing the basic values given in the data
    '''

    for tuples in s:
        row = tuples[0]
        column = tuples[1]
        new_f[row][column] = letter
    return new_f


# call the function for each tree type
basic_entry(F,'F')
basic_entry(W,'W')
basic_entry(G,'G')
basic_entry(J,'J')




def adjacent_list(adjacent_array):

    '''
    create a list containing adjacent trees
    adjacent_array: sliced array containing adjacent values
    return: list of trees that are present adjacent to it
    '''

    list=[]
    for vert in adjacent_array:
        for thing in vert:
            if thing!='_' and thing not in list:
                list.append(thing)
    return list




def tree_selection(adj_list):

    '''
    select the appropriate tree that will fill the empty place
    adj_list: list of trees present adjacent to it
    return: the alphabet of the tree that is going to take the given place
    '''

    if len(adj_list)==0:
        return '_'
    elif len(adj_list)==1:
        return adj_list[0]
    elif len(adj_list)==4:
        return 'M'
    elif len(adj_list)==2:
        if 'J' in adj_list:
            return 'J'
        elif 'F' in adj_list and 'W' in adj_list:
            return 'W'
        elif 'F' in adj_list and 'G' in adj_list:
            return 'F'
        elif 'G' in adj_list and 'W' in adj_list:
            return 'G'
    elif len(adj_list)==3:
        if 'J' in adj_list:
            return 'J'
        else:
            return '_'



def spring_changes(current_array):

    '''
    account for the changes going to take place in spring
    current_array: the current grid of the trees
    return: grid of the trees after spring expansion
    '''

    new_f_change=current_array.copy()

    r = 0
    for rows in current_array:
        c = 0
        for items in rows:

            if items == '_':
                if r != 0:
                    if c != 0:
                        adj = current_array[r - 1:r + 2, c - 1:c + 2]
                        adj_list = adjacent_list(adj)
                        new_f_change[r, c] = tree_selection(adj_list)
                    else:
                        adj = current_array[r - 1:r + 2, 0:2]
                        adj_list = adjacent_list(adj)
                        new_f_change[r, c] = tree_selection(adj_list)

                else:
                    if c != 0:
                        adj = current_array[0:2, c - 1:c + 2]
                        adj_list = adjacent_list(adj)
                        new_f_change[r, c] = tree_selection(adj_list)

                    else:
                        adj = current_array[0:2, 0:2]
                        adj_list = adjacent_list(adj)
                        new_f_change[r, c] = tree_selection(adj_list)
            c += 1
        r += 1
    return new_f_change



def harvest(tree_array):

    '''
    harvest during a particular season
    tree_array: the array that has to be harvested
    return: list containing number of trees of each type
    '''

    f=0
    w=0
    g=0
    j=0
    m=0
    for rows in tree_array:
        for value in rows:
            if value=='F':
                f+=1
            elif value=='W':
                w+=1
            elif value=='G':
                g+=1
            elif value=='J':
                j+=1
            elif value=='M':
                m+=1
    return [f,w,g,j,m]


current=new_f                      # the current array
new=spring_changes(current)        # the array that will be made in the next spring


# these variables deal with the total production during all the harvests
F=0
W=0
G=0
J=0
M=0


year=1
while list(new[new!=current])!=[]:            # while the array in this year is not same as the array in the next year
    new1=new.copy()
    current=new
    new=spring_changes(new1)
    production=harvest(new1)


    # these variables deal with harvest of the current year
    f=production[0]
    w=production[1]
    g=production[2]
    j=production[3]
    m=production[4]

    year+=1

    F+=f
    G+=g
    W+=w
    J+=j
    M+=m



print(f'Result from the final {year-1} year: ')
print(f'Firefruit : {f}')
print(f'Waterfruit : {w}')
print(f'Grassfruit : {g}')
print(f'Joltfruit : {j}')
print(f'Megafruit : {m}')
print()



print('Result of the total Yield:')
print(f'Firefruit : {F}')
print(f'Waterfruit : {W}')
print(f'Grassfruit : {G}')
print(f'Joltfruit : {J}')
print(f'Megafruit : {M}')