####### 패키지
# 모듈들을 모아놓은 집합

# Travel 폴더안에 , thailand.py / vietnam.py / __init__.py 생성

import travel.thailand
#import travel.thailand.ThailandPackage #불가
trip_to = travel.thailand.ThailandPackage()
trip_to.detail()

from travel.thailand import ThailandPackage
trip_to = ThailandPackage()
trip_to.detail()

from travel import vietnam
trip_to = vietnam.VietnamPackage()
trip_to.detail()

####### _all_

from travel import *
trip_to = vietnam.VietnamPackage()
trip_to.detail()
#불가능
#__init__ 에 내용 채웠더니 사용가능 (__all__ = ["vietnam"])

###### 패키지, 모듈 위치

import inspect
import random
print (inspect.getfile(random))
print (inspect.getfile(thailand))


