#10527142
#10527142 10527239 10527245
#彭義翔 林威廷 陳宏溢

if __name__=='__main__' :
	high = input("輸入input(0 0結束):" )
	temp = high.split()
	firsthigh = temp[0]
	secondhigh = temp[1]
	firstT = input()
	first = firstT.split()
	secondT = input()
	second = secondT.split()
	"""print("firsthigh:", end='')
	print(firsthigh)
	print("secondhigh:", end='')
	print(secondhigh)
	print("first:", end='')
	print(first)
	print("second:", end='')
	print(second)"""
	while high != '0 0' : 
		totaltower = 1	#第幾座塔
		NFT = 0		#塔的高度
		if high == "0 0" :
			break 
		else :
			#LCS問題
			#先建表
			m = len(first)
			n = len(second)
			form = [[0 for i in range(n+1)] for j in range(m+1)]
			direct = [[0 for i in range(n+1)] for j in range(m+1)]
			for i in range(0, m) :
				for j in range(0, n) :
					if first[i]==second[j] :
						form[i+1][j+1] = form[i][j]+1
						direct[i+1][j+1] = "yes"
					elif form[i+1][j]>form[i][j+1] :
						form[i+1][j+1] = form[i+1][j]
						direct[i+1][j+1] = "left"
					else :	#form[i+1][j]>=form[i][j+1] 默認找上(一樣的話)
						form[i+1][j+1] = form[i][j+1]
						direct[i+1][j+1] = "up"	
			#從最底層數上來
			#如果方向是往左上長度就加1
			while m != 0 and n != 0 :
				if direct[m][n] == "yes" :
					NFT += 1 
					m -= 1
					n -= 1
				elif direct[m][n] == "left" :
					n -= 1 
				else :	#direct[m][n] == "up"
					m -= 1
			
			print("Twin Towers #", end="")
			print(totaltower)
			print("Number of Tiles : ", end="")
			print(NFT)
		
		totaltower += 1
		high = input("輸入input(0 0結束):" )
		temp = high.split()
		firsthigh = temp[0]
		secondhigh = temp[1]
		firstT = input()
		first = firstT.split()
		secondT = input()
		second = secondT.split()
