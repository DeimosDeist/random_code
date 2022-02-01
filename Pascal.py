def compute_child(parent_line, i):
    try:
        P1 = parent_line[i - 1]
        P2 = parent_line[i]
    except:
        P2 = 0
    return P1 + P2


def build_next_line(parent_line):
    result = []
    for i in range(len(parent_line) + 1):
        if i == 0:
            result.append(1)
        else:
            result.append(compute_child(parent_line, i))
    return result


def binomial(n, k):
    p = [1]
    for i in range(n):
        p = build_next_line(p)
    return p[k]
