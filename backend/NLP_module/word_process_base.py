from snownlp import SnowNLP
class Word_Process_Base:
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