def caesarClipher(message):
    PLAIN = message
    execludeStr = "{}_"
    KEY = 3
    result = ""

    for c in message :
        # 除外する文字列ならば変換せず、そのままにする
        if execludeStr.find(c) != -1 :
            result = result + c
            continue

        # 復号する処理
        if ord('a') <= ord(c) <= ord('z') :
            result = result + chr(abs(((ord(c) - KEY - ord('a')) % 26)) + ord('a'))
        else :
            result = result + chr(abs(((ord(c) - KEY - ord('A')) % 26)) + ord('A'))

    print(result)

if __name__ == '__main__':
    message = input('>>')
    caesarClipher(message)