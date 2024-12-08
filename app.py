from flask import Flask, request, jsonify
from netmiko import ConnectHandler

app = Flask(__name__,
            static_url_path='', 
            static_folder='static',
            )

@app.route("/")
def index():
   return app.send_static_file("index.html")

@app.route('/connect', methods=['POST'])
def connect():
    device_type = request.form['device_type']
    host = request.form['host']
    username = request.form['username']
    password = request.form['password']
    command = request.form['command']  # Get the command from the form

    # Setup the network connection
    net_connect = ConnectHandler(
        device_type=device_type,
        host=host,
        username=username,
        password=password,
    )

    try:
        # Send the command to the device and capture the output
        output = net_connect.send_command(command)
        result = {"status": "success", "output": output}
    except Exception as e:
        print(f"Error: {e}")  # Print the error to the console (or log it)
        result = {"status": "error", "message": str(e)}

    return jsonify(result)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
