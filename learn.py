import xlrd
import joblib
import progressbar
import traceback
def standlize(x):
	for m in range(0,len(x)):
		for n in range(0,30):
			a=x[m][n*8+5]
			b=x[m][n*8+6]
			x[m][n*8+5]=a/2000000
			x[m][n*8+6]=b/20000000
	return x
def symplize(y):
	for m in range(0,len(y)):
		if y[m] ==12:
			y[m]=0
		elif y[m] <=5:
			y[m]=1
		else:
			y[m]=2
	return y

# Good, so far so good, now you have rawmaterials for deep-learning 
#alphas=[1e-2,1e-3,1e-4,1e-5,1e-6,1e-7,1e-8]
#learning_rate_inits=[1e-3,1e-4,1e-5,1e-6,1e-7,1e-8,1e-9,1e-10]
#scores_wow=[]
try:
	print("initializing sklearn...")
	print("reading previous data...") 
	condss=[]
	resultss=[]
	for i in range(1,6):
		allcondsfile="allconds"+str(i)+".conds"
		allresultsfile="allresults"+str(i)+".results"
		allconds=joblib.load('allconds1.conds')
		allresults=joblib.load('allresults1.results')
		allconds=standlize(allconds)
		allresults=symplize(allresults)
		condss.append(allconds)
		resultss.append(allresults)
		print("set loaded ")
	from sklearn.neural_network import MLPClassifier
	#for alpha_selected in alphas:
		#for learning_rate_init_selected in learning_rate_inits:
	clf=MLPClassifier(solver='adam',alpha=1e-3,hidden_layer_sizes=(75, ), random_state=None,learning_rate_init=1e-5,beta_1=0.9,beta_2=0.999,warm_start=True)
	#joblib.dump(clf,"clf0.pkl")
	#clf=joblib.load("clf1.pkl")
	print("training...")

	#print(allconds[0])
	#print(allconds[34])
	#print(allresults[0])
		#if testresults[m] ==12:
		#	testresults[m]=0
		#elif testresults[m] <=5:
		#	testresults[m]=1
		#else:
		#	testresults[m]=2
	#print("examples picked out:")
	#print(allconds[0])
	#print(allconds[34])
	#print(allresults[0])

	#lenth1=len(allconds)
	#lenth2=len(allresults)
	#print('lenth1:',lenth1)
	#print('lenth2:',lenth2)

	#toload="clf"+str(i-1)+".pkl"
	#tosave="clf"+str(i)+".pkl"
	#print("loading previous model which is "+toload)
	#clf=joblib.load(toload)
	#print(toload+" loaded")
	
	#condslice=allconds[j*500:j*500+500]
	#resultslice=allresults[j*500:j*500+500]
	try:
		clf.fit(condss[0],resultss[0])
		joblib.dump(clf,"clfsuper.pkl")
	except Exception:
		#print("set ",j," abandoned")
		traceback.print_exc()
	#print("saving as "+tosave)
	#joblib.dump(clf,tosave)
	for i in range(1,5):
		score=clf.score(condss[i],resultss[i])
		print(score)
	#scores_wow.append([score,alpha_selected,learning_rate_init_selected])

	#print("test finished")
	#for i in scores_wow:
	#	text="score: "+str(i[0])+"learning_rate_init: "+str(i[1])+"alpha: "+str(i[2])
	#	print(text)

	#print("saving...")
	#print("saved")


	input("press any key to kill this process")
except Exception:
	traceback.print_exc()
	input("ERR")


#if wanna load:  clf2=joblib.load("filename.pkl")
#if wanna predict    clf2.predict( cond )

	




