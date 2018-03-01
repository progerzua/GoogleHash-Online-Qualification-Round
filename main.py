import numpy as np

def get_input(filename):
    '''
    Read given filename, return parsed params.
    '''

    with open(filename) as f:
        raw_data = f.readlines()


    params = raw_data[0].split()
    R = int(params[0])
    C = int(params[1])
    F = int(params[2])
    N = int(params[3])
    B = int(params[4])
    T = int(params[5])

    data = raw_data[1:]
    i = 0
    parsed_data = []

    for i in data:
        parsed_data.append(i.split())

    out_arr = np.asarray(parsed_data, dtype=np.int16)

    return [R, C, F, N, B, T, out_arr]

if __name__ == "__main__":
    R, C, F, N, B, T, data = get_input('a_example.in')
    print(R)
    print(C)
    print(F)
    print(N)
    print(B)
    print(T)
    print(data)
    print(data[0][2])