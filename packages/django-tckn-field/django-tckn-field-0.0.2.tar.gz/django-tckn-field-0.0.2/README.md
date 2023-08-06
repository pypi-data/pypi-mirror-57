# Django TCKN Field

A Django app built to integrate Republic of Turkey Identification Number to your project.

## Installation

```bash
pip install django-tckn-field
```

## Quick Start

```python
from tckn.fields import TCKNField

class MyModel(models.Model):
    tckn_field = TCKNField()
```

## How Numbers Are Validated

TCKNField inherits CharField, so it must be a string. Identification numbers are created by following these rules:

- The number must be 11 characters long
- The number mustn't start with 0
- The tenth character is created with this formula:

<a href="https://www.codecogs.com/eqnedit.php?latex=(((N_1&space;&plus;&space;N_3&space;&plus;&space;N_5&space;&plus;&space;N_7&space;&plus;&space;N_9)&space;*&space;7)&space;-&space;(N_2&space;&plus;&space;N_4&space;&plus;&space;N_6&space;&plus;&space;N_8))&space;(mod&space;10)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?(((N_1&space;&plus;&space;N_3&space;&plus;&space;N_5&space;&plus;&space;N_7&space;&plus;&space;N_9)&space;*&space;7)&space;-&space;(N_2&space;&plus;&space;N_4&space;&plus;&space;N_6&space;&plus;&space;N_8))&space;(mod&space;10)" title="(((N_1 + N_3 + N_5 + N_7 + N_9) * 7) - (N_2 + N_4 + N_6 + N_8)) (mod 10)" /></a>

- The eleventh character is created with this formula:

<a href="https://www.codecogs.com/eqnedit.php?latex=(N_1&space;&plus;&space;N_2&space;&plus;&space;N_3&space;&plus;&space;N_4&space;&plus;&space;N_5&space;&plus;&space;N_6&space;&plus;&space;N_7&space;&plus;&space;N_8&space;&plus;&space;N_9)&space;(mod&space;10)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?(N_1&space;&plus;&space;N_2&space;&plus;&space;N_3&space;&plus;&space;N_4&space;&plus;&space;N_5&space;&plus;&space;N_6&space;&plus;&space;N_7&space;&plus;&space;N_8&space;&plus;&space;N_9)&space;(mod&space;10)" title="(N_1 + N_2 + N_3 + N_4 + N_5 + N_6 + N_7 + N_8 + N_9) (mod 10)" /></a>

## License

You can use this program under the terms of MIT License. See LICENSE for details.

