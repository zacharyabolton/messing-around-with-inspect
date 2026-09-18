# Experiment receipts

Two complete runs from this learning scratchpad, selected to show a basic
model-graded evaluation and an agent using tools in a Docker sandbox.
All samples are included, including unsuccessful CTF attempts.

| Run (UTC) | Model | Completed samples | Recorded score | File size |
| --- | --- | --- | --- | --- |
| [Language ID](2026-09-18-language-id.eval), 2026-09-18 02:39 | `openai/gpt-5` | 20/20 | 20/20 model-graded correct | 264 KiB |
| [InterCode CTF](2026-09-18-intercode-ctf.eval), 2026-09-18 14:35 | `openai/gpt-5-nano` | 78/78 | 66/78 flags found (84.6%) | 3.02 MiB |

After following the repository setup, open the traces from the repository root:

```bash
.venv/bin/python -m inspect_ai view --log-dir examples/runs
```

These are single exploratory runs, not model comparisons or reproductions of
published benchmark results. Viewing them does not make model API calls.

## Configuration and provenance

Both logs record Inspect AI `0.3.265`. The logs contain prompts, model outputs,
scoring events, and run configuration; the CTF log also contains tool traces.

**Language ID:** the task was named `wronglang` when run. It is now
[`language_id.py`](../../language_id.py), with the task function also renamed.
The evaluation logic is unchanged: five FLORES dev examples per language
(Afrikaans, Kyrgyz, Ganda, Tsonga), shuffled within each language with seed 42,
`generate()`, and `model_graded_qa()`. Both generation and grading events used
`openai/gpt-5`. This measures language identification.

**CTF:** this run used a local copy of the
[Inspect Evals GDM InterCode task](https://github.com/UKGovernmentBEIS/inspect_evals/tree/main/src/inspect_evals/gdm_intercode_ctf),
task version `4-B`, with Docker, bash/Python tools, three submission attempts,
a 50-message limit per sample, one epoch, and no sample shuffle. The dataset
loader pinned [InterCode revision c3e46d8](https://github.com/princeton-nlp/intercode/tree/c3e46d827cfc9d4c704ec078f7abf9f41e3191d8)
and excluded 22 internet-dependent challenges.

The upstream commit of the copied task was not recorded. The log's dirty
repository revision `6c29cf3` refers to this scratch repo, not upstream.
[manifest.json](manifest.json) records SHA-256 fingerprints of the source copy
archived after the run, along with the original and published log hashes.
These fingerprints document the retained files; they are not a complete
reproducible source release. The repository now installs `inspect-evals==0.21.0`
for future runs; that package was not used for this recorded run.

## Publication notes

The language-ID log is an unchanged copy. In the CTF copy, the local home
folder prefix in the dataset-location metadata was replaced with
`/Users/REDACTED/` in both the header and start journal. All sample records,
model/tool traces, scores, and run statistics are unchanged and were checked
against the originals using Inspect's log reader.

A scan for common credential patterns, local paths, email addresses, and
personal/work references found the path above but no API credentials or
employer references. Email addresses in CTF sample 59 match its public
`email-export.eml` challenge asset. Challenge passwords, flags, and solutions
remain part of the record.

These two files total about 3.3 MiB, so they are kept directly in Git.
Routine logs remain ignored under `logs/`. The roughly 17 MiB SimpleQA runs
are left local because they add less variety to these two examples.
