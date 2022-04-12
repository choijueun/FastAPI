> uvicorn main:app --reload

- `main`: `main.py` file(python *module*)
- `app`: the object created inside of `main.py` with the line `app = FastAPI()`.
- `--reload`: 코드가 변경된 후 서버 재시작하기. 개발환경에서만 사용