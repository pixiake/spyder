#encoding: utf-8

from urllib import request

guofneg_url = "http://www.renren.com/289199450/profile"

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.75 Safari/537.36 Maxthon/5.1.3.2000',
    'Cookie':'anonymid=jbnkq9w4-9rt2sl; UM_distinctid=16092ac884a537-0211681233488f-7e243017-100200-16092ac884b43b; depovince=HUB; jebecookies=7a0014ec-0f30-4409-b8d8-ebf9fba2d409|||||; _r01_=1; JSESSIONID=abciB8ZtDd5_MfnJU4Wcw; ick_login=4a07ba02-814e-4eab-bd3a-92c560881cfd; _de=D5AFDB0A3A1C18D17F0808EC67FE0F931383380866D39FF5; p=de0f12ba35dfb116c5598d941ced097d0; first_login_flag=1; ln_uact=guotongxue123@163.com; ln_hurl=http://hdn.xnimg.cn/photos/hdn121/20110619/2135/h_main_2R1i_295300004de72f76.jpg; t=a8b845d51a846d85464927919100f9b60; societyguester=a8b845d51a846d85464927919100f9b60; id=289199450; xnsid=4f1cde1d; jebe_key=aa6223d9-262d-4716-b011-7aa79259eb3f%7C261e1ffc5f1fa13ddea10edb0192f836%7C1514796166452%7C1%7C1514796164541; ver=7.0; loginfrom=null; wp_fold=0; CNZZDATA1256793290=131009450-1514792652-null%7C1514792652'
}

req = request.Request(url=guofneg_url , headers=headers)
resp = request.urlopen(req)
# print(resp.read().decode('utf-8'))

with open('renren.html','w',encoding='utf-8') as fp:
    fp.write(resp.read().decode('utf-8'))