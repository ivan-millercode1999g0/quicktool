import hashlib
import time
import logging

log = logging.getLogger(__name__)

def file_hash(path: str) -> str:
 h = hashlib.sha256()
 with open(path, "rb") as f:
 for c in iter(lambda: f.read(8192), b""):
 h.update(c)
 return h.hexdigest()
