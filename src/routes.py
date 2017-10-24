from form import form
from flask import Flask, request, redirect
app = Flask(__name__)


@app.route('/', methods=['POST'])
def contact():
    if request.form:
        form.submit(request.form)

    return redirect(request.referrer + '?success')
