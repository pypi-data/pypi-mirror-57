# mypy-boto3-lex-models

Mypy-friendly auto-generated type annotations for `boto3 lex-models 1.10.34` service.
More information can be found [here](https://github.com/vemel/mypy_boto3).

- [mypy-boto3-lex-models](#mypy-boto3-lex-models)
  - [How to use](#how-to-use)
    - [Type checking](#type-checking)
    - [Code auto-complete](#code-auto-complete)
  - [How it works](#how-it-works)

## How to use

### Type checking

Make sure you have [mypy](https://github.com/python/mypy) installed and activated in your IDE.

Install `boto3-stubs` for `lex-models` service.

```bash
pip install boto3-stubs[mypy-boto3-lex-models]
```

Use `boto3` with `mypy_boto3` in your project and enjoy type checking.

```python
import boto3

from mypy_boto3 import lex_models
# alternative import if you do not want to install mypy_boto3 package
# import mypy_boto3_lex_models as lex_models

# Use this client as usual, now mypy can check if your code is valid.
client: lex_models.Client = boto3.client("lex-models")

# works for session as well
session = boto3.session.Session(region="us-west-1")
session_client: lex_models.Client = session.client("lex-models")


# Paginators need type annotation on creation
get_bot_aliases_paginator: lex_models.GetBotAliasesPaginator = client.get_paginator("get_bot_aliases")
get_bot_channel_associations_paginator: lex_models.GetBotChannelAssociationsPaginator = client.get_paginator("get_bot_channel_associations")
get_bot_versions_paginator: lex_models.GetBotVersionsPaginator = client.get_paginator("get_bot_versions")
get_bots_paginator: lex_models.GetBotsPaginator = client.get_paginator("get_bots")
get_builtin_intents_paginator: lex_models.GetBuiltinIntentsPaginator = client.get_paginator("get_builtin_intents")
get_builtin_slot_types_paginator: lex_models.GetBuiltinSlotTypesPaginator = client.get_paginator("get_builtin_slot_types")
get_intent_versions_paginator: lex_models.GetIntentVersionsPaginator = client.get_paginator("get_intent_versions")
get_intents_paginator: lex_models.GetIntentsPaginator = client.get_paginator("get_intents")
get_slot_type_versions_paginator: lex_models.GetSlotTypeVersionsPaginator = client.get_paginator("get_slot_type_versions")
get_slot_types_paginator: lex_models.GetSlotTypesPaginator = client.get_paginator("get_slot_types")
```

## How it works

Fully automated [builder](https://github.com/vemel/mypy_boto3) carefully generates
type annotations for each service, patiently waiting for `boto3` updates. It delivers
a drop-in type annotations for you and makes sure that:

- Latest version of `boto3` is used.
- Each public class and method of every `boto3` service gets valid type annotations
  extracted from latest documentation (blame `botocore` docs if types are incorrect).
- Type annotations include up-to-date documentation.
- Code is processed by [black](https://github.com/psf/black) for readability.

## Submodules

- `master` - Install `mypy-boto3` package.