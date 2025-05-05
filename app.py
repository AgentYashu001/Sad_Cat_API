from flask import Flask, jsonify
import random

app = Flask(__name__)

# Random facts array
facts = [
    "Cats sleep for 70% of their lives.",
    "I meowed and nobody meowed back...",
    "The Moon has moonquakes.",
    "Octopuses have three hearts. But I have only one.",
    "You can’t hum while holding your nose. Try it.",
    "Bananas are berries, but strawberries aren’t."
]

@app.route('/')
def home():
    return "Welcome to SadCat API!"

@app.route('/sadcat')
def random_fact():
    return jsonify({
        "fact": random.choice(facts)
    })

if __name__ == '__main__':
    app.run()
