# Module Template

Standard structure for new Django apps in Freelaworks.

```
apps/<module_name>/
├── __init__.py
├── apps.py                     # AppConfig (name = 'apps.<module_name>')
├── signals.py                  # Django signals
├── models/                     # Django models (directory)
│   ├── __init__.py             # from .models import *
│   └── models.py
├── forms/                      # Django forms (directory)
│   ├── __init__.py             # from .forms import *
│   └── forms.py
├── admin/                      # Admin configuration (directory)
│   ├── __init__.py             # from .admin import *
│   └── admin.py
├── services/                   # Business logic (never in views)
│   └── __init__.py
├── views/                      # Thin views — delegate to services
│   └── __init__.py
├── urls/                       # URL routing (directory, not single file)
│   └── __init__.py             # app_name = '<module_name>', urlpatterns
├── middlewares/                 # Custom middleware
│   └── __init__.py
├── management/
│   └── commands/               # Custom manage.py commands
│       └── __init__.py
├── migrations/
│   └── __init__.py
└── tests/
    └── __init__.py
```

## Rules

- `app_name` MUST be set in `urls/__init__.py` for namespace
- URL pattern names: `<module_name>:<action>` (e.g., `jobs:index`, `jobs:detail`)
- Business logic in `services/`, views are thin
- `urls/` is a directory — split into sub-modules if needed
- `models/`, `forms/`, `admin/` are directories — split by entity if needed
- `__init__.py` must re-export from sub-modules
