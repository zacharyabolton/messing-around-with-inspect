from inspect_ai import Task, task
from inspect_ai.dataset import FieldSpec, MemoryDataset, Sample, hf_dataset
from inspect_ai.scorer import model_graded_qa
from inspect_ai.solver import generate

langs = [
    ('Afrikaans', 'afr_Latn'),
    ('Kyrgyz', 'kir_Cyrl'),
    ('Ganda', 'lug_Latn'),
    ('Tsonga', 'tso_Latn')
]

@task
def language_id():
    labels = ", ".join(lang[0] for lang in langs)
    return Task(
        dataset=MemoryDataset(
            [
                Sample(
                    input=f"Classify this sentence as one of: {labels}.\n\n{sample.input}",
                    target=language,
                )
                for language, code in langs
                for sample in hf_dataset(
                    "facebook/flores", name=code, split="dev",
                    sample_fields=FieldSpec(input="sentence"),
                    shuffle=True,
                    seed=42,
                    limit=5,
                )
            ]
        ),
        solver=generate(),
        scorer=model_graded_qa(),
    )
