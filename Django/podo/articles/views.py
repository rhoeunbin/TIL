from django.shortcuts import render
import random
# Create your views here.

def index(request):

    dinner_list = [
        {"menu":"곱창", "src":'https://d12zq4w4guyljn.cloudfront.net/20220401114910508_photo_.jpg'},
        {"menu":"삼겹살", "src":"https://post-phinf.pstatic.net/MjAyMDAzMDNfMTcg/MDAxNTgzMTkwNjA3ODQ5.kUXPHqGJ2xPDSu_3FiEoFC3kY9QyQ_g9CziCGrFSDuEg.LpCfOTbc5qth9d-GKzGv9jwj2VKhcqmPHp5cp1KJYEsg.JPEG/IM_food02.jpg?type=w1200"},
        {"menu":"삼겹살", "src":'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSJ-DyH0b2uexJjewpRe5mpsbUJW3iRMo7doA&usqp=CAU'},
        {"menu":"피자", "src":'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT89_TZnFVdqAe4BG9VeqOEuSdBIqYg4S12nrEn5i0iWI2AQYWmj0s0&usqp=CAE&s'},
        {"menu":"떡볶이", "src":'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSeP8CHXmBrlYnweVYQkgJz-AfUDEeXfG_0Xg&usqp=CAU'},
        {"menu":"마라탕", "src":'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT6lbPMzn16QnJu9sTf2eUABh_qQBW-FbpK5g&usqp=CAU'},
        {"menu":"치킨", "src":'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR4zrRYDpWroSUMYfXIK4FWgmDAuDf9I7I9KQ&usqp=CAU'},
        {"menu":"초밥", "src":'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSefH9zzRuGoZFtL3qjD8p_5hsr-7vv5i2BUg&usqp=CAU'},
    ]

    dinner = random.choice(dinner_list)

    context = {
        "dinner" : dinner
    }

    return render(request,'index.html',context)


def lottoT(request):
    return render(request,'lottoT.html')

def lottoC(request):
    num = int(request.GET.get('num'))
    lottos = []
    for data in range(num):
        lottos.append(random.sample(range(1, 46),6))
    context = {
        'num' : num,
        'lottos' : lottos,
    }
    return render(request,'lottoC.html',context)


def lotto(request):
    lotto_list = []

    for _ in range(5):
        lotto = random.sample(range(1, 46),6)
        lotto_list.append(lotto)

    context = {
        "lotto_list" : lotto_list,
    }
    
    return render(request,'lotto.html',context)
