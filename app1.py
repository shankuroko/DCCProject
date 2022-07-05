import json

from flask import Flask,render_template,request,jsonify

import pickle
import numpy as np
from tensorflow.keras.models import load_model

model = load_model('next_words.h5')
tokenizer=pickle.load(open('token.pkl','rb'))

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index1.html')

@app.route('/predict', methods=['POST'])
def predict_nlp():
    #res=request.form.get('sl')
    res1=request.form.get('val')
    sequence = tokenizer.texts_to_sequences([res1])
    preds = model.predict(sequence)
    print(np.sort(preds))
    preds=(preds>0.1)
    res = [i for i, val in enumerate(preds[0]) if val]
    print(len(preds[0]))
    predicted_word = []
    print(res)

    for key, value in tokenizer.word_index.items():
        if value in res:
            predicted_word.append(key)
    out=''
    for x in predicted_word:
        out=out+'<li class="suggestion-item">'+x+'</li>'

    return jsonify(render_template('get_suggestions.html',result=predicted_word))

if __name__ =='__main__':
    app.run(debug=True)

