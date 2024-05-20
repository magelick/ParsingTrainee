from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

# Most high router
app = FastAPI(
    title="Parsing-Test-Project",
    description="Simple parsing Lamoda and Twitch",
    default_response_class=ORJSONResponse,
)
