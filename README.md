# Messing Around with Inspect

Small local evaluations using [Inspect AI](https://inspect.aisi.org.uk/).

## Setup

This project uses its own Python 3.11 virtual environment. Create it once:

```bash
python3.11 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install inspect-ai openai datasets 'Brotli>=1.2.0'
```

The `Brotli>=1.2.0` requirement avoids an incompatibility between the OpenAI SDK's `httpx2` dependency and older Brotli releases.

## Dependency snapshot

After installing or changing dependencies, record the exact working versions:

```bash
python -m pip freeze > requirements.txt
```

To recreate the environment later, activate `.venv` and install that snapshot:

```bash
python -m pip install -r requirements.txt
```

## Future use

From the repository root, activate the environment before running an eval:

```bash
source .venv/bin/activate
```

Make sure `OPENAI_API_KEY` is set in your shell, then run:

```bash
python -m inspect_ai eval simpleqa.py --model openai/gpt-5
```

Using `python -m inspect_ai` guarantees that the command uses the activated
`.venv`, rather than an `inspect` executable left on the shell path by another
Python environment.
