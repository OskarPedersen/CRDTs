bs_t = ['ActiveHashSet_int', 'DivTimeSet', 'OpOrSet', 'SubSet']
bs_inf = open('gen_bench_set.enc', 'r')
bs_gen = bs_inf.read()
bs_inf.close()
i = 0
for t in bs_t:
    bs_outf = open(t + '.enc', 'w')
    res = bs_gen.replace('__SET__', t)
    res = res.replace('__RUNS__', '1')
    res = res.replace('__WORKERS__', '4')
    res = res.replace('__OPERATIONS__', '1000000')
    bs_outf.write(res)
    bs_outf.close()
    i = i + 1
