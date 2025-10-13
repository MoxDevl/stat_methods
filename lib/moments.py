def init_moment_k(nums: list, k: int = 1) -> float:
    sum_k=0
    for n in nums:
        sum_k+=n**k
    return sum_k/len(nums)


def cent_moment_k(nums: list, k: int) -> float:
    dif_sum_k = 0
    mean_num = init_moment_k(nums)
    for n in nums:
        dif_sum_k+=(n-mean_num)**k
    return dif_sum_k/len(nums)


def init_moment_k_interval(val_array: list, freq_array: list, k=1):
    total_vf=0
    freq_sum = sum(freq_array)
    for val, freq in zip(val_array, freq_array):
        total_vf += freq*(val)**k
    return total_vf/freq_sum


def cent_moment_k_interval(val_array: list, freq_array: list, k):
    mean_val = init_moment_k_interval(val_array, freq_array, 1)

    total_vf=0
    freq_sum = sum(freq_array)
    for val, freq in zip(val_array, freq_array):
        total_vf += freq*(val-mean_val)**k
    return total_vf/freq_sum