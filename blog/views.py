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

    if choice=='이름':
        return JsonResponse({
            'message':{
                'text':"권성호"
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
                'buttons':['이름','나이','성별','학과']
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
            'buttons': ['이름', '나이', '성별', '학과']
        }
    })
    elif choice == '학년':
        return JsonResponse({
            'message': {
                'text': "3학년"
            },
            'keyboard': {
                'type': 'buttons',
                'buttons': ['이름', '나이', '성별', '학과']
            }
        })
    elif choice == '성적':
        return JsonResponse({
            'message': {
                'text': "4.0"
            },
            'keyboard': {
                'type': 'buttons',
                'buttons': ['이름', '나이', '성별', '학과']
            }
        })

    else:
        return JsonResponse({
            'message':{
                'text':"남자"
            },
            'keyboard':{
                'type':'buttons',
                'buttons':['이름','나이','성별','학과']
            }
        })