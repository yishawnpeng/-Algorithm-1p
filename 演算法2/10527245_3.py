#10527245
#10527142 10527239 10527245
#彭義翔 林威廷 陳宏溢

import copy

class Process :
	def __init__(self, ID, NUM):	#每個人自己的資料
		self.id = str(ID)
		self.num = int(NUM)
		#self.left = LEFT		#use ID
		#self.right = RIGHT		#use ID
		self.hc = ""
		self.hulfman = ""
		
	def appendHC(self, str) :			#霍夫曼密碼 str 建樹的時候就給
		if str == "0" :
			self.hc = "0 " + self.hc
		elif str == "1" :
			self.hc = "1 " + self.hc
			
	def goodnum(self) :
		for i in range(len(self.hc)) :	#霍夫曼密碼 轉int
			if self.hc[i] == "0" :
				self.hulfman = self.hulfman + "0"
			elif self.hc[i] == "1" :
				self.hulfman = self.hulfman + "1"
			else :
				pass
				
		return self.hulfman

def sortNUM(worklist) :		#回傳用數字大小排序的list
	n = len(worklist)
	#ans = worklist.copy()
	for i in range(0, n-1) :
		for j in range(0, n-i-1) :
			if worklist[j].num > worklist[j+1].num :
				worklist[j], worklist[j+1] = worklist[j+1], worklist[j]
				#print(worklist[j].num)
				#print(worklist[j+1].num)
		
	return worklist
	
def sortID(worklist) :		#回傳用ID大小排序的list
	n = len(worklist)
	#ans = worklist.copy()
	for i in range(0, n-1) :
		for j in range(0, n-i-1) :
			if worklist[j].id > worklist[j+1].id :
				worklist[j], worklist[j+1] = worklist[j+1], worklist[j]
		
	return worklist
	
def sortlong(worklist) :		#回傳用霍夫曼編碼長度排序的list 長到短
	n = len(worklist)
	#ans = worklist.copy()
	for i in range(0, n-1) :
		for j in range(0, n-i-1) :
			if len(worklist[j].hc) < len(worklist[j+1].hc) :
				worklist[j], worklist[j+1] = worklist[j+1], worklist[j]
		
	return worklist
	
def findid(worklist, ID) :		#找到在LIST裡面ID的位置
	n = 0
	for i in range(len(worklist)) :
		if worklist[i].id == ID :
			n = i
			
	return n
		
def buildtree(worklist, cleanlisrt) :	#建樹
	tt = worklist[0].id.split()			#把第一個人抓出來看他的ID長度
	findallid = len(tt)
	for i in range(findallid) :			#找到他在原本資料的list裡面位置
		n = findid(cleanlisrt, tt[i])
		cleanlisrt[n].appendHC("0")		#第一個給0
	tt = worklist[1].id.split()			#把第一個人抓出來看他的ID長度
	findallid = len(tt)		
	for i in range(findallid) :			#..
		n = findid(cleanlisrt, tt[i])
		cleanlisrt[n].appendHC("1")		#第二個給1
		
	worklist.append(Process(str(worklist[0].id)+" "+str(worklist[1].id), worklist[0].num+worklist[1].num))
	#把剛剛抓出來的第一二個人合併放進去LIST裡面
	worklist = sortNUM(worklist)	#再排一次
	worklist.pop(0)					#前兩個POP掉
	worklist.pop(0)
	#for i in  range (len(worklist)) :
		#print(worklist[i].num,end= "")
	#print("**",end = "")
	#print(len(worklist))
	
def decode(cleanlisrt, goal, ans) :		#給list還有目標數字(str) 找到第一個符合
	#print("**")
	#print(goal)
	#print("**")
	count = 0
	for i in range(len(cleanlisrt)) :
		cc = len(cleanlisrt[i].hulfman)
		temp = goal[0:cc]				#拿來檢查的小字串
		#print(temp)
		#print(cc)
		#print("")
		#print(cleanlisrt[0].id)
		#print(cleanlisrt[0].hulfman)
		if temp == cleanlisrt[i].hulfman :
			#print("yes")
			#print(temp)
			#print(cleanlisrt[i].hulfman)
			count = i
			goal = goal[cc:]
			break
	

	ans = str(ans) + str(cleanlisrt[count].id)
	#print(ans)
	#print(goal)
	
	return goal, ans
		
if __name__=='__main__' :
	filename = input("輸入input字元個數(單獨一個0結束):" )
	cc = 1
	while filename != '0' :
		worklist = []	#要加密的字母
		goalnum = 0		#要解密的字串
		inputcount = int(filename) 
		for i in range(inputcount) :
			print("還有", inputcount-i, "個尚未輸入")
			tempP = input("輸入字母和出現頻率 :")
			tempT = tempP.split()
			worklist.append(Process(tempT[0], tempT[1]))
			
		goalnum = input("輸入要解碼的數字 :")
		cleanlisrt = copy.copy(worklist)
		cleanlisrt = sortID(cleanlisrt)		#看數據用 其實可以不用排
		"""for i in range(inputcount) : 測試數據
			print(worklist[i].id)
			print(worklist[i].num)
		print(goalnum)"""
		
		while len(worklist) > 1 :			#把tree建好 順便算好霍夫曼編碼
			worklist = sortNUM(worklist)
			buildtree(worklist, cleanlisrt)
			
		print("Huffman Codes #", end = "")	#印出霍夫曼編碼
		print(cc)
		for i in  range (len(cleanlisrt)) :
			print(cleanlisrt[i].id, end = " ")
			print(cleanlisrt[i].hc)
		#print(type(worklist))
		#print(type(worklist[0]))
		#findid(cleanlisrt, cleanlisrt[0].id)
		cleanlisrt = sortlong(cleanlisrt)	#先把每個人的霍夫曼編碼轉INT
		for i in range(len(cleanlisrt)) :
			cleanlisrt[i].goodnum()
			
		#print(cleanlisrt[0].id)
		#print(cleanlisrt[1].id)
		goal = str(goalnum)
		ans = ""
		#aa = 7 底下and aa > 0 
		while len(goal) > 0 : 	#道還沒解完前都一直呼叫 他會回傳第一個找到的符合編碼
			goal, ans = decode(cleanlisrt, goal, ans)
			#aa -=1
		
		print("Decode = ", end = "")
		print(ans)		
		
		cc += 1
		filename = input("\n輸入input字元個數(單獨一個0結束):" )