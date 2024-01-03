
def problem_1() -> None:
    """
    문제 1) 1부터 자연수 N까지 소수가 몇개인지 찾아서 출력하는 프로그램을 작성
    """
    
    try:
        input_num = int(input("자연수를 입력해주세요: "))  # 입력값
        prime_list = list(range(2, input_num+1))
        
        # 2부터 N까지 탐색
        for num in range(2, input_num+1):
            for i in range(2, num//2+1):
                if num % i == 0:
                    prime_list.remove(num)
                    break
        
        print(*prime_list)  # 소수 출력
        print(f'소수의 개수 : {len(prime_list)}')  # 소수 개수 출력
    
    except ValueError:
        print("입력한 값은 숫자가 아닙니다.")



def problem_2(phone_book) -> bool:
    """
    문제2) 전화번호중 한 번호가 다른 번호가 접두어인 경우가 있는지 확인
    True: 중복이 없음, False: 중복이 있음
    """
    
    answer = True
    
    # 리스트 내 아이템 순회
    for i1, item1 in enumerate(phone_book):
        
        # 자기자신을 제외한 번호 중 중복된 글자가 있는지 확인
        for i2, item2 in enumerate(phone_book):
            if i1 != i2 and item2.find(item1) >= 0:
                answer = False
    
    return answer
    
    
if __name__ == '__main__':
    problem_1()
    print()
    
    print("문제 2 정답: ")
    print(problem_2(["12","123","1235","567","88"]))
    print(problem_2(["123","456","789"]))