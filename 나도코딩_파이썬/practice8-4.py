#######피클
#코딩데이터를 저장하는 방법, 다른사람이 받아서 또 쓸수있도록

import pickle
profile_file=open("profile.pickle", "wb")
profile = {"이름":"박명수", "나이":30, "취미":["축구","골프","코딩"]}
print(profile)
pickle.dump(profile, profile_file) #profile에 있는 정보를 file에 저장
profile_file.close()

profile_file=open("profile.pickle", "rb")
profile = pickle.load(profile_file) #file에 있는 정보를 profile에 불러오기
print(profile)
profile_file.close()

####### with

import pickle

with open("profile.pickle", "rb") as profile_file:
    print(pickle.load(profile_file))

#피클을 사용하지않고 파일 오픈방법
#close 따로 써주지않아도 되서 수월함
with open("study.txt", "w", encoding="utf8") as study_file:
    study_file.write("파이썬을 열심히 공부하고 있어요")

with open("study.txt", "r", encoding="utf8") as study_file:
    print(study_file.read())

####### 퀴즈7

#매주 1회 작성해야 하는 보고서가 있음
#항상 아래 형식으로

# - X 주차 주간보고 -
# 부서 : 
# 이름 : 
# 업무 요약 : 

# 1주차부터 50주차까지의 보고서 파일을 만드는 프로그램을 작성하시오
# 조건 : 파일명은 '1주차.txt' , '2주차.txt', ... 와 같이 만들기

for i in 

input ()

with open("{0}주차 보고서.txt", "w", encoding="utf8") as report_file:
    report_file.write(" - {0}주차 보고서 - \r 부서 : {1}\r 이름 : {2}\r 업무요약 : {3}").format(week, depart, name, contents)

#####################
for i in range(1, 51):
    with open(str(i) + "주차.txt", "w", encoding="utf8") as report_file:
        report.file.write("- {0}주차 주간보고 - ".format(i))
        report.file.write("\n부서 : ")
        report.file.write("\n이름 : ")
        report.file.write("\n업무 내용 : ")

