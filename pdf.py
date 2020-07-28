import PyPDF2
import sys

inputs = sys.argv[1:]

with open(inputs[0], 'rb') as file:
	reader = PyPDF2.PdfFileReader(file)
	page = reader.getPage(0)
	page.rotateClockwise(90)
	writer = PyPDF2.PdfFileWriter() 
	writer.addPage(page)
	with open('rotate.pdf', 'wb') as new_file:
		writer.write(new_file)


def pdf_combiner(pdf_list):
	merger = PyPDF2.PdfFileMerger()
	for pdf in pdf_list:
		print(pdf)

		merger.append(pdf)
	merger.write('combined.pdf')


if __name__ == "__main__":
	pdf_combiner(sys.argv[1:])