# Bracket Pairing

This is a simple bracket pairing porject by Python 3.

## Requirement

Python >= 3.6

Python 3.8 or higher preferred

## Usage

1. **First please change the file paths in the pathconf.py**

   ie. ` proj_path ` and `json_path`

2. Run with the following command

   ```bash
   python BracketPairing.py
   ```

   

3. Then you could find a folder called `.tmp`, **in the parent folder of the working directory**, which contains the JSON file we want.

   The output JSON file is like the following:

   ```json
   [
    {
     "File name": "Action.elm",
     "Maximum depth": 4, 
     "isPaired": true
    },
    {
     "File name": "Card.elm",
     "Maximum depth": 2,
     "isPaired": true
    },
    {
     "File name": "ColorScheme.elm",
     "Maximum depth": 1,
     "isPaired": true
    }
   ]
   ```

   