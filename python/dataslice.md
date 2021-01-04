# 1차원 배열 DataFrame 슬라이스 (1)

```python

import pandas as pd
x = pd.DataFrame([1,2,3,4,5,6,7,8,9,10])

print(x[:5]) # 1,2,3,4,5
print(x[5:]) # 6,7,8,9,10
print(x[4:7])# 5,6,7
print(x[::2]) # 1,3,5,7,8 #처음부터 요소를 하나씩 건너 뛴 배열 구성(= step인 2 배열 출력)
print(x[1::2])# 2,4,6,8,10 #인덱스1부터 시작해서 step이 2인 배열

# step이 음수일 떄는 start와 stop의 기본값이 서로 바뀐다.
print(x[::-1]) # 10,9,8,7,6,5,4,3,2,1 #모든 요소를 거꾸로 나열
print(x[9::-1]) # 10,9,8,7,6,5,4,3,2,1 #인덱스 9부터 step 을 -1로 처음까지 나열
print(x[5::-2]) # 6,4,2 #인덱스 5부터 step 을 -2로 처음까지 나열
```

# 1차원 배열 DataFrame 슬라이스 (2)

```python

import pandas as pd
x = pd.DataFrame([1,2,3,4,5,6,7,8,9,10],index=['a','b','c','d','e','f','g','h','i','j'])

print(x[:'f']) # 1,2,3,4,5,6 # 처음(인덱스a)부터 인덱스f까지 긁어서 보여줌
print(x['f':]) # 6,7,8,9,10 #인덱스 f부터 끝까지 긁어서 보여줌
print(x['e':'h' ]) # 인덱스 e부터 인덱스 h까지 보여줌
print(x[::2]) # 1,3,5,7,9 #처음부터 요소를 하나씩 건너 뛴 배열 구성(= step인 2 배열 출력)
print(x['b'::2]) #2,4,6,8,10 #인덱스 'b'부터 2칸씩
print(x[::-1]) #10,9,8,7,6,5,4,3,2,1 #뒤에서부터 나열
print(x['j'::-1]) # 10,9,8,7,6,5,4,3,2,1 #'j'인덱스부터 거꾸로 나열
print(x['f'::-2]) #6,4,2 #'f'에서부터 거꾸로 step 2칸씩
```

# 인덱스 loc , iloc

1. 행번호(row number)로 선택하는 방법 (.iloc)
2. label이나 조건표현으로 선택하는 방법 (.loc)

```python
# 행 선택:
data.iloc[0] # data의 첫번째 행만
data.iloc[1] # 두번째 행만
data.iloc[-1] # 마지막 행만
# 열 선택:
data.iloc[:,0] # 첫번째 열만
data.iloc[:,1] # 두번째 열만
data.iloc[:,-1] # 마지막 열만
```

```python
x = pd.DataFrame([1,2,3,4,5,6,7,8,9,10], index=['a','b','c','d','e','f','g','h','i','j'])

print('A : ' , x[1:4]) # 묵시적 인덱스
print('B : ' , x.iloc[1:4]) # 묵시적 인덱스
print('C : ' , x['b':'d']) # 명시적 인덱스
print('D : ' , x.loc['b':'d']) # 명시적 인덱스
```

# 2차원 배열 DataFrame 슬라이스

```python
import pandas as pd

x = pd.DataFrame([[3, 5, 2, 4], 
                  [7, 6, 8, 8],
                  [1, 6, 7, 7]], 
                  columns=['A','B','C','D'])

print(x.iloc[:2,:2]) # 두 개의 행, 두 개의 열
print(x.iloc[:2,::2]) # 두 개의 행, ['A', 'C'] 열만 출력
print(x.iloc[:2,0]) # 두 개의 행, 0 번째 열

# labeling 기반이라 :1은 1까지 포함한다.
print(x.loc[:1,:'B']) # 두 개의 행, 두 개의 열
print(x.loc[:1,['A','B','C']]) # 두 개의 행, ['A','B' ,'C'] 열만 출력
print(x.loc[:1,'A']) # 두 개의 행, 0 번째 열
```





### 출처 : 코드스테이츠
