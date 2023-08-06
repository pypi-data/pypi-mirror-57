# Django TCKN Field

A Django app built to integrate Republic of Turkey Identification Number to your project.

### Installation

```bash
pip install django-tckn-field
```

### Quick Start

```python
from tckn.fields import TCKNField

class MyModel(models.Model):
    tckn_field = TCKNField()
```

### License

You can use this program under the terms of MIT License. See LICENSE for details.

