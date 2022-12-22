import os
traineerDirectory = 'traineer';

u=os.listdir(traineerDirectory)
print('\n'.join([str(u.index(x))+'\t: '+x for x in u]));
trainFolder=u[int(input("Train Folder: "))]
print(f"Congiure training options for {trainFolder}...")
trainFolder = traineerDirectory+'/'+trainFolder+'/'
data = trainFolder+'data.yaml'
hyp = trainFolder+'hyp.yaml'

weights = "yolov5s.pt"
if('weights.pt' in os.listdir(trainFolder)):
    weights = trainFolder+'weights.pt'

epochs = '3'
u = input(f"epochs({epochs})?")
epochs = epochs if u=='' else (epochs if int(u)<1 else u)

img = '640'
u = input(f"img({img})?")
img = img if u=='' else u

batch = '16'
u = input(f"batch({batch})?")
batch = batch if u=='' else u
os.system(f"python3 train.py --img {img} --batch {batch} --epochs {epochs} --data {data} --weights {weights} --hyp {hyp} --cache")
os.system(f"cp runs/train/{os.listdir('runs/train')[-1]}/weights/best.pt {trainFolder}/weights.pt")