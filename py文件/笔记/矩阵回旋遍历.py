def LuoXuanBianLi(matrix):
    if matrix == []:
        return []

    result = []
    top, bottom, left, right = 0, len(matrix) - 1, 0, len(matrix[0]) - 1

    while top <= bottom and left <= right:
        # 从左到右遍历顶行
        for i in range(left, right + 1):
            result.append(matrix[top][i])
        top += 1

        # 从上到下遍历右列
        for i in range(top, bottom + 1):
            result.append(matrix[i][right])
        right -= 1

        # 如果还未超出底部，遍历底行
        if top <= bottom:
            for i in range(right, left - 1, -1):
                result.append(matrix[bottom][i])
            bottom -= 1

        # 如果还未超出左侧，遍历左列
        if left <= right:
            for i in range(bottom, top - 1, -1):
                result.append(matrix[i][left])
            left += 1

    return result

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print(LuoXuanBianLi(matrix))
# [1, 2, 3, 6, 9, 8, 7, 4, 5]
