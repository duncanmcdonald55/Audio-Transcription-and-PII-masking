import whisper

file_path = r"C:\Users\dunca\OneDrive\Desktop\audio_file.mp4"

model = whisper.load_model("base")

result = model.transcribe(file_path)

print(result["text"])

