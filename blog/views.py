from django.shortcuts import render
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
import random
from bs4 import BeautifulSoup
import requests as rq
from time import sleep

def crol_RealTimeContents():
    url_main_p = 'https://www.daum.net/'
    res_main_p = rq.get(url_main_p)
    soup_main = BeautifulSoup(res_main_p.text, 'html.parser')
    # print(soup_main)
    dic = {}  # 순위와 내용을 메핑시킬 dict선언 {'rank':'content'}
    result = soup_main.find('div', {'class': 'hotissue_mini'})
    # print(result)
    contents = result.find_all('a', {'class': 'link_issue'})
    for i in range(1, 11):
        dic[i] = contents[i - 1].text
    return dic

SR=[]
for i in crol_RealTimeContents().values():
    SR.append(i)




def keyboard(request):
    return JsonResponse({
        'type':'buttons',
        'buttons':['1->'+SR[0],'2->'+SR[1] ,'3->'+SR[2],'4->'+SR[3],'5->'+SR[4],'6->'+SR[5],'7->'+SR[6],'8->'+SR[7],'9->'+SR[8],'10->'+SR[9]]
    })

@csrf_exempt
def message(request):
    json_str = ((request.body)).decode('utf-8')
    received_json_data = json.loads(json_str)

    user=received_json_data['user_key']
    type=received_json_data['type']
    choice=received_json_data['content']

    if choice==SR[0]:
        return JsonResponse({
            'message': {
                'text': "NEXT"
            },
            'keyboard': {
                'type': 'buttons',
                'buttons':['1->'+SR[0],'2->'+SR[1] ,'3->'+SR[2],'4->'+SR[3],'5->'+SR[4],'6->'+SR[5],'7->'+SR[6],'8->'+SR[7],'9->'+SR[8],'10->'+SR[9]]
            }
        })
    elif choice==SR[1]:
        return JsonResponse({
            'message': {
                'text': "NEXT"
            },
            'keyboard': {
                'type': 'buttons',
                'buttons':['1->'+SR[0],'2->'+SR[1] ,'3->'+SR[2],'4->'+SR[3],'5->'+SR[4],'6->'+SR[5],'7->'+SR[6],'8->'+SR[7],'9->'+SR[8],'10->'+SR[9]]
            }
        })
    elif choice==SR[2]:
        return JsonResponse({
            'message': {
                'text': "NEXT"
            },
            'keyboard': {
                'type': 'buttons',
                'buttons': ['1->' + SR[0], '2->' + SR[1], '3->' + SR[2], '4->' + SR[3], '5->' + SR[4], '6->' + SR[5],
                            '7->' + SR[6], '8->' + SR[7], '9->' + SR[8], '10->' + SR[9]]
            }
        })
    elif choice==SR[3]:
        return JsonResponse({
            'message': {
                'text': "NEXT"
            },
            'keyboard': {
                'type': 'buttons',
                'buttons':['1->'+SR[0],'2->'+SR[1] ,'3->'+SR[2],'4->'+SR[3],'5->'+SR[4],'6->'+SR[5],'7->'+SR[6],'8->'+SR[7],'9->'+SR[8],'10->'+SR[9]]
            }
        })
    elif choice==SR[4]:
        return JsonResponse({
            'message': {
                'text': "NEXT"
            },
            'keyboard': {
                'type': 'buttons',
                'buttons':['1->'+SR[0],'2->'+SR[1] ,'3->'+SR[2],'4->'+SR[3],'5->'+SR[4],'6->'+SR[5],'7->'+SR[6],'8->'+SR[7],'9->'+SR[8],'10->'+SR[9]]
            }
        })
    elif choice==SR[5]:
        return JsonResponse({
            'message': {
                'text': "NEXT"
            },
            'keyboard': {
                'type': 'buttons',
                'buttons':['1->'+SR[0],'2->'+SR[1] ,'3->'+SR[2],'4->'+SR[3],'5->'+SR[4],'6->'+SR[5],'7->'+SR[6],'8->'+SR[7],'9->'+SR[8],'10->'+SR[9]]
            }
        })
    elif choice==SR[6]:
        return JsonResponse({
            'message': {
                'text': "NEXT"
            },
            'keyboard': {
                'type': 'buttons',
                'buttons':['1->'+SR[0],'2->'+SR[1] ,'3->'+SR[2],'4->'+SR[3],'5->'+SR[4],'6->'+SR[5],'7->'+SR[6],'8->'+SR[7],'9->'+SR[8],'10->'+SR[9]]
            }
        })
    elif choice==SR[7]:
        return JsonResponse({
            'message': {
                'text': "NEXT"
            },
            'keyboard': {
                'type': 'buttons',
                'buttons':['1->'+SR[0],'2->'+SR[1] ,'3->'+SR[2],'4->'+SR[3],'5->'+SR[4],'6->'+SR[5],'7->'+SR[6],'8->'+SR[7],'9->'+SR[8],'10->'+SR[9]]
            }
        })
    elif choice==SR[8]:
        return JsonResponse({
            'message': {
                'text': "NEXT"
            },
            'keyboard': {
                'type': 'buttons',
                'buttons':['1->'+SR[0],'2->'+SR[1] ,'3->'+SR[2],'4->'+SR[3],'5->'+SR[4],'6->'+SR[5],'7->'+SR[6],'8->'+SR[7],'9->'+SR[8],'10->'+SR[9]]
            }
        })
    else:
        return JsonResponse({
            'message': {
                'text': "NEXT"
            },
            'keyboard': {
                'type': 'buttons',
                'buttons':['1->'+SR[0],'2->'+SR[1] ,'3->'+SR[2],'4->'+SR[3],'5->'+SR[4],'6->'+SR[5],'7->'+SR[6],'8->'+SR[7],'9->'+SR[8],'10->'+SR[9]]
            }
        })





'''
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
#random.randrange(1,4)->1(가위),2(바위),3(보)중 난수발생




