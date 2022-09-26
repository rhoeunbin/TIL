from django.shortcuts import render
import random

# Create your views here.
def index(request):
    return render(request, "index.html")


def ping(request):
    return render(request, "ping.html")


def pong(request):
    # print(request)
    # print(dir(request))
    # print(request.GET)
    name = request.GET.get("ball")
    context = {
        "name": name,
    }
    return render(request, "pong.html", context)

    # return render(request, 'pong.html',{'name':request.GET.get('ball')}) 한 줄로 가능


def oddeven(request, number):
    if number % 2 == 0:
        answer = "짝수"
    elif number % 2 == 1:
        answer = "홀수"

    context = {
        "number": number,
        "answer": answer,
    }
    return render(request, "oddeven.html", context)


def calculate(request, num1, num2):

    plus = num1 + num2
    minus = num1 - num2
    gob = num1 * num2
    divide = num1 // num2

    context = {
        "num1": num1,
        "num2": num2,
        "plus": plus,
        "minus": minus,
        "gob": gob,
        "divide": divide,
    }

    return render(request, "calculate.html", context)


def names(request):
    return render(request, "names.html")


def past(request):
    animals = [
        "고양이",
        "강아지",
        "거북이",
        "토끼",
        "뱀",
        "사자",
        "호랑이",
        "표범",
        "치타",
        "하이에나",
        "기린",
        "코끼리",
        "코뿔소",
        "하마",
        "악어",
        "펭귄",
        "부엉이",
        "올빼미",
        "곰",
        "돼지",
        "소",
        "닭",
        "독수리",
        "타조",
        "고릴라",
        "오랑우탄",
        "침팬지",
        "원숭이",
        "코알라",
        "캥거루",
        "고래",
        "상어",
        "칠면조",
        "직박구리",
        "쥐",
        "청설모",
        "메추라기",
        "앵무새",
        "삵",
        "스라소니",
        "판다",
        "오소리",
        "오리",
        "거위",
        "백조",
        "두루미",
        "고슴도치",
        "두더지",
        "우파루파",
        "맹꽁이",
        "너구리",
        "개구리",
        "두꺼비",
        "카멜레온",
        "이구아나",
        "노루",
        "제비",
        "까치",
        "고라니",
        "수달",
        "당나귀",
        "순록",
        "염소",
        "공작",
        "바다표범",
        "들소",
        "박쥐",
        "참새",
        "물개",
        "바다사자",
        "살모사",
        "구렁이",
        "얼룩말",
        "산양",
        "멧돼지",
        "카피바라",
        "도롱뇽",
        "북극곰",
        "퓨마",
        "",
        "미어캣",
        "코요테",
        "라마",
        "딱따구리",
    ]

    past = random.choice(animals)
    name = request.GET.get("name")
    context = {
        "name": name,
        "past": past,
    }
    return render(request, "past.html", context)


def loremin(request):
    return render(request, "loremin.html")


def loremprint(request):
    paragraph = int(request.GET.get("para"))
    words = int(request.GET.get("word"))  # 받을 단어의수

    wordss = ["바나나", "딸기", "오렌지", "포도", "샤인머스켓", "금귤", "블루베리", "라즈베리"]

    list_ = []
    for _ in range(paragraph):
        l = []
        for _ in range(words):
            w = random.choice(wordss)
            l.append(w)
        list_.append(l)
    print(list_)

    context = {
        # "para": paragraph,
        # "word": words,
        "list_": list_,
    }
    return render(request, "loremprint.html", context)
