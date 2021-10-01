# Image Analysis using Microsoft Azure

This is a project that uses Microsoft Azure Computer Vision API to analyze images.
To use this project, you need to install Microsoft Azure SDK for Python.
You must also create a Microsoft Azure account and create Cognitive Service resources.

After creating the Cognitive Service resource, you will get two pieces of information :
- `COGNITIVE KEY`
- `COGNITIVE ENDPOINT`

Paste the `COGNITIVE KEY` and `COGNITIVE ENDPOINT` into the `ImageAnalysis.py` file.

Also, to use this project, you need to put the image, whose analysis you want into the `data` folder.

Finally, run the project using the command :
`python ImageAnalysis.py`