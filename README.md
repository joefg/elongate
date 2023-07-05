# elongate

A dumb Twitter proxy for the terminally online.

## Usage

`pipenv install; pipenv update; pipenv run python3 elongate.py`

Spawns a proxy on `localhost:8000`, use `localhost:8000/<username>` to see
a user's page.

It's literally a dumb proxy that tacks on a Googlebot user-agent header.

It doesn't support accounts or sessions and never will. Please don't ask.
