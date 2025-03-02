from flask import Flask
import subprocess

app = Flask(__name__)

@app.route('/run-script', methods=['GET'])
def run_script():
    try:
        result = subprocess.run(['python', 'webscancrawler.py'], capture_output=True, text=True)
        return f"Script output:\n{result.stdout}"
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)