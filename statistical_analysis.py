# The idea is to create a module that provides statistical analysis functions for data sets. This module will include functions for calculating mean, median, mode, variance, standard deviation, and other statistical measures.

dataset = [10, 20, 30, 40, 50]

def mean(data):
    ''' Calculate the mean of the dataset '''
    return sum(data) / len(data)

def median(data):
    ''' Calculate the median of the dataset '''
    sorted_data = sorted(data)
    n = len(sorted_data)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_data[mid - 1] + sorted_data[mid]) / 2
    else:
        return sorted_data[mid]
    
def mode(data):
    ''' Calculate the mode of the dataset '''
    frequency = {}
    for num in data:
        frequency[num] = frequency.get(num, 0) + 1
    max_freq = max(frequency.values())
    modes = [key for key, value in frequency.items() if value == max_freq]
    return modes

def variance(data):
    ''' Calculate the variance of the dataset '''
    m = mean(data)
    return sum((x - m) ** 2 for x in data) / len(data)

def standard_deviation(data):
    ''' Calculate the standard deviation of the dataset '''
    return variance(data) ** 0.5