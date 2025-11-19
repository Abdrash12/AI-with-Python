def alphabeta(node, is_max_turn, tree, values, alpha, beta):
    if node not in tree or len(tree[node]) == 0:
        return values.get(node, 0)  

    if is_max_turn:
        print("the max node is:",node)
        best = float('-inf')
        for child in tree[node]:
            val = alphabeta(child, False, tree, values, alpha, beta)
            best = max(best, val)
            alpha = max(alpha, best)
            print("max is evaluating:",child,"aplha:",alpha,"beta:",beta)
            if beta <= alpha:
                break
        return best
    else:
        best = float('inf')
        print("the min node is:",node)
        for child in tree[node]:
            val = alphabeta(child, True, tree, values, alpha, beta)
            best = min(best, val)
            beta = min(beta, best)
            print("min is evalutaing:",child,"aplha:",alpha,"beta:",beta)
            if beta <= alpha:
                break
        return best

tree = {
    'a': ['b', 'c', 'd'],
    'b': ['e', 'f'],
    'c': ['g', 'h', 'f'],
    'd': ['k', 'l'],
    'h': ['m', 'n'],
    'j': ['o', 'p'],
    'e': [],
    'f': [],
    'g': [],
    'm': [],
    'n': [],
    'o': [],
    'p': [],
    'k': [],
    'l': [],
}

values = {
    'e': 4, 'f': 5, 'g': 6, 'm': 3, 'n': 4, 'o': 7, 'p': 9, 'k': 3, 'l': 8
}

final_value = alphabeta('a', True, tree, values, float('-inf'), float('inf'))
print("answer =", final_value)
