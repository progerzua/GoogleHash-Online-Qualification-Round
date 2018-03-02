import numpy as np
from main import get_input
'''
3 4 2 3 2 10
0 0 1 3 2 9
1 2 1 0 0 9
2 0 2 2 0 9
'''

R, C, F, N, B, T, out_arr = get_input('a_example.in')
#R # ROWS
#C # COLUMNS
#F # VEHICLES
#N # RIDES
#B # BONUS
#T # STEPS
v_array = np.zeros((F,2), dtype='uint8')
map_array = np.ones((R, C), dtype='bool')

for i in range(0, T):
    for v_ in v_array:
        for coordinate in v_:

