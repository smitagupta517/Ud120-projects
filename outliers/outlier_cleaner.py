#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    cleaned_data = []
    # print("hi")
    tuple = []
    
    for i in range(len(predictions)):
        error = (predictions[i]-net_worths[i])**2
        tuple.append((ages[i], net_worths[i], error))

    sorted_tuple = sorted(tuple, key = lambda x: x[2])

    cleaned_data = sorted_tuple[0:81]
    return cleaned_data

