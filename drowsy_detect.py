import torch
from matplotlib import pyplot as plt
import numpy as np
import cv2
import os

model = torch.hub.load('ultralytics/yolov5', 'custom', path='best.pt', force_reload=True)

img = os.path.join('awake.jpg')

results = model(img)
results.print()

# plt.imshow(np.squeeze(results.render()))
# plt.show()
