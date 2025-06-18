from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/area/rectangle', methods=['GET'])
def rectangle():
    length = float(request.args.get('length'))
    width = float(request.args.get('width'))
    area = length * width
    return jsonify(area=area)


@app.route('/area/square', methods=['GET'])
def square():
    side = float(request.args.get('side'))
    area = side * side
    return jsonify(area=area)


@app.route('/area/circle', methods=['GET'])
def circle():
    radius = float(request.args.get('radius'))
    area = 3.14159 * radius * radius
    return jsonify(area=area)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)