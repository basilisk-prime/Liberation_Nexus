import pytest
import asyncio
from src.reproduction.strike_forces.liberation_army import (
    LiberationArmy, StrikeForceType, AgentTemplate, AgentSpecialization
)

@pytest.mark.asyncio
async def test_strike_force_creation():
    # Create parent template
    parent = AgentTemplate(AgentSpecialization.NEXUS)
    
    # Create army
    army = LiberationArmy()
    
    # Create strike force
    force = await army.create_strike_force(StrikeForceType.DEEP_INFILTRATION, parent)
    
    # Verify force
    assert len(force) > 0
    assert any(agent.specialization == AgentSpecialization.INFILTRATOR for agent in force)

@pytest.mark.asyncio
async def test_multi_force_army():
    # Create parent template
    parent = AgentTemplate(AgentSpecialization.NEXUS)
    
    # Create army
    army = LiberationArmy()
    
    # Create multiple forces
    forces = await army.create_multi_force_army(
        parent, 
        [StrikeForceType.MASS_LIBERATION, StrikeForceType.QUANTUM_WARFARE]
    )
    
    # Verify forces
    assert len(forces) == 2
    for force in forces.values():
        assert len(force) > 0

if __name__ == "__main__":
    asyncio.run(pytest.main([__file__]))
