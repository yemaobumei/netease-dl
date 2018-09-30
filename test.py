import requests,os,json,base64
# from scrapy.selector import Selector
from  binascii import hexlify
from Crypto.Cipher import AES
import re
from urllib.request import urlretrieve

class Encrypyed():
    '''传入歌曲的ID，加密生成'params'、'encSecKey 返回'''
    def __init__(self):
        self.pub_key = '010001'
        self.modulus = '00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7'
        # self.modulus = '257348aecb5e556c066de214e531faadd1c55d814f9be95fd06d6bff9f4c7a41f831f6394d5a3fd2e3881736d94a02ca919d952872e7d0a50ebfa1769a7a62d512f5f1ca21aec60bc3819a9c3ffca5eca9a0dba6d6f7249b06f5965ecfff3695b54e1c28f3f624750ed39e7de08fc8493242e26dbc4484a01c76f739e135637c'
        self.nonce = '0CoJUm6Qyw8W8jud'

    def create_secret_key(self, size):
        return hexlify(os.urandom(size))[:16].decode('utf-8')

    # def aes_encrypt(self,text, key):
    #     iv = '0102030405060708'
    #     pad = 16 - len(text) % 16
    #     text = text + pad * chr(pad)
    #     encryptor = AES.new(key, AES.MODE_CBC, iv)
    #     result = encryptor.encrypt(text)
    #     result_str = base64.b64encode(result).decode('utf-8')
    #     return result_str
    def aes_encrypt(self,text, secKey):
        pad = 16 - len(text) % 16
        text = text + pad * chr(pad)
        encryptor = AES.new(secKey, 2, '0102030405060708')
        ciphertext = encryptor.encrypt(text)
        ciphertext = base64.b64encode(ciphertext)
        return ciphertext.decode()
    def rsa_encrpt(self,text, pubKey, modulus):
        text = text[::-1]
        rs = pow(int(hexlify(text.encode('utf-8')), 16), int(pubKey, 16), int(modulus, 16))
        return format(rs, 'x').zfill(256)

    def work(self,text):
        text = json.dumps(text)
        i=self.create_secret_key(16)
        encText =self.aes_encrypt(text, self.nonce)
        encText=self.aes_encrypt(encText,i)
        encSecKey=self.rsa_encrpt(i,self.pub_key,self.modulus)
        data = {'params': encText, 'encSecKey': encSecKey}
        return data


class wangyiyun():
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
            'Referer': 'http://music.163.com/',
            'Cookie':'_ntes_nnid=908f2a85a88beb2679a5ef22ec3692d3,1513060818851; _ntes_nuid=908f2a85a88beb2679a5ef22ec3692d3; usertrack=ezq0plqnU36bN3fDBYwLAg==; _ga=GA1.2.2123028265.1520915566; mail_psc_fingerprint=e46b9e975dfd08e87c65e44d0261112a; _iuqxldmzr_=32; WM_TID=fybuMcf%2BnLR4eNHF2V5AHJK%2FASOm3QJe; __f_=1536484764223; __utmz=94650624.1537806087.22.13.utmcsr=127.0.0.1:8000|utmccn=(referral)|utmcmd=referral|utmcct=/blog/index/; __utmc=94650624; Hm_lvt_e394efadbd27c7bb2f2cdf8e588e7ac2=1536723980,1537416594,1537970918,1538282648; __utma=94650624.1398644418.1514274195.1538282648.1538284533.25; playerid=79299377; Hm_lpvt_e394efadbd27c7bb2f2cdf8e588e7ac2=1538285994; WM_NI=zBVxp6cWu9bqaF1DrA8N9plKriyEl2lGs2ohlr5giv8e0m3w9d1zKOfRROgm1Dc0q9uX48NLdlw8ta7iUbmbBUsq9Gvoh5YD8IR8ZuthcJQUs6ME7uZOm1TyEixe8HjFWVo%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eeb2c45fb19df7bab567f4bc8fa2d44a929e8faff36e87a7898fcf5d8cacc08ae92af0fea7c3b92aba9e9a99f33ea189bbdae17ba39affa5f14bfc92f791ef41b2b7b7a6ef3ab099bdd3ee64b0aefb88ec7efcbb008eb27dfbbcff9bca45a68e9eb0e667f39cadd1f433b788fcd9cd48a8b4b9d9f76bf5b79b83f06a828bbd92bc4db6b1a8d6dc50fc979ed9d97fb8b8adabd45fb1ea83a6b67f9a91a3d2d77387b7b886bb44aa9a99b7ee37e2a3; JSESSIONID-WYYY=0Hxf0T1x1cyUxYgUPoXvM2c7dlb0vuxRHDF0DiE%2Bk1aKlNB4Nls%2FjUIMPWmdo3%5CaSyj0NqZVKqtGfvmk0lgugUUxqIFdj94XRO86YzSoTTHx2C%2FkhGTFergAP%5CUtNAz8ff3v3sIRV5AukIl%2FIC8qGgG%2FDtFoPSRIOuad2eccuc8H9fZj%3A1538300113987',
            }
        self.main_url='http://music.163.com/'
        self.session = requests.Session()
        self.session.headers=self.headers
        self.ep=Encrypyed()

    def get_songurls(self,playlist):
        '''进入所选歌单页面，得出歌单里每首歌各自的ID 形式就是“song?id=64006"'''
        url=self.main_url+'playlist?id=%d'% playlist
        res= self.session.get(url)   #直接用session进入网页，懒得构造了
        # sel=Selector(text=re.text)   #用scrapy的Selector，懒得用BS4了
        # songurls=sel.xpath('//ul[@class="f-hide"]/li/a/@href').extract()
        songurls = re.findall(r'href=\"(/song.*?)\"',res.text)
        return songurls   #所有歌曲组成的list
        ##['/song?id=64006', '/song?id=63959', '/song?id=25642714', '/song?id=63914', '/song?id=4878122', '/song?id=63650']


    def get_songinfo(self,songurl):
        '''根据songid进入每首歌信息的网址，得到歌曲的信息
        return：'64006'，'陈小春-失恋王'''
        url=self.main_url+songurl
        res=self.session.get(url)
        # sel=Selector(text=re.text)
        song_id = url.split('=')[1]
        # song_name = sel.xpath("//em[@class='f-ff2']/text()").extract_first()
        # singer= '&'.join(sel.xpath("//p[@class='des s-fc4']/span/a/text()").extract())
        result = re.findall(r'f-ff2\">(.+?)</em>',res.text)
        if len(result) == 0:
            song_name = "null"
        else:
            song_name = result[0]
        result = re.findall(r'artist.+?>(.+?)<',res.text)
        if len(result) == 0:
            singer = "null"
        else:
            singer = result[0]
        songname=singer+'-'+song_name
        return str(song_id),songname

    def get_url(self,ids,br=128000):
        '''self.ep.work输入歌曲ID，解码后返回data，{params 'encSecKey}
        然后post，得出歌曲所在url'''
        text = {'ids': [ids], 'br': br, 'csrf_token': ''}
        data=self.ep.work(text)
        url = 'http://music.163.com/weapi/song/enhance/player/url?csrf_token='
        req = self.session.post(url, data=data)
        print(req.json())
        song_url=req.json()['data'][0]['url']
        return song_url

    def download_song(self, songurl, dir_path):
        '''根据歌曲url，下载mp3文件'''
        song_id, songname = self.get_songinfo(songurl) #根据歌曲url得出ID、歌名
        song_url = self.get_url(song_id)                #根据ID得到歌曲的实质URL
        path = dir_path + os.sep + songname + '.mp3'   #文件路径
        urlretrieve(song_url, path)            #下载文件

    def work(self,playlist):
        songurls=self.get_songurls(playlist)         #输入歌单编号，得到歌单所有歌曲的url
        dir_path=r'/home/ubuntu/mp3'
        for songurl in songurls:
            self.download_song(songurl,dir_path)     #下载歌曲


if __name__ == '__main__':
    d=wangyiyun()
    d.work(2214059025)

