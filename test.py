import sys
if __name__ == "__main__":
    # 读取第一行的n
    features = {}
    n = int(sys.stdin.readline().strip())
    m = int(sys.stdin.readline().strip())
    ans = 0
    for i in range(m):
        # 读取每一行
        line = sys.stdin.readline().strip()
        # 把每一行的数字分隔后转化成int列表
        values = list(map(int, line.split()))
        featurelen = values[0]

    print(ans)