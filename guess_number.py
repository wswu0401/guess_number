# 產生一個隨機整數1~100 (不要印出來)
# 讓使用者重複輸入數字去猜
# 猜對的話 印出 "終於猜對了"
# 猜錯的話 要告訴他 比答案大/小

import random # 載入亂數，已經在library，但是不常用，需要import才能用
start = input('請決定隨機數字範圍開始值: ')
end = input('請決定隨機數字範圍結束值: ')
start = int(start)
end = int(end)
r = random.randint(start, end) # 從1到100產生一個隨機整數, 第4版本由使用者自己決定隨機數的開始結束範圍
count = 0
while True:
	count += 1 # 跟count = count + 1 一樣 只是寫法不同
	num = input('請猜數字: ')
	num = int(num)
	if num == r:
		print('你猜中了!')
		print('這是你猜的第', count,'次')	
		break
	elif num > r:
		print('你猜的數字比答案大')
	elif num < r:
		print('你猜的數字比答案小')	
	print('這是你猜的第', count,'次')		