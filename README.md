# Bracket Pairing 

This is a simple bracket pairing porject by Python 3.

## Usage

1. Use python 3 to compile the file

```bash
python3 BracketPairing.py
```

2. Input the file name that you want to check (eg. ```i1```)

3. Then the program will output a List

   eg.

   For input file ```i1```

   ```
   ))hello (world
   )
   ni(hao)
   ```

   we will have the result:

   ```
   [[(-1, -1), (-1, -1), (1, 9), (3, 3)], [(1, 1), (1, 2), (2, 1), (3, 7)]]
   ```

   The result is composed of 2 parts: **Left brackets' postions + Right ones' positions**

   If any of the brackets are not pairing, then the missing ones' positions will be ```(-1,-1)```

