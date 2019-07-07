import pos_ngram as png
import char_ngram as cng
import func_words as fw
import freq_dictionary as freqd
import text_info as ti
import angle as ang
import statistics


def test_all_pairs(test, method):
    all = []
    for i in range(1, 7):
        for j in range(1, 7):
            file1 = "simple_text_{}_{}.txt".format(str(i), str(test))
            file2 = "simple_text_{}_{}.txt".format(str(j), str(test))
            res = method(file1, file2)
            if (i >= j):
                res = 0.0
            else:
                all.append(res)
            if (True or "freq" not in method.__name__):
                print("{0:9.3f}".format(float(res)), end='')
        print()
    print(statistics.mean(all))


def test_all_similars(method):
    all = []
    for i in range(1, 7):
        file1 = "simple_text_{}_{}.txt".format(str(i), "1")
        file2 = "simple_text_{}_{}.txt".format(str(i), "2")
        res = method(file1, file2)
        all.append(res)
        if (True or "freq" not in method.__name__):
            print("{0:9.3f}".format(float(res)), end='')
    print(statistics.mean(all))


def test_all_pairs_file(test, method):
    all = []
    with open("{}_stats.txt".format(method.__name__), 'a') as ouf:
        ouf.write("--set{}\n".format(str(test)))
        for i in range(1, 7):
            for j in range(1, 7):
                file1 = "simple_text_{}_{}.txt".format(str(i), str(test))
                file2 = "simple_text_{}_{}.txt".format(str(j), str(test))
                res = method(file1, file2)
                if (i >= j):
                    res = 0.0
                else:
                    all.append(res)
                if (True or "freq" not in method.__name__):
                    ouf.write("{0:9.3f}".format(float(res)))
            ouf.write("\n")
        ouf.write(str(statistics.mean(all)) + "\n")


def test_all_similars_file(method):
    all = []
    with open("{}_stats.txt".format(method.__name__), 'a') as ouf:
        for i in range(1, 7):
            file1 = "simple_text_{}_{}.txt".format(str(i), "1")
            file2 = "simple_text_{}_{}.txt".format(str(i), "2")
            res = method(file1, file2)
            all.append(res)
            if (True or "freq" not in method.__name__):
                ouf.write("{0:9.3f}".format(float(res)))
        ouf.write("{0:9.3f}\n".format(statistics.mean(all)))


def freq_only(file1, file2):
    f1 = freqd.get_freq(file1, local_thre)
    f2 = freqd.get_freq(file2, local_thre)
    perc = 100 * (max(f1, f2) - min(f1, f2)) / min(f1, f2)
    return perc


def cng_only(file1, file2):
    v1 = cng.get_vector(file1)
    v2 = cng.get_vector(file2)
    return ang.angle_between(v1, v2)


def png_only(file1, file2):
    v1 = png.get_vector(file1)
    v2 = png.get_vector(file2)
    return ang.angle_between(v1, v2)


def fw_only(file1, file2):
    v1 = fw.get_vector(file1)
    v2 = fw.get_vector(file2)
    return ang.angle_between(v1, v2)


def ti_only(file1, file2):
    v1 = ti.get_vector(file1)
    v2 = ti.get_vector(file2)
    return ang.dist_between(v1, v2)


def cng_png(file1, file2):
    vc1 = cng.get_vector(file1)
    vc2 = cng.get_vector(file2)
    vp1 = png.get_vector(file1)
    vp2 = png.get_vector(file2)
    v1 = vc1 + vp1
    v2 = vc2 + vp2
    return ang.angle_between(v1, v2)


def png_fw(file1, file2):
    vp1 = png.get_vector(file1)
    vp2 = png.get_vector(file2)
    vf1 = fw.get_vector(file1)
    vf2 = fw.get_vector(file2)
    v1 = vp1 + vf1
    v2 = vp2 + vf2
    return ang.angle_between(v1, v2)


def cng_fw(file1, file2):
    vc1 = cng.get_vector(file1)
    vc2 = cng.get_vector(file2)
    vf1 = fw.get_vector(file1)
    vf2 = fw.get_vector(file2)
    v1 = vc1 + vf1
    v2 = vc2 + vf2
    return ang.angle_between(v1, v2)


def png_cng_fw(file1, file2):
    vc1 = cng.get_vector(file1)
    vc2 = cng.get_vector(file2)
    vp1 = png.get_vector(file1)
    vp2 = png.get_vector(file2)
    vf1 = fw.get_vector(file1)
    vf2 = fw.get_vector(file2)
    v1 = vc1 + vp1 + vf1
    v2 = vc2 + vp2 + vf2
    return ang.angle_between(v1, v2)


def png_cng_fw_freq(file1, file2):
    vc1 = cng.get_vector(file1)
    vc2 = cng.get_vector(file2)
    vp1 = png.get_vector(file1)
    vp2 = png.get_vector(file2)
    vf1 = fw.get_vector(file1)
    vf2 = fw.get_vector(file2)
    f1 = freqd.get_freq(file1, local_thre)
    f2 = freqd.get_freq(file2, local_thre)
    v1 = vc1 + vp1 + vf1
    v1.append(f1 / 50)
    v2 = vc2 + vp2 + vf2
    v2.append(f2 / 50)
    return ang.angle_between(v1, v2)


def test_all_freq(thre=5000):
    for i in range(1, 7):
        file1 = "simple_text_{}_{}.txt".format(str(i), "1")
        file2 = "simple_text_{}_{}.txt".format(str(i), "2")
        res = freqd.get_freq(file1, thre)
        print("{0}_{1}: {2:0.3f}".format(str(i), "1", res))
        res = freqd.get_freq(file2, thre)
        print("{0}_{1}: {2:0.3f}".format(str(i), "2", res))


local_thre = 5000


''' 
thres = [5000, 1000, 200, 100, 40, 10, 2]
for t in thres:
    local_thre = t
    test_all_similars_file(freq_only)
'''
'''
test_all_pairs_file(1, png_only)
test_all_pairs_file(2, png_only)
test_all_similars_file(png_only)
'''
