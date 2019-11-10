# 演算法分析機測
# 學號姓名 : 10527142彭義翔/10527239林威廷/10527245 陳宏溢
# 中原大學資訊工程學系
import numpy as np

tempW = input("輸入算式(單獨一個0結束):" )
#work 答案
work = []

while tempW != '0':
	
	#放進來
	work.append(tempW)
	#算有幾個左括號跟右括號 不一樣ERROR
	count = len(tempW) 
	reighB = 0 #右括號 )
	leftB = 0 #左括號 (
	"""print ("work" , end =":")
	print(work)
	print ("tempw" , end =":")
	print(tempW)"""
	while  count > 0 :
		if tempW[count-1] == ')' :
			reighB +=1
		if tempW[count-1] == '(' :
			leftB +=1
		
		"""print("count", end = ":")
		print(count)
		print("reighB",end = ':')
		print(reighB)
		print("leftB",end = ':')
		print(leftB)"""
		count -=1
		
	#print ("ourtwork" , end =":")
	#print(work)	
	if 	reighB != leftB :
		work[len(work)-1] = "Error"
	#沒ERROR可以做	
	elif reighB == leftB :
		work[len(work)-1] = eval(work[len(work)-1])
		
	#讀
	tempW = input()

	
#印出答案
if work :
	print("******")
	print( "The Anser is :")
	n = 0
	while n <= len(work)-1 :
		print("	", end = " ")
		print( work[n] )
		n += 1
