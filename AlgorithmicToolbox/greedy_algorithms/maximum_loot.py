from sys import stdin

def best_item(w, v):
    n = len(v)
    best_index = 0
    max_val_per_unit = 0
    for i in range(n):
        if w[i] > 0: # if weight > 0
            if v[i] / w[i] > max_val_per_unit: # if v_i / w_i > max value per unit
                best_index = i
                max_val_per_unit = v[i] / w[i]
    return best_index

def knapsack(W, w, v):
    n = len(w)
    best_list = [0] * n
    total_value = 0
    for _ in range(n):
        if W == 0:
            return best_list, total_value
        best_i = best_item(w, v)
        a = min(w[best_i], W)
        best_list[best_i] += a
        total_value += a * (v[best_i] / w[best_i])
        w[best_i] -= a
        W -= a
    return best_list, total_value

if __name__ == '__main__':
    data = list(map(int, stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2) : 2]
    best_list, total_value = knapsack(capacity, weights, values)
    # print(best_list)
    print(f"{total_value:.4f}")
    # print(values, weights)
    # print(best_item(weights, values))



    # n, W = map(int, input().split())
    # v_w = []
    # for i in range(n):
    #     v, w = map(int, input().split())
    #     v_w.append([v,w])

    # best_list, total_value = knapsack(W, v_w)
    # # print(best_list)
    # print(f"{total_value:.4f}")

    # # print(best_item(v_w))

    