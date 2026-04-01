import yaml
import os

DEFAULT = {"verbose": False, "output_dir": "./output"}

def load_config(path="config.yaml"):
 if not os.path.exists(path):
 with open(path, "w") as f:
 yaml.dump(DEFAULT, f)
 return dict(DEFAULT)
 with open(path) as f:
 return {**DEFAULT, **(yaml.safe_load(f) or {})}
