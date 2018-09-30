# -*- coding: utf-8 -*-

"""
netease-dl.config
~~~~~~~~~~~~~~~~~

Configuration file.
"""
import os


conf_dir = os.path.join(os.path.expanduser('~'), '.netease-dl')
person_info_path = os.path.join(conf_dir, 'person_info.json')
cookie_path = os.path.join(conf_dir, 'cookie')
log_path = os.path.join(conf_dir, 'logger.log')

headers = {
    # 'Cookie': 'appver=1.5.2',
    'Accept': '*/*',
    'Accept-Encoding': 'gzip,deflate,sdch',
    'Accept-Language': 'zh-CN,zh;q=0.8,gl;q=0.6,zh-TW;q=0.4',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Host': 'music.163.com',
    'Referer': 'http://music.163.com/search/',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/56.0.2924.76 Chrome/56.0.2924.76 Safari/537.36',
    'Cookie':'_ntes_nnid=908f2a85a88beb2679a5ef22ec3692d3,1513060818851; _ntes_nuid=908f2a85a88beb2679a5ef22ec3692d3; usertrack=ezq0plqnU36bN3fDBYwLAg==; _ga=GA1.2.2123028265.1520915566; mail_psc_fingerprint=e46b9e975dfd08e87c65e44d0261112a; _iuqxldmzr_=32; WM_TID=fybuMcf%2BnLR4eNHF2V5AHJK%2FASOm3QJe; __f_=1536484764223; __utmz=94650624.1537806087.22.13.utmcsr=127.0.0.1:8000|utmccn=(referral)|utmcmd=referral|utmcct=/blog/index/; __utmc=94650624; Hm_lvt_e394efadbd27c7bb2f2cdf8e588e7ac2=1536723980,1537416594,1537970918,1538282648; __utma=94650624.1398644418.1514274195.1538282648.1538284533.25; playerid=79299377; Hm_lpvt_e394efadbd27c7bb2f2cdf8e588e7ac2=1538285994; WM_NI=zBVxp6cWu9bqaF1DrA8N9plKriyEl2lGs2ohlr5giv8e0m3w9d1zKOfRROgm1Dc0q9uX48NLdlw8ta7iUbmbBUsq9Gvoh5YD8IR8ZuthcJQUs6ME7uZOm1TyEixe8HjFWVo%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eeb2c45fb19df7bab567f4bc8fa2d44a929e8faff36e87a7898fcf5d8cacc08ae92af0fea7c3b92aba9e9a99f33ea189bbdae17ba39affa5f14bfc92f791ef41b2b7b7a6ef3ab099bdd3ee64b0aefb88ec7efcbb008eb27dfbbcff9bca45a68e9eb0e667f39cadd1f433b788fcd9cd48a8b4b9d9f76bf5b79b83f06a828bbd92bc4db6b1a8d6dc50fc979ed9d97fb8b8adabd45fb1ea83a6b67f9a91a3d2d77387b7b886bb44aa9a99b7ee37e2a3; JSESSIONID-WYYY=0Hxf0T1x1cyUxYgUPoXvM2c7dlb0vuxRHDF0DiE%2Bk1aKlNB4Nls%2FjUIMPWmdo3%5CaSyj0NqZVKqtGfvmk0lgugUUxqIFdj94XRO86YzSoTTHx2C%2FkhGTFergAP%5CUtNAz8ff3v3sIRV5AukIl%2FIC8qGgG%2FDtFoPSRIOuad2eccuc8H9fZj%3A1538300113987',

}

modulus = '00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7'
nonce = '0CoJUm6Qyw8W8jud'
pub_key = '010001'
