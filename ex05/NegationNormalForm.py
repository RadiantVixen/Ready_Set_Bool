
class node:
    def __init__(self, val, left = None, right=None):
        self.val = val
        self.left = left
        self.right = right


def print_infix(node):
    if node is None:
        return ""
    if node.val == '!':
        return f"![{print_infix(node.left)}]"
    return f"[{print_infix(node.left)} {node.val} {print_infix(node.right)}]"

def expression_to_tree(exp) -> node:
    stack = []

    for c in exp:
        if c.isalpha():
            stack.append(node(c))
        elif c == '!':
            a = stack.pop()
            stack.append(node('!', a))
        else:
            a = stack.pop()
            b = stack.pop()
            stack.append(node(c, b, a))

    print(print_infix(stack[0]))
    return stack[0]


def simplify(tree) -> str:
    if not tree:
        return None
    
    if tree.val == '>':
        return simplify(node('|', simplify(node('!', (tree.left))), tree.right))
    
    if tree.val == '=':
        left = node('&', simplify(tree.left), simplify(tree.right))
        right = node('&', simplify(node('!', tree.left)), simplify(node('!', tree.right)))
        return node('|', left, right)
    
    if tree.val == '^':
        left = node('&', simplify(tree.left), simplify(node('!', tree.right)))
        right = node('&', simplify(node('!', tree.left)), simplify(tree.right))
        return node('|', left, right)

    if tree.val == '!':
        left = tree.left
        if left.val == '!':
            return simplify(left.left)
        
        if left.val == '&':
            return node('|', simplify(node('!', tree.left)), simplify(tree.right))

        if left.val == '|':
            return node('&', simplify(node('!', left.left)), simplify(node('!', left.right)))
        
        return node('!', simplify(left))

    return node(tree.val, simplify(tree.left), simplify(tree.right))


def tree_to_expression(tree) -> str:
    if not tree:
        return ""
    # if tree.val == '!':
    #     return tree_to_expression(tree.left) + '!'
    return tree_to_expression(tree.left) + tree_to_expression(tree.right) + tree.val


def negation_normal_form(expr):
    tree = expression_to_tree(expr)
    simplified = simplify(tree)
    return tree_to_expression(simplified)


if __name__ == "__main__":
    print("result = ", negation_normal_form("AB&!"))
