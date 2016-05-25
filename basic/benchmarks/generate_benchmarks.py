bodys = ['repeat i <- operations { set.add(i) }']
names = ['add']
j = 0
for b in bodys:
    n = names[j]

    bs_t = ['ActiveHashSet_int',    'DivTimeSet',   'OpOrSet',  'SubSet']
    bs_wg = ['get',                 '',             '',         '']
    bs_inf = open('gen_bench_set.enc', 'r')
    bs_gen = bs_inf.read()
    bs_inf.close()
    i = 0
    for t in bs_t:
        bs_outf = open(n + t + '.enc', 'w')
        res = bs_gen.replace('__SET__', t)
        res = res.replace('__RUNS__', '1')
        res = res.replace('__WORKERS__', '4')
        res = res.replace('__OPERATIONS__', '300000')
        res = res.replace('__WAIT_GET__', bs_wg[i])
        res = res.replace('__BODY__', b)
        bs_outf.write(res)
        bs_outf.close()
        i = i + 1
    j = j + 1
