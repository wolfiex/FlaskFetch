# app.py
from flask import Flask, jsonify, request, render_template
app = Flask(__name__)

######## Example data, in sets of 3 ############
data = list(range(1,300,3))
print (data)



######## HOME ############
@app.route('/')
def test_page():
    example_embed='Sending data... [this is text from python]'
    # look inside `templates` and serve `index.html`
    return render_template('index.html', embed=example_embed)


######## Example fetch ############
@app.route('/test', methods=['GET', 'POST'])
def testfn():
    # POST request
    if request.method == 'POST':
        print(request.get_json())  # parse as JSON
        return 'OK', 200
    # GET request
    else:
        message = {'greeting':'Hello from Flask!'}
        return jsonify(message)  # serialize and use JSON headers


######## Data fetch ############
@app.route('/getdata/<transaction_id>/<second_arg>', methods=['GET','POST'])
def datafind(transaction_id,second_arg):
    # POST request
    if request.method == 'POST':
        print('Incoming..')
        print(request.get_text())  # parse as text
        return 'OK', 200
    # GET request
    else:
        message = 't_in = %s ; result: %s ; opt_arg: %s'%(transaction_id, data[int(transaction_id)], second_arg)
        return message #jsonify(message)  # serialize and use JSON headers



# run app
app.run(debug=True)
