from flask import Flask, render_template, request
from flask import jsonify
from flask_cors import CORS
import jieba.posseg as pseg

app = Flask(__name__,
            static_folder="./dist/static",
            template_folder="./dist")
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

def word_split(text):
  # 分词功能
  split_result = ""
  words = pseg.cut(text)
  for w in words:
    split_result += str(w.word)+ " "
  return split_result

@app.route('/api/random')
def home():
  input_text = request.args.get('input')
  result = word_split(input_text)
  response = {
    'split_result': result
  }

  return jsonify(response)


if __name__ == '__main__':
  app.run()


