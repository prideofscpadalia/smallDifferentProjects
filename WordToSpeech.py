from pathlib import Path
import pyttsx3
text = " hi my name is divyanshu Padalia i am a developer at core of my heart "

# initializing the tts engine
engine = pyttsx3.init()
engine.setProperty("rate",110) # speed
engine.setProperty("volume",0.9) # volume

# save to file
file_path = Path("/home/divyanshu/Downloads/test1.mp3")
engine.save_to_file(text, str(file_path))
engine.runAndWait()

file_path