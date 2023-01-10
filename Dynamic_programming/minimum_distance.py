blocks = [
    {"gym": False, 'school': True, 'store': False},
    {"gym": True, 'school': False, 'store': False},
    {"gym": True, 'school': True, 'store': False},
    {"gym": False, 'school': True, 'store': False},
    {"gym": False, 'school': True, 'store': True}
]

req = ['gym', 'school', 'store']

"""
block 1 = [1, 0, 4]
block 2 = [0, 1, 3]
block 3 = [0, 0, 2]
block 4 = [1, 0, 1]
block 5 = [2, 0, 0]

The minimum distance is block 4

    [0, 1],
    [0, 0],
    [1, 0],
    [0, 0],
    [1, 0]
]
"""


def min_distance(block, req):
    # create a hash map of array to store each requirement where they exist at all blocks
    req_cache = {i: [] for i in req}
    # run an iteration on all blocks
    for i in range(len(block)):
        # run an iteration for the keys in the req cache created above
        for j in req_cache:
            # if on block 0, gym is true, we want to append to the gym array the block number
            if block[i][j] == True:
                # so we will append 0 to the school array
                req_cache[j].append(i)
    # create a hash map of array to store each block
    block_min = {i: [] for i in range(len(block))}
    # create an array to store
    res = []
    # run an iteration on all block min
    for i in block_min:
        # use the req cache we got above, get the key and value
        for k, v in req_cache.items():
            # set min value to 0
            min_val = 0
            # check if on the first block, gym is false, if it is false
            if block[i][k] == False:
                # for j in value, i - j would give me an array but i want the minimum as my final value
                min_val = min([abs(i - j) for j in v])
                block_min[i].append(min_val)
            else:
                block_min[i].append(min_val)
        res.append(max(block_min[i]))
    return f"requs_cache: {req_cache},\n apart_min: {block_min},\n res: {res},\n res_index: {res.index(min(res))}"


apart = [
    {"gym": False, 'school': True, 'store': False},
    {"gym": True, 'school': False, 'store': False},
    {"gym": True, 'school': True, 'store': False},
    {"gym": False, 'school': True, 'store': False},
    {"gym": False, 'school': True, 'store': True}
]
requs = ['gym', 'school', 'store']
print("The minimum distance is block: \n", min_distance(apart, requs))
