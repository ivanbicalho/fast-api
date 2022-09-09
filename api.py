from fastapi import FastAPI
import routes.users as users
import routes.login as login
import routes.greetings as greetings

# Multiple versions strategies:
# https://github.com/tiangolo/fastapi/issues/381#issuecomment-584132553

DESCRIPTION = """
This is an example of an API written using python FastAPI framework<br>
To see more details, check <a href="https://github.com/ivanbicalho/fast-api">this github project</a><br><br>
See redoc instead of swagger: <a href="/redoc">go to redoc</a><br>
See swagger instead of redoc: <a href="/docs">go to swagger</a><br><br>
To authenticate, click the AUTHORIZE button and enter these credentials:<br>
username: admin<br>
password: admin
"""

app = FastAPI(
    title="My first Fast API",
    description=DESCRIPTION,
    terms_of_service="https://carta.com",
    contact={
        "Developer name": "Ivan Bicalho",
        "email": "ivan.bicalho@carta.com",
    },
    version="0.0.1",
    docs_url="/docs",  # Swagger, None to disable
    redoc_url="/redoc",  # Redoc, None to disable
)

app.include_router(login.router)
app.include_router(greetings.router)
app.include_router(users.router)


# RUN LOCALLY:
# pip install uvicorn
# uvicorn main:app --reload
