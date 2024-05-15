from pathlib import Path


ASSETS_DIR = Path("./assets")
DEFINITIONS_FILE = ASSETS_DIR / "data" / "data.json"

APP_STYLESHEET = """
background-color: yellow;
font-family: 'Courier New';
font-size: 12pt;
"""

TITLE_STYLESHEET = """
font-size: 30px;
font-weight: bold;
color: #333333; 
margin: 10px; 
text-align: center;  
"""

BUTTON1_STYLESHEET = """
background-color: pink;
font-weight: bold;
"""

BUTTON2_STYLESHEET = """
background-color: orange;
font-weight: bold;
"""

SIGNATURE_STYLESHEET = """
font-family: 'Arial';
font-size: 10pt;
"""