from flask import Flask, render_template, request
import logging

logging.basicConfig(filename='logs/event.log', format='%(asctime)s-%(levelname)s-%(message)s')
logger = logging.getLogger()
logger.setLevel(logging.INFO)


app = Flask(__name__)

@app.route('/')
def homepage():
    try:
        return render_template('index.html')
    except Exception as e:
        print(f'in index Exception {e}')
        logger.error(f'in index Exception {e}')

@app.route('/math', methods=['POST'])
def math():
    try:
        if (request.method=='POST'):
            return request.form
             
    except Exception as e:
        print(f'in index Exception {e}')
        logger.error(f'in index Exception {e}')



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)