@ECHO OFF
:comentario
virtualenv venv
pip install --upgrade pip
pip install -r requirements.txt
PAUSE