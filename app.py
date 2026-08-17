from flask import Flask, render_template, request
from database.sqlite_manager import create_table
from rag.ingest import ingest
from rag.retrieval import retrieve
from rag.llm import ask_llm
import os

app = Flask(__name__)

create_table()


@app.route("/", methods=["GET", "POST"])
def index():
    cevap = None
    kaynaklar = []
    mesaj = None

    if request.method == "POST":

        # PDF yükleme
        if "pdf" in request.files:
            pdf = request.files["pdf"]

            if pdf and pdf.filename:
                os.makedirs("data", exist_ok=True)

                pdf_path = os.path.join("data", pdf.filename)
                pdf.save(pdf_path)

                ingest(pdf_path)

                mesaj = f"{pdf.filename} başarıyla yüklendi."

        # Soru sorma
        soru = request.form.get("soru")

        if soru:
            results = retrieve(soru)

            context = "\n\n".join([item[2] for item in results])

            cevap = ask_llm(soru, context)

            kaynaklar = [item[1] for item in results]

    return render_template(
        "index.html",
        cevap=cevap,
        kaynaklar=kaynaklar,
        mesaj=mesaj
    )


if __name__ == "__main__":
    app.run(debug=True)