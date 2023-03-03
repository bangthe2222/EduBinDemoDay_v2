import tensorflow as tf
import cv2
import numpy as np
import time
interpreter = tf.lite.Interpreter(model_path="vending_5class_ResNet50V2_30epoch_avg_float32.tflite")
interpreter.allocate_tensors()
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

print("input details", input_details)
print("ouput details", output_details)


# im = im/255
input_shape = input_details[0]['shape']

cap = cv2.VideoCapture(0)
while True:
    t1 = time.time()
    _, im = cap.read()
    im = cv2.resize(im, (224,224))
    im = np.asarray([im],dtype=np.float32)
    
    interpreter.set_tensor(input_details[0]['index'], im)
    
    interpreter.invoke()
    print(time.time() - t1)
    # The function `get_tensor()` returns a copy of the tensor data.
    # Use `tensor()` in order to get a pointer to the tensor.
    output_data = interpreter.get_tensor(output_details[0]['index'])
    print(output_data)