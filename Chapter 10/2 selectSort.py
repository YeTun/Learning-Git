# Me Computer, Mandalay.
# Nov 3, 2018
# selectSort.py

#Figure 10.4
def selSort(L):
    """Assumes that L is a list of elements that can be
         compared using >.
       Sorts L in ascending order"""
    suffixStart = 0
    while suffixStart != len(L):
        #look at each element in suffix
        for i in range(suffixStart, len(L)):            
            if L[i] < L[suffixStart]:
                #swap position of elements
                L[suffixStart], L[i] = L[i], L[suffixStart]                
        suffixStart += 1
        print(L)
#        print(L[0:suffixStart], L[suffixStart:len(L)])

def testSelSort():
    test1 = [1,6,3,4,5,2]
#    test1 = [1234, 123, 12, 9, 1]
    print(test1)
    input('run selective test 1') 
    selSort(test1)
    print()

#    test2 = [6,1,2,3,4,5]
#    print(test2)
#    input('run selective test 2') 
#    selSort(test2)
#    print()
#
#    test3 = [6,5,4,3,2,1] 
#    print(test3)
#    input('run selective test 3') 
#    selSort(test3)
#    print()
#
#    test4 = [1,2,3,4,5,6] 
#    print(test4)
#    input('run selective test 4') 
#    selSort(test4)
#    print()

testSelSort()