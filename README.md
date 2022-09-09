# FastAPI

---

This is an example of an API written using python [FastAPI framework](https://fastapi.tiangolo.com/) and you can check some useful examples implemented here.

## Bootstrapping

FastAPI project is mainly an instance of `FastAPI` class. You can set many configurations when instance this class like title, description and so on.

You get [Swagger](https://swagger.io/) and [Redoc](https://redocly.com/redoc/) for free, just enabling at the instance time, like:

```python
app = FastAPI(
    title="API title",
    description="API Description",
    docs_url="/docs",  # Swagger, None to disable
    redoc_url="/redoc",  # Redoc, None to disable
)
```

## Pydantic

FastAPI relies on pydantic library to data validation and also uses it in the docs like Swagger

```python
class UserRequest(BaseModel):  # BaseModel = pydantic base class
    name: str = Field(title="Name", description="User first name", example="Ivan")
    age: int = Field(title="Age", description="User age", example="22", gt=0)
```

## Routes

Once you define an instance FastAPI variable, in this case: `app`, we just need to define as a simple decorator in a function to create a route:

```python
@app.get("/users/{id}", summary="Get a specific user")
def get(id: int):
    user = user_repository.get(id)
    if not user:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "Not found")
    return user
```

If you `User` type has a lot of fields and you want only return a few fields, you can simply set a `response_model` and keep the function untouched, like:

```python
class UserResponse(BaseModel):
    id: int
    name: str

@app.get("/users/{id}", summary="Get a specific user", response_model=UserResponse)
def get(id: int):
    ...
```

## Dependency injection

FastAPI has a very powerful [Dependency Injection system](https://fastapi.tiangolo.com/tutorial/dependencies/) that is very useful when you need to:

- Have shared logic (the same code logic again and again).
- Share database connections.
- Enforce security, authentication, role requirements, etc.
- And many other things...

If you want to ensure that a request is protected and can only be accessed for a known user, you can define a structure like that:

```python
def get_logged_username():
    # check token existence in the header request
    # parse and validate the token
    # extract and return current user
    # if something goes wrong, raise and HTTP 401 exception
    ...

@app.get("/users/{id}", summary="Get a specific user", response_model=UserResponse)
def get(id: int, username: str = Depends(get_logged_username)):
    # this method will be executed only if we get a valid username 
    ...
```

## Run locally

Command to run locally: `uvicorn python_module:instance_variable`. You can also put the flag `--reload` to reload the project every time you make a change:

```python
pip install uvicorn
uvicorn main:app --reload  # main.py -> app = FastAPI(...)
```

## More info

You can find all details in the [official documentation here](https://fastapi.tiangolo.com/).
