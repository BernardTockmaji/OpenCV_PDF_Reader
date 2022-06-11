# OpenCV_PDF_Reader
This is a PDF Reader done using open CV and machine learning

<h1>Project Brief:</h1>
This project is written using Python programming language, PyCharm IDE, and OpenCV library<br>
Our functionalities are:<br>
<br>
a.	Converting a pdf file to a list of images.<br>
b.	Changing text color.<br>
c.	Changing background color.<br>
d.	Bookmarking and highlighting text.<br>
e.	Taking screenshots by blinking on a real time video capture. <br>

<h1>Architecture:</h1><br>
The Project consists of separate files combined to work together in the main() file.<br>
<br>
1-	Pdf_files: in this .py file we used the following libraries: fitz, tkinter, glob, os, to build pdf to image function which allows us to transform a pdf file into separate images and store them in our designated directory.<br>
<br>
2-	Eye_comfort_mode: used libraries are cv2 and glob.<br>
for the eye comfort mode, we chose a slightly different method, originally the idea was to extract blue light from the image and replace these blue shades with warmer colors<br>
instead of doing that, we used old computers for reference; their blue light filter screens, and we wrote a function that draws above all our images a transparent rectangle with a slightly yellowish Hue to help diminish the blue light effect and relief the eye from strain.<br>
<br>
3-	Text_coloring: changing text and background colors, we read all the images in the pdf file, saved them in a list and applied Canny edge transformation, then we multiplied the edges with the array of our designated color, as for the background, we replaced the background color as well with the color desired.<br>
<br>
4-	Mark_page: for this functionality we developed three functions.<br>
Draw(path) : takes direct input from mouse and draws rectangle on the area you wish to mark.<br>
Highlight(path): draws a transparent rectangle around the text you wish to highlight.<br>
Draw_marker(path): draws a rectangle around a certain are in the page to mark it. <br>
<br>
5-	Eye_detection: we used ImageGrab from PIL and the haarcascade module to solve this functionality, it works by opening a live feed from the front facing camera, when the face and eyes of the user are recognized, he has the option to enter screenshot mode by pressing ‘s’<br>
After he does, blinking the eyes is an indicator for the device to take a screenshot. <br>
<br>
6-	Main: we used all the previous files along tkinter to apply all written functions.<br>
After choosing the file destination you wish to modify, you can choose which type of functionality would you like to do on your pdf file.<br>
