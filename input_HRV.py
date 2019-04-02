import numpy as np
import pandas as pd  

"""
從CSV讀出HRV資料，並且分為label與原始資料
輸入: .csv的data檔案
輸出: 整理好的data(np.array的形式)，以及對應各個data的label
"""
def reda_in_hrv_data(dataFile):
    #inputData=[]

    #從csv內讀入資料(HRV資料)，並且儲存為panda格式，格式為原始csv的格式(與csv儲存格式一模一樣)
    filePathStr=dataFile
    inputData=pd.read_csv(filePathStr)
    #print(inputData)
    #print(inputData[['datasetId', 'MEAN_RR']])  #只輸出這兩欄資料
    #print(len(inputData))   #41033

    #將需要的feature欄位另外儲存起來，每一個sample儲存為一個列，方便整理
    #(X, Y): X為列數，也是資料的個數；Y為feature個數，也就是每一個資料包含的特徵數量
    inputList=[]
    inputList=(inputData[['MEAN_RR', 'RMSSD', 'pNN50', 'VLF', 'LF', 'HF', 'LF_HF', 'LF_NU']])
    #print(len(inputList))       #41033
    #print(type(inputList))      #<class 'pandas.core.frame.DataFrame'>
    #print(inputList)

    inputArray=[]
    inputArray=np.array(inputList)
    #print(inputArray.shape)     #(41033, 8), 8為取的欄位數量
    #print(inputArray)

    
    #接下來要取得各個資料的label
    inputLabelList=inputData[['condition']]
    inputLabelArray=np.array(inputLabelList)
    #print(inputLabelArray.shape)        #(41033, 1) 後面的數字應該要是一，因為label只會有一個欄位表示label幾
    
    #condition出來的為'no stress', 'time pressure', 'interruption'
    #目前先將no stress歸類成1, 其他兩個歸類成1(假設都是有壓力的情況底下)
    #降維度從2維降到1維
    inputLabelArray = inputLabelArray.reshape(inputLabelArray.shape[0])
    #print(inputLabelArray)
    #print(inputLabelArray.shape)   #(41033, )
    for x in range(0, len(inputLabelArray)):
        if inputLabelArray[x] == 'no stress':
            inputLabelArray[x]=0
        else:
            inputLabelArray[x]=1

    #print(inputLabelArray)
    #print(inputLabelArray.shape)
    inputLabelArray = np.array(inputLabelArray, dtype=int)
    return inputArray, inputLabelArray

#for test
#reda_in_hrv_data('test.csv')