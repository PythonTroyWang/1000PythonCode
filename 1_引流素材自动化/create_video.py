import time

from moviepy.editor import *
import random
import os
# 更换conda环境，解决IMAGEMAGICK环境问题
from moviepy.config import change_settings
change_settings({"IMAGEMAGICK_BINARY": "magick"})


def yl_video(video_path, wx_text):
    # 打开视频剪辑
    with VideoFileClip(video_path) as video_clip:
        # 裁剪前5秒并调整大小
        cropped_clip = video_clip.subclip(0, 3).resize((400, 255))

        # 创建文本剪辑
        # text_clip_1 = TextClip("薇", fontsize=30, color="white", font='Microsoft-YaHei-&-Microsoft-YaHei-UI')
        # text_clip_2 = TextClip("❤️", fontsize=30, color="white", font='Segoe-UI-Symbol')
        text_clip_3 = TextClip(f"{wx_text}", fontsize=30, color="white", font='Microsoft-YaHei-&-Microsoft-YaHei-UI')

        # 计算文本的宽度
        # text_width = sum([text_clip_1.w, text_clip_2.w, text_clip_3.w])
        text_width = sum([text_clip_3.w])

        # 计算文本居中的位置
        center_x = (cropped_clip.w - text_width) / 2

        # 设置每个文本剪辑的位置
        # text_clip_1 = text_clip_1.set_position((center_x, 100)).set_duration(5)
        # text_clip_2 = text_clip_2.set_position((center_x + text_clip_1.w, 100)).set_duration(5)
        # text_clip_3 = text_clip_3.set_position((center_x + text_clip_1.w + text_clip_2.w, 100)).set_duration(5)
        text_clip_3 = text_clip_3.set_position((center_x, 180)).set_duration(3)

        # arrow_clip = VideoFileClip("assets/gif/arrow.gif")
        # arrow_clip = arrow_clip.resize((50, 50))
        #
        # looped_arrow_clip = arrow_clip.fx(vfx.loop, duration=5)
        #
        # # 设置 GIF 图像的位置
        # looped_arrow_clip = looped_arrow_clip.set_position((center_x, 10)).set_duration(5)

        # 将视频剪辑和文本剪辑组合在一起
        # composite_clip = CompositeVideoClip([cropped_clip, text_clip_1, text_clip_2, text_clip_3, looped_arrow_clip])
        # composite_clip = CompositeVideoClip([cropped_clip, text_clip_3, looped_arrow_clip])
        composite_clip = CompositeVideoClip([cropped_clip, text_clip_3])

        # 创建保存图片的文件夹
        output_directory = "output_videos"
        if not os.path.exists(output_directory):
            os.makedirs(output_directory)

        current_timestamp = int(time.time())
        # 将组合后的视频剪辑写入文件
        output_path = os.path.join(output_directory, f"{wx_text}_{current_timestamp}.mp4")
        composite_clip.write_videofile(output_path, codec="libx264")

        # 关闭视频剪辑
        # arrow_clip.close()
        cropped_clip.close()
        # text_clip_1.close()
        # text_clip_2.close()
        text_clip_3.close()
        # looped_arrow_clip.close()
        composite_clip.close()


def get_video_template():
    template_dir = 'assets/videos'
    template_files = []
    for root, dirs, files in os.walk(template_dir):
        for file in files:
            template_files.append(os.path.join(root, file))
    return template_files


def get_txt_wx_account():
    wx_accounts = []
    with open('conf/wx_accounts.txt', 'r') as file:
        for line in file.readlines():
            wx_accounts.append(line.strip())
    return wx_accounts


if __name__ == '__main__':
    wx_array = get_txt_wx_account()
    my_array = get_video_template()

    # 遍历微信账号数组，同时使用不重复的随机模板
    for item_text in wx_array:
        for template in my_array:
            yl_video(template, item_text)
            print(f"已为您生成微信号为 {item_text} 的引流视频！")
