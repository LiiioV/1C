import cv2

img = None
matrix = [[-1, -1, -1],
          [-1, -1, -1],
          [-1, -1, -1]]
H = W = 0


def get_symbol(i, j):
    if img[(2 * i + 1) * H // 7][(W - H) // 2 + (2 * j + 1) * H // 7][3] != 0:
        return 1
    cnt = 0
    for x in range(i * H // 3 + 1, (i + 1) * H // 3):
        this_pix_a = img[x][(W - H) // 2 + (2 * j + 1) * H // 7][3]
        prev_pix_a = img[x - 1][(W - H) // 2 + (2 * j + 1) * H // 7][3]
        if this_pix_a != prev_pix_a:
            cnt += 1
    if cnt >= 3:
        return 0
    return -1


def is_col(i):
    return a[i][0] == a[i][1] == a[i][2] != -1


def is_row(i):
    return a[0][i] == a[1][i] == a[2][i] != -1


def is_diag_0():
    return a[0][0] == a[1][1] == a[2][2] != -1


def is_diag_1():
    return a[2][0] == a[1][1] == a[0][2] != -1


def get_line():
    for i in range(3):
        if is_col(i):
            return i + 1
        if is_row(i):
            return i + 4

    if is_diag_0():
        return 7
    if is_diag_0():
        return 8


def color_col(i):
    global img
    for x in range(H):
        img[(2 * i + 1) * H // 7][(W - H) // 2 + x] = [0, 0, 0, 1]
        img[(2 * i + 1) * H // 7 + 1][(W - H) // 2 + x] = [0, 0, 0, 1]
        img[(2 * i + 1) * H // 7 - 1][(W - H) // 2 + x] = [0, 0, 0, 1]


def color_row(i):
    global img
    for x in range(H):
        img[x][(W - H) // 2 + (2 * i + 1) * H // 7] = [0, 0, 0, 1]
        img[x][(W - H) // 2 + (2 * i + 1) * H // 7 + 1] = [0, 0, 0, 1]
        img[x][(W - H) // 2 + (2 * i + 1) * H // 7 - 1] = [0, 0, 0, 1]


def color_diag_0():
    global img
    for x in range(H):
        img[x][(W - H) // 2 + x] = [0, 0, 0, 1]
        if x != 0:
            img[x - 1][(W - H) // 2 + x] = [0, 0, 0, 1]
            img[x][(W - H) // 2 + x - 1] = [0, 0, 0, 1]


def color_diag_1():
    global img
    for x in range(H):
        img[H - x][(W - H) // 2 + x] = [0, 0, 0, 1]
        if x != H:
            img[H - x - 1][(W - H) // 2 + x] = [0, 0, 0, 1]
        if x != 0:
            img[H - x][(W - H) // 2 + x - 1] = [0, 0, 0, 1]


def solve():
    filename = input()
    global img
    global matrix
    global H, W
    img = cv2.imread(filename, cv2.COLOR_RGB2RGBA)
    H = img.shape[0]
    W = img.shape[1]
    for i in range(3):
        for j in range(3):
            matrix[i][j] = get_symbol(i, j)

    ans = get_line()

    if 1 <= ans <= 3:
        color_col(ans - 1)
    elif 4 <= ans <= 6:
        color_row(ans - 4)
    elif ans == 7:
        color_diag_0()
    elif ans == 8:
        color_diag_1()

    cv2.imshow("result_" + filename, png)
    cv2.waitKey(0)
    cv2.imwrite("result_" + filename, png)


def main():
    solve()


if __name__ == "__main__":
    main()
