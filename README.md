# Calculator API — GitHub Actions CI/CD Learning Project

A tiny Flask web API that does basic math. The app is intentionally simple —
the real purpose of this repo is to **learn CI/CD with GitHub Actions** step by step.

## Project structure

```
python-cicd-demo/
├── app/
│   ├── __init__.py        # package + version
│   ├── calculator.py      # pure business logic (add, subtract, multiply, divide)
│   └── main.py            # Flask API exposing the calculator
├── tests/
│   ├── test_calculator.py # unit tests for the logic
│   └── test_api.py        # tests for the HTTP endpoints
├── requirements.txt       # runtime dependencies
├── requirements-dev.txt   # dev/test dependencies (pytest, flake8)
├── .flake8                # lint settings
└── .gitignore
```

## Run locally

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements-dev.txt

python -m app.main               # starts on http://localhost:5000
```

Try it:

| Endpoint | Example | Response |
|---|---|---|
| `GET /` | `/` | welcome message + version |
| `GET /health` | `/health` | `{"status": "ok"}` |
| `GET /calculate/<op>` | `/calculate/add?a=2&b=3` | `{"result": 5.0, ...}` |

Operations: `add`, `subtract`, `multiply`, `divide`.

## Test and lint

```bash
pytest -v        # run all tests
flake8 .         # check code style
```

## CI/CD roadmap (we'll build these one by one)

- [ ] 1. First workflow — run tests on every push / pull request
- [ ] 2. Add linting (flake8) to the pipeline
- [ ] 3. Test on multiple Python versions (matrix build)
- [ ] 4. Dependency caching + code coverage report
- [ ] 5. Branch protection — block merges if CI fails
- [ ] 6. Build a Docker image
- [ ] 7. Push the image to a registry (GitHub Container Registry)
- [ ] 8. Deploy (secrets, environments, manual approvals)
- [ ] 9. Release on git tags
