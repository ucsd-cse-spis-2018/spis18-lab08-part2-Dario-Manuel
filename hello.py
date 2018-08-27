from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Whats Up!"
def ftoc(ftemp):
    return (ftemp-32.0)*(5.0/9.0)
def mtok(mdist):
    return (mdist * 1.61)

@app.route('/ftoc/<ftempString>')
def convertFtoC(ftempString):
    ftemp = 0.0
    try:
        ftemp = float(ftempString)
        ctemp = ftoc(ftemp)
        return "In Farenheit: " + ftempString + " In Celsius " + str(ctemp) 
    except ValueError:
        return "Sorry.  Could not convert " + ftempString + " to a number"

@app.route('/mtok/<mdistString>')
def convertMtoK(mdistString):
    mdist = 0.0
    try:
        mdist = float(mdistString)
        kdist = mtok(mdist)
        return "In Miles: " + mdistString + " In Kilometers: " + str(kdist)
    except ValueError:
        return "Sorry.  Could not convert " + mdistString + " to a number"

if __name__ == "__main__":
    app.run(port=5000, debug = False)
