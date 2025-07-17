import qrcode

# 目标 URL
url = "https://mwf-max.github.io/"

# 生成二维码
qr = qrcode.make(url)

# 保存为图片
qr.save("CPA_qrcode.png")

print("二维码已保存为 CPA_qrcode.png")
