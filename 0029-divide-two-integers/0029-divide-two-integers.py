class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # 1. Handle 32-bit signed integer overflow
        MAX_INT = 2147483647   # 2^31 - 1
        MIN_INT = -2147483648  # -2^31
        if dividend == MIN_INT and divisor == -1:
            return MAX_INT

        # 2. Check if the result should be negative
        is_negative = (dividend < 0) != (divisor < 0)

        # 3. Convert both numbers to positive
        a = abs(dividend)
        b = abs(divisor)
        quotient = 0

        # 4. Subtract largest doubled multiples of divisor
        while a >= b:
            temp_divisor = b
            multiple = 1
            while a >= (temp_divisor << 1):
                temp_divisor <<= 1
                multiple <<= 1
            
            a -= temp_divisor
            quotient += multiple

        # 5. Apply the sign and return
        return -quotient if is_negative else quotient
