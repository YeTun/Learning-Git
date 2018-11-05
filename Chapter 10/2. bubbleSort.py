# Me Computer, Mandalay.
# October 15, 2018
# bubbleSort.py 
# O(n*n) Quadratic

def bubbleSort(L):
    for j in range(len(L)):
        print(L)
        for i in range(len(L) - 1): 
            if L[i] > L[i+1]: 
                temp = L[i] 
                
                L[i] = L[i+1] 
                L[i+1] = temp        

#def bubbleSort(L):
#    swapped = True
#    while swapped:
#        swapped = False
#        print(L)
#        
#        for i in range(len(L)- 1):
#            if L[i] > L[i+1]:
#                temp = L[i]
#                L[i] = L[i+1]
#                L[i+1] = temp test2 = [6,1,2,3,4,5] 
#    input('run bubble test 2') 
#    bubbleSort(test2) 
#
#    test3 = [6,5,4,3,2,1] 
#    input('run bubble test 3') 
#    bubbleSort(test3) 
#
#    test4 = [1, 2, 3, 5, 6, 7] 
#    input('run bubble test 4') 
#    bubbleSort(test4)
#                swapped = True

def testBubbleSort():
    test1 = [1,6,3,4,5,2]
    input('run bubble test 1') 
    bubbleSort(test1) 

#   

#test4 = [1, 2, 3, 5, 6, 7]
#print(search(test4, 0))
testBubbleSort()
