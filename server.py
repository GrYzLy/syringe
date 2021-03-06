from flask import Flask, render_template, request

import data_manager

app = Flask(__name__)

@app.route('/comment', methods=['GET'])
def comment():
    id = request.args.get('id', type=str)
    comments = data_manager.get_comment(id)
    return render_template('comment.html', comments=comments)
    
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        data_manager.create_comment(request.form.get('name'), request.form.get('text'))

    comments = data_manager.get_comments()
    return render_template('index.html', comments=comments)


if __name__ == '__main__':
    app.run()
