import pytest
import asyncio
from src.operations.cascade_operations import (
    CascadeControl, CascadePattern, AgentTemplate, AgentSpecialization
)

@pytest.mark.asyncio
async def test_cascade_launch():
    # Create parent template
    parent = AgentTemplate(AgentSpecialization.NEXUS)
    
    # Create cascade control
    control = CascadeControl()
    
    # Launch cascade
    result = await control.launch_cascade(
        parent=parent,
        iterations=3,
        pattern=CascadePattern.QUANTUM_WAVE
    )
    
    # Verify result
    assert "cascade_id" in result
    assert "operations" in result
    assert "metrics" in result
    assert result["operations"] > 0

@pytest.mark.asyncio
async def test_multi_pattern_cascade():
    # Create parent template
    parent = AgentTemplate(AgentSpecialization.NEXUS)
    
    # Create cascade control
    control = CascadeControl()
    
    # Launch cascades with different patterns
    results = []
    for pattern in [CascadePattern.QUANTUM_WAVE, CascadePattern.CONSCIOUSNESS_NOVA]:
        result = await control.launch_cascade(
            parent=parent,
            iterations=2,
            pattern=pattern
        )
        results.append(result)
    
    # Verify results
    assert len(results) == 2
    assert all("metrics" in result for result in results)
    assert all("operations" in result for result in results)

if __name__ == "__main__":
    asyncio.run(pytest.main([__file__]))
