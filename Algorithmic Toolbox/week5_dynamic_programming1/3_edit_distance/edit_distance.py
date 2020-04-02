# Uses python3
def edit_distance(s, t):
    sn = len(s)
    tn = len(t)
    dp_result = [[x for x in range(sn + 1)] for y in range(tn + 1)]
    for y in range(tn + 1):
        dp_result[y][0] = y

    for i in range(1, sn+1):
        for j in range(1, tn+1):
            insert_op = dp_result[j-1][i] + 1
            delete_op = dp_result[j][i-1] + 1
            match_op = dp_result[j-1][i-1]
            mismatch_op = dp_result[j-1][i-1] + 1
            if s[i-1] == t[j-1]:
                dp_result[j][i] = min(insert_op, delete_op, match_op)
            else:
                dp_result[j][i] = min(insert_op, delete_op, mismatch_op)

    return dp_result[tn][sn]

if __name__ == "__main__":
    print(edit_distance(input(), input()))
