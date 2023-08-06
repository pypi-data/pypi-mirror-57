# mypy-boto3-servicecatalog

Mypy-friendly auto-generated type annotations for `boto3 servicecatalog 1.10.33` service.
More information can be found [here](https://github.com/vemel/mypy_boto3).

- [mypy-boto3-servicecatalog](#mypy-boto3-servicecatalog)
  - [How to use](#how-to-use)
    - [Type checking](#type-checking)
    - [Code auto-complete](#code-auto-complete)
  - [How it works](#how-it-works)

## How to use

### Type checking

Make sure you have [mypy](https://github.com/python/mypy) installed and activated in your IDE.

Install `boto3-stubs` for `servicecatalog` service.

```bash
pip install boto3-stubs[mypy-boto3-servicecatalog]
```

Use `boto3` with `mypy_boto3` in your project and enjoy type checking.

```python
import boto3

from mypy_boto3 import servicecatalog
# alternative import if you do not want to install mypy_boto3 package
# import mypy_boto3_servicecatalog as servicecatalog

# Use this client as usual, now mypy can check if your code is valid.
client: servicecatalog.Client = boto3.client("servicecatalog")

# works for session as well
session = boto3.session.Session(region="us-west-1")
session_client: servicecatalog.Client = session.client("servicecatalog")


# Paginators need type annotation on creation
list_accepted_portfolio_shares_paginator: servicecatalog.ListAcceptedPortfolioSharesPaginator = client.get_paginator("list_accepted_portfolio_shares")
list_constraints_for_portfolio_paginator: servicecatalog.ListConstraintsForPortfolioPaginator = client.get_paginator("list_constraints_for_portfolio")
list_launch_paths_paginator: servicecatalog.ListLaunchPathsPaginator = client.get_paginator("list_launch_paths")
list_organization_portfolio_access_paginator: servicecatalog.ListOrganizationPortfolioAccessPaginator = client.get_paginator("list_organization_portfolio_access")
list_portfolios_paginator: servicecatalog.ListPortfoliosPaginator = client.get_paginator("list_portfolios")
list_portfolios_for_product_paginator: servicecatalog.ListPortfoliosForProductPaginator = client.get_paginator("list_portfolios_for_product")
list_principals_for_portfolio_paginator: servicecatalog.ListPrincipalsForPortfolioPaginator = client.get_paginator("list_principals_for_portfolio")
list_provisioned_product_plans_paginator: servicecatalog.ListProvisionedProductPlansPaginator = client.get_paginator("list_provisioned_product_plans")
list_provisioning_artifacts_for_service_action_paginator: servicecatalog.ListProvisioningArtifactsForServiceActionPaginator = client.get_paginator("list_provisioning_artifacts_for_service_action")
list_record_history_paginator: servicecatalog.ListRecordHistoryPaginator = client.get_paginator("list_record_history")
list_resources_for_tag_option_paginator: servicecatalog.ListResourcesForTagOptionPaginator = client.get_paginator("list_resources_for_tag_option")
list_service_actions_paginator: servicecatalog.ListServiceActionsPaginator = client.get_paginator("list_service_actions")
list_service_actions_for_provisioning_artifact_paginator: servicecatalog.ListServiceActionsForProvisioningArtifactPaginator = client.get_paginator("list_service_actions_for_provisioning_artifact")
list_tag_options_paginator: servicecatalog.ListTagOptionsPaginator = client.get_paginator("list_tag_options")
scan_provisioned_products_paginator: servicecatalog.ScanProvisionedProductsPaginator = client.get_paginator("scan_provisioned_products")
search_products_as_admin_paginator: servicecatalog.SearchProductsAsAdminPaginator = client.get_paginator("search_products_as_admin")
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