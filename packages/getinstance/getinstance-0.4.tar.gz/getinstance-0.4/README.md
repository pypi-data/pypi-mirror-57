
## Installation

```
pip install getinstance
```

## Usage

```python
from getinstance import InstanceManager

class Country:
    instances = InstanceManager()
    
    def __init__(self, name):
        self.name = name
        
    def hello(self, username):
        print(f'hello, {username} from {self.name}')
            
au = Country('Australia')
ru = Country('Russia')

print(list(Country.instances.all()))
print(Country.instances.get(name='Australia')) 
Country.instances.filter(name='Russia').hello(username='Alice')

```
