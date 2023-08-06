import os, sys, argparse
from getpass import getpass, getuser
from types import GeneratorType
from . import __name__ as pkgname, __version__ as pkgversion


class EncapsAction(argparse.Action):
    def __init__(self, option_strings, dest, nargs=None, **kwargs):
        if nargs is not argparse.REMAINDER:
            raise ValueError("nargs must et REMAINDER")
        super(EncapsAction, self).__init__(
            option_strings, dest, nargs, **kwargs)

    def __call__(self, parser, namespace, values, option_string=None):
        setattr(namespace, self.dest, parser.parse_args(values))


class ExtendAction(argparse.Action):
    def __init__(self, option_strings, dest, nargs=None, **kwargs):
        if nargs not in "+*":
            raise ValueError("nargs must be + or *")
        super(ExtendAction, self).__init__(
            option_strings, dest, nargs, **kwargs)

    def __call__(self, parser, namespace, values, option_string=None):
        """We need exactly conatenate values instead of use list().extend() method because it lead sum of values from all level of recursion. See EnacapsAction in tunnel option.)"""
        da = getattr(namespace, self.dest, [])
        setattr(namespace, self.dest, da + values)


class PresetAction(argparse.Action):
    def __init__(self, option_strings, dest, nargs=None, cfgobj=None,
                 **kwargs):
        if cfgobj is None:
            raise AssertionError("You schould set preset_store kw-argument")
        if nargs not in "?+*":
            raise ValueError("nargs must be + or *")
        self.cfgobj = cfgobj
        super(PresetAction, self).__init__(option_strings, dest,
                                           nargs, **kwargs)

    def __call__(self, parser, namespace, values, option_string=None):
        if not namespace.config_file:
            exit("Missing -f/--config-file option or {} option set before -f/--config-file".format(option_string))
        da = getattr(namespace, self.dest, [])
        setattr(namespace, self.dest,
                da + [v for k,v in self.SCRIPTS.items() if k in values])

class ReadConfAction(argparse.Action):
    def __init__(self, option_strings, dest, nargs=None, cfgobj=None, **kwargs):
        if cfgobj is None:
            raise AssertionError("You schould set cfgobj kw-argument")
        if not isinstance(kwargs["type"], argparse.FileType):
            raise ValueError(
                "ReadConfAction aplicable only with argument type=FileType"
            )
        self.cfgobj = cfgobj
        super(ReadConfAction,self).__init__(option_strings, dest, nargs, **kwargs)

    def __call__(self, parser, namespace, conf_file, option_string=None):
        print("Parsing config", file=sys.stderr)
        if namespace is self.cfgjobj.settings and len(namespace.__dict__) > 0:
            exit("Option {} if set, must be first option in command line.".format(option_string))
#        if self.cfgobj.CONF: return
        self.cfgobj.read_config_file(conf_file)


class GetPassAction(argparse.Action):
    def __init__(self, option_strings, dest, nargs=None, **kwargs):
        self.dest = dest
        super(GetPassAction, self).__init__(option_strings, dest, nargs, **kwargs)

    def __call__(self, parser, namespace, value, option_string=None):
        if value == "-":
            try:
                setattr(namespace, getpass("Password: "))
            except (EOFError, KeyboardInterrupt):
                exit('')
        else: setattr(namespace, value)

class Configurator(object):
    """Class collecting and representing set of options
from command-line and config file"""

    settings = argparse.Namespace()
    HOSTS = {}
    SCRIPTS = {}
    CONF = {}
    params = argparse.ArgumentParser(prog=pkgname,
                                     description="Run commands through list of hosts and collect results asynchronously")
    gp = params.add_argument_group("global", "Global parameters, schould be set before main parameters.")
    mp = params.add_argument_group("main", "Main parameters")

    def __init__(self, *args, **kwargs):
        self.gp.add_argument('-f', "--config-file", nargs="?",
                             type=argparse.FileType("r", encoding="UTF-8"),
                             action=ReadConfAction,
                             cfgobj=self,
                             default=sys.stdin,
                             help="Path to config file to get values from.")
        self.gp.add_argument('-D', "--debug", action="count", default=0,
                             help="Debug level")
        self.gp.add_argument('-F', "--output-format", default="pythonic",
                             choices=["asis", "csv", "pythonic"],
                             help="Sets output format. Default: pythonic")
        self.gp.add_argument('-o', "--output", nargs="?",
                             type=argparse.FileType('w', encoding="UTF-8"),
                             default=sys.stdout)
        self.gp.add_argument("--version", action="version",
                             version='-'.join((pkgname, pkgversion)))

    
        self.mp.add_argument('-S', "--scripts", nargs='+', metavar='ScriptName',
                             action=PresetAction,
                             cfgobj=self,
                             dest="commands",
                             # choices=settings.SCRIPTS,
                             default=[],
                             help="Script preset name (from config file) to execute on remote host")
        self.mp.add_argument('-c', "--commands", metavar="CMD", nargs='+',
                             action=ExtendAction,
                             default=[],
                             help="Command to execute on remote host")
        self.mp.add_argument('-d', "--downloads", nargs='+', metavar="DL",
                             default=[],
                             help="List of absolute paths to download from remote hosts.")
        self.mp.add_argument("--download-dir", nargs='?', default="/tmp",
                             help="Root directory for downloading files from remote hosts. Actual files will be put in per host subdirectories of that directory.")
        self.mp.add_argument('-H', "--hosts-presets", type=str, nargs="+",
                             metavar="HostsPreset",
                             action=PresetAction,
                             cfgobj=self,
                             dest="hosts",
                             # choices=self.HOSTS.keys(),
                             default=[],
                             help="List of target hosts by preset name")
        self.mp.add_argument("--hosts", nargs="+", metavar='host', default=[],
                             action=ExtendAction,
                             help="List of target hosts by hostname")
        self.mp.add_argument('-i', "--privkey", metavar="PK", nargs='+',
                             default=[os.path.expanduser("~/.ssh/id_rsa")],
                             help="Path to SSH private key to use for connetions. It is possible to set several keys.")
        self.mp.add_argument('-L', "--limit", type=int, default=0, metavar='N',
                             help="Sets number of workers. Missing option or 0 means unlimited.")
        self.mp.add_argument('-p', "--port", type=int, default=22, metavar='P',
                             help="Port to connecto to SSH on remote host.")
        self.mp.add_argument('-P', "--password", nargs='?', const="-",
#                             action=GetPassAction,
                             help="Password for remote ssh connections. If special value \"-\" used, password will be prompted from stdandard input.")
        self.mp.add_argument('-t', "--timeout", type=float, nargs="?",
                             default=5,
                             help="Connection timeout.")
        self.mp.add_argument('-T', "--tunnel",
                             nargs=argparse.REMAINDER,
                             action=EncapsAction,
                             help="Open tunnel through connections described before option for connections described after this option. Multiple use of option (with multiple blocks of hosts obviously) allowed.")
        self.mp.add_argument('-U', "--username", nargs='?', default=getuser(),
                             help="Username to use for login to remote hosts. By defautl username of calling user.")
        self.mp.add_argument('-u', "--uploads", nargs='+', metavar="UL",
                             default=[], help="List of files to upload.")
        self.mp.add_argument("--upload-dir", nargs='?', default="/tmp",
                             help="Path on remote host to upload selected files")
        # Set defaults
        self.params.parse_args([], self.settings)


    def configure(self):
        """Parse arguments from command-line and config-file."""
        self.read_conf_file(sys.stdin)
        self.params.parse_args(namespace=self.settings)
        if self.CONF["password"] == "-":
            try:
                self.CONF["password"] = getpass("Password: ")
            except (EOFError, KeyboardInterrupt):
                exit('')
#        self.settings.__dict__.update(
#            {k:v for k,v in cmdline_arguments.__dict__.items()
#             if not self.params.get_default(k) == v})


    def _iter_concat(self, *args):
#        GeneratorType = type((i for i in (1,)))
        for x in args:
            if type(x) is str: yield x
            elif type(x) in (list, tuple, GeneratorType):
                for y in x: yield y
            else: raise TypeError


    def read_conf_file(self, conffile):
        conf = conffile.read().strip()
        if not conf: return
        gns = {
            "__builtins__": {
                k:v
                for k,v in (
                        __builtins__.__dict__ if __name__ == "__main__"
                        else __builtins__
                ).items()
                if k not in ("compile",
                             "open",
                             "exec",
                             "eval",
                             "quit",
                             "exit")}
        }
        try:
            d=eval("{{{}\n}}".format(conf, gns))
            self.SCRIPTS.update(d.pop("SCRIPTS", {}))
            self.HOSTS.update(d.pop("HOSTS", {}))
            self.CONF.update(
                {k:v for k,v in d.items() if k in self.settings.__dict__}
            )
            print(self.CONF, sep='\n', file=sys.stderr)
        except Exception as e:
            print("Configuration file", config_file_path, "is wrong formated", e)
