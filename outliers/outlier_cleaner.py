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
                                      
    ### your code goes here
    variation = [abs(predictions[i][0] - net_worths[i][0]) for i in range(len(ages))]
    touple = []  
    
    for i in range(len(ages)):
        touple.append([variation[i], ages[i][0], net_worths[i][0], predictions[i][0]])
        # print variation[i], ages[i][0] , net_worths[i][0] , predictions[i][0]
    
    from operator import itemgetter
    sortedTouple = sorted(touple, key = itemgetter(0))
    for elem in sortedTouple:
        #print elem
        cleaned_data.append([elem[1] , elem[2] , elem[0]])
    cleaned_data = cleaned_data[:-10]
    
    '''for elem in cleaned_data:
        print elem'''
        
    return cleaned_data

