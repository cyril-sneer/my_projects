def rec_max(in_list: list):
    if len(in_list) == 1:
        return in_list[0]
    else:
        rm = rec_max(in_list[1:])
        if in_list[0] > rm:
            return in_list[0]
        else:
            return rm

def main():
    res = rec_max([1, 15, 3, 3, 9, 3, 6])
    print(res)

main()


