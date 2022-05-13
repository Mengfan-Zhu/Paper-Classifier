# Paper-Classifier

## Installation
Download the source code with
`git clone https://github.com/Mengfan-Zhu/PaperClassifier`

### Install the extension

1. Navigate to `PaperClassifier/frontend`, run the command `npm run build`
3. open a Chrome browser, input `chrome://extensions/`, open the Developer mode at the top right side. 
4. Click the ``Load unpacked'' button and choose the `PaperClassifier/frontend/build` folder in the popup window.
5. The extension will appear in this page and make sure to turn on it. 
6. Now you can click the extensions panel on the top right and you can see the paper classifier extension is in here. You can pin the paper classifier extension in the extension bar so that you can access it easier.

### Install other support libraries

You need to install some support libraries if you don't have them in you local machine. Here are the names of the packages you need.<br>
`flask, flask_cors, gensim, nltk, pdfminer.six, bs4, PyPDF2`<br>
You can use `pip install <package-name>` to install the library. <br>
If you are not sure about whether you already have this library, you can use `pip show <package-name>` to check about it.

## Run the app

1. Begin the back-end server. Navigate to `PaperClassifier/backend` and run the command `flask run`.
2. Navigate to a google scholar page where you want to use the extension, and click the extension to open the popup. 
3. Click "Get Result" button to run the application.
4. Wait for several seconds until the table shows. 
5. Click a section to expand the table, and click any of the links to navigate to them. 
