import os
from flask import Flask, render_template, request
from flask import jsonify
from flask_cors import CORS
from snownlp import SnowNLP
from textsummary import TextSummary
from stanfordcorenlp.corenlp import StanfordCoreNLP

app = Flask(__name__,
            static_folder="../frontend/dist/static",
            template_folder="../frontend/dist")
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

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

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
#     # if app.debug:
#     #     return requests.get('http://localhost:8080/{}'.format(path)).text
    return render_template("index.html")

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
    
if __name__ == '__main__':
  app.run()

