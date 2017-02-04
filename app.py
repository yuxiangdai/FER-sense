from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def main():
    return render_template('index.html')

@app.route('/happy')
def my_link():
    import subprocess
    from gtts import gTTS

    import indicoio
    indicoio.config.api_key = 'a93e258e9dd46a47c2454287299ed82b'

    # single example
    output = indicoio.fer("Man-smiling.jpg")
    emotions = "The subject is"
    add='true'

    emotions += str(int(output['Happy']*100)) + " percent Happy"

    audio_file = "hello.mp3"
    tts = gTTS(text=emotions, lang="en")
    tts.save(audio_file)
    return_code = subprocess.call(["afplay", audio_file])

if __name__ == "__main__":
    app.run()
