from PIL import Image, ImageDraw, ImageFont

font60 = ImageFont.truetype("font/Alibaba-PuHuiTi-Regular.ttf", size=60)
font41 = ImageFont.truetype("font/Alibaba-PuHuiTi-Regular.ttf", size=41)
font39R = ImageFont.truetype("font/Alibaba-PuHuiTi-Regular.ttf", size=39)
font39M = ImageFont.truetype("font/Alibaba-PuHuiTi-Medium.ttf", size=39)
font30 = ImageFont.truetype("font/Alibaba-PuHuiTi-Regular.ttf", size=30)
# add 方正楷体简体
font25 = ImageFont.truetype("font/stkaiti.ttf", size=25)


def img_generate(data, text):
    # 打开模板
    img = Image.open('img/bg.jpg')
    draw = ImageDraw.Draw(img)
    # 开始绘制
    draw_text(draw, data, text)
    # 保存图片
    img.save('./result/展示图/' + str(data[1]['代码']) + '.jpg', quality=95)


def img_generate2(data, array, i, text, name, trend):
    # 打开模板
    img = Image.open('img/bg.jpg')
    draw = ImageDraw.Draw(img)
    # 开始绘制
    draw_text2(draw, data, array, i, text, trend)
    if name == 0:
        # 保存图片（名称为股票代码）
        img.save('./result/商品图-股票代码/' + str(data[1]['代码']) + '.jpg', quality=95)
    if name == 1:
        # 保存图片（名称排位号）
        img.save('./result/商品图-排位/' + str(i) + '.jpg', quality=95)


def draw_text(draw, data, text):
    # 编号
    draw.text((8, 176), str(data[1]['代码']), fill='yellow', font=font60)
    # 名称
    draw.text((228, 176), str(data[1]['名称_x']), fill='yellow', font=font60)
    # 主营
    draw.text((500, 180), u'主营:' + str(data[1]['细分行业'])[0:4], fill='white', font=font41)
    # 注册资本
    draw.text((500, 253), u'注册:' + str(data[1]['流通股(亿)'])[0:5], fill='white', font=font41)
    # 亿元单位
    draw.text((706, 253), u'亿元', fill='white', font=font41)
    # 地址
    draw.text((8, 320), data[1]['地区'], fill='black', font=font41)
    # 上市日期
    draw.text((500, 320), u'上市:' + str(data[1]['上市日期']), fill='white', font=font41)
    # 综合排位
    draw.text((9, 449), u'沪深综合排0000位', fill='red', font=font39R)
    # 行情
    draw.text((357, 449), u'0000行情', fill='red', font=font39R)
    # 大盘趋势
    draw.text((545, 449), u'大盘趋势0000', fill='red', font=font39R)
    # 比上证B指
    draw.text((80, 570), u'00', fill='red', font=font39M)
    draw.text((35, 623), u'比上证B指', fill='red', font=font30)
    # 比上证指数
    draw.text((278, 570), u'00', fill='red', font=font39M)
    draw.text((224, 623), u'比上证指数', fill='red', font=font30)
    # 比深证成指
    draw.text((473, 570), u'00', fill='red', font=font39M)
    draw.text((420, 623), u'比深证成指', fill='red', font=font30)
    # 比深证B指
    draw.text((670, 570), u'00', fill='red', font=font39M)
    draw.text((625, 623), u'比深证B指', fill='red', font=font30)

    # add tips
    width, height = font25.getsize(text)
    draw.text((800 - width - 18, 800 - height - 25), text, fill='white', font=font25)


def draw_text2(draw, data, array, i, text, trend):
    # 编号
    draw.text((8, 176), str(data[1]['代码']), fill='yellow', font=font60)
    # 名称
    draw.text((228, 176), str(data[1]['名称_x']), fill='yellow', font=font60)
    # 主营
    draw.text((500, 180), u'主营:' + str(data[1]['细分行业'])[0:4], fill='white', font=font41)
    # 注册资本
    draw.text((500, 253), u'注册:' + str(data[1]['流通股(亿)'])[0:5], fill='white', font=font41)
    # 亿元单位
    draw.text((706, 253), u'亿元', fill='white', font=font41)
    # 地址
    draw.text((8, 320), data[1]['地区'], fill='black', font=font41)
    # 上市日期
    draw.text((500, 320), u'上市:' + str(data[1]['上市日期']), fill='white', font=font41)
    # 综合排位
    draw.text((9, 449), u'沪深综合排' + str(i).zfill(4) + '位', fill='red', font=font39R)
    # 大盘趋势
    draw.text((553, 449), u'大盘趋势' + trend, fill='red', font=font39R)

    shangzhengBzhi = calcData(data[1]['BB-T'], array[0])
    shangzhengzhishu = calcData(data[1]['BB-T'], array[1])
    shenzhenchegnzhi = calcData(data[1]['BB-T'], array[2])
    shenzhenBzhi = calcData(data[1]['BB-T'], array[3])

    # 比上证B指
    draw.text((85, 570), shangzhengBzhi, fill='red', font=font39M)
    draw.text((35, 623), u'比上证B指', fill='red', font=font30)
    # 比上证指数
    draw.text((283, 570), shangzhengzhishu, fill='red', font=font39M)
    draw.text((224, 623), u'比上证指数', fill='red', font=font30)
    # 比深证成指
    draw.text((478, 570), shenzhenchegnzhi, fill='red', font=font39M)
    draw.text((420, 623), u'比深证成指', fill='red', font=font30)
    # 比深证B指
    draw.text((675, 570), shenzhenBzhi, fill='red', font=font39M)
    draw.text((625, 623), u'比深证B指', fill='red', font=font30)

    hangqing = ''
    if shangzhengBzhi == '强' and shangzhengzhishu == '强' and shenzhenchegnzhi == '强' and shenzhenBzhi == '强':
        hangqing = '强势行情'
    elif shangzhengBzhi == '弱' and shangzhengzhishu == '弱' and shenzhenchegnzhi == '弱' and shenzhenBzhi == '弱':
        hangqing = '弱势行情'
    else:
        hangqing = '一般行情'

    # 行情
    draw.text((370, 449), hangqing, fill='red', font=font39R)
    # add tips
    width, height = font25.getsize(text)
    draw.text((800 - width - 18, 800 - height - 25), text, fill='white', font=font25)


def calcData(data, compare_data):
    if data > compare_data:
        ret = '强'
    elif data < compare_data:
        ret = '弱'
    else:
        ret = '同'
    return ret
