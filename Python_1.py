def solution(a,b):
    if -10000000 <= a <= 10000000:
        if -10000000 <= b <= 10000000:
            if a>b:
                a,b = b,a
                data = sum(list(range(a,b+1)))
            elif a==b:
                data = a
            else:
                data = sum(list(range(a, b + 1)))
        else:
            data = "입력값을 크거나 작게 입력하였습니다."
    else:
        data = "입력값을 크거나 작게 입력하였습니다."

    return data

a = int(input("첫번째 값을 입력해주세요."))
b = int(input("두번째 값을 입력해주세요."))
print(solution(a,b))