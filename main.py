from PyPDF2 import PdfWriter, PdfReader
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

import os;



from data import document_data;







colors = [[1,8,133], [0,0,255], [255,0,255], [0,255,255]];

for i in range(0, len(colors)):
    for j in range(0, 3):
        colors[i][j] /= 255;


pdfmetrics.registerFont(TTFont('Arial Bold Italic', 'font.ttf'))

def main():
    reader = open("input.pdf", "rb");
    existing_pdf = PdfReader(reader)

    res = write_text(document_data, existing_pdf, reader);



def flatten(obj):

    out = [];

    keys = list(obj.keys());

    for i in range(0, len(keys)):
        coords = obj[keys[i]];

        for j in range(0, len(coords)):

            out.append(coords[j]);

    return out;



def write_text(document_data, input, reader):

    name = "output.pdf";

    keys = list(document_data.keys());

    for i in range(0, len(keys)):

        commands = flatten(document_data[keys[i]]);

        packet = io.BytesIO()
        packet.seek(0)
        can = canvas.Canvas(packet, pagesize=letter, bottomup=1);

        can.setFont("Arial Bold Italic", 10)

        if(len(commands) == 0): continue;

        for j in range(0, len(commands)):

            #print(str(i) + "," + str(j))

            command = commands[j];
            coordinate = command['coordinates'];
            x = coordinate[0];
            y = coordinate[1];
            color = colors[command['color']];
            text = command['value'];
            can.setFillColorRGB(color[0], color[1], color[2]);

            #print(text);

            can.drawString(x, y, text)

        can.save()

        new_pdf = PdfReader(packet)

        page = input.pages[i]
        page.merge_page(new_pdf.pages[0])

        print("Finished Page " + str(keys[i]))

    output = PdfWriter()

    for i in range(0, len(input.pages)):
        output.add_page(input.pages[i])

    reader.close();

    if(os.path.isfile(name)): os.remove(name);

    output_stream = open(name, "wb")

    print("Writing to '" + name + "'...");

    output.write(output_stream)
    output_stream.close()

    print("Finished writing!")

main();
