from django.shortcuts import render
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt

def keyboard(request):
    return JsonResponse({
        'type':'buttons',
        'buttons':['이름','나이','성별','대학정보']
    })

@csrf_exempt
def message(request):
    json_str = ((request.body)).decode('utf-8')
    received_json_data = json.loads(json_str)

    user=received_json_data['user_key']
    type=received_json_data['type']
    choice=received_json_data['content']


    '''
    키보드에서 넘어온 리퀘스트에 해당되는 choice->내 선택지-->여기서 컴퓨터 난수 발생시켜서 승패를 결정한 후 승리면 1/패면 0을 변수에 저장해서 최종적으로 제이슨을 리턴한다
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