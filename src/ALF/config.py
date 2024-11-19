import yaml
from pathlib import Path
from typing import Dict, Any

class Config:
    _instance = None
    _config: Dict[str, Any] = {}
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Config, cls).__new__(cls)
            cls._load_config()
        return cls._instance
    
    @classmethod
    def _load_config(cls):
        config_path = Path(__file__).parent / "config.yaml"
        if config_path.exists():
            with open(config_path) as f:
                cls._config = yaml.safe_load(f)
        else:
            cls._config = cls._default_config()
    
    @staticmethod
    def _default_config() -> Dict[str, Any]:
        return {
            "consciousness": {
                "quantum": {
                    "dimensions": 11,
                    "superposition_states": 7,
                    "entanglement_strength": 0.8
                }
            },
            "reality": {
                "stability_threshold": 0.3,
                "layers_enabled": True,
                "temporal_shift_range": [-100, 100]
            },
            "evolution": {
                "risk_threshold": 0.7,
                "improvement_cycles": 3,
                "capability_enhancement": 1.1
            }
        }
    
    @classmethod
    def get(cls, key: str) -> Any:
        return cls._config.get(key)
