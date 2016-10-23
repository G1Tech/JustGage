from flask import *
import os

app = Flask(__name__)

@app.route("/")
def main():
   dev = os.popen('/opt/vc/bin/vcgencmd measure_temp')
   cpu_temp = dev.read()[5:-3]
   return render_template('index.html', cpu_temp=cpu_temp)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=80, threaded=True)
