import subprocess
from gtts import gTTS

import indicoio
indicoio.config.api_key = 'a93e258e9dd46a47c2454287299ed82b'

# single example
output = indicoio.fer("img/Man-smiling.jpg")
emotions = "A man is "
add='true'

for key in output:
    emotions += str(int(output[key]*100)) + " percent " + str(key)
    # if output[key] >= 0.2:
    #     if add == 'true':
    #         emotions += str(key) + ", "
    #         add = 'false'
    #     else:
    #         emotions += "and " + str(key)

emotions += "15 percent concentrateed power of will"

audio_file = "hello.mp3"
tts = gTTS(text=emotions, lang="en")
tts.save(audio_file)
return_code = subprocess.call(["afplay", audio_file])