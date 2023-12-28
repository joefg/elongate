# elongate

---

**RETIRED AS OF END 2023**

This is no longer under active development, and will only come back online if
Elon decides to close the gate again.

---

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
| `localhost/<username>/with_replies`      | `http://twitter.com/<username>/with_replies`      |
| `localhost/<username>/status/<tweet-id>` | `http://twitter.com/<username>/status/<tweet-id>` |
