from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import uvicorn
import requests

app = FastAPI()

@app.get("/{username}")
async def twitter_user(username: str, response_class=HTMLResponse):
    headers = {
        "User-Agent": "Googlebot"
    }
    ret = requests.get("https://twitter.com/" + username, headers=headers)
    return HTMLResponse(content=ret.text, status_code=200)

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(
        description='elongate - dumb twitter proxy'
    )
    parser.add_argument(
        '--port', '-p',
        metavar='N',
        type=int,
        default=8000,
        help='Specify port, defaults to 8000.'
    )
    args = vars(parser.parse_args())

    uvicorn.run("elongate:app", host="127.0.0.1", port=args['port'], log_level="info")
