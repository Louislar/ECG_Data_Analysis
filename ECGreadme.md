# ECG程式使用說明

## 環境需求

1. python編譯器需要安裝matlab engine的套件，安裝說明網址如下: 
    https://www.mathworks.com/help/matlab/matlab_external/install-the-matlab-engine-for-python.html
    
2. python 3.6

3. keras



## 檔案介紹

|檔案名稱|作用|
|:-----------------------------|:--------------:|
|<span class="text-nowrap"> **callRaw_ECG.m**</span>|<span class="text-nowrap"> **此檔案為matlab的function函數，不僅會輸出RRI，並且會將RRI間期序列儲存到pythonReceiver_rri.txt當中**</span>|
|<span class="text-nowrap"> **DS_detect.m**</span>|<span class="text-nowrap"> **此檔案為matlab的function函數，並且會由callRaw_ECG.m呼叫，所以計算RRI需呼叫callRaw_ECG.m**</span>|
|<span class="text-nowrap"> **HRV.py**</span>|<span class="text-nowrap"> **此檔案為python程式碼，使用時請import HRV.py，再呼叫HRV.features_for_dnn_function()，輸入與輸出如前述**</span>|
|<span class="text-nowrap"> **DNN_ECG_predict.py**</span>|<span class="text-nowrap"> **此檔案為python程式碼，目的是使用預先train好的model，預測輸入的ECG的受測者的壓力感受情況**</span>|
|<span class="text-nowrap"> **DNN_Model.m**</span>|<span class="text-nowrap"> **此檔案為keras的model檔案，使用時請用keras的load_model函數，並且輸入為1*8的numpy array，其中8個數值為HRV的features**</span>|
|<span class="text-nowrap"> **adc03.csv**</span>|<span class="text-nowrap"> **此檔案為預設輸入之csv檔案，內容為raw ECG data，若要預測其他新測量的資料，就要將該資料整理成與adc03.csv相同的格式，才能正常輸入**</span>|

## 各檔案的輸出與輸入
|檔案名稱|輸入|輸出|
|:-----------------------------|:--------------:|:--------------:|
|<span class="text-nowrap"> **callRaw_ECG.m**</span>|<span class="text-nowrap"> **檔案位置**</span>|<span class="text-nowrap"> **RRI**</span>|
|<span class="text-nowrap"> **DS_detect.m**</span>|<span class="text-nowrap"> **raw ECG data**</span>|<span class="text-nowrap"> **RRI**</span>|
|<span class="text-nowrap"> **HRV.py**</span>|<span class="text-nowrap"> **檔案位置**</span>|<span class="text-nowrap"> **HRV的features**</span>|
|<span class="text-nowrap"> **DNN_ECG_predict.py**</span>|<span class="text-nowrap"> **無**</span>|<span class="text-nowrap"> **預測結果**</span>|
|<span class="text-nowrap"> **DNN_Model.m**</span>|<span class="text-nowrap"> **無**</span>|<span class="text-nowrap"> **無**</span>|
|<span class="text-nowrap"> **adc03.csv**</span>|<span class="text-nowrap"> **無**</span>|<span class="text-nowrap"> **無**</span>|

## 程式使用方式

1. 到DNN_ECG_predict.py的39行程式碼修改輸入檔案路徑(預設輸入檔案為同資料夾下的adc3.csv)，於下圖紅框處修改檔案路徑

![pic01](https://raw.githubusercontent.com/Louislar/ECG_Data_Analysis/master/ECG_readme_pic001.png "modify pic")

2. 使用command line執行DNN_ECG_predict.py，如下圖紅框處的指令

![pic02](https://raw.githubusercontent.com/Louislar/ECG_Data_Analysis/master/ECG_readme_pic002.png)

3. 最後得到預測結果，[1, 0]為不緊張，[0, 1]為緊張，如下圖的紅箭頭指向處的預測結果即為不緊張

![pic03](https://raw.githubusercontent.com/Louislar/ECG_Data_Analysis/master/ECG_readme_pic003.png)
