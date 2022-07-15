
#input_test = [list(map(int, input().split())) for _ in range(4)]

input_test = []
for _ in range(4):
   input_test.append(list(map(int, input().split())))


# for _ in range(4):
#    input_test = [list(map(int, input().split()))]

# input_test = [list(map(int, input().split()))]
print(input_test)
print(input_test[0])
print(input_test[1])
print(input_test[2])


"""
    input()                                                 # 입력을 받는다. 이상태는 한개만 받는상태        
    input().split()                                         # 입력받은 값을 특정 값을 기준으로 잘라서 저장한다. 이상태는 띄어쓰기를 기준으로.
    list(map(int, input().split()))                         # 입력받은 값을 띄어쓰기 기준으로 정수형태로 2차행렬넣지만 엔터한번이면 입력을 마치게된다.
    [list(map(int, input().split())) for _ in range(4)]     # 입력받은 값을 띄어쓰기 기준으로 정수형태로 2차행렬에 집어넣는다. 단 엔터를 눌러도 바로 종료하지는 않는다.

"""   