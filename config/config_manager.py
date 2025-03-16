import json
from pathlib import Path


class ConfigManager:
    def __init__(self, config_file="config.json"):
        """
        Initializes the ConfigManager with a configuration file path.
        """
        self.config_file = Path(config_file)
        self.config = self._load_default_config()  # Load default config
        self.load()  # Load configuration from file

    def _load_default_config(self):
        """
        Returns a dictionary of default configuration values.
        """
        return {
            "site_name": "My Blog",
            "base_url": "http://localhost:8080",
            "theme": "default",
            "output_dir": "output",
            "template_dir": "templates",
            "markdown_library": "mistune",
        }

    def load(self):
        """
        Loads configuration from the config file. Falls back to defaults if the file is missing or invalid.
        """
        try:
            with open(self.config_file, "r") as file:
                user_config = json.load(file)
                if self.validate(user_config):
                    self.config.update(user_config)  # Override defaults with user config
        except (FileNotFoundError, json.JSONDecodeError):
            print(
                f"Warning: Config file '{self.config_file}' not found or invalid. Using defaults."
            )

    def save(self):
        """
        Saves the current configuration to the config file.
        """
        with open(self.config_file, "w") as file:
            if self.validate(self.config):
                json.dump(self.config, file, indent=4)

    def get(self, key, default=None):
        """
        Retrieves a configuration value by key. Returns the default value if the key is not found.
        """
        return self.config.get(key, default)

    def validate(self, config):
        """
        Validates the configuration to ensure required keys are present.
        """
        required_keys = config
        for key in required_keys:
            if key not in self.config:
                raise ValueError(f"Missing required configuration key: {key}")
        for key in self.config:
            if key not in required_keys:
                print(f"Warning: Unknown configuration key: {key}")