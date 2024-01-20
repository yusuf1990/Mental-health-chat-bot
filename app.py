from flask import Flask, render_template, request
import csv
import random

app = Flask(__name__)

# Function to load data from CSV file
def load_data_from_csv(file_path, encoding='utf-8'):
    data = []
    with open(file_path, 'r', encoding=encoding) as csvfile:
        csvreader = csv.DictReader(csvfile)
        for row in csvreader:
            row = {key: value.strip() for key, value in row.items()}  # Remove leading/trailing whitespaces
            data.append(row)
    return data

# Function to get response based on user input
def get_response(user_input, data):
    user_input_lower = user_input.lower()
    for item in data:
        if user_input_lower in item["Question"].lower():
            return item["Answers"]
    return random.choice(["I'm sorry, I don't have information on that topic.", "I don't understand. Can you rephrase your question?", "I'm still learning!"])

# Load data from CSV file
csv_file_path = 'financeQA.csv'  # Replace with your CSV file path
data = load_data_from_csv(csv_file_path)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.form['user_input']
    response = get_response(user_input, data)
    return render_template('chat.html', user_input=user_input, response=response)

if __name__ == '__main__':
    app.run(debug=True)
