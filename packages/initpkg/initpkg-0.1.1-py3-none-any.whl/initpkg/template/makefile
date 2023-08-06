setup:
	if exist build rmdir /S /Q build
	if exist dist rmdir /S /Q dist
	python setup.py bdist_wheel
install:
	pip uninstall <your_pkg> -y
	pip install --find-links=dist  --no-cache-dir <your_pkg>==<your_version>

test:
	pytest tests

publish:
	git tag v0.0.1
	git push origin v0.0.1
	twine upload dist/*