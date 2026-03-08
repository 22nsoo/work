# 우편정보 파일 자료 읽기
# 키보드에서 입력한 동이름으로 해당 주소 정보 출력
def zipProcess():
    dongIrum = input('동 이름 입력 : ')
    # dongIrum = '도곡'
    # print(dongIrum)
    with open(r'zipcode.txt', mode = 'r', encoding = 'euc-kr') as f:        #utf-8 안되면 euc-kr하면 바로 읽힘
        line = f.readline()             # 한 행 읽기
        # 135-806 서울    강남구  개포1동 경남아파트              1     <-이건 하나의 문자열 이걸 잘라야 한다    
        # print(line)                   
        # lines = line.split('\t')        #\t는 tab키
        # lines = line.split(chr(9))      #chr(tab에 해당하는 ascii코드) 아스키 코드 알파벳 번호 알아두기, 10번 13번 외우기 10번과 13번이 엔터
        # print(lines)                    #['135-806', '서울', '강남구', '개포1동 경남아파트', '', '1\n'] 동은 lines의 3번째에 있음
        while line:
            lines = line.split(chr(9))
            if lines[3].startswith(dongIrum):
                # print(lines)
                print('우편번호 : ' + lines[0] + ', ' + lines[1] + ', ' + lines[2] + ', ' + lines[3])

            line = f.readline()


if __name__ == '__main__':
    zipProcess()