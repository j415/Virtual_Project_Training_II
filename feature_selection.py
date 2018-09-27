import operator
import csv
import pandas as pd


def main(y, z):
    dic_adnum = {}
    dic_adsum = {}
    dic_admin = {}
    dic_cnum = {}
    ln = []
    ls = []
    for i in range(y, z):
        if lost[i] not in ls:
            ls.append(lost[i])
    for j in range(len(ls)):
        name1 = ls[j]
        num = 0
        for i in range(y, z):
            if lost[i] == name1:
                num = num + 1
        dic_cnum[name1] = num

    for i in range(y, z):
        if lcst[i] not in ln:
            ln.append(lcst[i])
    for j in range(len(ln)):
        name = ln[j]
        time = 0
        min = 100000000
        sum = 0
        num = 0
        for i in range(y, z):
            if lcst[i] == name:
                if time == 0:
                    time = ltst[i]
                else:
                    sum = sum + (ltst[i] - time)
                    if min > ltst[i] - time:
                        min = ltst[i] - time
                    time = ltst[i]
                num = num + 1
        dic_admin[name] = min
        dic_adnum[name] = num
        if num == 1:
            dic_adsum[name] = 100000000
        else:
            dic_adsum[name] = sum / num

    cook = zero_or_infinity(dic_adnum, dic_adsum, dic_admin, ls, dic_cnum)[0]
    adnum = zero_or_infinity(dic_adnum, dic_adsum, dic_admin, ls, dic_cnum)[1]
    adsum = zero_or_infinity(dic_adnum, dic_adsum, dic_admin, ls, dic_cnum)[2]
    admin = zero_or_infinity(dic_adnum, dic_adsum, dic_admin, ls, dic_cnum)[3]

    # cook = remove_brackets(cook)
    # # print("原始admin", admin)
    # admin = remove_brackets(admin)
    # # print("修改admin:", admin)
    # adnum = remove_brackets(adnum)
    # adsum = remove_brackets(adsum)
    lt = (ltst[z - 1] - ltst[y]) / (z - y)

    w_csv_file(len(ls), len(ln), cook, admin, adnum, adsum, z - y, lt, lal[y])
    print(y, "-", z)


def zero_or_infinity(dic_adnum, dic_adsum, dic_admin, ls, dic_cnum):
    dic_li = []
    for k, w in dic_admin.items():
        dic_li.append(dic_admin[k])

    sorted_x = sorted(dic_adnum.items(), key=operator.itemgetter(1))
    sor = dict(sorted_x)

    dic_li = list(sor.keys())
    if len(dic_li) > 5:
        li = dic_li[-1:-6:-1]
    else:
        li = dic_li[::-1]
        for i in range(5 - len(dic_li)):
            li.append(0)

    cook = []
    adnum = []
    adsum = []
    admin = []
    for i in li:
        if i == 0:
            adnum.append(0)
            admin.append(100000000)
            adsum.append(100000000)
        else:
            adnum.append(dic_adnum[i])
            adsum.append(dic_adsum[i])
            admin.append(dic_admin[i])

    for i in range(0, 6):
        cook.append(0)
    for i in ls:
        if dic_cnum[i] == 1:
            cook[0] = cook[0] + 1
        if dic_cnum[i] == 2:
            cook[1] = cook[1] + 1
        if dic_cnum[i] == 3:
            cook[2] = cook[2] + 1
        if dic_cnum[i] == 4:
            cook[3] = cook[3] + 157
        if (dic_cnum[i] > 4 and dic_cnum[i] < 11):
            cook[4] = cook[4] + 1
        if dic_cnum[i] > 10:
            cook[5] = cook[5] + 1
    return (cook, adnum, adsum, admin)


# def remove_brackets(li):
#     list = []
#     for x in li:
#         list.append(str(x))
#
#     list = ' '.join(list)
#
#     return list


def w_csv_file(len_ls, len_ln, cook, admin, adnum, adsum, x, lt, lal):
    with open("files/testd1.csv", "a+", newline="") as csvfile:
        writer = csv.writer(csvfile)

        # 先写入columns_name
        writer.writerow(
            [len_ls, len_ln, cook[0], cook[1], cook[2], cook[3], cook[4], cook[5], admin[0], admin[1], admin[2],
             admin[3], admin[4], adnum[0], adnum[1], adnum[2], adnum[3], adnum[4], adsum[0], adsum[1], adsum[2],
             adsum[3], adsum[4], x, lt, lal])


def w_one_file():
    with open("files/testd1.csv", "a+", newline="") as csvfile:
        writer = csv.writer(csvfile)

        # 先写入columns_name
        writer.writerow(
            ["len_ls", "len_ln", "cook[0]", "cook[1]", "cook[2]", "cook[3]", "cook[4]", "cook[5]", "admin[0]",
             "admin[1]", "admin[2]", "admin[3]", "admin[4]", "adnum[0]", "adnum[1]", "adnum[2]", "adnum[3]", "adnum[4]",
             "adsum[0]", "adsum[1]", "adsum[2]",
             "adsum[3]", "adsum[4]", "x", "lt", "lal"])


def run():
    dic_start = {}
    dic_end = {}
    ip = lyst[0]
    dic_start[ip] = 0
    for i in range(len(lyst)):
        if ip != lyst[i]:
            dic_end[ip] = i - 1
            ip = lyst[i]
            dic_start[ip] = i
    li = []
    for i in range(len(lyst)):
        if lyst[i] not in li:
            li.append(lyst[i])

    for j in range(len(li) - 1):
        main(dic_start[li[j]], dic_end[li[j]] + 1)


if __name__ == '__main__':
    titanic = pd.read_csv('files/day1.csv')
    lost = list(titanic["V3"])
    lyst = list(titanic["V4"])
    lcst = list(titanic["V17"])
    ltst = list(titanic["V10"])
    lal = list(titanic["V22"])

    w_one_file()

    run()
