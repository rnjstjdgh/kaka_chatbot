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

#실검 리스트를 인자로 받아서 각 실검별 블로그, 뉴스, 연관검색어 title을 반환해주는 함수 구현
def main_crolling(realTimeContents):
    #print('=' * 100 + realTimeContents + '=' * 100)
    # url에 q부분에 실검 내용을 포함시키면 그 주소로 이동함!
    url_search = 'https://search.daum.net/search?w=tot&DA=ATG'
    res1 = rq.get(url_search, params={'q': realTimeContents})
    soup_search = BeautifulSoup(res1.text, 'html.parser')
    # print(soup_search.prettify())  # prettify-> html code를 좀더 보기 쉽게 만들기
    # 블로그 개시글 재목 4개 가져오기
    route_bolg_title = soup_search.find('div', {'id': 'blogColl'})
    bolg_title = route_bolg_title.find_all('a', {'class': 'f_link_b'})
    blog_title_list = []
    for i in bolg_title:
        blog_title_list.append(i.text)
    # 뉴스 개시글 재목 가져오기
    route_news_title = soup_search.find('div', {'id': 'newsColl'})
    news_title = route_news_title.find_all('a', {'class': 'f_link_b'})
    news_title_list = []
    for i in news_title:
        news_title_list.append(i.text)
    # 관련 검색어 가져오기
    route_relevant_content = soup_search.find('div', {'id': 'netizenColl_right'})
    relevant_content = route_relevant_content.find_all('span', {'class': 'txt_keyword'})
    relevant_content_list = []
    for i in relevant_content:
        relevant_content_list.append(i.text)
    return blog_title_list,news_title_list,relevant_content_list

dic = crol_RealTimeContents()

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
        t=main_crolling(dic[0])
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
        t = main_crolling(dic[1])
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
        t = main_crolling(dic[2])
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
        t = main_crolling(dic[3])
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
        t = main_crolling(dic[4])
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
        t = main_crolling(dic[5])
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
        t = main_crolling(dic[6])
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
        t = main_crolling(dic[7])
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
        t = main_crolling(dic[8])
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
        t = main_crolling(dic[9])
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




