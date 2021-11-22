import sys
import subprocess
import pkg_resources

required = {
    'Flask', 
    'flask-cors',
    'numpy',
    'pandas',
    'SQLAlchemy',
    'psycopg2',
    }

installed = {pkg.key for pkg in pkg_resources.working_set}
missing = required - installed

print('verificando dependencias e instalando se necessário...aguarde.')

if missing:
    python = sys.executable
    subprocess.check_call([python, '-m', 'pip', 'install', *missing], stdout=subprocess.DEVNULL)
