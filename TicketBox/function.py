# 인터페이스 구성 기능 함수 모음

from food import *
from movie import *
from admin import *
from recipe import *

# ----------------------------------- <서비스 선택> ---------------------------------------------------------------

def user_select_service(): # 처음 서비스 선택을 하는 메뉴를 출력해주는 함수
    select_service = 0
    print('-' * 79)
    print('-                                 서비스 선택                                 -')
    print('-' * 79)
    print('1. 음식 구매')
    print('2. 영화관 예매')
    print('3. 상영정보')
    print('(종료를 원하시면 0번을 누르십시오. 종료 시 결재가 진행됩니다.)')
    select_service = int(input('입력 : ')) # 1~3번은 서비스 선택, 0번은 종료
    return select_service # 유저가 선택한 값으로 반환
# ----------------------------------- <음식 주문 함수> ---------------------------------------------------------------

def user_select_food(): # 음식 주문 함수
    print('-' * 79)
    print('-                                  음식 주문                                  -')
    print('-' * 79)
    for i in range(0, len(food_list)):
        print('{}. {} | 가격 : {}₩'.format(food_list[i].menu_num, food_list[i].name, food_list[i].cost))
    print('(뒤로가기를 원하시면 0번을 누르십시오.)')
    select_food = int(input('입력 : '))
    return select_food

def food_recipe(list, select_food): # 주문 음식 영수증 추가 함수
    list.append(recipe(food_list[select_food-1].menu_num, food_list[select_food-1].cost))

# ----------------------------------- <영화관 함수> ---------------------------------------------------------------

def user_select_movie(): # 유저가 영화관 예매를 선택할 시 나오는 선택란 출력 함수 - 2번
    print('-' * 79)
    print('-                                 영화관 선택                                 -')
    print('-' * 79)
    print('1. 가족 영화 1관')
    print('2. 애니메이션 영화 2관')
    print('3. 프리미엄 영화 3관 (음료수 제공)')
    print('(뒤로가기를 원하시면 0번을 누르십시오.)')
    select_cinema = int(input('입력 : ')) # 1~3번은 영화관 선택지 입력
    return select_cinema

# ----------------------------------- <영화 예매 함수> ---------------------------------------------------------------

def movie_service(select_cinema): # 유저가 입력한 영화관 선택에 따라 영화 종류를 출력해주는 함수
    if select_cinema == 1: # 가족 영화관 선택
        print('-' * 79)
        print('-                                가족영화 선택                                -')
        print('-' * 79)
        for i in range(0, len(family_movie_list)):
            print('{}. {}|가격:{}₩|남은좌석:200/{}'.format(family_movie_list[i].menu_num, family_movie_list[i].name, family_movie_list[i].cost, family_movie_list[i].extra_seat)) # 영화 객체 출력
        print('(뒤로가기를 원하시면 0번을 누르십시오.)')
        select_movie = int(input('입력 : '))
        return select_movie
    elif select_cinema == 2: # 애니메이션 영화관 선택
        print('-' * 79)
        print('-                              애니메이션 영화 선택                              -')
        print('-' * 79)
        for i in range(0, len(family_movie_list)):
            print('{}. {}|가격:{}₩|남은좌석:200/{}'.format(animation_movie_list[i].menu_num, animation_movie_list[i].name, animation_movie_list[i].cost, animation_movie_list[i].extra_seat)) # 영화 객체 출력
        print('(뒤로가기를 원하시면 0번을 누르십시오.)')
        select_movie = int(input('입력 : '))
        return select_movie
    elif select_cinema == 3: # 프리미엄 영화관 선택
        print('-' * 79)
        print('-                             프리미엄 영화 선택                              -')
        print('-' * 79)
        for i in range(0, len(family_movie_list)):
            print('{}. {}|가격:{}₩|남은좌석:200/{}'.format(premium_movie_list[i].menu_num, premium_movie_list[i].name, premium_movie_list[i].cost, premium_movie_list[i].extra_seat)) # 영화 객체 출력
        print('(뒤로가기를 원하시면 0번을 누르십시오.)')
        select_movie = int(input('입력 : '))
        return select_movie
    elif select_cinema == 15377: # 관리자
        admin_movie()
    else: # 유저가 다른 숫자를 입력했을 시
        return 0

if __name__ == '__main__':
    a = user_select_service()
    b = user_select_movie()
    movie_service(b)
