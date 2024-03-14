import os
from dotenv import load_dotenv

load_dotenv()

from .base import *

if os.getenv("PROD", "false") in ["True", "true"]:
    from .prod import *
else:
    from .dev import *
