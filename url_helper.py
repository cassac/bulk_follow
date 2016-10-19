urls = [
'http://shouldhavehttps.com/in/dude',
'https://shouldbeok.com/in/girl',
'thisneedsstuff.com/in/some/thing',
'www.nogo.com/something',
'www.nope.com/in/connect',
'https://www.thisisok.com/myname']

def url_checker(url):
  if url[:11] != 'https://www':
    part1 = url.split('//')[-1]
    part2 = part1.split('www.')[-1]
    url = 'https://www.' + part2
  return url
