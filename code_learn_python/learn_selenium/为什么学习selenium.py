import urllib.request
url ='https://www.jd.com/'
headers={
    'Access-Control-Allow-Origin': '*',
    'Age': '12',
    'Cache-Control': 'max-age=30',
    'Connection': 'keep-alive',
    'Content-Encoding': 'gzip',
    'Content-Length': '50234',
    'Content-Type': 'text/html; charset=utf-8',
    'Date': 'Sun, 17 Oct 2021 03:44:17 GMT',
    'Expires': 'Sun, 17 Oct 2021 03:44:36 GMT',
    'init-worker-firstscreen': 'off',
    'init-worker-pageconfig': 'on',
    'ser': '149.22',
    'Server': 'nginx',
    'Strict-Transport-Security': 'max-age=3600',
    'Timing-Allow-Origin': '*',
    'Vary': 'Accept-Encoding',
    'Via': 'http/1.1 ORI-CLOUD-HB3-MIX-19 (jcs [cSsSfU]), http/1.1 HB-UNI-3-MIX-22 (jcs [cRs f ])',
    'X-Content-Type-Options': 'nosniff',
    'X-Frame-Options': 'SAMEORIGIN',
    'X-Trace': '200-1634442246137-0-0-15-36-36;200-1634442246123-0-0-0-62-62;200-1634442257993-0-0-0-0-0',
    'X-XSS-Protection': '1; mode=block',
}
request = urllib.request.Request(url=url, headers=headers)

response = urllib.request.urlopen(request)

content = response.read().decode('utf-8')
print(content)
