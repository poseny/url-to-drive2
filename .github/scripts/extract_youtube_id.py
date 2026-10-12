import sys

def extract_video_id(u):
    i = u.find('youtu.be/')
    if i >= 0:
        s = u[i+9:]
        for sep in ['&', '?', '#']:
            j = s.find(sep)
            if j >= 0:
                s = s[:j]
        return s
    for p in ['/shorts/', '/embed/', '/v/']:
        if p in u:
            try:
                s = u.split(p)[1]
            except:
                continue
            for sep in ['&', '?', '#']:
                j = s.find(sep)
                if j >= 0:
                    s = s[:j]
            return s
    i = u.find('v=')
    if i >= 0:
        s = u[i+2:]
        for sep in ['&', '?', '#']:
            j = s.find(sep)
            if j >= 0:
                s = s[:j]
        return s
    return ''

if __name__ == '__main__':
    url = sys.argv[1] if len(sys.argv) > 1 else sys.stdin.read().strip()
    print(extract_video_id(url))
