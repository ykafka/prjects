firsline = input().split(" ")
secline = input().split(" ")


#creates matrix
m = []
for i in firsline:
    int_val = int(i, base = 16,)
    #int_val = int()
    bin_val = int(str(bin(int_val))[2:])
    m.append([int(d) for d in str(bin_val)])

#adds zeroes and completes 8x8 matrix
for i in m:
    if len(i) != 8:
        for j in range(8-len(i)):
            i.insert(0, 0)

#creates subarray
m2 = []
for x in secline[2:]:
    m2.append([int(d) for d in str(x)])


#creates row and column numbers
row = int(secline[0])
col = int(secline[1])

#main
def iterate_main(mat):
    global m2
    global row
    global col
    count = 0
    for ro in range(0, 7-row):
        for co in range(0, 7-col):
            new_sub = []
            for rol in range(ro, ro+row):
                rw = []
                for coll in range(co, co+col):
                    element = mat[rol][coll]
                    rw.append(element)
                new_sub.append(rw)
            #print(new_sub)
            #print(m2)
    
            if compare_mat(new_sub, m2):
                count += 1
    return count
                

            #print(compare_mat(new_sub, m2))
            #print('-----')
                #print("1")

def compare_mat(mat, submat):
    global row
    global col
    for r in range(0, row):
        for c in range(0, col):
            if mat[r][c] != submat[r][c]:
                return False
    return True


print(iterate_main(m))

