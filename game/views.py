from django.http import HttpResponse

def index(request):
    line1 = '<h1 style="text-align: center">术士之战</h1>'
    line3 = '<a href="/play/">游戏页面</a><br>'
    line2 = '<img src="https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fc-ssl.duitang.com%2Fuploads%2Fitem%2F201608%2F27%2F20160827052725_AdQKx.thumb.1000_0.png&refer=http%3A%2F%2Fc-ssl.duitang.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=auto?sec=1676880248&t=d2db4929464fd8822edf28b4752fb74c" width = 1200 >'
    return HttpResponse(line1 + line3 + line2)

def play(request):
    line1 = '<h1 style="text align: center"> 游戏界面</h1>'
    line2 = '<a href="/">主页面</a><br>'
    line3 = '<img src="https://img0.baidu.com/it/u=2457054660,3698959532&fm=253&fmt=auto&app=138&f=JPEG?w=500&h=281" width = 1200 >'
    return HttpResponse(line1 + line2 + line3)
