#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import keras
from keras.models import load_model
import numpy as np
import json
import sys
import cv2

img_path = sys.argv[1]

model_path = "hidden/weights_mixed_best.hdf5"

model = load_model(model_path)
print('here')
