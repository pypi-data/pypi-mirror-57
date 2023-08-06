# mypy-boto3-comprehend

Mypy-friendly auto-generated type annotations for `boto3 comprehend 1.10.34` service.
More information can be found [here](https://github.com/vemel/mypy_boto3).

- [mypy-boto3-comprehend](#mypy-boto3-comprehend)
  - [How to use](#how-to-use)
    - [Type checking](#type-checking)
    - [Code auto-complete](#code-auto-complete)
  - [How it works](#how-it-works)

## How to use

### Type checking

Make sure you have [mypy](https://github.com/python/mypy) installed and activated in your IDE.

Install `boto3-stubs` for `comprehend` service.

```bash
pip install boto3-stubs[mypy-boto3-comprehend]
```

Use `boto3` with `mypy_boto3` in your project and enjoy type checking.

```python
import boto3

from mypy_boto3 import comprehend
# alternative import if you do not want to install mypy_boto3 package
# import mypy_boto3_comprehend as comprehend

# Use this client as usual, now mypy can check if your code is valid.
client: comprehend.Client = boto3.client("comprehend")

# works for session as well
session = boto3.session.Session(region="us-west-1")
session_client: comprehend.Client = session.client("comprehend")


# Paginators need type annotation on creation
list_document_classification_jobs_paginator: comprehend.ListDocumentClassificationJobsPaginator = client.get_paginator("list_document_classification_jobs")
list_document_classifiers_paginator: comprehend.ListDocumentClassifiersPaginator = client.get_paginator("list_document_classifiers")
list_dominant_language_detection_jobs_paginator: comprehend.ListDominantLanguageDetectionJobsPaginator = client.get_paginator("list_dominant_language_detection_jobs")
list_entities_detection_jobs_paginator: comprehend.ListEntitiesDetectionJobsPaginator = client.get_paginator("list_entities_detection_jobs")
list_entity_recognizers_paginator: comprehend.ListEntityRecognizersPaginator = client.get_paginator("list_entity_recognizers")
list_key_phrases_detection_jobs_paginator: comprehend.ListKeyPhrasesDetectionJobsPaginator = client.get_paginator("list_key_phrases_detection_jobs")
list_sentiment_detection_jobs_paginator: comprehend.ListSentimentDetectionJobsPaginator = client.get_paginator("list_sentiment_detection_jobs")
list_topics_detection_jobs_paginator: comprehend.ListTopicsDetectionJobsPaginator = client.get_paginator("list_topics_detection_jobs")
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