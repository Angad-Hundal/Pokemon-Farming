
import numpy as np
from Pokemon_Farm import tuple_making

test_case1=[{'input': [[8], [8, 5]] ,
              'output': [[8],[(8,5)]],
              'reason' : 'general case'},

            {'input' : [[8]],
              'output' : [[8]] ,
              'reason' : 'case when only one item in the list'},

            {'input' : [[5],[8,5],[10,65,25,4,2,5],[7,8,63,56]] ,
              'output' : [[5], [(8, 5)], [(10, 65), (25, 4), (2, 5)], [(7, 8), (63, 56)]],
              'reason' : 'the case where there are lists of different lengths.'}]


for dict in test_case1:
    if dict['output']!=tuple_making(dict['input']):
        print(f"Error ocurred during the {dict['reason']}")



from Pokemon_Farm import basic_entry

test_case2=[
    {'input' : [[(0,0),(5,4)],'T'],
     'output' : np.array([['T', '_', '_', 'F', '_', '_', '_'],
                        ['_', '_', '_', 'W', '_', '_', '_'],
                        ['_', '_', '_', '_', '_', '_', '_'],
                        ['_', '_', '_', 'J', '_', '_', '_'],
                        ['_', '_', '_', '_', '_', '_', '_'],
                        ['_', 'G', '_', '_', 'T', 'F', '_'],
                        ['W', '_', '_', '_', '_', '_', 'G']]),
    'reason': 'general case'},

    {'input' : [[],'T'],
     'output' : np.array([
                ['T', '_', '_', 'F', '_', '_', '_'],
                ['_', '_', '_', 'W', '_', '_', '_'],
                ['_', '_', '_', '_', '_', '_', '_'],
                ['_', '_', '_', 'J', '_', '_', '_'],
                ['_', '_', '_', '_', '_', '_', '_'],
                ['_', 'G', '_', '_', 'T', 'F', '_'],
                ['W', '_', '_', '_', '_', '_', 'G']]),
     'reason': 'case when the no item has to be added'},

    {'input': [[(6, 0)], 'T'],
     'output' : np.array([['T', '_', '_', 'F', '_', '_', '_'],
                        ['_', '_', '_', 'W', '_', '_', '_'],
                        ['_', '_', '_', '_', '_', '_', '_'],
                        ['_', '_', '_', 'J', '_', '_', '_'],
                        ['_', '_', '_', '_', '_', '_', '_'],
                        ['_', 'G', '_', '_', 'T', 'F', '_'],
                        ['T', '_', '_', '_', '_', '_', 'G']])}

    ]

for dict in test_case2:
    if list(dict['output'][dict['output']!=basic_entry(dict['input'][0],dict['input'][1])])!=[]:
        print(f"Error in the {dict['reason']}")



from Pokemon_Farm import adjacent_list

test_case3=[
    {'input' : np.array([[1,2,3],[2,5,6],[4,5,6]]),
     'output' : [1,2,3,5,6,4],
     'reason' : 'general case of items being repeated'},

    {'input' : np.array([]),
     'output' : [],
     'reason' : 'case for the empty list'},

    {'input' : np.array([[1,2,3],[4,5,6],[7,8,9]]),
     'output' : [1,2,3,4,5,6,7,8,9],
     'reason' : 'case where no item is being repeated'},

    {'input' : np.array([[1]]),
     'output': [1],
     'reason' : 'case where there is only one item in an array'}
]

for dict in test_case3:
    if dict['output']!=adjacent_list(dict['input']):
        print(f" Error in {dict['reason']}")




from Pokemon_Farm import tree_selection

test_case4=[
    {'input': [],
     'output' : '_',
     'reason' : 'case where there is no adjacent item'},

    {'input' : ['F','W','G','J'],
     'output': 'M',
     'reason': 'case where megatree growth takes place'},

    {'input': ['F','W','G'],
     'output' : '_',
     'reason' : 'case where no tree dominates'},

    {'input' : ['F','W','J'],
     'output' : 'J',
     'reason' : 'case where the J dominates from all the three'},

    {'input' : ['F','W'],
     'output' : 'W',
     'reason' : 'case where two adjacent trees are there.'}
]

for dict in test_case4:
    if dict['output']!=tree_selection(dict['input']):
        print(f"Error in the {dict['reason']}")



from Pokemon_Farm import spring_changes

test_case5=[
    {'input': np.array([['_','_','_'],['_','_','_']]),
     'output' : np.array([['_','_','_'],['_','_','_']]),
     'reason' : 'case of empty array'  },

    {'input' : np.array([['F','_','G'],['G','J','W']]),
     'output' : np.array([['F','M','G'],['G','J','W']]),
     'reason' : 'case when there is mega tree growth'},

    {'input' : np.array([['F','_','_'],['J','_','_']]),
     'output' : np.array([['F','J','_'],['J','J','_']])}
]

for dict in test_case5:
    if list(dict['output'][dict['output']!=spring_changes(dict['input'])]) != []:
        print(f"Error in {dict['reason']}")


from Pokemon_Farm import harvest

test_case6=[
    {'input': np.array([['F','W','_'],['F','M','J']]),
     'output' : [2,1,0,1,1],
     'reason':'general case'},

    {'input':np.array([['_','_','_'],['_','_','_']]),
     'output': [0,0,0,0,0],
     'reason' : 'case of empty array.'},

    {'input':np.array([['F','W'],['G','J']]),
     'output': [1,1,1,1,0],
     'reason': 'case where all array is filled'}
]

for dict in test_case6:
    if dict['output'] != harvest(dict['input']):
        print(f"Error for {dict['reason']}")