import cv2
import numpy as np
import tensorflow as tf

camera = cv2.VideoCapture(0)

keras = tf.keras.models.load_model("C:\\Users\\cliente\\Downloads\\converted_keras (1)\\keras_model.h5")

while True:
    bol, frame = camera.read()

    cv2.imshow("camera",frame)

    tamanho = cv2.resize(frame,(224,224))
    transformar = np.array(tamanho, dtype=np.float32)
    transformar = np.expand_dims(transformar,axis=0)
    normalização = transformar/255

    previsão = (keras.predict(normalização))
    
    var0 = int(previsão[0][0] * 100)
    var1 = int(previsão[0][1] * 100)
    var2 = int(previsão[0][2] * 100)

    print("pedra:", var0)
    print("papel:",var1)
    print("tesoura:",var2)

    if cv2.waitKey(30) == 32:
        break

camera.release()
cv2.destroyAllWindows()