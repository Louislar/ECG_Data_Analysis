import matlab.engine
import numpy as np
eng = matlab.engine.start_matlab()

matlabOutPut = eng.callRaw_ECG(nargout=1)
#eng.callRaw_ECG()
eng.quit()

print('matlab output')
npArray = np.array(matlabOutPut[0])
print(npArray.shape)