## Summary
<br>
Not every python script has to be complicated to be super useful. If you can automate simple manipulations, like these shortcuts, it can still relieve some general repetative manual tasks. This project shows some simple ways to automate pieces of your workflow. These are examples of string manipulation that save time when working in SQL or Excel. Once these shortcuts are copied to your computer you can easily double click on the python file to manipulate string values from your clipboard. 

If you are looking for a slightly different way to run these shortcuts, check out the tkinter version here: https://github.com/danajsalk/Python-shortcuts-tkinter-application 

## Source Data
<br>
When the scripts are run, they directly access values copied to your clipboard.

## Run Directions:
<br>

1. Save shortcuts to folder.

2. Copy values to clipboard

3. Run script to edit values and put them back on clipboard

4. Paste new string

## Examples
Below are some examaples of the inputs and outputs for the shortcuts. 

| Shortcut          | Input                                        | Output                           |
|-------------------|----------------------------------------------|----------------------------------|
| Comma Shortcut    | apples <br> apples <br> oranges <br> bananas | apples, oranges, bananas         |
| Tick Shortcut     | apples <br> apples <br> oranges <br> bananas | 'apples', 'oranges', 'bananas'   |
| Tick a Comma      | apples, oranges, bananas                     | 'apples', 'oranges', 'bananas'   |
| Remove Duplicates | apples <br> apples <br> oranges <br> bananas | apples <br> oranges <br> bananas |


Use of string manipulations in SQL: 

```SQL
SELECT * 
FROM fruits_table ft
WHERE ft.fruit IN ('apples', 'oranges', 'bananas')
```
