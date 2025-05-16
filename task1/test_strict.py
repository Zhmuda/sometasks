import unittest
from typing import Union

class TestStrictDecorator(unittest.TestCase):
    def test_correct_types(self):
        @strict
        def sum_two(a: int, b: int) -> int:
            return a + b
        
        self.assertEqual(sum_two(1, 2), 3)
    
    def test_incorrect_positional_arg(self):
        @strict
        def sum_two(a: int, b: int) -> int:
            return a + b
        
        with self.assertRaises(TypeError) as context:
            sum_two(1, 2.4)
        self.assertEqual(str(context.exception), "Argument 'b' must be <class 'int'>, not <class 'float'>")
    
    def test_incorrect_keyword_arg(self):
        @strict
        def greet(name: str, age: int) -> str:
            return f"{name} is {age} years old"
        
        with self.assertRaises(TypeError) as context:
            greet(name="Alice", age="25")
        self.assertEqual(str(context.exception), "Argument 'age' must be <class 'int'>, not <class 'str'>")
    
    def test_mixed_args(self):
        @strict
        def mixed(a: int, b: float, c: str) -> tuple:
            return (a, b, c)
        
        self.assertEqual(mixed(1, 2.0, "3"), (1, 2.0, "3"))
        
        with self.assertRaises(TypeError):
            mixed(1.0, 2.0, "3")
        with self.assertRaises(TypeError):
            mixed(1, 2, "3")
    
    def test_no_annotations(self):
        @strict
        def no_annotations(a, b):
            return a + b
        
        self.assertEqual(no_annotations(1, 2), 3)
        self.assertEqual(no_annotations("a", "b"), "ab")
    
    def test_return_type_not_checked(self):
        @strict
        def returns_wrong_type(a: int) -> str:
            return a
        
        self.assertEqual(returns_wrong_type(123), 123)
    
    def test_union_types(self):
        @strict
        def union_arg(a: Union[int, float]) -> int:
            return int(a)
        
        self.assertEqual(union_arg(5), 5)
        self.assertEqual(union_arg(5.0), 5)
        
        with self.assertRaises(TypeError):
            union_arg("5")
    
    def test_kwargs_only(self):
        @strict
        def kwargs_only(*, a: int, b: str) -> str:
            return f"{a}{b}"
        
        self.assertEqual(kwargs_only(a=1, b="2"), "12")
        
        # Проверка ошибок
        with self.assertRaises(TypeError):
            kwargs_only(a="1", b="2")
        with self.assertRaises(TypeError):
            kwargs_only(a=1, b=2)


if __name__ == '__main__':
    unittest.main()
