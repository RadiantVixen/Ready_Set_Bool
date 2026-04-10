

def  eval_formula(s)->bool:
    if not s:
        return False

    stack = []

    for c in s:
        if c == '0' or c =='1':
            stack.append(int(c))
        elif c == '!':
            if len(stack) < 1:
                print("the formula is invalid")
                return False
            a = stack.pop()
            stack.append(not a)
        else:
            if len(stack) < 2:
                print("the formula is invalid")
                return False
            a = stack.pop()
            b = stack.pop()
            if c == '&':
                stack.append(a & b)
            elif c == '|':
                stack.append(a | b)
            elif c == '^':
                stack.append(a ^ b)
            elif c == '>':
                stack.append(not (b == 0  and a == 1))
            elif c == '=':
                stack.append(a == b)
            else:
                print("the formula is invalid")
                return False
    
    if len(stack) > 1:
        print("the formula is invalid")
        return False
    return bool(stack[0])



if __name__ == "__main__":

    print("{}", eval_formula("11&"))
    # false
    print("{}", eval_formula("00|"))
    # true
    print("{}", eval_formula("01>"))
    # true
    print("{}", eval_formula("10="))
    # false
    print("{}", eval_formula("1011||="))
    # true


