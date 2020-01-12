# -*- coding: utf-8 -*-
class Callback(object):

    def __init__(self, callback):
        self.callback = callback

    def PinVerified(self, pin):
        self.callback("PINコード(" + pin + ")を2分以内にスマートフォンのLINEで入力して下さい。")

    def QrUrl(self, url, showQr=True):
        if showQr:
            notice='くか、QRコードをスキャンし'
        else:
            notice='い'
        self.callback('スマートフォンのLINEで2分以内にこのリンクを開' + notice + 'て下さい\n' + url)
        if showQr:
            try:
                import pyqrcode
                url = pyqrcode.create(url)
                self.callback(url.terminal('green', 'white', 1))
            except:
                pass

    def default(self, str):
        self.callback(str)
