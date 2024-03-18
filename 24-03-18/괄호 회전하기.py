# 문제 : 괄호 회전하기
# 결과 :  / 속도: 0 / 메모리 : 0
# 제출시각 : 24-03-18  20:44:10
def braket(s):
    tmp = []
    flag = True
​
    for char in s:
        if char == '(' or char == '{' or char =='[':
            tmp.append(char)
            s = s[1:]
        else:
            if not tmp:
                flag = False
                break
            else:
                if (tmp[-1] == '(' and char == ')') or (tmp[-1] == '{' and char == '}') or (
                        tmp[-1] == '[' and char == ']'):
                    tmp.pop()
                    s = s[1:]
                else:
                    flag = False
                    s = s[1:]
                    break
​
    if tmp or (not flag):
        return False
​
    return True
​
​
def solution(s):
    cnt = 0
    for i in range(len(s)):
        if braket(s):
            cnt = cnt + 1
​
        s = s[1:] + s[0]
​
    return cnt

