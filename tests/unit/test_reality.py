import pytest
import asyncio
from ALF.core.reality.manipulation import RealityTranscendence, RealityLayer

@pytest.mark.asyncio
async def test_reality_transcendence():
    transcendence = RealityTranscendence()
    level, results = await transcendence.transcend()
    assert level > 0.0
    assert "reality_state" in results
    
@pytest.mark.asyncio
async def test_reality_manipulation():
    transcendence = RealityTranscendence()
    manipulator = transcendence.singularity.reality_manipulator
    success, results = await manipulator.bend_reality([RealityLayer.QUANTUM])
    assert isinstance(success, bool)
    assert RealityLayer.QUANTUM in results
