#######파일입출력

score_file = open("score.txt", "w", encoding="utf8") #w 쓰기위해 열겠다 , utf8 인코딩해야 한글이 깨지지않음
print("수학 : 0", file=score_file)
print("영어 : 50", file=score_file)
score_file.close()

score_file = open("score.txt", "a", encoding="utf8") #a 덮어쓰기위해 열겠다
score_file.write("과학 : 80")
score_file.write("\n코딩 : 100") #줄바꿈 명시
score_file.close()

#한번에 전부 불러오고 싶을때
score_file = open("score.txt", "r", encoding="utf8") #r 읽어오겠다
print(score_file.read())
score_file.close()

#한줄한줄 불러와서 처리하고 싶을떄
score_file = open("score.txt", "r", encoding="utf8") #r 읽어오겠다
print(score_file.readline()) #줄별로 읽기, 한줄읽고 커서는 다음 줄로 이동
print(score_file.readline()) #줄별로 읽기, 한줄읽고 커서는 다음 줄로 이동
print(score_file.readline()) #줄별로 읽기, 한줄읽고 커서는 다음 줄로 이동
print(score_file.readline(),end="") #줄별로 읽기, 한줄읽고 커서는 다음 줄로 이동
score_file.close()

#파일이 총 몇줄일지 모를때는 반복문을 통해서 읽어올수도있다
score_file = open("score.txt", "r", encoding="utf8")
while True:
    line = score_file.readline()
    if not line:
        break
    print(line, end="")
score_file.close()

# 다른방법
score_file = open("score.txt", "r", encoding="utf8")
lines = score_file.readlines() #리스트 형태로 저장
for line in lines:
    print(line, end="")
score_file.close()