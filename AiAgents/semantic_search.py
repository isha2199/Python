import ollama
from pypdf import PdfReader
import math


def read_pdf(file_path):
    reader = PdfReader(file_path)

    text = ""

    for page in reader.pages:
        text += page.extract_text() + "\n"

    return text


def split_text(text, chunk_size=500):
    words = text.split()

    chunks = []
    current_chunk = []
    current_length = 0

    for word in words:

        if current_length + len(word) > chunk_size:
            chunks.append(" ".join(current_chunk))

            current_chunk = []
            current_length = 0

        current_chunk.append(word)
        current_length += len(word) + 1

    if current_chunk:
        chunks.append(" ".join(current_chunk))

    return chunks


def cosine_similarity(vector_a, vector_b):
    dot_product = 0
    magnitude_a = 0
    magnitude_b = 0

    for a, b in zip(vector_a, vector_b):
        dot_product += a * b
        magnitude_a += a * a
        magnitude_b += b * b

    magnitude_a = math.sqrt(magnitude_a)
    magnitude_b = math.sqrt(magnitude_b)

    return dot_product / (magnitude_a * magnitude_b)


# --------------------------------
# 1. Read PDF
# --------------------------------

pdf_text = read_pdf("Isha_Resume.pdf")

# --------------------------------
# 2. Split into chunks
# --------------------------------

chunks = split_text(pdf_text)

# --------------------------------
# 3. Create embeddings
# --------------------------------

chunk_embeddings = []

for chunk in chunks:

    response = ollama.embed(
        model="nomic-embed-text",
        input=chunk
    )

    embedding = response["embeddings"][0]

    chunk_embeddings.append(embedding)


print("Created embeddings for", len(chunks), "chunks")


# --------------------------------
# 4. Ask a question
# --------------------------------

question = input("\nAsk a question: ")

question_response = ollama.embed(
    model="nomic-embed-text",
    input=question
)

question_embedding = question_response["embeddings"][0]


# --------------------------------
# 5. Compare question with chunks
# --------------------------------

similarities = []

for i, chunk_embedding in enumerate(chunk_embeddings):

    similarity = cosine_similarity(
        question_embedding,
        chunk_embedding
    )

    similarities.append((similarity, i))


# --------------------------------
# 6. Sort by similarity
# --------------------------------

similarities.sort(reverse=True)


# --------------------------------
# 7. Show top 3 chunks
# --------------------------------

print("\nMost relevant chunks:\n")

for similarity, index in similarities[:3]:

    print("Similarity:", similarity)
    print("Chunk:", index)
    print(chunks[index])
    print("-" * 50)