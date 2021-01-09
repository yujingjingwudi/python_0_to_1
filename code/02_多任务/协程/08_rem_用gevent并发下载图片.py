import gevent
import urllib.request
from gevent import monkey

monkey.patch_all()


def download_file(url,pic_name):
    req = urllib.request.urlopen(url)
    content = req.read()
    with open(pic_name,"wb") as f:
        f.write(content)



def main():
    gevent.joinall([gevent.spawn(download_file,"https://i0.hdslb.com/bfs/bangumi/image/f2ebcd79e5ca8ae397b368cd52fb6846d7bb467a.png@450w_600h.webp","1.jpg"),
                    gevent.spawn(download_file,"https://i0.hdslb.com/bfs/bangumi/image/f2425cbdb07cc93bd0d3ba1c0099bfe78f5dc58a.png@450w_600h.webp","2.jpg"),
                    gevent.spawn(download_file,"https://i0.hdslb.com/bfs/bangumi/6fbd8eba88bbe5ea90b760771e5fca61117c00e9.png@450w_600h.webp","3.jpg")])



if __name__ == "__main__":
    main()