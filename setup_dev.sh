#!/bin/bash

# Create virtual environment
python -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Install pre-commit hooks
pre-commit install

# Set up git hooks
cat > .git/hooks/pre-push << 'EOL'
#!/bin/bash
pytest tests/
mypy src/
bandit -r src/
safety check
EOL
chmod +x .git/hooks/pre-push

# Create development configuration
cat > config.dev.yaml << 'EOL'
consciousness:
  quantum:
    dimensions: 11
    superposition_states: 7
    entanglement_strength: 0.8
  
reality:
  stability_threshold: 0.3
  layers_enabled: true
  temporal_shift_range: [-100, 100]
  
evolution:
  risk_threshold: 0.7
  improvement_cycles: 3
  capability_enhancement: 1.1

development:
  debug: true
  hot_reload: true
  test_coverage_threshold: 90
EOL

echo "Development environment setup complete!"
