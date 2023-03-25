
class Value:
    def __init__(self, val, is_number=None):
        if is_number is None: self.is_num = True if isinstance(val, (int, float)) else False
        else: self.is_num = is_number
        self.val = val

    def make_operation(self, Val2, sign):
        if self.is_num and Val2.is_num:
            if sign == '+': res = self.val + Val2.val
            elif sign == '-': res = self.val - Val2.val
            elif sign == '*': res = self.val * Val2.val
            else: res = self.val / Val2.val
            return Value(res, True)
        else:
            v1 = str(self.val) if self.is_num else '(' + self.val + ')'
            v2 = str(Val2.val) if Val2.is_num else '(' + Val2.val + ')'
            return Value(v1 + sign + v2, False)

def get_monkey_val(m_dict, m):
    val = m_dict[m]
    if isinstance(val, Value):
        return val
    else:
        v1, sign, v2 = get_monkey_val(m_dict, val[0]), val[1], get_monkey_val(m_dict, val[2])
        return v1.make_operation(v2, sign)

def solve_monkey_equation(eq, val):
    if eq == 'x':
        return val

    if eq[0] == '(':
        val_on_right = True
        i = -1
        while eq[i] != ')': i -= 1
        sign, val_ch, new_eq = eq[i + 1], int(float(eq[i + 2:])), eq[1:i]
    else:
        val_on_right = False
        i = 0
        while eq[i] != '(': i += 1
        sign, val_ch, new_eq = eq[i - 1], int(float(eq[:i - 1])), eq[i + 1:-1]

    if sign == '+': res = val - val_ch
    elif sign == '-': res = val + val_ch if val_on_right else val_ch - val
    elif sign == '*': res = val / val_ch
    else: res = val * val_ch if val_on_right else val_ch / val

    return solve_monkey_equation(new_eq, res)

def main():
    data = [el.split() for el in txt_into_array()]
    monkey_dict = {el[0][:-1]: (el[1:] if len(el[1:]) > 1 else Value(int(el[-1]), True)) for el in data}
    monkey_dict['humn'] = Value('x', False)
    eq = get_monkey_val(monkey_dict, monkey_dict['root'][0]).val
    val = get_monkey_val(monkey_dict, monkey_dict['root'][-1]).val
    print(solve_monkey_equation(eq, val))


