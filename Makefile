setup_venv:
	@echo "Setting up virtual environment..."
	@python3.12 -m venv .venv

# run this manually if you want to activate the virtual environment - make does not support activating venvs directly
# activate_venv:
# 	@echo "Activating virtual environment..."
# 	. .venv/bin/activate

freeze_deps:
	@echo "Freezing dependencies..."
	@pip freeze > requirements.lock.txt 
	@echo "Dependencies frozen."

install_deps:
	@echo "Installing dependencies..."
	@pip install -r requirements.txt -e .
	@echo "Dependencies installed."

run:
	@echo "Running application..."
	@python src/app.py

test:
	@echo "Running tests..."
	@pytest --cov=src --cov-report=html --cov-report=term-missing --verbose
	@echo "Tests completed."

test_sanity:
	@echo "Running sanity tests..."
	@pytest -m sanity --cov=src --cov-report=html --cov-report=term-missing --verbose
	@echo "Sanity tests completed."

test_not_sanity:
	@echo "Running non-sanity tests..."
	@pytest -m "not sanity" --cov=src --cov-report=html --cov-report=term-missing --verbose
	@echo "Non-sanity tests completed."