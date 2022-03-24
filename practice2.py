import sys
sys.stdin = open('sample_input (3).txt')

def GCD(num1, num2):
    while num2:
        num1, num2 = num2, num1%num2
    return num1

dict = {
    '0' : '0000',
    '1' : '0001',
    '2' : '0010',
    '3' : '0011',
    '4' : '0100',
    '5' : '0101',
    '6' : '0110',
    '7' : '0111',
    '8' : '1000',
    '9' : '1001',
    'A' : '1010',
    'B' : '1011',
    'C' : '1100',
    'D' : '1101',
    'E' : '1110',
    'F' : '1111'
}

T = int(input())
for TC in range(1, T+1):
    N, M = map(int, input().split())
    result = 0
    maps = [list(input()) for _ in range(N)]

    # 0 사이에 암호문 먼저 찾아내기
    passcode_lst = []
    for y in range(N):
        if '1' in maps[y] or '2' in maps[y] or '3' in maps[y] or '4' in maps[y] or '5' in maps[y] or '6' in maps[y] or '7' in maps[y] or '8' in maps[y] or '9' in maps[y] or 'A' in maps[y] or 'B' in maps[y] or 'C' in maps[y] or 'D' in maps[y] or 'E' in maps[y] or 'F' in maps[y]:
            if maps[y] not in passcode_lst:
                passcode_lst.append(maps[y])

    # 전부 다 2진수로 변환시키기
    B_code = ['0' for _ in range(len(passcode_lst))]
    for i in range(len(passcode_lst)):
        for j in range(M):
            B_code[i] = B_code[i] + dict[passcode_lst[i][j]]

    # 암호코드로 변환
    pswd_lst = []
    for k in B_code:
        cnt = len(k)-1
        pswd = ''
        while cnt >= 0:
            if k[cnt] == '1':
                each = 0 # 변환용 초기화
                number1 = 0 # 첫번째 1의 갯수
                number2 = 0 # 첫번째 0의 갯수
                number3 = 0 # 두번째 1의 갯수
                # 1의 갯수 계속 찾기
                while k[cnt] == '1':
                    cnt -= 1
                    number1 += 1
                # 0의 갯수 계속 찾기
                while k[cnt] == '0':
                    cnt -= 1
                    number2 += 1
                # 두번째 1의 갯수 계속 찾기
                while k[cnt] == '1':
                    cnt -= 1
                    number3 += 1
                # 최대공약수로 나누어주기
                cdgys1 = GCD(number1, number2)
                cdgys2 = GCD(cdgys1, number3)
                number1 = number1//cdgys2
                number2 = number2//cdgys2
                number3 = number3//cdgys2
                each = number3*100 + number2*10 + number1

                # 변환하기
                if each == 211:
                    pswd = '0' + pswd
                elif each == 221:
                    pswd = '1' + pswd
                elif each == 122:
                    pswd = '2' + pswd
                elif each == 411:
                    pswd = '3' + pswd
                elif each == 132:
                    pswd = '4' + pswd
                elif each == 231:
                    pswd = '5' + pswd
                elif each == 114:
                    pswd = '6' + pswd
                elif each == 312:
                    pswd = '7' + pswd
                elif each == 213:
                    pswd = '8' + pswd
                elif each == 112:
                    pswd = '9' + pswd
            if len(pswd) == 8:
                if pswd not in pswd_lst:
                    pswd_lst.append(pswd)
                pswd = ''
            cnt -= 1

    for p in pswd_lst:
        if (3*(int(p[0]) + int(p[2]) + int(p[4]) + int(p[6])) + int(p[1]) + int(p[3]) + int(p[5]) + int(p[7])) % 10 == 0:
            for q in range(8):
                result += int(p[q])
    print('#{} {}' .format(TC, result))