class BigInt:
    def __init__(self, value: str):
        if value[0] == '-':
            self.sign = -1
            value = value[1:]
        else:
            self.sign = 1
        self.digits = list(map(int, value))
        self.digits.reverse()

    def __str__(self):
        result = ''.join(map(str, reversed(self.digits)))
        return f"{'-' if self.sign < 0 else ''}{result}"

    def __add__(self, other):
        if self.sign == other.sign:
            return self._add_magnitude(other)
        if self._compare_magnitude(other) >= 0:
            return self._subtract_magnitude(other)
        result = other._subtract_magnitude(self)
        result.sign *= -1
        return result

    def __sub__(self, other):
        other_copy = BigInt(str(other))
        other_copy.sign *= -1
        return self.__add__(other_copy)

    def __mul__(self, other):
        result = BigInt("0")
        for i, digit in enumerate(other.digits):
            temp = self._multiply_by_digit(digit)
            temp.digits = [0] * i + temp.digits
            result = result + temp
        result.sign = self.sign * other.sign
        return result

    def __truediv__(self, other):
        if str(other) == "0":
            raise ValueError("Division by zero")
        return self._divide(other)[0]

    def __mod__(self, other):
        if str(other) == "0":
            raise ValueError("Modulo by zero")
        return self._divide(other)[1]

    def __pow__(self, other):
        if str(other) == "0":
            return BigInt("1")
        if str(other) == "1":
            return self
        result = BigInt("1")
        base = BigInt(str(self))
        power = BigInt(str(other))
        while str(power) != "0":
            if power.digits[0] % 2 == 1:
                result *= base
            base *= base
            power = power._divide_by_two()
        return result

    def factorial(self):
        if self.sign < 0:
            raise ValueError("Factorial of a negative number is undefined")
        result = BigInt("1")
        n = BigInt(str(self))
        while str(n) != "0":
            result *= n
            n -= BigInt("1")
        return result

    def _add_magnitude(self, other):
        carry = 0
        result = BigInt("0")
        result.digits = []
        for i in range(max(len(self.digits), len(other.digits))):
            digit_sum = (self.digits[i] if i < len(self.digits) else 0) + \
                        (other.digits[i] if i < len(other.digits) else 0) + carry
            carry = digit_sum // 10
            result.digits.append(digit_sum % 10)
        if carry:
            result.digits.append(carry)
        result.sign = self.sign
        return result

    def _subtract_magnitude(self, other):
        carry = 0
        result = BigInt("0")
        result.digits = []
        for i in range(len(self.digits)):
            digit_diff = self.digits[i] - \
                         (other.digits[i] if i < len(other.digits) else 0) - carry
            carry = 1 if digit_diff < 0 else 0
            result.digits.append(digit_diff % 10)
        while len(result.digits) > 1 and result.digits[-1] == 0:
            result.digits.pop()
        result.sign = self.sign
        return result

    def _multiply_by_digit(self, digit):
        carry = 0
        result = BigInt("0")
        result.digits = []
        for d in self.digits:
            temp = d * digit + carry
            carry = temp // 10
            result.digits.append(temp % 10)
        if carry:
            result.digits.append(carry)
        return result

    def _compare_magnitude(self, other):
        if len(self.digits) != len(other.digits):
            return len(self.digits) - len(other.digits)
        for a, b in zip(reversed(self.digits), reversed(other.digits)):
            if a != b:
                return a - b
        return 0

    def _divide(self, other):
        if str(other) == "0":
            raise ValueError("Division by zero")
        quotient = BigInt("0")
        remainder = BigInt("0")
        for digit in reversed(self.digits):
            remainder.digits.insert(0, digit)
            quotient_digit = 0
            while remainder._compare_magnitude(other) >= 0:
                remainder = remainder._subtract_magnitude(other)
                quotient_digit += 1
            quotient.digits.insert(0, quotient_digit)
        while len(quotient.digits) > 1 and quotient.digits[-1] == 0:
            quotient.digits.pop()
        quotient.sign = self.sign * other.sign
        remainder.sign = self.sign
        return quotient, remainder

    def _divide_by_two(self):
        carry = 0
        result = BigInt("0")
        result.digits = []
        for digit in reversed(self.digits):
            current = carry * 10 + digit
            result.digits.append(current // 2)
            carry = current % 2
        result.digits.reverse()
        while len(result.digits) > 1 and result.digits[-1] == 0:
            result.digits.pop()
        return result


def repl():
    print("Welcome to the Arbitrary-Precision Integer Calculator!")
    print("Enter commands like 'add 123 456' or 'mul 10 20'")
    print("Supported operations: add, sub, mul, div, mod, pow, fact")
    while True:
        try:
            command = input(">> ").strip().split()
            if len(command) == 0:
                continue
            if command[0] == "exit":
                break
            op = command[0]
            args = command[1:]
            if op == "fact" and len(args) == 1:
                print(BigInt(args[0]).factorial())
            elif len(args) == 2:
                a = BigInt(args[0])
                b = BigInt(args[1])
                if op == "add":
                    print(a + b)
                elif op == "sub":
                    print(a - b)
                elif op == "mul":
                    print(a * b)
                elif op == "div":
                    print(a / b)
                elif op == "mod":
                    print(a % b)
                elif op == "pow":
                    print(a ** b)
                else:
                    print("Unsupported operation")
            else:
                print("Invalid command")
        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    repl()


