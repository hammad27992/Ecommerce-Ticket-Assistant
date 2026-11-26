from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from service import mock_analyze

app = FastAPI()


class TicketRequest(BaseModel):
    ticket: str
    prompt_version: str = "v2"


@app.post("/analyze")
def analyze_ticket(request: TicketRequest):

    try:
        result = mock_analyze(
            request.ticket,
            request.prompt_version
        )
        return result

    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )