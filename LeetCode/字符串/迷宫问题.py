# 利用动态规划和递归解
def jud(x, y, l, ll, lll):  # 求x,y点坐标在迷宫里的可能走法，即向上，向下，向左，向右
    n, m = len(l)-1, len(l[0])-1  # l为迷宫位置二维图，ll为迷宫的每点从起点到该点
    k = []  # 的最短路径，lll为记录正在探索的从起点到该点的路线用以避免走重复
    if x+1 <= n and (x+1, y) not in lll and l[x+1][y] != 1:
        k += [(x+1, y)]
    if x-1 >= 0 and (x-1, y) not in lll and l[x-1][y] != 1:
        k += [(x-1, y)]
    if y+1 <= m and (x, y+1) not in lll and l[x][y+1] != 1:
        k += [(x, y+1)]
    if y-1 >= 0 and (x, y-1) not in lll and l[x][y] != 1:
        k += [(x, y-1)]
    return k


def mg(x, y, l, ll, lll):  # x,y为该点坐标，其余同上，探索x,y的走法
    k = jud(x, y, l, ll, lll)  # k为可能的走法
    lll += [(x, y)]  # lll位置储存
    if len(k) > 0:  # 是否为可走
        for v in k:
            x1, y1 = v
            if not ll[x1][y1]:  # 如果x1,y1位置 还没有路径信息，用x,y位置进
                ll[x1][y1] = ll[x][y]+[(x1, y1)]  # 行更新
            # 如果x1,y1之前储存的路径#要长于从x,y的路径到x1,y1的，则更新x1,y1路径信息
            if len(ll[x1][y1]) >= len(ll[x][y])+1:
                ll[x1][y1] = ll[x][y]+[(x1, y1)]
            mg(x1, y1, l, ll, lll.copy())  # 再对x1,y1 这点进行探索
    return False


while True:
    try:
        nn, mm = list(map(int, input().split()))
        l, ll, lll = [], [], []
        for i in range(nn):
            l += [list(map(int, input().split()))]
        for i in range(nn):
            ll.append([])
            for j in range(mm):
                ll[i].append([])
        ll[0][0] = [(0, 0)]
        mg(0, 0, l, ll, lll)   # 设置起始点为（0，0），你也可以设为其他点为起始，
        for v in ll[-1][-1]:  # 来探索其他点到任意一点的最短位置
            print("(%d,%d)" % (v[0], v[1]))  # ll[-1][-1], 指的是将右下角一点设
    except:
        break
# 为终点并打印出来，你也可以求其他点，如ll[2][3],来实现任意
# 两点求最短路
