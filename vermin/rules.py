# Module requirements: name -> min version per major or None if N.A.
MOD_REQS = {
  "ConfigParser": (2.0, None),
  "DocXMLRPCServer": (2.3, None),
  "HTMLParser": (2.2, None),
  "Queue": (2.0, None),
  "SimpleXMLRPCServer": (2.2, None),
  "SocketServer": (2.0, None),
  "Tkinter": (2.0, None),
  "__builtin__": (2.0, None),
  "__future__": (2.1, 3.0),
  "_dummy_thread": (None, 3.0),
  "_markupbase": (None, 3.0),
  "_winreg": (2.0, None),
  "abc": (2.6, 3.0),
  "argparse": (2.7, 3.2),
  "ast": (2.6, 3.0),
  "asyncio": (None, 3.4),
  "atexit": (2.0, 3.0),
  "builtins": (None, 3.0),
  "bz2": (2.3, 3.0),
  "cProfile": (2.5, 3.0),
  "cgitb": (2.2, 3.0),
  "collections": (2.4, 3.0),
  "configparser": (None, 3.0),
  "contextlib": (2.5, 3.0),
  "contextvars": (None, 3.7),
  "cookielib": (2.4, None),
  "copy_reg": (2.0, None),
  "copyreg": (None, 3.0),
  "csv": (2.3, 3.0),
  "ctypes": (2.5, 3.0),
  "dataclasses": (None, 3.7),
  "datetime": (2.3, 3.0),
  "dbm.io": (None, 3.0),
  "dbm.ndbm": (None, 3.0),
  "dbm.os": (None, 3.0),
  "dbm.struct": (None, 3.0),
  "dbm.sys": (None, 3.0),
  "dbm.whichdb": (None, 3.0),
  "decimal": (2.4, 3.0),
  "difflib": (2.1, 3.0),
  "dummy_thread": (2.3, None),
  "dummy_threading": (2.3, None),
  "email": (2.2, 3.0),
  "email.charset": (2.2, 3.0),
  "email.contentmanager": (None, 3.6),
  "email.header": (2.2, 3.0),
  "email.headerregistry": (None, 3.6),
  "email.policy": (None, 3.3),
  "faulthandler": (None, 3.3),
  "fractions": (2.6, 3.0),
  "functools": (2.5, 3.0),
  "future_builtins": (2.6, None),
  "hashlib": (2.5, 3.0),
  "heapq": (2.3, 3.0),
  "hmac": (2.2, 3.0),
  "hotshot": (2.2, None),
  "html": (None, 3.0),
  "htmlentitydefs": (2.0, None),
  "http": (None, 3.0),
  "http.cookiejar": (None, 3.0),
  "importlib": (2.7, 3.1),
  "importlib.resources": (None, 3.7),
  "inspect": (2.1, 3.0),
  "io": (2.6, 3.0),
  "ipaddress": (None, 3.3),
  "itertools": (2.3, 3.0),
  "json": (2.6, 3.0),
  "logging": (2.3, 3.0),
  "lzma": (None, 3.3),
  "markupbase": (2.0, None),
  "md5": (2.0, None),
  "modulefinder": (2.3, 3.0),
  "msilib": (2.5, 3.0),
  "multiprocessing": (2.6, 3.0),
  "new": (2.0, None),
  "numbers": (2.6, 3.0),
  "optparse": (2.3, 3.0),
  "ossaudiodev": (2.3, 3.0),
  "pathlib": (None, 3.4),
  "pickletools": (2.3, 3.0),
  "pkgutil": (2.3, 3.0),
  "platform": (2.3, 3.0),
  "pydoc": (2.1, 3.0),
  "queue": (None, 3.0),
  "repr": (2.0, None),
  "reprlib": (None, 3.0),
  "runpy": (2.5, 3.0),
  "secrets": (None, 3.6),
  "sets": (2.3, None),
  "shlex": (2.0, 3.0),
  "socketserver": (None, 3.0),
  "spwd": (2.5, 3.0),
  "sqlite3": (2.5, 3.0),
  "ssl": (2.6, 3.0),
  "string.letters": (2.0, None),
  "string.lowercase": (2.0, None),
  "string.uppercase": (2.0, None),
  "stringprep": (2.3, 3.0),
  "subprocess": (2.4, 3.0),
  "sysconfig": (2.7, 3.2),
  "tarfile": (2.3, 3.0),
  "textwrap": (2.3, 3.0),
  "timeit": (2.3, 3.0),
  "tkinter": (None, 3.0),
  "tracemalloc": (None, 3.4),
  "typing": (None, 3.5),
  "unittest": (2.1, 3.0),
  "unittest.mock": (None, 3.3),
  "urllib2": (2.0, None),
  "uuid": (2.5, 3.0),
  "venv": (None, 3.3),
  "warnings": (2.1, 3.0),
  "weakref": (2.1, 3.0),
  "winreg": (None, 3.0),
  "wsgiref": (2.5, 3.0),
  "xmlrpc": (None, 3.0),
  "xmlrpc.client": (None, 3.0),
  "xmlrpc.server": (None, 3.0),
  "xmlrpclib": (2.2, None),
  "zipimport": (2.3, 3.0),
}

# Module member requirements: member -> (module, requirements)
MOD_MEM_REQS = {
  # Builtin classes
  "bool": (2.2, 3.0),
  "bytearray": (2.6, 3.0),
  "frozenset": (2.4, 3.0),
  "object": (2.2, 3.0),
  "set": (2.4, 3.0),
  "type": (2.2, 3.0),

  # Classes
  "SimpleXMLRPCServer.CGIXMLRPCRequestHandler": (2.3, None),
  "abc.ABC": (None, 3.4),
  "collections.Counter": (2.7, 3.1),
  "collections.OrderedDict": (2.7, 3.1),
  "collections.UserDict": (None, 3.0),
  "collections.UserList": (None, 3.0),
  "collections.UserString": (None, 3.0),
  "collections.defaultdict": (2.5, 3.0),
  "collections.deque": (2.4, 3.0),
  "collections.namedtuple": (2.6, 3.0),
  "contextlib.AbstractContextManager": (None, 3.6),
  "contextlib.ContextDecorator": (None, 3.2),
  "contextlib.ExitStack": (None, 3.3),
  "csv.unix_dialect": (None, 3.2),
  "ctypes.c_bool": (2.6, 3.0),
  "ctypes.c_longdouble": (2.6, 3.0),
  "ctypes.c_ssize_t": (2.7, 3.2),
  "datetime.timezone": (None, 3.2),
  "difflib.HtmlDiff": (2.4, 3.0),
  "email.generator.BytesGenerator": (None, 3.2),
  "email.generator.DecodedGenerator": (2.2, 3.0),
  "email.mime.application.MIMEApplication": (2.5, 3.0),
  "email.mime.multipart.MIMEMultipart": (2.2, 3.0),
  "email.mime.nonmultipart.MIMENonMultipart": (2.2, 3.0),
  "email.parser.BytesFeedParser": (None, 3.2),
  "email.parser.BytesHeaderParser": (None, 3.3),
  "email.parser.BytesParser": (None, 3.2),
  "email.parser.FeedParser": (2.4, 3.0),
  "email.policy.EmailPolicy": (None, 3.6),
  "importlib.machinery.ExtensionFileLoader": (None, 3.3),
  "importlib.machinery.FileFinder": (None, 3.3),
  "importlib.machinery.ModuleSpec": (None, 3.4),
  "importlib.machinery.SourceFileLoader": (None, 3.3),
  "importlib.machinery.SourcelessFileLoader": (None, 3.3),
  "importlib.machinery.WindowsRegistryFinder": (None, 3.3),
  "importlib.util.LazyLoader": (None, 3.5),
  "inspect.BoundArguments": (None, 3.3),
  "inspect.Parameter": (None, 3.3),
  "inspect.Signature": (None, 3.3),
  "json.JSONDecodeError": (None, 3.5),
  "logging.LoggerAdapter": (2.6, 3.0),
  "multiprocessing.Barrier": (None, 3.3),
  "os.PathLike": (None, 3.6),
  "os.terminal_size": (None, 3.3),
  "pkgutil.ModuleInfo": (None, 3.6),
  "ssl.SSLContext": (2.7, 3.2),
  "ssl.SSLMemoryBIO": (None, 3.6),
  "ssl.SSLObject": (None, 3.6),
  "ssl.SSLSession": (None, 3.6),
  "subprocess.CompletedProcess": (None, 3.5),
  "tracemalloc.DomainFilter": (None, 3.6),
  "typing.AsyncGenerator": (None, 3.6),
  "typing.ChainMap": (None, 3.6),
  "typing.ClassVar": (None, 3.5),
  "typing.Collection": (None, 3.6),
  "typing.ContextManager": (None, 3.6),
  "typing.Counter": (None, 3.6),
  "typing.Deque": (None, 3.6),
  "typing.Text": (None, 3.6),
  "unittest.TextTestResult": (2.7, 3.0),
  "warnings.catch_warnings": (2.6, 3.0),
  "weakref.WeakMethod": (None, 3.4),
  "weakref.WeakSet": (2.7, 3.0),
  "weakref.finalize": (None, 3.4),
  "wsgiref.handlers.IISCGIHandler": (None, 3.2),
  "xml.etree.ElementTree": (2.5, 3.0),
  "xml.etree.ElementTree.XMLPullParser": (None, 3.4),
  "xmlrpclib.MultiCall": (2.4, None),

  # Exceptions
  "email.errors.CloseBoundaryNotFoundDefect": (None, 3.3),
  "email.errors.FirstHeaderLineIsContinuationDefect": (2.4, 3.0),
  "email.errors.MalformedHeaderDefect": (2.4, 3.0),
  "email.errors.MisplacedEnvelopeHeaderDefect": (2.4, 3.0),
  "email.errors.MissingHeaderBodySeparatorDefect": (None, 3.3),
  "email.errors.MultipartInvariantViolationDefect": (2.4, 3.0),
  "email.errors.NoBoundaryInMultipartDefect": (2.4, 3.0),
  "email.errors.StartBoundaryNotFoundDefect": (2.4, 3.0),
  "ssl.SSLEOFError": (2.7, 3.3),
  "ssl.SSLSyscallError": (2.7, 3.3),
  "ssl.SSLWantReadError": (2.7, 3.3),
  "ssl.SSLWantWriteError": (2.7, 3.3),
  "ssl.SSLZeroReturnError": (2.7, 3.3),
  "subprocess.SubprocessError": (None, 3.3),
  "subprocess.TimeoutExpired": (None, 3.3),
  "tarfile.HeaderError": (2.6, 3.0),
  "zipfile.BadZipFile": (None, 3.2),

  # Builtin functions
  "all": (2.5, 3.0),
  "any": (2.5, 3.0),
  "basestring": (2.3, 3.0),
  "bin": (2.6, 3.0),
  "breakpoint": (None, 3.7),
  "classmethod": (2.2, 3.0),
  "enumerate": (2.3, 3.0),
  "file": (2.2, 3.0),
  "format": (2.6, 3.0),
  "help": (2.2, 3.0),
  "iter": (2.2, 3.0),
  "next": (2.6, 3.0),
  "reversed": (2.4, 3.0),
  "sorted": (2.4, 3.0),
  "staticmethod": (2.2, 3.0),
  "sum": (2.3, 3.0),
  "super": (2.2, 3.0),
  "unichr": (2.0, 3.0),
  "unicode": (2.0, 3.0),
  "zip": (2.0, 3.0),

  # Functions
  "SimpleXMLRPCServer.SimpleXMLRPCServer.register_introspection_functions": (2.3, None),
  "Tkinter.Tcl": (2.4, None),
  "bz2.BZ2File.fileno": (None, 3.3),
  "bz2.BZ2File.peek": (None, 3.3),
  "bz2.BZ2File.read1": (None, 3.3),
  "bz2.BZ2File.readable": (None, 3.3),
  "bz2.BZ2File.readinto": (None, 3.3),
  "bz2.BZ2File.seekable": (None, 3.3),
  "bz2.BZ2File.writable": (None, 3.3),
  "bz2.open": (None, 3.3),
  "collections.OrderedDict.move_to_end": (None, 3.2),
  "collections.deque.copy": (None, 3.5),
  "collections.deque.count": (2.7, 3.2),
  "collections.deque.index": (None, 3.5),
  "collections.deque.insert": (None, 3.5),
  "collections.deque.remove": (2.5, 3.0),
  "collections.deque.reverse": (2.7, 3.2),
  "contextlib.redirect_stderr": (None, 3.5),
  "contextlib.redirect_stdout": (None, 3.4),
  "contextlib.suppress": (None, 3.4),
  "crypt.mksalt": (None, 3.3),
  "csv.field_size_limit": (2.5, 3.0),
  "ctypes._CData.from_buffer": (2.6, 3.0),
  "ctypes._CData.from_buffer_copy": (2.6, 3.0),
  "ctypes.get_errno": (2.6, 3.0),
  "ctypes.get_last_error": (2.6, 3.0),
  "ctypes.set_errno": (2.6, 3.0),
  "ctypes.set_last_error": (2.6, 3.0),
  "ctypes.util.find_msvcrt": (2.6, 3.0),
  "datetime.datetime.timestamp": (None, 3.3),
  "datetime.timedelta.total_seconds": (None, 3.2),
  "decimal.Context.clear_traps": (None, 3.3),
  "decimal.Context.create_decimal_from_float": (2.7, 3.1),
  "decimal.Decimal.as_integer_ratio": (None, 3.6),
  "decimal.Decimal.canonical": (2.6, 3.0),
  "decimal.Decimal.compare_signal": (2.6, 3.0),
  "decimal.Decimal.compare_total": (2.6, 3.0),
  "decimal.Decimal.compare_total_mag": (2.6, 3.0),
  "decimal.Decimal.conjugate": (2.6, 3.0),
  "decimal.Decimal.copy_abs": (2.6, 3.0),
  "decimal.Decimal.copy_negate": (2.6, 3.0),
  "decimal.Decimal.copy_sign": (2.6, 3.0),
  "decimal.Decimal.exp": (2.6, 3.0),
  "decimal.Decimal.fma": (2.6, 3.0),
  "decimal.Decimal.from_float": (2.7, 3.1),
  "decimal.Decimal.is_canonical": (2.6, 3.0),
  "decimal.Decimal.is_finite": (2.6, 3.0),
  "decimal.Decimal.is_infinite": (2.6, 3.0),
  "decimal.Decimal.is_nan": (2.6, 3.0),
  "decimal.Decimal.is_normal": (2.6, 3.0),
  "decimal.Decimal.is_qnan": (2.6, 3.0),
  "decimal.Decimal.is_signed": (2.6, 3.0),
  "decimal.Decimal.is_snan": (2.6, 3.0),
  "decimal.Decimal.is_subnormal": (2.6, 3.0),
  "decimal.Decimal.is_zero": (2.6, 3.0),
  "decimal.Decimal.ln": (2.6, 3.0),
  "decimal.Decimal.log10": (2.6, 3.0),
  "decimal.Decimal.logb": (2.6, 3.0),
  "decimal.Decimal.logical_and": (2.6, 3.0),
  "decimal.Decimal.logical_invert": (2.6, 3.0),
  "decimal.Decimal.logical_or": (2.6, 3.0),
  "decimal.Decimal.logical_xor": (2.6, 3.0),
  "decimal.Decimal.max_mag": (2.6, 3.0),
  "decimal.Decimal.min_mag": (2.6, 3.0),
  "decimal.Decimal.next_minus": (2.6, 3.0),
  "decimal.Decimal.next_plus": (2.6, 3.0),
  "decimal.Decimal.next_toward": (2.6, 3.0),
  "decimal.Decimal.number_class": (2.6, 3.0),
  "decimal.Decimal.radix": (2.6, 3.0),
  "decimal.Decimal.rotate": (2.6, 3.0),
  "decimal.Decimal.scaleb": (2.6, 3.0),
  "decimal.Decimal.shift": (2.6, 3.0),
  "decimal.Decimal.to_integral_exact": (2.6, 3.0),
  "decimal.Decimal.to_integral_value": (2.6, 3.0),
  "decimal.localcontext": (2.5, 3.0),
  "difflib.SequenceMatcher.get_grouped_opcodes": (2.3, 3.0),
  "difflib.context_diff": (2.3, 3.0),
  "difflib.diff_bytes": (None, 3.5),
  "difflib.unified_diff": (2.3, 3.0),
  "email.utils.format_datetime": (None, 3.3),
  "email.utils.formatdate": (2.4, 3.0),
  "email.utils.localtime": (None, 3.3),
  "email.utils.parsedate_to_datetime": (None, 3.3),
  "functools.cmp_to_key": (2.7, 3.2),
  "functools.lru_cache": (None, 3.2),
  "functools.partial_method": (None, 3.4),
  "functools.reduce": (2.6, 3.0),
  "functools.total_ordering": (2.7, 3.2),
  "hashlib.pbkdf2_hmac": (2.7, 3.4),
  "hashlib.scrypt": (None, 3.6),
  "heapq.heappushpop": (2.6, 3.0),
  "heapq.merge": (2.6, 3.0),
  "heapq.nlargest": (2.4, 3.0),
  "heapq.nsmallest": (2.4, 3.0),
  "hmac.compare_digest": (2.7, 3.3),
  "hmac.digest": (None, 3.7),
  "importlib.machinery.ExtensionFileLoader.create_module": (None, 3.5),
  "importlib.machinery.ExtensionFileLoader.exec_module": (None, 3.5),
  "importlib.machinery.ExtensionFileLoader.get_filename": (None, 3.4),
  "importlib.machinery.FileFinder.find_spec": (None, 3.4),
  "importlib.machinery.PathFinder.find_spec": (None, 3.4),
  "importlib.machinery.all_suffixes": (None, 3.3),
  "importlib.util.cache_from_source": (None, 3.4),
  "importlib.util.decode_source": (None, 3.4),
  "importlib.util.find_spec": (None, 3.4),
  "importlib.util.module_from_spec": (None, 3.5),
  "importlib.util.resolve_name": (None, 3.3),
  "importlib.util.source_from_cache": (None, 3.4),
  "importlib.util.source_hash": (None, 3.7),
  "importlib.util.spec_from_file_location": (None, 3.4),
  "importlib.util.spec_from_loader": (None, 3.4),
  "inspect.BoundArguments.apply_defaults": (None, 3.6),
  "inspect.cleandoc": (2.6, 3.0),
  "inspect.getattr_static": (None, 3.2),
  "inspect.getcallargs": (2.7, 3.2),
  "inspect.getclosurevars": (None, 3.3),
  "inspect.getcoroutinelocals": (None, 3.5),
  "inspect.getcoroutinestate": (None, 3.5),
  "inspect.getgeneratorlocals": (None, 3.2),
  "inspect.getgeneratorstate": (None, 3.2),
  "inspect.isabstract": (2.6, 3.0),
  "inspect.isasyncgen": (None, 3.6),
  "inspect.isasyncgenfunction": (None, 3.6),
  "inspect.isawaitable": (None, 3.5),
  "inspect.iscoroutine": (None, 3.5),
  "inspect.iscoroutinefunction": (None, 3.5),
  "inspect.isdatadescriptor": (2.3, 3.0),
  "inspect.isgenerator": (2.6, 3.0),
  "inspect.isgeneratorfunction": (2.6, 3.0),
  "inspect.isgetsetdescriptor": (2.5, 3.0),
  "inspect.ismemberdescriptor": (2.5, 3.0),
  "inspect.signature": (None, 3.3),
  "inspect.unwrap": (None, 3.4),
  "io.BufferedIOBase.detach": (2.7, 3.1),
  "io.BufferedIOBase.readinto1": (None, 3.5),
  "io.BytesIO.getbuffer": (None, 3.2),
  "io.BytesIO.readinto1": (None, 3.5),
  "io.TextIOBase.detach": (2.7, 3.1),
  "itertools.accumulate": (None, 3.2),
  "itertools.combinations": (2.6, 3.0),
  "itertools.combinations_with_replacement": (2.7, 3.1),
  "itertools.compress": (2.7, 3.1),
  "itertools.groupby": (2.4, 3.0),
  "itertools.izip_longest": (2.6, 3.0),
  "itertools.permutations": (2.6, 3.0),
  "itertools.product": (2.6, 3.0),
  "itertools.tee": (2.4, 3.0),
  "logging.Logger.getChild": (2.7, 3.2),
  "logging.Logger.hasHandlers": (None, 3.2),
  "logging.getLogRecordFactory": (None, 3.2),
  "logging.setLogRecordFactory": (None, 3.2),
  "math.acosh": (2.6, 3.0),
  "math.asinh": (2.6, 3.0),
  "math.atanh": (2.6, 3.0),
  "math.copysign": (2.6, 3.0),
  "math.erf": (2.7, 3.2),
  "math.erfc": (2.7, 3.2),
  "math.expm1": (2.7, 3.2),
  "math.fsum": (2.6, 3.0),
  "math.gamma": (2.7, 3.2),
  "math.gcd": (None, 3.5),
  "math.isclose": (None, 3.5),
  "math.isfinite": (None, 3.2),
  "math.isinf": (2.6, 3.0),
  "math.isnan": (2.6, 3.0),
  "math.lgamma": (2.7, 3.2),
  "math.log1p": (2.6, 3.0),
  "math.log2": (None, 3.3),
  "math.trunc": (2.6, 3.0),
  "multiprocessing.Pool.starmap": (None, 3.3),
  "multiprocessing.Pool.starmap_async": (None, 3.3),
  "multiprocessing.connection.wait": (None, 3.3),
  "multiprocessing.get_all_start_methods": (None, 3.4),
  "multiprocessing.get_context": (None, 3.4),
  "multiprocessing.get_start_method": (None, 3.4),
  "multiprocessing.set_start_method": (None, 3.4),
  "os.fsdecode": (None, 3.2),
  "os.fsencode": (None, 3.2),
  "os.fspath": (None, 3.6),
  "os.get_blocking": (None, 3.5),
  "os.get_exec_path": (None, 3.2),
  "os.get_handle_inheritable": (None, 3.4),
  "os.get_inheritable": (None, 3.4),
  "os.get_terminal_size": (None, 3.3),
  "os.getenvb": (None, 3.2),
  "os.getgrouplist": (None, 3.3),
  "os.getpgid": (2.3, 3.0),
  "os.getpriority": (None, 3.3),
  "os.getresgid": (2.7, 3.0),
  "os.getresuid": (2.7, 3.0),
  "os.getsid": (2.4, 3.0),
  "os.initgroups": (2.7, 3.2),
  "os.lockf": (None, 3.3),
  "os.path.commonpath": (None, 3.5),
  "os.path.getctime": (2.3, 3.0),
  "os.path.ismount": (None, 3.4),
  "os.path.lexists": (2.4, 3.0),
  "os.path.realpath": (2.2, 3.0),
  "os.path.relpath": (2.6, 3.0),
  "os.pipe2": (None, 3.3),
  "os.posix_fadvise": (None, 3.3),
  "os.posix_fallocate": (None, 3.3),
  "os.pread": (None, 3.3),
  "os.pwrite": (None, 3.3),
  "os.readv": (None, 3.3),
  "os.sendfile": (None, 3.3),
  "os.set_blocking": (None, 3.5),
  "os.set_handle_inheritable": (None, 3.4),
  "os.set_inheritable": (None, 3.4),
  "os.setgroups": (2.2, 3.0),
  "os.setpriority": (None, 3.3),
  "os.setresgid": (2.7, 3.2),
  "os.setresuid": (2.7, 3.2),
  "os.writev": (None, 3.3),
  "pathlib.Path.expanduser": (None, 3.5),
  "pathlib.Path.home": (None, 3.5),
  "pathlib.Path.is_mount": (None, 3.7),
  "pathlib.Path.read_bytes": (None, 3.5),
  "pathlib.Path.read_text": (None, 3.5),
  "pathlib.Path.samefile": (None, 3.5),
  "pathlib.Path.write_bytes": (None, 3.5),
  "pathlib.Path.write_text": (None, 3.5),
  "pickletools.optimize": (2.6, 3.0),
  "pkgutil.get_data": (2.6, 3.0),
  "platform.linux_distribution": (2.6, 3.0),
  "platform.python_branch": (2.6, 3.0),
  "platform.python_implementation": (2.6, 3.0),
  "platform.python_revision": (2.6, 3.0),
  "runpy.run_path": (2.7, 3.2),
  "shlex.pop_source": (2.1, 3.0),
  "shlex.push_source": (2.1, 3.0),
  "shlex.quote": (None, 3.3),
  "shlex.split": (2.3, 3.0),
  "sqlite3.Connection.enable_load_extension": (2.7, 3.2),
  "sqlite3.Connection.iter_dump": (2.6, 3.0),
  "sqlite3.Connection.load_extension": (2.7, 3.2),
  "sqlite3.Connection.set_progress_handler": (2.6, 3.0),
  "sqlite3.Connection.set_trace_callback": (None, 3.3),
  "sqlite3.Row.keys": (2.6, 3.0),
  "ssl.RAND_bytes": (None, 3.3),
  "ssl.RAND_pseudo_bytes": (None, 3.3),
  "ssl.SSLContext.cert_store_stats": (None, 3.4),
  "ssl.SSLContext.get_ca_certs": (None, 3.4),
  "ssl.SSLContext.get_ciphers": (None, 3.6),
  "ssl.SSLContext.load_default_certs": (None, 3.4),
  "ssl.SSLContext.load_dh_params": (None, 3.3),
  "ssl.SSLContext.set_alpn_protocols": (2.7, 3.5),
  "ssl.SSLContext.set_ecdh_curve": (None, 3.3),
  "ssl.SSLContext.set_npn_protocols": (2.7, 3.3),
  "ssl.SSLContext.set_servername_callback": (None, 3.4),
  "ssl._https_verify_certificates": (2.7, None),
  "ssl.compression": (2.7, 3.3),
  "ssl.create_default_context": (2.7, 3.4),
  "ssl.enum_certificates": (2.7, 3.4),
  "ssl.enum_crls": (2.7, 3.4),
  "ssl.get_channel_binding": (2.7, 3.3),
  "ssl.get_default_verify_paths": (2.7, 3.4),
  "ssl.match_hostname": (2.7, 3.2),
  "ssl.selected_alpn_protocol": (2.7, 3.5),
  "ssl.selected_npn_protocol": (2.7, 3.3),
  "ssl.shared_ciphers": (None, 3.5),
  "ssl.version": (2.7, 3.5),
  "subprocess.CompletedProcess.check_returncode": (None, 3.5),
  "subprocess.Popen.kill": (2.6, 3.0),
  "subprocess.Popen.send_signal": (2.6, 3.0),
  "subprocess.Popen.terminate": (2.6, 3.0),
  "subprocess.check_call": (2.5, 3.0),
  "subprocess.check_output": (2.7, 3.1),
  "subprocess.run": (None, 3.5),
  "sys.exc_clear": (2.3, None),
  "sys.getcheckinterval": (2.3, 3.0),
  "sys.getdefaultencoding": (2.0, 3.0),
  "sys.getdlopenflags": (2.2, 3.0),
  "sys.getfilesystemencoding": (2.3, 3.0),
  "sys.getprofile": (2.6, 3.0),
  "sys.getsizeof": (2.6, 3.0),
  "sys.gettrace": (2.6, 3.0),
  "sys.getwindowsversion": (2.3, 3.0),
  "tarfile.TarFile.extractall": (2.5, 3.0),
  "tarfile.TarInfo.fromtarfile": (2.6, 3.0),
  "textwrap.indent": (None, 3.3),
  "textwrap.shorten": (None, 3.4),
  "time.clock_getres": (None, 3.3),
  "time.clock_gettime": (None, 3.3),
  "time.clock_gettime_ns": (None, 3.7),
  "time.clock_settime": (None, 3.3),
  "time.clock_settime_ns": (None, 3.7),
  "time.get_clock_info": (None, 3.3),
  "time.monotonic": (None, 3.3),
  "time.monotonic_ns": (None, 3.7),
  "time.perf_counter": (None, 3.3),
  "time.perf_counter_ns": (None, 3.7),
  "time.process_time": (None, 3.3),
  "time.process_time_ns": (None, 3.7),
  "time.pthread_getcpuclockid": (None, 3.7),
  "time.thread_time": (None, 3.7),
  "time.thread_time_ns": (None, 3.7),
  "time.time_ns": (None, 3.7),
  "timeit.repeat": (2.6, 3.0),
  "timeit.timeit": (2.6, 3.0),
  "typing.NewType": (None, 3.5),
  "unittest.TestCase.addCleanup": (2.7, 3.1),
  "unittest.TestCase.addTypeEqualityFunc": (2.7, 3.1),
  "unittest.TestCase.assertDictContainsSubset": (2.7, 3.1),
  "unittest.TestCase.assertDictEqual": (2.7, 3.1),
  "unittest.TestCase.assertGreater": (2.7, 3.1),
  "unittest.TestCase.assertGreaterEqual": (2.7, 3.1),
  "unittest.TestCase.assertIn": (2.7, 3.1),
  "unittest.TestCase.assertIs": (2.7, 3.1),
  "unittest.TestCase.assertIsInstance": (2.7, 3.2),
  "unittest.TestCase.assertIsNone": (2.7, 3.1),
  "unittest.TestCase.assertIsNot": (2.7, 3.1),
  "unittest.TestCase.assertIsNotNone": (2.7, 3.1),
  "unittest.TestCase.assertItemsEqual": (2.7, 3.1),
  "unittest.TestCase.assertLess": (2.7, 3.1),
  "unittest.TestCase.assertLessEqual": (2.7, 3.1),
  "unittest.TestCase.assertListEqual": (2.7, 3.1),
  "unittest.TestCase.assertMultilineEqual": (2.7, 3.1),
  "unittest.TestCase.assertNotIn": (2.7, 3.1),
  "unittest.TestCase.assertNotIsInstance": (2.7, 3.2),
  "unittest.TestCase.assertNotRegex": (None, 3.1),
  "unittest.TestCase.assertNotRegexpMatches": (2.7, 3.1),
  "unittest.TestCase.assertRaisesRegexp": (2.7, 3.1),
  "unittest.TestCase.assertRegex": (None, 3.1),
  "unittest.TestCase.assertRegexpMatches": (2.7, 3.1),
  "unittest.TestCase.assertSequenceEqual": (2.7, 3.1),
  "unittest.TestCase.assertSetEqual": (2.7, 3.1),
  "unittest.TestCase.assertTupleEqual": (2.7, 3.1),
  "unittest.TestCase.doCleanups": (2.7, 3.1),
  "unittest.TestCase.longMessage": (2.7, 3.1),
  "unittest.TestCase.maxDiff": (2.7, 3.2),
  "unittest.TestLoader.discover": (2.7, 3.2),
  "unittest.TestResult.startTestRun": (2.7, 3.1),
  "unittest.TestResult.stopTestRun": (2.7, 3.1),
  "warnings.warnpy3k": (2.6, 3.0),
  "weakref.WeakKeyDictionary.iterkeyrefs": (2.5, 3.0),
  "weakref.WeakKeyDictionary.keyrefs": (2.5, 3.0),
  "weakref.WeakValueDictionary.itervaluerefs": (2.5, 3.0),
  "weakref.WeakValueDictionary.valuerefs": (2.5, 3.0),
  "wsgiref.handlers.read_environ": (None, 3.2),
  "xml.etree.ElementTree.Element.extend": (2.7, 3.2),
  "xml.etree.ElementTree.Element.iter": (2.7, 3.2),
  "xml.etree.ElementTree.Element.iterfind": (2.7, 3.2),
  "xml.etree.ElementTree.Element.itertext": (2.7, 3.2),
  "xml.etree.ElementTree.ElementTree.iterfind": (2.7, 3.2),
  "xml.etree.ElementTree.TreeBuilder.doctype": (2.7, 3.2),
  "xml.etree.ElementTree.fromstringlist": (2.7, 3.2),
  "xml.etree.ElementTree.register_namespace": (2.7, 3.2),
  "xml.etree.ElementTree.tostringlist": (2.7, 3.2),
  "xmlrpc.server.SimpleXMLRPCServer.register_introspection_functions": (None, 3.0),
  "zipfile.ZipFile.extract": (2.6, 3.0),
  "zipfile.ZipFile.extractall": (2.6, 3.0),
  "zipfile.ZipFile.open": (2.6, 3.0),
  "zipfile.ZipFile.setpassword": (2.6, 3.0),
  "zipfile.ZipInfo.from_file": (None, 3.6),
  "zipfile.ZipInfo.is_dir": (None, 3.6),
  "zipimport.zipimporter.get_filename": (2.7, 3.1),

  # Variables and Constants
  "SimpleXMLRPCServer.SimpleXMLRPCRequestHandler.encode_threshold": (2.7, None),
  "SimpleXMLRPCServer.SimpleXMLRPCRequestHandler.rpc_paths": (2.5, None),
  "__future__.absolute_import": (2.5, 3.0),
  "__future__.division": (2.2, 3.0),
  "__future__.generator_stop": (None, 3.5),
  "__future__.generators": (2.2, 3.0),
  "__future__.nested_scopes": (2.1, 3.0),
  "__future__.print_function": (2.6, 3.0),
  "__future__.unicode_literals": (2.6, 3.0),
  "__future__.with_statement": (2.5, 3.0),
  "bz2.BZ2Decompressor.eof": (None, 3.3),
  "bz2.BZ2Decompressor.needs_input": (None, 3.5),
  "collections.deque.maxlen": (2.7, 3.1),
  "contextvars.ContextVar.name": (None, 3.7),
  "crypt.METHOD_CRYPT": (None, 3.3),
  "crypt.METHOD_MD5": (None, 3.3),
  "crypt.METHOD_SHA256": (None, 3.3),
  "crypt.METHOD_SHA512": (None, 3.3),
  "crypt.methods": (None, 3.3),
  "datetime.datetime.fold": (None, 3.6),
  "hashlib.algorithms": (2.7, None),
  "hashlib.algorithms_available": (2.7, 3.2),
  "hashlib.algorithms_guaranteed": (2.7, 3.2),
  "hmac.HMAC.block_size": (None, 3.4),
  "hmac.HMAC.name": (None, 3.4),
  "importlib.machinery.BYTECODE_SUFFIXES": (None, 3.3),
  "importlib.machinery.DEBUG_BYTECODE_SUFFIXES": (None, 3.3),
  "importlib.machinery.EXTENSION_SUFFIXES": (None, 3.3),
  "importlib.machinery.OPTIMIZED_BYTECODE_SUFFIXES": (None, 3.3),
  "importlib.machinery.SOURCE_SUFFIXES": (None, 3.3),
  "importlib.util.MAGIC_NUMBER": (None, 3.4),
  "inspect.CO_ASYNC_GENERATOR": (None, 3.6),
  "inspect.CO_COROUTINE": (None, 3.5),
  "inspect.CO_ITERABLE_COROUTINE": (None, 3.5),
  "ipaddress.IPv4Address.is_global": (None, 3.4),
  "ipaddress.IPv4Address.reverse_pointer": (None, 3.5),
  "ipaddress.IPv6Address.is_global": (None, 3.4),
  "logging.lastResort": (None, 3.2),
  "math.inf": (None, 3.5),
  "math.nan": (None, 3.5),
  "math.tau": (None, 3.6),
  "multiprocessing.Process.sentinel": (None, 3.3),
  "os.F_LOCK": (None, 3.3),
  "os.F_TEST": (None, 3.3),
  "os.F_TLOCK": (None, 3.3),
  "os.F_ULOCK": (None, 3.3),
  "os.O_CLOEXEC": (None, 3.3),
  "os.O_PATH": (None, 3.4),
  "os.O_TMPFILE": (None, 3.4),
  "os.POSIX_FADV_DONTNEED": (None, 3.3),
  "os.POSIX_FADV_NOREUSE": (None, 3.3),
  "os.POSIX_FADV_NORMAL": (None, 3.3),
  "os.POSIX_FADV_RANDOM": (None, 3.3),
  "os.POSIX_FADV_SEQUENTIAL": (None, 3.3),
  "os.POSIX_FADV_WILLNEED": (None, 3.3),
  "os.PRIO_PGRP": (None, 3.3),
  "os.PRIO_PROCESS": (None, 3.3),
  "os.PRIO_USER": (None, 3.3),
  "os.SF_MNOWAIT": (None, 3.3),
  "os.SF_NODISKIO": (None, 3.3),
  "os.SF_SYNC": (None, 3.3),
  "os.environb": (None, 3.2),
  "os.path.supports_unicode_filenames": (2.3, 3.0),
  "os.supports_bytes_environ": (None, 3.2),
  "shlex.eof": (2.3, 3.0),
  "shlex.escape": (2.3, 3.0),
  "shlex.escapedquotes": (2.3, 3.0),
  "shlex.punctuation_chars": (None, 3.6),
  "shlex.whitespace_split": (2.3, 3.0),
  "ssl.ALERT_DESCRIPTION_HANDSHAKE_FAILURE": (2.7, 3.4),
  "ssl.ALERT_DESCRIPTION_INTERNAL_ERROR": (2.7, 3.4),
  "ssl.CHANNEL_BINDING_TYPES": (2.7, 3.3),
  "ssl.HAS_ALPN": (2.7, 3.5),
  "ssl.HAS_ECDH": (2.7, 3.3),
  "ssl.HAS_NPN": (2.7, 3.3),
  "ssl.HAS_SNI": (2.7, 3.2),
  "ssl.HAS_TLSv1_3": (2.7, 3.6),
  "ssl.OPENSSL_VERSION": (2.7, 3.2),
  "ssl.OPENSSL_VERSION_INFO": (2.7, 3.2),
  "ssl.OPENSSL_VERSION_NUMBER": (2.7, 3.2),
  "ssl.OP_ALL": (2.7, 3.2),
  "ssl.OP_CIPHER_SERVER_PREFERENCE": (2.7, 3.3),
  "ssl.OP_NO_COMPRESSION": (2.7, 3.3),
  "ssl.OP_NO_SSLv2": (2.7, 3.2),
  "ssl.OP_NO_SSLv3": (2.7, 3.2),
  "ssl.OP_NO_TLSv1": (2.7, 3.2),
  "ssl.OP_NO_TLSv1_1": (2.7, 3.4),
  "ssl.OP_NO_TLSv1_2": (2.7, 3.4),
  "ssl.OP_NO_TLSv1_3": (2.7, 3.6),
  "ssl.OP_SINGLE_DH_USE": (2.7, 3.3),
  "ssl.OP_SINGLE_ECDH_USE": (2.7, 3.3),
  "ssl.PROTOCOL_TLS": (2.7, 3.6),
  "ssl.PROTOCOL_TLSv1_1": (2.7, 3.4),
  "ssl.PROTOCOL_TLSv1_2": (2.7, 3.4),
  "ssl.SSLContext.check_hostname": (None, 3.4),
  "ssl.SSLContext.verify_flags": (None, 3.4),
  "ssl.SSLError.library": (2.7, 3.3),
  "ssl.SSLError.reason": (2.7, 3.3),
  "ssl.SSLSocket.context": (2.7, 3.2),
  "ssl.SSLSocket.server_hostname": (None, 3.2),
  "ssl.SSLSocket.server_side": (None, 3.2),
  "ssl.SSLSocket.session": (None, 3.2),
  "ssl.SSLSocket.session_reused": (None, 3.2),
  "ssl.VERIFY_CRL_CHECK_CHAIN": (2.7, 3.4),
  "ssl.VERIFY_CRL_CHECK_LEAF": (2.7, 3.4),
  "ssl.VERIFY_DEFAULT": (2.7, 3.4),
  "ssl.VERIFY_X509_STRICT": (2.7, 3.4),
  "ssl.VERIFY_X509_TRUSTED_FIRST": (2.7, 3.4),
  "subprocess.DEVNULL": (None, 3.3),
  "subprocess.Popen.args": (None, 3.3),
  "sys.api_version": (2.3, 3.0),
  "sys.flags": (2.6, 3.0),
  "sys.float_info": (2.6, 3.0),
  "sys.float_repr_style": (2.7, 3.0),
  "sys.long_info": (2.7, None),
  "sys.py3kwarning": (2.6, None),
  "sys.subversion": (2.5, None),
  "sys.version_info": (2.0, 3.0),
  "tarfile.TarFile.pax_headers": (2.6, 3.0),
  "tarfile.TarInfo.pax_headers": (2.6, 3.0),
  "time.CLOCK_BOOTTIME": (None, 3.7),
  "time.CLOCK_HIGHRES": (None, 3.3),
  "time.CLOCK_MONOTONIC": (None, 3.3),
  "time.CLOCK_MONOTONIC_RAW": (None, 3.3),
  "time.CLOCK_PROCESS_CPUTIME_ID": (None, 3.3),
  "time.CLOCK_PROF": (None, 3.7),
  "time.CLOCK_REALTIME": (None, 3.3),
  "time.CLOCK_THREAD_CPUTIME_ID": (None, 3.3),
  "time.CLOCK_UPTIME": (None, 3.7),
  "typing.TYPE_CHECKING": (None, 3.5),
  "unittest.TestResult.buffer": (2.7, 3.0),
  "unittest.TestResult.failfast": (2.7, 3.0),
  "unittest.TestResult.skipped": (2.7, 3.0),
  "xmlrpc.server.SimpleXMLRPCRequestHandler.rpc_paths": (None, 3.0),
  "zipfile.ZIP_BZIP2": (None, 3.3),
  "zipfile.ZIP_LZMA": (None, 3.3),
}

# Keyword arguments requirements: (function, keyword argument) -> (requirements)
KWARGS_REQS = {
  ("SimpleXMLRPCServer.CGIXMLRPCRequestHandler", "allow_none"): (2.5, None),
  ("SimpleXMLRPCServer.CGIXMLRPCRequestHandler", "encoding"): (2.5, None),
  ("SimpleXMLRPCServer.SimpleXMLRPCServer", "allow_none"): (2.5, None),
  ("SimpleXMLRPCServer.SimpleXMLRPCServer", "bind_and_active"): (2.6, None),
  ("SimpleXMLRPCServer.SimpleXMLRPCServer", "encoding"): (2.5, None),
  ("SimpleXMLRPCServer.SimpleXMLRPCServer.register_instance", "allow_dotted_names"): (2.3, 3.0),
  ("__import__", "level"): (2.5, 3.0),
  ("bz2.BZ2Decompressor.decompress", "max_length"): (None, 3.5),
  ("collections.deque", "maxlen"): (2.6, 3.0),
  ("collections.namedtuple", "module"): (None, 3.6),
  ("collections.namedtuple", "rename"): (2.7, 3.1),
  ("compile", "dont_inherit"): (2.3, 3.0),
  ("compile", "flags"): (2.3, 3.0),
  ("compile", "optimize"): (None, 3.2),
  ("ctypes.CDLL", "use_errno"): (2.6, 3.0),
  ("ctypes.CDLL", "use_last_error"): (2.6, 3.0),
  ("ctypes.CFUNCTYPE", "use_errno"): (2.6, 3.0),
  ("ctypes.CFUNCTYPE", "use_last_error"): (2.6, 3.0),
  ("ctypes.OleDLL", "use_errno"): (2.6, 3.0),
  ("ctypes.OleDLL", "use_last_error"): (2.6, 3.0),
  ("ctypes.WinDLL", "use_errno"): (2.6, 3.0),
  ("ctypes.WinDLL", "use_last_error"): (2.6, 3.0),
  ("ctypes.byref", "offset"): (2.6, 3.0),
  ("datetime.datetime", "fold"): (None, 3.6),
  ("datetime.datetime.combine", "tzinfo"): (None, 3.6),
  ("datetime.datetime.isoformat", "timespec"): (None, 3.6),
  ("datetime.datetime.replace", "fold"): (None, 3.6),
  ("difflib.HtmlDiff.make_file", "charset"): (None, 3.5),
  ("difflib.SequenceMatcher", "autojunk"): (2.7, 3.2),
  ("email.generator.BytesGenerator", "policy"): (None, 3.3),
  ("email.generator.Generator", "policy"): (None, 3.3),
  ("email.message_from_file", "strict"): (2.2, 3.0),
  ("email.message_from_string", "strict"): (2.2, 3.0),
  ("email.mime.application.MIMEApplication", "policy"): (None, 3.6),
  ("email.mime.audio.MIMEAudio", "policy"): (None, 3.6),
  ("email.mime.base.MIMEBase", "policy"): (None, 3.6),
  ("email.mime.image.MIMEImage", "policy"): (None, 3.6),
  ("email.mime.message.MIMEMessage", "policy"): (None, 3.6),
  ("email.mime.multipart.MIMEMultipart", "policy"): (None, 3.6),
  ("email.mime.text.MIMEText", "policy"): (None, 3.6),
  ("email.parser.BytesFeedParser", "policy"): (None, 3.3),
  ("email.parser.FeedParser", "policy"): (None, 3.3),
  ("email.utils.formatdate", "charset"): (None, 3.3),
  ("email.utils.make_msgid", "domain"): (None, 3.2),
  ("enumerate", "start"): (2.6, 3.0),
  ("functools.lru_cache", "typed"): (None, 3.3),
  ("heapq.merge", "key"): (None, 3.5),
  ("heapq.merge", "reverse"): (None, 3.5),
  ("heapq.nlargest", "key"): (2.4, 3.0),
  ("heapq.nsmallest", "key"): (2.4, 3.0),
  ("importlib.util.cache_from_source", "optimization"): (None, 3.5),
  ("inspect.signature", "follow_wrapped"): (None, 3.5),
  ("io.TextIOWrapper", "write_through"): (None, 3.3),
  ("itertools.accumulate", "func"): (None, 3.3),
  ("itertools.count", "step"): (None, 3.1),
  ("json.JSONDecoder", "object_pairs_hook"): (2.7, 3.1),
  ("json.load", "object_pairs_hook"): (2.7, 3.1),
  ("logging.Formatter", "style"): (None, 3.2),
  ("logging.LogRecord", "func"): (2.5, 3.0),
  ("logging.Logger.makeRecord", "extra"): (2.5, 3.0),
  ("logging.Logger.makeRecord", "func"): (2.5, 3.0),
  ("logging.debug", "extra"): (2.5, 3.0),
  ("logging.debug", "stack_info"): (None, 3.2),
  ("lzma.decompress", "max_length"): (None, 3.5),
  ("math.log", "base"): (2.3, 3.0),
  ("max", "default"): (None, 3.4),
  ("max", "key"): (2.5, 3.0),
  ("min", "default"): (None, 3.4),
  ("min", "key"): (2.5, 3.0),
  ("multiprocessing.Pool", "context"): (None, 3.4),
  ("multiprocessing.Pool", "maxtasksperchild"): (None, 3.2),
  ("multiprocessing.Process", "daemon"): (None, 3.3),
  ("open", "opener"): (None, 3.3),
  ("os.access", "dir_fd"): (None, 3.3),
  ("os.access", "effective_ids"): (None, 3.3),
  ("os.access", "follow_symlinks"): (None, 3.3),
  ("os.chflags", "follow_symlinks"): (None, 3.3),
  ("os.chmod", "dir_fd"): (None, 3.3),
  ("os.chmod", "follow_symlinks"): (None, 3.3),
  ("os.chown", "dir_fd"): (None, 3.3),
  ("os.chown", "follow_symlinks"): (None, 3.3),
  ("os.dup2", "inheritable"): (None, 3.4),
  ("os.link", "dst_dir_fd"): (None, 3.3),
  ("os.link", "follow_symlinks"): (None, 3.3),
  ("os.link", "src_dir_fd"): (None, 3.3),
  ("os.open", "dir_fd"): (None, 3.3),
  ("pathlib.Path.mkdir", "exist_ok"): (None, 3.5),
  ("pathlib.Path.resolve", "strict"): (None, 3.6),
  ("pickletools.dis", "annotate"): (None, 3.2),
  ("pprint.PrettyPrinter", "compact"): (None, 3.4),
  ("pprint.pformat", "compact"): (None, 3.4),
  ("pprint.pprint", "compact"): (None, 3.4),
  ("print", "flush"): (None, 3.3),
  ("shlex.shlex", "punctuation_chars"): (None, 3.6),
  ("shlex.split", "posix"): (2.6, 3.0),
  ("ssl.SSLContext.load_cert_chain", "password"): (None, 3.3),
  ("ssl.SSLContext.load_verify_locations", "cadata"): (None, 3.4),
  ("ssl.wrap_socket", "ciphers"): (2.7, 3.2),
  ("subprocess.Popen", "encoding"): (None, 3.6),
  ("subprocess.Popen", "errors"): (None, 3.6),
  ("subprocess.Popen", "pass_fds"): (None, 3.2),
  ("subprocess.Popen", "restore_signals"): (None, 3.2),
  ("subprocess.Popen", "start_new_session"): (None, 3.2),
  ("subprocess.Popen.communicate", "timeout"): (None, 3.3),
  ("subprocess.Popen.wait", "timeout"): (None, 3.3),
  ("subprocess.call", "timeout"): (None, 3.3),
  ("subprocess.check_call", "timeout"): (None, 3.3),
  ("subprocess.check_output", "input"): (None, 3.4),
  ("subprocess.check_output", "timeout"): (None, 3.3),
  ("subprocess.run", "encoding"): (None, 3.6),
  ("subprocess.run", "errors"): (None, 3.6),
  ("tarfile.TarFile.add", "exclude"): (2.6, 3.0),
  ("tarfile.TarFile.add", "filter"): (2.7, 3.2),
  ("tarfile.TarFile.extract", "numeric_owner"): (None, 3.5),
  ("tarfile.TarFile.extract", "set_attrs"): (None, 3.2),
  ("tarfile.TarFile.extractall", "numeric_owner"): (None, 3.5),
  ("tarfile.TarFile.list", "members"): (None, 3.5),
  ("tarfile.TarInfo.tobuf", "encoding"): (2.6, 3.0),
  ("tarfile.TarInfo.tobuf", "errors"): (2.6, 3.0),
  ("tarfile.TarInfo.tobuf", "format"): (2.6, 3.0),
  ("tracemalloc.Filter", "domain"): (None, 3.6),
  ("unittest.TestCase.assertAlmostEqual", "delta"): (2.7, 3.0),
  ("unittest.TestCase.assertNotAlmostEqual", "delta"): (2.7, 3.0),
  ("unittest.mock.Mock", "unsafe"): (None, 3.5),
  ("venv.EnvBuilder", "prompt"): (None, 3.6),
  ("venv.EnvBuilder", "with_pip"): (None, 3.4),
  ("venv.create", "with_pip"): (None, 3.4),
  ("warnings.formatwarning", "line"): (2.6, 3.0),
  ("warnings.warn", "source"): (None, 3.6),
  ("warnings.warn_explicit", "module_globals"): (2.5, 3.0),
  ("warnings.warn_explicit", "source"): (None, 3.6),
  ("xml.etree.ElementTree.iterparse", "parser"): (None, 3.4),
  ("xml.etree.ElementTree.tostring", "short_empty_elements"): (None, 3.4),
  ("xml.etree.ElementTree.tostringlist", "short_empty_elements"): (None, 3.4),
  ("xml.etree.ElementTree.write", "short_empty_elements"): (None, 3.4),
  ("xmlrpc.server.CGIXMLRPCRequestHandler", "use_builtin_types"): (None, 3.3),
  ("xmlrpc.server.DocXMLRPCServer", "use_builtin_types"): (None, 3.3),
  ("xmlrpc.server.SimpleXMLRPCServer", "use_builtin_types"): (None, 3.3),
  ("xmlrpclib.ServerProxy", "context"): (2.7, None),
  ("xmlrpclib.ServerProxy", "use_datetime"): (2.5, None),
  ("xmlrpclib.loads", "use_datetime"): (2.5, None),
  ("zipfile.PyZipFile", "optimize"): (None, 3.2),
  ("zipfile.PyZipFile.writepy", "filterfunc"): (None, 3.4),
  ("zipfile.ZipFile.read", "pwd"): (2.6, 3.0),
  ("zipfile.ZipFile.writestr", "compress_type"): (2.7, 3.2),
}

# datetime+time strftime/strptime requirements: directive -> requirements
STRFTIME_REQS = {
  "%G": (None, 3.6),
  "%V": (None, 3.6),
  "%f": (2.6, 3.0),
  "%u": (None, 3.6),
}
