import random
import math


def task1(n):
    if n <= 0:
        return "Error: invalid number of variables"
    num = random.randrange(0, 2 ** (2 ** n))
    s = bin(num)
    return "0" * (2 ** n - len(s) + 2) + s[2:]



def task2(string, var, residual):
    lg = math.log(len(string), 2)
    if 2**int(lg) !=len(string):
        return "Error: invalid length of boolean function"
    if(var <= 0 or var > lg):
        return "Error: invalid number of variable"
    if(not(residual in [0,1])):
       return "Error: invalid value of residual"
    r = lg-var
    ans = ""
    i = 0
    while i < len(string):
        if not(i%(2**r)) and (i/(2**r)%2 != residual):
            i += (2**r)
            continue
        ans += string[int(i)]
        i += 1
    return ans




def task3(zero, one, var):
    lg = math.log(len(zero), 2)
    if 2**int(lg) != len(zero) or len(zero) != len(one):
        return "Error: invalid length of residual"
    if var <= 0 or var > lg+1:
        return "Error: invalid number of variable"
    ans = ""
    r = lg+1-var
    for i in range(2**(var-1)):
        ans += zero[int((2**r)*i) : int((2**r)*(i+1))]
        ans += one[int((2**r)*i) : int((2**r)*(i+1))]
    return ans



def task5(string):
    ans = ""
    for i in range(1, 4):
        if(task2(string, i, 0) == task2(string, i, 1)):
            ans += '0'
        else:
            ans += '1'
    return ans




def toPolish(string):
    ans = ""
    string1 = string
    stack = []
    for el in string1:
        if el == '~':
            stack.append(el)
        elif el == '(':
            stack.append(el)
        elif el == ')':
            while stack[-1] != '(':
                ans += stack[-1]
                stack.pop()
            stack.pop()
        elif el == '&' or el == '|':
            while len(stack) > 0 and (stack[-1] == '~' or stack[-1] == '&' or stack[-1] == el):
                ans += stack[-1]
                stack.pop()
            stack.append(el)
        else:
            ans += el
    while len(stack) > 0:
        ans += stack[-1]
        stack.pop()
    return ans


def task6(string, func):
    ln = int(math.log(len(string), 2))
    func1 = func
    func = func.replace('~', ' not ')
    func = func.replace('|', ' or ')
    func = func.replace('&', ' and ')
    varrs = [0] * ln
    ans = True
    s = ""
    for i in range(len(string)):
        for j in range(ln):
            globals()['x' + str(j + 1)] = varrs[j]
        try:
            a = eval(func)
        except:
            return "Error: invalid expression"
        else:
            pass
        s += str(a)
        ans &= (a == int(string[i]))
        for j in range(ln - 1, -1, -1):
            if varrs[j] == 0:
                varrs[j] = 1
                break
            varrs[j] = 0
    if not ans:
        return 0

    a = ['&', '|']
    strr = toPolish(func1)
    for i in range(len(strr) - 1, -1, -1):
        if strr[i] == '&':
            i -= 1
            k = 0
            while i >= 0 and strr[i] != '|':
                if strr[i] == 'x':
                    k += 1
                if strr[i] == '&':
                    i += 1
                    break
                i -= 1
            if i >= 0 and strr[i] == '|' and k < 2:
                return 0
    return 1


def task7(string, func):
    ln = int(math.log(len(string), 2))
    func1 = func
    func = func.replace('~', ' not ')
    func = func.replace('|', ' or ')
    func = func.replace('&', ' and ')
    varrs = [0] * ln
    ans = True
    s = ""
    for i in range(len(string)):
        for j in range(ln):
            globals()['x' + str(j + 1)] = varrs[j]
        try:
            a = eval(func)
        except:
            return "Error: invalid expression"
        else:
            pass
        s += str(a)
        ans &= (a == int(string[i]))
        for j in range(ln - 1, -1, -1):
            if varrs[j] == 0:
                varrs[j] = 1
                break
            varrs[j] = 0
    if not ans:
        return 0

    a = ['&', '|']
    strr = toPolish(func1)
    for i in range(len(strr) - 1, -1, -1):
        if strr[i] == '|':
            i -= 1
            k = 0
            while i >= 0 and strr[i] != '&':
                if strr[i] == 'x':
                    k += 1
                if strr[i] == '|':
                    i += 1
                    break
                i -= 1
            if i >= 0 and strr[i] == '&' and k < 2:
                return 0
    return 1


def task8(string):
    ln = int(math.log(len(string), 2))
    if 2 ** ln != len(string):
        return "Error: invalid length of boolean function"
    x = [0] * ln
    p = 0
    ans = ""
    for el in string:
        if el == '1':
            if p == 1:
                ans += '|'
            else:
                p = 1

            for i in range(ln):
                if x[i] == 0:
                    ans += '~'
                ans += 'x' + str(i + 1)
                if i != ln - 1:
                    ans += '&'

        for i in range(ln - 1, -1, -1):
            if x[i] == 1:
                x[i] = 0
            else:
                x[i] = 1
                break
    return ans




def task9(string):
    ln = int(math.log(len(string), 2))
    if 2 ** ln != len(string):
        return "Error: invalid length of boolean function"
    x = [0] * ln
    p = 0
    ans = ""
    for el in string:
        if el == '0':
            if p == 1:
                ans += '&'
            else:
                p = 1

            ans += '('

            for i in range(ln):
                if x[i] == 1:
                    ans += '~'
                ans += 'x' + str(i + 1)
                if i != ln - 1:
                    ans += '|'

            ans += ')'

        for i in range(ln - 1, -1, -1):
            if x[i] == 1:
                x[i] = 0
            else:
                x[i] = 1
                break
    return ans


def task10(s):
    ans = ""
    if s[0] == '0':
        ans += '1'
    else:
        ans += '0'

    if s[-1] == '1':
        ans += '1'
    else:
        ans += '0'

    p = True
    for i in range(4):
        p &= (s[i] != s[-(i+1)])
    if p is True:
        ans += '1'
    else:
        ans += '0'

    p = True
    for i in range(7):
        if s[i] == '0':
            continue
        for j in range(i+1, 8):
            if (i&j == i) and s[j] == '0':
                p = False
                break
        if p is False:
            break
    if p is True:
        ans += '1'
    else:
        ans += '0'

    a12 = int(s[0])^int(s[2])^int(s[4])^int(s[6])
    a13 = int(s[0])^int(s[1])^int(s[4])^int(s[5])
    a23 = int(s[0])^int(s[1])^int(s[2])^int(s[3])
    a123 = int(s[0])^int(s[1])^int(s[2])^int(s[3])^int(s[4])^int(s[5])^int(s[6])

    if a12 or a13 or a23 or a123:
        ans += '0'
    else:
        ans += '1'

    return ans



def task11(strs):
    anss = []
    for string in strs:
        anss.append(task10(string))
    ans = ""
    for i in range(5):
        p = 1
        for el in anss:
            p &= int(str(el[i]))
        ans += str(p)
    return ans


import math


def task12(string):
    ln = int(math.log(len(string), 2))
    if 2 ** ln != len(string):
        return "Error: invalid length of boolean function"
    varrs = [0] * ln
    func = []
    for i in range(len(string)):
        if string[i] == '1':
            s = ""
            for j in range(ln):
                if varrs[j] == 0:
                    s += '0'
                else:
                    s += '1'
            func.append(s)
        for j in range(ln - 1, -1, -1):
            if varrs[j] == 0:
                varrs[j] = 1
                break
            varrs[j] = 0
    f1 = func.copy()
    t = True
    while t:
        t = False
        varsnew = []
        varscheck = [0] * len(func)
        for i in range(len(func)):
            for j in range(i + 1, len(func)):
                k = 0
                ind = 0
                for kk in range(ln):
                    if func[i][kk] != func[j][kk]:
                        k += 1
                        ind = kk
                if k == 1:
                    s = ""
                    for kk in range(ln):
                        if kk == ind:
                            s += '-'
                        else:
                            s += func[i][kk]
                    varsnew.append(s)
                    varscheck[i] = 1
                    varscheck[j] = 1
        if len(varsnew) > 0:
            t = True
        for i in range(len(func)):
            if varscheck[i] == 0:
                if not (func[i] in varsnew):
                    varsnew.append(func[i])
        func = varsnew

    matrix = []
    for i in range(len(func)):
        m = []
        for j in range(len(f1)):
            t = True
            for k in range(ln):
                t &= (func[i][k] == '-' or func[i][k] == f1[j][k])
            if t:
                m.append(1)
            else:
                m.append(0)
        matrix.append(m)

    ans = set()

    while len(matrix) > 0:
        for i in range(len(matrix)):
            if sum(matrix[i]) == len(matrix[0]):
                ans.add(func[i])
                matrix = []
                break
        if len(matrix) == 0:
            break

        sm = [0] * len(matrix[0])
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                sm[j] += matrix[i][j]

        ind = 0
        for i in range(len(matrix[0])):
            if sm[i] == 1:
                ind = 1
                for j in range(len(matrix)):
                    if matrix[j][i] == 1:
                        a = []
                        ans.add(func[j])
                        for k in range(len(matrix[j])):
                            if matrix[j][k] == 1:
                                a.append(k)
                        for i in range(len(a) - 1, -1, -1):
                            for el in matrix:
                                el.pop(a[i])
                        matrix.pop(j)
                        func.pop(j)
                        break
                break
        if ind == 1:
            continue

        ind = 0
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                if i == j:
                    continue
                if all(matrix[i] >= matrix[j] for i in range(len(matrix[0]))):
                    matrix.pop(j)
                    ind = 1
                    break
            if ind == 1:
                break
        if ind == 1:
            continue
        else:
            break

    if '-' * ln in ans:
        ans.remove('-' * ln)

    answer = ""
    for el in ans:
        if answer != '':
            answer += '|'
        for i in range(ln):
            if el[i] == '-':
                continue
            if el[i] == '0':
                answer += '~'
            answer += 'x' + str(i + 1)

    return answer

