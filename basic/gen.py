list_t = ['int', 'HashMapEntry_int_int']
list_inf = open('gen_list.enc', 'r')
list_gen = list_inf.read()
list_inf.close()
list_outf = open('list.enc', 'w')
list_outf.write('bundle list where\n')
for l in list_t:
    list_outf.write(list_gen.replace('__TYPE__', l))
list_outf.close()


hm_k = ["int"]
hm_v = ["int"]
hm_eq = ["a == b"]
hm_to = ["a"]
hm_null = ["-1"]
hm_inf = open('gen_hashmap.enc', 'r')
hm_gen = hm_inf.read()
hm_inf.close()
hm_outf = open('hashmap.enc', 'w')
hm_outf.write('bundle hashmap where\n')
i = 0
for k in hm_k:
    v = hm_v[i]
    e = hm_eq[i]
    t = hm_to[i]
    n = hm_null[i]
    res = hm_gen.replace('__KEY__', k)
    res = res.replace('__VALUE__', v)
    res = res.replace('__EQUAL__', e)
    res = res.replace('__TOINT__', t)
    res = res.replace('__NULL__', n)
    hm_outf.write(res)

    i = i + 1
hm_outf.close()



hs_t = ["int"]
hs_null = ["-1"]
hs_inf = open('gen_hashset.enc', 'r')
hs_gen = hs_inf.read()
hs_inf.close()
hs_outf = open('hashset.enc', 'w')
hs_outf.write('bundle hashset where\n')
i = 0
for t in hs_t:
    n = hs_null[i]
    res = hs_gen.replace('__TYPE__', t)
    res = res.replace('__NULL__', n)
    hs_outf.write(res)
    i = i + 1
hs_outf.close()
