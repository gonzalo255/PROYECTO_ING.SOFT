import fitz 
#Abrir el archivo PDF 
doc= fitz.open("PDF1")

#Leer el texto 
with open( "frases.pdf","r") as file: 
    frases= file.readlines()

#Analizar el archivo PDF
with open("PDF2","w") as file: 
    for page in doc: 
        text= page.getText()
        for frase in frases: 
            if frase in text: 
                file.write(frase)
