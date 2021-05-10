import os
import asyncio
import paddlehub as hub
import json
from urllib import request
from urllib import parse
from wechaty import (
    Contact,
    FileBox,
    Message,
    Wechaty,
    ScanStatus,
)

os.environ['WECHATY_PUPPET'] = "wechaty-puppet-service"
os.environ['WECHATY_PUPPET_SERVICE_TOKEN'] = "80908090"
os.environ['WECHATY_PUPPET_SERVICE_ENDPOINT'] = "127.0.0.1:8080"
os.environ['CUDA_VISIBLE_DEVICES']='0'
module = hub.Module(name="plato2_en_base")

#翻译
def fanyi(i='',type='zh-CHS2en'):
    Request_URL = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
    #创建Form_Data字典，存储上图的Form Data
    Form_Data = {}
    # en2zh-CHS 英文-中文
    # zh-CHS2en 中文-英文
    Form_Data['type'] = type
    Form_Data['i'] = i
    Form_Data['doctype'] = 'json'
    Form_Data['Version'] = '2.1'
    Form_Data['keyfrom'] = 'fanyi.web'
    Form_Data['action'] = 'FY_BY_REALTlME'
    data = parse.urlencode(Form_Data).encode('utf-8')
    response = request.urlopen(Request_URL,data)
    html = response.read().decode('utf-8')
    translate_results = json.loads(html)
    results = translate_results['translateResult'][0][0]['tgt']
    return results

async def on_message(msg: Message):

    who = msg.talker()  # 发消息的人
    
    #设置好微信名，只要是他发的消息就回复
    if who.name == 'TTZO':
        #输入，翻译，模型输出，翻译，发送
        tf = fanyi(text,'zh-CHS2en')
        robott = module.generate(list(tf))
        returns = fanyi(robott[0],'en2zh-CHS')
        await msg.say(returns)

async def on_login(user: Contact):
    print(user)

async def main():
    bot = Wechaty()
    # bot.on('login',     on_login)
    bot.on('message',   on_message)
    await bot.start()

asyncio.run(main())
