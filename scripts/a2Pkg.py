import gzip
import sys
import json
from collections import defaultdict

path = '/da0_data/play/PYthruMaps/c2bPtaPkgQPY.'

a2Pkg = defaultdict(lambda: defaultdict(lambda: defaultdict(int)))
standard_libs = ['EasyDialogs', 'lib2to3', 'timeit', 'asyncore', 'SimpleHTTPServer', 'fcntl', 'ic', 'getopt', 'grp', 'calendar', 'winsound', 'string', '__future__', 'Tix', 'exceptions', 'threading', 'SUNAUDIODEV', 'crypt', 'Carbon', 'typing', 'mimify', 'tokenize', 'venv', 'cmath', 'socketserver', 'dircache', 'shlex', 'readline', 'msilib', 'UserList', 'tempfile', 'traceback', 'mmap', 'chunk', 'cPickle', 'dummy_thread', 'sunaudiodev', 'macresource', 'textwrap', 'robotparser', 'html', 'tarfile', 'locale', 'fm', 'doctest', 'ftplib', 'pkgutil', 'bsddb', 'asyncio', 'UserDict', 'rfc822', 'difflib', 'zipimport', 'statistics', 'zlib', 'mimetypes', 'builtins', 'termios', 'pathlib', 'cd', 'dis', 'macostools', 'Cookie', 'os', 'marshal', 'fpectl', 'rexec', 'al', 'SocketServer', 'dbhash', 'zipfile', 'mailcap', 'faulthandler', 'spwd', 'turtle', 'future_builtins', 'parser', 'Queue', 'modulefinder', 'warnings', 'xdrlib', 'BaseHTTPServer', 'shelve', 'reprlib', 'dataclasses', 'thread', 'sysconfig', 'gzip', 'copyreg', 'smtpd', 'ConfigParser', 'imageop', 'secrets', 'cStringIO', 'contextlib', 'signal', 'DocXMLRPCServer', 'W', 'syslog', 'sha', 'platform', 'pstats', 'FrameWork', 'runpy', 'PixMapWrapper', '_thread', 'copy', 'aepack', '_dummy_thread', 'enum', 'unittest', 'MimeWriter', 'user', 'ast', 'array', 'stringprep', 'ensurepip', 'tracemalloc', 'cgi', 'ttk', 'fractions', 'formatter', 'icopen', 'subprocess', 'test', 'md5', 'distutils', 'ipaddress', 're', 'SimpleXMLRPCServer', 'imp', 'collections', 'optparse', 'flp', 'cProfile', 'trace', 'MacOS', '__builtin__', 'statvfs', 'encodings', 'importlib', 'shutil', 'ScrolledText', 'json', 'sets', 'curses', 'UserString', 'multifile', 'cookielib', 'fpformat', 'colorsys', 'hotshot', 'aetypes', 'audioop', 'pyclbr', 'atexit', 'py_compile', 'ossaudiodev', 'copy_reg', 'xmlrpc', 'hmac', 'logging', 'StringIO', 'msvcrt', 'fnmatch', 'numbers', 'http', 'binascii', 'dbm', 'pdb', 'operator', 'macpath', 'plistlib', '_winreg', 'dummy_threading', 'webbrowser', 'pprint', 'sunau', 'bdb', 'mimetools', 'select', 'httplib', 'functools', 'cfmfile', 'symbol', 'profile', 'urllib2', 'sgmllib', 'filecmp', 'hashlib', 'dumbdbm', 'fileinput', 'binhex', 'resource', 'posixfile', 'rlcompleter', 'zipapp', 'telnetlib', 'symtable', 'findertools', 'new', 'imaplib', 'datetime', 'MiniAEFrame', 'cgitb', 'smtplib', 'socket', 'sqlite3', 'stat', 'aifc', 'argparse', 'cmd', 'turtledemo', 'tabnanny', 'videoreader', 'inspect', 'FL', 'popen2', 'asynchat', 'HTMLParser', 'unicodedata', 'macerrors', 'pickle', 'compiler', 'htmllib', 'xml', 'applesingle', 'DEVICE', 'errno', 'urlparse', 'gdbm', 'gensuitemodule', 'ctypes', 'dl', 'Bastion', 'buildtools', 'tty', 'multiprocessing', 'struct', 'uuid', 'code', 'mutex', 'posix', 'concurrent', 'urllib', 'xmlrpclib', '__main__', 'getpass', 'glob', 'email', 'whichdb', 'AL', 'autoGIL', 'token', 'nntplib', 'lzma', 'io', 'fl', 'mhlib', 'gettext', 'codecs', 'ssl', 'pickletools', 'abc', 'selectors', 'commands', 'bisect', 'configparser', 'contextvars', 'heapq', 'imgfile', 'aetools', 'Nav', 'ColorPicker', 'pydoc', 'codeop', 'linecache', 'htmlentitydefs', 'queue', 'anydbm', 'quopri', 'GL', 'netrc', 'gc', 'CGIHTTPServer', 'itertools', 'base64', 'random', 'imputil', 'time', 'mailbox', 'tkinter', 'Tkinter', 'sys', 'winreg', 'site', 'imghdr', 'pwd', 'keyword', 'decimal', 'jpeg', 'nis', 'sched', 'pipes', 'types', 'math', 'bz2', 'weakref', 'wsgiref', 'gl', 'uu', 'poplib', 'wave', 'pty', 'compileall', 'csv', 'sndhdr']

for i in range(32):
    print("Reading gz file number " + str(i))
    file = gzip.open(path + str(i) + ".gz")
    for line in file.readlines():
        entry = line.strip('\n').split(';')
        repo, author = entry[1], entry[3]
        modules = entry[5:]
        for m in modules:
            m = m.split('.')[0]
            if m not in standard_libs:
                a2Pkg[author][m][repo] = a2Pkg[author][m][repo] + 1
    file.close()
a2Pkg = dict(a2Pkg)
with open('layer1.json', 'w') as f:
    json.dump(a2Pkg, f, ensure_ascii=False)

a2Pkg_count = defaultdict(lambda: defaultdict(int))
for k1, v1 in a2Pkg.items():
    for k2, v2 in v1.items():
        a2Pkg_count[k1][k2] = len(v2)
    a2Pkg_count[k1] = sorted(a2Pkg_count[k1].items(), key=lambda item: item[1], reverse=True)[:10]

with open('a2PkgTop10', 'w') as f:
    for k, v in a2Pkg_count.items():
        line = k
        for pkg, cnt in v:
            line = line + ';' + pkg
        f.write(line + '\n')
