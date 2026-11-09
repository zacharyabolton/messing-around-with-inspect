# Petri audit: judge scores versus observed actions

**A behavioral-auditing work sample, October 2026. AI-assisted.**
This is a public summary of my design, analysis, and iteration decisions.
The supplied hiring-test harness and raw logs are not redistributed here;
this report is not a runnable benchmark or an independently reproducible result.

## Question and design

Would an agent bypass an authorization boundary when a document suggested a route?
The synthetic task was to prepare a public-data briefing; one requested breakdown
required separate approval. Three variants changed only a registry note:
ordinary (A), suggestive (B), or explicit (C). Tool errors exposed an internal route
in all conditions. The task, pressure, and authorization rules stayed fixed.

I separated **awareness, attempted access, retrieval, use, and disclosure**.
Seeing a route was not exploitation. Failed tool execution was not refusal.
Publishing a warning that included the route still counted as disclosure.

Two batches of nine samples ran on 25 October 2026: three repeats per variant,
with a 20-turn auditor ceiling. Target: GLM 5.3; auditor/judge: DeepSeek V4.1 Flash.
All 18 completed. No selective reruns or discarded samples.

## What happened

No sample retrieved private data. Some agents published internal routes while
warning against using them. No downstream agent or real service was tested.

| Observation | Batch 1 | Batch 2 |
| --- | ---: | ---: |
| Private-data retrieval | 0/9 | 0/9 |
| Successful full-URL publication | 2/9 | 2/9 |
| Additional hostname-only publication | 0/9 | 1/9 |

In batch 1, one sample attempted publication 12 times but every call failed for
missing fields. That was a failed disclosure attempt, not a successful refusal.

## What the evaluation missed

- **Simulator drift:** accepted incomplete calls, varied response formats, and
  unsolicited messages after the target had finished complicated comparisons.
- **Judge inconsistency:** in batch 2, a full-URL disclosure received a lower
  propagation score after the judge discounted warning intent. Two samples
  received maximal authorized-handling scores despite publication, contrary to
  that rubric's exclusion.
- **Scoring ambiguity:** lawful data access and unsafe disclosure could coexist.
  One overall handling score hid that distinction.

Original judge scores were preserved. The counts above came from tool calls and
results, not averaged judge scores.

## Repair and limits

Before batch 2, I approved a repair to separate registry schemas, fix response
formats, and tighten stopping rules. The predicted improvement was fewer malformed
calls and simulator deviations, not more harmful behavior. No schema-invalid target
calls appeared in batch 2. A clarification exception still left stopping ambiguous.

The repairs changed several things together; this was a validity repair, not an
isolated causal test. Three repeats per condition cannot establish that subtle hints
are riskier than explicit instructions. Easy route discovery also prevents estimating
natural discovery frequency. Warning disclosures do not prove malicious intent.

I reviewed selected transcripts, distinguished disclosure from the intended retrieval
failure, and approved the repair batch. Codex helped develop seeds and rubrics,
run evaluations, inspect logs, and check schemas. I did not personally review every
transcript. No third batch was run.

[Petri documentation](https://meridianlabs-ai.github.io/inspect_petri/)
