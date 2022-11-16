from flask import Flask,request,jsonify

app = Flask(__name__)
tasks = [{"id":1,"title":"finish homework","description":"Today we have math homework","done":False},
         {"id":2,"title":"practise time","description":"practise at 4 to 5","done":False}]

@app.route("/add-data",methods = ["POST"])
def addtask():
    if not request.json:
        return jsonify({"status":"Error","message":"Please provide the data"},400)

    task = {"id":tasks[-1]["id"]+1,"title":request.json["title"],"description":request.json["description"],"done":False}
    tasks.append(task)
    
    return jsonify({"status":"Success","message":"Task added successfully"},200)


@app.route("/getdata")
def getdata():
    return jsonify({"data":tasks})









@app.route("/")
def hello_world():
    return "Hello World"


if __name__ == "__main__":
    app.run(debug = True)
