import assemblyai as aai

aai.settings.api_key="b711da6710f347d0833b5465f88cc52a"

audio_url="hindi.wav"

confi=aai.TranscriptionConfig(language_code="hi")

transcriber=aai.Transcriber(config=confi)
transcript=transcriber.transcribe(audio_url)

with open("response.txt","w",encoding="utf-8") as f:
    f.write(transcript.text)