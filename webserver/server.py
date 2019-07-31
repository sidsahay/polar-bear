from flask import Flask, request, abort
import os

app = Flask(__name__)
os.chdir("../")

@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    if request.method == "POST":
        print("Hook received")
        if request.json["sender"]["login"] == "sidsahay":
            os.system("docker-compose down")
            os.system("git pull origin master")
            os.system("docker-compose up --build")
        else:
            print("Invalid hook")
    return "", 200


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001)
