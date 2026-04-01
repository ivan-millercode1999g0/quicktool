#!/usr/bin/env python3
"""Ghost tool."""
import argparse
import logging
import sys

log = logging.getLogger(__name__)

class Quicktool:
 def __init__(self, config_path: str = "config.yaml"):
 self.config = self._load_config(config_path)
 log.info("quicktool initialized")

 def _load_config(self, path: str) -> dict:
 import yaml, os
 if not os.path.exists(path):
 return {"verbose": False}
 with open(path) as f:
 return yaml.safe_load(f) or {}

 def run(self) -> int:
 log.info("quicktool running...")
 return 0

def main():
 parser = argparse.ArgumentParser(description=__doc__)
 parser.add_argument("-c", "--config", default="config.yaml")
 parser.add_argument("-v", "--verbose", action="store_true")
 args = parser.parse_args()
 logging.basicConfig(
 level=logging.DEBUG if args.verbose else logging.INFO,
 format="%(asctime)s [%(levelname)s] %(message)s",
 )
 sys.exit(Quicktool(args.config).run())

if __name__ == "__main__":
 main()
