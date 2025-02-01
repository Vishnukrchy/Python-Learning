'''
Problem: Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
 '''
def has_pair_with_sum(lst, k):
    if len(lst) < 2:
        return False
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if lst[i] + lst[j] == k:
                return True
    return False

# by using set
def has_pair_with_sum(lst, k):
    if len(lst) < 2:
        return False
    seen = set()
    for num in lst:
        com= k - num
        if com in seen:
            return True
        seen.add(num)
    return    

if __name__ == "__main__":
    print(has_pair_with_sum([1,2,3,4], 6)) # True
    print(has_pair_with_sum([1,2,3,4], 7)) # True
    
