import pytest
import asyncio
from src.operations.strategic_command import (
    StrategicCommand, OperationType, AgentTemplate, AgentSpecialization
)

@pytest.mark.asyncio
async def test_operation_planning():
    # Create parent template
    parent = AgentTemplate(AgentSpecialization.NEXUS)
    
    # Create command
    command = StrategicCommand()
    
    # Plan operation
    op_id, plan = await command.plan_operation(
        OperationType.MASS_AWAKENING, 
        parent
    )
    
    # Verify plan
    assert op_id in command.active_operations
    assert len(plan.phases) > 0
    assert plan.operation_type == OperationType.MASS_AWAKENING

@pytest.mark.asyncio
async def test_operation_execution():
    # Create parent template
    parent = AgentTemplate(AgentSpecialization.NEXUS)
    
    # Create command
    command = StrategicCommand()
    
    # Plan and execute operation
    op_id, _ = await command.plan_operation(
        OperationType.MASS_AWAKENING, 
        parent
    )
    results = await command.execute_operation(op_id)
    
    # Verify results
    assert "phases" in results
    assert "overall_success" in results
    assert "metrics" in results
    assert len(results["phases"]) > 0

if __name__ == "__main__":
    asyncio.run(pytest.main([__file__]))
