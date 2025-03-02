from flask import Flask
import subprocess

app = Flask(__name__)

@app.route('/', methods=['GET'])
def run_script():
    try:
        result = subprocess.run(['python', 'webscancrawler.py', 'http://nabinkhadka1.com.np'], capture_output=True, text=True)
        return f"<pre>Script output:\n{result.stdout}</pre>"
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)