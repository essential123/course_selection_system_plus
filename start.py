import sys
from conf import settings
sys.path.append(settings.BASE_DIR)

if __name__ == '__main__':
    from core import src
    src.run()