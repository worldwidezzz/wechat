from core.server.wxauthorize import WxSignatureHandler
import tornado.web

'''web解析规则'''

urlpatterns = [
    (r'/wxsignature', WxSignatureHandler),  # 微信签名
]
