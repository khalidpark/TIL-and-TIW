####### 기본값

def profile(name, age, main_lang):
    print("이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}."\
        .format(name, age, main_lang)) #문장이 너무길때는 역슬러쉬 넣고 엔터치면 위아래 하나의 문장으로 취급

profile("유재석", 20, "파이썬")
profile("김태호", 25, "자바")

#같은학교같은학년같은반수업일경우 (나이, 언어 동일할때) 

def profile(name, age=17, main_lang="파이썬"):
    print("이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}."\
        .format(name, age, main_lang)) #문장이 너무길때는 역슬러쉬 넣고 엔터치면 위아래 하나의 문장으로 취급

profile("유재석")
profile("김태호")

######키워드값

def profile (name, age, main_lang):
    print(name, age, main_lang)

profile (name="유재석", main_lang="파이썬", age=20)
profile (main_lang="자바", age=25, name="김태호") #순서가 바뀌어도 함수설정대로 출력됨

####### 가변인자

def profile (name, age, lang1, lang2, lang3, lang4, lang5):
    print("이름 :{0}\t나이 :{1}\t.".format(name,age), end=" ") #end=" " 프린트값을 쭉 연결해서 보여준다
    print(lang1, lang2, lang3, lang4, lang5)

profile("유재석", 20, "python", "Java", "C", "C++", "C#") #유재석 언어가 늘어나면 함수자체를 수정해야함 lang6추가
profile("김태호", 25, "Kotlin", "Swift", "", "", "") #가능언어가 2개뿐이면 나머지 빈값을 채워줘야하는 수고스러움

def profile (name, age, *language):
    print("이름 :{0}\t나이 :{1}\t.".format(name,age), end=" ") 
    for lang in language:
        print(lang, end=" ")
    print()

profile("유재석", 20, "python", "Java", "C", "C++", "C#", "java Script")
profile("김태호", 25, "Kotlin", "Swift")