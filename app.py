from flask import Flask,request,render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route('/demo',methods=['POST'])
def profit():
    if (request.method=='POST'):
        operation=request.json['operation']
        item1=request.json['item1']
        item2=request.json['item2']
        item3=request.json['item3']
        item4=request.json['item4']
        item5=request.json['item5']
        result=item1+item2+item3+item4+item5
        cost=0
        if result<=1000:
            cost=result-result*0.1
        elif result>1000 and result<=2000:
            cost=result-result*0.2
        else: 
            cost=result-result*0.3
        return 'the price of the good is {}'.format(cost,result)


@app.route('/demo2',methods=['POST'])
def profit2():
    if (request.method=='POST'):
        operation=request.form['operation']
        item1=int(request.form['item1'])
        item2=int(request.form['item2'])
        item3=int(request.form['item3'])
        item4=int(request.form['item4'])
        item5=int(request.form['item5'])
        result=item1+item2+item3+item4+item5
        cost=0
        if result<=1000:
            cost=result-result*0.1
        elif result>1000 and result<=2000:
            cost=result-result*0.2
        else: 
            cost=result-result*0.3
        return render_template('result.html',cost=cost)

if __name__=="__main__":
    app.run(host="0.0.0.0",port=5000)
