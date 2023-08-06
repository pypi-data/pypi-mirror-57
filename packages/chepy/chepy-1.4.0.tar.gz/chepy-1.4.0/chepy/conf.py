import sys
import importlib
import inspect
import pkgutil
import json
from pathlib import Path
from configparser import ConfigParser


class Config(object):
    def __init__(self):
        home = Path.home()
        self.chepy_dir = Path(home / ".chepy")
        self.chepy_conf = Path(self.chepy_dir / "chepy.conf")

        if not self.chepy_dir.exists():
            self.chepy_dir.mkdir()
            c = ConfigParser()
            c["Plugin"] = {"PluginPath": "None"}
            c["Cli"] = {"HistoryPath": str(self.chepy_dir / "chepy_history")}
            Path(str(self.chepy_dir / "chepy_history")).touch()
            if not self.chepy_conf.exists():
                with open(str(self.chepy_conf), "w") as f:
                    c.write(f)

        self.config = ConfigParser()
        self.config.read(str(self.chepy_conf))

        self.plugin_path = self.config["Plugin"]["PluginPath"]

        self.history_path = self.config["Cli"]["HistoryPath"]

    def load_plugins(self):
        plugins = []
        if self.plugin_path != "None":
            sys.path.append(self.plugin_path)

            my_plugins = [
                importlib.import_module(name)
                for finder, name, ispkg in pkgutil.iter_modules()
                if name.startswith("chepy_")
            ]

            for plugin in my_plugins:
                klass, mod = inspect.getmembers(plugin, inspect.isclass)[0]
                loaded = getattr(plugin, klass)
                plugins.append(loaded)
        return plugins
