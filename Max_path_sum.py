# ProjectEuler
def create_matrix(list1, base):
    matrix = [[ 0 for i in xrange(base)] for j in xrange(base)]
    k = 0
    for p in xrange(base):
        for q in xrange(p+1):
            matrix[p][q]=list1[k]
            k = k + 1
    return matrix

def pathsum(list2,base1): 
    for p in xrange(base1-1,0,-1):
        for q in xrange(p):
            list2[p-1][q] = int(list2[p-1][q]) + max(int(list2[p][q]),int(list2[p][q+1]))
    
    return list2[0][0]        

if __name__ == '__main__':
    t1 = "3 7 4 2 4 6 8 5 9 3"
    array1 = t1.split(" ")
    base1 = 4
    list1 = create_matrix(array1, base1)
    print pathsum(list1, base1)
    
    t2 = "75 95 64 17 47 82 18 35 87 10 20 04 82 47 65 19 01 23 75 03 34 88 02 77 73 07 63 67 99 65 04 28 06 16 70 92 41 41 26 56 83 40 80 70 33 41 48 72 33 47 32 37 16 94 29 53 71 44 65 25 43 91 52 97 51 14 70 11 33 28 77 73 17 78 39 68 17 57 91 71 52 38 17 14 91 43 58 50 27 29 48 63 66 04 68 89 53 67 30 73 16 69 87 40 31 04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"
    a2 = t2.split(" ")
    b1 = 15
    l2 = create_matrix(a2, b1)
    print pathsum(l2, b1)
    
