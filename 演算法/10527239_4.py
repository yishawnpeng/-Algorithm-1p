#10527239
#10527142 10527239 10527245
#彭義翔 林威廷 陳宏溢

import copy

class Edgeall :
	def __init__(self, star, end, num) :	#邊的資料 起點終點權重
		self.starID = star
		self.endID = end 
		self.weight = num
		
class Vertex :
	def __init__(self, K) :					#頂點資料 名子距離父節點
		self.key = K
		self.d = 10000
		self.pi = None

def findkeylist(worklist, key) :	#找出KEY在worklist的位置 如果沒找到回傳-1
	n = -1
	for i in range(len(worklist)) :
		if worklist[i].starID == key :
			n = i 
			
	return n
	
def cleanlist(worklist) :					#把多餘的邊找出(要新增頂點 重複的名稱不用)
	whichismore = []
	#for i in range(len(worklist)) :
		#print(worklist[i].key)
	ans = copy.copy(worklist)
	for i in range(0, len(ans)) :
		for j in range(i+1, len(ans)) :
			if ans[i].key == ans[j].key :
				whichismore.append(j)
				#print(i)
				#print(ans[j].key)
	#print(whichismore)
	while len(whichismore) > 0 :
		n = int(whichismore.pop())
		#print(n)
		ans.pop(n)
				
	return ans
	
def findmininlist(queue) :				#從min priority queue找出最小的(要release)
	n = 10000	#距離
	x = -1		#在Q的位置
	for i in range(0, len(queue), 2) :
		if int(queue[i]) < int(n) :
			n = queue[i] 
			x = i
		
	return n, x
	
def releasea(vertexlist, worklist, goalpoint) : 	#找出一條邊對他做到點距離的更新
	#donum = -1
	dlist = []
	mpq = []			#最小優先佇列 先放距離再放名稱
	for i in range(len(worklist)) :				#先把起點的邊都做完
		if goalpoint == worklist[i].starID :
			#donum = i 
			dlist.append(i)
			for j in range(len(vertexlist)) :
				if vertexlist[j].key == goalpoint :
					vertexlist[j].d = 0
					break
	
	#if donum != -1 :							#起點還沒做完
	while len(dlist) > 0 :
		x = dlist.pop(-1)
		for i in range(len(vertexlist)) :
			if vertexlist[i].key == worklist[x].endID :
				#print("**")
				vertexlist[i].pi = worklist[x].starID
				vertexlist[i].d = worklist[x].weight
				mpq.append(vertexlist[i].d)
				mpq.append(vertexlist[i].key)
				worklist.pop(x)
				break
	#elif donum == -1 :							#起點做完了
	while len(mpq) > 0 :
		workn, workx = findmininlist(mpq)
		#print(mpq)
		workkey = mpq[workx+1]				#把是誰抓出來
		gg = -1 
		for i in range(len(vertexlist)) :		#gg 現在這個KEY在VERTEX(頂點)的位置
			if workkey == vertexlist[i].key :
				gg = i 
		mpq.pop(workx)						#MPQ前兩個(距離 ID) POP掉
		mpq.pop(workx)
		for i in range(len(worklist)) :		#從所有邊找到剛剛想要找MQP最小的起點去release
			if worklist[i].starID == str(workkey) :
				nowkey = worklist[i].endID  #找到的話 再去找他的終點
				for j in range(len(vertexlist)) :
					if vertexlist[j].key == nowkey : 	#再找到的話 去看距離有沒有比較近
						if int(worklist[i].weight) + int(vertexlist[gg].d) < int(vertexlist[j].d) :
							vertexlist[j].d = int(worklist[i].weight) + int(vertexlist[gg].d)
							#vertexlist[j].pi = vertexlist[gg].key
							if vertexlist[j].pi == None : #如果原本的點沒有被加過就加到MPQ 準備去排程計算
								#print("???")
								mpq.append(vertexlist[j].d)
								mpq.append(vertexlist[j].key)
							vertexlist[j].pi = vertexlist[gg].key	#父節點更新 要等前面的IF結束才能跑 不然IF都進不去 
							#worklist.pop(i)
							
							
							
	"""print(vertexlist[0].key)
	#print(vertexlist[0].d)
	print(vertexlist[1].key)
	#print(vertexlist[1].d)
	print(vertexlist[2].key)
	#print(vertexlist[2].d)
	print(vertexlist[3].key)
	#print(vertexlist[3].d)
	print(vertexlist[4].key)
	#print(vertexlist[4].d)"""
				
		
if __name__=='__main__' :
	filename = input("請輸入頂點個數的個數(單獨一個0結束)")
	while filename != "0" :
		worklist = []
		edgenum = input("請輸入邊個數的個數")
		goalpoint = input("請輸入要開始的頂點")
		for i in range(int(edgenum)) :					#把邊的資訊處理好
			print("還有" , int(edgenum)-i , "條邊還沒輸入")
			temp = input("請輸入每條邊")
			tempA = temp.split()
			worklist.append(Edgeall(tempA[0], tempA[1], tempA[2]))

		#for i in range(int(edgenum)) :
			#print(worklist[i].weight)
			
		isFind = -1
		vertexlist = []
		for i in range(0, len(worklist)) :				#把頂點的資訊處理好
			vertexlist.append(Vertex(worklist[i].starID)) 
				
		vertexlist = cleanlist(vertexlist)				#多餘定點的清理
				
		#for i in range(len(vertexlist)) :
			#print(vertexlist[i].key)
			
		#for i in range(int(filename)) :
		releasea(vertexlist, worklist, goalpoint)		#更新距離
		
		print("ANS")
		for i in range(len(vertexlist)) :				#印出
			if int(vertexlist[i].key) != int(goalpoint) :
				print(int(goalpoint), " to " , vertexlist[i].key, " =  ", end = "")
				print(vertexlist[i].d)
		
		filename = input("請輸入邊的個數(單獨一個0結束)")