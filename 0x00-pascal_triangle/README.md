# Pascal's Triangle

Pascal's Triangle is a triangular arrangement of binomial coefficients.

## 📘 Description

This project contains a Python implementation that generates Pascal’s Triangle up to a given number of rows.

The triangle begins with `1` at the top. Each subsequent row starts and ends with `1`, and each inner element is the sum of the two elements directly above it.

Pascal’s Triangle is used in:
- **Binomial expansions**
- **Combinatorics (e.g. combinations nCr)**
- **Probability theory**
- **Algebraic identities**

## 🧠 Example of Pascal's Triangle

```
     [1]
    [1, 1]
   [1, 2, 1]
  [1, 3, 3, 1]
 [1, 4, 6, 4, 1]
```

## 🧪 How It Works

Each row is constructed based on the previous row:
- The first and last elements of each row are always `1`.
- Middle elements are calculated as:  
  `row[j] = previous_row[j-1] + previous_row[j]`



## ✅ Sample Output (n = 5)

```
[1]
[1, 1]
[1, 2, 1]
[1, 3, 3, 1]
[1, 4, 6, 4, 1]
```

---
