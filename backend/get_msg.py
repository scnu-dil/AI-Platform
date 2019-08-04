import os,sys,random,string
from flask import Flask,request
from flask import jsonify
from flask_cors import CORS
import dlib
import numpy as np
import cv2
import json
import time

basedir = os.path.abspath(os.path.dirname(__file__))

detector = dlib.cnn_face_detection_model_v1('mmod_human_face_detector.dat')
sp=dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')
facerec=dlib.face_recognition_model_v1('dlib_face_recognition_resnet_model_v1.dat')
threshold=0.54
def GetFace():
    imagePath='static/img/'
    data=np.zeros((1,128))
    label=[]
    for file in os.listdir(imagePath):
        if '.jpg' in file or '.png' in file:
            fileName=file
            labelName=file.split('_')[0]
            print('current image:',file)
            print('current label:',labelName)
		
            img=cv2.imread(imagePath+file)
            if img.shape[0]*img.shape[1]>50000:
                img=cv2.resize(img,(0,0),fx=0.5,fy=0.5)
            dets=detector(img,1)
            for k,d in enumerate(dets):
                rec=dlib.rectangle(d.rect.left(),
					d.rect.top(),
					d.rect.right(),
					d.rect.bottom())
                shape=sp(img,rec)
                face_descriptor=facerec.compute_face_descriptor(img,shape)
                faceArray=np.array(face_descriptor).reshape((1,128))
                data=np.concatenate((data,faceArray))
                label.append(labelName)
                cv2.rectangle(img,(rec.left(),rec.top()),
					(rec.right(),rec.bottom()),
					(0,255,0),2)
    data = data[1:, :]                                                                                  
    np.savetxt('faceData.txt', data, fmt='%f')                                                         

    labelFile=open('label.txt','w')                                      
    json.dump(label, labelFile)                                                                         
    labelFile.close()

    cv2.destroyAllWindows()   

def del_file():
    path=basedir+"/static/img/"
    for i in os.listdir(path):
        path_file=os.path.join(path,i)
        if os.path.isfile(path_file):
            os.remove(path_file)
        else:
            del_file(path_file)

def recognition(img,label,data):
    dets = detector(img, 1)
    for k, d in enumerate(dets):
        print("Detection {}: Left: {} Top: {} Right: {} Bottom: {}".format(
            k, d.rect.left(), d.rect.top(), d.rect.right(), d.rect.bottom()))
        rec = dlib.rectangle(d.rect.left(),d.rect.top(),d.rect.right(),d.rect.bottom())
        print(rec.left(),rec.top(),rec.right(),rec.bottom())
        shape = sp(img, rec)
        face_descriptor = facerec.compute_face_descriptor(img, shape)        
        
        class_pre = findNearestClassForImage(face_descriptor, label,data)
        print(class_pre)
        cv2.rectangle(img, (rec.left(), rec.top()+10), (rec.right(), rec.bottom()), (0, 255, 0), 2)
        cv2.putText(img, class_pre , (rec.left(),rec.top()), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,255,0), 2, cv2.LINE_AA)

def findNearestClassForImage(face_descriptor, faceLabel,data):
    temp =  face_descriptor - data
    e = np.linalg.norm(temp,axis=1,keepdims=True)
    min_distance = e.min() 
    print('distance: ', min_distance)
    if min_distance > threshold:
        return 'other'
    index = np.argmin(e)
    return faceLabel[index]

def CheckFace():
    labelFile=open('label.txt','r')
    label = json.load(labelFile)                                                  
    labelFile.close()

    data = np.loadtxt('faceData.txt',dtype=float)     
    path = basedir+"/static/re/"   
    url = path+'re.jpg'                         
    img = cv2.imread(url,1)
    recognition(img,label,data)
    cv2.imwrite(url,img)
    cv2.destroyAllWindows()
    url='http://127.0.0.1:5000/static/re/re.jpg'
    return url

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/')
def hello_world():
    return 'Hello World'


@app.route('/getMsg', methods=['GET', 'POST'])
def home():
  
    img = request.files.get('upload')
    print(img)

    path = basedir+"/static/img/"
  
    imgName = img.filename
  
    file_path = path+imgName

    img.save(file_path)

    url = '/static/img/'+imgName

    return url

@app.route('/getPic', methods=['GET', 'POST'])
def getPic():
  
    img = request.files.get('upload1')
    
    path = basedir+"/static/re/"
  
    imgName = 're.'+img.filename.split('.')[1]
   
    file_path = path+imgName
     
    img.save(file_path)

    img1=cv2.imread(file_path,1)

    img1 = cv2.resize(img1,(0,0),fx=0.5,fy=0.5)

    cv2.imwrite(file_path,img1)

    return file_path


@app.route('/checkFace', methods=['GET', 'POST'])
def face():
    GetFace()
    del_file()
    url=CheckFace()
    times=time.time()
    response = {
        'msg': url,
        'times':int(times)
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run()

