import sys
input = sys.stdin.readline

# 입력 처리
n = int(input())
video = [list(map(int, input().strip())) for _ in range(n)]

# 쿼드트리 함수 정의
def quadtree(N, vlist):
    # 모든 값이 동일한 경우
    if all(v == vlist[0][0] for row in vlist for v in row):
        return str(vlist[0][0])

    # N이 1인 경우 처리
    if N == 1:
        return str(vlist[0][0])

    # 영역 분할
    half = N // 2
    top_left = [row[:half] for row in vlist[:half]]
    top_right = [row[half:] for row in vlist[:half]]
    bottom_left = [row[:half] for row in vlist[half:]]
    bottom_right = [row[half:] for row in vlist[half:]]

    # 결과 조합
    return '(' + quadtree(half, top_left) + quadtree(half, top_right) + \
           quadtree(half, bottom_left) + quadtree(half, bottom_right) + ')'

# 결과 출력
print(quadtree(n, video))