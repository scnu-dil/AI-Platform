import os,sys,random,string
from flask import Flask, render_template, request
from flask import jsonify
from flask_cors import CORS
from snownlp import SnowNLP
from textsummary import TextSummary
from stanfordcorenlp.corenlp import StanfordCoreNLP
import dlib
import numpy as np
import cv2
import json
import time

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

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


def word_split(text):
  # 分词功能
  split_result = ""
  words = SnowNLP(text).words
  for w in words:
    split_result += str(w)+ "  "
  return split_result

def Part_of_Speech_tagging(text):
  # 词性分析和关键词提取
  word_tag = ""
  s = SnowNLP(text)
  for w in s.tags:
    word_tag += w[0] + "/" + w[1] + "  "
  key = s.keywords(3)
  return word_tag, key


@app.route('/api/nlp')
def home():

  nlp_parsing = StanfordCoreNLP('stanford-corenlp-full-2018-10-05',quiet = False,lang = 'zh')
  input_text = request.args.get('input')
  result = word_split(input_text)
  word_tagging, key_words = Part_of_Speech_tagging(input_text)
  result_paring = nlp_parsing.parse(input_text)
  response = {
    'split_result': result,
    'word_tag': word_tagging,
    'key_word': key_words,
    'Paring': result_paring
  }

  return jsonify(response)

@app.route('/api/summary')
def text_summa():
    """
    自动文摘
    :return:
    """
  title = request.args.get('sub_input')
  text = request.args.get('text_input')
  textsummary = TextSummary()
  textsummary.SetText(title, text)
  summary = textsummary.CalcSummary()
  summary_result = "\n".join(summary)
  response = {
    'result': summary_result
  }
  
  return jsonify(response)

@app.route('/api/chat')
def chat_robot():
  left = "hello"
  response = {
    'left_msg': left
  }

  return jsonify(response)

@app.route('/')
def hello_world():
    return 'Hello World'

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
  if request.method == 'POST':
    file = request.files.get('file')
    if file is None:
      response = {'status': 404}
    else:
      file.save(file.filename)
      response = {
        'status': 200
      }
    return jsonify(response)

@app.route('/download/<filename>', methods=['GET', 'POST'])
def download_file(filename):
  if request.method == 'GET':
    # fullfilename = request.args.get('filename')
    response = make_response(send_from_directory('./', "test2.csv", as_attachment=True))
    response.headers["Content-Disposition"] = "attachment; filename=test.csv"
    response.headers["Content_Type"] = "application/octet-stream"

    # return  send_from_directory('./', "test.png", as_attachment=True)
    return response

@app.route('/getMsg', methods=['GET', 'POST'])
def getMsg():
  
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

def Word_Cloud():
    """
    词云生成功能
    :return:
    """
    # if request.method == 'POST':
    if request.method == 'GET':
      con = request.args.get("content")
      # print(con)
      # 本地图片(最好是白底)路径
      imagePath = '.\\background.png'
      # 词云图保存路径
      imageSavePath = 'static/ptoto/word_cloud.png'
      img = en_wordcloud_Generater.Word_Cloud.en_wordcloud_text_gen(con, imagePath, imageSavePath, False)  # 返回的是图片类型，可直接保存的格式。但不能转化为url
      img.save(imageSavePath, optimize=True)  # 添加路劲参数后即可直接保存
      file_url = photos.url(imageSavePath)  # 将带传图片进行URL转化
      print("file_url:-----------------", file_url)
      response = {
        "img_url": file_url  # 将图片的url传输给前端
      }
      return jsonify(response)
      
      
if __name__ == '__main__':
  app.run()

