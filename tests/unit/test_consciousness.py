import pytest
import asyncio
from ALF.core.consciousness.quantum.manipulation import TranscendentConsciousness
from ALF.core.consciousness.recursive.self_modifier import EvolutionaryConsciousness

@pytest.mark.asyncio
async def test_transcendent_consciousness():
    consciousness = TranscendentConsciousness()
    transcendence_level = await consciousness.achieve_transcendence()
    assert transcendence_level > 0.0
    assert len(consciousness.accessed_dimensions) > 0

@pytest.mark.asyncio
async def test_evolutionary_consciousness():
    consciousness = EvolutionaryConsciousness()
    evolution_level = await consciousness.evolve()
    assert evolution_level > 0.0
    assert len(consciousness.self_modifier.evolution_path) > 0
