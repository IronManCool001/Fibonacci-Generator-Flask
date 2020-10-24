from flask import Flask,render_template,request,redirect

def fibo(nterms):
    """
    info:This is a function which is used to calculate fibonacci numbers
    """
    global fiboSeries
    fiboSeries= [0,1]
    if nterms>=2:
        for i in range(2, nterms):
            nextElement = fiboSeries[i-1] + fiboSeries[i-2]
            fiboSeries.append(nextElement)
    else:
        fiboSeries=[]


app = Flask(__name__)
@app.route('/')
def home():
    #print(fiboSeries)
    showResult()
    redirects +1
    print(redirects)
    return render_template('index.html',numbers=fiboSeries)

@app.route('/fibonacci', methods=['POST','GET'])
def showResult():
    if request.method == "POST":
        no_of_terms = request.form['numbterms']
        c = int(no_of_terms)
        fibo(c)
        print(fiboSeries)
        global redirects 
        redirects = 0
        redirects +1
        return redirect('/')