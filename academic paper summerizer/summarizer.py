from transformers import pipeline

generator = pipeline(
    task="text-generation",
    model="distilgpt2"
)

def summarize_text(text):
    prompt = (
        "Summarize the following academic text in a concise paragraph:\n\n"
        f"{text}\n\nSummary:"
    )

    output = generator(
        prompt,
        max_new_tokens=120,
        do_sample=False
    )

    return output[0]["generated_text"].split("Summary:")[-1].strip()
