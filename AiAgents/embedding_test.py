import ollama

response = ollama.embed(
    model="nomic-embed-text",
    input="I am a frontend engineer with experience in React."
)

embedding = response["embeddings"][0]

print("Number of values:", len(embedding))
print("First 10 values:", embedding[:10])