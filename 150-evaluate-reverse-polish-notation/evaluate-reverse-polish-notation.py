class Solution:
    def evalRPN(self, tokens):
        stack = []

        for token in tokens:
            # если это число, просто кладем в стек
            if token not in "+-*/":
                stack.append(int(token))
            else:
                a = stack.pop()  # второи операнд
                b = stack.pop()  # первыи операнд

                # считаем в зависимости от оператора
                if token == "+":
                    stack.append(b + a)
                elif token == "-":
                    stack.append(b - a)
                elif token == "*":
                    stack.append(b * a)
                else:
                    # аккуратно делим, чтобы было как в условии
                    if b * a < 0:
                        stack.append(-(abs(b) // abs(a)))
                    else:
                        stack.append(b // a)

        # в конце в стеке останется ответ
        return stack[0]