
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


def simplify(tree) -> node:
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



def distribute(tree):
    if not tree:
        return

    if tree.val == '|' and tree.left and tree.left.val == '&':
        A = tree.left.left
        B = tree.left.right
        C = tree.right

        return node('&',
            distribute(node('|', A, C)),
            distribute(node('|', B, C))
        )

    if tree.val == '|' and tree.right and tree.right.val == '&':
        A = tree.left
        B = tree.right.left
        C = tree.right.right

        return node('&',
            distribute(node('|', A, B)),
            distribute(node('|', A, C))
        )

    return node(
    tree.val,
    distribute(tree.left),
    distribute(tree.right)
    )



def tree_to_expression(tree) -> str:
    if not tree:
        return ""
    # if tree.val == '!':
    #     return tree_to_expression(tree.left) + '!'
    return tree_to_expression(tree.left) + tree_to_expression(tree.right) + tree.val


def conjunctive_normal_form(expr):
    tree = expression_to_tree(expr)
    simplified = simplify(tree)
    distributed = distribute(simplified)
    return tree_to_expression(distributed)


if __name__ == "__main__":
    print("{}", conjunctive_normal_form("AB&!"))
    print("{}", conjunctive_normal_form("AB|!"))
    print("{}", conjunctive_normal_form("AB|C&"))
    print("{}", conjunctive_normal_form("AB|C|D|"))
    print("{}", conjunctive_normal_form("AB&C&D&"))
    print("{}", conjunctive_normal_form("AB&!C!|"))
    print("{}", conjunctive_normal_form("AB|!C!&"))


# my output

# {} A!B!|
# {} A!B!&
# {} AB|C&
# {} AB|C|D|
# {} AB&C&D&
# {} A!B!|C!|
# {} A!B!&C!&


# the supject output


# // A!B!|
# // A!B!&
# // AB|C&
# // ABCD|||
# // ABCD&&&
# // A!B!C!||
# // A!B!C!&&