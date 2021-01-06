#######연산자

print(3-2)

print(2**3) #2^3 2의3제곱
print(5%3) #5를 3으로 나눈 나머지
print(10%3) #10 나누기 3의 나머지 = 1
print(5//3) #몫 , 5나누기3의 몫

print(10>3) #True 출력
print(4>=7) #False 출력

print (3 == 3) #3은 3과 같다
print (4 == 2) # False
print (3+4 == 7)

print( 1 != 3) #1은 3과 같지않다 #True
print(not (1!=3)) #True의반대 즉 false

print ((3>0) and (3<5)) #True #앞과 뒤 모두 충족해야 true 나옴
print ((3>0) & (3<5)) #True

print((3>0) or (3>5)) #둘중하나라도 맞으면 True
print((3>0 | (3>5))) #백스페이스 아래있는

print(5>4>3)
print(5>4>7)

#######수식
number = 2 + 3 *4
print(number) #14
number = number + 2
print(number) #16
number += 2 #더 빠르게하는법, 32행과 같은 의미
print(number) #18
number -= 2
print(number) #16
number /= 2
print(number) #8
number *= 2
print(number) #16
number %= 5
print(number) #1