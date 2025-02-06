from fastapi import FastAPI
import router

app = FastAPI(title="Number Classification API")

app.include_router(router.router)
