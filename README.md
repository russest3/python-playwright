# python-playwright
- Versions used in training
    - Playwright 1.46
    - Python 3.12

Very important to use a Virtual Environment!

<pre>srussel0@development:~/repos/python-playwright$ source .venv/local/bin/activate
pip install pytest-playwright
playwright install
</pre>

Run playwright scripts using pytest:

<pre>pytest .\demo.py</pre>

pytest.ini file for configuration:
<pre>
[pytest]
markers = 
    smoke: part of the smoke test suite
addopts = --headed --browser chromium --browser firefox --screenshot only-on-failure --numprocesses auto
</pre>

Error running playwright install:
<pre>
║ Host system is missing dependencies to run browsers. ║
║ Missing libraries:                                   ║
║     libgstcodecparsers-1.0.so.0                      ║
║     libavif.so.13 
</pre>







