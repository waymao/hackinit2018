from PIL import Image
from keras.models import load_model
from keras import backend as K
import sys
import numpy as np
from numpy import array

def getIndex(Filepath):
    K.clear_session()

    model = load_model(sys.path[0] + '/model111.h5')
    # keras.models.load_weights('my_model_weights.h5')

    img = Image.open(Filepath)
    img0 = array(img.resize((64,64)))
    img0.flatten()
    p = model.predict(img0.reshape(1,64,64,3))

    index = np.where(p==np.max(p))

    return int(index[1][0])