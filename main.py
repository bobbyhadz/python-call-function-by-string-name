# Call a function by a String name in Python

import example_module

func = getattr(example_module, 'example_function')
print(func('ab', 'cd'))  # 👉️ 'abcd'