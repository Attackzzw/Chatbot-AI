# Chatbot-AI

# **游戏'必备'，微信免打扰，让机器人和朋友瞎聊会**
## **项目说明：**
#### ·  该项目是由 Wechaty 和 PaddleHub 组成，Windows下Python运行。
#### ·  至于为什么不用Linux？是因为之前电脑是双系统，后来存储空间不够就把Linux那块硬盘格式化了，主要使用Windows的多，还有就是我要玩的游戏也是Windows下的，哈哈哈。
#### ·  还有就是5月8号接本考试，这个在之前4月中旬已经把对话功能写完了，就建立了该项目和github，剩下的是在5月9号才开始写的，在来弄Linux来不及了，就直接Windows下写了。
#### ·  当然小伙伴们自己电脑不长开机的话，也可以用服务器来gan，这个之后再说吧，反正我是没时间了~）

## **环境说明**
#### ·  **系统：** Windows 10 家庭中文版
#### ·  **运行环境：** Docker Desktop for Windows 
#### ·  **运行环境：** Python3.7
#### ·  **运行环境：** PaddlePaddle1.8.2
#### ·  **运行环境：** PaddleHub1.7.0
#### ·  **运行环境：** Sublime Text3（个人习惯，也可以使用别的，只要能运行python就可以）

## **安装说明：**
### 如果以上环境都有可以直接跳过‘安装说明’

### **1. Docker Desktop for Windows:**
#### **1.1. Docker官网下载：[Docker](https://hub.docker.com/editions/community/docker-ce-desktop-windows)**
&nbsp;

![Docker下载页面](https://ai-studio-static-online.cdn.bcebos.com/d91eafc3a1de41c4afe5fa1d9d20c909d38a565604f0424d91381dec3c19e4ba)
#### **1.2. 打开Hyper-V**
&nbsp;

#### ·  Windows下运行Docker还需要使用Hyper-V （微软开发的虚拟机）  **注意：使用Hyper-V的话，VM虚拟就使用不了了，所以慎重**
#### ·  打开Hyper-V ：启用或关闭Windows功能-->Hyper-V 打上对勾
#### ·  如果没有Hyper-V，参考链接安装：[win10家庭版没有自带虚拟机怎么办](http://www.xitongcheng.com/jiaocheng/win10_article_47641.html)
![Hyper-V打开](https://ai-studio-static-online.cdn.bcebos.com/1c7f88c0d54440e997775674f026d9e116c444e9f9dd4ac2a3ae6381566cd539)
#### **1.3.  安装Docker**
&nbsp;

#### ·  安装就直接下一步就行，关键是安装完成后打开，如果报错 **WSL 2**  ，参考链接：[适用于 Linux 的 Windows 子系统安装指南 (Windows 10)](https://docs.microsoft.com/zh-cn/windows/wsl/install-win10)   我也出来过，当时没有截图，报错大概就是一个对话框，提示你没有WSL 2，安装后重启即可

### **2. PaddlePaddle & PaddleHub**
#### **如果Paddle环境安装有问题请参考链接：[Windows-paddle-深度学习环境搭建](https://aistudio.baidu.com/aistudio/projectdetail/1147447)**

&nbsp;

#### Paddle版本是1.8.2  Hub版本是1.7.0，这里你可能会问：**为什么使用的都不是最新版呢!**  这个是因为版本兼容问题，我要使用的是‘plato2_en_base’这个模型，然而最新的paddle版本使用这个模型会报错，所以使用最初的支持这个模型的paddle版本还会更兼容一些
&nbsp;

#### **cmd运行以下命令，安装：**
```
pip install PaddleHub==1.7.0
pip install  paddlepaddle-gpu==1.8.2.post97 -i https://mirror.baidu.com/pypi/simple
hub install plato2_en_base==1.0.0 
```

#### **注：post后面两个数字是指CUDA版本，CUDNN版本，根据自己机器安装**

### **3. 编辑器**
#### **代码编辑器就不说了，一人一习惯，也可以Pycharm，也可以sublime，也可以直接文本编辑，反正能把Python运行起来就行**

## **一切就绪，开始‘合体’**
#### **介绍：**
&nbsp;

#### **接下来我们要把对话模型和WeChaty整理到一起**

&nbsp;

#### [WeChaty](https://wechaty.js.org/)：WeChaty是一款开源的微信机器人框架，它基于微信公开的API，对接口进行了一系列的封装，提供一系列简单的接口，然后开发者可以在其之上进行微信机器人的开发。若使用WeChaty需要申请token：免费申请链接[http://pad-local.com](http://pad-local.com)  申请后会有7天的使用时间，如果想要延长可以续费，或者访问官网：[WeChaty](https://wechaty.js.org/)
&nbsp;

#### [Plato2_en_base模型](https://www.paddlepaddle.org.cn/hubdetail?name=plato2_en_base)：PLATO2是一个超大规模生成式对话系统模型。它承袭了PLATO隐变量进行回复多样化生成的特性，能够就开放域话题进行流畅深入的聊天。这里使用的是PaddleHub的预训练模型，也就是不需要训练，下载安装就可以使用，需要注意的是这里是**英文**的对话，而且是小型的（大型的那个存储空间有点大，干不动），所以使用起来加上了翻译
&nbsp;



### **1.安装Python-WeChaty** 
&nbsp;

#### 我本地使用的是Python来对接GateWay（Docker内开启的服务），下载Python版WeChaty：[GitHub__python-wechaty-getting-started](https://github.com/wechaty/python-wechaty-getting-started)
&nbsp;

![python-wechaty下载](https://ai-studio-static-online.cdn.bcebos.com/ea63f5e5d0b64cf683a1f16ed384eb6d574f000764a2414ca03f920ac7b49c0f)
&nbsp;

#### 下载完成后解压ZIP
&nbsp;

#### **进入解压后的目录，安装关联包**
&nbsp;

```
cd /d python-wechaty-getting-started解压目录
pip install -r requirements.txt
```
&nbsp;

![](https://ai-studio-static-online.cdn.bcebos.com/25dec5e604a44e57bef63cbcb65a17797d2e2267ded14b9ca607787b1d986968)

&nbsp;

#### **安装完成后开始看Docker**

### **2. Docker**
&nbsp;

#### 这个是Docker拉取WeChaty镜像
&nbsp;
#### 我自己理解为下载安装WeChaty环境，第一次用Docker，不太懂，反正用下面这条语句就能够下载安装上WeChaty镜像（大约2G多）
#### 以管理员运行cmd：输入以下命令
```
docker pull wechaty/wechaty:latest
```
#### 等下载安装完是这个样子：
&nbsp;

![](https://ai-studio-static-online.cdn.bcebos.com/553644126a32401ab7391087e92e14e9a256b0ab9adb4175aa18da27009040a8)
&nbsp;


### **3. 设置环境变量，运行WeChaty**
&nbsp;

#### **还是刚才那个以管理员运行的CMD窗口输入以下命令：**
&nbsp;

```
set WECHATY_LOG=verbose
set WECHATY_PUPPET=wechaty-puppet-padlocal
set WECHATY_PUPPET_PADLOCAL_TOKEN=上面申请到的token
set WECHATY_PUPPET_SERVER_PORT=8080  
set WECHATY_TOKEN=80908090
```
#### **更改说明：**
- **WECHATY_PUPPET_PADLOCAL_TOKEN**  这个是上面申请到的**token码**

- **WECHATY_PUPPET_SERVER_PORT**    这个是**本地的端口**，可以写别的但要确保这个端口号没人用

- **WECHATY_TOKEN**             这个随便写，一会python会用得到

&nbsp;

#### **Docker运行WeChaty**
```
docker run -ti \
--name wechaty_puppet_service_token_gateway \
--rm \
-e WECHATY_LOG \
-e WECHATY_PUPPET \
-e WECHATY_TOKEN \
-e WECHATY_PUPPET_SERVER_PORT \
-e WECHATY_PUPPET_PADLOCAL_TOKEN \
-p "8080:8080" \
wechaty/wechaty:latest
```
&nbsp;

#### **上面这段是为了好看参数，cmd执行命令是不能分行的，要连成一条语句执行（-p 后面就是SERVER_PORT的端口号）**

&nbsp;

```
docker run -ti --name wechaty_puppet_service_token_gateway --rm  -e WECHATY_LOG -e WECHATY_PUPPET -e WECHATY_TOKEN -e WECHATY_PUPPET_SERVER_PORT -e WECHATY_PUPPET_PADLOCAL_TOKEN -p "8080:8080" wechaty/wechaty:latest
 ```
 
&nbsp;

#### **成功运行后会出现一个链接，如下图，复制到浏览器，扫码登录微信即可**
&nbsp;

![](https://ai-studio-static-online.cdn.bcebos.com/06d35160419b4077ac2279e5382973770ab10b0195fb40d59d1f76c5167e4e57)


![](https://ai-studio-static-online.cdn.bcebos.com/01d142aeee8a4f129661c74341b4eff494fae6685117447ab09ce26df03ffed8)



&nbsp;

#### **登录后，该CMD窗口就会一直运行着WeChaty，微信有什么消息也会在这显示出来**
&nbsp;

<table>
  <tr>
    <td ><center><img src="https://ai-studio-static-online.cdn.bcebos.com/fc06b8be20f746069eeffab8ae6924a791fc860c8ee64ef6a81b9e31544c5184" >图1</center></td>
    <td ><center><img src="https://ai-studio-static-online.cdn.bcebos.com/faec2ecffd8646389f6272a5eda66ee5d673690a8c8d4e3cb0063aed3af7678c" >图2</center></td>
  </tr>
</table>

### **到这里完成了一大半了，剩下的就是运行python**


```python
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

```

### 最后的样子：
![](https://ai-studio-static-online.cdn.bcebos.com/142eb7208d0f45ad819b7c6e5ec5e444bbfa87445f71496fa7dc624061d4346d)
&nbsp;

###  挺好的api被我完成了人工智障。。。。。
