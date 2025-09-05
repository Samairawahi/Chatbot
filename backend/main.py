
from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from typing import Optional
import io

from chatbot import get_chatbot_response
from contacts import EMERGENCY_CONTACTS
from finaltts import generate_tts

app = FastAPI()



class Query(BaseModel):
    prompt: str
    persona: Optional[str] = "farmer"

class TTSRequest(BaseModel):
    text: str
    



@app.post("/ask")
def ask_ai(query: Query):
    user_message = query.prompt.strip().lower()

    if user_message == "help":
        contacts_list = "\n".join(
            [f"• {k.title().replace('_', ' ')}: {v}" for k, v in EMERGENCY_CONTACTS.items()]
        )
        return {"response": f"Emergency Contacts:\n\n{contacts_list}"}

    chatbot_text = get_chatbot_response(query.prompt, query.persona)
    return {"response": chatbot_text}

@app.post("/tts")
def tts_endpoint(request: TTSRequest):
    audio_bytes = generate_tts(request.text)
    return StreamingResponse(io.BytesIO(audio_bytes), media_type="audio/mpeg")







