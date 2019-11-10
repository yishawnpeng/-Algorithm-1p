# 演算法分析機測
# 學號姓名 : 10527142彭義翔/10527239林威廷/10527245 陳宏溢
# 中原大學資訊工程學系
import numpy as np

inputnum = 1
while inputnum > 0 : 
	inputnum = int( input('輸入一個正整數') )
	if inputnum == 0 :	exit(0)
	
	inputlist = input('輸入集合')
	#print ( 'GG' + str(len(inputlist))) 
	if len(inputlist) == 2 :	 # 空
		continue 				#跳出本次迴圈
	
	#整理字串 inputlist 去頭去尾把逗號換空格
	inputlist = inputlist.replace(',',' ') 
	inputlist = inputlist.replace('{','') 
	inputlist = inputlist.replace('}','') 
	#print(len(inputlist))
	
	
	"""worklist = [ inputlist.split()[0], inputlist.split()[1], inputlist.split()[2] ]
	print(worklist,end='')
	print("here")"""
	#print(inputlist)
	#print(len(worklist),end='')
	#print("***")
	#print(worklist[0])
	#把字串合起來
	worklist = inputlist.split() ;
	#print(worklist)
	"""worklist = [] 
	if len(inputlist) == 3 :
		worklist = [ inputlist.split(" ")[0], inputlist.split()[1] ]
	elif len(inputlist) == 1 :
		worklist = [ inputlist.split()[0] ]
	elif len(inputlist) == 2 :
		worklist = [ inputlist.split()[0], inputlist.split()[1] ]
	elif len(inputlist) == 5 :
		worklist = [ inputlist.split()[0], inputlist.split()[1], inputlist.split()[2] ]
	elif len(inputlist) == 6 :
		worklist = [ inputlist.split()[0], inputlist.split()[1], inputlist.split()[2] ]
	elif len(inputlist) == 7 :
		worklist = [ inputlist.split()[0], inputlist.split()[1], inputlist.split()[2], inputlist.split()[3] ]
	elif len(inputlist) == 10 :
		worklist = [ inputlist.split()[0], inputlist.split()[1], inputlist.split()[2], inputlist.split()[3], inputlist.split()[4] ]
	elif len(inputlist) == 13 :
		worklist = [ inputlist.split()[0], inputlist.split()[1], inputlist.split()[2], inputlist.split()[3], inputlist.split()[4], \
					 inputlist.split()[5] ]
	elif len(inputlist) == 12 :
		worklist = [ inputlist.split()[0], inputlist.split()[1], inputlist.split()[2], inputlist.split()[3], inputlist.split()[4], \
					 inputlist.split()[5] ]
	elif len(inputlist) == 15 :
		worklist = [ inputlist.split()[0], inputlist.split()[1], inputlist.split()[2], inputlist.split()[3], inputlist.split()[4], \
					 inputlist.split()[5], inputlist.split()[6] ]
	elif len(inputlist) == 17 :
		worklist = [ inputlist.split()[0], inputlist.split()[1], inputlist.split()[2], inputlist.split()[3], inputlist.split()[4], \
					 inputlist.split()[5], inputlist.split()[6], inputlist.split()[7] ]
	elif len(inputlist) == 19 :
		worklist = [ inputlist.split()[0], inputlist.split()[1], inputlist.split()[2], inputlist.split()[3], inputlist.split()[4], \
					 inputlist.split()[5], inputlist.split()[6], inputlist.split()[7], inputlist.split()[8] ]
	elif len(inputlist) == 20 :
		worklist = [ inputlist.split()[0], inputlist.split()[1], inputlist.split()[2], inputlist.split()[3], inputlist.split()[4], \
					 inputlist.split()[5], inputlist.split()[6], inputlist.split()[7], inputlist.split()[8], inputlist.split()[9] ]"""

	#排序集合
	worklist.sort()
	
	"""print( "inputlist",end='' )
	print( inputlist )
	print( "worklist",end='' )
	print( worklist )
	
	print( len(inputlist),end='' )
	print( "inputlist長度" )
	print( len(worklist),end='' )
	print( "worklist長度" )"""
	#計算
	count = 0 
		
	#使用DP動態規劃法
	# (0可不可以用\空集合來達成-最大子集合\)--(目標數字可不可以用\空集合來達成-最大子集合\)
	#再來找初始情況
	#建立二維陣列
	#[目標數字][集合的表] 
	row = inputnum+1
	column = ( len(worklist)+1 )
	form = np.array( (row)*[(column)*[True]] )

	#如果你要目標數字0 那麼空集合都可以成立(空集合的和為0)
	for i in range( 0, column) :
		form[ 0, i] = True
	
	#如果你要的數字不是0 但你只有空集合可以成合成(全都不行)
	for i in range( 1,  row) :
		form[ i, 0] = False
		
	#把表格完成
	#if你目標的數字 比現在正檢查的新數字來的小 就去看你左邊  因為你的結果跟少你一格人的子集一樣
	#elif (你要的>=正檢查的數字) 結果會是你左邊的(當然如果你的子集可以妳一定可以)  或是看  把目標減掉你會剩多少 的那個字集去找
	for i in range( 1, row) :
		for j in range( 1, column) :
			#print(i, end='')
			#print(j, end='')
			if i < int(worklist[j-1]) :
				form[ i, j] = form[ i, j-1]
				#print("worklist[j-1]", end = ' ')
				#print(int(worklist[j-1]))
				#print("j", end = ' ')
				#print(j)
				#print("Yes")
			else :
				form[ i, j] = form[ i, j-1] or form[ i-int(worklist[j-1]), j-1]
				#print(form[ i-int(worklist[j-1]), j-1])
				#print("NO")
				
			#print (form[i,j])
	
	"""for i in range( 0, row):
		for j in range( 0, column):
			print( '%-3s'%form[i][j], end="  ")

			
		
		print("*************")"""
	
	#找答案的子集合
	i = inputnum
	j = len(worklist)
	#print(i)
	#print(j)
	#one = False
	if form[ i, j] :
		ans = []
		#print( "{ ", end = '')
		while j >= 0 :
			#print("HERE")
			#print (form[i,j])
			#print(form[ i-1, j])
			#如果你這裡TRUE 而且你左邊是FALSE 就代表你一定要
			if form[ i, j] and not form[ i, j-1]:
				#print("inside")
				#if one :
					#print( ', ', end = '' )
				#print( worklist[j-1], end = '' )
				#one = True
				ans.append(int(worklist[j-1]))
				i -= int( worklist[j-1] )
			if i == 0 :
				break
			j -= 1
		
		ans.sort()
		#print(type(ans))
		print( '{', end = ' ' )

		print (','.join('%s' %id for id in ans ), end = '')
		##print(ans[1:len(ans)-1], end = ' ')
		print( '}' )
		#print( "}")
	else :
		print( "No Solution" )
	
	#印出表
	"""for i in range( 0, row):
		for j in range( 0, column):
			print( '%-3s'%form[i][j], end="  ")

			
		
		print(" ")"""
		
	
	
	


