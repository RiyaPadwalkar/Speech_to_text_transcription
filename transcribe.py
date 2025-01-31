# Import the necessary libraries
import whisper

# Load the Whisper model
model = whisper.load_model("base")

# Define the function to transcribe the audio file
def transcribe_audio(audio_file):
    # Load the audio file
    audio = whisper.load_audio(audio_file)
    
    # Transcribe the audio file
    result = model.transcribe(audio)
    
    # Get the transcribed text
    text = ""
    for segment in result["segments"]:
        text += segment["text"] + " "
    
    # Return the transcribed text
    return text

# Define the main function
def main():
    # Define the input audio file
    audio_file = "engpoem.wav"
    
    # Transcribe the audio file
    text = transcribe_audio(audio_file)
    
    # Append the transcribed text to a text file
    with open("transcribed_textengpoem.txt", "a", encoding="utf-8") as f:
        f.write(text + "\n")

# Call the main function
if __name__ == "__main__":
    main()