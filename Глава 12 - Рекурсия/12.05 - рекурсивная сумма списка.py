def rec_sum(in_list: list):
    if len(in_list) == 1:
        return in_list[0]
    else:
        return in_list[0] + rec_sum(in_list[1:])

def main():
    res = rec_sum([1, 15, 3, 3, 9, 3, 6])
    print(res)

main()
