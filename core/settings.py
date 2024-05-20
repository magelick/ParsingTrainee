from pathlib import Path
from core.types.settings import Settings

# Main full path to the project
BASE_DIR = Path(__file__).resolve().parent.parent
# Initial instance of Settings
SETTINGS = Settings()  # type: ignore
