# Messing Around with Inspect

Small experiments while learning [Inspect AI](https://inspect.aisi.org.uk/).
Personal learning scratchpad; no benchmark conclusions.

- [Language ID](language_id.py): classify 20 FLORES examples across four
  languages, using model-graded scoring. A 20-sample run completed with GPT-5.
- [SimpleQA](simpleqa.py): load SimpleQA-Verified and try model-graded QA.
  A 1,000-sample run completed with GPT-5.
- **Agentic evaluation:** trying the upstream
  [GDM InterCode CTF task](https://github.com/UKGovernmentBEIS/inspect_evals/tree/main/src/inspect_evals/gdm_intercode_ctf)
  with bash/Python tools in Docker. A 78-sample run completed with GPT-5 nano
  (66/78 flags found) using a local copy of the upstream task.
  Future runs use the installed `inspect-evals` package.
- [Dataset scratch script](scratch/ds_inspect.py): exploratory dataset inspection.

## Setup

Use Python 3.11 and a repository-local environment:

```bash
python3.11 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
```

Commands use the environment's interpreter explicitly, including when another
Python environment is active. `requirements.txt` pins the main packages, not
every transitive dependency. The Brotli minimum avoids a decoding error seen
with older versions in the OpenAI client's HTTP stack.

## Run

Set `OPENAI_API_KEY` in your shell. These commands make paid API calls;
the QA exercises also use a grader model.

```bash
.venv/bin/python -m inspect_ai eval language_id.py --model openai/gpt-5 --model-role grader=openai/gpt-5 --limit 5
.venv/bin/python -m inspect_ai eval simpleqa.py --model openai/gpt-5 --model-role grader=openai/gpt-5 --limit 5
```

For the CTF exploration, start Docker first. The initial run builds a sandbox
image and downloads the upstream challenge data:

```bash
.venv/bin/python -m inspect_ai eval inspect_evals/gdm_intercode_ctf --model openai/gpt-5-nano --limit 1
```

View local logs with:

```bash
.venv/bin/python -m inspect_ai view
```

Two [experiment receipts](examples/runs/README.md) include the full language-ID
and CTF traces, with configuration and provenance notes. Routine `logs/` and
credentials are excluded from Git. Completed runs above are learning exercises,
not comparisons between models or reproductions of published scores.
