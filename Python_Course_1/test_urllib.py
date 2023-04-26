import urllib.request

response = urllib.request.urlopen("")
info = response.read()
html = info.decode("UTF-8")
target_ini = '<span class="description">'
pos_ini = html.find(target_ini) + len(target_ini)
pos_fim = html.find('</span>', pos_ini)
print(html[pos_ini:pos_fim].replace('\n', '').lstrip())

