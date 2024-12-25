#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 10:56:27 2024

@author: jcbang
"""

# Catchers in the comet
# 수정본

'''
해설
1. 프로그램 목적
- 생태계 개체군 내 상호작용 중 텃세를 시뮬레이션
- 환경이 변화하였을 때 개체군의 변화 관찰
- 변화를 관찰하여 환경이 변화한 경우 실제로 텃세로 상호작용하는 개체군을 보호하는 방안 탐구

2. 프로그램 원리
- (생략(어제 짰는데 뭔소린지 모르겠음(내가 짠건데도)))

3. 결과
- (...)

4. 향후 추가 탐구 방안
- (...)




메모
- 개체 50개, 먹이 800개 정도에서 균형을 이룸

- 실험할 사항
- 먹이 줄 때, 특정 지역에서만 줄 때, 먹이 늘 때, 환경이 나빠질 때
- 대응 방법 : 환경이 나빠질 때 먹이를 늘리는 방안 등


'''


import random
import matplotlib.pyplot as plt


a = [] # 전체
for i in range(100):
    a.append([])
    for j in range(100):
        a[i].append([])

print(a)

# print(a[0][0][0][0]) # x좌표, y좌표, 있는 것, 몇번째 것인지

# a에 들어가는 리스트 형태 [[A, B, C...]]       A, B, C : 있는 것(개체 또는 먹이)

b = {} # 개체
c = {} # 먹이
n1 = 0
for i in range(50):
    rx1 = random.randrange(0, 100)
    ry1 = random.randrange(0, 100)
    rx2 = random.randrange(-2, 3)
    ry2 = random.randrange(-2, 3)
    print(rx1, ry1)
    if a[rx1][ry1] == []:
        b[n1] = [[0, n1], random.randrange(70, 131), rx1, ry1, [[(rx1+rx2)%100, (ry1+ry2)%100], [rx1, ry1]], [rx1, ry1], [0, 0]] # 이름(개체이기에 0 사용함), 에너지, x좌표, y좌표, 움직인 위치, 목적 위치, 목적(0 : 먹이, 1 : 활동 반경 유지, 2 : 침입자 제거, 3 : 침범, 목적의 이름)
        a[rx1][ry1].append(b[n1])
        n1 += 1
        
print(a)
print(b)

'''

for k in range(1000):
    for i in range(50):
        p1 = ''
        for j in range(100):
            
            if a[i][j] != []:
                p1 += '0'
            else:
                p1 += '_'
        print(p1)
               
        
'''

#while True:

    
n2 = 0
deli3 = []


comet0 = 0
comet1 = 0
comet2 = 0
comet3 = 0


ali = [] # 먹이 수
rli = [] # 개체 수
hli = [] # 이동 목적 : 먹이
oli = [] # 이동 목적 : 범위 유지
sli = [] # 이동 목적 : 침입자 공격
ili = [] # 이동 목적 : 침입

# '\033[38;5;164m' + 
#  + '\033[0m'


for i in range(800):
    rx1 = random.randrange(0, 100)
    ry1 = random.randrange(0, 100)
    c[n2] = [[1, n2], random.randrange(5, 16), rx1, ry1, 0] # 이름(먹이이기에 1 사용함), 에너지, x좌표, y좌표, 나이
    a[rx1][ry1].append(c[n2])
    n2 += 1


for yasashisanitsutsumaretanara in range(1000):
    if yasashisanitsutsumaretanara < 666:
        for i in range(25):
            rx1 = random.randrange(0, 100)
            ry1 = random.randrange(0, 100)
            c[n2] = [[1, n2], random.randrange(5, 16), rx1, ry1, 0] # 이름(먹이이기에 1 사용함), 에너지, x좌표, y좌표, 나이
            a[rx1][ry1].append(c[n2])
            n2 += 1
    else:
        for i in range(25):
            rx1 = random.randrange(0, 100)
            ry1 = random.randrange(0, 100)
            c[n2] = [[1, n2], random.randrange(5, 16), rx1, ry1, 0] # 이름(먹이이기에 1 사용함), 에너지, x좌표, y좌표, 나이
            a[rx1][ry1].append(c[n2])
            n2 += 1
    #print(a)
        
    
    print('실행 횟수 :', yasashisanitsutsumaretanara, '    먹이 수 :', len(c), '    개체 수 :', len(b), '                 이동 목적', '\033[38;5;34m' + '  1. 먹이 :', comet0, '\033[0m' + '    2. 활동 반경 유지 :', comet1, '\033[38;5;226m' + '    3. 침입자 공격 :', comet2, '\033[38;5;196m' + '    4. 침입 :', comet3, '\033[0m')
    print('수정 사항 : 그래프 표시, 업그레이드, 중간에 먹이 줄임')
    
    ali.append(len(c))
    rli.append(len(b))
    hli.append(comet0)
    oli.append(comet1)
    sli.append(comet2)
    ili.append(comet3)
    
    
    
    '''
    for kimiwonosete in range(7000000):
        inochinonamae = 0
    '''
        
    comet0 = 0
    comet1 = 0
    comet2 = 0
    comet3 = 0
        
    
    print()
    for i in range(50):
        p1 = ''
        for j in range(60):
            
            if a[i][j] != []:
                if len(a[i][j]) > 2:
                    if a[i][j][0][0][0] == 1:
                        p1 += '\033[38;5;164m' + '☄' + '\033[0m'
                    else:
                        if a[i][j][0][6][0] == 0:
                            p1 += '\033[38;5;34m' + str(chr(a[i][j][0][0][1]%94+33)) + '\033[0m' # 33~126
                        elif a[i][j][0][6][0] == 1:
                            p1 += str(chr(a[i][j][0][0][1]%94+33)) # 33~126
                        elif a[i][j][0][6][0] == 2:
                            p1 += '\033[38;5;226m' + str(chr(a[i][j][0][0][1]%94+33)) + '\033[0m' # 33~126
                        else:
                            p1 += '\033[38;5;196m' + str(chr(a[i][j][0][0][1]%94+33)) + '\033[0m' # 33~126
                        
                    if a[i][j][1][0][0] == 1:
                        p1 += '\033[38;5;164m' + '☄' + '\033[0m'
                    else:
                        if a[i][j][1][6][0] == 0:
                            p1 += '\033[38;5;34m' + str(chr(a[i][j][1][0][1]%94+33)) + '\033[0m' # 33~126
                        elif a[i][j][1][6][0] == 1:
                            p1 += str(chr(a[i][j][1][0][1]%94+33)) # 33~126
                        elif a[i][j][1][6][0] == 2:
                            p1 += '\033[38;5;226m' + str(chr(a[i][j][1][0][1]%94+33)) + '\033[0m' # 33~126
                        else:
                            p1 += '\033[38;5;196m' + str(chr(a[i][j][1][0][1]%94+33)) + '\033[0m' # 33~126
                        
                    if a[i][j][2][0][0] == 1:
                        p1 += '\033[38;5;164m' + '☄' + '\033[0m'
                    else:
                        if a[i][j][2][6][0] == 0:
                            p1 += '\033[38;5;34m' + str(chr(a[i][j][2][0][1]%94+33)) + '\033[0m' # 33~126
                        elif a[i][j][2][6][0] == 1:
                            p1 += str(chr(a[i][j][2][0][1]%94+33)) # 33~126
                        elif a[i][j][2][6][0] == 2:
                            p1 += '\033[38;5;226m' + str(chr(a[i][j][2][0][1]%94+33)) + '\033[0m' # 33~126
                        else:
                            p1 += '\033[38;5;196m' + str(chr(a[i][j][2][0][1]%94+33)) + '\033[0m' # 33~126

                elif len(a[i][j]) > 1:
                    if a[i][j][0][0][0] == 1:
                        p1 += '\033[38;5;164m' + '☄' + '\033[0m'
                    else:
                        if a[i][j][0][6][0] == 0:
                            p1 += '\033[38;5;34m' + str(chr(a[i][j][0][0][1]%94+33)) + '\033[0m' # 33~126
                        elif a[i][j][0][6][0] == 1:
                            p1 += str(chr(a[i][j][0][0][1]%94+33)) # 33~126
                        elif a[i][j][0][6][0] == 2:
                            p1 += '\033[38;5;226m' + str(chr(a[i][j][0][0][1]%94+33)) + '\033[0m' # 33~126
                        else:
                            p1 += '\033[38;5;196m' + str(chr(a[i][j][0][0][1]%94+33)) + '\033[0m' # 33~126
                        
                    if a[i][j][1][0][0] == 1:
                        p1 += '\033[38;5;164m' + '☄' + '\033[0m'
                    else:
                        if a[i][j][1][6][0] == 0:
                            p1 += '\033[38;5;34m' + str(chr(a[i][j][1][0][1]%94+33)) + '\033[0m' # 33~126
                        elif a[i][j][1][6][0] == 1:
                            p1 += str(chr(a[i][j][1][0][1]%94+33)) # 33~126
                        elif a[i][j][1][6][0] == 2:
                            p1 += '\033[38;5;226m' + str(chr(a[i][j][1][0][1]%94+33)) + '\033[0m' # 33~126
                        else:
                            p1 += '\033[38;5;196m' + str(chr(a[i][j][1][0][1]%94+33)) + '\033[0m' # 33~126
                    p1 += ' '
                else:
                    if a[i][j][0][0][0] == 1:
                        p1 += '\033[38;5;164m' + '☄' + '\033[0m'
                    else:
                        if a[i][j][0][6][0] == 0:
                            p1 += '\033[38;5;34m' + str(chr(a[i][j][0][0][1]%94+33)) + '\033[0m' # 33~126
                        elif a[i][j][0][6][0] == 1:
                            p1 += str(chr(a[i][j][0][0][1]%94+33)) # 33~126
                        elif a[i][j][0][6][0] == 2:
                            p1 += '\033[38;5;226m' + str(chr(a[i][j][0][0][1]%94+33)) + '\033[0m' # 33~126
                        else:
                            p1 += '\033[38;5;196m' + str(chr(a[i][j][0][0][1]%94+33)) + '\033[0m' # 33~126
                    p1 += '  '
            else:
                p1 += '   '
        print(p1)
            
    
    rx1 = random.randrange(0, 100)
    ry1 = random.randrange(0, 100)
    rx2 = random.randrange(-2, 3)
    ry2 = random.randrange(-2, 3)
    if a[rx1][ry1] == []:
        b[n1] = [[0, n1], random.randrange(70, 131), rx1, ry1, [[(rx1+rx2)%100, (ry1+ry2)%100], [rx1, ry1]], [rx1, ry1], [0, 0]] # 이름(개체이기에 0 사용함), 에너지, x좌표, y좌표, 움직인 위치, 목적 위치, 목적(0 : 먹이, 1 : 활동 반경 유지, 2 : 침입자 제거, 3 : 침범, 목적의 이름)
        a[rx1][ry1].append(b[n1])
        n1 += 1
    
    
    deli2 = []
    
    deli4 = []
    
    for i in c:
        c[i][4] += 1
        if c[i][4] > 100:
            deli4.append(i)
            a[c[i][2]][c[i][3]].remove(c[i])
    
    
    for i in deli4:
        del c[i]
    
    
    
    for i in b:

        if b[i][1] < 51: #사망
            deli2.append(i)
            deli3.append(i)
            a[b[i][2]][b[i][3]].remove(b[i])
            continue
        
        wh = [b[i][6][0], b[i][6][1], b[i][5][0], b[i][5][1]] # 목적, 이름(없음), 위치
        wh1 = []
        wh0 = []
        wh2 = []
        wh3 = []
        
        
        ah0 = 0
        ah1 = 0
        ah2 = 0
        ah3 = 0
        
        if b[i][6][0] == 0:
            comet0 += 1
        elif b[i][6][0] == 1:
            comet1 += 1
        elif b[i][6][0] == 2:
            comet2 += 1
        elif b[i][6][0] == 3:
            comet3 += 1
        
        
        
        #print(a[b[i][2]][b[i][3]], b[i])
        
        a[b[i][2]][b[i][3]].remove(b[i])
        #print(a[b[i][2]][b[i][3]])
        
        if wh[0] == 0:
            deli = []
            for j in c:
                if abs(b[i][4][-1][0]-c[j][2]) < 3 and abs(b[i][4][-1][1]-c[j][3]) < 3:
                    # wh0.append([0, c[j][0], c[j][2], c[j][3]]) # 목적, 이름, 위치
                    ah0 = 1
                    a[c[j][2]][c[j][3]].remove(c[j])
                    b[i][1] += c[j][1]
                    deli.append(j)
            for j in deli:
                del c[j]
        
        if wh[0] == 2:
            for j in b:
                if i != j:
                    if abs(b[i][4][-1][0]-b[j][2]) < 3 and abs(b[i][4][-1][1]-b[j][3]) < 3:
                        # wh2.append([2, b[j][0], b[j][2], b[j][3]]) # 목적, 이름, 위치
                        ah2 = 1
                        # 두 개체 만난 경우 처리 (b[j], b[i])
                        if random.randrange(0, b[i][1]+b[j][1]) < b[i][1]: # 내가 이김!!!
                            b[i][1] -= random.randrange(5, 16)
                            b[j][1] -= random.randrange(25, 36)
                            b[j][5] = b[j][4][0]
                            b[j][6] = [1, 0]
                            b[i][5] = b[i][4][0]
                            b[i][6] = [1, 0]
                        else: # 짐...
                            b[i][1] -= random.randrange(25, 36)
                            b[j][1] -= random.randrange(5, 16)
                            b[i][5] = b[i][4][0]
                            b[i][6] = [1, 0]
                            b[j][5] = b[j][4][0]
                            b[j][6] = [1, 0]
                        
                        
                
        if wh[0] == 1 or wh[0] == 3:
            if abs(b[i][2]-b[i][5][0]) < 3 and abs(b[i][3]-b[i][5][1]) < 3:
                ah1 = 1
                ah3 = 1
        
        
         #먹이나 다른 개체 만났을때
        
        wh = [b[i][6][0], b[i][6][1], b[i][5][0], b[i][5][1]] # 목적, 이름(없음), 위치
        if (ah0+ah1+ah2+ah3) > 0: # 위 조건과 통일(미사용)
            

            for j in b:
                if i != j:
                    for k in range(len(b[i][4])):
                        if abs(b[i][4][k][0]-b[j][2]) < 4 and abs(b[i][4][k][1]-b[j][3]) < 4:
                            wh2.append([2, b[j][0][1], b[j][2], b[j][3]]) # 목적, 이름, 위치
                            break
                        
            for j in c:
                for k in range(len(b[i][4])):
                    if abs(b[i][4][k][0]-c[j][2]) < 4 and abs(b[i][4][k][1]-c[j][3]) < 4:
                        wh0.append([0, c[j][0][1], c[j][2], c[j][3]]) # 목적, 이름, 위치
                        break
            
            wh1.append([1, 0, b[i][4][0][0], b[i][4][0][1]]) # 목적, 이름(없음), 위치
            wh3.append([3, 0, (2*b[i][4][-1][0]-b[i][4][0][0])%100, (2*b[i][4][-1][1]-b[i][4][0][1])%100]) # 목적, 이름(없음), 위치
            if b[i][1] > 100:
                if wh2 != []:
                    wh = wh2[-1]
                elif random.randrange(0, 2) == 0 and wh0 != []:
                    wh = wh0[-1]
                else:
                    wh = wh1[-1]
                
            else:
                if wh0 != []:
                    wh = wh0[-1]
                else:
                    wh = wh3[-1]
        else:
            if b[i][6][0] == 0:
                if a[b[i][5][0]][b[i][5][1]] == []:
                    wh = [1, 0, b[i][4][0][0], b[i][4][0][1]]
            elif b[i][6][0] == 1:
                wh = wh # ikuyo~~~
            elif b[i][6][0] == 2:
                if wh[1] not in deli3:
                    wh = [wh[0], wh[1], b[wh[1]][2], b[wh[1]][3]]
                else:
                    wh = [1, 0, b[i][4][0][0], b[i][4][0][1]]
            else:
                for j in c:
                    if abs(b[i][4][-1][0]-c[j][2]) < 6 and abs(b[i][4][-1][1]-c[j][3]) < 6:
                        wh0.append([0, c[j][0][1], c[j][2], c[j][3]]) # 목적, 이름, 위치
                if wh0 != []:
                    wh = wh0[-1]
        
        # 움직임(움직일 곳은 위에서 설정 완료)
        
        # a[b[i][2]][b[i][3]].remove(b[i])
        
        if yasashisanitsutsumaretanara < 333:
            b[i][1] -= random.randrange(2, 5)
        else:
            b[i][1] -= random.randrange(2, 5)
            
            
        if b[i][1] > 200:
            b[i][1] = 200
        b[i][5] = [wh[2], wh[3]]
        b[i][6] = [wh[0], wh[1]]
        if wh[2] == b[i][2] and wh[3] == b[i][3]:
            wh = wh # lol
        else:
            for h in range(10000):
                rx2 = random.randrange(-2, 3)
                ry2 = random.randrange(-2, 3)
                if ((b[i][2]-wh[2])**2+(b[i][3]-wh[3])**2) > ((abs(b[i][2]-wh[2]+rx2)%100)**2+(abs(b[i][3]-wh[3]+ry2)%100)**2):
                    b[i][2] = (b[i][2]+rx2)%100
                    b[i][3] = (b[i][3]+ry2)%100
                    b[i][4].append([b[i][2], b[i][3]])
                    if len(b[i][4]) == 11:
                        del b[i][4][0]
                    break
        
        a[b[i][2]][b[i][3]].append(b[i])
    
    for i in deli2:
        del b[i]


plt.subplot(2, 3, 1)   
plt.plot(ali)
plt.title('food')


plt.subplot(2, 3, 2)   
plt.plot(rli)
plt.title('individual')


plt.subplot(2, 3, 3)   
plt.plot(hli)
plt.title('to gain food')


plt.subplot(2, 3, 4)   
plt.plot(oli)
plt.title('to maintain area')


plt.subplot(2, 3, 5)   
plt.plot(sli)
plt.title('to defend')


plt.subplot(2, 3, 6)   
plt.plot(ili)
plt.title('to attack')

plt.tight_layout()
plt.show()

