
import frida
import sys
from frida import ServerNotRunningError


src = """
Java.perform(function() {
    var array_list = Java.use("java.util.ArrayList");
    var ApiClient = Java.use('com.android.org.conscrypt.TrustManagerImpl');
    ApiClient.checkTrustedRecursive.implementation = function(a1, a2, a3, a4, a5, a6) {
        console.log('Bypassing SSL Pinning');
        return array_list.$new();
    }
}, 0);
"""


def message(message, data):
    if message["type"] == 'send':
        print(u"[*] {0}".format(message['payload']))
    else:
        print("msg:", message)


def get_device():
    try:
        device = frida.get_usb_device(5)
        print("已连接USB设备")
        return device
    except ServerNotRunningError:
        print("连接USB设备失败，尝试网络连接...")
        try:
            device = frida.get_remote_device()
            print("已连接远程设备")
            return device
        except ServerNotRunningError:
            print("连接远程设备失败")
            raise


if __name__ == "__main__":
    session = get_device().attach("com.jingdong.app.mall")
    script = session.create_script(src)
    script.on("message", message)
    script.load()
    sys.stdin.read()
