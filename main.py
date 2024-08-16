def convert_base(num, base):
    """将一个十进制数转换为指定的基数"""
    if num == 0:
        return "0"
    digits = []
    while num:
        digits.append(int(num % base))
        num //= base
    return ''.join(str(x) for x in digits[::-1])

def school_addition(I1_str, I2_str, B):
    """在基数B下进行逐位加法"""
    max_len = max(len(I1_str), len(I2_str))
    I1_str = I1_str.zfill(max_len)
    I2_str = I2_str.zfill(max_len)
    
    carry = 0
    result = []
    
    for i in range(max_len - 1, -1, -1):
        digit_sum = int(I1_str[i], B) + int(I2_str[i], B) + carry
        carry = digit_sum // B
        result.append(digit_sum % B)
    
    if carry:
        result.append(carry)
    
    result.reverse()
    return ''.join(str(digit) for digit in result)

def karatsuba(x, y):
    """Karatsuba 乘法算法实现"""
    # 基本情况，小于10的数字直接相乘
    if x < 10 or y < 10:
        return x * y

    # 计算数字的长度
    n = max(len(str(x)), len(str(y)))
    m = n // 2

    # 将 x 和 y 分解为两部分
    high1, low1 = divmod(x, 10**m)
    high2, low2 = divmod(y, 10**m)

    # 递归计算三个子乘积
    z0 = karatsuba(low1, low2)
    z1 = karatsuba((low1 + high1), (low2 + high2))
    z2 = karatsuba(high1, high2)

    # 合并结果
    return (z2 * 10**(2*m)) + ((z1 - z2 - z0) * 10**m) + z0

def main():
    # 输入格式：I1 I2 B
    input_line = input().strip()
    I1_str, I2_str, B_str = input_line.split()
    
    # 解析输入的基数 B 和将数字 I1, I2 从 B 进制转换为十进制
    B = int(B_str)
    I1 = int(I1_str, B)
    I2 = int(I2_str, B)

    # 使用学校方法计算加法
    sum_result_base_b = school_addition(I1_str, I2_str, B)

    # 使用 Karatsuba 算法计算乘法
    product_result = karatsuba(I1, I2)
    product_result_base_b = convert_base(product_result, B)

    # 计算商（向下取整）
    quotient_result = I1 // I2
    quotient_result_base_b = convert_base(quotient_result, B)

    # 打印最终结果
    print(f"{sum_result_base_b} {product_result_base_b} {quotient_result_base_b}")

if __name__ == "__main__":
    main()
