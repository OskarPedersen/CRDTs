IDValues = """
----------- BEGINNING of manually created 'generic' IDValue and TimeValue --------------
--- They are put here so that they know of list, but collections.enc is re genereated
passive class IDValue_int
  id : int
  value : int

  def init(id : int, value : int) : void {
    this.id = id;
    this.value = value;
  }

  def equals(n : IDValue_int) : bool {
    (this.id == n.id) and (this.value == n.value);
  }

  def toInt() : int {
    this.id + this.value * 73
  }

passive class IDValue_List_int
  id : int
  value : List_int

  def init(id : int, value : List_int) : void {
    this.id = id;
    this.value = value;
  }

  def equals(n : IDValue_List_int) : bool {
    let value = this.value;
    let addressA = embed int ((int64_t )#{value}); end;
    let addressB = embed int ((int64_t )#{n}); end;
    (this.id == n.id) and (addressA == addressB);
  }

  def toInt() : int {
    let value = this.value;
    this.id + embed int ((int64_t )#{value}); end
  }



passive class TimeValue_int
    time : int
    value : int

    def init(value : int) : void {
      this.time = currentTime();
      this.value = value;
    }

    def toInt() : int {
      this.time + this.value * 73
    }

passive class TimeValue_List_int
    time : int
    value : List_int

    def init(value : List_int) : void {
      this.time = currentTime();
      this.value = value;
    }

    def toInt() : int {
      let value = this.value;
      this.time + embed int ((int64_t )#{value}); end
    }
----------- END of manually created 'generic' IDValue and TimeValue---------------


"""

list_t = ['int', 'HashMapEntry_int_int', 'HashMapEntry_int_TimeOp',
    'HashMapEntry_int_HashSet_int', 'HashMapEntry_NodeID_RGANode',
    'HashMapEntry_NodeID_int', 'HashMapEntry_VertexPair_int', 'FromTo',
    'HashMapEntry_int_List_int', 'HashMapEntry_FromTo_int',
    'HashMapEntry_FromTo_TimeValue', 'HashMapEntry_FromTo_HashSet_int',
    'HashMapEntry_FromTo_HashSet_IDNext', 'HashMapEntry_IDNext_int',
    'HashMapEntry_IDValue_List_int_int', 'HashMapEntry_IDValue_int_int',
    'HashMapEntry_int_HashSet_IDValue_List_int',
    'HashMapEntry_VertexPair_HashSet_IDValue_int',
    'HashMapEntry_FromTo_HashSet_IDValue_int', 'HashMapEntry_int_TimeValue',
    'HashMapEntry_VertexPair_TimeValue', 'HashMapEntry_int_TimeValue_List_int',
    'HashMapEntry_VertexPair_TimeValue_int', 'HashMapEntry_FromTo_TimeValue_int']
list_inf = open('gen_list.enc', 'r')
list_gen = list_inf.read()
list_inf.close()
outf = open('collections.enc', 'w')
outf.write('bundle collections where\n')
outf.write('import collections_data\n')
outf.write(IDValues)
for l in list_t:
    outf.write(list_gen.replace('__TYPE__', l))


hm_k =      ['int',     'int',          'int',                 'NodeID',        'NodeID',       'VertexPair',   'int',              'FromTo',       'FromTo',           'FromTo',               'FromTo',               'IDNext',       'int',                              'IDValue_int',  'IDValue_List_int', 'VertexPair',               'FromTo',                       'int',              'VertexPair',       'int',                      'VertexPair',           'FromTo']
hm_v =      ['int',     'TimeOp',       'HashSet_int',         'RGANode',       'int',          'int',          'List_int',         'int',          'TimeValue',        'HashSet_int',          'HashSet_IDNext',       'int',          'HashSet_IDValue_List_int',         'int',          'int',              'HashSet_IDValue_int',      'HashSet_IDValue_int',          'TimeValue',        'TimeValue',        'TimeValue_List_int',       'TimeValue_int',        'TimeValue_int']
hm_eq =     ['a == b',  'a == b',       'a == b',              'a.equals(b)',   'a.equals(b)',  'a.equals(b)',  'a == b',           'a.equals(b)',  'a.equals(b)',      'a.equals(b)',          'a.equals(b)',          'a.equals(b)',  'a == b',                           'a.equals(b)',  'a.equals(b)',      'a.equals(b)',              'a.equals(b)',                  'a == b',           'a.equals(b)',      'a == b',                   'a.equals(b)',          'a.equals(b)']
hm_to =     ['a',       'a',            'a',                   'a.toInt()',     'a.toInt()',    'a.toInt()',    'a',                'a.toInt()',    'a.toInt()',        'a.toInt()',            'a.toInt()',            'a.toInt()',    'a',                                'a.toInt()',    'a.toInt()',        'a.toInt()',                'a.toInt()',                    'a',                'a.toInt()',        'a',                        'a.toInt()',            'a.toInt()']
hm_k_null = ['-1',      '-1',           '-1',                  'null',          'null',         'null',          '-1',              'null',         'null',             'null',                 'null',                 'null',         '-1',                               'null',         'null',             'null',                     'null',                         '-1',               'null',             '-1',                       'null',                 'null']
hm_v_null = ['-1',      'null : TimeOp','null : HashSet_int',  'null : RGANode','-1',           '-1',            'null : List_int', '-1',           'null : TimeValue', 'null : HashSet_int',   'null : HashSet_IDNext','-1',           'null : HashSet_IDValue_List_int',  '-1',           '-1',               'null : HashSet_IDValue_int','null : HashSet_IDValue_int',  'null : TimeValue', 'null : TimeValue', 'null : TimeValue_List_int','null : TimeValue_int', 'null : TimeValue_int']
hm_inf = open('gen_hashmap.enc', 'r')
hm_gen = hm_inf.read()
hm_inf.close()
#hm_outf = open('hashmap.enc', 'w')
#hm_outf.write('bundle hashmap where\n')
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
    outf.write(res)

    i = i + 1



hs_t = ['int', 'NodeID', 'VertexPair', 'FromTo', 'IDNext', 'IDValue_List_int', 'IDValue_int']
hs_null = ['-1', 'null', 'null', 'null','null', 'null', 'null']
hs_inf = open('gen_hashset.enc', 'r')
hs_gen = hs_inf.read()
hs_inf.close()
#hs_outf = open('hashset.enc', 'w')
#hs_outf.write('bundle hashset where\n')
i = 0
for t in hs_t:
    n = hs_null[i]
    res = hs_gen.replace('__TYPE__', t)
    res = res.replace('__NULL__', n)
    outf.write(res)
    i = i + 1
outf.close()


pm_k = ['FromTo', 'VertexPair', 'int']
pm_v = ['int', 'int', 'List_int']
pm_v_null = ['-1', '-1', 'null : List_int']
pm_to = ['key.from + key.to * 73', 'key.a + key.b * 73', 'key * 73']
pm_infs = ['gen_map_div_time.enc', 'gen_map_op_or.enc', 'gen_map_sub.enc']
pm_b = ['map_div_time', 'map_op_or', 'map_sub']
bi = 0
for inf in pm_infs:
    infile = open(inf, 'r')
    pm_gen = infile.read()
    infile.close()
    pm_outf = open(inf[4:], 'w')
    pm_outf.write('bundle ' + pm_b[bi] + ' where')
    i = 0
    for k in pm_k:
        res = pm_gen.replace('__KEY__', pm_k[i])
        res = res.replace('__VALUE__', pm_v[i])
        res = res.replace('__TOINT__', pm_to[i])
        res = res.replace('__VALUE_NULL__', pm_v_null[i])
        if not (inf == 'gen_map_div_time.enc' and k == 'int'):
            pm_outf.write(res)
        i = i + 1
    pm_outf.close()
    bi = bi + 1


t_set_sp = ['ActiveHashMap_FromTo_int', 'SubMap_FromTo_int', 'DivTimeMap_FromTo_int', 'OpOrMap_FromTo_int']
t_set_edge = ['ActiveHashMap_VertexPair_int', 'SubMap_VertexPair_int', 'DivTimeMap_VertexPair_int', 'OpOrMap_VertexPair_int']
t_set_neighbours = ['ActiveHashMap_int_List_int', 'SubMap_int_List_int', 'DivTimeMap_int_List_int', 'OpOrMap_int_List_int']
t_reps = ['0', '1', '2', '4', '8']
#t_get = ['get', '']
t_inf = open('gen_traffic.enc', 'r')
t_gen = t_inf.read()
t_inf.close()

for sp in t_set_sp:
    for edge in t_set_edge:
        for neighbour in t_set_neighbours:
            for rep in t_reps:
                version = sp[0] + edge[0] + neighbour[0]
                if version == 'AAA' and rep != '0':
                    continue
                if version[2] == 'D' or version[2] == 'O': # segfaults for some reason
                    continue
                t_outf = open('traffic/traffic-' + version + rep +'.enc', 'w')
                res = t_gen.replace('__SP_SET__', sp)
                res = res.replace('__E_SET__', edge)
                res = res.replace('__N_SET__', neighbour)
                res = res.replace('__VERSION__', '"' + version + rep +'"')
                if version[0] == 'A':
                    res = res.replace('__REPLICATION_SP__', '')
                else:
                    res = res.replace('__REPLICATION_SP__', rep)

                if version[1] == 'A':
                    res = res.replace('__REPLICATION_E__', '')
                else:
                    res = res.replace('__REPLICATION_E__', rep)

                if version[2] == 'A':
                    res = res.replace('__REPLICATION_N__', '')
                else:
                    res = res.replace('__REPLICATION_N__', rep)

                if neighbour == 'DivTimeMap_int_List_int':
                    res = res.replace('__NEIGHBOUR_DIV_TIME_START__', '')
                    res = res.replace('__NEIGHBOUR_DIV_TIME_END__', '')
                    res = res.replace('__NEIGHBOUR_DEFAULT_START__', '{-')
                    res = res.replace('__NEIGHBOUR_DEFAULT_END__', '-}')
                else:
                    res = res.replace('__NEIGHBOUR_DIV_TIME_START__', '{-')
                    res = res.replace('__NEIGHBOUR_DIV_TIME_END__', '-}')
                    res = res.replace('__NEIGHBOUR_DEFAULT_START__', '')
                    res = res.replace('__NEIGHBOUR_DEFAULT_END__', '')
                t_outf.write(res)
                t_outf.close()
