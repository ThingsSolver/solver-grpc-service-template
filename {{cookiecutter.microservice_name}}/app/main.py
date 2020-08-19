import uvicorn
import time
from uuid import uuid4
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from app.utils.logger import AppLogger
from app.routers.routes import api

app = FastAPI()

log = AppLogger('main').logger


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    rid = "UID-" + str(uuid4())
    log.info(f"rid={rid} start request path={request.url.path}")
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    formatted_process_time = '{0:.2f}'.format(process_time)
    log.info(f"rid={rid} completed_in={formatted_process_time}ms status_code={response.status_code}")
    response.headers["X-Process-Time"] = str(process_time)
    return response


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(api)

if __name__ == "__main__":
    uvicorn.run(app, port=8080, log_level="info")
