# look and say sequence
# len(a[30]) = ?
# a = [1, 11, 21, 1211, 111221, ...]


def looksay(number):
    result = ""
    x = str(number)
    if len(x) == 1:
        return "1" + x

    cur = x[0]

    count = 1
    for ch in x[1:]:
        if ch == cur:
            count += 1
        else:
            break

    result += str(count)
    result += cur
    extra = ""
    if len(x) > count:
        extra = looksay(x[count:])

    return result + extra


# print(num)
# print(len(num))


def looksay_iter(number):

    x = str(number)
    result = ""
    cur = x[0]
    count = 1
    for ch in x[1:]:
        if ch == cur:
            count += 1
        else:
            result += str(count)
            result += cur
            count = 1
            cur = ch

    result += str(count)
    result += cur

    return result


num = "1"
for i in range(31):
    print(len(num))
    num = looksay_iter(num)
