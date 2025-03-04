from fastapi import FastAPI
from src.api import users
from src.middlewares import error_handler
app = FastAPI()
app.add_middleware(error_handler.ErrorHandlerMiddleware)
error_handler.setup_exception_handlers(app)
