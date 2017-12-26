import easygui as g
import urllib.parse
import json
import urllib.request

title='在线翻译软件'
msg='请输入想要翻译的内容'

while 1:
    #把要输入的内容返回给content
    content=g.enterbox(msg,title)

    url='http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=https://www.baidu.com/link'
    data={}
    data['type']='AUTO'
    data['i']=content
    data['doctype']='json'
    data['xmlVersion']='1.8'
    data['keyfrom']='fanyi.web'
    data['ue']='UTF-8'
    data['action']='FY_BY_CLICKBUTTON'
    data['typoResult']='true'
    data=urllib.parse.urlencode(data).encode('utf-8')




    response=urllib.request.urlopen(url,data)
    html=response.read().decode('utf-8')
    target=json.loads(html)
    g.msgbox(target['translateResult'][0][0]['tgt'],'翻译结果')
    if not g.enterbox():
        break
