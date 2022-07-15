sdorq = []
T=int(input())
for _ in range(0,T):
    for _ in range(9):
        sdorq.append(list(map(int, input().split())))

for test_case in range(0,T) : 
    for x in range(0,9):
        for y in range(test_case*10,(test_case+1)*10):    #세로읽기
            for y_check_range in (y+1,(test_case+1)*10):
                if sdorq[x][y]==sdorq[x][y_check_range]:
                    error_t="0"

    for y in range(test_case*10+1,(test_case+1)*10):    #가로읽기
        for x in range(0,9):		                    
            for x_range in (x,10):
                if sdorq[x][y]==sdorq[x_range][y]:
                    error_t="0"

print(error_t)

"""
    for x_count in range(0,3):
        for y_count in range(test_case*9,):
            print()
"""
