# Me Computer, Mandalay.
# Nov 3, 2018
# search.py

#Figure 10.2
def li_Search(L, e):
    """Assumes L is a list, the elements of which are in
          ascending order.
       Returns True if e is in L and False otherwise"""
    for i in range(len(L)):
        if L[i] == e:
            return True
        if L[i] > e: 
            return False
    return False

#Figure 10.3
def bi_Search(L, e):
    """Assumes L is a list, the elements of which are in
          ascending order.
       Returns True if e is in L and False otherwise"""
    
    def bSearch(L, e, low, high):
        #Decrements high - low
        if high == low:
            return L[low] == e
        
        mid = (low + high)//2
        if L[mid] == e:
            return True
        elif L[mid] > e:
            if low == mid: #nothing left to search
                return False
            else:
                return bSearch(L, e, low, mid - 1)
        else:
            return bSearch(L, e, mid + 1, high)
        
    if len(L) == 0:
        return False
    else:
        return bSearch(L, e, 0, len(L) - 1)

if "__main__" == __name__:
    l = [1, 3, 5, 7, 9, 11]
    
    print(li_Search(l, 1)) # best case
    print(li_Search(l, 9)) # average case
    print(li_Search(l, 2)) # worst case
    print()
    
    print(bi_Search(l, 4))
    print(bi_Search(l, 11))
	