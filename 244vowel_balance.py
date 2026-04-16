#与えられた文字列において、前半部分に含まれる母音の数と、後半部分に含まれる母音の数が等しいかどうかを判定してください。
#文字列にはあらゆる文字が含まれる可能性があります。
#大文字・小文字を問わず、「a, e, i, o, u」を母音とみなします。
#文字列の長さが奇数の場合は、中央の文字を無視してください。

def is_balanced(s):
    #母音の集合を定義
    vowels = set("aeuioAEUIO")

    #文字列の長さを半分にする
    n = len(s)
    half_len = n//2

    #スライスで文字列の前半と後半をそれぞれ取得
    first_half = s[:half_len] #0から文字数/2-1まで
    second_half = s[n-half_len:] #文字列の後ろから半分まで

    #母音数をカウント
    def count_vowels(text):
        return sum(1 for char in text if char in vowels)

    #文字列の前半と後半の母音数がイコールか？
    return count_vowels(first_half) == count_vowels(second_half)   
