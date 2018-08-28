import os
from flask import Flask, url_for, render_template, request

app = Flask(__name__)


@app.route('/')
def render_main():
    return render_template('home.html')


@app.route('/ctof')
def render_ctof():
    return render_template('ctof.html')


@app.route('/ftoc')
def render_ftoc():
    return render_template('ftoc.html')


@app.route('/mtokm')
def render_mtokm():
    return render_template('mtokm.html')


@app.route('/ftoc_result')
def render_ftoc_result():
    try:
        ftemp_result = float(request.args['fTemp'])
        ctemp_result = ftoc(ftemp_result)
        return render_template('ftoc_result.html', fTemp=ftemp_result, cTemp=ctemp_result)
    except ValueError:
        return "Sorry: something went wrong."


@app.route('/ctof_result')
def render_ctof_result():
    try:
        ctemp_result = float(request.args['cTemp'])
        ftemp_result = ctof(ctemp_result)
        return render_template('ctof_result.html', cTemp=ctemp_result, fTemp=ftemp_result)
    except ValueError:
        return "Sorry: something went wrong."


@app.route('/mtokm_result')
def render_mtokm_result():
    try:
        mdist_result = float(request.args['mDist'])
        kmdist_result = mtokm(mdist_result)
        return render_template('mtokm_result.html', mDist=mdist_result, kmDist=kmdist_result)
    except ValueError:
        return "Sorry: something went wrong."


def hello():
    return "What's Up!"


def ftoc(ftemp):
    return (ftemp - 32.0) * (5.0 / 9.0)


def ctof(ctemp):
    return (ctemp * (9 / 5)) + 32


def mtokm(mdist):
    return (mdist * 1.61)


if __name__ == "__main__":
    app.run(port=5000, debug=False)
