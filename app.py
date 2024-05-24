from flask import Flask, request, render_template
from stories import *
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SECRET_KEY'] = '123'

debug = DebugToolbarExtension(app)

@app.route('/')
def get_questions():
    """Shows story and form at homepage"""
    prompts = story.prompts
    return render_template("questions.html", prompts=prompts)

@app.route('/story')
def get_story():
    """shows resulting story for the answers"""
    ans = {prompt: request.args.get(prompt) for prompt in story.prompts}
    your_story = story.generate(ans)
    return render_template("answer.html", answer=your_story)
    