from flask import Flask, request, jsonify
from flask_cors import CORS

import cv2
import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F
app = Flask(__name__)
CORS(app)


class CNN(nn.Module):
    def __init__(self):
        super(CNN,self).__init__()
        self.C1=nn.Conv2d(1,24,3)
        self.bn1=nn.BatchNorm2d(24)
        self.C2=nn.Conv2d(24,36,3)
        self.bn2=nn.BatchNorm2d(36)
        self.fc1=nn.Linear(36*5*5,128)
        self.fc2=nn.Linear(128,64)
        self.fc3=nn.Linear(64,36)

    def forward(self,x):
        x=F.max_pool2d(F.relu(self.C1(x)),(2,2))
        x=self.bn1(x)
        x=F.max_pool2d(F.relu(self.C2(x)),(2,2))
        x=self.bn2(x)
        x=torch.flatten(x,1)
        x=F.relu(self.fc1(x))
        x=F.relu(self.fc2(x))
        x=self.fc3(x)
        return x
model=CNN()
model.load_state_dict(torch.load("CNNmodel.pth"))
classes=(0,1,2,3,4,5,6,7,8,9,'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z')



@app.route('/predict', methods=['POST'])
def predict():
    file = request.files['image']
    image = cv2.imdecode(np.frombuffer(file.read(), np.uint8), cv2.IMREAD_GRAYSCALE)
    image=cv2.resize(image, (28,28), 
               interpolation = cv2.INTER_LINEAR)
    image=torch.tensor(image,dtype=torch.float32)
    image=image.unsqueeze(0)
    image=image.unsqueeze(0)
    print(image.shape)
    # Use your ML model for prediction
    prediction = model(image)
    print(prediction)
    pred=torch.argmax(prediction)
    label=classes[pred]
    print("predicted label:",label)
    return jsonify({'label':label})


if __name__ == '__main__':
    app.run(debug=True)