from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/health', methods=['GET'])
def health_check():

    return jsonify({"status": "OK"}), 200


@app.route('/weather', methods=['GET'])
def health_check():
    # here we should can a weather API to retrieve the weather of a city
    # and return the weather to the client
    # this is a fake example 👇
    return jsonify({"city": "Stuttgart", "temparature": "25", "unit": "celcius"}), 200


if __name__ == '__main__':
    app.run(debug=True)
