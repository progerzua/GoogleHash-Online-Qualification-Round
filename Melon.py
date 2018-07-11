import numpy as np
from main import get_input
'''
3 4 2 3 2 10
0 0 1 3 2 9
1 2 1 0 0 9
2 0 2 2 0 9
'''

R, C, F, N, B, T, out_arr = get_input('d_metropolis.in')
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


def calculate_distance(x1,y1, x2, y2):
    xr = x1 - x2
    yr = y1 - y2
    return abs(xr)+abs(yr)


for i, j in enumerate(routes):
    routes_path[i] = calculate_distance(j[0], j[1], j[2], j[3])
    routes_start_point[i] = calculate_distance(0, 0, j[0], j[1])
    routes_waittime[i] = j[4]
#print(routes_path.T)
#print(routes_start_point.T)
#print(routes_waittime.T)


List = [randint(0, F-1) for _ in range(len(routes))]

#print('#random', List)
List_array = np.array(List)

#result_rime = [{} for i in range(len(routes))]
result_time = np.zeros((len(routes), 1), dtype='uint8')

for i, j  in enumerate(List_array):
    time = routes_start_point[i] + routes_waittime[i] + routes_path[i]
    #print('TIME', time, 'CAR', j)

    result_time[i] += time

    indices = [i for i, x in enumerate(List) if x == j]
    #print(indices)
    for ii in indices:
        if ii > i:
            result_time[ii] += time

    #print(List_array == j)
    #print(result_time[List_array==j].T)

#print(result_time.T)

#print(routes[:,5] >= result_time)
print(False in (routes[:,5] >= result_time[:]))
print(False in np.unique(List_array in result_time))

uniq = np.unique(List)
for i in uniq:
    indexes = []
    for j in range(len(List)):
        if List[j] == i:
            indexes.append(j)
    print(len(indexes) , indexes)


#def give_new_coor(routes, number_route):
#    waypoint_corr[number_route] = routes[number_route,(2, 3)]
#    return waypoint_corr

"""
for i in range(0, T):
    for j, v_ in enumerate(v_array):
        if routes[j][4] < i:
            None
        else:
            print(waypoint_corr, v_[0], v_[1] )
            if list(waypoint_corr[j]) == [v_[0], v_[1]]:
                give_new_coor(routes, j)
"""

