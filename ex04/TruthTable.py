from collections import defaultdict

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
            stack.append(int(not a))
        else:
            if len(stack) < 2:
                print("the formula is invalid")
                return False
            a = stack.pop()
            b = stack.pop()
            if c == '&':
                stack.append(int(a & b))
            elif c == '|':
                stack.append(int(a | b))
            elif c == '^':
                stack.append(int(a ^ b))
            elif c == '>':
                stack.append(int(not (b == 0  and a == 1)))
            elif c == '=':
                stack.append(int(a == b))
            else:
                print("the formula is invalid")
                return False
    
    if len(stack) != 1:
        print("the formula is invalid")
        return False
    return bool(stack[0])



def TruthTable(s):
    mapping = defaultdict(int)
    sl = list(s)
    
    for i in range(len(s)):
        if s[i].isalpha():
            mapping[s[i]] = 0

    tab = list(mapping.keys())

    print("| " + " | ".join(tab) + " | = |")
    print("|" + "---|" * (len(tab) + 1))

    def replace():
        nonlocal sl
        nonlocal mapping

        for i in range(len(s)):
            if s[i].isalpha():
                if mapping[s[i]] == 1:
                    sl[i] = '1'
                else:
                    sl[i] = '0'


    def rec(tab, i):
        nonlocal mapping
        nonlocal sl
        
        if len(tab) == i:
            replace()
            result = eval_formula("".join(sl))
            print("| " + " | ".join(str(mapping[v]) for v in tab) + f" | {int(result)} |")
            return
        
        mapping[tab[i]] = 0
        rec(tab, i + 1)

        mapping[tab[i]] = 1
        rec(tab, i + 1)


    rec(tab, 0)




if __name__ == "__main__":
    TruthTable("AB&C|")

