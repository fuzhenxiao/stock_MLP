import xlrd
import progressbar
import joblib
class Whatever():
	def __init__(self,file="",stocknum=0):
		self.conds=[]
		self.results=[]
		self.file=file
		self.stocknum=stocknum
	def getconds(self): #stock num start with 0

# stock num = 0  start with 2 in excel
# stock num = 1  start with 10 in excel
# stock num =2   start with 18 in excel
# sheet.cell_value(m,n)    row m-1   volumn n-1
		workbook = xlrd.open_workbook(self.file)
		sheet=workbook.sheets()[0]

		stockindex=self.stocknum*8+2
		for i in range(4,3100):
			single_example=[]
			for j in range(0,30):
				for k in range(0,8):
					a=sheet.cell_value(i+j-1,stockindex+k-1)
					single_example.append(a)
			self.conds.append(single_example)
	def getresults(self):
		stockindex=self.stocknum*8+2
		workbook = xlrd.open_workbook(self.file)
		sheet=workbook.sheets()[0]
		for i in range(4,3100):

			former=sheet.cell_value(i-1+29,stockindex-1+4)
			later=sheet.cell_value(i-1+5+29,stockindex-1+4)
			if former != 0.:
				result=(later-former)/former
			else: 
				result=1121
			
				
			trueresult=0
			if result==1121:
				trueresult=12 #12:means special
			
			elif result < -0.1 :
				trueresult=0
			elif result <-0.08:
				trueresult=1
			elif result <-0.06:
				trueresult=2
			elif result <-0.04:
				trueresult=3
			elif result <-0.02:
				trueresult=4
			elif result <0.:
				trueresult=5
			elif result <0.02:
				trueresult=6
			elif result <0.04:
				trueresult=7
			elif result <0.06:
				trueresult=8
			elif result <0.08:
				trueresult=9
			elif result <0.1:
				trueresult=10
			else:
				trueresult=11

			'''if i == 4:
				print("this is a test")
				print(former)
				print(later)
				print(result,trueresult)'''

			self.results.append(trueresult)

print("loading raw material...")

for j in range(1,6):
	
	#allconds=[]
	allresults=[]
	filename="SH"+str(j)+".xlsx"
	#tosavefilename1="allconds"+str(j)+".conds"
	tosavefilename2="allresults"+str(j)+".results"
	print("reading ",j,"th file which is "+filename)
	#print("will generate two files: ",tosavefilename1," ",tosavefilename2)
	for i in progressbar.progressbar(range(0,49)):
		a1=Whatever(filename,i)
		#a1.getconds()
		a1.getresults()
		#allconds=allconds+a1.conds
		allresults=allresults+a1.results
	#joblib.dump(allconds,tosavefilename1)
	joblib.dump(allresults,tosavefilename2)

'''
for i in progressbar.progressbar(range(1,6)):
	toloadfilename1="allconds"+str(j)+".conds"
	allconds=joblib.load(toloadfilename1)
	allresults=[]
	for j in progressbar.progressbar(range(0,len(allconds))):

	
	tosavefilename2="allresults"+str(j)+".results"
'''

print("reading finished, file saved")
input("press any key to quit")
