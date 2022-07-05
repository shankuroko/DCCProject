from flask import Flask, render_template,request,jsonify
import pickle
import bz2file as bz2
def decompress_pickle(file):
    data = bz2.BZ2File(file, 'rb')
    data = pickle.load(data)
    return data
model = decompress_pickle('picmodel.pbz2')
tokenizer=pickle.load(open('token.pkl','rb'))
app= Flask(__name__)
@app.route("/")
def index():
  return render_template("./index.html")

@app.route("/getSuggestionList")
def getSiggestion():
  print()
  print(request.args.get('val'))
  print()
  val=request.args.get('val')
  sequence = tokenizer.texts_to_sequences([val])
  preds = model.predict(sequence)
  preds=(preds>0.1)
  res = [i for i, val in enumerate(preds[0]) if val]
  predicted_word = []
  for key, value in tokenizer.word_index.items():
      if value in res:
          predicted_word.append(key)
  return jsonify(render_template("./list.html",x=predicted_word))

if __name__=="__main__":
  app.run(debug=True)