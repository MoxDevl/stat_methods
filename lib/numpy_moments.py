import numpy as np

def init_moment_k(nums: np.ndarray, k: int = 1) -> float:
    return np.sum(nums**k)/nums.size


def cent_moment_k(nums: np.ndarray, k: int) -> float:
    return np.sum((nums - nums.mean())**k)/nums.size