from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import FileResponse
import os
from converters.docx_to_pdf import convert_docx_to_pdf

app = FastAPI()

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.post("/convert")
async def convert(file: UploadFile = File(...)):
    if not file.filename.endswith(".docx"):
        raise HTTPException(status_code=400, detail="Only .docx files are allowed.")

    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    with open(file_path, "wb") as f:
        f.write(await file.read())

    try:
        pdf_path = convert_docx_to_pdf(file_path)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    return FileResponse(pdf_path, media_type="application/pdf", filename=os.path.basename(pdf_path))


#creates uploads directory
def create_upload_folder():
    try:
        os.makedirs(UPLOAD_FOLDER, exist_ok=True)
        print(f"[INFO] Pasta '{UPLOAD_FOLDER}/' verificada/criada com sucesso.")
    except Exception as e:
        print(f"[ERRO] Não foi possível criar a pasta '{UPLOAD_FOLDER}/': {str(e)}")
        raise

create_upload_folder()