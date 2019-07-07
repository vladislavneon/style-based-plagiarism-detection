import complex as cmp
import order


def cng_only(file1, file2, c):
    if (cmp.cng_only(file1, file2) < c):
        return 0
    else:
        return 1


def png_only(file1, file2, c):
    if (cmp.png_only(file1, file2) < c):
        return 0
    else:
        return 1


def fw_only(file1, file2, c):
    if (cmp.fw_only(file1, file2) < c):
        return 0
    else:
        return 1


def cng_png(file1, file2, c):
    if (cmp.cng_png(file1, file2) < c):
        return 0
    else:
        return 1


def png_fw(file1, file2, c):
    if (cmp.png_fw(file1, file2) < c):
        return 0
    else:
        return 1


def cng_fw(file1, file2, c):
    if (cmp.cng_fw(file1, file2) < c):
        return 0
    else:
        return 1


def png_cng_fw(file1, file2, c):
    if (cmp.png_cng_fw(file1, file2) < c):
        return 0
    else:
        return 1


def freq_only(file1, file2, c):
    if (cmp.freq_only(file1, file2) < c):
        return 0
    else:
        return 1


def png_cng_fw_freq(file1, file2, c):
    if (cmp.png_cng_fw_freq(file1, file2) < c):
        return 0
    else:
        return 1


def make_dump(method):
    ans = []
    for i in range(len(order.order) - 1):
        f1 = "common\\" + order.order[i] + ".txt"
        f2 = "common\\" + order.order[i + 1] + ".txt"
        cur_ans = method(f1, f2)
        ans.append(cur_ans)
    return ans


def eval_corp(dump, c=0.0):
    ans = []
    for i in range(len(dump)):
        if (dump[i] < c):
            cur_ans = 0
        else:
            cur_ans = 1
        ans.append(cur_ans)
    right = 0
    prec_sum = 0
    recall_sum = 0
    for i in range(40):
        if (order.right_ans[i] == 1):
            recall_sum += 1
            if (ans[i] == 1):
                prec_sum += 1
                right += 1
        else:
            if (ans[i] == 1):
                prec_sum += 1
    if (prec_sum == 0):
        prec = 0
    else:
        prec = right / prec_sum
    recall = right / recall_sum
    fm = 2 * recall * prec
    if ((prec + recall) == 0):
        fm = 0
    else:
        fm /= (prec + recall)
    return (prec, recall, fm)


def test_method(method, l, r, debug="n"):
    fn = "{}_results.csv".format(method.__name__)
    dump = make_dump(method)
    with open(fn, 'w') as ouf:
        for i in range(l, r):
            c = i / 100
            t = eval_corp(dump, c)
            s = "{0:0.3f};{1:0.3f};{2:0.3f};{3:0.3f}\n".format(c, t[0], t[1], t[2])
            if (debug == "n"):
                ouf.write(s)
            else:
                print(s, end='')
