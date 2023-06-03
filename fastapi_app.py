import random
import string

from fastapi import FastAPI


app = FastAPI()
items = []


def get_random_string(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))


@app.get("/")
async def get_items():
    return {
        "message": "App is running",
    }


@app.get("/items")
async def get_items():
    return {
        "message": "Test_get",
        "items": items
    }


@app.post("/items")
async def post_items():
    item = get_random_string(10)
    items.append(item)
    return {
        "message": "Test_post",
        "item": item
    }


@app.put("/items/{item_slug}")
async def put_item(item_slug):
    item = get_random_string(10)
    try:
        items.remove(item_slug)
    except ValueError:
        pass
    items.append(item)
    return {
        "message": "Test_put",
        "item": item
    }


@app.delete("/items/{item_slug}", status_code=204)
async def del_item():
    try:
        items.remove(10)
    except ValueError:
        pass
    return
