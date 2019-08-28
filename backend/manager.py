import os
from flask import Flask, render_template, request, make_response, send_from_directory
from flask import jsonify
from flask_cors import CORS
from textsummary import TextSummary
from stanfordcorenlp.corenlp import StanfordCoreNLP
import dlib
import numpy as np
import cv2
import time
from NLP_module.word_process_base import Word_Process_Base
from NLP_module import en_wordcloud_Generater
from flask_uploads import UploadSet, configure_uploads, IMAGES, patch_request_class
from CV.face_recognition import GetFace, del_file, recognition, findNearestClassForImage, CheckFace


app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

app.config['UPLOAD_FOLDER'] = os.getcwd()  # 配置文件存储路径为-当前工作目录
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 配置文件存储大小限制
app.config['UPLOADED_PHOTOS_DEST'] = os.getcwd()
app.config.from_pyfile("config.ini")

basedir = os.path.abspath(os.path.dirname(__file__))
photos = UploadSet('photos', IMAGES)
configure_uploads(app, photos)
patch_request_class(app)  # set maximum file size, default is 16MB


@app.route('/api/nlp')
def home():
  nlp_parsing = StanfordCoreNLP('stanford-corenlp-full-2018-10-05',quiet = False,lang = 'zh')
  input_text = request.args.get('input')
  result = Word_Process_Base.word_split(input_text)
  word_tagging, key_words = Word_Process_Base.Part_of_Speech_tagging(input_text)
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
    # fullfilename = request.args.get('filename')  # 获取需下载的文件名
    response = make_response(send_from_directory('./', "test2.csv", as_attachment=True))
    response.headers["Content-Disposition"] = "attachment; filename=test.csv"
    response.headers["Content_Type"] = "application/octet-stream"
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

@app.route('/api/word_cloud', methods=['GET', 'POST'])
def Word_Cloud():
    """
    词云生成功能
    :return:
    """
    if request.method == 'GET':
      con = request.args.get("content")
      # 本地图片(最好是白底)路径
      imagePath = 'static/img/background.png'
      # 词云图保存路径
      imageSavePath = 'static/word_cloud_img/word_cloud.png'
      img = en_wordcloud_Generater.Word_Cloud.en_wordcloud_text_gen(con, imagePath, imageSavePath, False)  # 返回的是图片类型，可直接保存的格式。但不能转化为url
      img.save(imageSavePath, optimize=True)  # 添加路劲参数后即可直接保存
      file_url = photos.url(imageSavePath)  # 将待传图片进行URL转化
      response = {
        "img_url": file_url  # 将图片的url传输给前端
      }
      return jsonify(response)
      
      
if __name__ == '__main__':
  app.run()

