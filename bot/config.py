import yaml
import dotenv
from pathlib import Path
import os

config_dir = Path(__file__).parent.parent.resolve() / "config"

# load yaml config
config_filepath = os.getenv("CONFIG_FILEPATH", "config.yml")
with open(config_filepath, 'r') as f:
    config_yaml = yaml.safe_load(f)

# load .env config
dotenv.load_dotenv()

# config parameters
telegram_token = os.getenv("TELEGRAM_TOKEN")
openai_api_key = os.getenv("OPENAI_API_KEY")
anthropic_api_key = os.getenv("ANTHROPIC_API_KEY")


openai_api_base = config_yaml.get("openai_api_base", None)
allowed_telegram_usernames = config_yaml["allowed_telegram_usernames"]
new_dialog_timeout = config_yaml["new_dialog_timeout"]
enable_message_streaming = config_yaml.get("enable_message_streaming", True)
return_n_generated_images = config_yaml.get("return_n_generated_images", 1)
image_size = config_yaml.get("image_size", "512x512")
n_chat_modes_per_page = config_yaml.get("n_chat_modes_per_page", 5)
mongodb_uri = f"mongodb://{os.getenv('MONGODB_HOST')}:{os.getenv('MONGODB_PORT')}"
mongodb_password = os.getenv('MONGODB_PASSWORD', '')
mongodb_username = os.getenv('MONGODB_USERNAME', 'root')

# chat_modes
with open(config_dir / "chat_modes.yml", 'r') as f:
    chat_modes = yaml.safe_load(f)

# models
with open(config_dir / "models.yml", 'r') as f:
    models = yaml.safe_load(f)

# files
help_group_chat_video_path = Path(__file__).parent.parent.resolve() / "static" / "help_group_chat.mp4"
