# 產生一個隨機整數1~100 (不要印出來)
# 讓使用者重複輸入數字去猜
# 猜對的話 印出 "終於猜對了"
# 猜錯的話 要告訴他 比答案大/小

import random # 載入亂數，已經在library，但是不常用，需要import才能用
r = random.randint(1, 100) # 從1到100產生一個隨機整數
while True:
	num = input('請猜數字: ')
	num = int(num)
	if num == r:
		print('你猜中了!')
		break
	elif num > r:
		print('你猜的數字比答案大')
	elif num < r:
		print('你猜的數字比答案小')		