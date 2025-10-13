from math import ceil
from random import sample 

def repeating_sample_number(stand_dev: float, precision: float, multiplicity: float) -> int:
    '''**multiplicity** means **t**
    
    **precision** means **delta**'''
    return ceil((multiplicity*stand_dev/precision)**2)


def get_sample(nums: list, sample_size: int) -> list:
    '''Returns a random list of `sample_size` different elements from `nums`'''
    res = []
    for i in sample(range(0, len(nums)), sample_size):
        res.append(nums[i])
    return res