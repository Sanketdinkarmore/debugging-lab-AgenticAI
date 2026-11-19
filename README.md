# Debugging Lab

A Python debugging practice lab with a shopping cart example.

## Files

- `cart.py` — Shopping cart implementation with intentional bugs for debugging practice
- `test_cart.py` — Unit tests for the cart functionality
- `debugging-report.md` — Debugging analysis and findings

## Running Tests

```bash
python -m pytest test_cart.py -v
```

Or simply:

```bash
python test_cart.py
```

## Purpose

This lab demonstrates common Python debugging scenarios including:
- Logic errors in price calculations
- Edge case handling (empty cart, negative quantities)
- Floating-point precision issues
- State management bugs