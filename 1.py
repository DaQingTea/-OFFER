#1.获取行列的最大值
row = len(array)
col = len(array[1])

#从右上角（即array[row][0]）开始判断大小，若比结果大则i--，若比结果小则j++

#若数组为空直接返回
if row=0 and col=0:
	return False

i = 0
j = col - 1
while (i < row and j >= 0 ):
	if array[i][j] == target:
		return True

	elif array[i][j] > target:
			i -= 1

	else array[i][j] < target:
			j += 1
return False