bodys = ['repeat i <- operations { set.add(i) }',
    'repeat i <- operations { set.add(i) }; repeat i <- operations { set.contains(i) }',
    'repeat i <- operations { set.add(i) }; repeat i <- operations { set.remove(i) }',
    'repeat i <- operations { set.add(i % 10) }',
    'repeat i <- operations / 1000 { set.add(i) }; repeat i <- operations  { set.contains(i % (operations / 1000)) }',
    'repeat i <- operations { set.add(i); set.remove(i) }'  ]
names = ['add',
    'add_contains',
    'add_remove',
    'add_same',
    'few_add_contains',
    'add_remove_mixed']
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
        bs_outf = open('./generated/' + n + '-' + t + '.enc', 'w')
        res = bs_gen.replace('__SET__', t)
        res = res.replace('__RUNS__', '10')
        res = res.replace('__WORKERS__', '8')
        res = res.replace('__OPERATIONS__', '10000') #300000
        res = res.replace('__WAIT_GET__', bs_wg[i])
        res = res.replace('__BODY__', b)
        bs_outf.write(res)
        bs_outf.close()
        i = i + 1
    j = j + 1
