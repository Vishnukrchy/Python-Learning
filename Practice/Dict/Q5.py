# **Count Frequency of Elements in a List Using a Dictionary:** Write a function that counts the frequency of each element in a list and stores the result in a dictionary.

list=[1,4,5,1,3,5,6,3,5,8,9,0,2,0,4,23,6,]

def count_frequency(list):
    frequency_dict={}
    if len(list)==0:
       return frequency_dict
    else:
        for i in list:
            if i in frequency_dict:
                frequency_dict[i]=frequency_dict[i]+1
            else:
                frequency_dict[i]=1
    return frequency_dict

print("count frequency is ",count_frequency(list)) 

