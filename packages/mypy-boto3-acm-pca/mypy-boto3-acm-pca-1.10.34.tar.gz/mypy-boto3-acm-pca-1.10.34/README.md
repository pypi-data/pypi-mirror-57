# mypy-boto3-acm-pca

Mypy-friendly auto-generated type annotations for `boto3 acm-pca 1.10.34` service.
More information can be found [here](https://github.com/vemel/mypy_boto3).

- [mypy-boto3-acm-pca](#mypy-boto3-acm-pca)
  - [How to use](#how-to-use)
    - [Type checking](#type-checking)
    - [Code auto-complete](#code-auto-complete)
  - [How it works](#how-it-works)

## How to use

### Type checking

Make sure you have [mypy](https://github.com/python/mypy) installed and activated in your IDE.

Install `boto3-stubs` for `acm-pca` service.

```bash
pip install boto3-stubs[mypy-boto3-acm-pca]
```

Use `boto3` with `mypy_boto3` in your project and enjoy type checking.

```python
import boto3

from mypy_boto3 import acm_pca
# alternative import if you do not want to install mypy_boto3 package
# import mypy_boto3_acm_pca as acm_pca

# Use this client as usual, now mypy can check if your code is valid.
client: acm_pca.Client = boto3.client("acm-pca")

# works for session as well
session = boto3.session.Session(region="us-west-1")
session_client: acm_pca.Client = session.client("acm-pca")


# Waiters need type annotation on creation
audit_report_created_waiter: acm_pca.AuditReportCreatedWaiter = client.get_waiter("audit_report_created")
certificate_authority_csr_created_waiter: acm_pca.CertificateAuthorityCSRCreatedWaiter = client.get_waiter("certificate_authority_csr_created")
certificate_issued_waiter: acm_pca.CertificateIssuedWaiter = client.get_waiter("certificate_issued")

# Paginators need type annotation on creation
list_certificate_authorities_paginator: acm_pca.ListCertificateAuthoritiesPaginator = client.get_paginator("list_certificate_authorities")
list_permissions_paginator: acm_pca.ListPermissionsPaginator = client.get_paginator("list_permissions")
list_tags_paginator: acm_pca.ListTagsPaginator = client.get_paginator("list_tags")
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