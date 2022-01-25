# 训练baseline模型
# python train.py --weights 'weights/yolov5s.pt' --epochs 25 --data data/boat.yaml --cfg models/yolov5s_boat.yaml --batch-size 16 --img-size 640
python train.py --weights 'weights/yolov5x6.pt' --epochs 10 --data data/boat.yaml --cfg models/yolov5x6_boat.yaml --batch-size 2 --img-size 1280
