# def solution(participant, completion):
#     hashDict = {}
#     hashSum = 0
#     for part in participant:
#         hashDict[hash(part)] = part
#         hashSum += hash(part)
        
#     for comp in completion:
#         hashSum -= hash(comp)

#     return hashDict[hashSum]

    
# print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))




# def solution(participant, completion):
#     participant.sort()
#     completion.sort()

    
#     for i in range(len(completion)):
#         if participant[i] != completion[i]:
#             return participant[i]
        
    

#     return participant[(len(participant)-1)]
#     #1. 두 리스트를 sorting 한다
#     #2. completion list의 length 만큼 돌면서
#     return answer

# print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))


####BFS
####아이디어, 시간복잡도, 알고리즘을 볼것

# a, b = map(int, input().split())
# print(a, b)

# num_list = list(map(int, input().split()))
# print(num_list)

# a, b = input().split()
# print(a, b)

# string = [input() for _ in range(3)]
# print(string)

# mylist = [list(map(int, input().split())) for i in range(4)]
# print(mylist)

# n = int(input())
# array = list(map(int, input().split()))
# print(array)
# min = array[0]
# max = array[0]

# for i in array :
#     if i >= max:
#         max = i
#     if i <= min:
#         min = i

# print(min, max)



# arr = [list(map(int, input().split())) for _ in range(5)]
# print(arr)
# human_hap = [0]*5
# print(human_hap)
# for i in range(5):
#     sum = 0
#     for j in range(4):
#         sum += arr[i][j]
    
#     human_hap[i] = sum
#     score = max(human_hap)

# max_num = human_hap[0]
# for i in range(5):
#     if human_hap[i] == score:
#         break
            

# print(i+1, score)






a = [list(map, input().split())]
print(a)