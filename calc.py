class Calculator_app(object):
    def __init__(self):
        self.result = 0
        self.left = ''
        self.right = ''
        self.math_operator_selected = False
        self.math_operator = None

    def computation(self):
        if self.math_operator == '+':
            if self.right == '' or self.left == '':
                pass
            else:
                self.result = int(self.left) + int(self.right)
                print(self.result)
                self.clear_selections()
        else:
            pass

    def typing(self, digit):
        if self.math_operator_selected:
            self.left += str(digit)
            print(digit)
        else:
            self.right += str(digit)
            print(self.right)

    def select_math_operator(self, operator):
        self.math_operator = operator
        self.math_operator_selected = True

    def clear_selections(self):
        self.result = 0
        self.left = 0
        self.right = 0
        self.math_operator_selected = False
        self.math_operator = None
