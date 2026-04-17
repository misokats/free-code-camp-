#数値を表す文字列と、2から36までの整数基数が与えられたとき、その数値がその基数において有効かどうかを判定する。
#文字列には整数、大文字、小文字を含めることができます。
#小数点以下の大文字・小文字は区別しない。
#基数は2～36の任意の数で構いません。
#数値が有効であるとは、その数値に含まれるすべての文字が、指定された基数における有効な数字である場合をいう。
#基数に使用できる有効な数字の例：
#ベース2：0-1
#ベース8：0-7
#10進法：0～9
#ベース16：0-9およびAF
#ベース36：0-9とAZ

#base:基数2~36
#num_str:数値を表す文字列
#digit_value:num_strを一文字ずつ数値に変換した値

def is_valid_for_base(num_str, base):
    
    # 1. 基数の範囲チェック (2〜36)
    if not (2 <= base <= 36):
        return False
    
    # 2. 文字列を大文字に統一
    num_str = num_str.upper()
    
    # 3. 1文字ずつチェック
    for char in num_str:
        # 数字 (0-9) の場合
        if '0' <= char <= '9':
            digit_value = ord(char) - ord('0')
        # 英字 (A-Z) の場合
        elif 'A' <= char <= 'Z':
            digit_value = ord(char) - ord('A') + 10
        # それ以外の記号などは無効
        else:
            return False
        
        # 取り出した値が基数以上なら、その基数では表現できない
        if digit_value >= base:
            return False
            
    return True

# --- テストケース ---
test_cases = [
    ("1011", 2),    # True: 2進数で1011は有効
    ("102", 2),     # False: 2進数に2は存在しない
    ("AF1", 16),    # True: 16進数でAF1は有効
    ("G1", 16),     # False: 16進数にG(16)は存在しない
    ("Z", 36),      # True: 36進数ならZ(35)までOK
    ("apple", 36)   # True: 36進数ならa-zはすべて有効
]

for s, b in test_cases:
    result = is_valid_for_base(s, b)
    print(f"文字列: '{s}', 基数: {b} => 有効か: {result}")