import  urllib.request

# 下载网页
url_page='http://www.baidu.com'

# url 代表下载的路径 filename文件的名字
# urllib.request.urlretrieve(url_page,'baidu.html')
#下载图片
url_img='https://img0.baidu.com/it/u=644930533,687560765&fm=253&fmt=auto&app=120&f=JPEG?w=500&h=649'
# urllib.request.urlretrieve(url_img,filename='林允儿.jpg')

#下载视频
url_video='https://vd3.bdstatic.com/mda-mi51pj6xb2dtdupc/fhd/cae_h264_nowatermark/1630890877645404018/mda-mi51pj6xb2dtdupc.mp4?v_from_s=hkapp-haokan-shunyi&auth_key=1630985096-0-0-ecacbb4443f473983504388aaf7922c5&bcevod_channel=searchbox_feed&pd=1&pt=3&abtest=3000186_1'

urllib.request.urlretrieve(url_video, filename='视频下载.mp4')