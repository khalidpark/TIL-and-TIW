####### pip 로 패키지 설치하기

# 구글에서 pypi 검색
# beautifulsup4 4.8.2

# pip install beautifulsoup4 아래 창에 넣고 설치

from bs4 import BeautifulSoup
soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
print(soup.prettify())

# pip list 현재 설치되어있는 리스트 확인가능
# pip show beautifulsoup4 설치되어있는 패키지 정보확인
# pip install --upgrade beautifulsoup4
# pip uninstall beautifulsoup4

####### 내장함수
#내장되어있으니 따로 import 필요없음

# input : 사용자 입력을 받는 함수
langauge = input("무슨 언어를 좋아하세요?")
print("{0}은 아주 좋은 언어입니다!".format(langauge))

# dir : 어떤 객체를 넘겨줬을 때 그 객체가 어떤 변수와 함수를 가지고 있는지 표시
import random #외장 함수
print(dir())
#['BeautifulSoup', '__annotations__', '__builtins__', '__cached__', '__doc__',
# '__file__', '__loader__', '__name__', '__package__', '__spec__',
# '__warningregistry__', 'langauge', 'random', 'soup']
# 상단에 random이 추가되어있음

print(dir(random))
#랜덤 안에 쓸수있는 내역이 나옴 예)randint, randrange, sample, seed 등

# 구글에 list of python builtins
# 파이썬 내에서 쓸수있는 내장함수 볼수있음

####### 외장함수

# 구글에 list of python modules
# 파이썬 내에서 쓸수있는 외장함수 볼수있음

# glob : 경로 내의 폴더 / 파일 목록 조회 (윈도우 dir)
import glob
print(glob.glob("*.py")) #확장자가 py 인 모든 파일

# os : 운영체제에서 제공하는 기본 기능
# 예를들어 , 폴더를 만들고 삭제하는 기능
import os
print(os.getcwd()) #현재 디렉토리

folder = "sample_dir"

if os.path.exits(folder):
    print("이미 존재하는 폴더입니다")
    os.rmdir(folder) #폴더 삭제
    print(folder, "폴더를 삭제하였습니다")
else:
    os.makedirs(folder) #폴더 생성
    print(folder, "폴더를 생성하였습니다")

print(os.listdir()) #glob과 비슷한 기능

# time : 시간관련 외장함수
import time
print(time.localtime())
print(time.strftime("%Y-%m-%d %H:%M:%S"))

import datetime
print("오늘 날짜는", datetime.date.today())

#timedelta : 두 날짜 사이의 간격
today = datetime.date.today()
td = datetime.timedelta(days=100) #오늘날짜로부터 100일 뒤 저장
print("우리가 만난지 100일은", today + td) #오늘부터 100일 후