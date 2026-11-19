# Debugging Report: Shopping Cart Calculation Bug

## Project
- **Location**: `C:\Users\Dinkar\Hermes-Lab\debugging-lab\`
- **Files**: `cart.py`, `test_cart.py`

---

## Initial Investigation

### Application Behavior
The `calculate_total(items, discount_percent=0, tax_rate=0.08)` function computes a shopping cart total by:
1. Summing `price * quantity` for each item (subtotal)
2. Applying a percentage discount
3. Adding tax (default 8%)
4. Returning the rounded total

### Initial Test Results
```
FAIL: test_single_item - 11.88 != 10.8
FAIL: test_multiple_quantities - 19.44 != 27.0
FAIL: test_discount - 98.17 != 97.2
PASS: test_empty_cart
```

---

## Root Cause Analysis

### Faulty Logic
**File**: `cart.py`, **Line 5** (original)
```python
subtotal += item["price"] + item["quantity"]
```

**Problem**: The code **adds** price and quantity instead of **multiplying** them.

### Execution Trace (Single Item Test)
- Input: `{"price": 10, "quantity": 1}`
- Buggy: `subtotal = 10 + 1 = 11`
- Tax (8%): `11 * 0.08 = 0.88`
- Total: `11 + 0.88 = 11.88` ❌ (expected 10.8)

### Correct Logic
- Input: `{"price": 10, "quantity": 1}`
- Fixed: `subtotal = 10 * 1 = 10`
- Tax (8%): `10 * 0.08 = 0.8`
- Total: `10 + 0.8 = 10.8` ✅

### Affected Functions & Lines
- **Function**: `calculate_total()`
- **Line**: 5 (inside the for-loop)
- **Impact**: All non-empty cart calculations were incorrect

---

## Fix Applied

### Change
**File**: `cart.py`, **Line 5**
```diff
-        subtotal += item["price"] + item["quantity"]
+        subtotal += item["price"] * item["quantity"]
```

### Fixed File Content
```python
def calculate_total(items, discount_percent=0, tax_rate=0.08):
    subtotal = 0

    for item in items:
        subtotal += item["price"] * item["quantity"]

    discount = subtotal * (discount_percent / 100)
    discounted_subtotal = subtotal - discount

    tax = discounted_subtotal * tax_rate

    return round(discounted_subtotal + tax, 2)
```

---

## Validation Results

### Unit Tests (After Fix)
```
test_discount (__main__.TestShoppingCart.test_discount) ... ok
test_empty_cart (__main__.TestShoppingCart.test_empty_cart) ... ok
test_multiple_quantities (__main__.TestShoppingCart.test_multiple_quantities) ... ok
test_single_item (__main__.TestShoppingCart.test_single_item) ... ok

Ran 4 tests in 0.000s
OK
```

### Edge Case Testing
| Test Case | Input | Result | Expected | Status |
|-----------|-------|--------|----------|--------|
| Empty cart | `[]` | 0.0 | 0 | ✅ |
| Single item | `10 x 1` | 10.8 | 10.8 | ✅ |
| Multiple items | `10x2 + 5x1` | 27.0 | 27.0 | ✅ |
| 10% discount | `100 x 1` | 97.2 | 97.2 | ✅ |
| Zero discount | `50 x 2` | 108.0 | 108.0 | ✅ |
| 100% discount | `50 x 1` | 0.0 | 0.0 | ✅ |
| Custom tax 10% | `100 x 1` | 110.0 | 110.0 | ✅ |
| Large quantity | `1 x 100` | 108.0 | 108.0 | ✅ |
| Decimal prices | `9.99 x 3` | 32.37 | 32.37 | ✅ |

### Manual Verification
```
Items: [{"price": 10, "quantity": 2}, {"price": 5, "quantity": 1}]
Subtotal: 10*2 + 5*1 = 25
Discount (0%): 0
Tax (8%): 25 * 0.08 = 2.0
Total: 25 + 2.0 = 27.0 ✅
```

---

## Before vs After Behavior

| Scenario | Before (Buggy) | After (Fixed) |
|----------|----------------|---------------|
| `10 x 1` | 11.88 | 10.8 |
| `10 x 2, 5 x 1` | 19.44 | 27.0 |
| `100 x 1, 10% off` | 98.17 | 97.2 |
| Empty cart | 0.0 | 0.0 |

---

## Tools Used
- `terminal` - File inspection, test execution, edge case validation
- `read_file` - Reading source code and test files
- `patch` / `write_file` (via terminal) - Fixing the bug
- `python` - Running unit tests and manual verification

## Files Modified
- `C:\Users\Dinkar\Hermes-Lab\debugging-lab\cart.py` (Line 5: `+` → `*`)

---

## Conclusion
The bug was a single-character typo (`+` instead of `*`) in the subtotal calculation. All 4 unit tests now pass, and extensive edge case testing confirms correct behavior across discounts, tax rates, quantities, and decimal prices.