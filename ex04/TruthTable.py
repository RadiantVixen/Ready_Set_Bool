from ex03.BooleanEvaluation import eval_formula

def  print_truth_table(s):
    if not s:
        return False
    
    n = 0
    
    map = {chr(i): 0 for i in range(ord('A'), ord('Z') + 1)}

    for c in s:
        if c.isalphabet():
            n += 1

    
    s = list(s)
    for i in range(len(s)):
        if s[i].alphabet():
            if map[s[i]] == 1:
                s[i] = '1'
            else:
                s[i] = '0'
    eval_formula(str(s))



if __name__ == "__main__" :
     print("eval_formula:", eval_formula("AB&C|"))
     print("print_truth_table:", print_truth_table("AB&C|"))


