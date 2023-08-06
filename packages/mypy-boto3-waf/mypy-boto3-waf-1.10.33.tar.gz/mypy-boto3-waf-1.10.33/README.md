# mypy-boto3-waf

Mypy-friendly auto-generated type annotations for `boto3 waf 1.10.33` service.
More information can be found [here](https://github.com/vemel/mypy_boto3).

- [mypy-boto3-waf](#mypy-boto3-waf)
  - [How to use](#how-to-use)
    - [Type checking](#type-checking)
    - [Code auto-complete](#code-auto-complete)
  - [How it works](#how-it-works)

## How to use

### Type checking

Make sure you have [mypy](https://github.com/python/mypy) installed and activated in your IDE.

Install `boto3-stubs` for `waf` service.

```bash
pip install boto3-stubs[mypy-boto3-waf]
```

Use `boto3` with `mypy_boto3` in your project and enjoy type checking.

```python
import boto3

from mypy_boto3 import waf
# alternative import if you do not want to install mypy_boto3 package
# import mypy_boto3_waf as waf

# Use this client as usual, now mypy can check if your code is valid.
client: waf.Client = boto3.client("waf")

# works for session as well
session = boto3.session.Session(region="us-west-1")
session_client: waf.Client = session.client("waf")


# Paginators need type annotation on creation
get_rate_based_rule_managed_keys_paginator: waf.GetRateBasedRuleManagedKeysPaginator = client.get_paginator("get_rate_based_rule_managed_keys")
list_activated_rules_in_rule_group_paginator: waf.ListActivatedRulesInRuleGroupPaginator = client.get_paginator("list_activated_rules_in_rule_group")
list_byte_match_sets_paginator: waf.ListByteMatchSetsPaginator = client.get_paginator("list_byte_match_sets")
list_geo_match_sets_paginator: waf.ListGeoMatchSetsPaginator = client.get_paginator("list_geo_match_sets")
list_ip_sets_paginator: waf.ListIPSetsPaginator = client.get_paginator("list_ip_sets")
list_logging_configurations_paginator: waf.ListLoggingConfigurationsPaginator = client.get_paginator("list_logging_configurations")
list_rate_based_rules_paginator: waf.ListRateBasedRulesPaginator = client.get_paginator("list_rate_based_rules")
list_regex_match_sets_paginator: waf.ListRegexMatchSetsPaginator = client.get_paginator("list_regex_match_sets")
list_regex_pattern_sets_paginator: waf.ListRegexPatternSetsPaginator = client.get_paginator("list_regex_pattern_sets")
list_rule_groups_paginator: waf.ListRuleGroupsPaginator = client.get_paginator("list_rule_groups")
list_rules_paginator: waf.ListRulesPaginator = client.get_paginator("list_rules")
list_size_constraint_sets_paginator: waf.ListSizeConstraintSetsPaginator = client.get_paginator("list_size_constraint_sets")
list_sql_injection_match_sets_paginator: waf.ListSqlInjectionMatchSetsPaginator = client.get_paginator("list_sql_injection_match_sets")
list_subscribed_rule_groups_paginator: waf.ListSubscribedRuleGroupsPaginator = client.get_paginator("list_subscribed_rule_groups")
list_web_acls_paginator: waf.ListWebACLsPaginator = client.get_paginator("list_web_acls")
list_xss_match_sets_paginator: waf.ListXssMatchSetsPaginator = client.get_paginator("list_xss_match_sets")
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