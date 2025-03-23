from flask import Flask, render_template, request
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scan', methods=['POST'])
def run_script():
    url = request.form.get('url')
    try:
        result = subprocess.run(['python', 'webscancrawler.py', url], capture_output=True, text=True)   # http://nabinkhadka1.com.np  i was looking at this guy portfolio let's see how many security vulnerabilities he have
        return render_template('result.html', output=result.stdout, url=url)
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)