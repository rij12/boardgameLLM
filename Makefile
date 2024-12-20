init:
	python3 -m venv venv && venv/bin/pip install -r requirements.txt && venv/bin/python create_db.py --reset

run:
	venv/bin/python query_data.py "$(if $q,$q,)"

reset: 
	venv/bin/python create_db.py --reset
