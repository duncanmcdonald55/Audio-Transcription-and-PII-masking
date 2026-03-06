import whisper
from presidio_analyzer import AnalyzerEngine
from presidio_anonymizer import AnonymizerEngine

file_path = r"C:\Users\dunca\OneDrive\Desktop\audio_file.mp4"

"""Transcription Stage"""
model = whisper.load_model("base")
result = model.transcribe(file_path)
transcribed_text = result["text"]

print("============Transcribed Text===============")
print(transcribed_text)


"""PII Detection Stage"""
analyzer = AnalyzerEngine()
entities_found = analyzer.analyze(text=transcribed_text, language="en")

print("\n======PII Entities Detected======")
for entity in entities_found:
    print(f"{entity.entity_type} | score: {entity.score:.2f} | '{transcribed_text[entity.start:entity.end]}'")


"""PII Masking"""
anonymizer = AnonymizerEngine()
anonymized = anonymizer.anonymize(text=transcribed_text, analyzer_results=entities_found)

print("====Anonymized Text====")
print(anonymized.text)

