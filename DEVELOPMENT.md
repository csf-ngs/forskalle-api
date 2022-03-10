# Auto-models and query params

Model classes, json de/serialization and query parameters are auto-generated
from forskalle. You need a working fsk checkout (docker container).

Try:

```bash
docker-compose run script/forskalle3 create_python_api first_class --outfile ../skalle-api/forskalle-api/forskalle_api/auto/models.py
docker-compose run script/forskalle3 create_python_api queryparams --outfile ../skalle-api/forskalle-api/forskalle_api/auto/queryparams.py
```

remember to change paths as applicable.

The generated files need to be committed.