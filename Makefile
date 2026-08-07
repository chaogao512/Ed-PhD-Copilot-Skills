# Ed-PhD-Copilot-Skills — standard project checks
# Usage: make check   (equivalent to python3 scripts/check_skill_structure.py)

.PHONY: check

check:
	python3 scripts/check_skill_structure.py
