from fastapi import FastAPI, Request, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
import router

app = FastAPI(title="Number Classification API")

app.include_router(router.router)

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exec:RequestValidationError):
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content=jsonable_encoder({"number":"alphabet", "error": True})
    )