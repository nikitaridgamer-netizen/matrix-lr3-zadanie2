from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import uvicorn
from process_project import process_project

app = FastAPI()

class MatrixRequest(BaseModel):
    matrix: List[List[float]]
    column: int

class MatrixResponse(BaseModel):
    status: str
    result_matrix: List[List[float]]

@app.post("/api/delete_column", response_model=MatrixResponse)
def delete_column_api(data: MatrixRequest):
    try:
        result = process_project(data.matrix, data.column)
        return {"status": "success", "result_matrix": result}
    except Exception:
        return {"status": "error", "result_matrix": []}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)