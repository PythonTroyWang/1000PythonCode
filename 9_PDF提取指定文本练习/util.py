from pdfminer.pdfparser import PDFParser
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LTTextBoxHorizontal, LAParams
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfpage import PDFTextExtractionNotAllowed

import re
import os
import shutil


def parse(file):
    f = open(file, 'rb')
    title = ''
    parser = PDFParser(f)
    doc = PDFDocument(parser)
    parser.set_document(doc)
    if not doc.is_extractable:
        raise PDFTextExtractionNotAllowed
    else:
        rsrcmagr = PDFResourceManager()
        laparams = LAParams()
        device = PDFPageAggregator(rsrcmagr, laparams=laparams)
        interpreter = PDFPageInterpreter(rsrcmagr, device)

        for page in PDFPage.create_pages(doc):
            interpreter.process_page(page)
            layout = device.get_result()
            for x in layout:
                if isinstance(x, LTTextBoxHorizontal):
                    word = x.get_text().replace('\n', '')
                    p = re.compile(r'(.*?)Document Nr.:(\d{10})')
                    result_match = p.match(word)
                    if result_match is not None:
                        a = p.match(word).group(2)
                        title = a
    f.close()
    shutil.copyfile(file, 'result/' + title + ".pdf")


def get_file(dir_path):
    file_type = ".pdf"
    ret_array = []

    for dir_path, dir_names, file_names in os.walk(dir_path):
        for filename in file_names:
            if file_type in filename:
                ret_array.append(os.path.join(dir_path, filename))
    return ret_array
