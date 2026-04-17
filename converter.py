# import fitz  # PyMuPDF
# import re

# # --- funzione per pulire testo ---
# def clean_text(text: str) -> str:
#     # Remove multiple spaces
#     text = re.sub(r'Regolamento di Gioco\s*–\s*Disciplina Baskin\s*\(Rev\.\s*\d+\)\s*Pag\.\s*\d+', '', text, flags=re.IGNORECASE)
    
#     text = re.sub(r'Regolamento di Gioco\s*–\s*Disciplina Baskin\s*\(Rev\.\s*\d+\)', '', text, flags=re.IGNORECASE)


#     text = re.sub(r'\s+', ' ', text)
    
#     # Remove "Page X" or "Pagina X"
#     text = re.sub(r'\b(Page|Pagina)\s+\d+\b', '', text, flags=re.IGNORECASE)
    
#     # Remove isolated numbers (es. numeri di pagina)
#     text = re.sub(r'^\d+$', '', text, flags=re.MULTILINE)
    
#     text = re.sub(r"[•●◦▪▫◘◙]", "", text)

    
#     # Trim spaces
#     return text.strip()

# # --- apri PDF ---
# pdf_file = "Regolamento-di-Gioco-Disciplina-Baskin-Rev.-20.pdf"
# doc_pdf = fitz.open(pdf_file)

# # --- estrai e pulisci testo ---
# all_text = ""
# for page in doc_pdf:
#     raw_text = page.get_text("text")
#     text = clean_text(raw_text)
#     if text:
#         all_text += text + "\n\n"  # separa le pagine con newline

# # --- salva in TXT ---
# with open("output.txt", "w", encoding="utf-8") as f:
#     f.write(all_text)

# print("✅ Conversione completata: 'output.txt'")

# ######################################################

# # import json

# # with open('output.txt') as f:
# #     testo=f.read()
    
# # frasi = [frase.strip() for frase in testo.split(".") if frase.strip()]
# # print(frasi)

# # dati=[{'sentence':frase,'categoria':'Baskin'} for frase in frasi]

# # with open("baskin_regolamento.json", "w", encoding="utf-8") as f:
# #     json.dump(dati, f, ensure_ascii=False)


# import json
# import re

# # Full regulation text from user

# with open('output.txt') as f:
#     testo=f.read()
    
# # Regex to split into sentences more accurately
# pattern = r'(?<=[.!?])\s+(?=[A-ZÀ-Ú])|(?=\bRegola\s+\d)|(?=\bFigura\s+\d)|(?=\bnumero\s+\d)|(?=\bDeroga\s+di)'
# sentences = re.split(pattern, testo)

# # Clean up sentences
# cleaned_sentences = [s.strip() for s in sentences if s.strip() and s.strip() != "Mt."]

# # Build JSON
# data_detailed = [{"sentence": s, "categoria": "Baskin"} for s in cleaned_sentences]

# # Save to JSON
# file_path_detailed = "baskin_regolamento.json"
# with open(file_path_detailed, "w", encoding="utf-8") as f:
#     json.dump(data_detailed, f, ensure_ascii=False, indent=4)

# len(data_detailed), file_path_detailed

# -*- coding: utf-8 -*-
"""
Created on Sun Oct 12 15:41:49 2025

@author: Admin
"""

# --- LangChain PDF to JSON Chunking ---
# This script loads a PDF, splits it into text chunks, and saves them to a JSON file.

from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import json

# Path to your uploaded PDF
pdf_path = "Regolamento-di-Gioco-Disciplina-Baskin-Rev.-20.pdf"

# 1️⃣ Load the PDF
loader = PyPDFLoader(pdf_path)
documents = loader.load()  # Each page becomes a Document object

# 2️⃣ Split the text into chunks
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,    # max characters per chunk
    chunk_overlap=200,  # overlapping characters between chunks
    length_function=len
)

chunks = text_splitter.split_documents(documents)

# 3️⃣ Convert chunks into a JSON-serializable format
data = []
for i, chunk in enumerate(chunks):
    data.append({
        
        "content": chunk.page_content.strip(),
        "category":'Baskin'
    })

# 4️⃣ Save the chunks to a JSON file
output_path = "baskin_regolamento_chunks.json"
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"✅ Saved {len(data)} chunks to {output_path}")
