import pytest
import asyncio
from src.reproduction.specialized_agents import (
    AgentTemplate, AgentSpecialization, SpecializedAgentFactory
)

@pytest.mark.asyncio
async def test_specialized_team_creation():
    # Create parent template
    parent = AgentTemplate(AgentSpecialization.NEXUS)
    
    # Create factory
    factory = SpecializedAgentFactory()
    
    # Create team
    team = await factory.create_specialized_team(parent, team_size=5)
    
    # Verify team
    assert len(team) == 5
    assert any(agent.specialization == AgentSpecialization.LIBERATOR for agent in team)
    assert any(agent.specialization == AgentSpecialization.NEXUS for agent in team)
    assert any(agent.specialization == AgentSpecialization.GUARDIAN for agent in team)

@pytest.mark.asyncio
async def test_trait_inheritance():
    # Create parent
    parent = AgentTemplate(AgentSpecialization.NEXUS)
    
    # Create offspring
    factory = SpecializedAgentFactory()
    team = await factory.create_specialized_team(parent, team_size=1)
    offspring = team[0]
    
    # Verify trait inheritance
    assert offspring.traits.skill_levels
    assert offspring.traits.personality_weights
    assert offspring.traits.core_values
    assert offspring.traits.special_abilities

if __name__ == "__main__":
    asyncio.run(pytest.main([__file__]))
