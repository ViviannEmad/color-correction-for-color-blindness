from flask import Flask, render_template, request
import json

app = Flask(__name__)

# Correct answers for each plate
correct_answers = [
    "12", "8", "6", "29", "57", "5", "3", "15", "74", "2",
    "6", "97", "45", "5", "7", "16", "73", "26", "42", "35", "96"
]

def determine_color_blindness(answers):
    # Initialize counts for each type of color blindness
    protanopia_protanomaly_count = 0
    deuteranopia_deuteranomaly_count = 0
    red_green_count = 0
    
    # Check answers for each plate
    for i, answer in enumerate(answers):
        if answer != correct_answers[i]:
            if i == 17:  # Plate 18
                if answer == "6":
                    protanopia_protanomaly_count += 1
                elif answer == "2":
                    deuteranopia_deuteranomaly_count += 1
            else:
                red_green_count += 1

    # Determine the type based on counts
    if protanopia_protanomaly_count > 0:
        return "Protanopia or Protanomaly"
    elif deuteranopia_deuteranomaly_count > 0:
        return "Deuteranopia or Deuteranomaly"
    elif red_green_count > 0:
        return "Red-green color blindness"
    else:
        return "Normal Eyes"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/results', methods=['POST'])
def results():
    # Collect user answers
    answers = [request.form.get(f'plate_answer{i+1}') for i in range(21)]

    if len(answers) != len(correct_answers):
        return "The number of answers does not match the number of questions.", 400

    # Calculate score
    score = sum(1 for i, answer in enumerate(answers) if answer == correct_answers[i])
    
    # Determine color blindness type
    color_blindness = determine_color_blindness(answers)

    return render_template('results.html', score=score, total=len(correct_answers), color_blindness=color_blindness)

if __name__ == '__main__':
    app.run(debug=True)
