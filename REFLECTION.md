# Part B: Reflection

## 1. Tests and Production Code

I wrote 8 tests in Part A. My `kitchen.py` has 38 non-blank lines of production code. The ratio is about 1 test per 4.75 production-code lines.

## 2. The Longest Red Bar

The longest red bar was mixed-unit addition. I needed to understand how `Sum`, `reduce()`, and conversion rates worked together.

## 3. TDD Techniques

I used **Fake It** by returning `grams(500)` in `plus()`. I used **Triangulation** by testing addition with the same and different units. I used **Obvious Implementation** for multiplication. These choices helped me develop the code step by step.

## 4. Remaining Test List

The combined addition and multiplication test and `__hash__` are still unfinished. I would implement the combined operation next and leave `__hash__` out if it is not required. I also need to improve the test that checks whether multiplication changes the original quantity.

## 5. Quantity.reduce

I might not have designed `Quantity.reduce()` this way from the beginning. TDD helped me discover that both `Quantity` and `Sum` needed to support reduction.

## 6. Part 0 vs. Part A

In Part 0, I wrote tests after the code, so I mainly checked the implementation. In Part A, writing tests first helped me understand the requirements and shape the design. The addition tests especially helped me decide to create `Sum` and use conversion rates.