from subprocess import Popen, PIPE
import os, sys
try:
    import json
except ImportError:
    import simplejson as json

lookup_path = "/usr/bin/python2.7 /home/noteacer/TMS/Music/echoprint-server/examples/lookup_API.py"
base_path = "/home/noteacer/TMS/Music/"
sys.path.insert(0, os.path.join(base_path, 'echoprint-server/API'))
import fp

codegen_path = os.path.abspath(
        os.path.join(base_path, "echoprint-codegen/echoprintcodegen"))

def codegen(file):
    proclist = [codegen_path,
                os.path.abspath(file),]
    p = Poen(proclist, stdout=PIPE)
    code = p.communicate()[0]
    return json.loads(code)

def lookup(file):
    file_format_error = "File format wrong"
    codes = codegen(file)
    if len(codes) and "code" in codes[0]:
        decoded = fp.decode_code_string(codes[0]["code"])
        result = fp.best_match_for_query(decoded)
        if result.TRID:
            return result.TRID
        else:
            return result
    else:
        return file_format_error

