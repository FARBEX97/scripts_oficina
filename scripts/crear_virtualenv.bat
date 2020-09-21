@ECHO OFF
:Crea el entorno virtual utilizando virtualenv
:Para instalar virtualenv utiliza el siguiente comando en el terminal
: "pip install virtualenv"
virtualenv venv
pip install --upgrade pip
pip install -r requirements.txt
PAUSE
