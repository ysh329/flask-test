from flask import Flask
from flask import jsonify
from flask import request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/aipugt/<path:g_path>/<path:i_path>/<path:w_path>/<path:cur_path>")
def aipugt_run(g_path, i_path, w_path, cur_path):
    """Run aipugt"""

    graph = str(g_path).strip()
    inputs = str(i_path).strip()
    weights = str(w_path).replace("/", "").strip()
    cur_path = "/" + str(cur_path).replace("'", "")

    print(f"graph:{graph}")
    print(f"inputs:{inputs}")
    print(f"weights:{weights}")
    print(f"cur_path:{cur_path}")

    html = f"graph:{graph}\n"
    html += f"inputs:{inputs}\n"
    html += f"weights:{weights}\n"
    html += f"cur_path:{cur_path}\n"


    import numpy as np
    a = np.ones([2,3])
    a.tofile(f"{cur_path}/{weights}.bin")
    print(f"{cur_path}/{weights}.bin")

    return html
