import venv
import subprocess
from shutil import rmtree

venv.create('venv', with_pip=True)
subprocess.run(['./venv/bin/pip', 'install', 'pyfiglet'], capture_output=True)
subprocess.run(['./venv/bin/python3', '-m', 'figdate', '%Y %d %b, %A', 'graceful'])
rmtree('venv')
