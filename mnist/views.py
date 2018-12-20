from django.shortcuts import render, redirect
from PIL import Image
import numpy as np
import base64
import tensorflow as tf
import os

#学習モデルのロード
from keras.models import load_model
model = load_model('C:\\<path>\\mnist.h5')
graph = tf.get_default_graph()


def upload(request):  
    
    #画像データの取得
    files = request.FILES.getlist("files[]")

    #簡易エラーチェック（jpg拡張子）
    for memory_file in files:

        root, ext = os.path.splitext(memory_file.name)
     
        if ext != '.jpg':
            
            message ="【ERROR】jpg以外の拡張子ファイルが指定されています。"
            return render(request, 'mnist/index.html', {
                "message": message,
                })


    if request.method =='POST' and files:
        result=[]
        labels=[]
        for file in files:
            img = Image.open(file)
            gray_img = img.convert('L')
            img = gray_img.resize((28, 28))
            img = np.array(img).reshape(1,28,28,1)
            labels.append(mnist(img))
        
        for file, label in zip(files, labels):
            file.seek(0)
            file_name = file
            src = base64.b64encode(file.read())
            src = str(src)[2:-1]
            result.append((src, label))

        context = {
            'result': result
           }
        return render(request, 'mnist/result.html', context)
    
    else:
        return redirect('index')


def mnist(input):
    
    global graph
    with graph.as_default():
        result = (model.predict(input, batch_size=None, verbose=0, steps=None)).argmax()

    return result
    