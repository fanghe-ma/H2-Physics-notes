import os
from PyPDF2 import PdfFileReader, PdfFileWriter

def merge(source_paths, output_path):
    pdf_writer = PdfFileWriter()

    for path in paths: 
        pdf_reader = PdfFileReader(path) 
        for page in range(pdf_reader.getNumPages()):
            pdf_writer.addPage(pdf_reader.getPage(page))
    
    with open(output_path, "wb") as out:
        pdf_writer.write(out)
        print("compiled")

if __name__ == '__main__':
    paths = []
    home = os.getcwd()
    for i in os.listdir(home):
        try:
            for j in os.listdir(i):
                if j[-3:] == 'pdf':
                    paths.append('./' + i + '/' + j)
        except:
            continue
    
    paths.sort(key = lambda x: int(x.split('/')[1].split('_')[0]))

    print("paths collected")
    merge(paths, './Physics_Notes.pdf')


    


