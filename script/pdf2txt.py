import fitz
import re 

pdf = fitz.open("data/Diabetes/DIABETES.pdf")
text = ""
for page in pdf:
    text += page.get_text()

def clean_text(text):
    text = re.sub(r'\n+', '\n', text)  # Replace multiple newlines with a single newline
    text = re.sub(r'\s+', ' ', text)  # Replace multiple spaces with a single space
    return text.strip()  # Remove leading and trailing whitespace

cleaned_text = clean_text(text)

with open("data/Diabetes/DIABETES.txt", "w", encoding="utf-8") as f:
    f.write(cleaned_text)