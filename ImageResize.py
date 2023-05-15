from PIL import Image
from tkinter import filedialog
import tkinter as tk
import random
import time

root = tk.Tk()

print("画像選択してください。")
filename = filedialog.askopenfilename(
    title = "画像ファイルを開く",
    filetypes = [("Image file", ".png .jpg"), ("PNG", ".png"), ("JPEG", ".jpg")],
    initialdir = "/" 
    )

root.mainloop()


def resize_image(image_path, output_path, max_resolution):
    null = ''
    if filename == null:
        print('画像が選択されていないので再度選択お願いします。')
        print('5秒後にプログラムを終了します。')
        print('再度変換する場合は開きなおしてください。')
        time.sleep(5)
        return 0
    else:
        pass
    
    # 画像を開く
    image = Image.open(filename).convert('RGB')

    # 元の解像度を取得
    width, height = image.size

    # 解像度の比率を計算
    if width > height:
        ratio = max_resolution / width
    else:
        ratio = max_resolution / height

    # 新しい解像度を計算
    new_width = int(width * ratio)
    new_height = int(height * ratio)

    # 画像のリサイズ
    resized_image = image.resize((new_width, new_height))

    # リサイズされた画像を保存
    resized_image.save(output_path)
    print('画像の生成が完了しました')

try:
    # 画像のパスと保存先パスを指定
    image_path = filename

    # 桁数
    digit = 6

    output_name = random.randrange(10**(digit-1),10**digit)
    output_path =  'output_image/' + str(output_name) + '.jpg'

    print("最大解像度を入力してください。")
    input_data = input() 
    int_input = int(input_data)
    
    if int_input == 0:
        print("0以外の数値を入力してください。")
        print('5秒後にプログラムを終了します。')
        print('再度変換する場合は開きなおしてください。')
        time.sleep(5)
        exit()
    else:
        pass
    
    # 最大解像度を指定
    max_resolution = int_input

    # 画像の解像度を下げて保存
    resize_image(image_path, output_path, max_resolution)
    
except ValueError:
    # ValueError例外を処理するコード
    print('数字以外が入力されました。数字のみを入力してください。')
    print('5秒後にプログラムを終了します。')
    print('再度変換する場合は開きなおしてください。')
    time.sleep(5)
    exit()
except KeyboardInterrupt:
    exit()
else:
    pass