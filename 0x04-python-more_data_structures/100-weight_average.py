#!/usr/bin/python3


def weight_average(my_list=[]):
    """returns the weighted average of all integers tuple 
        (<score>, <weight>)
    """

    if len(my_list) == 0:
        return (0)

    w_sum = 0; # sum total of (score * weight)
    t_weight = 0; # sum of all weight values

    for i, j in my_list:
        w_sum += (i * j)
        t_weight += j

    return (w_sum / t_weight)
