import httplib
import urllib

HTTP_PROXY_HEADER_NAME = ["CLIENTIP", "X-FORWARDED-FOR"]


class HttpUtils(object):

    def __init__(self, host):
        self.host = host
        self.reqheaders = {'Content-type': 'application/x-www-form-urlencoded',
                           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                           'Host': host,
                           'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1', }

    def get(self, url, param):
        conn = None
        res = None
        try:
            conn = httplib.HTTPConnection(self.host)
            if param is not None:
                data = urllib.urlencode(param)
                conn.request("GET", url + "?" + data, self.reqheaders)
            else:
                conn.request("GET", url, headers=self.reqheaders)
            res = conn.getresponse().read()
        except Exception, e:
            print e
        finally:
            if conn:
                conn.close()
        return res

    def post(self, url, param):
        conn = None
        res = None
        try:
            conn = httplib.HTTPConnection(self.host)
            if param is not None:
                data = urllib.urlencode(param)
                conn.request('POST', url, data, self.reqheaders)
            else:
                conn.request('POST', url, headers=self.reqheaders)
            res = conn.getresponse().read()
        except Exception, e:
            print e
        finally:
            if conn:
                conn.close()
        return res


def getClientIP(head):
    for name in HTTP_PROXY_HEADER_NAME:
        if name in head:
            ip = head[name.upper()]
            if len(ip) > 0:
                return ip.split(",")[0]
