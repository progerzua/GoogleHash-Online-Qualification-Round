import numpy as np
import operator

def get_input(filename):
    '''
    Read given filename, return parsed params.
    '''

    with open(filename) as f:
        raw_data = f.readlines()


    params = raw_data[0].split()
    R = int(params[0]) #ROWS
    C = int(params[1]) #COLUMNS
    F = int(params[2]) #VEHICLES
    N = int(params[3]) #RIDES
    B = int(params[4]) #BONUS
    T = int(params[5]) #STEPS

    data = raw_data[1:]
    i = 0
    parsed_data = []

    for i in data:
        parsed_data.append(i.split())

    out_arr = np.asarray(parsed_data, dtype=np.int16)

    return R, C, F, N, B, T, out_arr

def calculate_distance(x1,y1, x2, y2):
    xr = x1 - x2
    yr = y1 - y2
    return abs(xr)+abs(yr)

def assign_task(data, curposition, curiter):

    available_tasks = []

    j = 0

    for i in data:
        distance = calculate_distance(curposition[0], curposition[1], i[0], i[1])
        distance += calculate_distance(i[0], i[1], i[2], i[3])
        if distance + curiter <= i[5]:
            available_tasks.append([j ,distance, data[j]])
        j += 1

    if available_tasks:
        sorted_tasks = sorted(available_tasks, key=lambda x: x[1])
        return sorted_tasks[0][0]
    else:
        return -1


if __name__ == "__main__":
    R, C, F, N, B, T, data = get_input('a_example.in')

    pool_of_cars = [[-1 for i in range(5)] for j in range(F)]
    for i in range(len(pool_of_cars)):
        pool_of_cars[i][1] = [0, 0] # curpos
        pool_of_cars[i][2] = 0 # enditer
        pool_of_cars[i][3] = [] # history
        pool_of_cars[i][4] = 1 # status

    print(pool_of_cars)

    #diffs = {}

    #j = 0
    #for i in data:
    #    diff = i[5] - i[4]
    #    diffs[j] = diff
    #    j += 1

    #sorted_diffs = sorted(diffs.items(), key=operator.itemgetter(1))

    print('Number of iterations:', T)
    curiter = 0
    for i in list(range((T-1))):

        for j in range(len(pool_of_cars)):



            if j[0] == -1 and pool_of_cars[j][4] != -1:
                task = assign_task(data, pool_of_cars[j][1], i)
                if task == -1:
                    pool_of_cars[j][4] = -1
                else:
                    pool_of_cars[j][4] = task
                del data[task]
