# prophet-wrapper

Please refer to [https://randyphoa.com/deploying-prophet-model-with-custom-environments-on-ibm-watson-machine-learning-46dfb4d8a2ac](https://randyphoa.com/deploying-prophet-model-with-custom-environments-on-ibm-watson-machine-learning-46dfb4d8a2ac) for an updated approach.

python -m pip install --upgrade build
python -m pip install --upgrade twine

python -m build
python -m twine upload dist/*
