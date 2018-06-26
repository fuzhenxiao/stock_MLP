
import joblib
a=joblib.load("allresults1.results")
total1=0
total2=0
for i in a:
	if i == 12:
		total1+=0
	elif i<=5:
		total1+=(-0.02)*(5-i)-0.01
	else:
		total2+=(0.02)*(i-5)+0.01

average1=total1/len(a)
average2=total2/len(a)
print(average1)
print(average2)
input("finish")


	




