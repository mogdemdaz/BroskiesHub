class Calculator:
    @staticmethod
    def addition(a, b): return a + b
    @staticmethod
    def subtraction(a, b): return a - b
    @staticmethod
    def multiplication(a, b): return a * b
    @staticmethod
    def division(a, b): return a / b if b != 0 else float('infinity')

class RunCalculator:
    @staticmethod
    def run():
        first = input("Enter a number (or 'exit' to quit): ")
        if first.lower() == "exit":
            print("Goodbye!")
            return
        total = float(first)

        while True:
            operation = input("Operation (+, -, *, /) or 'exit' to quit: ")
            if operation.lower() == "exit":
                break
            if operation not in ['+', '-', '*', '/']:
                print("Invalid operation.")
                continue

            nxt = input("Enter a number (or 'exit' to quit): ")
            if nxt.lower() == "exit":
                break
            num = float(nxt)

            if operation == '+':
                total = Calculator.addition(total, num)
            elif operation == '-':
                total = Calculator.subtraction(total, num)
            elif operation == '*':
                total = Calculator.multiplication(total, num)
            elif operation == '/':
                total = Calculator.division(total, num)

            print("total:", total)


if __name__ == '__main__':
    calculator = RunCalculator()
    calculator.run()


