from fastapi import FastAPI


app = FastAPI(
    title="Recipe API", openapi_url="/openapi.json"
)


@app.get("/items/{item_id}")
async def read_item(item_id):
    return {"item_id": item_id}

