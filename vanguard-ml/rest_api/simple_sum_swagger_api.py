import json
import numpy as np
import pickle
from flask import Flask, request, jsonify
from flasgger import Swagger
from flasgger.utils import swag_from
from flasgger import LazyString, LazyJSONEncoder
from sklearn import tree

def add_2_numbers(num1, num2):
    output = {"sum_of_numbers": 0}
    sum_of_2_numbers = num1 + num2
    output["sum_of_numbers"] = sum_of_2_numbers
    return output

def ml_predict(l_input):
    print("2", l_input)
    pickled_model = pickle.load(open('model.pkl', 'rb'))
    output = pickled_model.predict([l_input])
    print(output)
    return output

app = Flask(__name__)
app.config["SWAGGER"] = {"title": "Swagger-UI", "uiversion": 2}


swagger_config = {
    "headers": [],
    "specs": [
        {
            "endpoint": "apispec_1",
            "route": "/apispec_1.json",
            "rule_filter": lambda rule: True,  # all in
            "model_filter": lambda tag: True,  # all in
        }
    ],
    "static_url_path": "/flasgger_static",
    # "static_folder": "static",  # must be set by user
    "swagger_ui": True,
    "specs_route": "/swagger/",
}

template = dict(
    swaggerUiPrefix=LazyString(lambda: request.environ.get("HTTP_X_SCRIPT_NAME", ""))
)

app.json_encoder = LazyJSONEncoder
swagger = Swagger(app, config=swagger_config, template=template)


@app.route("/")
def index():
    return "Add 2 Numbers!"


@app.route("/ml_predict", methods=["POST"])
@swag_from("swagger_config.yml")
def add_numbers():
    input_json = request.get_json()
    print(input_json)
    try:
        l_test = []

        num1 = int(input_json["x1"])
        num2 = int(input_json["x2"])
        num3 = int(input_json["x3"])

        print(num1, num2, num3)
        
        l_test.append(num1)
        l_test.append(num2)
        l_test.append(num3)

        #res = add_2_numbers(num1, num2)
        print("1", l_test)
        arr_res = ml_predict(l_test)

        # serialize a NumPy array into JSON
        lists_res = arr_res.tolist()

    except:
        lists_res = {"success": False, "message": "Unknown error"}

    return json.dumps(lists_res)


if __name__ == "__main__":
    app.run(debug=True, port=8791)
