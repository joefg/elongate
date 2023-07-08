from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import uvicorn
import requests

app = FastAPI(
    docs_url=None,
    redoc_url=None
)

@app.get("/{username}")
async def twitter_user(username: str, response_class=HTMLResponse):
    headers = {
        "User-Agent": "Googlebot"
    }
    ret = requests.get("https://twitter.com/" + username, headers=headers)
    return HTMLResponse(content=ret.text, status_code=200)

@app.get("/{username}/with_replies")
async def twitter_user_with_replies(username: str, response_class=HTMLResponse):
    headers = {
        "User-Agent": "Googlebot"
    }
    ret = requests.get("https://twitter.com/" + "/".join([username, 'with_replies']), headers=headers)
    return HTMLResponse(content=ret.text, status_code=200)

@app.get("/{username}/status/{tweet}")
async def twitter_tweet(username: str, tweet: int, response_class=HTMLResponse):
    headers = {
        "User-Agent": "Googlebot"
    }
    ret = requests.get("https://twitter.com/" + "/".join([username, 'status', str(tweet)]), headers=headers)
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
