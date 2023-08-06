"""test output
"""
import subprocess
import threading
import time


ENCODING = 'utf-8'
TIMEOUT = 1  # second


def test_alwaysok():
    return 1


class Utils:
    @staticmethod
    def decode_out(open_file_desc):
        return open_file_desc.read().decode(ENCODING)


class ExeThread(threading.Thread):
    def __init__(self, exe, args):
        self.exe = exe
        self.args = args

        self.process = None
        self.retcode = None
        self.stdout = None
        self.stderr = None

        super().__init__()

    def run(self):
        command = [self.exe] + self.args
        self.process = subprocess.Popen(
            command,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        self.process.wait()
        self.retcode = self.process.returncode
        self.stdout = Utils.decode_out(self.process.stdout)
        self.stderr = Utils.decode_out(self.process.stderr)


def test_one_situation(exetest):
    starttime = time.time()
    exethread = ExeThread(exetest['exe'], exetest['args'])
    exethread.start()
    while True:

        if exethread.retcode is not None:
            break

        time.sleep(0.1)
        now = time.time()
        try:
            assert now < starttime + TIMEOUT, "Exe took too long"
        except AssertionError:
            exethread.process.kill()
            if exetest.get('expect_too_long', False):
                return
            raise

    assert not exetest.get('expect_too_long', False), \
        'Execution should have timed out'

    assert exetest['stdout'] == exethread.stdout
    assert exetest['stderr'] == exethread.stderr
    assert exetest['retcode'] == exethread.retcode
