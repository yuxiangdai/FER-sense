from flask import Flask, render_template
import subprocess
from gtts import gTTS

import indicoio
indicoio.config.api_key = 'a93e258e9dd46a47c2454287299ed82b'

output = indicoio.fer("img/Man-smiling.jpg")

app = Flask(__name__)

@app.route("/")
def main():
    return render_template('index.html')

@app.route('/happy')
def happy():
    output = indicoio.fer("img/Man-smiling.jpg")
    emotions = "The subject is"
    add='true'

    emotions += str(int(output['Happy']*100)) + " percent happy"

    audio_file = "output.mp3"
    tts = gTTS(text=emotions, lang="en")
    tts.save(audio_file)
    return_code = subprocess.call(["afplay", audio_file])
    return render_template('index.html')

@app.route('/sad')
def sad():
    emotions = "The subject is" + str(int(output['Sad']*100)) + " percent sad"

    audio_file = "output.mp3"
    tts = gTTS(text=emotions, lang="en")
    tts.save(audio_file)
    return_code = subprocess.call(["afplay", audio_file])
    return render_template('index.html')

@app.route('/angry')
def angry():
    emotions = "The subject is" + str(int(output['Angry']*100)) + " percent angry"

    audio_file = "output.mp3"
    tts = gTTS(text=emotions, lang="en")
    tts.save(audio_file)
    return_code = subprocess.call(["afplay", audio_file])
    return render_template('index.html')

@app.route('/fear')
def fear():
    emotions = "The subject is" + str(int(output['Fear']*100)) + " percent fear"
    
    audio_file = "output.mp3"
    tts = gTTS(text=emotions, lang="en")
    tts.save(audio_file)
    return_code = subprocess.call(["afplay", audio_file])
    return render_template('index.html')

@app.route('/surprise')
def surprise():
    emotions = "The subject is" + str(int(output['Surprise']*100)) + " percent surprise"
    
    audio_file = "output.mp3"
    tts = gTTS(text=emotions, lang="en")
    tts.save(audio_file)
    return_code = subprocess.call(["afplay", audio_file])
    return render_template('index.html')

@app.route('/neutral')
def neutral():
    emotions = "The subject is" + str(int(output['Neutral']*100)) + " percent neutral"
    
    audio_file = "output.mp3"
    tts = gTTS(text=emotions, lang="en")
    tts.save(audio_file)
    return_code = subprocess.call(["afplay", audio_file])
    return render_template('index.html')

if __name__ == "__main__":
    app.run()
