import pyqrcode
link = "https://cocoabytes.substack.com/p/hiya-its-cocoabytes"
qr_code = pyqrcode.create(link)
qr_code.png('cocoabyes_qr.png', scale=6, module_color=[0, 0, 0, 128], background=[0xff, 0xff, 0xcc])
qr_code.show()
