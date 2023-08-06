# mypy-boto3-inspector

Mypy-friendly auto-generated type annotations for `boto3 inspector 1.10.34` service.
More information can be found [here](https://github.com/vemel/mypy_boto3).

- [mypy-boto3-inspector](#mypy-boto3-inspector)
  - [How to use](#how-to-use)
    - [Type checking](#type-checking)
    - [Code auto-complete](#code-auto-complete)
  - [How it works](#how-it-works)

## How to use

### Type checking

Make sure you have [mypy](https://github.com/python/mypy) installed and activated in your IDE.

Install `boto3-stubs` for `inspector` service.

```bash
pip install boto3-stubs[mypy-boto3-inspector]
```

Use `boto3` with `mypy_boto3` in your project and enjoy type checking.

```python
import boto3

from mypy_boto3 import inspector
# alternative import if you do not want to install mypy_boto3 package
# import mypy_boto3_inspector as inspector

# Use this client as usual, now mypy can check if your code is valid.
client: inspector.Client = boto3.client("inspector")

# works for session as well
session = boto3.session.Session(region="us-west-1")
session_client: inspector.Client = session.client("inspector")


# Paginators need type annotation on creation
list_assessment_run_agents_paginator: inspector.ListAssessmentRunAgentsPaginator = client.get_paginator("list_assessment_run_agents")
list_assessment_runs_paginator: inspector.ListAssessmentRunsPaginator = client.get_paginator("list_assessment_runs")
list_assessment_targets_paginator: inspector.ListAssessmentTargetsPaginator = client.get_paginator("list_assessment_targets")
list_assessment_templates_paginator: inspector.ListAssessmentTemplatesPaginator = client.get_paginator("list_assessment_templates")
list_event_subscriptions_paginator: inspector.ListEventSubscriptionsPaginator = client.get_paginator("list_event_subscriptions")
list_exclusions_paginator: inspector.ListExclusionsPaginator = client.get_paginator("list_exclusions")
list_findings_paginator: inspector.ListFindingsPaginator = client.get_paginator("list_findings")
list_rules_packages_paginator: inspector.ListRulesPackagesPaginator = client.get_paginator("list_rules_packages")
preview_agents_paginator: inspector.PreviewAgentsPaginator = client.get_paginator("preview_agents")
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