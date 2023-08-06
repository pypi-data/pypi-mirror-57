# mypy-boto3-alexaforbusiness

Mypy-friendly auto-generated type annotations for `boto3 alexaforbusiness 1.10.33` service.
More information can be found [here](https://github.com/vemel/mypy_boto3).

- [mypy-boto3-alexaforbusiness](#mypy-boto3-alexaforbusiness)
  - [How to use](#how-to-use)
    - [Type checking](#type-checking)
    - [Code auto-complete](#code-auto-complete)
  - [How it works](#how-it-works)

## How to use

### Type checking

Make sure you have [mypy](https://github.com/python/mypy) installed and activated in your IDE.

Install `boto3-stubs` for `alexaforbusiness` service.

```bash
pip install boto3-stubs[mypy-boto3-alexaforbusiness]
```

Use `boto3` with `mypy_boto3` in your project and enjoy type checking.

```python
import boto3

from mypy_boto3 import alexaforbusiness
# alternative import if you do not want to install mypy_boto3 package
# import mypy_boto3_alexaforbusiness as alexaforbusiness

# Use this client as usual, now mypy can check if your code is valid.
client: alexaforbusiness.Client = boto3.client("alexaforbusiness")

# works for session as well
session = boto3.session.Session(region="us-west-1")
session_client: alexaforbusiness.Client = session.client("alexaforbusiness")


# Paginators need type annotation on creation
list_business_report_schedules_paginator: alexaforbusiness.ListBusinessReportSchedulesPaginator = client.get_paginator("list_business_report_schedules")
list_conference_providers_paginator: alexaforbusiness.ListConferenceProvidersPaginator = client.get_paginator("list_conference_providers")
list_device_events_paginator: alexaforbusiness.ListDeviceEventsPaginator = client.get_paginator("list_device_events")
list_skills_paginator: alexaforbusiness.ListSkillsPaginator = client.get_paginator("list_skills")
list_skills_store_categories_paginator: alexaforbusiness.ListSkillsStoreCategoriesPaginator = client.get_paginator("list_skills_store_categories")
list_skills_store_skills_by_category_paginator: alexaforbusiness.ListSkillsStoreSkillsByCategoryPaginator = client.get_paginator("list_skills_store_skills_by_category")
list_smart_home_appliances_paginator: alexaforbusiness.ListSmartHomeAppliancesPaginator = client.get_paginator("list_smart_home_appliances")
list_tags_paginator: alexaforbusiness.ListTagsPaginator = client.get_paginator("list_tags")
search_devices_paginator: alexaforbusiness.SearchDevicesPaginator = client.get_paginator("search_devices")
search_profiles_paginator: alexaforbusiness.SearchProfilesPaginator = client.get_paginator("search_profiles")
search_rooms_paginator: alexaforbusiness.SearchRoomsPaginator = client.get_paginator("search_rooms")
search_skill_groups_paginator: alexaforbusiness.SearchSkillGroupsPaginator = client.get_paginator("search_skill_groups")
search_users_paginator: alexaforbusiness.SearchUsersPaginator = client.get_paginator("search_users")
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