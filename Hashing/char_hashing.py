# def charHash(s,q):
#     hash_list = [0]*26
    
#     for ch in s:
#         ascii_val = ord(ch)
#         index = ascii_val - 97
#         hash_list[index] +=1
#     for ch in q:
#         ascii_val = ord(ch)
#         index = ascii_val - 97
#         print(hash_list[index])
# s = ['a','z','y','x','a','a','a','a','z','y','y']
# q = ['d','a','y','x']
# charHash(s,q)

def charHash(s,q):
    hash_map = {}
    for ch in s:
        hash_map[ch] = hash_map.get(ch,0) + 1
    print(hash_map)
    for ch in q:
        print(hash_map.get(ch,0))

s = "aAAbB12@#!3!@#aa"
q = "aA1#z"
charHash(s,q)