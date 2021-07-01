def Council(t):
    t = sorted(t, key=lambda a: a[0]) #시작 시간 정렬
    t = sorted(t, key=lambda a: a[1]) #종료 시간 정렬
    meeting_count = 0  #알고리즘
    end_time = 0
    for i in range(len(t)):
        if t[i][0] >= end_time:
            meeting_count += 1
            end_time = t[i][1]
    return meeting_count
# 입력
N = int(input())
T = []
for i in range(N):
    first, second = map(int, input().split())
    T.append([first, second])
print(Council(T))


