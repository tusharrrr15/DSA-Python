#finding how many times the number from one list occured in other list
#Brute force
# def occur1(n,m):
#     for num in m:
#         count = 0
#         for x in n:
#             if x == num:
#                 count += 1
#         print(count)

# n = [5,3,2,2,1,5,5,7,5,10]
# m = [10,111,1,9,5,67,2]
# occur1(n,m)

#Optimal Solution

# def occur2(n,m):
#     hash_list = [0]*11
#     for num in n:
#         hash_list[num] += 1
#     for x in m:
#         if x<1 or x>10:
#             print(0)
#         else:
#             print(hash_list[x])

# n = [5,3,2,2,1,5,5,7,5,10]
# m = [10,111,1,9,5,67,2]
# occur2(n,m)

#Using Dictionary
# def occur3(n,m):
#     frq_dict = dict()
#     for i in range(0,len(n)):
#         if n[i] in frq_dict:
#             frq_dict[n[i]] += 1
#         else:
#             frq_dict[n[i]] = 1
#     for x in m:
       
#         print(frq_dict.get(x,0))
        
# n = [5,3,2,2,1,5,5,7,5,10]
# m = [10,111,1,9,5,67,2]
# occur3(n,m)

#using dictionary hash_map
def occur4(n, m):
    hash_map = {}
    for i in n:
        hash_map[i] = hash_map.get(i, 0) + 1
    print(hash_map)

    for x in m:
        print(hash_map.get(x, 0))

n = [5, 3, 2, 2, 1, 5, 5, 7, 5, 10,111, 67,111,67]
m = [10, 111, 1, 9, 5, 67, 2]
occur4(n, m)

            
    
