import fitz 
import os

def extraer_texto_pdf (nombre_archivo): 
    texto_extraido= ""
    documento= fitz.open(nombre_archivo)
    for pagina in documento: 
        texto_extraido += pagina.get_text()
        documento.close()


def buscar_palabras_c(pdf_file,palabras_a_buscar,archivo_salida): 
    coincidencias=[]

    pdf= fitz.open (pdf.file)

    for n_pag in range(len(pdf)):
        page= pdf.load_page(n_pag)
        texto= page.get_text()

        for palabra in palabras_a_buscar:
            if palabra in texto: 
                coincidencias.append ((n_pag+1,palabra))

def main(archivo_pdf,archivo_palabras,archivo_salida):
    texto_pdf= extraer_texto_pdf(archivo_pdf)
   

