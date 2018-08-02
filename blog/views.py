from django.shortcuts import render
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
import random
#daum실검 크롤링->그 데이터를 쿼리스트링으로 넘겨서 1위부터 10위까지 사이트로 순차접근->접근한 사이트에서 각각 정보 획득(까페 제목3개/ 블로그 개시글 제목 3개 등등...)
from bs4 import BeautifulSoup
import requests as rq
from time import sleep





def keyboard(request):
    return JsonResponse({
        'type':'buttons',
        'buttons':['가위', '바위', '보']
    })

@csrf_exempt
def message(request):
    json_str = ((request.body)).decode('utf-8')
    received_json_data = json.loads(json_str)

    user=received_json_data['user_key']
    type=received_json_data['type']
    choice=received_json_data['content']

    user=choice
    computer=random.randrange(1,4)
    if computer==1:
        computer='가위'
    elif computer==2:
        computer='바위'
    else:
        computer='보'

    if user=='가위':
        if computer=='가위':
            return JsonResponse({
                'message': {
                    'text': "컴퓨터는 %s" % computer+"\n" + '사용자는 %s' % user +"\n"+ '--->비겼습니다!'
                },
                'keyboard': {
                    'type': 'buttons',
                    'buttons': ['가위', '바위', '보']
                }
            })
        elif computer=='바위':
            return JsonResponse({
                'message': {
                    'text': "컴퓨터는 %s" % computer+"\n" + '사용자는 %s' % user +"\n"+'--->컴퓨터가 이겼습니다!'
                },
                'keyboard': {
                    'type': 'buttons',
                    'buttons': ['가위', '바위', '보']
                }
            })
        else:
            return JsonResponse({
                'message': {
                    'text': "컴퓨터는 %s" % computer+"\n" + '사용자는 %s' % user +"\n"+'--->사용자가 이겼습니다!'
                },
                'keyboard': {
                    'type': 'buttons',
                    'buttons': ['가위', '바위', '보']
                }
            })
    elif user=='바위':
        if computer=='가위':
            return JsonResponse({
                'message': {
                    'text': "컴퓨터는 %s" % computer+"\n" + '사용자는 %s' % user +"\n"+ '--->사용자가 이겼습니다!'
                },
                'keyboard': {
                    'type': 'buttons',
                    'buttons': ['가위', '바위', '보']
                }
            })
        elif computer=='바위':
            return JsonResponse({
                'message': {
                    'text': "컴퓨터는 %s" % computer+"\n" + '사용자는 %s' % user +"\n"+ '--->비겼습니다!'
                },
                'keyboard': {
                    'type': 'buttons',
                    'buttons': ['가위', '바위', '보']
                }
            })
        else:
            return JsonResponse({
                'message': {
                    'text':"컴퓨터는 %s" % computer+"\n" + '사용자는 %s' % user +"\n"+'--->컴퓨터가 이겼습니다!'
                },
                'keyboard': {
                    'type': 'buttons',
                    'buttons': ['가위', '바위', '보']
                }
            })
    else :
        if computer=='가위':
            return JsonResponse({
                'message': {
                    'text': "컴퓨터는 %s" % computer+"\n" + '사용자는 %s' % user +"\n"+ '--->컴퓨터가 이겼습니다!'
                },
                'keyboard': {
                    'type': 'buttons',
                    'buttons': ['가위', '바위', '보']
                }
            })
        elif computer=='바위':
            return JsonResponse({
                'message': {
                    'text': "컴퓨터는 %s" % computer+"\n" + '사용자는 %s' % user +"\n"+ '--->사용자가 이겼습니다!'
                },
                'keyboard': {
                    'type': 'buttons',
                    'buttons': ['가위', '바위', '보']
                }
            })
        else:
            return JsonResponse({
                'message': {
                    'text': "컴퓨터는 %s" % computer+"\n" + '사용자는 %s' % user +"\n"+ '--->비겼습니다!'
                },
                'keyboard': {
                    'type': 'buttons',
                    'buttons': ['가위', '바위', '보']
                }
            })





    '''
    일단은 가위,바위,보를 내가 선택하고 컴퓨터는 임이로 선택해서 누가이겼는지만 출력하게 만들자
    '''

#random.randrange(1,4)->1(가위),2(바위),3(보)중 난수발생




