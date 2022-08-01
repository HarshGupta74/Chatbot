from email import message
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from chat import get_response
import mysql.connector
db1=mysql.connector.connect(host='localhost',user='root',password='Harsh@2002',database='college')

cur=db1.cursor()
s='insert into chat values(%s,%s)'

app= Flask(__name__)
CORS(app)


@app.post("/predict")
def predict():
    text = request.get_json().get("message")
    # TODO: check if text is valid
    response = get_response(text)
    message = {"answer": response}
    if response=="I do not understand...":
        t=("*",text)
        cur.execute(s,t)
        db1.commit()
    return jsonify(message)

if __name__ == "__main__":
    app.run(debug=True)


