#sous windows
.\env\Scripts\activate.bat

#sous linux/MacOS
source \env\Scripts\activate

#installer les packages 
pip install -r requirements.txt

#lancer le serveur
python app.py
