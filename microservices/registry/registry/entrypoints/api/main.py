from aws_lambda_powertools import Logger
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from mangum import Mangum
from registry.entrypoints.api.v1.api import router as api_router
from infra.dynamodb import *
from registry.adapters.dynamodb_query_service import *


logger = Logger(service="mangum")

app = FastAPI(
    title="Akello",
    description="API for Measurement Based Care Microservice",
    version="1.0",
    docs_url='/docs',
    openapi_url='/openapi.json',
    redoc_url=None
)


@app.get("/")
def root():
    return {"message": "Measurement Based Care Microservice"}


app.include_router(api_router, prefix="/v1")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

handler = Mangum(app)
handler = logger.inject_lambda_context(handler, clear_state=True)
logger.info('Loaded')
