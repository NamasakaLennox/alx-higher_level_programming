#!/usr/bin/python3
def weight_average(my_list=[]):
    average = 0
    total_weight = 0
    total_score = 0
    for elem in my_list:
        score, weight = elem
        total_weight += weight
        total_score += (score * weight)
    if (total_weight != 0):
        average = total_score / total_weight
    return (average)
