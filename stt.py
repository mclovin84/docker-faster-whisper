from fastapi import FastAPI, UploadFile
import whisper

app = FastAPI()
model = whisper.load_model("base")

@app.post("/transcribe")
async def transcribe(file: UploadFile):
    data = await file.read()
    result = model.transcribe(data)
    return {"text": result["text"]}
