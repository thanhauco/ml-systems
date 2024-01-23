import os
import yaml
from typing import Dict, Any, Type, TypeVar
from dataclasses import dataclass

T = TypeVar('T')

class ConfigLoader:
    """
    Handles loading configuration from YAML files and environment variables.
    Supports basic variable substitution.
    """
    
    @staticmethod
    def load_yaml(path: str) -> Dict[str, Any]:
        if not os.path.exists(path):
            raise FileNotFoundError(f"Config file not found: {path}")
        
        with open(path, 'r') as f:
            # Safe loader for security
            content = yaml.safe_load(f)
            
        return ConfigLoader._resolve_env_vars(content)

    @staticmethod
    def _resolve_env_vars(config: Any) -> Any:
        """Recursively replace ${VAR} with os.environ['VAR']"""
        if isinstance(config, dict):
            return {k: ConfigLoader._resolve_env_vars(v) for k, v in config.items()}
        elif isinstance(config, list):
            return [ConfigLoader._resolve_env_vars(i) for i in config]
        elif isinstance(config, str) and config.startswith("${") and config.endswith("}"):
            var_name = config[2:-1]
            return os.getenv(var_name, config) # Return original if not found (or raise error)
        return config

    @staticmethod
    def to_dataclass(config_dict: Dict[str, Any], dataclass_type: Type[T]) -> T:
        """Hydrates a dataclass from a dict."""
        # In a real system, use Pydantic for validation
        return dataclass_type(**config_dict)
