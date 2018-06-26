import xlwt
import progressbar
import joblib
import traceback
def run(ModelName,CondsName,ResultName):
    print("Loading...")
    Result=joblib.load(ResultName)
    Model=joblib.load(ModelName)
    Conds=joblib.load(CondsName)
    for m in range(0,len(Conds)):
        for n in range(0,30):
            a=Conds[m][n*8+5]
            b=Conds[m][n*8+6]
            Conds[m][n*8+5]=a/2000000
            Conds[m][n*8+6]=b/20000000
    PredictResult=[]
    print("Loaded, now start to predict")

    for i in progressbar.progressbar(range(0,len(Conds))):
        PredictResult.append(Model.predict([Conds[i]]))

    print("Example Picked Out:")
    print(PredictResult[1],type(PredictResult[1]),PredictResult[1][0],type(PredictResult[1][0]))
    print("Prediction complete. Start to generate Excel file")

    
    wb=xlwt.Workbook()
    ws1=wb.add_sheet("1")
    ws2=wb.add_sheet("2")
    ws3=wb.add_sheet("3")
    for i in progressbar.progressbar(range(0,len(Conds))):
        if i <60000:
            ws1.write(i,0,Result[i])
            ws1.write(i,1,int(PredictResult[i][0]))
        elif i <120000:
            ws2.write(i-60000,0,Result[i])
            ws2.write(i-60000,1,int(PredictResult[i][0]))
        else:
            ws3.write(i-120000,0,Result[i])
            ws3.write(i-120000,1,int(PredictResult[i][0]))
    wb.save("Prediction.xls")


try:
    run("clf1.pkl","allconds2.conds","allresults2.results")
    print("OVER")
    input()
except Exception as e:
    print(e)
    input()








