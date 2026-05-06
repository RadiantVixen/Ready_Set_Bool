
class node:
    def __init__(self, val, left = None, right=None):
        self.val = val
        self.left = left
        self.right = right


def print_tree(node, prefix="", is_left=True):
    if node is None:
        return

    print(prefix + ("├── " if is_left else "└── ") + str(node.val))

    if node.left or node.right:
        if node.left:
            print_tree(node.left, prefix + ("│   " if is_left else "    "), True)
        if node.right:
            print_tree(node.right, prefix + ("│   " if is_left else "    "), False)


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

    # print(print_tree(stack[0]))
    return stack[0]


def simplify(tree) -> str:
    if not tree:
        return None
    
    if tree.val == '>':
        return node('|', simplify(node('!', (tree.left))), tree.right)
    
    if tree.val == '=':
        left = node('&', simplify(tree.left), simplify(tree.right))
        right = node('&', simplify(node('!', tree.left)), simplify(node('!', tree.right)))
        return node('|', left, right)
    
    if tree.val == '^':
        left = node('&', simplify(tree.left), simplify(node('!', tree.right)))
        right = node('&', simplify(node('!', tree.left)), simplify(tree.right))
        return node('|', left, right)

    if tree.val == '!':
        child = tree.left
        if child.val == '!':
            return simplify(child.left)
        
        if child.val == '&':
            return node('|', simplify(node('!', child.left)), simplify(node('!', child.right)))

        if child.val == '|':
            return node('&', simplify(node('!', child.left)), simplify(node('!', child.right)))
        
        return node('!', simplify(child))

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
    print("result = ", negation_normal_form("AB|!"))
    print("result = ", negation_normal_form("AB>"))
    print("result = ", negation_normal_form("AB="))
    print("result = ", negation_normal_form("AB|C&!"))
