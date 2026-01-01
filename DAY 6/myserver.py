from flask import Flask

# 1. Create the App (The "Manager")
app = Flask(__name__)

# 2. Define the Homepage (The "Reception Desk")
@app.route('/')
def home():
    return "<h1>Hello Class! This is my Pi Server.</h1>"

# 3. Define a Secret Page (A "Back Room")
@app.route('/secret')
def secret_room():
    return "<h2>You found the secret page! 🕵️‍♂️</h2>"

# 4. Start the Server (Open the Shop)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5100)
