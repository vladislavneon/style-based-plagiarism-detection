def make_dump(method):
    ans = []
    for i in range(20):
        for j in range(i + 1, 20):
            author1 = i // 4
            num1 = i % 4 + 1
            author2 = j // 4
            num2 = j % 4 + 1
            if ((author1 == author2) or (num1 == num2)):
                f1 = "travel\\" + "{}_{}.txt".format(str(author1), str(num1))
                f2 = "travel\\" + "{}_{}.txt".format(str(author2), str(num2))
                cur_ans = method(f1, f2)
                ans.append(cur_ans)
    return ans


def gen_right_ans():
    right_ans = []
    for i in range(20):
        for j in range(i + 1, 20):
            author1 = i // 4
            num1 = i % 4 + 1
            author2 = j // 4
            num2 = j % 4 + 1
            if ((author1 == author2) or (num1 == num2)):
                if (author1 == author2):
                    right_ans.append(0)
                else:
                    right_ans.append(1)
    return right_ans


def eval_corp(dump, right_ans, c=0.0):
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
        if (right_ans[i] == 1):
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
    fn = "{}_topic_results.csv".format(method.__name__)
    right_ans = gen_right_ans()
    dump = make_dump(method)
    with open(fn, 'w') as ouf:
        for i in range(l, r):
            c = i / 100
            t = eval_corp(dump, right_ans, c)
            s = "{0:0.3f};{1:0.3f};{2:0.3f};{3:0.3f}\n".format(c, t[0], t[1], t[2])
            if (debug == "n"):
                ouf.write(s)
            else:
                print(s, end='')
