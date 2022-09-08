from flask import Flask
from flask import jsonify
from flask import request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/aipugt")
def hello_aipugt():
    return "<p>Hello, AIPUGT!</p>"

@app.route("/aipugt/<path:cmd_params>")
def aipugt(cmd_params):
    # NOTE: replace space blank with +
    print(f"cmd_params:{cmd_params}")
    cmd = cmd_params.split("+")
    cmd = list(filter(lambda s: s=="", cmd))

    def parser_cmd(cmd):
        import argparse
        parser = argparser.ArgumentParser()
        # TODO:replace here
        args = parser.parse_args(cmd)
        return args

    args = parser_cmd(cmd)
    print(f"cmd:{cmd}")

    return jsonify({"cmd_params": cmd_params, "cmd":cmd})




#@app.route("/aipugt/<path:g_path>/<path:i_path>/<path:w_path>/<path:cur_path>")
def aipugt_params(g_path, i_path, w_path, cur_path):
    """Run aipugt with params"""

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

if __name__ == "__main__":
    app.run(debug=True)
