import PyPDF2
import os
import helper.processing as pr

pdfWriter = PyPDF2.PdfWriter()

def automaticOption():
    init_dir = r'Documents'
    for pdfs in os.listdir(init_dir):
        final_dir = f'{init_dir}\{pdfs}'
        pdf = PyPDF2.PdfReader(final_dir)
        for pageNum in range(len(pdf.pages)):
            pageObj = pdf.pages[pageNum]
            pdfWriter.add_page(pageObj)
            
    fileName = input('Ingrese el nombre con el qeu se guardará el PDF (sin extensión .pdf): ')
    fileName = f'Results\{fileName}.pdf'
    pdfOutputFile = open(fileName, 'wb')
    pdfWriter.write(pdfOutputFile)
    pdfOutputFile.close()

def manualOption():
    print('Cuando desee terminar con el uultimo documento presione enter sin ingresar ningun nombre:')
    file = input('Ingrese el nombre del documento: ')
    while file != '':
        file = pr.eliminateParts(file)
        pdf = PyPDF2.PdfReader(file)
        for pageNum in range(len(pdf.pages)):
            pageObj = pdf.pages[pageNum]
            pdfWriter.add_page(pageObj)
        print('PDF Cargado')
        file = input('Ingrese el nombre del documento: ')
    
    fileName = input('Ingrese el nombre con el qeu se guardará el PDF (sin extensión .pdf): ')
    fileName = f'Results\{fileName}.pdf'
    pdfOutputFile = open(fileName, 'wb')
    pdfWriter.write(pdfOutputFile)
    pdfOutputFile.close()

        
