from annoy import AnnoyIndex


def index(pool):
    flag = True
    xb = []  # array to be indexed
    xb = list(pool)
    d = len(pool[0])
    nb = len(xb)  # database size
    nq = 1  # nb of queries

    if flag:
        annoy_index(d, xb)
    else:
        pass
    return 'annoy_index.ann'


def similar_index(target, pool, build, k, include_distance):
    b = []  # array to be indexed
    xb = list(pool)
    d = len(pool[0])
    nb = len(xb)  # database size
    nq = 1  # nb of queries

    xq = 0
    query_vector = target

    xq = xb.index(query_vector)
    I = annoy_search(xq, build, k, d, include_distance)

    return explain_result(I)


def _index_and_search(k, target, pool, flag=False):
    xb = []  # array to be indexed
    xb = list(pool)

    if target not in xb:
        xb.append(target)
    d = 3
    nb = len(xb)  # database size
    nq = 1  # nb of queries
    if flag:
        annoy_index(d, xb)
    # print("End Indexing"+str(datetime.datetime.now()))

    xq = 0
    query_vector = target

    try:
        xq = xb.index(query_vector)
    except:
        #         print('query appended')
        xb.append(query_vector)
        xq = xb.index(query_vector)
        # print("Start Searching"+str(datetime.datetime.now()))
    I = annoy_search(xq, 'annoy_index.ann', k, d)  # search results
    # print("End Searching"+str(datetime.datetime.now()))
    # return {"I":I}
    return explain_result(I)


#     except Exception as e:
#         raise
#         return {"message":"query_id not found in index"}

def get_value_for_key(key, object):
    if key in object:
        return object[key]
    else:
        return ""


def annoy_index(d, xb):
    t = AnnoyIndex(d)  # Length of item vector that will be indexed
    for i, x in enumerate(xb):
        t.add_item(i, x)

    t.build(20)  # 10 trees
    t.save('annoy_index.ann')


def annoy_search(xq, index, k, d, include_distances):
    u = AnnoyIndex(d)
    u.load(index)  # super fast, will just mmap the file
    I = u.get_nns_by_item(xq, k, include_distances=include_distances)
    return I


def explain_result(I):
    #     print(I)

    return {"message": I}
