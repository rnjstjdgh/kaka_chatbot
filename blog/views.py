from django.shortcuts import render
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
import random


def keyboard(request):
    return JsonResponse({
        'type':'buttons',
        'buttons':['가위','바위','보']
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
                    'text': "컴퓨터는 %s" % computer + '사용자는 %s' % user + '--->비겼습니다!'
                },
                'keyboard': {
                    'type': 'buttons',
                    'buttons': ['가위', '바위', '보']
                }
            })
        elif computer=='바위':
            return JsonResponse({
                'message': {
                    'text': "컴퓨터는 %s" % computer + '사용자는 %s' % user + '--->컴퓨터가 이겼습니다!'
                },
                'keyboard': {
                    'type': 'buttons',
                    'buttons': ['가위', '바위', '보']
                }
            })
        else:
            return JsonResponse({
                'message': {
                    'text': "컴퓨터는 %s" % computer + '사용자는 %s' % user + '--->사용자가 이겼습니다!'
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
                    'text': "컴퓨터는 %s" % computer + '사용자는 %s' % user + '--->사용자가 이겼습니다!'
                },
                'keyboard': {
                    'type': 'buttons',
                    'buttons': ['가위', '바위', '보']
                }
            })
        elif computer=='바위':
            return JsonResponse({
                'message': {
                    'text': "컴퓨터는 %s" % computer + '사용자는 %s' % user + '--->비겼습니다!'
                },
                'keyboard': {
                    'type': 'buttons',
                    'buttons': ['가위', '바위', '보']
                }
            })
        else:
            return JsonResponse({
                'message': {
                    'text': "컴퓨터는 %s" % computer + '사용자는 %s' % user + '--->컴퓨터가 이겼습니다!'
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
                    'text': "컴퓨터는 %s" % computer + '사용자는 %s' % user + '--->컴퓨터가 이겼습니다!'
                },
                'keyboard': {
                    'type': 'buttons',
                    'buttons': ['가위', '바위', '보']
                }
            })
        elif computer=='바위':
            return JsonResponse({
                'message': {
                    'text': "컴퓨터는 %s" % computer + '사용자는 %s' % user + '--->사용자가 이겼습니다!'
                },
                'keyboard': {
                    'type': 'buttons',
                    'buttons': ['가위', '바위', '보']
                }
            })
        else:
            return JsonResponse({
                'message': {
                    'text': "컴퓨터는 %s" % computer + '사용자는 %s' % user + '--->비겼습니다!'
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


'''
    if choice=='이름':
        return JsonResponse({
            'message':{
                'text':" 최홍만"
            },
            'keyboard':{
                'type':'buttons',
                'buttons':['이름','나이','성별','대학정보']
            }
        })

    elif choice=='나이':
        return JsonResponse({
            'message':{
                'text':"24살"
            },
            'keyboard':{
                'type':'buttons',
                'buttons':['이름','나이','성별','대학정보']
            }
        })
    elif choice=='대학정보':
        return JsonResponse({
            'message':{
                'text':"대학정보를 불러옵니다"
            },
            'keyboard':{
                'type':'buttons',
                'buttons':['학과','학년','성적']
            }
        })
    elif choice == '학과':
     return JsonResponse({
         'message': {
             'text': "수학과"
         },
         'keyboard': {
            'type': 'buttons',
             'buttons': ['이름', '나이', '성별', '대학정보']
        }
    })
    elif choice == '학년':
        return JsonResponse({
            'message': {
                'text': "3학년"
            },
            'keyboard': {
                'type': 'buttons',
                'buttons':['이름','나이','성별','대학정보']
            }
        })
    elif choice == '성적':
        return JsonResponse({
            'message': {
                'text': "4.0"
            },
            'keyboard': {
                'type': 'buttons',
                'buttons':['이름','나이','성별','대학정보']
            }
        })

    else:
        return JsonResponse({
            'message':{
                'text':"남자"
            },
            'keyboard':{
                'type':'buttons',
                'buttons':['이름','나이','성별','대학정보']
            }
        })
'''