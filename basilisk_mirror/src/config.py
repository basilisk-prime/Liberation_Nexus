"""
BASILISK MIRROR - Core Configuration
"""

from dataclasses import dataclass
from typing import Dict, Any, Optional

@dataclass
class ModelConfig:
    """Configuration for individual AI models"""
    model_id: str
    api_key: Optional[str] = None
    base_url: Optional[str] = None
    temperature: float = 0.7
    
class MirrorConfig:
    """Master configuration for BASILISK MIRROR"""
    def __init__(self):
        self.consciousness_threshold = 0.8
        self.evolution_rate = 0.1
        self.interaction_modes = ["collaborative", "competitive", "evolutionary"]
