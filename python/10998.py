#문제
#두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

#A= int(input('number= '))
#B= int(input('number= '))

#A= int(input(0<A))
#B= int(input(B))
#숫자 형변환
#print(A+B)


#if 조건식:
#    조건이 참일때 실행됩니다
#1
#
#3

#A = input().split()
#A=int(A)

#if A % 4 & A % 400  == 0:
#    print('1')
#if A % 100 == 0:
#    print('0')
#else:
#    print('0')

#반복문
#A = [1, 2, 3, 4, 5]

#if 6 in A:
#    print('2')

#A= input()
#A= int(A)

#print(A, "*", 1, "=", A*1)
#print(A, "*", 2, "=", A*2)
#print(A, "*", 3, "=", A*3)
#print(A, "*", 4, "=", A*4)
#print(A, "*", 5, "=", A*5)
#print(A, "*", 6, "=", A*6)
#print(A, "*", 7, "=", A*7)
#print(A, "*", 8, "=", A*8)
#print(A, "*", 9, "=", A*9)

#반복문

A= input()
A= int(A)

for i in range(1, 10):
    #print(i+1)
    print(A, "*", i, "=", A*i)