from flask import Flask, request, jsonify
from netmiko import ConnectHandler

# Initialize Flask application
app = Flask(
    __name__,
    static_url_path='',  # Specify static file URL path
    static_folder='static',  # Specify folder for static files
)

# Route for serving the main HTML page
@app.route("/")
def index():
    return app.send_static_file("index.html")  # Serve the index.html file

# Route for connecting to a network device
@app.route('/connect', methods=['POST'])
def connect():
    # Get form data from the POST request
    device_type = request.form['device_type']  # Type of the device (e.g., cisco_ios)
    host = request.form['host']  # IP address of the device
    username = request.form['username']  # Username for authentication
    password = request.form['password']  # Password for authentication
    command = request.form['command']  # Command to execute on the device

    try:
        # Establish a connection to the network device
        net_connect = ConnectHandler(
            device_type=device_type,
            host=host,
            username=username,
            password=password,
        )

        # Send the command to the device and capture the output
        output = net_connect.send_command(command)
        result = {"status": "success", "output": output}  # Success response
    except Exception as e:
        print(f"Error: {e}")  # Log the error to the console
        result = {"status": "error", "message": str(e)}  # Error response

    return jsonify(result)  # Return the result as JSON

# Entry point for running the application
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)  # Run the app on all interfaces, port 5000
