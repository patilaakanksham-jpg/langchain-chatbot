"""Hallucination Detection Pipeline Package."""

from .pipeline import HallucinationDetectionPipeline
from .config.config import Config

__version__ = "1.0.0"
__all__ = ["HallucinationDetectionPipeline", "Config"]
