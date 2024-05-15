from pathlib import Path

# Get the directory where the script is located dynamically to avoid errors when generating exe file package
SCRIPT_DIR = Path(__file__).resolve().parent

ASSETS_DIR = SCRIPT_DIR / "assets"
DEFINITIONS_FILE = ASSETS_DIR / "data" / "data.json"

APP_STYLESHEET = """
background-color: #C3FF93;
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
background-color: #FFDB5C;
font-weight: bold;
"""

BUTTON2_STYLESHEET = """
background-color: #FFAF61;
font-weight: bold;
"""

SIGNATURE_STYLESHEET = """
font-family: 'Verdana';
font-size: 10pt;
"""
