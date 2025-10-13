from math import ceil, floor

def make_interval_freq_list(array: list, delta_x: int) -> list:
    '''inter_array[0] = count[min_val; min_val + delta_x)

    inter_array[1] = count[min + delta_x; min + 2*delta_x)

    ...'''    
    nice_array = sorted(array)
    if len(nice_array)==0:
        return []
    
    min_val = floor(nice_array[0])
    max_val = ceil(nice_array[-1])
    num_intervals = ceil((max_val-min_val)/delta_x)

    interval_array = [0]*num_intervals
    for a in array:
        interval_array[floor(a-min_val)//delta_x]+=1
    return interval_array


def make_interval_median_list(min_val: float, max_val: float, delta_x: int) -> list:
    num_intervals = ceil((max_val-min_val)/delta_x)
    interval_median_array = [0.]*num_intervals
    
    curr_val = min_val
    for i in range(num_intervals):
        interval_median_array[i] = (2*curr_val+delta_x)/2
        curr_val += delta_x

    return interval_median_array


def get_interval_borders(min_val, max_val, delta_x) -> list:
    num_intervals = ceil((max_val-min_val)/delta_x)
    return [min_val+i*delta_x for i in range(num_intervals+1)]