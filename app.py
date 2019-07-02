

from flask import Flask, render_template, request
from flask import jsonify
from flask_cors import CORS
#import jieba.posseg as pseg
from snownlp import SnowNLP
# import unicode

app = Flask(__name__,
            static_folder="./frontend/dist/static",
            template_folder="./frontend/dist")
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

def word_split(text):
  # 分词功能
  split_result = ""
  words = SnowNLP(text).words
  for w in words:
    split_result += str(w)+ "/"
  return split_result

def Part_of_Speech_tagging(text):
  # 词性分析和关键词提取
  word_tag = ""
  s = SnowNLP(text)
  for w in s.tags:
    word_tag += w[0] + "->" + w[1] + "/"
  key = s.keywords(3)
  return word_tag, key

@app.route('/api/nlp')
def home():
  input_text = request.args.get('input')
  result = word_split(input_text)
  word_tagging, key_words = Part_of_Speech_tagging(input_text)
  response = {
    'split_result': result,
    'word_tag': word_tagging,
    'key_word': key_words
  }

  return jsonify(response)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
#     # if app.debug:
#     #     return requests.get('http://localhost:8080/{}'.format(path)).text
    return render_template("index.html")

if __name__ == '__main__':
  app.run(host="47.107.228.165")

