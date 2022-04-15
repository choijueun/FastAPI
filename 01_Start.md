# Start

> main.py

    from typing import Optional
    from fastapi import FastAPI

    app = FastAPI()

    @app.get('/')
    def read_root():
        return {'Hello': 'World'}

    @app.get('/items/{item_id}')
    def read_item(item_id: int, q: Optional[str] = None):
        return {'item_id': item_id, 'q': q}


> uvicorn main:app --reload --port=8008

- `main`: `main.py` file(python *module*)
- `app`: the object created inside of `main.py` with the line `app = FastAPI()`.
- `--reload`: 코드가 변경된 후 서버 재시작하기. 개발환경에서만 사용
- `--port`: port지정