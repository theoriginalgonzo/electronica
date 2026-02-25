# PDF examination
## 1. What is the name of the program that exported this PDF file?
- Go to https://www.metadata2go.com/view-metadata
- Select the pdf file
- under creator_tool 
- Answer is Adobe Photoshop CC 2019 
## 2. What PDF version is this file?
- look for pdf_version instead of creator_tool
- answer is 1.7
## 3. What software was used to redact the file and insert a watermark?
- Download PDF-XChangeEditor
- Open the Pdf 
- Right click the black boxes around the watermark and cut
- Black boxes are now gone
- answer is PDFTron
## 4. What is the flag?
- In the document, cut the black box near tlsSocket.getFlag()
- the answer is SKY-PDRD-2390\

# Magic Bytes
## 1. What is the original file type?
- Put the jpeg into cyberchef
- Select strings option
- The output shows IHDR and IDAT in all of the result
- The answer is png
## 2. What is the flag?
- go to https://hexed.it/
- open the file 
- replace the first 12 bytes with: 89 50 4E 47 0D 0A 1A 0A 00 00 00 0D
- open the updated file 
- image will show that the flag is SKY-DSFG-5792