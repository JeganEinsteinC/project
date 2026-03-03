from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/contact', methods=['POST'])
def contact():
    data = request.json
    name = data.get('name')
    email = data.get('email')
    message = data.get('message')

    print("New Message Received:")
    print(f"Name: {name}")
    print(f"Email: {email}")
    print(f"Message: {message}")

    return jsonify({"message": "Message received successfully!"})

if __name__ == '__main__':
    app.run(debug=True)
