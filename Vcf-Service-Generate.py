from fastapi import FastAPI, Query, BackgroundTasks
from fastapi.responses import FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
import os
import time
import logging
import unicodedata
import re

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()
VCF_FOLDER = "vcf_files"
os.makedirs(VCF_FOLDER, exist_ok=True)

app.mount("/vcf", StaticFiles(directory=VCF_FOLDER), name="vcf")

def slugify(text):
	text = unicodedata.normalize('NFD', text).encode('ascii', 'ignore').decode('utf-8')
	text = re.sub(r'[^a-zA-Z0-0Z\s]', '', text)
	text = re.sub(r'\s+', '_', text)
	return text.lower()

def delete_file_later(file_path: str, delay_seconds: int = 300):
	import time
	logger.info(f"[INFO] Agendado para deletar {file_path} em {delay_seconds} segundos")
	time.sleep(delay_seconds)
	if os.path.exists(file_path):
		try:
			os.remove(file_path)
			if not os.path.exists(file_path):
				logger.info(f"[SUCESS] Arquivo {file_path} deletado após {delay_seconds} segundos")
			else:
				logger.error(f"[FAIL] Tentativa de deletar {file_path}, mas o arquivo ainda existe")
		except Exception as e:
			logger.exception(f"[ERROR] Falha ao tentar deletar {file_path}: {e}")
	else:
		logger.info(f"[INFO] O arquivo {file_path} não existe mais no momento da exclusão")

@app.get("/generate_vcf")
async def generate_vcf(
	nome: str = Query(...),
	telefone: str = Query(...),
	background_tasks: BackgroundTasks = None
):
	timestamp = int(time.time())
	nome_slug = slugify(nome)
	filename = f"{nome_slug}_{timestamp}.vcf"
	vcf_path = os.path.join(VCF_FOLDER, filename)

	vcf_content = f"""BEGIN:VCARD
VERSION:3.0
FN:{nome}
TEL;TYPE=CELL:{telefone}
END:VCARD
"""

	with open(vcf_path, "w") as f:
		f.write(vcf_content)

	background_tasks.add_task(delete_file_later, vcf_path, 300)
	logger.info(f"[INFO] Arquivo {filename} gerado e agendada exclusão em 300 segundos.")

	return {
		"vcf_url": f"/vcf/{filename}",
		"filename": filename
	}

