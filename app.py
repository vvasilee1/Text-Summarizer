from flask import Flask, render_template, request
from textSummarizer.pipeline.prediction import PredictionPipeline

app = Flask(__name__)

# Home route - displays the HTML form
@app.route('/')
def index():
    return render_template('index.html')

# Summarization route - handles the text summarization logic
@app.route('/summarize', methods=['POST'])
def summarize():
    if request.method == 'POST':
        input_text = request.form['inputText']
        obj=PredictionPipeline()
        summary_text = obj.predict(input_text)
        return render_template('index.html', inputText=input_text, summaryText=summary_text)

if __name__ == '__main__':
    app.run(debug=True)