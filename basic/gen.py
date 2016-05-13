list_t = ['int', 'HashMapEntry_int_int', 'HashMapEntry_int_TimeOp',
    'HashMapEntry_int_HashSet_int', 'HashMapEntry_NodeID_RGANode',
    'HashMapEntry_NodeID_int']
list_inf = open('gen_list.enc', 'r')
list_gen = list_inf.read()
list_inf.close()
list_outf = open('list.enc', 'w')
list_outf.write('bundle list where\n')
for l in list_t:
    list_outf.write(list_gen.replace('__TYPE__', l))
list_outf.close()


hm_k =      ['int',     'int',          'int',                 'NodeID',        'NodeID']
hm_v =      ['int',     'TimeOp',       'HashSet_int',         'RGANode',       'int']
hm_eq =     ['a == b',  'a == b',       'a == b',              'a.equals(b)',   'a.equals(b)']
hm_to =     ['a',       'a',            'a',                   'a.toInt()',     'a.toInt()']
hm_k_null = ['-1',      '-1',           '-1',                  'null',          'null']
hm_v_null = ['-1',      'null : TimeOp','null : HashSet_int',  'null : RGANode','-1']
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
    kn = hm_k_null[i]
    vn = hm_v_null[i]
    res = hm_gen.replace('__KEY__', k)
    res = res.replace('__VALUE__', v)
    res = res.replace('__EQUAL__', e)
    res = res.replace('__TOINT__', t)
    res = res.replace('__KEY_NULL__', kn)
    res = res.replace('__VALUE_NULL__', vn)
    hm_outf.write(res)

    i = i + 1
hm_outf.close()



hs_t = ['int', 'NodeID']
hs_null = ['-1', 'null']
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