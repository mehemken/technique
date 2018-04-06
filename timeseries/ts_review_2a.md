# Time Series Review 2

```python
import pandas as pd
import numpy as np
from datetime import datetime
```

```
timeser = pd.Series(
    np.random.randn(1000),
    index=pd.date_range(
        '1/1/2018',
        periods=1000
    )
)
```

```
timeser.loc['5-2019'][::4]
```
