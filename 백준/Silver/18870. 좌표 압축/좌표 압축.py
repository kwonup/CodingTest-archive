import sys
input = sys.stdin.readline
n = int(input())
coord = list(map(int,input().split())) #좌표담는 리스트
coord_sorted = sorted(list(set(coord))) #좌표에서 중복제거하고 정렬한 리스트
coord_dict={} #정렬된 리스트의 값과 인덱스를 key와 value롤 저장할수 있도록 딕셔너리 선언(리스트로 탐색하면 속도가 너무 느려지기때문)

#정렬된 리스트를 돌면서 딕셔너리에 key,value값으로 각각 값과 인덱스 추가
for i in range(len(coord_sorted)):
    coord_dict[coord_sorted[i]] = i
 
for i in range(n):
    coord[i] = str(coord_dict[coord[i]])

print(' '.join(coord))
