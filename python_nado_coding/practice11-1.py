####### 모듈

#자동차 사고나면 타이어만, 범퍼만 수리하는것처럼 특정부분만 유지보수 하는 방법

#극장이 있다. 현금만 받고, 잔돈을 거슬러주지않는 극장
#practice11-1_module.py 에 내용 넣음

import practice11_module
practice11_module.price(3) #3명 가격은 30000원 입니다.
practice11_module.price_mornning(4) #4명 조조 할인 가격은 24000원 입니다.
practice11_module.price_soldier(5) #5명 군인 할인 가격은 20000원 입니다.

import practice11_module as mv
mv.price(3) #3명 가격은 30000원 입니다.

from practice11_module import *
price(3) #3명 가격은 30000원 입니다.

from practice11_module import price, price_mornning #전부말고 특정 함수만 가지고오고 싶을때
price(3) #3명 가격은 30000원 입니다.

from practice11_module import price_soldier as price #솔져만 가지고오는데 별명을 price로 지정해서 사용
