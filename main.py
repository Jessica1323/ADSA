def convert_base(num, base):
    """将一个十进制数转换为指定的基数"""
    if num == 0:
        return "0"
    digits = []
    while num:
        digits.append(int(num % base))
        num //= base
    return ''.join(str(x) for x in digits[::-1])

def karatsuba(x, y):
    """Karatsuba 乘法算法实现"""
    if x < 10 or y < 10:
        return x * y

    n = max(len(str(x)), len(str(y)))
    m = n // 2

    high1, low1 = divmod(x, 10**m)
    high2, low2 = divmod(y, 10**m)

    z0 = karatsuba(low1, low2)
    z1 = karatsuba((low1 + high1), (low2 + high2))
    z2 = karatsuba(high1, high2)

    return (z2 * 10**(2*m)) + ((z1 - z2 - z0) * 10**m) + z0

def main():
    # 输入格式：I1 I2 B
    input_line = input("Enter I1 I2 B: ")
    I1_str, I2_str, B_str = input_line.split()
    
    # 将输入的 I1 和 I2 从进制 B 转换为十进制
    B = int(B_str)
    I1 = int(I1_str, B)
    I2 = int(I2_str, B)

    # 使用学校方法计算加法
    sum_result = I1 + I2

    # 使用 Karatsuba 算法计算乘法
    product_result = karatsuba(I1, I2)

    # 计算商（向下取整）
    quotient_result = I1 // I2

    # 将结果转换回基数 B
    sum_result_base_b = convert_base(sum_result, B)
    product_result_base_b = convert_base(product_result, B)
    quotient_result_base_b = convert_base(quotient_result, B)

    # 输出结果，结果之间用空格分隔
    print(f"{sum_result_base_b} {product_result_base_b} {quotient_result_base_b}")


