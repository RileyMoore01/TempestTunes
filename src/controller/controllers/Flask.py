#pip install flask

from flask import request, Flask, render_template

app = Flask('server')

@app.route('/py', methods=['Get', 'POST'])

def server():
    if request.method == 'POST':
        # Get data from the form
        tag = request.form['tag']

        # Get the username/password associated with this tag
        user, password = tag.lookup(tag)

        return 'Tag: %s Username: %s Password: %s' % (tag, user, password) 
        # return render_template('asset_information.html',
        #                        username=user, 
        #                        password=password)

    else:   
        return render_template('index.html')

test = 'test'
username = ''
password = ''
asset_tag = {{}}

print(test)