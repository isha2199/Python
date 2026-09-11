from pypdf import PdfReader

def read_pdf(file_path):
    reader = PdfReader(file_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"

    return text


def split_text(text, chunk_size=500):
    chunks = []
    for i in range(0, len(text), chunk_size):
        chunk = text[i:i + chunk_size]
        chunks.append(chunk)

    return chunks


pdf_text = read_pdf("Isha_Resume.pdf")

chunks = split_text(pdf_text)

print("Number of chunks:", len(chunks))

for i, chunk in enumerate(chunks):
    print("\n--- CHUNK", i, "---")
    print(chunk)