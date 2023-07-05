# elongate

A dumb Twitter proxy for the terminally online.

## Usage

```
# Prepare your python environment
pipenv install && pipenv update

# Run the service through the virtualenv
pipenv run python3 elongate.py
```

It's literally a dumb proxy that tacks on a Googlebot user-agent header.

It doesn't support accounts or sessions and never will. Please don't ask.

## Endpoints

Ideally, each local URL should correspond to the real Twitter URL.

| Local URL                                | Twitter URL                     |
| ---------------------------------------  | ------------------------------- |
| `localhost/<username>`                   | `http://twitter.com/<username>`                   |
| `localhost/<username>/status/<tweet-id>` | `http://twitter.com/<username>/status/<tweet-id>` |
