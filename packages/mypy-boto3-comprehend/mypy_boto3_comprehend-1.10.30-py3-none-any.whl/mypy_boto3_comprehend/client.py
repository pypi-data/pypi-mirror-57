"Main interface for comprehend service Client"
from __future__ import annotations

from typing import Any, Dict, List
from botocore.client import BaseClient
from botocore.exceptions import ClientError as Boto3ClientError
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3.type_defs import Literal, overload

# pylint: disable=import-self
import mypy_boto3_comprehend.client as client_scope

# pylint: disable=import-self
import mypy_boto3_comprehend.paginator as paginator_scope
from mypy_boto3_comprehend.type_defs import (
    ClientBatchDetectDominantLanguageResponseTypeDef,
    ClientBatchDetectEntitiesResponseTypeDef,
    ClientBatchDetectKeyPhrasesResponseTypeDef,
    ClientBatchDetectSentimentResponseTypeDef,
    ClientBatchDetectSyntaxResponseTypeDef,
    ClientClassifyDocumentResponseTypeDef,
    ClientCreateDocumentClassifierInputDataConfigTypeDef,
    ClientCreateDocumentClassifierOutputDataConfigTypeDef,
    ClientCreateDocumentClassifierResponseTypeDef,
    ClientCreateDocumentClassifierTagsTypeDef,
    ClientCreateDocumentClassifierVpcConfigTypeDef,
    ClientCreateEndpointResponseTypeDef,
    ClientCreateEndpointTagsTypeDef,
    ClientCreateEntityRecognizerInputDataConfigTypeDef,
    ClientCreateEntityRecognizerResponseTypeDef,
    ClientCreateEntityRecognizerTagsTypeDef,
    ClientCreateEntityRecognizerVpcConfigTypeDef,
    ClientDescribeDocumentClassificationJobResponseTypeDef,
    ClientDescribeDocumentClassifierResponseTypeDef,
    ClientDescribeDominantLanguageDetectionJobResponseTypeDef,
    ClientDescribeEndpointResponseTypeDef,
    ClientDescribeEntitiesDetectionJobResponseTypeDef,
    ClientDescribeEntityRecognizerResponseTypeDef,
    ClientDescribeKeyPhrasesDetectionJobResponseTypeDef,
    ClientDescribeSentimentDetectionJobResponseTypeDef,
    ClientDescribeTopicsDetectionJobResponseTypeDef,
    ClientDetectDominantLanguageResponseTypeDef,
    ClientDetectEntitiesResponseTypeDef,
    ClientDetectKeyPhrasesResponseTypeDef,
    ClientDetectSentimentResponseTypeDef,
    ClientDetectSyntaxResponseTypeDef,
    ClientListDocumentClassificationJobsFilterTypeDef,
    ClientListDocumentClassificationJobsResponseTypeDef,
    ClientListDocumentClassifiersFilterTypeDef,
    ClientListDocumentClassifiersResponseTypeDef,
    ClientListDominantLanguageDetectionJobsFilterTypeDef,
    ClientListDominantLanguageDetectionJobsResponseTypeDef,
    ClientListEndpointsFilterTypeDef,
    ClientListEndpointsResponseTypeDef,
    ClientListEntitiesDetectionJobsFilterTypeDef,
    ClientListEntitiesDetectionJobsResponseTypeDef,
    ClientListEntityRecognizersFilterTypeDef,
    ClientListEntityRecognizersResponseTypeDef,
    ClientListKeyPhrasesDetectionJobsFilterTypeDef,
    ClientListKeyPhrasesDetectionJobsResponseTypeDef,
    ClientListSentimentDetectionJobsFilterTypeDef,
    ClientListSentimentDetectionJobsResponseTypeDef,
    ClientListTagsForResourceResponseTypeDef,
    ClientListTopicsDetectionJobsFilterTypeDef,
    ClientListTopicsDetectionJobsResponseTypeDef,
    ClientStartDocumentClassificationJobInputDataConfigTypeDef,
    ClientStartDocumentClassificationJobOutputDataConfigTypeDef,
    ClientStartDocumentClassificationJobResponseTypeDef,
    ClientStartDocumentClassificationJobVpcConfigTypeDef,
    ClientStartDominantLanguageDetectionJobInputDataConfigTypeDef,
    ClientStartDominantLanguageDetectionJobOutputDataConfigTypeDef,
    ClientStartDominantLanguageDetectionJobResponseTypeDef,
    ClientStartDominantLanguageDetectionJobVpcConfigTypeDef,
    ClientStartEntitiesDetectionJobInputDataConfigTypeDef,
    ClientStartEntitiesDetectionJobOutputDataConfigTypeDef,
    ClientStartEntitiesDetectionJobResponseTypeDef,
    ClientStartEntitiesDetectionJobVpcConfigTypeDef,
    ClientStartKeyPhrasesDetectionJobInputDataConfigTypeDef,
    ClientStartKeyPhrasesDetectionJobOutputDataConfigTypeDef,
    ClientStartKeyPhrasesDetectionJobResponseTypeDef,
    ClientStartKeyPhrasesDetectionJobVpcConfigTypeDef,
    ClientStartSentimentDetectionJobInputDataConfigTypeDef,
    ClientStartSentimentDetectionJobOutputDataConfigTypeDef,
    ClientStartSentimentDetectionJobResponseTypeDef,
    ClientStartSentimentDetectionJobVpcConfigTypeDef,
    ClientStartTopicsDetectionJobInputDataConfigTypeDef,
    ClientStartTopicsDetectionJobOutputDataConfigTypeDef,
    ClientStartTopicsDetectionJobResponseTypeDef,
    ClientStartTopicsDetectionJobVpcConfigTypeDef,
    ClientStopDominantLanguageDetectionJobResponseTypeDef,
    ClientStopEntitiesDetectionJobResponseTypeDef,
    ClientStopKeyPhrasesDetectionJobResponseTypeDef,
    ClientStopSentimentDetectionJobResponseTypeDef,
    ClientTagResourceTagsTypeDef,
)


__all__ = ("Client",)


class Client(BaseClient):
    exceptions: client_scope.Exceptions

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def batch_detect_dominant_language(
        self, TextList: List[str]
    ) -> ClientBatchDetectDominantLanguageResponseTypeDef:
        """
        Determines the dominant language of the input text for a batch of documents. For a list of
        languages that Amazon Comprehend can detect, see `Amazon Comprehend Supported Languages
        <https://docs.aws.amazon.com/comprehend/latest/dg/how-languages.html>`__ .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/comprehend-2017-11-27/BatchDetectDominantLanguage>`_

        **Request Syntax**
        ::

          response = client.batch_detect_dominant_language(
              TextList=[
                  'string',
              ]
          )
        :type TextList: list
        :param TextList: **[REQUIRED]**

          A list containing the text of the input documents. The list can contain a maximum of 25
          documents. Each document should contain at least 20 characters and must contain fewer than
          5,000 bytes of UTF-8 encoded characters.

          - *(string) --*

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'ResultList': [
                    {
                        'Index': 123,
                        'Languages': [
                            {
                                'LanguageCode': 'string',
                                'Score': ...
                            },
                        ]
                    },
                ],
                'ErrorList': [
                    {
                        'Index': 123,
                        'ErrorCode': 'string',
                        'ErrorMessage': 'string'
                    },
                ]
            }
          **Response Structure**

          - *(dict) --*

            - **ResultList** *(list) --*

              A list of objects containing the results of the operation. The results are sorted in
              ascending order by the ``Index`` field and match the order of the documents in the
              input list. If all of the documents contain an error, the ``ResultList`` is empty.

              - *(dict) --*

                The result of calling the operation. The operation returns one object for each
                document that is successfully processed by the operation.

                - **Index** *(integer) --*

                  The zero-based index of the document in the input list.

                - **Languages** *(list) --*

                  One or more  DominantLanguage objects describing the dominant languages in the
                  document.

                  - *(dict) --*

                    Returns the code for the dominant language in the input text and the level of
                    confidence that Amazon Comprehend has in the accuracy of the detection.

                    - **LanguageCode** *(string) --*

                      The RFC 5646 language code for the dominant language. For more information
                      about RFC 5646, see `Tags for Identifying Languages
                      <https://tools.ietf.org/html/rfc5646>`__ on the *IETF Tools* web site.

                    - **Score** *(float) --*

                      The level of confidence that Amazon Comprehend has in the accuracy of the
                      detection.

            - **ErrorList** *(list) --*

              A list containing one object for each document that contained an error. The results
              are sorted in ascending order by the ``Index`` field and match the order of the
              documents in the input list. If there are no errors in the batch, the ``ErrorList`` is
              empty.

              - *(dict) --*

                Describes an error that occurred while processing a document in a batch. The
                operation returns on ``BatchItemError`` object for each document that contained an
                error.

                - **Index** *(integer) --*

                  The zero-based index of the document in the input list.

                - **ErrorCode** *(string) --*

                  The numeric error code of the error.

                - **ErrorMessage** *(string) --*

                  A text description of the error.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def batch_detect_entities(
        self,
        TextList: List[str],
        LanguageCode: Literal[
            "en", "es", "fr", "de", "it", "pt", "ar", "hi", "ja", "ko", "zh", "zh-TW"
        ],
    ) -> ClientBatchDetectEntitiesResponseTypeDef:
        """
        Inspects the text of a batch of documents for named entities and returns information about
        them. For more information about named entities, see  how-entities

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/comprehend-2017-11-27/BatchDetectEntities>`_

        **Request Syntax**
        ::

          response = client.batch_detect_entities(
              TextList=[
                  'string',
              ],
              LanguageCode='en'|'es'|'fr'|'de'|'it'|'pt'|'ar'|'hi'|'ja'|'ko'|'zh'|'zh-TW'
          )
        :type TextList: list
        :param TextList: **[REQUIRED]**

          A list containing the text of the input documents. The list can contain a maximum of 25
          documents. Each document must contain fewer than 5,000 bytes of UTF-8 encoded characters.

          - *(string) --*

        :type LanguageCode: string
        :param LanguageCode: **[REQUIRED]**

          The language of the input documents. You can specify any of the primary languages
          supported by Amazon Comprehend. All documents must be in the same language.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'ResultList': [
                    {
                        'Index': 123,
                        'Entities': [
                            {
                                'Score': ...,
                                'Type':
                                'PERSON'|'LOCATION'|'ORGANIZATION'
                                |'COMMERCIAL_ITEM'|'EVENT'|'DATE'|'QUANTITY'
                                |'TITLE'|'OTHER',
                                'Text': 'string',
                                'BeginOffset': 123,
                                'EndOffset': 123
                            },
                        ]
                    },
                ],
                'ErrorList': [
                    {
                        'Index': 123,
                        'ErrorCode': 'string',
                        'ErrorMessage': 'string'
                    },
                ]
            }
          **Response Structure**

          - *(dict) --*

            - **ResultList** *(list) --*

              A list of objects containing the results of the operation. The results are sorted in
              ascending order by the ``Index`` field and match the order of the documents in the
              input list. If all of the documents contain an error, the ``ResultList`` is empty.

              - *(dict) --*

                The result of calling the operation. The operation returns one object for each
                document that is successfully processed by the operation.

                - **Index** *(integer) --*

                  The zero-based index of the document in the input list.

                - **Entities** *(list) --*

                  One or more  Entity objects, one for each entity detected in the document.

                  - *(dict) --*

                    Provides information about an entity.

                    - **Score** *(float) --*

                      The level of confidence that Amazon Comprehend has in the accuracy of the
                      detection.

                    - **Type** *(string) --*

                      The entity's type.

                    - **Text** *(string) --*

                      The text of the entity.

                    - **BeginOffset** *(integer) --*

                      A character offset in the input text that shows where the entity begins (the
                      first character is at position 0). The offset returns the position of each
                      UTF-8 code point in the string. A *code point* is the abstract character from
                      a particular graphical representation. For example, a multi-byte UTF-8
                      character maps to a single code point.

                    - **EndOffset** *(integer) --*

                      A character offset in the input text that shows where the entity ends. The
                      offset returns the position of each UTF-8 code point in the string. A *code
                      point* is the abstract character from a particular graphical representation.
                      For example, a multi-byte UTF-8 character maps to a single code point.

            - **ErrorList** *(list) --*

              A list containing one object for each document that contained an error. The results
              are sorted in ascending order by the ``Index`` field and match the order of the
              documents in the input list. If there are no errors in the batch, the ``ErrorList`` is
              empty.

              - *(dict) --*

                Describes an error that occurred while processing a document in a batch. The
                operation returns on ``BatchItemError`` object for each document that contained an
                error.

                - **Index** *(integer) --*

                  The zero-based index of the document in the input list.

                - **ErrorCode** *(string) --*

                  The numeric error code of the error.

                - **ErrorMessage** *(string) --*

                  A text description of the error.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def batch_detect_key_phrases(
        self,
        TextList: List[str],
        LanguageCode: Literal[
            "en", "es", "fr", "de", "it", "pt", "ar", "hi", "ja", "ko", "zh", "zh-TW"
        ],
    ) -> ClientBatchDetectKeyPhrasesResponseTypeDef:
        """
        Detects the key noun phrases found in a batch of documents.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/comprehend-2017-11-27/BatchDetectKeyPhrases>`_

        **Request Syntax**
        ::

          response = client.batch_detect_key_phrases(
              TextList=[
                  'string',
              ],
              LanguageCode='en'|'es'|'fr'|'de'|'it'|'pt'|'ar'|'hi'|'ja'|'ko'|'zh'|'zh-TW'
          )
        :type TextList: list
        :param TextList: **[REQUIRED]**

          A list containing the text of the input documents. The list can contain a maximum of 25
          documents. Each document must contain fewer that 5,000 bytes of UTF-8 encoded characters.

          - *(string) --*

        :type LanguageCode: string
        :param LanguageCode: **[REQUIRED]**

          The language of the input documents. You can specify any of the primary languages
          supported by Amazon Comprehend. All documents must be in the same language.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'ResultList': [
                    {
                        'Index': 123,
                        'KeyPhrases': [
                            {
                                'Score': ...,
                                'Text': 'string',
                                'BeginOffset': 123,
                                'EndOffset': 123
                            },
                        ]
                    },
                ],
                'ErrorList': [
                    {
                        'Index': 123,
                        'ErrorCode': 'string',
                        'ErrorMessage': 'string'
                    },
                ]
            }
          **Response Structure**

          - *(dict) --*

            - **ResultList** *(list) --*

              A list of objects containing the results of the operation. The results are sorted in
              ascending order by the ``Index`` field and match the order of the documents in the
              input list. If all of the documents contain an error, the ``ResultList`` is empty.

              - *(dict) --*

                The result of calling the operation. The operation returns one object for each
                document that is successfully processed by the operation.

                - **Index** *(integer) --*

                  The zero-based index of the document in the input list.

                - **KeyPhrases** *(list) --*

                  One or more  KeyPhrase objects, one for each key phrase detected in the document.

                  - *(dict) --*

                    Describes a key noun phrase.

                    - **Score** *(float) --*

                      The level of confidence that Amazon Comprehend has in the accuracy of the
                      detection.

                    - **Text** *(string) --*

                      The text of a key noun phrase.

                    - **BeginOffset** *(integer) --*

                      A character offset in the input text that shows where the key phrase begins
                      (the first character is at position 0). The offset returns the position of
                      each UTF-8 code point in the string. A *code point* is the abstract character
                      from a particular graphical representation. For example, a multi-byte UTF-8
                      character maps to a single code point.

                    - **EndOffset** *(integer) --*

                      A character offset in the input text where the key phrase ends. The offset
                      returns the position of each UTF-8 code point in the string. A ``code point``
                      is the abstract character from a particular graphical representation. For
                      example, a multi-byte UTF-8 character maps to a single code point.

            - **ErrorList** *(list) --*

              A list containing one object for each document that contained an error. The results
              are sorted in ascending order by the ``Index`` field and match the order of the
              documents in the input list. If there are no errors in the batch, the ``ErrorList`` is
              empty.

              - *(dict) --*

                Describes an error that occurred while processing a document in a batch. The
                operation returns on ``BatchItemError`` object for each document that contained an
                error.

                - **Index** *(integer) --*

                  The zero-based index of the document in the input list.

                - **ErrorCode** *(string) --*

                  The numeric error code of the error.

                - **ErrorMessage** *(string) --*

                  A text description of the error.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def batch_detect_sentiment(
        self,
        TextList: List[str],
        LanguageCode: Literal[
            "en", "es", "fr", "de", "it", "pt", "ar", "hi", "ja", "ko", "zh", "zh-TW"
        ],
    ) -> ClientBatchDetectSentimentResponseTypeDef:
        """
        Inspects a batch of documents and returns an inference of the prevailing sentiment,
        ``POSITIVE`` , ``NEUTRAL`` , ``MIXED`` , or ``NEGATIVE`` , in each one.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/comprehend-2017-11-27/BatchDetectSentiment>`_

        **Request Syntax**
        ::

          response = client.batch_detect_sentiment(
              TextList=[
                  'string',
              ],
              LanguageCode='en'|'es'|'fr'|'de'|'it'|'pt'|'ar'|'hi'|'ja'|'ko'|'zh'|'zh-TW'
          )
        :type TextList: list
        :param TextList: **[REQUIRED]**

          A list containing the text of the input documents. The list can contain a maximum of 25
          documents. Each document must contain fewer that 5,000 bytes of UTF-8 encoded characters.

          - *(string) --*

        :type LanguageCode: string
        :param LanguageCode: **[REQUIRED]**

          The language of the input documents. You can specify any of the primary languages
          supported by Amazon Comprehend. All documents must be in the same language.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'ResultList': [
                    {
                        'Index': 123,
                        'Sentiment': 'POSITIVE'|'NEGATIVE'|'NEUTRAL'|'MIXED',
                        'SentimentScore': {
                            'Positive': ...,
                            'Negative': ...,
                            'Neutral': ...,
                            'Mixed': ...
                        }
                    },
                ],
                'ErrorList': [
                    {
                        'Index': 123,
                        'ErrorCode': 'string',
                        'ErrorMessage': 'string'
                    },
                ]
            }
          **Response Structure**

          - *(dict) --*

            - **ResultList** *(list) --*

              A list of objects containing the results of the operation. The results are sorted in
              ascending order by the ``Index`` field and match the order of the documents in the
              input list. If all of the documents contain an error, the ``ResultList`` is empty.

              - *(dict) --*

                The result of calling the operation. The operation returns one object for each
                document that is successfully processed by the operation.

                - **Index** *(integer) --*

                  The zero-based index of the document in the input list.

                - **Sentiment** *(string) --*

                  The sentiment detected in the document.

                - **SentimentScore** *(dict) --*

                  The level of confidence that Amazon Comprehend has in the accuracy of its
                  sentiment detection.

                  - **Positive** *(float) --*

                    The level of confidence that Amazon Comprehend has in the accuracy of its
                    detection of the ``POSITIVE`` sentiment.

                  - **Negative** *(float) --*

                    The level of confidence that Amazon Comprehend has in the accuracy of its
                    detection of the ``NEGATIVE`` sentiment.

                  - **Neutral** *(float) --*

                    The level of confidence that Amazon Comprehend has in the accuracy of its
                    detection of the ``NEUTRAL`` sentiment.

                  - **Mixed** *(float) --*

                    The level of confidence that Amazon Comprehend has in the accuracy of its
                    detection of the ``MIXED`` sentiment.

            - **ErrorList** *(list) --*

              A list containing one object for each document that contained an error. The results
              are sorted in ascending order by the ``Index`` field and match the order of the
              documents in the input list. If there are no errors in the batch, the ``ErrorList`` is
              empty.

              - *(dict) --*

                Describes an error that occurred while processing a document in a batch. The
                operation returns on ``BatchItemError`` object for each document that contained an
                error.

                - **Index** *(integer) --*

                  The zero-based index of the document in the input list.

                - **ErrorCode** *(string) --*

                  The numeric error code of the error.

                - **ErrorMessage** *(string) --*

                  A text description of the error.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def batch_detect_syntax(
        self, TextList: List[str], LanguageCode: Literal["en", "es", "fr", "de", "it", "pt"]
    ) -> ClientBatchDetectSyntaxResponseTypeDef:
        """
        Inspects the text of a batch of documents for the syntax and part of speech of the words in
        the document and returns information about them. For more information, see  how-syntax .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/comprehend-2017-11-27/BatchDetectSyntax>`_

        **Request Syntax**
        ::

          response = client.batch_detect_syntax(
              TextList=[
                  'string',
              ],
              LanguageCode='en'|'es'|'fr'|'de'|'it'|'pt'
          )
        :type TextList: list
        :param TextList: **[REQUIRED]**

          A list containing the text of the input documents. The list can contain a maximum of 25
          documents. Each document must contain fewer that 5,000 bytes of UTF-8 encoded characters.

          - *(string) --*

        :type LanguageCode: string
        :param LanguageCode: **[REQUIRED]**

          The language of the input documents. You can specify any of the following languages
          supported by Amazon Comprehend: German ("de"), English ("en"), Spanish ("es"), French
          ("fr"), Italian ("it"), or Portuguese ("pt"). All documents must be in the same language.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'ResultList': [
                    {
                        'Index': 123,
                        'SyntaxTokens': [
                            {
                                'TokenId': 123,
                                'Text': 'string',
                                'BeginOffset': 123,
                                'EndOffset': 123,
                                'PartOfSpeech': {
                                    'Tag':
                                    'ADJ'|'ADP'|'ADV'|'AUX'|'CONJ'
                                    |'CCONJ'|'DET'|'INTJ'|'NOUN'|'NUM'
                                    |'O'|'PART'|'PRON'|'PROPN'|'PUNCT'
                                    |'SCONJ'|'SYM'|'VERB',
                                    'Score': ...
                                }
                            },
                        ]
                    },
                ],
                'ErrorList': [
                    {
                        'Index': 123,
                        'ErrorCode': 'string',
                        'ErrorMessage': 'string'
                    },
                ]
            }
          **Response Structure**

          - *(dict) --*

            - **ResultList** *(list) --*

              A list of objects containing the results of the operation. The results are sorted in
              ascending order by the ``Index`` field and match the order of the documents in the
              input list. If all of the documents contain an error, the ``ResultList`` is empty.

              - *(dict) --*

                The result of calling the operation. The operation returns one object that is
                successfully processed by the operation.

                - **Index** *(integer) --*

                  The zero-based index of the document in the input list.

                - **SyntaxTokens** *(list) --*

                  The syntax tokens for the words in the document, one token for each word.

                  - *(dict) --*

                    Represents a work in the input text that was recognized and assigned a part of
                    speech. There is one syntax token record for each word in the source text.

                    - **TokenId** *(integer) --*

                      A unique identifier for a token.

                    - **Text** *(string) --*

                      The word that was recognized in the source text.

                    - **BeginOffset** *(integer) --*

                      The zero-based offset from the beginning of the source text to the first
                      character in the word.

                    - **EndOffset** *(integer) --*

                      The zero-based offset from the beginning of the source text to the last
                      character in the word.

                    - **PartOfSpeech** *(dict) --*

                      Provides the part of speech label and the confidence level that Amazon
                      Comprehend has that the part of speech was correctly identified. For more
                      information, see  how-syntax .

                      - **Tag** *(string) --*

                        Identifies the part of speech that the token represents.

                      - **Score** *(float) --*

                        The confidence that Amazon Comprehend has that the part of speech was
                        correctly identified.

            - **ErrorList** *(list) --*

              A list containing one object for each document that contained an error. The results
              are sorted in ascending order by the ``Index`` field and match the order of the
              documents in the input list. If there are no errors in the batch, the ``ErrorList`` is
              empty.

              - *(dict) --*

                Describes an error that occurred while processing a document in a batch. The
                operation returns on ``BatchItemError`` object for each document that contained an
                error.

                - **Index** *(integer) --*

                  The zero-based index of the document in the input list.

                - **ErrorCode** *(string) --*

                  The numeric error code of the error.

                - **ErrorMessage** *(string) --*

                  A text description of the error.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        :type operation_name: string
        :param operation_name: The operation name.  This is the same name
            as the method name on the client.  For example, if the
            method name is ``create_foo``, and you'd normally invoke the
            operation as ``client.create_foo(**kwargs)``, if the
            ``create_foo`` operation can be paginated, you can use the
            call ``client.get_paginator("create_foo")``.

        :return: ``True`` if the operation can be paginated,
            ``False`` otherwise.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def classify_document(
        self, Text: str, EndpointArn: str
    ) -> ClientClassifyDocumentResponseTypeDef:
        """
        Creates a new document classification request to analyze a single document in real-time,
        using a previously created and trained custom model and an endpoint.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/comprehend-2017-11-27/ClassifyDocument>`_

        **Request Syntax**
        ::

          response = client.classify_document(
              Text='string',
              EndpointArn='string'
          )
        :type Text: string
        :param Text: **[REQUIRED]**

          The document text to be analyzed.

        :type EndpointArn: string
        :param EndpointArn: **[REQUIRED]**

          The Amazon Resource Number (ARN) of the endpoint.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Classes': [
                    {
                        'Name': 'string',
                        'Score': ...
                    },
                ]
            }
          **Response Structure**

          - *(dict) --*

            - **Classes** *(list) --*

              The classes used by the document being analyzed. These are used for multi-class
              trained models. Individual classes are mutually exclusive and each document is
              expected to have only a single class assigned to it. For example, an animal can be a
              dog or a cat, but not both at the same time.

              - *(dict) --*

                Specifies the class that categorizes the document being analyzed

                - **Name** *(string) --*

                  The name of the class.

                - **Score** *(float) --*

                  The confidence score that Amazon Comprehend has this class correctly attributed.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_document_classifier(
        self,
        DocumentClassifierName: str,
        DataAccessRoleArn: str,
        InputDataConfig: ClientCreateDocumentClassifierInputDataConfigTypeDef,
        LanguageCode: Literal[
            "en", "es", "fr", "de", "it", "pt", "ar", "hi", "ja", "ko", "zh", "zh-TW"
        ],
        Tags: List[ClientCreateDocumentClassifierTagsTypeDef] = None,
        OutputDataConfig: ClientCreateDocumentClassifierOutputDataConfigTypeDef = None,
        ClientRequestToken: str = None,
        VolumeKmsKeyId: str = None,
        VpcConfig: ClientCreateDocumentClassifierVpcConfigTypeDef = None,
    ) -> ClientCreateDocumentClassifierResponseTypeDef:
        """
        Creates a new document classifier that you can use to categorize documents. To create a
        classifier you provide a set of training documents that labeled with the categories that you
        want to use. After the classifier is trained you can use it to categorize a set of labeled
        documents into the categories. For more information, see  how-document-classification .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/comprehend-2017-11-27/CreateDocumentClassifier>`_

        **Request Syntax**
        ::

          response = client.create_document_classifier(
              DocumentClassifierName='string',
              DataAccessRoleArn='string',
              Tags=[
                  {
                      'Key': 'string',
                      'Value': 'string'
                  },
              ],
              InputDataConfig={
                  'S3Uri': 'string'
              },
              OutputDataConfig={
                  'S3Uri': 'string',
                  'KmsKeyId': 'string'
              },
              ClientRequestToken='string',
              LanguageCode='en'|'es'|'fr'|'de'|'it'|'pt'|'ar'|'hi'|'ja'|'ko'|'zh'|'zh-TW',
              VolumeKmsKeyId='string',
              VpcConfig={
                  'SecurityGroupIds': [
                      'string',
                  ],
                  'Subnets': [
                      'string',
                  ]
              }
          )
        :type DocumentClassifierName: string
        :param DocumentClassifierName: **[REQUIRED]**

          The name of the document classifier.

        :type DataAccessRoleArn: string
        :param DataAccessRoleArn: **[REQUIRED]**

          The Amazon Resource Name (ARN) of the AWS Identity and Management (IAM) role that grants
          Amazon Comprehend read access to your input data.

        :type Tags: list
        :param Tags:

          Tags to be associated with the document classifier being created. A tag is a key-value
          pair that adds as a metadata to a resource used by Amazon Comprehend. For example, a tag
          with "Sales" as the key might be added to a resource to indicate its use by the sales
          department.

          - *(dict) --*

            A key-value pair that adds as a metadata to a resource used by Amazon Comprehend. For
            example, a tag with the key-value pair ‘Department’:’Sales’ might be added to a resource
            to indicate its use by a particular department.

            - **Key** *(string) --* **[REQUIRED]**

              The initial part of a key-value pair that forms a tag associated with a given
              resource. For instance, if you want to show which resources are used by which
              departments, you might use “Department” as the key portion of the pair, with multiple
              possible values such as “sales,” “legal,” and “administration.”

            - **Value** *(string) --*

              The second part of a key-value pair that forms a tag associated with a given resource.
              For instance, if you want to show which resources are used by which departments, you
              might use “Department” as the initial (key) portion of the pair, with a value of
              “sales” to indicate the sales department.

        :type InputDataConfig: dict
        :param InputDataConfig: **[REQUIRED]**

          Specifies the format and location of the input data for the job.

          - **S3Uri** *(string) --* **[REQUIRED]**

            The Amazon S3 URI for the input data. The S3 bucket must be in the same region as the
            API endpoint that you are calling. The URI can point to a single input file or it can
            provide the prefix for a collection of input files.

            For example, if you use the URI ``S3://bucketName/prefix`` , if the prefix is a single
            file, Amazon Comprehend uses that file as input. If more than one file begins with the
            prefix, Amazon Comprehend uses all of them as input.

        :type OutputDataConfig: dict
        :param OutputDataConfig:

          Enables the addition of output results configuration parameters for custom classifier
          jobs.

          - **S3Uri** *(string) --*

            When you use the ``OutputDataConfig`` object while creating a custom classifier, you
            specify the Amazon S3 location where you want to write the confusion matrix. The URI
            must be in the same region as the API endpoint that you are calling. The location is
            used as the prefix for the actual location of this output file.

            When the custom classifier job is finished, the service creates the output file in a
            directory specific to the job. The ``S3Uri`` field contains the location of the output
            file, called ``output.tar.gz`` . It is a compressed archive that contains the confusion
            matrix.

          - **KmsKeyId** *(string) --*

            ID for the AWS Key Management Service (KMS) key that Amazon Comprehend uses to encrypt
            the output results from an analysis job. The KmsKeyId can be one of the following
            formats:

            * KMS Key ID: ``"1234abcd-12ab-34cd-56ef-1234567890ab"``

            * Amazon Resource Name (ARN) of a KMS Key:
            ``"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"``

            * KMS Key Alias: ``"alias/ExampleAlias"``

            * ARN of a KMS Key Alias: ``"arn:aws:kms:us-west-2:111122223333:alias/ExampleAlias"``

        :type ClientRequestToken: string
        :param ClientRequestToken:

          A unique identifier for the request. If you don't set the client request token, Amazon
          Comprehend generates one.

          This field is autopopulated if not provided.

        :type LanguageCode: string
        :param LanguageCode: **[REQUIRED]**

          The language of the input documents. You can specify any of the following languages
          supported by Amazon Comprehend: German ("de"), English ("en"), Spanish ("es"), French
          ("fr"), Italian ("it"), or Portuguese ("pt"). All documents must be in the same language.

        :type VolumeKmsKeyId: string
        :param VolumeKmsKeyId:

          ID for the AWS Key Management Service (KMS) key that Amazon Comprehend uses to encrypt
          data on the storage volume attached to the ML compute instance(s) that process the
          analysis job. The VolumeKmsKeyId can be either of the following formats:

          * KMS Key ID: ``"1234abcd-12ab-34cd-56ef-1234567890ab"``

          * Amazon Resource Name (ARN) of a KMS Key:
          ``"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"``

        :type VpcConfig: dict
        :param VpcConfig:

          Configuration parameters for an optional private Virtual Private Cloud (VPC) containing
          the resources you are using for your custom classifier. For more information, see `Amazon
          VPC <https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html>`__ .

          - **SecurityGroupIds** *(list) --* **[REQUIRED]**

            The ID number for a security group on an instance of your private VPC. Security groups
            on your VPC function serve as a virtual firewall to control inbound and outbound traffic
            and provides security for the resources that you’ll be accessing on the VPC. This ID
            number is preceded by "sg-", for instance: "sg-03b388029b0a285ea". For more information,
            see `Security Groups for your VPC
            <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html>`__ .

            - *(string) --*

          - **Subnets** *(list) --* **[REQUIRED]**

            The ID for each subnet being used in your private VPC. This subnet is a subset of the a
            range of IPv4 addresses used by the VPC and is specific to a given availability zone in
            the VPC’s region. This ID number is preceded by "subnet-", for instance:
            "subnet-04ccf456919e69055". For more information, see `VPCs and Subnets
            <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html>`__ .

            - *(string) --*

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'DocumentClassifierArn': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **DocumentClassifierArn** *(string) --*

              The Amazon Resource Name (ARN) that identifies the document classifier.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_endpoint(
        self,
        EndpointName: str,
        ModelArn: str,
        DesiredInferenceUnits: int,
        ClientRequestToken: str = None,
        Tags: List[ClientCreateEndpointTagsTypeDef] = None,
    ) -> ClientCreateEndpointResponseTypeDef:
        """
        Creates a model-specific endpoint for synchronous inference for a previously trained custom
        model

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/comprehend-2017-11-27/CreateEndpoint>`_

        **Request Syntax**
        ::

          response = client.create_endpoint(
              EndpointName='string',
              ModelArn='string',
              DesiredInferenceUnits=123,
              ClientRequestToken='string',
              Tags=[
                  {
                      'Key': 'string',
                      'Value': 'string'
                  },
              ]
          )
        :type EndpointName: string
        :param EndpointName: **[REQUIRED]**

          This is the descriptive suffix that becomes part of the ``EndpointArn`` used for all
          subsequent requests to this resource.

        :type ModelArn: string
        :param ModelArn: **[REQUIRED]**

          The Amazon Resource Number (ARN) of the model to which the endpoint will be attached.

        :type DesiredInferenceUnits: integer
        :param DesiredInferenceUnits: **[REQUIRED]**

          The desired number of inference units to be used by the model using this endpoint. Each
          inference unit represents of a throughput of 100 characters per second.

        :type ClientRequestToken: string
        :param ClientRequestToken:

          An idempotency token provided by the customer. If this token matches a previous endpoint
          creation request, Amazon Comprehend will not return a ``ResourceInUseException`` .

          This field is autopopulated if not provided.

        :type Tags: list
        :param Tags:

          Tags associated with the endpoint being created. A tag is a key-value pair that adds
          metadata to the endpoint. For example, a tag with "Sales" as the key might be added to an
          endpoint to indicate its use by the sales department.

          - *(dict) --*

            A key-value pair that adds as a metadata to a resource used by Amazon Comprehend. For
            example, a tag with the key-value pair ‘Department’:’Sales’ might be added to a resource
            to indicate its use by a particular department.

            - **Key** *(string) --* **[REQUIRED]**

              The initial part of a key-value pair that forms a tag associated with a given
              resource. For instance, if you want to show which resources are used by which
              departments, you might use “Department” as the key portion of the pair, with multiple
              possible values such as “sales,” “legal,” and “administration.”

            - **Value** *(string) --*

              The second part of a key-value pair that forms a tag associated with a given resource.
              For instance, if you want to show which resources are used by which departments, you
              might use “Department” as the initial (key) portion of the pair, with a value of
              “sales” to indicate the sales department.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'EndpointArn': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **EndpointArn** *(string) --*

              The Amazon Resource Number (ARN) of the endpoint being created.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_entity_recognizer(
        self,
        RecognizerName: str,
        DataAccessRoleArn: str,
        InputDataConfig: ClientCreateEntityRecognizerInputDataConfigTypeDef,
        LanguageCode: Literal[
            "en", "es", "fr", "de", "it", "pt", "ar", "hi", "ja", "ko", "zh", "zh-TW"
        ],
        Tags: List[ClientCreateEntityRecognizerTagsTypeDef] = None,
        ClientRequestToken: str = None,
        VolumeKmsKeyId: str = None,
        VpcConfig: ClientCreateEntityRecognizerVpcConfigTypeDef = None,
    ) -> ClientCreateEntityRecognizerResponseTypeDef:
        """
        Creates an entity recognizer using submitted files. After your ``CreateEntityRecognizer``
        request is submitted, you can check job status using the API.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/comprehend-2017-11-27/CreateEntityRecognizer>`_

        **Request Syntax**
        ::

          response = client.create_entity_recognizer(
              RecognizerName='string',
              DataAccessRoleArn='string',
              Tags=[
                  {
                      'Key': 'string',
                      'Value': 'string'
                  },
              ],
              InputDataConfig={
                  'EntityTypes': [
                      {
                          'Type': 'string'
                      },
                  ],
                  'Documents': {
                      'S3Uri': 'string'
                  },
                  'Annotations': {
                      'S3Uri': 'string'
                  },
                  'EntityList': {
                      'S3Uri': 'string'
                  }
              },
              ClientRequestToken='string',
              LanguageCode='en'|'es'|'fr'|'de'|'it'|'pt'|'ar'|'hi'|'ja'|'ko'|'zh'|'zh-TW',
              VolumeKmsKeyId='string',
              VpcConfig={
                  'SecurityGroupIds': [
                      'string',
                  ],
                  'Subnets': [
                      'string',
                  ]
              }
          )
        :type RecognizerName: string
        :param RecognizerName: **[REQUIRED]**

          The name given to the newly created recognizer. Recognizer names can be a maximum of 256
          characters. Alphanumeric characters, hyphens (-) and underscores (_) are allowed. The name
          must be unique in the account/region.

        :type DataAccessRoleArn: string
        :param DataAccessRoleArn: **[REQUIRED]**

          The Amazon Resource Name (ARN) of the AWS Identity and Management (IAM) role that grants
          Amazon Comprehend read access to your input data.

        :type Tags: list
        :param Tags:

          Tags to be associated with the entity recognizer being created. A tag is a key-value pair
          that adds as a metadata to a resource used by Amazon Comprehend. For example, a tag with
          "Sales" as the key might be added to a resource to indicate its use by the sales
          department.

          - *(dict) --*

            A key-value pair that adds as a metadata to a resource used by Amazon Comprehend. For
            example, a tag with the key-value pair ‘Department’:’Sales’ might be added to a resource
            to indicate its use by a particular department.

            - **Key** *(string) --* **[REQUIRED]**

              The initial part of a key-value pair that forms a tag associated with a given
              resource. For instance, if you want to show which resources are used by which
              departments, you might use “Department” as the key portion of the pair, with multiple
              possible values such as “sales,” “legal,” and “administration.”

            - **Value** *(string) --*

              The second part of a key-value pair that forms a tag associated with a given resource.
              For instance, if you want to show which resources are used by which departments, you
              might use “Department” as the initial (key) portion of the pair, with a value of
              “sales” to indicate the sales department.

        :type InputDataConfig: dict
        :param InputDataConfig: **[REQUIRED]**

          Specifies the format and location of the input data. The S3 bucket containing the input
          data must be located in the same region as the entity recognizer being created.

          - **EntityTypes** *(list) --* **[REQUIRED]**

            The entity types in the input data for an entity recognizer. A maximum of 12 entity
            types can be used at one time to train an entity recognizer.

            - *(dict) --*

              Information about an individual item on a list of entity types.

              - **Type** *(string) --* **[REQUIRED]**

                Entity type of an item on an entity type list.

          - **Documents** *(dict) --* **[REQUIRED]**

            S3 location of the documents folder for an entity recognizer

            - **S3Uri** *(string) --* **[REQUIRED]**

              Specifies the Amazon S3 location where the training documents for an entity recognizer
              are located. The URI must be in the same region as the API endpoint that you are
              calling.

          - **Annotations** *(dict) --*

            S3 location of the annotations file for an entity recognizer.

            - **S3Uri** *(string) --* **[REQUIRED]**

              Specifies the Amazon S3 location where the annotations for an entity recognizer are
              located. The URI must be in the same region as the API endpoint that you are calling.

          - **EntityList** *(dict) --*

            S3 location of the entity list for an entity recognizer.

            - **S3Uri** *(string) --* **[REQUIRED]**

              Specifies the Amazon S3 location where the entity list is located. The URI must be in
              the same region as the API endpoint that you are calling.

        :type ClientRequestToken: string
        :param ClientRequestToken:

          A unique identifier for the request. If you don't set the client request token, Amazon
          Comprehend generates one.

          This field is autopopulated if not provided.

        :type LanguageCode: string
        :param LanguageCode: **[REQUIRED]**

          The language of the input documents. All documents must be in the same language. Only
          English ("en") is currently supported.

        :type VolumeKmsKeyId: string
        :param VolumeKmsKeyId:

          ID for the AWS Key Management Service (KMS) key that Amazon Comprehend uses to encrypt
          data on the storage volume attached to the ML compute instance(s) that process the
          analysis job. The VolumeKmsKeyId can be either of the following formats:

          * KMS Key ID: ``"1234abcd-12ab-34cd-56ef-1234567890ab"``

          * Amazon Resource Name (ARN) of a KMS Key:
          ``"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"``

        :type VpcConfig: dict
        :param VpcConfig:

          Configuration parameters for an optional private Virtual Private Cloud (VPC) containing
          the resources you are using for your custom entity recognizer. For more information, see
          `Amazon VPC <https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html>`__
          .

          - **SecurityGroupIds** *(list) --* **[REQUIRED]**

            The ID number for a security group on an instance of your private VPC. Security groups
            on your VPC function serve as a virtual firewall to control inbound and outbound traffic
            and provides security for the resources that you’ll be accessing on the VPC. This ID
            number is preceded by "sg-", for instance: "sg-03b388029b0a285ea". For more information,
            see `Security Groups for your VPC
            <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html>`__ .

            - *(string) --*

          - **Subnets** *(list) --* **[REQUIRED]**

            The ID for each subnet being used in your private VPC. This subnet is a subset of the a
            range of IPv4 addresses used by the VPC and is specific to a given availability zone in
            the VPC’s region. This ID number is preceded by "subnet-", for instance:
            "subnet-04ccf456919e69055". For more information, see `VPCs and Subnets
            <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html>`__ .

            - *(string) --*

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'EntityRecognizerArn': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **EntityRecognizerArn** *(string) --*

              The Amazon Resource Name (ARN) that identifies the entity recognizer.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_document_classifier(self, DocumentClassifierArn: str) -> Dict[str, Any]:
        """
        Deletes a previously created document classifier

        Only those classifiers that are in terminated states (IN_ERROR, TRAINED) will be deleted. If
        an active inference job is using the model, a ``ResourceInUseException`` will be returned.

        This is an asynchronous action that puts the classifier into a DELETING state, and it is
        then removed by a background job. Once removed, the classifier disappears from your account
        and is no longer available for use.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/comprehend-2017-11-27/DeleteDocumentClassifier>`_

        **Request Syntax**
        ::

          response = client.delete_document_classifier(
              DocumentClassifierArn='string'
          )
        :type DocumentClassifierArn: string
        :param DocumentClassifierArn: **[REQUIRED]**

          The Amazon Resource Name (ARN) that identifies the document classifier.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {}
          **Response Structure**

          - *(dict) --*
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_endpoint(self, EndpointArn: str) -> Dict[str, Any]:
        """
        Deletes a model-specific endpoint for a previously-trained custom model. All endpoints must
        be deleted in order for the model to be deleted.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/comprehend-2017-11-27/DeleteEndpoint>`_

        **Request Syntax**
        ::

          response = client.delete_endpoint(
              EndpointArn='string'
          )
        :type EndpointArn: string
        :param EndpointArn: **[REQUIRED]**

          The Amazon Resource Number (ARN) of the endpoint being deleted.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {}
          **Response Structure**

          - *(dict) --*
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_entity_recognizer(self, EntityRecognizerArn: str) -> Dict[str, Any]:
        """
        Deletes an entity recognizer.

        Only those recognizers that are in terminated states (IN_ERROR, TRAINED) will be deleted. If
        an active inference job is using the model, a ``ResourceInUseException`` will be returned.

        This is an asynchronous action that puts the recognizer into a DELETING state, and it is
        then removed by a background job. Once removed, the recognizer disappears from your account
        and is no longer available for use.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/comprehend-2017-11-27/DeleteEntityRecognizer>`_

        **Request Syntax**
        ::

          response = client.delete_entity_recognizer(
              EntityRecognizerArn='string'
          )
        :type EntityRecognizerArn: string
        :param EntityRecognizerArn: **[REQUIRED]**

          The Amazon Resource Name (ARN) that identifies the entity recognizer.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {}
          **Response Structure**

          - *(dict) --*
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_document_classification_job(
        self, JobId: str
    ) -> ClientDescribeDocumentClassificationJobResponseTypeDef:
        """
        Gets the properties associated with a document classification job. Use this operation to get
        the status of a classification job.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/comprehend-2017-11-27/DescribeDocumentClassificationJob>`_

        **Request Syntax**
        ::

          response = client.describe_document_classification_job(
              JobId='string'
          )
        :type JobId: string
        :param JobId: **[REQUIRED]**

          The identifier that Amazon Comprehend generated for the job. The operation returns this
          identifier in its response.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'DocumentClassificationJobProperties': {
                    'JobId': 'string',
                    'JobName': 'string',
                    'JobStatus':
                    'SUBMITTED'|'IN_PROGRESS'|'COMPLETED'|'FAILED'|'STOP_REQUESTED'
                    |'STOPPED',
                    'Message': 'string',
                    'SubmitTime': datetime(2015, 1, 1),
                    'EndTime': datetime(2015, 1, 1),
                    'DocumentClassifierArn': 'string',
                    'InputDataConfig': {
                        'S3Uri': 'string',
                        'InputFormat': 'ONE_DOC_PER_FILE'|'ONE_DOC_PER_LINE'
                    },
                    'OutputDataConfig': {
                        'S3Uri': 'string',
                        'KmsKeyId': 'string'
                    },
                    'DataAccessRoleArn': 'string',
                    'VolumeKmsKeyId': 'string',
                    'VpcConfig': {
                        'SecurityGroupIds': [
                            'string',
                        ],
                        'Subnets': [
                            'string',
                        ]
                    }
                }
            }
          **Response Structure**

          - *(dict) --*

            - **DocumentClassificationJobProperties** *(dict) --*

              An object that describes the properties associated with the document classification
              job.

              - **JobId** *(string) --*

                The identifier assigned to the document classification job.

              - **JobName** *(string) --*

                The name that you assigned to the document classification job.

              - **JobStatus** *(string) --*

                The current status of the document classification job. If the status is ``FAILED`` ,
                the ``Message`` field shows the reason for the failure.

              - **Message** *(string) --*

                A description of the status of the job.

              - **SubmitTime** *(datetime) --*

                The time that the document classification job was submitted for processing.

              - **EndTime** *(datetime) --*

                The time that the document classification job completed.

              - **DocumentClassifierArn** *(string) --*

                The Amazon Resource Name (ARN) that identifies the document classifier.

              - **InputDataConfig** *(dict) --*

                The input data configuration that you supplied when you created the document
                classification job.

                - **S3Uri** *(string) --*

                  The Amazon S3 URI for the input data. The URI must be in same region as the API
                  endpoint that you are calling. The URI can point to a single input file or it can
                  provide the prefix for a collection of data files.

                  For example, if you use the URI ``S3://bucketName/prefix`` , if the prefix is a
                  single file, Amazon Comprehend uses that file as input. If more than one file
                  begins with the prefix, Amazon Comprehend uses all of them as input.

                - **InputFormat** *(string) --*

                  Specifies how the text in an input file should be processed:

                  * ``ONE_DOC_PER_FILE`` - Each file is considered a separate document. Use this
                  option when you are processing large documents, such as newspaper articles or
                  scientific papers.

                  * ``ONE_DOC_PER_LINE`` - Each line in a file is considered a separate document.
                  Use this option when you are processing many short documents, such as text
                  messages.

              - **OutputDataConfig** *(dict) --*

                The output data configuration that you supplied when you created the document
                classification job.

                - **S3Uri** *(string) --*

                  When you use the ``OutputDataConfig`` object with asynchronous operations, you
                  specify the Amazon S3 location where you want to write the output data. The URI
                  must be in the same region as the API endpoint that you are calling. The location
                  is used as the prefix for the actual location of the output file.

                  When the topic detection job is finished, the service creates an output file in a
                  directory specific to the job. The ``S3Uri`` field contains the location of the
                  output file, called ``output.tar.gz`` . It is a compressed archive that contains
                  the ouput of the operation.

                - **KmsKeyId** *(string) --*

                  ID for the AWS Key Management Service (KMS) key that Amazon Comprehend uses to
                  encrypt the output results from an analysis job. The KmsKeyId can be one of the
                  following formats:

                  * KMS Key ID: ``"1234abcd-12ab-34cd-56ef-1234567890ab"``

                  * Amazon Resource Name (ARN) of a KMS Key:
                  ``"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"``

                  * KMS Key Alias: ``"alias/ExampleAlias"``

                  * ARN of a KMS Key Alias:
                  ``"arn:aws:kms:us-west-2:111122223333:alias/ExampleAlias"``

              - **DataAccessRoleArn** *(string) --*

                The Amazon Resource Name (ARN) of the AWS identity and Access Management (IAM) role
                that grants Amazon Comprehend read access to your input data.

              - **VolumeKmsKeyId** *(string) --*

                ID for the AWS Key Management Service (KMS) key that Amazon Comprehend uses to
                encrypt data on the storage volume attached to the ML compute instance(s) that
                process the analysis job. The VolumeKmsKeyId can be either of the following formats:

                * KMS Key ID: ``"1234abcd-12ab-34cd-56ef-1234567890ab"``

                * Amazon Resource Name (ARN) of a KMS Key:
                ``"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"``

              - **VpcConfig** *(dict) --*

                Configuration parameters for a private Virtual Private Cloud (VPC) containing the
                resources you are using for your document classification job. For more information,
                see `Amazon VPC
                <https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html>`__ .

                - **SecurityGroupIds** *(list) --*

                  The ID number for a security group on an instance of your private VPC. Security
                  groups on your VPC function serve as a virtual firewall to control inbound and
                  outbound traffic and provides security for the resources that you’ll be accessing
                  on the VPC. This ID number is preceded by "sg-", for instance:
                  "sg-03b388029b0a285ea". For more information, see `Security Groups for your VPC
                  <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html>`__ .

                  - *(string) --*

                - **Subnets** *(list) --*

                  The ID for each subnet being used in your private VPC. This subnet is a subset of
                  the a range of IPv4 addresses used by the VPC and is specific to a given
                  availability zone in the VPC’s region. This ID number is preceded by "subnet-",
                  for instance: "subnet-04ccf456919e69055". For more information, see `VPCs and
                  Subnets <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html>`__ .

                  - *(string) --*
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_document_classifier(
        self, DocumentClassifierArn: str
    ) -> ClientDescribeDocumentClassifierResponseTypeDef:
        """
        Gets the properties associated with a document classifier.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/comprehend-2017-11-27/DescribeDocumentClassifier>`_

        **Request Syntax**
        ::

          response = client.describe_document_classifier(
              DocumentClassifierArn='string'
          )
        :type DocumentClassifierArn: string
        :param DocumentClassifierArn: **[REQUIRED]**

          The Amazon Resource Name (ARN) that identifies the document classifier. The operation
          returns this identifier in its response.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'DocumentClassifierProperties': {
                    'DocumentClassifierArn': 'string',
                    'LanguageCode': 'en'|'es'|'fr'|'de'|'it'|'pt'|'ar'|'hi'|'ja'|'ko'|'zh'|'zh-TW',
                    'Status':
                    'SUBMITTED'|'TRAINING'|'DELETING'|'STOP_REQUESTED'|'STOPPED'
                    |'IN_ERROR'|'TRAINED',
                    'Message': 'string',
                    'SubmitTime': datetime(2015, 1, 1),
                    'EndTime': datetime(2015, 1, 1),
                    'TrainingStartTime': datetime(2015, 1, 1),
                    'TrainingEndTime': datetime(2015, 1, 1),
                    'InputDataConfig': {
                        'S3Uri': 'string'
                    },
                    'OutputDataConfig': {
                        'S3Uri': 'string',
                        'KmsKeyId': 'string'
                    },
                    'ClassifierMetadata': {
                        'NumberOfLabels': 123,
                        'NumberOfTrainedDocuments': 123,
                        'NumberOfTestDocuments': 123,
                        'EvaluationMetrics': {
                            'Accuracy': 123.0,
                            'Precision': 123.0,
                            'Recall': 123.0,
                            'F1Score': 123.0
                        }
                    },
                    'DataAccessRoleArn': 'string',
                    'VolumeKmsKeyId': 'string',
                    'VpcConfig': {
                        'SecurityGroupIds': [
                            'string',
                        ],
                        'Subnets': [
                            'string',
                        ]
                    }
                }
            }
          **Response Structure**

          - *(dict) --*

            - **DocumentClassifierProperties** *(dict) --*

              An object that contains the properties associated with a document classifier.

              - **DocumentClassifierArn** *(string) --*

                The Amazon Resource Name (ARN) that identifies the document classifier.

              - **LanguageCode** *(string) --*

                The language code for the language of the documents that the classifier was trained
                on.

              - **Status** *(string) --*

                The status of the document classifier. If the status is ``TRAINED`` the classifier
                is ready to use. If the status is ``FAILED`` you can see additional information
                about why the classifier wasn't trained in the ``Message`` field.

              - **Message** *(string) --*

                Additional information about the status of the classifier.

              - **SubmitTime** *(datetime) --*

                The time that the document classifier was submitted for training.

              - **EndTime** *(datetime) --*

                The time that training the document classifier completed.

              - **TrainingStartTime** *(datetime) --*

                Indicates the time when the training starts on documentation classifiers. You are
                billed for the time interval between this time and the value of TrainingEndTime.

              - **TrainingEndTime** *(datetime) --*

                The time that training of the document classifier was completed. Indicates the time
                when the training completes on documentation classifiers. You are billed for the
                time interval between this time and the value of TrainingStartTime.

              - **InputDataConfig** *(dict) --*

                The input data configuration that you supplied when you created the document
                classifier for training.

                - **S3Uri** *(string) --*

                  The Amazon S3 URI for the input data. The S3 bucket must be in the same region as
                  the API endpoint that you are calling. The URI can point to a single input file or
                  it can provide the prefix for a collection of input files.

                  For example, if you use the URI ``S3://bucketName/prefix`` , if the prefix is a
                  single file, Amazon Comprehend uses that file as input. If more than one file
                  begins with the prefix, Amazon Comprehend uses all of them as input.

              - **OutputDataConfig** *(dict) --*

                Provides output results configuration parameters for custom classifier jobs.

                - **S3Uri** *(string) --*

                  When you use the ``OutputDataConfig`` object while creating a custom classifier,
                  you specify the Amazon S3 location where you want to write the confusion matrix.
                  The URI must be in the same region as the API endpoint that you are calling. The
                  location is used as the prefix for the actual location of this output file.

                  When the custom classifier job is finished, the service creates the output file in
                  a directory specific to the job. The ``S3Uri`` field contains the location of the
                  output file, called ``output.tar.gz`` . It is a compressed archive that contains
                  the confusion matrix.

                - **KmsKeyId** *(string) --*

                  ID for the AWS Key Management Service (KMS) key that Amazon Comprehend uses to
                  encrypt the output results from an analysis job. The KmsKeyId can be one of the
                  following formats:

                  * KMS Key ID: ``"1234abcd-12ab-34cd-56ef-1234567890ab"``

                  * Amazon Resource Name (ARN) of a KMS Key:
                  ``"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"``

                  * KMS Key Alias: ``"alias/ExampleAlias"``

                  * ARN of a KMS Key Alias:
                  ``"arn:aws:kms:us-west-2:111122223333:alias/ExampleAlias"``

              - **ClassifierMetadata** *(dict) --*

                Information about the document classifier, including the number of documents used
                for training the classifier, the number of documents used for test the classifier,
                and an accuracy rating.

                - **NumberOfLabels** *(integer) --*

                  The number of labels in the input data.

                - **NumberOfTrainedDocuments** *(integer) --*

                  The number of documents in the input data that were used to train the classifier.
                  Typically this is 80 to 90 percent of the input documents.

                - **NumberOfTestDocuments** *(integer) --*

                  The number of documents in the input data that were used to test the classifier.
                  Typically this is 10 to 20 percent of the input documents.

                - **EvaluationMetrics** *(dict) --*

                  Describes the result metrics for the test data associated with an documentation
                  classifier.

                  - **Accuracy** *(float) --*

                    The fraction of the labels that were correct recognized. It is computed by
                    dividing the number of labels in the test documents that were correctly
                    recognized by the total number of labels in the test documents.

                  - **Precision** *(float) --*

                    A measure of the usefulness of the classifier results in the test data. High
                    precision means that the classifier returned substantially more relevant results
                    than irrelevant ones.

                  - **Recall** *(float) --*

                    A measure of how complete the classifier results are for the test data. High
                    recall means that the classifier returned most of the relevant results.

                  - **F1Score** *(float) --*

                    A measure of how accurate the classifier results are for the test data. It is
                    derived from the ``Precision`` and ``Recall`` values. The ``F1Score`` is the
                    harmonic average of the two scores. The highest score is 1, and the worst score
                    is 0.

              - **DataAccessRoleArn** *(string) --*

                The Amazon Resource Name (ARN) of the AWS Identity and Management (IAM) role that
                grants Amazon Comprehend read access to your input data.

              - **VolumeKmsKeyId** *(string) --*

                ID for the AWS Key Management Service (KMS) key that Amazon Comprehend uses to
                encrypt data on the storage volume attached to the ML compute instance(s) that
                process the analysis job. The VolumeKmsKeyId can be either of the following formats:

                * KMS Key ID: ``"1234abcd-12ab-34cd-56ef-1234567890ab"``

                * Amazon Resource Name (ARN) of a KMS Key:
                ``"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"``

              - **VpcConfig** *(dict) --*

                Configuration parameters for a private Virtual Private Cloud (VPC) containing the
                resources you are using for your custom classifier. For more information, see
                `Amazon VPC
                <https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html>`__ .

                - **SecurityGroupIds** *(list) --*

                  The ID number for a security group on an instance of your private VPC. Security
                  groups on your VPC function serve as a virtual firewall to control inbound and
                  outbound traffic and provides security for the resources that you’ll be accessing
                  on the VPC. This ID number is preceded by "sg-", for instance:
                  "sg-03b388029b0a285ea". For more information, see `Security Groups for your VPC
                  <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html>`__ .

                  - *(string) --*

                - **Subnets** *(list) --*

                  The ID for each subnet being used in your private VPC. This subnet is a subset of
                  the a range of IPv4 addresses used by the VPC and is specific to a given
                  availability zone in the VPC’s region. This ID number is preceded by "subnet-",
                  for instance: "subnet-04ccf456919e69055". For more information, see `VPCs and
                  Subnets <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html>`__ .

                  - *(string) --*
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_dominant_language_detection_job(
        self, JobId: str
    ) -> ClientDescribeDominantLanguageDetectionJobResponseTypeDef:
        """
        Gets the properties associated with a dominant language detection job. Use this operation to
        get the status of a detection job.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/comprehend-2017-11-27/DescribeDominantLanguageDetectionJob>`_

        **Request Syntax**
        ::

          response = client.describe_dominant_language_detection_job(
              JobId='string'
          )
        :type JobId: string
        :param JobId: **[REQUIRED]**

          The identifier that Amazon Comprehend generated for the job. The operation returns this
          identifier in its response.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'DominantLanguageDetectionJobProperties': {
                    'JobId': 'string',
                    'JobName': 'string',
                    'JobStatus':
                    'SUBMITTED'|'IN_PROGRESS'|'COMPLETED'|'FAILED'|'STOP_REQUESTED'
                    |'STOPPED',
                    'Message': 'string',
                    'SubmitTime': datetime(2015, 1, 1),
                    'EndTime': datetime(2015, 1, 1),
                    'InputDataConfig': {
                        'S3Uri': 'string',
                        'InputFormat': 'ONE_DOC_PER_FILE'|'ONE_DOC_PER_LINE'
                    },
                    'OutputDataConfig': {
                        'S3Uri': 'string',
                        'KmsKeyId': 'string'
                    },
                    'DataAccessRoleArn': 'string',
                    'VolumeKmsKeyId': 'string',
                    'VpcConfig': {
                        'SecurityGroupIds': [
                            'string',
                        ],
                        'Subnets': [
                            'string',
                        ]
                    }
                }
            }
          **Response Structure**

          - *(dict) --*

            - **DominantLanguageDetectionJobProperties** *(dict) --*

              An object that contains the properties associated with a dominant language detection
              job.

              - **JobId** *(string) --*

                The identifier assigned to the dominant language detection job.

              - **JobName** *(string) --*

                The name that you assigned to the dominant language detection job.

              - **JobStatus** *(string) --*

                The current status of the dominant language detection job. If the status is
                ``FAILED`` , the ``Message`` field shows the reason for the failure.

              - **Message** *(string) --*

                A description for the status of a job.

              - **SubmitTime** *(datetime) --*

                The time that the dominant language detection job was submitted for processing.

              - **EndTime** *(datetime) --*

                The time that the dominant language detection job completed.

              - **InputDataConfig** *(dict) --*

                The input data configuration that you supplied when you created the dominant
                language detection job.

                - **S3Uri** *(string) --*

                  The Amazon S3 URI for the input data. The URI must be in same region as the API
                  endpoint that you are calling. The URI can point to a single input file or it can
                  provide the prefix for a collection of data files.

                  For example, if you use the URI ``S3://bucketName/prefix`` , if the prefix is a
                  single file, Amazon Comprehend uses that file as input. If more than one file
                  begins with the prefix, Amazon Comprehend uses all of them as input.

                - **InputFormat** *(string) --*

                  Specifies how the text in an input file should be processed:

                  * ``ONE_DOC_PER_FILE`` - Each file is considered a separate document. Use this
                  option when you are processing large documents, such as newspaper articles or
                  scientific papers.

                  * ``ONE_DOC_PER_LINE`` - Each line in a file is considered a separate document.
                  Use this option when you are processing many short documents, such as text
                  messages.

              - **OutputDataConfig** *(dict) --*

                The output data configuration that you supplied when you created the dominant
                language detection job.

                - **S3Uri** *(string) --*

                  When you use the ``OutputDataConfig`` object with asynchronous operations, you
                  specify the Amazon S3 location where you want to write the output data. The URI
                  must be in the same region as the API endpoint that you are calling. The location
                  is used as the prefix for the actual location of the output file.

                  When the topic detection job is finished, the service creates an output file in a
                  directory specific to the job. The ``S3Uri`` field contains the location of the
                  output file, called ``output.tar.gz`` . It is a compressed archive that contains
                  the ouput of the operation.

                - **KmsKeyId** *(string) --*

                  ID for the AWS Key Management Service (KMS) key that Amazon Comprehend uses to
                  encrypt the output results from an analysis job. The KmsKeyId can be one of the
                  following formats:

                  * KMS Key ID: ``"1234abcd-12ab-34cd-56ef-1234567890ab"``

                  * Amazon Resource Name (ARN) of a KMS Key:
                  ``"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"``

                  * KMS Key Alias: ``"alias/ExampleAlias"``

                  * ARN of a KMS Key Alias:
                  ``"arn:aws:kms:us-west-2:111122223333:alias/ExampleAlias"``

              - **DataAccessRoleArn** *(string) --*

                The Amazon Resource Name (ARN) that gives Amazon Comprehend read access to your
                input data.

              - **VolumeKmsKeyId** *(string) --*

                ID for the AWS Key Management Service (KMS) key that Amazon Comprehend uses to
                encrypt data on the storage volume attached to the ML compute instance(s) that
                process the analysis job. The VolumeKmsKeyId can be either of the following formats:

                * KMS Key ID: ``"1234abcd-12ab-34cd-56ef-1234567890ab"``

                * Amazon Resource Name (ARN) of a KMS Key:
                ``"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"``

              - **VpcConfig** *(dict) --*

                Configuration parameters for a private Virtual Private Cloud (VPC) containing the
                resources you are using for your dominant language detection job. For more
                information, see `Amazon VPC
                <https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html>`__ .

                - **SecurityGroupIds** *(list) --*

                  The ID number for a security group on an instance of your private VPC. Security
                  groups on your VPC function serve as a virtual firewall to control inbound and
                  outbound traffic and provides security for the resources that you’ll be accessing
                  on the VPC. This ID number is preceded by "sg-", for instance:
                  "sg-03b388029b0a285ea". For more information, see `Security Groups for your VPC
                  <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html>`__ .

                  - *(string) --*

                - **Subnets** *(list) --*

                  The ID for each subnet being used in your private VPC. This subnet is a subset of
                  the a range of IPv4 addresses used by the VPC and is specific to a given
                  availability zone in the VPC’s region. This ID number is preceded by "subnet-",
                  for instance: "subnet-04ccf456919e69055". For more information, see `VPCs and
                  Subnets <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html>`__ .

                  - *(string) --*
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_endpoint(self, EndpointArn: str) -> ClientDescribeEndpointResponseTypeDef:
        """
        Gets the properties associated with a specific endpoint. Use this operation to get the
        status of an endpoint.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/comprehend-2017-11-27/DescribeEndpoint>`_

        **Request Syntax**
        ::

          response = client.describe_endpoint(
              EndpointArn='string'
          )
        :type EndpointArn: string
        :param EndpointArn: **[REQUIRED]**

          The Amazon Resource Number (ARN) of the endpoint being described.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'EndpointProperties': {
                    'EndpointArn': 'string',
                    'Status': 'CREATING'|'DELETING'|'FAILED'|'IN_SERVICE'|'UPDATING',
                    'Message': 'string',
                    'ModelArn': 'string',
                    'DesiredInferenceUnits': 123,
                    'CurrentInferenceUnits': 123,
                    'CreationTime': datetime(2015, 1, 1),
                    'LastModifiedTime': datetime(2015, 1, 1)
                }
            }
          **Response Structure**

          - *(dict) --*

            - **EndpointProperties** *(dict) --*

              Describes information associated with the specific endpoint.

              - **EndpointArn** *(string) --*

                The Amazon Resource Number (ARN) of the endpoint.

              - **Status** *(string) --*

                Specifies the status of the endpoint. Because the endpoint updates and creation are
                asynchronous, so customers will need to wait for the endpoint to be ``Ready`` status
                before making inference requests.

              - **Message** *(string) --*

                Specifies a reason for failure in cases of ``Failed`` status.

              - **ModelArn** *(string) --*

                The Amazon Resource Number (ARN) of the model to which the endpoint is attached.

              - **DesiredInferenceUnits** *(integer) --*

                The desired number of inference units to be used by the model using this endpoint.
                Each inference unit represents of a throughput of 100 characters per second.

              - **CurrentInferenceUnits** *(integer) --*

                The number of inference units currently used by the model using this endpoint.

              - **CreationTime** *(datetime) --*

                The creation date and time of the endpoint.

              - **LastModifiedTime** *(datetime) --*

                The date and time that the endpoint was last modified.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_entities_detection_job(
        self, JobId: str
    ) -> ClientDescribeEntitiesDetectionJobResponseTypeDef:
        """
        Gets the properties associated with an entities detection job. Use this operation to get the
        status of a detection job.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/comprehend-2017-11-27/DescribeEntitiesDetectionJob>`_

        **Request Syntax**
        ::

          response = client.describe_entities_detection_job(
              JobId='string'
          )
        :type JobId: string
        :param JobId: **[REQUIRED]**

          The identifier that Amazon Comprehend generated for the job. The operation returns this
          identifier in its response.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'EntitiesDetectionJobProperties': {
                    'JobId': 'string',
                    'JobName': 'string',
                    'JobStatus':
                    'SUBMITTED'|'IN_PROGRESS'|'COMPLETED'|'FAILED'|'STOP_REQUESTED'
                    |'STOPPED',
                    'Message': 'string',
                    'SubmitTime': datetime(2015, 1, 1),
                    'EndTime': datetime(2015, 1, 1),
                    'EntityRecognizerArn': 'string',
                    'InputDataConfig': {
                        'S3Uri': 'string',
                        'InputFormat': 'ONE_DOC_PER_FILE'|'ONE_DOC_PER_LINE'
                    },
                    'OutputDataConfig': {
                        'S3Uri': 'string',
                        'KmsKeyId': 'string'
                    },
                    'LanguageCode': 'en'|'es'|'fr'|'de'|'it'|'pt'|'ar'|'hi'|'ja'|'ko'|'zh'|'zh-TW',
                    'DataAccessRoleArn': 'string',
                    'VolumeKmsKeyId': 'string',
                    'VpcConfig': {
                        'SecurityGroupIds': [
                            'string',
                        ],
                        'Subnets': [
                            'string',
                        ]
                    }
                }
            }
          **Response Structure**

          - *(dict) --*

            - **EntitiesDetectionJobProperties** *(dict) --*

              An object that contains the properties associated with an entities detection job.

              - **JobId** *(string) --*

                The identifier assigned to the entities detection job.

              - **JobName** *(string) --*

                The name that you assigned the entities detection job.

              - **JobStatus** *(string) --*

                The current status of the entities detection job. If the status is ``FAILED`` , the
                ``Message`` field shows the reason for the failure.

              - **Message** *(string) --*

                A description of the status of a job.

              - **SubmitTime** *(datetime) --*

                The time that the entities detection job was submitted for processing.

              - **EndTime** *(datetime) --*

                The time that the entities detection job completed

              - **EntityRecognizerArn** *(string) --*

                The Amazon Resource Name (ARN) that identifies the entity recognizer.

              - **InputDataConfig** *(dict) --*

                The input data configuration that you supplied when you created the entities
                detection job.

                - **S3Uri** *(string) --*

                  The Amazon S3 URI for the input data. The URI must be in same region as the API
                  endpoint that you are calling. The URI can point to a single input file or it can
                  provide the prefix for a collection of data files.

                  For example, if you use the URI ``S3://bucketName/prefix`` , if the prefix is a
                  single file, Amazon Comprehend uses that file as input. If more than one file
                  begins with the prefix, Amazon Comprehend uses all of them as input.

                - **InputFormat** *(string) --*

                  Specifies how the text in an input file should be processed:

                  * ``ONE_DOC_PER_FILE`` - Each file is considered a separate document. Use this
                  option when you are processing large documents, such as newspaper articles or
                  scientific papers.

                  * ``ONE_DOC_PER_LINE`` - Each line in a file is considered a separate document.
                  Use this option when you are processing many short documents, such as text
                  messages.

              - **OutputDataConfig** *(dict) --*

                The output data configuration that you supplied when you created the entities
                detection job.

                - **S3Uri** *(string) --*

                  When you use the ``OutputDataConfig`` object with asynchronous operations, you
                  specify the Amazon S3 location where you want to write the output data. The URI
                  must be in the same region as the API endpoint that you are calling. The location
                  is used as the prefix for the actual location of the output file.

                  When the topic detection job is finished, the service creates an output file in a
                  directory specific to the job. The ``S3Uri`` field contains the location of the
                  output file, called ``output.tar.gz`` . It is a compressed archive that contains
                  the ouput of the operation.

                - **KmsKeyId** *(string) --*

                  ID for the AWS Key Management Service (KMS) key that Amazon Comprehend uses to
                  encrypt the output results from an analysis job. The KmsKeyId can be one of the
                  following formats:

                  * KMS Key ID: ``"1234abcd-12ab-34cd-56ef-1234567890ab"``

                  * Amazon Resource Name (ARN) of a KMS Key:
                  ``"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"``

                  * KMS Key Alias: ``"alias/ExampleAlias"``

                  * ARN of a KMS Key Alias:
                  ``"arn:aws:kms:us-west-2:111122223333:alias/ExampleAlias"``

              - **LanguageCode** *(string) --*

                The language code of the input documents.

              - **DataAccessRoleArn** *(string) --*

                The Amazon Resource Name (ARN) that gives Amazon Comprehend read access to your
                input data.

              - **VolumeKmsKeyId** *(string) --*

                ID for the AWS Key Management Service (KMS) key that Amazon Comprehend uses to
                encrypt data on the storage volume attached to the ML compute instance(s) that
                process the analysis job. The VolumeKmsKeyId can be either of the following formats:

                * KMS Key ID: ``"1234abcd-12ab-34cd-56ef-1234567890ab"``

                * Amazon Resource Name (ARN) of a KMS Key:
                ``"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"``

              - **VpcConfig** *(dict) --*

                Configuration parameters for a private Virtual Private Cloud (VPC) containing the
                resources you are using for your entity detection job. For more information, see
                `Amazon VPC
                <https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html>`__ .

                - **SecurityGroupIds** *(list) --*

                  The ID number for a security group on an instance of your private VPC. Security
                  groups on your VPC function serve as a virtual firewall to control inbound and
                  outbound traffic and provides security for the resources that you’ll be accessing
                  on the VPC. This ID number is preceded by "sg-", for instance:
                  "sg-03b388029b0a285ea". For more information, see `Security Groups for your VPC
                  <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html>`__ .

                  - *(string) --*

                - **Subnets** *(list) --*

                  The ID for each subnet being used in your private VPC. This subnet is a subset of
                  the a range of IPv4 addresses used by the VPC and is specific to a given
                  availability zone in the VPC’s region. This ID number is preceded by "subnet-",
                  for instance: "subnet-04ccf456919e69055". For more information, see `VPCs and
                  Subnets <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html>`__ .

                  - *(string) --*
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_entity_recognizer(
        self, EntityRecognizerArn: str
    ) -> ClientDescribeEntityRecognizerResponseTypeDef:
        """
        Provides details about an entity recognizer including status, S3 buckets containing training
        data, recognizer metadata, metrics, and so on.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/comprehend-2017-11-27/DescribeEntityRecognizer>`_

        **Request Syntax**
        ::

          response = client.describe_entity_recognizer(
              EntityRecognizerArn='string'
          )
        :type EntityRecognizerArn: string
        :param EntityRecognizerArn: **[REQUIRED]**

          The Amazon Resource Name (ARN) that identifies the entity recognizer.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'EntityRecognizerProperties': {
                    'EntityRecognizerArn': 'string',
                    'LanguageCode': 'en'|'es'|'fr'|'de'|'it'|'pt'|'ar'|'hi'|'ja'|'ko'|'zh'|'zh-TW',
                    'Status':
                    'SUBMITTED'|'TRAINING'|'DELETING'|'STOP_REQUESTED'|'STOPPED'
                    |'IN_ERROR'|'TRAINED',
                    'Message': 'string',
                    'SubmitTime': datetime(2015, 1, 1),
                    'EndTime': datetime(2015, 1, 1),
                    'TrainingStartTime': datetime(2015, 1, 1),
                    'TrainingEndTime': datetime(2015, 1, 1),
                    'InputDataConfig': {
                        'EntityTypes': [
                            {
                                'Type': 'string'
                            },
                        ],
                        'Documents': {
                            'S3Uri': 'string'
                        },
                        'Annotations': {
                            'S3Uri': 'string'
                        },
                        'EntityList': {
                            'S3Uri': 'string'
                        }
                    },
                    'RecognizerMetadata': {
                        'NumberOfTrainedDocuments': 123,
                        'NumberOfTestDocuments': 123,
                        'EvaluationMetrics': {
                            'Precision': 123.0,
                            'Recall': 123.0,
                            'F1Score': 123.0
                        },
                        'EntityTypes': [
                            {
                                'Type': 'string',
                                'EvaluationMetrics': {
                                    'Precision': 123.0,
                                    'Recall': 123.0,
                                    'F1Score': 123.0
                                },
                                'NumberOfTrainMentions': 123
                            },
                        ]
                    },
                    'DataAccessRoleArn': 'string',
                    'VolumeKmsKeyId': 'string',
                    'VpcConfig': {
                        'SecurityGroupIds': [
                            'string',
                        ],
                        'Subnets': [
                            'string',
                        ]
                    }
                }
            }
          **Response Structure**

          - *(dict) --*

            - **EntityRecognizerProperties** *(dict) --*

              Describes information associated with an entity recognizer.

              - **EntityRecognizerArn** *(string) --*

                The Amazon Resource Name (ARN) that identifies the entity recognizer.

              - **LanguageCode** *(string) --*

                The language of the input documents. All documents must be in the same language.
                Only English ("en") is currently supported.

              - **Status** *(string) --*

                Provides the status of the entity recognizer.

              - **Message** *(string) --*

                A description of the status of the recognizer.

              - **SubmitTime** *(datetime) --*

                The time that the recognizer was submitted for processing.

              - **EndTime** *(datetime) --*

                The time that the recognizer creation completed.

              - **TrainingStartTime** *(datetime) --*

                The time that training of the entity recognizer started.

              - **TrainingEndTime** *(datetime) --*

                The time that training of the entity recognizer was completed.

              - **InputDataConfig** *(dict) --*

                The input data properties of an entity recognizer.

                - **EntityTypes** *(list) --*

                  The entity types in the input data for an entity recognizer. A maximum of 12
                  entity types can be used at one time to train an entity recognizer.

                  - *(dict) --*

                    Information about an individual item on a list of entity types.

                    - **Type** *(string) --*

                      Entity type of an item on an entity type list.

                - **Documents** *(dict) --*

                  S3 location of the documents folder for an entity recognizer

                  - **S3Uri** *(string) --*

                    Specifies the Amazon S3 location where the training documents for an entity
                    recognizer are located. The URI must be in the same region as the API endpoint
                    that you are calling.

                - **Annotations** *(dict) --*

                  S3 location of the annotations file for an entity recognizer.

                  - **S3Uri** *(string) --*

                    Specifies the Amazon S3 location where the annotations for an entity recognizer
                    are located. The URI must be in the same region as the API endpoint that you are
                    calling.

                - **EntityList** *(dict) --*

                  S3 location of the entity list for an entity recognizer.

                  - **S3Uri** *(string) --*

                    Specifies the Amazon S3 location where the entity list is located. The URI must
                    be in the same region as the API endpoint that you are calling.

              - **RecognizerMetadata** *(dict) --*

                Provides information about an entity recognizer.

                - **NumberOfTrainedDocuments** *(integer) --*

                  The number of documents in the input data that were used to train the entity
                  recognizer. Typically this is 80 to 90 percent of the input documents.

                - **NumberOfTestDocuments** *(integer) --*

                  The number of documents in the input data that were used to test the entity
                  recognizer. Typically this is 10 to 20 percent of the input documents.

                - **EvaluationMetrics** *(dict) --*

                  Detailed information about the accuracy of an entity recognizer.

                  - **Precision** *(float) --*

                    A measure of the usefulness of the recognizer results in the test data. High
                    precision means that the recognizer returned substantially more relevant results
                    than irrelevant ones.

                  - **Recall** *(float) --*

                    A measure of how complete the recognizer results are for the test data. High
                    recall means that the recognizer returned most of the relevant results.

                  - **F1Score** *(float) --*

                    A measure of how accurate the recognizer results are for the test data. It is
                    derived from the ``Precision`` and ``Recall`` values. The ``F1Score`` is the
                    harmonic average of the two scores. The highest score is 1, and the worst score
                    is 0.

                - **EntityTypes** *(list) --*

                  Entity types from the metadata of an entity recognizer.

                  - *(dict) --*

                    Individual item from the list of entity types in the metadata of an entity
                    recognizer.

                    - **Type** *(string) --*

                      Type of entity from the list of entity types in the metadata of an entity
                      recognizer.

                    - **EvaluationMetrics** *(dict) --*

                      Detailed information about the accuracy of the entity recognizer for a
                      specific item on the list of entity types.

                      - **Precision** *(float) --*

                        A measure of the usefulness of the recognizer results for a specific entity
                        type in the test data. High precision means that the recognizer returned
                        substantially more relevant results than irrelevant ones.

                      - **Recall** *(float) --*

                        A measure of how complete the recognizer results are for a specific entity
                        type in the test data. High recall means that the recognizer returned most
                        of the relevant results.

                      - **F1Score** *(float) --*

                        A measure of how accurate the recognizer results are for for a specific
                        entity type in the test data. It is derived from the ``Precision`` and
                        ``Recall`` values. The ``F1Score`` is the harmonic average of the two
                        scores. The highest score is 1, and the worst score is 0.

                    - **NumberOfTrainMentions** *(integer) --*

                      Indicates the number of times the given entity type was seen in the training
                      data.

              - **DataAccessRoleArn** *(string) --*

                The Amazon Resource Name (ARN) of the AWS Identity and Management (IAM) role that
                grants Amazon Comprehend read access to your input data.

              - **VolumeKmsKeyId** *(string) --*

                ID for the AWS Key Management Service (KMS) key that Amazon Comprehend uses to
                encrypt data on the storage volume attached to the ML compute instance(s) that
                process the analysis job. The VolumeKmsKeyId can be either of the following formats:

                * KMS Key ID: ``"1234abcd-12ab-34cd-56ef-1234567890ab"``

                * Amazon Resource Name (ARN) of a KMS Key:
                ``"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"``

              - **VpcConfig** *(dict) --*

                Configuration parameters for a private Virtual Private Cloud (VPC) containing the
                resources you are using for your custom entity recognizer. For more information, see
                `Amazon VPC
                <https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html>`__ .

                - **SecurityGroupIds** *(list) --*

                  The ID number for a security group on an instance of your private VPC. Security
                  groups on your VPC function serve as a virtual firewall to control inbound and
                  outbound traffic and provides security for the resources that you’ll be accessing
                  on the VPC. This ID number is preceded by "sg-", for instance:
                  "sg-03b388029b0a285ea". For more information, see `Security Groups for your VPC
                  <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html>`__ .

                  - *(string) --*

                - **Subnets** *(list) --*

                  The ID for each subnet being used in your private VPC. This subnet is a subset of
                  the a range of IPv4 addresses used by the VPC and is specific to a given
                  availability zone in the VPC’s region. This ID number is preceded by "subnet-",
                  for instance: "subnet-04ccf456919e69055". For more information, see `VPCs and
                  Subnets <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html>`__ .

                  - *(string) --*
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_key_phrases_detection_job(
        self, JobId: str
    ) -> ClientDescribeKeyPhrasesDetectionJobResponseTypeDef:
        """
        Gets the properties associated with a key phrases detection job. Use this operation to get
        the status of a detection job.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/comprehend-2017-11-27/DescribeKeyPhrasesDetectionJob>`_

        **Request Syntax**
        ::

          response = client.describe_key_phrases_detection_job(
              JobId='string'
          )
        :type JobId: string
        :param JobId: **[REQUIRED]**

          The identifier that Amazon Comprehend generated for the job. The operation returns this
          identifier in its response.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'KeyPhrasesDetectionJobProperties': {
                    'JobId': 'string',
                    'JobName': 'string',
                    'JobStatus':
                    'SUBMITTED'|'IN_PROGRESS'|'COMPLETED'|'FAILED'|'STOP_REQUESTED'
                    |'STOPPED',
                    'Message': 'string',
                    'SubmitTime': datetime(2015, 1, 1),
                    'EndTime': datetime(2015, 1, 1),
                    'InputDataConfig': {
                        'S3Uri': 'string',
                        'InputFormat': 'ONE_DOC_PER_FILE'|'ONE_DOC_PER_LINE'
                    },
                    'OutputDataConfig': {
                        'S3Uri': 'string',
                        'KmsKeyId': 'string'
                    },
                    'LanguageCode': 'en'|'es'|'fr'|'de'|'it'|'pt'|'ar'|'hi'|'ja'|'ko'|'zh'|'zh-TW',
                    'DataAccessRoleArn': 'string',
                    'VolumeKmsKeyId': 'string',
                    'VpcConfig': {
                        'SecurityGroupIds': [
                            'string',
                        ],
                        'Subnets': [
                            'string',
                        ]
                    }
                }
            }
          **Response Structure**

          - *(dict) --*

            - **KeyPhrasesDetectionJobProperties** *(dict) --*

              An object that contains the properties associated with a key phrases detection job.

              - **JobId** *(string) --*

                The identifier assigned to the key phrases detection job.

              - **JobName** *(string) --*

                The name that you assigned the key phrases detection job.

              - **JobStatus** *(string) --*

                The current status of the key phrases detection job. If the status is ``FAILED`` ,
                the ``Message`` field shows the reason for the failure.

              - **Message** *(string) --*

                A description of the status of a job.

              - **SubmitTime** *(datetime) --*

                The time that the key phrases detection job was submitted for processing.

              - **EndTime** *(datetime) --*

                The time that the key phrases detection job completed.

              - **InputDataConfig** *(dict) --*

                The input data configuration that you supplied when you created the key phrases
                detection job.

                - **S3Uri** *(string) --*

                  The Amazon S3 URI for the input data. The URI must be in same region as the API
                  endpoint that you are calling. The URI can point to a single input file or it can
                  provide the prefix for a collection of data files.

                  For example, if you use the URI ``S3://bucketName/prefix`` , if the prefix is a
                  single file, Amazon Comprehend uses that file as input. If more than one file
                  begins with the prefix, Amazon Comprehend uses all of them as input.

                - **InputFormat** *(string) --*

                  Specifies how the text in an input file should be processed:

                  * ``ONE_DOC_PER_FILE`` - Each file is considered a separate document. Use this
                  option when you are processing large documents, such as newspaper articles or
                  scientific papers.

                  * ``ONE_DOC_PER_LINE`` - Each line in a file is considered a separate document.
                  Use this option when you are processing many short documents, such as text
                  messages.

              - **OutputDataConfig** *(dict) --*

                The output data configuration that you supplied when you created the key phrases
                detection job.

                - **S3Uri** *(string) --*

                  When you use the ``OutputDataConfig`` object with asynchronous operations, you
                  specify the Amazon S3 location where you want to write the output data. The URI
                  must be in the same region as the API endpoint that you are calling. The location
                  is used as the prefix for the actual location of the output file.

                  When the topic detection job is finished, the service creates an output file in a
                  directory specific to the job. The ``S3Uri`` field contains the location of the
                  output file, called ``output.tar.gz`` . It is a compressed archive that contains
                  the ouput of the operation.

                - **KmsKeyId** *(string) --*

                  ID for the AWS Key Management Service (KMS) key that Amazon Comprehend uses to
                  encrypt the output results from an analysis job. The KmsKeyId can be one of the
                  following formats:

                  * KMS Key ID: ``"1234abcd-12ab-34cd-56ef-1234567890ab"``

                  * Amazon Resource Name (ARN) of a KMS Key:
                  ``"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"``

                  * KMS Key Alias: ``"alias/ExampleAlias"``

                  * ARN of a KMS Key Alias:
                  ``"arn:aws:kms:us-west-2:111122223333:alias/ExampleAlias"``

              - **LanguageCode** *(string) --*

                The language code of the input documents.

              - **DataAccessRoleArn** *(string) --*

                The Amazon Resource Name (ARN) that gives Amazon Comprehend read access to your
                input data.

              - **VolumeKmsKeyId** *(string) --*

                ID for the AWS Key Management Service (KMS) key that Amazon Comprehend uses to
                encrypt data on the storage volume attached to the ML compute instance(s) that
                process the analysis job. The VolumeKmsKeyId can be either of the following formats:

                * KMS Key ID: ``"1234abcd-12ab-34cd-56ef-1234567890ab"``

                * Amazon Resource Name (ARN) of a KMS Key:
                ``"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"``

              - **VpcConfig** *(dict) --*

                Configuration parameters for a private Virtual Private Cloud (VPC) containing the
                resources you are using for your key phrases detection job. For more information,
                see `Amazon VPC
                <https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html>`__ .

                - **SecurityGroupIds** *(list) --*

                  The ID number for a security group on an instance of your private VPC. Security
                  groups on your VPC function serve as a virtual firewall to control inbound and
                  outbound traffic and provides security for the resources that you’ll be accessing
                  on the VPC. This ID number is preceded by "sg-", for instance:
                  "sg-03b388029b0a285ea". For more information, see `Security Groups for your VPC
                  <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html>`__ .

                  - *(string) --*

                - **Subnets** *(list) --*

                  The ID for each subnet being used in your private VPC. This subnet is a subset of
                  the a range of IPv4 addresses used by the VPC and is specific to a given
                  availability zone in the VPC’s region. This ID number is preceded by "subnet-",
                  for instance: "subnet-04ccf456919e69055". For more information, see `VPCs and
                  Subnets <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html>`__ .

                  - *(string) --*
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_sentiment_detection_job(
        self, JobId: str
    ) -> ClientDescribeSentimentDetectionJobResponseTypeDef:
        """
        Gets the properties associated with a sentiment detection job. Use this operation to get the
        status of a detection job.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/comprehend-2017-11-27/DescribeSentimentDetectionJob>`_

        **Request Syntax**
        ::

          response = client.describe_sentiment_detection_job(
              JobId='string'
          )
        :type JobId: string
        :param JobId: **[REQUIRED]**

          The identifier that Amazon Comprehend generated for the job. The operation returns this
          identifier in its response.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'SentimentDetectionJobProperties': {
                    'JobId': 'string',
                    'JobName': 'string',
                    'JobStatus':
                    'SUBMITTED'|'IN_PROGRESS'|'COMPLETED'|'FAILED'|'STOP_REQUESTED'
                    |'STOPPED',
                    'Message': 'string',
                    'SubmitTime': datetime(2015, 1, 1),
                    'EndTime': datetime(2015, 1, 1),
                    'InputDataConfig': {
                        'S3Uri': 'string',
                        'InputFormat': 'ONE_DOC_PER_FILE'|'ONE_DOC_PER_LINE'
                    },
                    'OutputDataConfig': {
                        'S3Uri': 'string',
                        'KmsKeyId': 'string'
                    },
                    'LanguageCode': 'en'|'es'|'fr'|'de'|'it'|'pt'|'ar'|'hi'|'ja'|'ko'|'zh'|'zh-TW',
                    'DataAccessRoleArn': 'string',
                    'VolumeKmsKeyId': 'string',
                    'VpcConfig': {
                        'SecurityGroupIds': [
                            'string',
                        ],
                        'Subnets': [
                            'string',
                        ]
                    }
                }
            }
          **Response Structure**

          - *(dict) --*

            - **SentimentDetectionJobProperties** *(dict) --*

              An object that contains the properties associated with a sentiment detection job.

              - **JobId** *(string) --*

                The identifier assigned to the sentiment detection job.

              - **JobName** *(string) --*

                The name that you assigned to the sentiment detection job

              - **JobStatus** *(string) --*

                The current status of the sentiment detection job. If the status is ``FAILED`` , the
                ``Messages`` field shows the reason for the failure.

              - **Message** *(string) --*

                A description of the status of a job.

              - **SubmitTime** *(datetime) --*

                The time that the sentiment detection job was submitted for processing.

              - **EndTime** *(datetime) --*

                The time that the sentiment detection job ended.

              - **InputDataConfig** *(dict) --*

                The input data configuration that you supplied when you created the sentiment
                detection job.

                - **S3Uri** *(string) --*

                  The Amazon S3 URI for the input data. The URI must be in same region as the API
                  endpoint that you are calling. The URI can point to a single input file or it can
                  provide the prefix for a collection of data files.

                  For example, if you use the URI ``S3://bucketName/prefix`` , if the prefix is a
                  single file, Amazon Comprehend uses that file as input. If more than one file
                  begins with the prefix, Amazon Comprehend uses all of them as input.

                - **InputFormat** *(string) --*

                  Specifies how the text in an input file should be processed:

                  * ``ONE_DOC_PER_FILE`` - Each file is considered a separate document. Use this
                  option when you are processing large documents, such as newspaper articles or
                  scientific papers.

                  * ``ONE_DOC_PER_LINE`` - Each line in a file is considered a separate document.
                  Use this option when you are processing many short documents, such as text
                  messages.

              - **OutputDataConfig** *(dict) --*

                The output data configuration that you supplied when you created the sentiment
                detection job.

                - **S3Uri** *(string) --*

                  When you use the ``OutputDataConfig`` object with asynchronous operations, you
                  specify the Amazon S3 location where you want to write the output data. The URI
                  must be in the same region as the API endpoint that you are calling. The location
                  is used as the prefix for the actual location of the output file.

                  When the topic detection job is finished, the service creates an output file in a
                  directory specific to the job. The ``S3Uri`` field contains the location of the
                  output file, called ``output.tar.gz`` . It is a compressed archive that contains
                  the ouput of the operation.

                - **KmsKeyId** *(string) --*

                  ID for the AWS Key Management Service (KMS) key that Amazon Comprehend uses to
                  encrypt the output results from an analysis job. The KmsKeyId can be one of the
                  following formats:

                  * KMS Key ID: ``"1234abcd-12ab-34cd-56ef-1234567890ab"``

                  * Amazon Resource Name (ARN) of a KMS Key:
                  ``"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"``

                  * KMS Key Alias: ``"alias/ExampleAlias"``

                  * ARN of a KMS Key Alias:
                  ``"arn:aws:kms:us-west-2:111122223333:alias/ExampleAlias"``

              - **LanguageCode** *(string) --*

                The language code of the input documents.

              - **DataAccessRoleArn** *(string) --*

                The Amazon Resource Name (ARN) that gives Amazon Comprehend read access to your
                input data.

              - **VolumeKmsKeyId** *(string) --*

                ID for the AWS Key Management Service (KMS) key that Amazon Comprehend uses to
                encrypt data on the storage volume attached to the ML compute instance(s) that
                process the analysis job. The VolumeKmsKeyId can be either of the following formats:

                * KMS Key ID: ``"1234abcd-12ab-34cd-56ef-1234567890ab"``

                * Amazon Resource Name (ARN) of a KMS Key:
                ``"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"``

              - **VpcConfig** *(dict) --*

                Configuration parameters for a private Virtual Private Cloud (VPC) containing the
                resources you are using for your sentiment detection job. For more information, see
                `Amazon VPC
                <https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html>`__ .

                - **SecurityGroupIds** *(list) --*

                  The ID number for a security group on an instance of your private VPC. Security
                  groups on your VPC function serve as a virtual firewall to control inbound and
                  outbound traffic and provides security for the resources that you’ll be accessing
                  on the VPC. This ID number is preceded by "sg-", for instance:
                  "sg-03b388029b0a285ea". For more information, see `Security Groups for your VPC
                  <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html>`__ .

                  - *(string) --*

                - **Subnets** *(list) --*

                  The ID for each subnet being used in your private VPC. This subnet is a subset of
                  the a range of IPv4 addresses used by the VPC and is specific to a given
                  availability zone in the VPC’s region. This ID number is preceded by "subnet-",
                  for instance: "subnet-04ccf456919e69055". For more information, see `VPCs and
                  Subnets <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html>`__ .

                  - *(string) --*
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_topics_detection_job(
        self, JobId: str
    ) -> ClientDescribeTopicsDetectionJobResponseTypeDef:
        """
        Gets the properties associated with a topic detection job. Use this operation to get the
        status of a detection job.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/comprehend-2017-11-27/DescribeTopicsDetectionJob>`_

        **Request Syntax**
        ::

          response = client.describe_topics_detection_job(
              JobId='string'
          )
        :type JobId: string
        :param JobId: **[REQUIRED]**

          The identifier assigned by the user to the detection job.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'TopicsDetectionJobProperties': {
                    'JobId': 'string',
                    'JobName': 'string',
                    'JobStatus':
                    'SUBMITTED'|'IN_PROGRESS'|'COMPLETED'|'FAILED'|'STOP_REQUESTED'
                    |'STOPPED',
                    'Message': 'string',
                    'SubmitTime': datetime(2015, 1, 1),
                    'EndTime': datetime(2015, 1, 1),
                    'InputDataConfig': {
                        'S3Uri': 'string',
                        'InputFormat': 'ONE_DOC_PER_FILE'|'ONE_DOC_PER_LINE'
                    },
                    'OutputDataConfig': {
                        'S3Uri': 'string',
                        'KmsKeyId': 'string'
                    },
                    'NumberOfTopics': 123,
                    'DataAccessRoleArn': 'string',
                    'VolumeKmsKeyId': 'string',
                    'VpcConfig': {
                        'SecurityGroupIds': [
                            'string',
                        ],
                        'Subnets': [
                            'string',
                        ]
                    }
                }
            }
          **Response Structure**

          - *(dict) --*

            - **TopicsDetectionJobProperties** *(dict) --*

              The list of properties for the requested job.

              - **JobId** *(string) --*

                The identifier assigned to the topic detection job.

              - **JobName** *(string) --*

                The name of the topic detection job.

              - **JobStatus** *(string) --*

                The current status of the topic detection job. If the status is ``Failed`` , the
                reason for the failure is shown in the ``Message`` field.

              - **Message** *(string) --*

                A description for the status of a job.

              - **SubmitTime** *(datetime) --*

                The time that the topic detection job was submitted for processing.

              - **EndTime** *(datetime) --*

                The time that the topic detection job was completed.

              - **InputDataConfig** *(dict) --*

                The input data configuration supplied when you created the topic detection job.

                - **S3Uri** *(string) --*

                  The Amazon S3 URI for the input data. The URI must be in same region as the API
                  endpoint that you are calling. The URI can point to a single input file or it can
                  provide the prefix for a collection of data files.

                  For example, if you use the URI ``S3://bucketName/prefix`` , if the prefix is a
                  single file, Amazon Comprehend uses that file as input. If more than one file
                  begins with the prefix, Amazon Comprehend uses all of them as input.

                - **InputFormat** *(string) --*

                  Specifies how the text in an input file should be processed:

                  * ``ONE_DOC_PER_FILE`` - Each file is considered a separate document. Use this
                  option when you are processing large documents, such as newspaper articles or
                  scientific papers.

                  * ``ONE_DOC_PER_LINE`` - Each line in a file is considered a separate document.
                  Use this option when you are processing many short documents, such as text
                  messages.

              - **OutputDataConfig** *(dict) --*

                The output data configuration supplied when you created the topic detection job.

                - **S3Uri** *(string) --*

                  When you use the ``OutputDataConfig`` object with asynchronous operations, you
                  specify the Amazon S3 location where you want to write the output data. The URI
                  must be in the same region as the API endpoint that you are calling. The location
                  is used as the prefix for the actual location of the output file.

                  When the topic detection job is finished, the service creates an output file in a
                  directory specific to the job. The ``S3Uri`` field contains the location of the
                  output file, called ``output.tar.gz`` . It is a compressed archive that contains
                  the ouput of the operation.

                - **KmsKeyId** *(string) --*

                  ID for the AWS Key Management Service (KMS) key that Amazon Comprehend uses to
                  encrypt the output results from an analysis job. The KmsKeyId can be one of the
                  following formats:

                  * KMS Key ID: ``"1234abcd-12ab-34cd-56ef-1234567890ab"``

                  * Amazon Resource Name (ARN) of a KMS Key:
                  ``"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"``

                  * KMS Key Alias: ``"alias/ExampleAlias"``

                  * ARN of a KMS Key Alias:
                  ``"arn:aws:kms:us-west-2:111122223333:alias/ExampleAlias"``

              - **NumberOfTopics** *(integer) --*

                The number of topics to detect supplied when you created the topic detection job.
                The default is 10.

              - **DataAccessRoleArn** *(string) --*

                The Amazon Resource Name (ARN) of the AWS Identity and Management (IAM) role that
                grants Amazon Comprehend read access to your job data.

              - **VolumeKmsKeyId** *(string) --*

                ID for the AWS Key Management Service (KMS) key that Amazon Comprehend uses to
                encrypt data on the storage volume attached to the ML compute instance(s) that
                process the analysis job. The VolumeKmsKeyId can be either of the following formats:

                * KMS Key ID: ``"1234abcd-12ab-34cd-56ef-1234567890ab"``

                * Amazon Resource Name (ARN) of a KMS Key:
                ``"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"``

              - **VpcConfig** *(dict) --*

                Configuration parameters for a private Virtual Private Cloud (VPC) containing the
                resources you are using for your topic detection job. For more information, see
                `Amazon VPC
                <https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html>`__ .

                - **SecurityGroupIds** *(list) --*

                  The ID number for a security group on an instance of your private VPC. Security
                  groups on your VPC function serve as a virtual firewall to control inbound and
                  outbound traffic and provides security for the resources that you’ll be accessing
                  on the VPC. This ID number is preceded by "sg-", for instance:
                  "sg-03b388029b0a285ea". For more information, see `Security Groups for your VPC
                  <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html>`__ .

                  - *(string) --*

                - **Subnets** *(list) --*

                  The ID for each subnet being used in your private VPC. This subnet is a subset of
                  the a range of IPv4 addresses used by the VPC and is specific to a given
                  availability zone in the VPC’s region. This ID number is preceded by "subnet-",
                  for instance: "subnet-04ccf456919e69055". For more information, see `VPCs and
                  Subnets <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html>`__ .

                  - *(string) --*
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def detect_dominant_language(self, Text: str) -> ClientDetectDominantLanguageResponseTypeDef:
        """
        Determines the dominant language of the input text. For a list of languages that Amazon
        Comprehend can detect, see `Amazon Comprehend Supported Languages
        <https://docs.aws.amazon.com/comprehend/latest/dg/how-languages.html>`__ .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/comprehend-2017-11-27/DetectDominantLanguage>`_

        **Request Syntax**
        ::

          response = client.detect_dominant_language(
              Text='string'
          )
        :type Text: string
        :param Text: **[REQUIRED]**

          A UTF-8 text string. Each string should contain at least 20 characters and must contain
          fewer that 5,000 bytes of UTF-8 encoded characters.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Languages': [
                    {
                        'LanguageCode': 'string',
                        'Score': ...
                    },
                ]
            }
          **Response Structure**

          - *(dict) --*

            - **Languages** *(list) --*

              The languages that Amazon Comprehend detected in the input text. For each language,
              the response returns the RFC 5646 language code and the level of confidence that
              Amazon Comprehend has in the accuracy of its inference. For more information about RFC
              5646, see `Tags for Identifying Languages <https://tools.ietf.org/html/rfc5646>`__ on
              the *IETF Tools* web site.

              - *(dict) --*

                Returns the code for the dominant language in the input text and the level of
                confidence that Amazon Comprehend has in the accuracy of the detection.

                - **LanguageCode** *(string) --*

                  The RFC 5646 language code for the dominant language. For more information about
                  RFC 5646, see `Tags for Identifying Languages
                  <https://tools.ietf.org/html/rfc5646>`__ on the *IETF Tools* web site.

                - **Score** *(float) --*

                  The level of confidence that Amazon Comprehend has in the accuracy of the
                  detection.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def detect_entities(
        self,
        Text: str,
        LanguageCode: Literal[
            "en", "es", "fr", "de", "it", "pt", "ar", "hi", "ja", "ko", "zh", "zh-TW"
        ],
    ) -> ClientDetectEntitiesResponseTypeDef:
        """
        Inspects text for named entities, and returns information about them. For more information,
        about named entities, see  how-entities .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/comprehend-2017-11-27/DetectEntities>`_

        **Request Syntax**
        ::

          response = client.detect_entities(
              Text='string',
              LanguageCode='en'|'es'|'fr'|'de'|'it'|'pt'|'ar'|'hi'|'ja'|'ko'|'zh'|'zh-TW'
          )
        :type Text: string
        :param Text: **[REQUIRED]**

          A UTF-8 text string. Each string must contain fewer that 5,000 bytes of UTF-8 encoded
          characters.

        :type LanguageCode: string
        :param LanguageCode: **[REQUIRED]**

          The language of the input documents. You can specify any of the primary languages
          supported by Amazon Comprehend. All documents must be in the same language.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Entities': [
                    {
                        'Score': ...,
                        'Type':
                        'PERSON'|'LOCATION'|'ORGANIZATION'|'COMMERCIAL_ITEM'|'EVENT'
                        |'DATE'|'QUANTITY'|'TITLE'|'OTHER',
                        'Text': 'string',
                        'BeginOffset': 123,
                        'EndOffset': 123
                    },
                ]
            }
          **Response Structure**

          - *(dict) --*

            - **Entities** *(list) --*

              A collection of entities identified in the input text. For each entity, the response
              provides the entity text, entity type, where the entity text begins and ends, and the
              level of confidence that Amazon Comprehend has in the detection. For a list of entity
              types, see  how-entities .

              - *(dict) --*

                Provides information about an entity.

                - **Score** *(float) --*

                  The level of confidence that Amazon Comprehend has in the accuracy of the
                  detection.

                - **Type** *(string) --*

                  The entity's type.

                - **Text** *(string) --*

                  The text of the entity.

                - **BeginOffset** *(integer) --*

                  A character offset in the input text that shows where the entity begins (the first
                  character is at position 0). The offset returns the position of each UTF-8 code
                  point in the string. A *code point* is the abstract character from a particular
                  graphical representation. For example, a multi-byte UTF-8 character maps to a
                  single code point.

                - **EndOffset** *(integer) --*

                  A character offset in the input text that shows where the entity ends. The offset
                  returns the position of each UTF-8 code point in the string. A *code point* is the
                  abstract character from a particular graphical representation. For example, a
                  multi-byte UTF-8 character maps to a single code point.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def detect_key_phrases(
        self,
        Text: str,
        LanguageCode: Literal[
            "en", "es", "fr", "de", "it", "pt", "ar", "hi", "ja", "ko", "zh", "zh-TW"
        ],
    ) -> ClientDetectKeyPhrasesResponseTypeDef:
        """
        Detects the key noun phrases found in the text.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/comprehend-2017-11-27/DetectKeyPhrases>`_

        **Request Syntax**
        ::

          response = client.detect_key_phrases(
              Text='string',
              LanguageCode='en'|'es'|'fr'|'de'|'it'|'pt'|'ar'|'hi'|'ja'|'ko'|'zh'|'zh-TW'
          )
        :type Text: string
        :param Text: **[REQUIRED]**

          A UTF-8 text string. Each string must contain fewer that 5,000 bytes of UTF-8 encoded
          characters.

        :type LanguageCode: string
        :param LanguageCode: **[REQUIRED]**

          The language of the input documents. You can specify any of the primary languages
          supported by Amazon Comprehend. All documents must be in the same language.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'KeyPhrases': [
                    {
                        'Score': ...,
                        'Text': 'string',
                        'BeginOffset': 123,
                        'EndOffset': 123
                    },
                ]
            }
          **Response Structure**

          - *(dict) --*

            - **KeyPhrases** *(list) --*

              A collection of key phrases that Amazon Comprehend identified in the input text. For
              each key phrase, the response provides the text of the key phrase, where the key
              phrase begins and ends, and the level of confidence that Amazon Comprehend has in the
              accuracy of the detection.

              - *(dict) --*

                Describes a key noun phrase.

                - **Score** *(float) --*

                  The level of confidence that Amazon Comprehend has in the accuracy of the
                  detection.

                - **Text** *(string) --*

                  The text of a key noun phrase.

                - **BeginOffset** *(integer) --*

                  A character offset in the input text that shows where the key phrase begins (the
                  first character is at position 0). The offset returns the position of each UTF-8
                  code point in the string. A *code point* is the abstract character from a
                  particular graphical representation. For example, a multi-byte UTF-8 character
                  maps to a single code point.

                - **EndOffset** *(integer) --*

                  A character offset in the input text where the key phrase ends. The offset returns
                  the position of each UTF-8 code point in the string. A ``code point`` is the
                  abstract character from a particular graphical representation. For example, a
                  multi-byte UTF-8 character maps to a single code point.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def detect_sentiment(
        self,
        Text: str,
        LanguageCode: Literal[
            "en", "es", "fr", "de", "it", "pt", "ar", "hi", "ja", "ko", "zh", "zh-TW"
        ],
    ) -> ClientDetectSentimentResponseTypeDef:
        """
        Inspects text and returns an inference of the prevailing sentiment (``POSITIVE`` ,
        ``NEUTRAL`` , ``MIXED`` , or ``NEGATIVE`` ).

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/comprehend-2017-11-27/DetectSentiment>`_

        **Request Syntax**
        ::

          response = client.detect_sentiment(
              Text='string',
              LanguageCode='en'|'es'|'fr'|'de'|'it'|'pt'|'ar'|'hi'|'ja'|'ko'|'zh'|'zh-TW'
          )
        :type Text: string
        :param Text: **[REQUIRED]**

          A UTF-8 text string. Each string must contain fewer that 5,000 bytes of UTF-8 encoded
          characters.

        :type LanguageCode: string
        :param LanguageCode: **[REQUIRED]**

          The language of the input documents. You can specify any of the primary languages
          supported by Amazon Comprehend. All documents must be in the same language.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Sentiment': 'POSITIVE'|'NEGATIVE'|'NEUTRAL'|'MIXED',
                'SentimentScore': {
                    'Positive': ...,
                    'Negative': ...,
                    'Neutral': ...,
                    'Mixed': ...
                }
            }
          **Response Structure**

          - *(dict) --*

            - **Sentiment** *(string) --*

              The inferred sentiment that Amazon Comprehend has the highest level of confidence in.

            - **SentimentScore** *(dict) --*

              An object that lists the sentiments, and their corresponding confidence levels.

              - **Positive** *(float) --*

                The level of confidence that Amazon Comprehend has in the accuracy of its detection
                of the ``POSITIVE`` sentiment.

              - **Negative** *(float) --*

                The level of confidence that Amazon Comprehend has in the accuracy of its detection
                of the ``NEGATIVE`` sentiment.

              - **Neutral** *(float) --*

                The level of confidence that Amazon Comprehend has in the accuracy of its detection
                of the ``NEUTRAL`` sentiment.

              - **Mixed** *(float) --*

                The level of confidence that Amazon Comprehend has in the accuracy of its detection
                of the ``MIXED`` sentiment.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def detect_syntax(
        self, Text: str, LanguageCode: Literal["en", "es", "fr", "de", "it", "pt"]
    ) -> ClientDetectSyntaxResponseTypeDef:
        """
        Inspects text for syntax and the part of speech of words in the document. For more
        information,  how-syntax .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/comprehend-2017-11-27/DetectSyntax>`_

        **Request Syntax**
        ::

          response = client.detect_syntax(
              Text='string',
              LanguageCode='en'|'es'|'fr'|'de'|'it'|'pt'
          )
        :type Text: string
        :param Text: **[REQUIRED]**

          A UTF-8 string. Each string must contain fewer that 5,000 bytes of UTF encoded characters.

        :type LanguageCode: string
        :param LanguageCode: **[REQUIRED]**

          The language code of the input documents. You can specify any of the following languages
          supported by Amazon Comprehend: German ("de"), English ("en"), Spanish ("es"), French
          ("fr"), Italian ("it"), or Portuguese ("pt").

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'SyntaxTokens': [
                    {
                        'TokenId': 123,
                        'Text': 'string',
                        'BeginOffset': 123,
                        'EndOffset': 123,
                        'PartOfSpeech': {
                            'Tag':
                            'ADJ'|'ADP'|'ADV'|'AUX'|'CONJ'|'CCONJ'|'DET'|'INTJ'
                            |'NOUN'|'NUM'|'O'|'PART'|'PRON'|'PROPN'|'PUNCT'
                            |'SCONJ'|'SYM'|'VERB',
                            'Score': ...
                        }
                    },
                ]
            }
          **Response Structure**

          - *(dict) --*

            - **SyntaxTokens** *(list) --*

              A collection of syntax tokens describing the text. For each token, the response
              provides the text, the token type, where the text begins and ends, and the level of
              confidence that Amazon Comprehend has that the token is correct. For a list of token
              types, see  how-syntax .

              - *(dict) --*

                Represents a work in the input text that was recognized and assigned a part of
                speech. There is one syntax token record for each word in the source text.

                - **TokenId** *(integer) --*

                  A unique identifier for a token.

                - **Text** *(string) --*

                  The word that was recognized in the source text.

                - **BeginOffset** *(integer) --*

                  The zero-based offset from the beginning of the source text to the first character
                  in the word.

                - **EndOffset** *(integer) --*

                  The zero-based offset from the beginning of the source text to the last character
                  in the word.

                - **PartOfSpeech** *(dict) --*

                  Provides the part of speech label and the confidence level that Amazon Comprehend
                  has that the part of speech was correctly identified. For more information, see
                  how-syntax .

                  - **Tag** *(string) --*

                    Identifies the part of speech that the token represents.

                  - **Score** *(float) --*

                    The confidence that Amazon Comprehend has that the part of speech was correctly
                    identified.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> None:
        """
        Generate a presigned url given a client, its method, and arguments

        :type ClientMethod: string
        :param ClientMethod: The client method to presign for

        :type Params: dict
        :param Params: The parameters normally passed to
            ``ClientMethod``.

        :type ExpiresIn: int
        :param ExpiresIn: The number of seconds the presigned url is valid
            for. By default it expires in an hour (3600 seconds)

        :type HttpMethod: string
        :param HttpMethod: The http method to use on the generated url. By
            default, the http method is whatever is used in the method's model.

        :returns: The presigned url
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_document_classification_jobs(
        self,
        Filter: ClientListDocumentClassificationJobsFilterTypeDef = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ClientListDocumentClassificationJobsResponseTypeDef:
        """
        Gets a list of the documentation classification jobs that you have submitted.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/comprehend-2017-11-27/ListDocumentClassificationJobs>`_

        **Request Syntax**
        ::

          response = client.list_document_classification_jobs(
              Filter={
                  'JobName': 'string',
                  'JobStatus':
                  'SUBMITTED'|'IN_PROGRESS'|'COMPLETED'|'FAILED'|'STOP_REQUESTED'
                  |'STOPPED',
                  'SubmitTimeBefore': datetime(2015, 1, 1),
                  'SubmitTimeAfter': datetime(2015, 1, 1)
              },
              NextToken='string',
              MaxResults=123
          )
        :type Filter: dict
        :param Filter:

          Filters the jobs that are returned. You can filter jobs on their names, status, or the
          date and time that they were submitted. You can only set one filter at a time.

          - **JobName** *(string) --*

            Filters on the name of the job.

          - **JobStatus** *(string) --*

            Filters the list based on job status. Returns only jobs with the specified status.

          - **SubmitTimeBefore** *(datetime) --*

            Filters the list of jobs based on the time that the job was submitted for processing.
            Returns only jobs submitted after the specified time. Jobs are returned in ascending
            order, oldest to newest.

          - **SubmitTimeAfter** *(datetime) --*

            Filters the list of jobs based on the time that the job was submitted for processing.
            Returns only jobs submitted before the specified time. Jobs are returned in descending
            order, newest to oldest.

        :type NextToken: string
        :param NextToken:

          Identifies the next page of results to return.

        :type MaxResults: integer
        :param MaxResults:

          The maximum number of results to return in each page. The default is 100.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'DocumentClassificationJobPropertiesList': [
                    {
                        'JobId': 'string',
                        'JobName': 'string',
                        'JobStatus':
                        'SUBMITTED'|'IN_PROGRESS'|'COMPLETED'|'FAILED'
                        |'STOP_REQUESTED'|'STOPPED',
                        'Message': 'string',
                        'SubmitTime': datetime(2015, 1, 1),
                        'EndTime': datetime(2015, 1, 1),
                        'DocumentClassifierArn': 'string',
                        'InputDataConfig': {
                            'S3Uri': 'string',
                            'InputFormat': 'ONE_DOC_PER_FILE'|'ONE_DOC_PER_LINE'
                        },
                        'OutputDataConfig': {
                            'S3Uri': 'string',
                            'KmsKeyId': 'string'
                        },
                        'DataAccessRoleArn': 'string',
                        'VolumeKmsKeyId': 'string',
                        'VpcConfig': {
                            'SecurityGroupIds': [
                                'string',
                            ],
                            'Subnets': [
                                'string',
                            ]
                        }
                    },
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **DocumentClassificationJobPropertiesList** *(list) --*

              A list containing the properties of each job returned.

              - *(dict) --*

                Provides information about a document classification job.

                - **JobId** *(string) --*

                  The identifier assigned to the document classification job.

                - **JobName** *(string) --*

                  The name that you assigned to the document classification job.

                - **JobStatus** *(string) --*

                  The current status of the document classification job. If the status is ``FAILED``
                  , the ``Message`` field shows the reason for the failure.

                - **Message** *(string) --*

                  A description of the status of the job.

                - **SubmitTime** *(datetime) --*

                  The time that the document classification job was submitted for processing.

                - **EndTime** *(datetime) --*

                  The time that the document classification job completed.

                - **DocumentClassifierArn** *(string) --*

                  The Amazon Resource Name (ARN) that identifies the document classifier.

                - **InputDataConfig** *(dict) --*

                  The input data configuration that you supplied when you created the document
                  classification job.

                  - **S3Uri** *(string) --*

                    The Amazon S3 URI for the input data. The URI must be in same region as the API
                    endpoint that you are calling. The URI can point to a single input file or it
                    can provide the prefix for a collection of data files.

                    For example, if you use the URI ``S3://bucketName/prefix`` , if the prefix is a
                    single file, Amazon Comprehend uses that file as input. If more than one file
                    begins with the prefix, Amazon Comprehend uses all of them as input.

                  - **InputFormat** *(string) --*

                    Specifies how the text in an input file should be processed:

                    * ``ONE_DOC_PER_FILE`` - Each file is considered a separate document. Use this
                    option when you are processing large documents, such as newspaper articles or
                    scientific papers.

                    * ``ONE_DOC_PER_LINE`` - Each line in a file is considered a separate document.
                    Use this option when you are processing many short documents, such as text
                    messages.

                - **OutputDataConfig** *(dict) --*

                  The output data configuration that you supplied when you created the document
                  classification job.

                  - **S3Uri** *(string) --*

                    When you use the ``OutputDataConfig`` object with asynchronous operations, you
                    specify the Amazon S3 location where you want to write the output data. The URI
                    must be in the same region as the API endpoint that you are calling. The
                    location is used as the prefix for the actual location of the output file.

                    When the topic detection job is finished, the service creates an output file in
                    a directory specific to the job. The ``S3Uri`` field contains the location of
                    the output file, called ``output.tar.gz`` . It is a compressed archive that
                    contains the ouput of the operation.

                  - **KmsKeyId** *(string) --*

                    ID for the AWS Key Management Service (KMS) key that Amazon Comprehend uses to
                    encrypt the output results from an analysis job. The KmsKeyId can be one of the
                    following formats:

                    * KMS Key ID: ``"1234abcd-12ab-34cd-56ef-1234567890ab"``

                    * Amazon Resource Name (ARN) of a KMS Key:
                    ``"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"``

                    * KMS Key Alias: ``"alias/ExampleAlias"``

                    * ARN of a KMS Key Alias:
                    ``"arn:aws:kms:us-west-2:111122223333:alias/ExampleAlias"``

                - **DataAccessRoleArn** *(string) --*

                  The Amazon Resource Name (ARN) of the AWS identity and Access Management (IAM)
                  role that grants Amazon Comprehend read access to your input data.

                - **VolumeKmsKeyId** *(string) --*

                  ID for the AWS Key Management Service (KMS) key that Amazon Comprehend uses to
                  encrypt data on the storage volume attached to the ML compute instance(s) that
                  process the analysis job. The VolumeKmsKeyId can be either of the following
                  formats:

                  * KMS Key ID: ``"1234abcd-12ab-34cd-56ef-1234567890ab"``

                  * Amazon Resource Name (ARN) of a KMS Key:
                  ``"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"``

                - **VpcConfig** *(dict) --*

                  Configuration parameters for a private Virtual Private Cloud (VPC) containing the
                  resources you are using for your document classification job. For more
                  information, see `Amazon VPC
                  <https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html>`__ .

                  - **SecurityGroupIds** *(list) --*

                    The ID number for a security group on an instance of your private VPC. Security
                    groups on your VPC function serve as a virtual firewall to control inbound and
                    outbound traffic and provides security for the resources that you’ll be
                    accessing on the VPC. This ID number is preceded by "sg-", for instance:
                    "sg-03b388029b0a285ea". For more information, see `Security Groups for your VPC
                    <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html>`__ .

                    - *(string) --*

                  - **Subnets** *(list) --*

                    The ID for each subnet being used in your private VPC. This subnet is a subset
                    of the a range of IPv4 addresses used by the VPC and is specific to a given
                    availability zone in the VPC’s region. This ID number is preceded by "subnet-",
                    for instance: "subnet-04ccf456919e69055". For more information, see `VPCs and
                    Subnets <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html>`__ .

                    - *(string) --*

            - **NextToken** *(string) --*

              Identifies the next page of results to return.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_document_classifiers(
        self,
        Filter: ClientListDocumentClassifiersFilterTypeDef = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ClientListDocumentClassifiersResponseTypeDef:
        """
        Gets a list of the document classifiers that you have created.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/comprehend-2017-11-27/ListDocumentClassifiers>`_

        **Request Syntax**
        ::

          response = client.list_document_classifiers(
              Filter={
                  'Status':
                  'SUBMITTED'|'TRAINING'|'DELETING'|'STOP_REQUESTED'|'STOPPED'|'IN_ERROR'
                  |'TRAINED',
                  'SubmitTimeBefore': datetime(2015, 1, 1),
                  'SubmitTimeAfter': datetime(2015, 1, 1)
              },
              NextToken='string',
              MaxResults=123
          )
        :type Filter: dict
        :param Filter:

          Filters the jobs that are returned. You can filter jobs on their name, status, or the date
          and time that they were submitted. You can only set one filter at a time.

          - **Status** *(string) --*

            Filters the list of classifiers based on status.

          - **SubmitTimeBefore** *(datetime) --*

            Filters the list of classifiers based on the time that the classifier was submitted for
            processing. Returns only classifiers submitted before the specified time. Classifiers
            are returned in ascending order, oldest to newest.

          - **SubmitTimeAfter** *(datetime) --*

            Filters the list of classifiers based on the time that the classifier was submitted for
            processing. Returns only classifiers submitted after the specified time. Classifiers are
            returned in descending order, newest to oldest.

        :type NextToken: string
        :param NextToken:

          Identifies the next page of results to return.

        :type MaxResults: integer
        :param MaxResults:

          The maximum number of results to return in each page. The default is 100.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'DocumentClassifierPropertiesList': [
                    {
                        'DocumentClassifierArn': 'string',
                        'LanguageCode':
                        'en'|'es'|'fr'|'de'|'it'|'pt'|'ar'|'hi'|'ja'|'ko'|'zh'
                        |'zh-TW',
                        'Status':
                        'SUBMITTED'|'TRAINING'|'DELETING'|'STOP_REQUESTED'|'STOPPED'
                        |'IN_ERROR'|'TRAINED',
                        'Message': 'string',
                        'SubmitTime': datetime(2015, 1, 1),
                        'EndTime': datetime(2015, 1, 1),
                        'TrainingStartTime': datetime(2015, 1, 1),
                        'TrainingEndTime': datetime(2015, 1, 1),
                        'InputDataConfig': {
                            'S3Uri': 'string'
                        },
                        'OutputDataConfig': {
                            'S3Uri': 'string',
                            'KmsKeyId': 'string'
                        },
                        'ClassifierMetadata': {
                            'NumberOfLabels': 123,
                            'NumberOfTrainedDocuments': 123,
                            'NumberOfTestDocuments': 123,
                            'EvaluationMetrics': {
                                'Accuracy': 123.0,
                                'Precision': 123.0,
                                'Recall': 123.0,
                                'F1Score': 123.0
                            }
                        },
                        'DataAccessRoleArn': 'string',
                        'VolumeKmsKeyId': 'string',
                        'VpcConfig': {
                            'SecurityGroupIds': [
                                'string',
                            ],
                            'Subnets': [
                                'string',
                            ]
                        }
                    },
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **DocumentClassifierPropertiesList** *(list) --*

              A list containing the properties of each job returned.

              - *(dict) --*

                Provides information about a document classifier.

                - **DocumentClassifierArn** *(string) --*

                  The Amazon Resource Name (ARN) that identifies the document classifier.

                - **LanguageCode** *(string) --*

                  The language code for the language of the documents that the classifier was
                  trained on.

                - **Status** *(string) --*

                  The status of the document classifier. If the status is ``TRAINED`` the classifier
                  is ready to use. If the status is ``FAILED`` you can see additional information
                  about why the classifier wasn't trained in the ``Message`` field.

                - **Message** *(string) --*

                  Additional information about the status of the classifier.

                - **SubmitTime** *(datetime) --*

                  The time that the document classifier was submitted for training.

                - **EndTime** *(datetime) --*

                  The time that training the document classifier completed.

                - **TrainingStartTime** *(datetime) --*

                  Indicates the time when the training starts on documentation classifiers. You are
                  billed for the time interval between this time and the value of TrainingEndTime.

                - **TrainingEndTime** *(datetime) --*

                  The time that training of the document classifier was completed. Indicates the
                  time when the training completes on documentation classifiers. You are billed for
                  the time interval between this time and the value of TrainingStartTime.

                - **InputDataConfig** *(dict) --*

                  The input data configuration that you supplied when you created the document
                  classifier for training.

                  - **S3Uri** *(string) --*

                    The Amazon S3 URI for the input data. The S3 bucket must be in the same region
                    as the API endpoint that you are calling. The URI can point to a single input
                    file or it can provide the prefix for a collection of input files.

                    For example, if you use the URI ``S3://bucketName/prefix`` , if the prefix is a
                    single file, Amazon Comprehend uses that file as input. If more than one file
                    begins with the prefix, Amazon Comprehend uses all of them as input.

                - **OutputDataConfig** *(dict) --*

                  Provides output results configuration parameters for custom classifier jobs.

                  - **S3Uri** *(string) --*

                    When you use the ``OutputDataConfig`` object while creating a custom classifier,
                    you specify the Amazon S3 location where you want to write the confusion matrix.
                    The URI must be in the same region as the API endpoint that you are calling. The
                    location is used as the prefix for the actual location of this output file.

                    When the custom classifier job is finished, the service creates the output file
                    in a directory specific to the job. The ``S3Uri`` field contains the location of
                    the output file, called ``output.tar.gz`` . It is a compressed archive that
                    contains the confusion matrix.

                  - **KmsKeyId** *(string) --*

                    ID for the AWS Key Management Service (KMS) key that Amazon Comprehend uses to
                    encrypt the output results from an analysis job. The KmsKeyId can be one of the
                    following formats:

                    * KMS Key ID: ``"1234abcd-12ab-34cd-56ef-1234567890ab"``

                    * Amazon Resource Name (ARN) of a KMS Key:
                    ``"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"``

                    * KMS Key Alias: ``"alias/ExampleAlias"``

                    * ARN of a KMS Key Alias:
                    ``"arn:aws:kms:us-west-2:111122223333:alias/ExampleAlias"``

                - **ClassifierMetadata** *(dict) --*

                  Information about the document classifier, including the number of documents used
                  for training the classifier, the number of documents used for test the classifier,
                  and an accuracy rating.

                  - **NumberOfLabels** *(integer) --*

                    The number of labels in the input data.

                  - **NumberOfTrainedDocuments** *(integer) --*

                    The number of documents in the input data that were used to train the
                    classifier. Typically this is 80 to 90 percent of the input documents.

                  - **NumberOfTestDocuments** *(integer) --*

                    The number of documents in the input data that were used to test the classifier.
                    Typically this is 10 to 20 percent of the input documents.

                  - **EvaluationMetrics** *(dict) --*

                    Describes the result metrics for the test data associated with an documentation
                    classifier.

                    - **Accuracy** *(float) --*

                      The fraction of the labels that were correct recognized. It is computed by
                      dividing the number of labels in the test documents that were correctly
                      recognized by the total number of labels in the test documents.

                    - **Precision** *(float) --*

                      A measure of the usefulness of the classifier results in the test data. High
                      precision means that the classifier returned substantially more relevant
                      results than irrelevant ones.

                    - **Recall** *(float) --*

                      A measure of how complete the classifier results are for the test data. High
                      recall means that the classifier returned most of the relevant results.

                    - **F1Score** *(float) --*

                      A measure of how accurate the classifier results are for the test data. It is
                      derived from the ``Precision`` and ``Recall`` values. The ``F1Score`` is the
                      harmonic average of the two scores. The highest score is 1, and the worst
                      score is 0.

                - **DataAccessRoleArn** *(string) --*

                  The Amazon Resource Name (ARN) of the AWS Identity and Management (IAM) role that
                  grants Amazon Comprehend read access to your input data.

                - **VolumeKmsKeyId** *(string) --*

                  ID for the AWS Key Management Service (KMS) key that Amazon Comprehend uses to
                  encrypt data on the storage volume attached to the ML compute instance(s) that
                  process the analysis job. The VolumeKmsKeyId can be either of the following
                  formats:

                  * KMS Key ID: ``"1234abcd-12ab-34cd-56ef-1234567890ab"``

                  * Amazon Resource Name (ARN) of a KMS Key:
                  ``"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"``

                - **VpcConfig** *(dict) --*

                  Configuration parameters for a private Virtual Private Cloud (VPC) containing the
                  resources you are using for your custom classifier. For more information, see
                  `Amazon VPC
                  <https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html>`__ .

                  - **SecurityGroupIds** *(list) --*

                    The ID number for a security group on an instance of your private VPC. Security
                    groups on your VPC function serve as a virtual firewall to control inbound and
                    outbound traffic and provides security for the resources that you’ll be
                    accessing on the VPC. This ID number is preceded by "sg-", for instance:
                    "sg-03b388029b0a285ea". For more information, see `Security Groups for your VPC
                    <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html>`__ .

                    - *(string) --*

                  - **Subnets** *(list) --*

                    The ID for each subnet being used in your private VPC. This subnet is a subset
                    of the a range of IPv4 addresses used by the VPC and is specific to a given
                    availability zone in the VPC’s region. This ID number is preceded by "subnet-",
                    for instance: "subnet-04ccf456919e69055". For more information, see `VPCs and
                    Subnets <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html>`__ .

                    - *(string) --*

            - **NextToken** *(string) --*

              Identifies the next page of results to return.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_dominant_language_detection_jobs(
        self,
        Filter: ClientListDominantLanguageDetectionJobsFilterTypeDef = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ClientListDominantLanguageDetectionJobsResponseTypeDef:
        """
        Gets a list of the dominant language detection jobs that you have submitted.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/comprehend-2017-11-27/ListDominantLanguageDetectionJobs>`_

        **Request Syntax**
        ::

          response = client.list_dominant_language_detection_jobs(
              Filter={
                  'JobName': 'string',
                  'JobStatus':
                  'SUBMITTED'|'IN_PROGRESS'|'COMPLETED'|'FAILED'|'STOP_REQUESTED'
                  |'STOPPED',
                  'SubmitTimeBefore': datetime(2015, 1, 1),
                  'SubmitTimeAfter': datetime(2015, 1, 1)
              },
              NextToken='string',
              MaxResults=123
          )
        :type Filter: dict
        :param Filter:

          Filters that jobs that are returned. You can filter jobs on their name, status, or the
          date and time that they were submitted. You can only set one filter at a time.

          - **JobName** *(string) --*

            Filters on the name of the job.

          - **JobStatus** *(string) --*

            Filters the list of jobs based on job status. Returns only jobs with the specified
            status.

          - **SubmitTimeBefore** *(datetime) --*

            Filters the list of jobs based on the time that the job was submitted for processing.
            Returns only jobs submitted before the specified time. Jobs are returned in ascending
            order, oldest to newest.

          - **SubmitTimeAfter** *(datetime) --*

            Filters the list of jobs based on the time that the job was submitted for processing.
            Returns only jobs submitted after the specified time. Jobs are returned in descending
            order, newest to oldest.

        :type NextToken: string
        :param NextToken:

          Identifies the next page of results to return.

        :type MaxResults: integer
        :param MaxResults:

          The maximum number of results to return in each page. The default is 100.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'DominantLanguageDetectionJobPropertiesList': [
                    {
                        'JobId': 'string',
                        'JobName': 'string',
                        'JobStatus':
                        'SUBMITTED'|'IN_PROGRESS'|'COMPLETED'|'FAILED'
                        |'STOP_REQUESTED'|'STOPPED',
                        'Message': 'string',
                        'SubmitTime': datetime(2015, 1, 1),
                        'EndTime': datetime(2015, 1, 1),
                        'InputDataConfig': {
                            'S3Uri': 'string',
                            'InputFormat': 'ONE_DOC_PER_FILE'|'ONE_DOC_PER_LINE'
                        },
                        'OutputDataConfig': {
                            'S3Uri': 'string',
                            'KmsKeyId': 'string'
                        },
                        'DataAccessRoleArn': 'string',
                        'VolumeKmsKeyId': 'string',
                        'VpcConfig': {
                            'SecurityGroupIds': [
                                'string',
                            ],
                            'Subnets': [
                                'string',
                            ]
                        }
                    },
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **DominantLanguageDetectionJobPropertiesList** *(list) --*

              A list containing the properties of each job that is returned.

              - *(dict) --*

                Provides information about a dominant language detection job.

                - **JobId** *(string) --*

                  The identifier assigned to the dominant language detection job.

                - **JobName** *(string) --*

                  The name that you assigned to the dominant language detection job.

                - **JobStatus** *(string) --*

                  The current status of the dominant language detection job. If the status is
                  ``FAILED`` , the ``Message`` field shows the reason for the failure.

                - **Message** *(string) --*

                  A description for the status of a job.

                - **SubmitTime** *(datetime) --*

                  The time that the dominant language detection job was submitted for processing.

                - **EndTime** *(datetime) --*

                  The time that the dominant language detection job completed.

                - **InputDataConfig** *(dict) --*

                  The input data configuration that you supplied when you created the dominant
                  language detection job.

                  - **S3Uri** *(string) --*

                    The Amazon S3 URI for the input data. The URI must be in same region as the API
                    endpoint that you are calling. The URI can point to a single input file or it
                    can provide the prefix for a collection of data files.

                    For example, if you use the URI ``S3://bucketName/prefix`` , if the prefix is a
                    single file, Amazon Comprehend uses that file as input. If more than one file
                    begins with the prefix, Amazon Comprehend uses all of them as input.

                  - **InputFormat** *(string) --*

                    Specifies how the text in an input file should be processed:

                    * ``ONE_DOC_PER_FILE`` - Each file is considered a separate document. Use this
                    option when you are processing large documents, such as newspaper articles or
                    scientific papers.

                    * ``ONE_DOC_PER_LINE`` - Each line in a file is considered a separate document.
                    Use this option when you are processing many short documents, such as text
                    messages.

                - **OutputDataConfig** *(dict) --*

                  The output data configuration that you supplied when you created the dominant
                  language detection job.

                  - **S3Uri** *(string) --*

                    When you use the ``OutputDataConfig`` object with asynchronous operations, you
                    specify the Amazon S3 location where you want to write the output data. The URI
                    must be in the same region as the API endpoint that you are calling. The
                    location is used as the prefix for the actual location of the output file.

                    When the topic detection job is finished, the service creates an output file in
                    a directory specific to the job. The ``S3Uri`` field contains the location of
                    the output file, called ``output.tar.gz`` . It is a compressed archive that
                    contains the ouput of the operation.

                  - **KmsKeyId** *(string) --*

                    ID for the AWS Key Management Service (KMS) key that Amazon Comprehend uses to
                    encrypt the output results from an analysis job. The KmsKeyId can be one of the
                    following formats:

                    * KMS Key ID: ``"1234abcd-12ab-34cd-56ef-1234567890ab"``

                    * Amazon Resource Name (ARN) of a KMS Key:
                    ``"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"``

                    * KMS Key Alias: ``"alias/ExampleAlias"``

                    * ARN of a KMS Key Alias:
                    ``"arn:aws:kms:us-west-2:111122223333:alias/ExampleAlias"``

                - **DataAccessRoleArn** *(string) --*

                  The Amazon Resource Name (ARN) that gives Amazon Comprehend read access to your
                  input data.

                - **VolumeKmsKeyId** *(string) --*

                  ID for the AWS Key Management Service (KMS) key that Amazon Comprehend uses to
                  encrypt data on the storage volume attached to the ML compute instance(s) that
                  process the analysis job. The VolumeKmsKeyId can be either of the following
                  formats:

                  * KMS Key ID: ``"1234abcd-12ab-34cd-56ef-1234567890ab"``

                  * Amazon Resource Name (ARN) of a KMS Key:
                  ``"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"``

                - **VpcConfig** *(dict) --*

                  Configuration parameters for a private Virtual Private Cloud (VPC) containing the
                  resources you are using for your dominant language detection job. For more
                  information, see `Amazon VPC
                  <https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html>`__ .

                  - **SecurityGroupIds** *(list) --*

                    The ID number for a security group on an instance of your private VPC. Security
                    groups on your VPC function serve as a virtual firewall to control inbound and
                    outbound traffic and provides security for the resources that you’ll be
                    accessing on the VPC. This ID number is preceded by "sg-", for instance:
                    "sg-03b388029b0a285ea". For more information, see `Security Groups for your VPC
                    <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html>`__ .

                    - *(string) --*

                  - **Subnets** *(list) --*

                    The ID for each subnet being used in your private VPC. This subnet is a subset
                    of the a range of IPv4 addresses used by the VPC and is specific to a given
                    availability zone in the VPC’s region. This ID number is preceded by "subnet-",
                    for instance: "subnet-04ccf456919e69055". For more information, see `VPCs and
                    Subnets <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html>`__ .

                    - *(string) --*

            - **NextToken** *(string) --*

              Identifies the next page of results to return.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_endpoints(
        self,
        Filter: ClientListEndpointsFilterTypeDef = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ClientListEndpointsResponseTypeDef:
        """
        Gets a list of all existing endpoints that you've created.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/comprehend-2017-11-27/ListEndpoints>`_

        **Request Syntax**
        ::

          response = client.list_endpoints(
              Filter={
                  'ModelArn': 'string',
                  'Status': 'CREATING'|'DELETING'|'FAILED'|'IN_SERVICE'|'UPDATING',
                  'CreationTimeBefore': datetime(2015, 1, 1),
                  'CreationTimeAfter': datetime(2015, 1, 1)
              },
              NextToken='string',
              MaxResults=123
          )
        :type Filter: dict
        :param Filter:

          Filters the endpoints that are returned. You can filter endpoints on their name, model,
          status, or the date and time that they were created. You can only set one filter at a
          time.

          - **ModelArn** *(string) --*

            The Amazon Resource Number (ARN) of the model to which the endpoint is attached.

          - **Status** *(string) --*

            Specifies the status of the endpoint being returned. Possible values are: Creating,
            Ready, Updating, Deleting, Failed.

          - **CreationTimeBefore** *(datetime) --*

            Specifies a date before which the returned endpoint or endpoints were created.

          - **CreationTimeAfter** *(datetime) --*

            Specifies a date after which the returned endpoint or endpoints were created.

        :type NextToken: string
        :param NextToken:

          Identifies the next page of results to return.

        :type MaxResults: integer
        :param MaxResults:

          The maximum number of results to return in each page. The default is 100.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'EndpointPropertiesList': [
                    {
                        'EndpointArn': 'string',
                        'Status': 'CREATING'|'DELETING'|'FAILED'|'IN_SERVICE'|'UPDATING',
                        'Message': 'string',
                        'ModelArn': 'string',
                        'DesiredInferenceUnits': 123,
                        'CurrentInferenceUnits': 123,
                        'CreationTime': datetime(2015, 1, 1),
                        'LastModifiedTime': datetime(2015, 1, 1)
                    },
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **EndpointPropertiesList** *(list) --*

              Displays a list of endpoint properties being retrieved by the service in response to
              the request.

              - *(dict) --*

                Specifies information about the specified endpoint.

                - **EndpointArn** *(string) --*

                  The Amazon Resource Number (ARN) of the endpoint.

                - **Status** *(string) --*

                  Specifies the status of the endpoint. Because the endpoint updates and creation
                  are asynchronous, so customers will need to wait for the endpoint to be ``Ready``
                  status before making inference requests.

                - **Message** *(string) --*

                  Specifies a reason for failure in cases of ``Failed`` status.

                - **ModelArn** *(string) --*

                  The Amazon Resource Number (ARN) of the model to which the endpoint is attached.

                - **DesiredInferenceUnits** *(integer) --*

                  The desired number of inference units to be used by the model using this endpoint.
                  Each inference unit represents of a throughput of 100 characters per second.

                - **CurrentInferenceUnits** *(integer) --*

                  The number of inference units currently used by the model using this endpoint.

                - **CreationTime** *(datetime) --*

                  The creation date and time of the endpoint.

                - **LastModifiedTime** *(datetime) --*

                  The date and time that the endpoint was last modified.

            - **NextToken** *(string) --*

              Identifies the next page of results to return.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_entities_detection_jobs(
        self,
        Filter: ClientListEntitiesDetectionJobsFilterTypeDef = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ClientListEntitiesDetectionJobsResponseTypeDef:
        """
        Gets a list of the entity detection jobs that you have submitted.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/comprehend-2017-11-27/ListEntitiesDetectionJobs>`_

        **Request Syntax**
        ::

          response = client.list_entities_detection_jobs(
              Filter={
                  'JobName': 'string',
                  'JobStatus':
                  'SUBMITTED'|'IN_PROGRESS'|'COMPLETED'|'FAILED'|'STOP_REQUESTED'
                  |'STOPPED',
                  'SubmitTimeBefore': datetime(2015, 1, 1),
                  'SubmitTimeAfter': datetime(2015, 1, 1)
              },
              NextToken='string',
              MaxResults=123
          )
        :type Filter: dict
        :param Filter:

          Filters the jobs that are returned. You can filter jobs on their name, status, or the date
          and time that they were submitted. You can only set one filter at a time.

          - **JobName** *(string) --*

            Filters on the name of the job.

          - **JobStatus** *(string) --*

            Filters the list of jobs based on job status. Returns only jobs with the specified
            status.

          - **SubmitTimeBefore** *(datetime) --*

            Filters the list of jobs based on the time that the job was submitted for processing.
            Returns only jobs submitted before the specified time. Jobs are returned in ascending
            order, oldest to newest.

          - **SubmitTimeAfter** *(datetime) --*

            Filters the list of jobs based on the time that the job was submitted for processing.
            Returns only jobs submitted after the specified time. Jobs are returned in descending
            order, newest to oldest.

        :type NextToken: string
        :param NextToken:

          Identifies the next page of results to return.

        :type MaxResults: integer
        :param MaxResults:

          The maximum number of results to return in each page. The default is 100.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'EntitiesDetectionJobPropertiesList': [
                    {
                        'JobId': 'string',
                        'JobName': 'string',
                        'JobStatus':
                        'SUBMITTED'|'IN_PROGRESS'|'COMPLETED'|'FAILED'
                        |'STOP_REQUESTED'|'STOPPED',
                        'Message': 'string',
                        'SubmitTime': datetime(2015, 1, 1),
                        'EndTime': datetime(2015, 1, 1),
                        'EntityRecognizerArn': 'string',
                        'InputDataConfig': {
                            'S3Uri': 'string',
                            'InputFormat': 'ONE_DOC_PER_FILE'|'ONE_DOC_PER_LINE'
                        },
                        'OutputDataConfig': {
                            'S3Uri': 'string',
                            'KmsKeyId': 'string'
                        },
                        'LanguageCode':
                        'en'|'es'|'fr'|'de'|'it'|'pt'|'ar'|'hi'|'ja'|'ko'|'zh'
                        |'zh-TW',
                        'DataAccessRoleArn': 'string',
                        'VolumeKmsKeyId': 'string',
                        'VpcConfig': {
                            'SecurityGroupIds': [
                                'string',
                            ],
                            'Subnets': [
                                'string',
                            ]
                        }
                    },
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **EntitiesDetectionJobPropertiesList** *(list) --*

              A list containing the properties of each job that is returned.

              - *(dict) --*

                Provides information about an entities detection job.

                - **JobId** *(string) --*

                  The identifier assigned to the entities detection job.

                - **JobName** *(string) --*

                  The name that you assigned the entities detection job.

                - **JobStatus** *(string) --*

                  The current status of the entities detection job. If the status is ``FAILED`` ,
                  the ``Message`` field shows the reason for the failure.

                - **Message** *(string) --*

                  A description of the status of a job.

                - **SubmitTime** *(datetime) --*

                  The time that the entities detection job was submitted for processing.

                - **EndTime** *(datetime) --*

                  The time that the entities detection job completed

                - **EntityRecognizerArn** *(string) --*

                  The Amazon Resource Name (ARN) that identifies the entity recognizer.

                - **InputDataConfig** *(dict) --*

                  The input data configuration that you supplied when you created the entities
                  detection job.

                  - **S3Uri** *(string) --*

                    The Amazon S3 URI for the input data. The URI must be in same region as the API
                    endpoint that you are calling. The URI can point to a single input file or it
                    can provide the prefix for a collection of data files.

                    For example, if you use the URI ``S3://bucketName/prefix`` , if the prefix is a
                    single file, Amazon Comprehend uses that file as input. If more than one file
                    begins with the prefix, Amazon Comprehend uses all of them as input.

                  - **InputFormat** *(string) --*

                    Specifies how the text in an input file should be processed:

                    * ``ONE_DOC_PER_FILE`` - Each file is considered a separate document. Use this
                    option when you are processing large documents, such as newspaper articles or
                    scientific papers.

                    * ``ONE_DOC_PER_LINE`` - Each line in a file is considered a separate document.
                    Use this option when you are processing many short documents, such as text
                    messages.

                - **OutputDataConfig** *(dict) --*

                  The output data configuration that you supplied when you created the entities
                  detection job.

                  - **S3Uri** *(string) --*

                    When you use the ``OutputDataConfig`` object with asynchronous operations, you
                    specify the Amazon S3 location where you want to write the output data. The URI
                    must be in the same region as the API endpoint that you are calling. The
                    location is used as the prefix for the actual location of the output file.

                    When the topic detection job is finished, the service creates an output file in
                    a directory specific to the job. The ``S3Uri`` field contains the location of
                    the output file, called ``output.tar.gz`` . It is a compressed archive that
                    contains the ouput of the operation.

                  - **KmsKeyId** *(string) --*

                    ID for the AWS Key Management Service (KMS) key that Amazon Comprehend uses to
                    encrypt the output results from an analysis job. The KmsKeyId can be one of the
                    following formats:

                    * KMS Key ID: ``"1234abcd-12ab-34cd-56ef-1234567890ab"``

                    * Amazon Resource Name (ARN) of a KMS Key:
                    ``"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"``

                    * KMS Key Alias: ``"alias/ExampleAlias"``

                    * ARN of a KMS Key Alias:
                    ``"arn:aws:kms:us-west-2:111122223333:alias/ExampleAlias"``

                - **LanguageCode** *(string) --*

                  The language code of the input documents.

                - **DataAccessRoleArn** *(string) --*

                  The Amazon Resource Name (ARN) that gives Amazon Comprehend read access to your
                  input data.

                - **VolumeKmsKeyId** *(string) --*

                  ID for the AWS Key Management Service (KMS) key that Amazon Comprehend uses to
                  encrypt data on the storage volume attached to the ML compute instance(s) that
                  process the analysis job. The VolumeKmsKeyId can be either of the following
                  formats:

                  * KMS Key ID: ``"1234abcd-12ab-34cd-56ef-1234567890ab"``

                  * Amazon Resource Name (ARN) of a KMS Key:
                  ``"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"``

                - **VpcConfig** *(dict) --*

                  Configuration parameters for a private Virtual Private Cloud (VPC) containing the
                  resources you are using for your entity detection job. For more information, see
                  `Amazon VPC
                  <https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html>`__ .

                  - **SecurityGroupIds** *(list) --*

                    The ID number for a security group on an instance of your private VPC. Security
                    groups on your VPC function serve as a virtual firewall to control inbound and
                    outbound traffic and provides security for the resources that you’ll be
                    accessing on the VPC. This ID number is preceded by "sg-", for instance:
                    "sg-03b388029b0a285ea". For more information, see `Security Groups for your VPC
                    <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html>`__ .

                    - *(string) --*

                  - **Subnets** *(list) --*

                    The ID for each subnet being used in your private VPC. This subnet is a subset
                    of the a range of IPv4 addresses used by the VPC and is specific to a given
                    availability zone in the VPC’s region. This ID number is preceded by "subnet-",
                    for instance: "subnet-04ccf456919e69055". For more information, see `VPCs and
                    Subnets <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html>`__ .

                    - *(string) --*

            - **NextToken** *(string) --*

              Identifies the next page of results to return.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_entity_recognizers(
        self,
        Filter: ClientListEntityRecognizersFilterTypeDef = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ClientListEntityRecognizersResponseTypeDef:
        """
        Gets a list of the properties of all entity recognizers that you created, including
        recognizers currently in training. Allows you to filter the list of recognizers based on
        criteria such as status and submission time. This call returns up to 500 entity recognizers
        in the list, with a default number of 100 recognizers in the list.

        The results of this list are not in any particular order. Please get the list and sort
        locally if needed.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/comprehend-2017-11-27/ListEntityRecognizers>`_

        **Request Syntax**
        ::

          response = client.list_entity_recognizers(
              Filter={
                  'Status':
                  'SUBMITTED'|'TRAINING'|'DELETING'|'STOP_REQUESTED'|'STOPPED'|'IN_ERROR'
                  |'TRAINED',
                  'SubmitTimeBefore': datetime(2015, 1, 1),
                  'SubmitTimeAfter': datetime(2015, 1, 1)
              },
              NextToken='string',
              MaxResults=123
          )
        :type Filter: dict
        :param Filter:

          Filters the list of entities returned. You can filter on ``Status`` , ``SubmitTimeBefore``
          , or ``SubmitTimeAfter`` . You can only set one filter at a time.

          - **Status** *(string) --*

            The status of an entity recognizer.

          - **SubmitTimeBefore** *(datetime) --*

            Filters the list of entities based on the time that the list was submitted for
            processing. Returns only jobs submitted before the specified time. Jobs are returned in
            descending order, newest to oldest.

          - **SubmitTimeAfter** *(datetime) --*

            Filters the list of entities based on the time that the list was submitted for
            processing. Returns only jobs submitted after the specified time. Jobs are returned in
            ascending order, oldest to newest.

        :type NextToken: string
        :param NextToken:

          Identifies the next page of results to return.

        :type MaxResults: integer
        :param MaxResults:

          The maximum number of results to return on each page. The default is 100.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'EntityRecognizerPropertiesList': [
                    {
                        'EntityRecognizerArn': 'string',
                        'LanguageCode':
                        'en'|'es'|'fr'|'de'|'it'|'pt'|'ar'|'hi'|'ja'|'ko'|'zh'
                        |'zh-TW',
                        'Status':
                        'SUBMITTED'|'TRAINING'|'DELETING'|'STOP_REQUESTED'|'STOPPED'
                        |'IN_ERROR'|'TRAINED',
                        'Message': 'string',
                        'SubmitTime': datetime(2015, 1, 1),
                        'EndTime': datetime(2015, 1, 1),
                        'TrainingStartTime': datetime(2015, 1, 1),
                        'TrainingEndTime': datetime(2015, 1, 1),
                        'InputDataConfig': {
                            'EntityTypes': [
                                {
                                    'Type': 'string'
                                },
                            ],
                            'Documents': {
                                'S3Uri': 'string'
                            },
                            'Annotations': {
                                'S3Uri': 'string'
                            },
                            'EntityList': {
                                'S3Uri': 'string'
                            }
                        },
                        'RecognizerMetadata': {
                            'NumberOfTrainedDocuments': 123,
                            'NumberOfTestDocuments': 123,
                            'EvaluationMetrics': {
                                'Precision': 123.0,
                                'Recall': 123.0,
                                'F1Score': 123.0
                            },
                            'EntityTypes': [
                                {
                                    'Type': 'string',
                                    'EvaluationMetrics': {
                                        'Precision': 123.0,
                                        'Recall': 123.0,
                                        'F1Score': 123.0
                                    },
                                    'NumberOfTrainMentions': 123
                                },
                            ]
                        },
                        'DataAccessRoleArn': 'string',
                        'VolumeKmsKeyId': 'string',
                        'VpcConfig': {
                            'SecurityGroupIds': [
                                'string',
                            ],
                            'Subnets': [
                                'string',
                            ]
                        }
                    },
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **EntityRecognizerPropertiesList** *(list) --*

              The list of properties of an entity recognizer.

              - *(dict) --*

                Describes information about an entity recognizer.

                - **EntityRecognizerArn** *(string) --*

                  The Amazon Resource Name (ARN) that identifies the entity recognizer.

                - **LanguageCode** *(string) --*

                  The language of the input documents. All documents must be in the same language.
                  Only English ("en") is currently supported.

                - **Status** *(string) --*

                  Provides the status of the entity recognizer.

                - **Message** *(string) --*

                  A description of the status of the recognizer.

                - **SubmitTime** *(datetime) --*

                  The time that the recognizer was submitted for processing.

                - **EndTime** *(datetime) --*

                  The time that the recognizer creation completed.

                - **TrainingStartTime** *(datetime) --*

                  The time that training of the entity recognizer started.

                - **TrainingEndTime** *(datetime) --*

                  The time that training of the entity recognizer was completed.

                - **InputDataConfig** *(dict) --*

                  The input data properties of an entity recognizer.

                  - **EntityTypes** *(list) --*

                    The entity types in the input data for an entity recognizer. A maximum of 12
                    entity types can be used at one time to train an entity recognizer.

                    - *(dict) --*

                      Information about an individual item on a list of entity types.

                      - **Type** *(string) --*

                        Entity type of an item on an entity type list.

                  - **Documents** *(dict) --*

                    S3 location of the documents folder for an entity recognizer

                    - **S3Uri** *(string) --*

                      Specifies the Amazon S3 location where the training documents for an entity
                      recognizer are located. The URI must be in the same region as the API endpoint
                      that you are calling.

                  - **Annotations** *(dict) --*

                    S3 location of the annotations file for an entity recognizer.

                    - **S3Uri** *(string) --*

                      Specifies the Amazon S3 location where the annotations for an entity
                      recognizer are located. The URI must be in the same region as the API endpoint
                      that you are calling.

                  - **EntityList** *(dict) --*

                    S3 location of the entity list for an entity recognizer.

                    - **S3Uri** *(string) --*

                      Specifies the Amazon S3 location where the entity list is located. The URI
                      must be in the same region as the API endpoint that you are calling.

                - **RecognizerMetadata** *(dict) --*

                  Provides information about an entity recognizer.

                  - **NumberOfTrainedDocuments** *(integer) --*

                    The number of documents in the input data that were used to train the entity
                    recognizer. Typically this is 80 to 90 percent of the input documents.

                  - **NumberOfTestDocuments** *(integer) --*

                    The number of documents in the input data that were used to test the entity
                    recognizer. Typically this is 10 to 20 percent of the input documents.

                  - **EvaluationMetrics** *(dict) --*

                    Detailed information about the accuracy of an entity recognizer.

                    - **Precision** *(float) --*

                      A measure of the usefulness of the recognizer results in the test data. High
                      precision means that the recognizer returned substantially more relevant
                      results than irrelevant ones.

                    - **Recall** *(float) --*

                      A measure of how complete the recognizer results are for the test data. High
                      recall means that the recognizer returned most of the relevant results.

                    - **F1Score** *(float) --*

                      A measure of how accurate the recognizer results are for the test data. It is
                      derived from the ``Precision`` and ``Recall`` values. The ``F1Score`` is the
                      harmonic average of the two scores. The highest score is 1, and the worst
                      score is 0.

                  - **EntityTypes** *(list) --*

                    Entity types from the metadata of an entity recognizer.

                    - *(dict) --*

                      Individual item from the list of entity types in the metadata of an entity
                      recognizer.

                      - **Type** *(string) --*

                        Type of entity from the list of entity types in the metadata of an entity
                        recognizer.

                      - **EvaluationMetrics** *(dict) --*

                        Detailed information about the accuracy of the entity recognizer for a
                        specific item on the list of entity types.

                        - **Precision** *(float) --*

                          A measure of the usefulness of the recognizer results for a specific
                          entity type in the test data. High precision means that the recognizer
                          returned substantially more relevant results than irrelevant ones.

                        - **Recall** *(float) --*

                          A measure of how complete the recognizer results are for a specific entity
                          type in the test data. High recall means that the recognizer returned most
                          of the relevant results.

                        - **F1Score** *(float) --*

                          A measure of how accurate the recognizer results are for for a specific
                          entity type in the test data. It is derived from the ``Precision`` and
                          ``Recall`` values. The ``F1Score`` is the harmonic average of the two
                          scores. The highest score is 1, and the worst score is 0.

                      - **NumberOfTrainMentions** *(integer) --*

                        Indicates the number of times the given entity type was seen in the training
                        data.

                - **DataAccessRoleArn** *(string) --*

                  The Amazon Resource Name (ARN) of the AWS Identity and Management (IAM) role that
                  grants Amazon Comprehend read access to your input data.

                - **VolumeKmsKeyId** *(string) --*

                  ID for the AWS Key Management Service (KMS) key that Amazon Comprehend uses to
                  encrypt data on the storage volume attached to the ML compute instance(s) that
                  process the analysis job. The VolumeKmsKeyId can be either of the following
                  formats:

                  * KMS Key ID: ``"1234abcd-12ab-34cd-56ef-1234567890ab"``

                  * Amazon Resource Name (ARN) of a KMS Key:
                  ``"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"``

                - **VpcConfig** *(dict) --*

                  Configuration parameters for a private Virtual Private Cloud (VPC) containing the
                  resources you are using for your custom entity recognizer. For more information,
                  see `Amazon VPC
                  <https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html>`__ .

                  - **SecurityGroupIds** *(list) --*

                    The ID number for a security group on an instance of your private VPC. Security
                    groups on your VPC function serve as a virtual firewall to control inbound and
                    outbound traffic and provides security for the resources that you’ll be
                    accessing on the VPC. This ID number is preceded by "sg-", for instance:
                    "sg-03b388029b0a285ea". For more information, see `Security Groups for your VPC
                    <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html>`__ .

                    - *(string) --*

                  - **Subnets** *(list) --*

                    The ID for each subnet being used in your private VPC. This subnet is a subset
                    of the a range of IPv4 addresses used by the VPC and is specific to a given
                    availability zone in the VPC’s region. This ID number is preceded by "subnet-",
                    for instance: "subnet-04ccf456919e69055". For more information, see `VPCs and
                    Subnets <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html>`__ .

                    - *(string) --*

            - **NextToken** *(string) --*

              Identifies the next page of results to return.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_key_phrases_detection_jobs(
        self,
        Filter: ClientListKeyPhrasesDetectionJobsFilterTypeDef = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ClientListKeyPhrasesDetectionJobsResponseTypeDef:
        """
        Get a list of key phrase detection jobs that you have submitted.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/comprehend-2017-11-27/ListKeyPhrasesDetectionJobs>`_

        **Request Syntax**
        ::

          response = client.list_key_phrases_detection_jobs(
              Filter={
                  'JobName': 'string',
                  'JobStatus':
                  'SUBMITTED'|'IN_PROGRESS'|'COMPLETED'|'FAILED'|'STOP_REQUESTED'
                  |'STOPPED',
                  'SubmitTimeBefore': datetime(2015, 1, 1),
                  'SubmitTimeAfter': datetime(2015, 1, 1)
              },
              NextToken='string',
              MaxResults=123
          )
        :type Filter: dict
        :param Filter:

          Filters the jobs that are returned. You can filter jobs on their name, status, or the date
          and time that they were submitted. You can only set one filter at a time.

          - **JobName** *(string) --*

            Filters on the name of the job.

          - **JobStatus** *(string) --*

            Filters the list of jobs based on job status. Returns only jobs with the specified
            status.

          - **SubmitTimeBefore** *(datetime) --*

            Filters the list of jobs based on the time that the job was submitted for processing.
            Returns only jobs submitted before the specified time. Jobs are returned in ascending
            order, oldest to newest.

          - **SubmitTimeAfter** *(datetime) --*

            Filters the list of jobs based on the time that the job was submitted for processing.
            Returns only jobs submitted after the specified time. Jobs are returned in descending
            order, newest to oldest.

        :type NextToken: string
        :param NextToken:

          Identifies the next page of results to return.

        :type MaxResults: integer
        :param MaxResults:

          The maximum number of results to return in each page. The default is 100.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'KeyPhrasesDetectionJobPropertiesList': [
                    {
                        'JobId': 'string',
                        'JobName': 'string',
                        'JobStatus':
                        'SUBMITTED'|'IN_PROGRESS'|'COMPLETED'|'FAILED'
                        |'STOP_REQUESTED'|'STOPPED',
                        'Message': 'string',
                        'SubmitTime': datetime(2015, 1, 1),
                        'EndTime': datetime(2015, 1, 1),
                        'InputDataConfig': {
                            'S3Uri': 'string',
                            'InputFormat': 'ONE_DOC_PER_FILE'|'ONE_DOC_PER_LINE'
                        },
                        'OutputDataConfig': {
                            'S3Uri': 'string',
                            'KmsKeyId': 'string'
                        },
                        'LanguageCode':
                        'en'|'es'|'fr'|'de'|'it'|'pt'|'ar'|'hi'|'ja'|'ko'|'zh'
                        |'zh-TW',
                        'DataAccessRoleArn': 'string',
                        'VolumeKmsKeyId': 'string',
                        'VpcConfig': {
                            'SecurityGroupIds': [
                                'string',
                            ],
                            'Subnets': [
                                'string',
                            ]
                        }
                    },
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **KeyPhrasesDetectionJobPropertiesList** *(list) --*

              A list containing the properties of each job that is returned.

              - *(dict) --*

                Provides information about a key phrases detection job.

                - **JobId** *(string) --*

                  The identifier assigned to the key phrases detection job.

                - **JobName** *(string) --*

                  The name that you assigned the key phrases detection job.

                - **JobStatus** *(string) --*

                  The current status of the key phrases detection job. If the status is ``FAILED`` ,
                  the ``Message`` field shows the reason for the failure.

                - **Message** *(string) --*

                  A description of the status of a job.

                - **SubmitTime** *(datetime) --*

                  The time that the key phrases detection job was submitted for processing.

                - **EndTime** *(datetime) --*

                  The time that the key phrases detection job completed.

                - **InputDataConfig** *(dict) --*

                  The input data configuration that you supplied when you created the key phrases
                  detection job.

                  - **S3Uri** *(string) --*

                    The Amazon S3 URI for the input data. The URI must be in same region as the API
                    endpoint that you are calling. The URI can point to a single input file or it
                    can provide the prefix for a collection of data files.

                    For example, if you use the URI ``S3://bucketName/prefix`` , if the prefix is a
                    single file, Amazon Comprehend uses that file as input. If more than one file
                    begins with the prefix, Amazon Comprehend uses all of them as input.

                  - **InputFormat** *(string) --*

                    Specifies how the text in an input file should be processed:

                    * ``ONE_DOC_PER_FILE`` - Each file is considered a separate document. Use this
                    option when you are processing large documents, such as newspaper articles or
                    scientific papers.

                    * ``ONE_DOC_PER_LINE`` - Each line in a file is considered a separate document.
                    Use this option when you are processing many short documents, such as text
                    messages.

                - **OutputDataConfig** *(dict) --*

                  The output data configuration that you supplied when you created the key phrases
                  detection job.

                  - **S3Uri** *(string) --*

                    When you use the ``OutputDataConfig`` object with asynchronous operations, you
                    specify the Amazon S3 location where you want to write the output data. The URI
                    must be in the same region as the API endpoint that you are calling. The
                    location is used as the prefix for the actual location of the output file.

                    When the topic detection job is finished, the service creates an output file in
                    a directory specific to the job. The ``S3Uri`` field contains the location of
                    the output file, called ``output.tar.gz`` . It is a compressed archive that
                    contains the ouput of the operation.

                  - **KmsKeyId** *(string) --*

                    ID for the AWS Key Management Service (KMS) key that Amazon Comprehend uses to
                    encrypt the output results from an analysis job. The KmsKeyId can be one of the
                    following formats:

                    * KMS Key ID: ``"1234abcd-12ab-34cd-56ef-1234567890ab"``

                    * Amazon Resource Name (ARN) of a KMS Key:
                    ``"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"``

                    * KMS Key Alias: ``"alias/ExampleAlias"``

                    * ARN of a KMS Key Alias:
                    ``"arn:aws:kms:us-west-2:111122223333:alias/ExampleAlias"``

                - **LanguageCode** *(string) --*

                  The language code of the input documents.

                - **DataAccessRoleArn** *(string) --*

                  The Amazon Resource Name (ARN) that gives Amazon Comprehend read access to your
                  input data.

                - **VolumeKmsKeyId** *(string) --*

                  ID for the AWS Key Management Service (KMS) key that Amazon Comprehend uses to
                  encrypt data on the storage volume attached to the ML compute instance(s) that
                  process the analysis job. The VolumeKmsKeyId can be either of the following
                  formats:

                  * KMS Key ID: ``"1234abcd-12ab-34cd-56ef-1234567890ab"``

                  * Amazon Resource Name (ARN) of a KMS Key:
                  ``"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"``

                - **VpcConfig** *(dict) --*

                  Configuration parameters for a private Virtual Private Cloud (VPC) containing the
                  resources you are using for your key phrases detection job. For more information,
                  see `Amazon VPC
                  <https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html>`__ .

                  - **SecurityGroupIds** *(list) --*

                    The ID number for a security group on an instance of your private VPC. Security
                    groups on your VPC function serve as a virtual firewall to control inbound and
                    outbound traffic and provides security for the resources that you’ll be
                    accessing on the VPC. This ID number is preceded by "sg-", for instance:
                    "sg-03b388029b0a285ea". For more information, see `Security Groups for your VPC
                    <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html>`__ .

                    - *(string) --*

                  - **Subnets** *(list) --*

                    The ID for each subnet being used in your private VPC. This subnet is a subset
                    of the a range of IPv4 addresses used by the VPC and is specific to a given
                    availability zone in the VPC’s region. This ID number is preceded by "subnet-",
                    for instance: "subnet-04ccf456919e69055". For more information, see `VPCs and
                    Subnets <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html>`__ .

                    - *(string) --*

            - **NextToken** *(string) --*

              Identifies the next page of results to return.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_sentiment_detection_jobs(
        self,
        Filter: ClientListSentimentDetectionJobsFilterTypeDef = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ClientListSentimentDetectionJobsResponseTypeDef:
        """
        Gets a list of sentiment detection jobs that you have submitted.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/comprehend-2017-11-27/ListSentimentDetectionJobs>`_

        **Request Syntax**
        ::

          response = client.list_sentiment_detection_jobs(
              Filter={
                  'JobName': 'string',
                  'JobStatus':
                  'SUBMITTED'|'IN_PROGRESS'|'COMPLETED'|'FAILED'|'STOP_REQUESTED'
                  |'STOPPED',
                  'SubmitTimeBefore': datetime(2015, 1, 1),
                  'SubmitTimeAfter': datetime(2015, 1, 1)
              },
              NextToken='string',
              MaxResults=123
          )
        :type Filter: dict
        :param Filter:

          Filters the jobs that are returned. You can filter jobs on their name, status, or the date
          and time that they were submitted. You can only set one filter at a time.

          - **JobName** *(string) --*

            Filters on the name of the job.

          - **JobStatus** *(string) --*

            Filters the list of jobs based on job status. Returns only jobs with the specified
            status.

          - **SubmitTimeBefore** *(datetime) --*

            Filters the list of jobs based on the time that the job was submitted for processing.
            Returns only jobs submitted before the specified time. Jobs are returned in ascending
            order, oldest to newest.

          - **SubmitTimeAfter** *(datetime) --*

            Filters the list of jobs based on the time that the job was submitted for processing.
            Returns only jobs submitted after the specified time. Jobs are returned in descending
            order, newest to oldest.

        :type NextToken: string
        :param NextToken:

          Identifies the next page of results to return.

        :type MaxResults: integer
        :param MaxResults:

          The maximum number of results to return in each page. The default is 100.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'SentimentDetectionJobPropertiesList': [
                    {
                        'JobId': 'string',
                        'JobName': 'string',
                        'JobStatus':
                        'SUBMITTED'|'IN_PROGRESS'|'COMPLETED'|'FAILED'
                        |'STOP_REQUESTED'|'STOPPED',
                        'Message': 'string',
                        'SubmitTime': datetime(2015, 1, 1),
                        'EndTime': datetime(2015, 1, 1),
                        'InputDataConfig': {
                            'S3Uri': 'string',
                            'InputFormat': 'ONE_DOC_PER_FILE'|'ONE_DOC_PER_LINE'
                        },
                        'OutputDataConfig': {
                            'S3Uri': 'string',
                            'KmsKeyId': 'string'
                        },
                        'LanguageCode':
                        'en'|'es'|'fr'|'de'|'it'|'pt'|'ar'|'hi'|'ja'|'ko'|'zh'
                        |'zh-TW',
                        'DataAccessRoleArn': 'string',
                        'VolumeKmsKeyId': 'string',
                        'VpcConfig': {
                            'SecurityGroupIds': [
                                'string',
                            ],
                            'Subnets': [
                                'string',
                            ]
                        }
                    },
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **SentimentDetectionJobPropertiesList** *(list) --*

              A list containing the properties of each job that is returned.

              - *(dict) --*

                Provides information about a sentiment detection job.

                - **JobId** *(string) --*

                  The identifier assigned to the sentiment detection job.

                - **JobName** *(string) --*

                  The name that you assigned to the sentiment detection job

                - **JobStatus** *(string) --*

                  The current status of the sentiment detection job. If the status is ``FAILED`` ,
                  the ``Messages`` field shows the reason for the failure.

                - **Message** *(string) --*

                  A description of the status of a job.

                - **SubmitTime** *(datetime) --*

                  The time that the sentiment detection job was submitted for processing.

                - **EndTime** *(datetime) --*

                  The time that the sentiment detection job ended.

                - **InputDataConfig** *(dict) --*

                  The input data configuration that you supplied when you created the sentiment
                  detection job.

                  - **S3Uri** *(string) --*

                    The Amazon S3 URI for the input data. The URI must be in same region as the API
                    endpoint that you are calling. The URI can point to a single input file or it
                    can provide the prefix for a collection of data files.

                    For example, if you use the URI ``S3://bucketName/prefix`` , if the prefix is a
                    single file, Amazon Comprehend uses that file as input. If more than one file
                    begins with the prefix, Amazon Comprehend uses all of them as input.

                  - **InputFormat** *(string) --*

                    Specifies how the text in an input file should be processed:

                    * ``ONE_DOC_PER_FILE`` - Each file is considered a separate document. Use this
                    option when you are processing large documents, such as newspaper articles or
                    scientific papers.

                    * ``ONE_DOC_PER_LINE`` - Each line in a file is considered a separate document.
                    Use this option when you are processing many short documents, such as text
                    messages.

                - **OutputDataConfig** *(dict) --*

                  The output data configuration that you supplied when you created the sentiment
                  detection job.

                  - **S3Uri** *(string) --*

                    When you use the ``OutputDataConfig`` object with asynchronous operations, you
                    specify the Amazon S3 location where you want to write the output data. The URI
                    must be in the same region as the API endpoint that you are calling. The
                    location is used as the prefix for the actual location of the output file.

                    When the topic detection job is finished, the service creates an output file in
                    a directory specific to the job. The ``S3Uri`` field contains the location of
                    the output file, called ``output.tar.gz`` . It is a compressed archive that
                    contains the ouput of the operation.

                  - **KmsKeyId** *(string) --*

                    ID for the AWS Key Management Service (KMS) key that Amazon Comprehend uses to
                    encrypt the output results from an analysis job. The KmsKeyId can be one of the
                    following formats:

                    * KMS Key ID: ``"1234abcd-12ab-34cd-56ef-1234567890ab"``

                    * Amazon Resource Name (ARN) of a KMS Key:
                    ``"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"``

                    * KMS Key Alias: ``"alias/ExampleAlias"``

                    * ARN of a KMS Key Alias:
                    ``"arn:aws:kms:us-west-2:111122223333:alias/ExampleAlias"``

                - **LanguageCode** *(string) --*

                  The language code of the input documents.

                - **DataAccessRoleArn** *(string) --*

                  The Amazon Resource Name (ARN) that gives Amazon Comprehend read access to your
                  input data.

                - **VolumeKmsKeyId** *(string) --*

                  ID for the AWS Key Management Service (KMS) key that Amazon Comprehend uses to
                  encrypt data on the storage volume attached to the ML compute instance(s) that
                  process the analysis job. The VolumeKmsKeyId can be either of the following
                  formats:

                  * KMS Key ID: ``"1234abcd-12ab-34cd-56ef-1234567890ab"``

                  * Amazon Resource Name (ARN) of a KMS Key:
                  ``"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"``

                - **VpcConfig** *(dict) --*

                  Configuration parameters for a private Virtual Private Cloud (VPC) containing the
                  resources you are using for your sentiment detection job. For more information,
                  see `Amazon VPC
                  <https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html>`__ .

                  - **SecurityGroupIds** *(list) --*

                    The ID number for a security group on an instance of your private VPC. Security
                    groups on your VPC function serve as a virtual firewall to control inbound and
                    outbound traffic and provides security for the resources that you’ll be
                    accessing on the VPC. This ID number is preceded by "sg-", for instance:
                    "sg-03b388029b0a285ea". For more information, see `Security Groups for your VPC
                    <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html>`__ .

                    - *(string) --*

                  - **Subnets** *(list) --*

                    The ID for each subnet being used in your private VPC. This subnet is a subset
                    of the a range of IPv4 addresses used by the VPC and is specific to a given
                    availability zone in the VPC’s region. This ID number is preceded by "subnet-",
                    for instance: "subnet-04ccf456919e69055". For more information, see `VPCs and
                    Subnets <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html>`__ .

                    - *(string) --*

            - **NextToken** *(string) --*

              Identifies the next page of results to return.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_tags_for_resource(self, ResourceArn: str) -> ClientListTagsForResourceResponseTypeDef:
        """
        Lists all tags associated with a given Amazon Comprehend resource.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/comprehend-2017-11-27/ListTagsForResource>`_

        **Request Syntax**
        ::

          response = client.list_tags_for_resource(
              ResourceArn='string'
          )
        :type ResourceArn: string
        :param ResourceArn: **[REQUIRED]**

          The Amazon Resource Name (ARN) of the given Amazon Comprehend resource you are querying.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'ResourceArn': 'string',
                'Tags': [
                    {
                        'Key': 'string',
                        'Value': 'string'
                    },
                ]
            }
          **Response Structure**

          - *(dict) --*

            - **ResourceArn** *(string) --*

              The Amazon Resource Name (ARN) of the given Amazon Comprehend resource you are
              querying.

            - **Tags** *(list) --*

              Tags associated with the Amazon Comprehend resource being queried. A tag is a
              key-value pair that adds as a metadata to a resource used by Amazon Comprehend. For
              example, a tag with "Sales" as the key might be added to a resource to indicate its
              use by the sales department.

              - *(dict) --*

                A key-value pair that adds as a metadata to a resource used by Amazon Comprehend.
                For example, a tag with the key-value pair ‘Department’:’Sales’ might be added to a
                resource to indicate its use by a particular department.

                - **Key** *(string) --*

                  The initial part of a key-value pair that forms a tag associated with a given
                  resource. For instance, if you want to show which resources are used by which
                  departments, you might use “Department” as the key portion of the pair, with
                  multiple possible values such as “sales,” “legal,” and “administration.”

                - **Value** *(string) --*

                  The second part of a key-value pair that forms a tag associated with a given
                  resource. For instance, if you want to show which resources are used by which
                  departments, you might use “Department” as the initial (key) portion of the pair,
                  with a value of “sales” to indicate the sales department.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_topics_detection_jobs(
        self,
        Filter: ClientListTopicsDetectionJobsFilterTypeDef = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ClientListTopicsDetectionJobsResponseTypeDef:
        """
        Gets a list of the topic detection jobs that you have submitted.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/comprehend-2017-11-27/ListTopicsDetectionJobs>`_

        **Request Syntax**
        ::

          response = client.list_topics_detection_jobs(
              Filter={
                  'JobName': 'string',
                  'JobStatus':
                  'SUBMITTED'|'IN_PROGRESS'|'COMPLETED'|'FAILED'|'STOP_REQUESTED'
                  |'STOPPED',
                  'SubmitTimeBefore': datetime(2015, 1, 1),
                  'SubmitTimeAfter': datetime(2015, 1, 1)
              },
              NextToken='string',
              MaxResults=123
          )
        :type Filter: dict
        :param Filter:

          Filters the jobs that are returned. Jobs can be filtered on their name, status, or the
          date and time that they were submitted. You can set only one filter at a time.

          - **JobName** *(string) --*

          - **JobStatus** *(string) --*

            Filters the list of topic detection jobs based on job status. Returns only jobs with the
            specified status.

          - **SubmitTimeBefore** *(datetime) --*

            Filters the list of jobs based on the time that the job was submitted for processing.
            Only returns jobs submitted before the specified time. Jobs are returned in descending
            order, newest to oldest.

          - **SubmitTimeAfter** *(datetime) --*

            Filters the list of jobs based on the time that the job was submitted for processing.
            Only returns jobs submitted after the specified time. Jobs are returned in ascending
            order, oldest to newest.

        :type NextToken: string
        :param NextToken:

          Identifies the next page of results to return.

        :type MaxResults: integer
        :param MaxResults:

          The maximum number of results to return in each page. The default is 100.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'TopicsDetectionJobPropertiesList': [
                    {
                        'JobId': 'string',
                        'JobName': 'string',
                        'JobStatus':
                        'SUBMITTED'|'IN_PROGRESS'|'COMPLETED'|'FAILED'
                        |'STOP_REQUESTED'|'STOPPED',
                        'Message': 'string',
                        'SubmitTime': datetime(2015, 1, 1),
                        'EndTime': datetime(2015, 1, 1),
                        'InputDataConfig': {
                            'S3Uri': 'string',
                            'InputFormat': 'ONE_DOC_PER_FILE'|'ONE_DOC_PER_LINE'
                        },
                        'OutputDataConfig': {
                            'S3Uri': 'string',
                            'KmsKeyId': 'string'
                        },
                        'NumberOfTopics': 123,
                        'DataAccessRoleArn': 'string',
                        'VolumeKmsKeyId': 'string',
                        'VpcConfig': {
                            'SecurityGroupIds': [
                                'string',
                            ],
                            'Subnets': [
                                'string',
                            ]
                        }
                    },
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **TopicsDetectionJobPropertiesList** *(list) --*

              A list containing the properties of each job that is returned.

              - *(dict) --*

                Provides information about a topic detection job.

                - **JobId** *(string) --*

                  The identifier assigned to the topic detection job.

                - **JobName** *(string) --*

                  The name of the topic detection job.

                - **JobStatus** *(string) --*

                  The current status of the topic detection job. If the status is ``Failed`` , the
                  reason for the failure is shown in the ``Message`` field.

                - **Message** *(string) --*

                  A description for the status of a job.

                - **SubmitTime** *(datetime) --*

                  The time that the topic detection job was submitted for processing.

                - **EndTime** *(datetime) --*

                  The time that the topic detection job was completed.

                - **InputDataConfig** *(dict) --*

                  The input data configuration supplied when you created the topic detection job.

                  - **S3Uri** *(string) --*

                    The Amazon S3 URI for the input data. The URI must be in same region as the API
                    endpoint that you are calling. The URI can point to a single input file or it
                    can provide the prefix for a collection of data files.

                    For example, if you use the URI ``S3://bucketName/prefix`` , if the prefix is a
                    single file, Amazon Comprehend uses that file as input. If more than one file
                    begins with the prefix, Amazon Comprehend uses all of them as input.

                  - **InputFormat** *(string) --*

                    Specifies how the text in an input file should be processed:

                    * ``ONE_DOC_PER_FILE`` - Each file is considered a separate document. Use this
                    option when you are processing large documents, such as newspaper articles or
                    scientific papers.

                    * ``ONE_DOC_PER_LINE`` - Each line in a file is considered a separate document.
                    Use this option when you are processing many short documents, such as text
                    messages.

                - **OutputDataConfig** *(dict) --*

                  The output data configuration supplied when you created the topic detection job.

                  - **S3Uri** *(string) --*

                    When you use the ``OutputDataConfig`` object with asynchronous operations, you
                    specify the Amazon S3 location where you want to write the output data. The URI
                    must be in the same region as the API endpoint that you are calling. The
                    location is used as the prefix for the actual location of the output file.

                    When the topic detection job is finished, the service creates an output file in
                    a directory specific to the job. The ``S3Uri`` field contains the location of
                    the output file, called ``output.tar.gz`` . It is a compressed archive that
                    contains the ouput of the operation.

                  - **KmsKeyId** *(string) --*

                    ID for the AWS Key Management Service (KMS) key that Amazon Comprehend uses to
                    encrypt the output results from an analysis job. The KmsKeyId can be one of the
                    following formats:

                    * KMS Key ID: ``"1234abcd-12ab-34cd-56ef-1234567890ab"``

                    * Amazon Resource Name (ARN) of a KMS Key:
                    ``"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"``

                    * KMS Key Alias: ``"alias/ExampleAlias"``

                    * ARN of a KMS Key Alias:
                    ``"arn:aws:kms:us-west-2:111122223333:alias/ExampleAlias"``

                - **NumberOfTopics** *(integer) --*

                  The number of topics to detect supplied when you created the topic detection job.
                  The default is 10.

                - **DataAccessRoleArn** *(string) --*

                  The Amazon Resource Name (ARN) of the AWS Identity and Management (IAM) role that
                  grants Amazon Comprehend read access to your job data.

                - **VolumeKmsKeyId** *(string) --*

                  ID for the AWS Key Management Service (KMS) key that Amazon Comprehend uses to
                  encrypt data on the storage volume attached to the ML compute instance(s) that
                  process the analysis job. The VolumeKmsKeyId can be either of the following
                  formats:

                  * KMS Key ID: ``"1234abcd-12ab-34cd-56ef-1234567890ab"``

                  * Amazon Resource Name (ARN) of a KMS Key:
                  ``"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"``

                - **VpcConfig** *(dict) --*

                  Configuration parameters for a private Virtual Private Cloud (VPC) containing the
                  resources you are using for your topic detection job. For more information, see
                  `Amazon VPC
                  <https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html>`__ .

                  - **SecurityGroupIds** *(list) --*

                    The ID number for a security group on an instance of your private VPC. Security
                    groups on your VPC function serve as a virtual firewall to control inbound and
                    outbound traffic and provides security for the resources that you’ll be
                    accessing on the VPC. This ID number is preceded by "sg-", for instance:
                    "sg-03b388029b0a285ea". For more information, see `Security Groups for your VPC
                    <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html>`__ .

                    - *(string) --*

                  - **Subnets** *(list) --*

                    The ID for each subnet being used in your private VPC. This subnet is a subset
                    of the a range of IPv4 addresses used by the VPC and is specific to a given
                    availability zone in the VPC’s region. This ID number is preceded by "subnet-",
                    for instance: "subnet-04ccf456919e69055". For more information, see `VPCs and
                    Subnets <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html>`__ .

                    - *(string) --*

            - **NextToken** *(string) --*

              Identifies the next page of results to return.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def start_document_classification_job(
        self,
        DocumentClassifierArn: str,
        InputDataConfig: ClientStartDocumentClassificationJobInputDataConfigTypeDef,
        OutputDataConfig: ClientStartDocumentClassificationJobOutputDataConfigTypeDef,
        DataAccessRoleArn: str,
        JobName: str = None,
        ClientRequestToken: str = None,
        VolumeKmsKeyId: str = None,
        VpcConfig: ClientStartDocumentClassificationJobVpcConfigTypeDef = None,
    ) -> ClientStartDocumentClassificationJobResponseTypeDef:
        """
        Starts an asynchronous document classification job. Use the operation to track the progress
        of the job.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/comprehend-2017-11-27/StartDocumentClassificationJob>`_

        **Request Syntax**
        ::

          response = client.start_document_classification_job(
              JobName='string',
              DocumentClassifierArn='string',
              InputDataConfig={
                  'S3Uri': 'string',
                  'InputFormat': 'ONE_DOC_PER_FILE'|'ONE_DOC_PER_LINE'
              },
              OutputDataConfig={
                  'S3Uri': 'string',
                  'KmsKeyId': 'string'
              },
              DataAccessRoleArn='string',
              ClientRequestToken='string',
              VolumeKmsKeyId='string',
              VpcConfig={
                  'SecurityGroupIds': [
                      'string',
                  ],
                  'Subnets': [
                      'string',
                  ]
              }
          )
        :type JobName: string
        :param JobName:

          The identifier of the job.

        :type DocumentClassifierArn: string
        :param DocumentClassifierArn: **[REQUIRED]**

          The Amazon Resource Name (ARN) of the document classifier to use to process the job.

        :type InputDataConfig: dict
        :param InputDataConfig: **[REQUIRED]**

          Specifies the format and location of the input data for the job.

          - **S3Uri** *(string) --* **[REQUIRED]**

            The Amazon S3 URI for the input data. The URI must be in same region as the API endpoint
            that you are calling. The URI can point to a single input file or it can provide the
            prefix for a collection of data files.

            For example, if you use the URI ``S3://bucketName/prefix`` , if the prefix is a single
            file, Amazon Comprehend uses that file as input. If more than one file begins with the
            prefix, Amazon Comprehend uses all of them as input.

          - **InputFormat** *(string) --*

            Specifies how the text in an input file should be processed:

            * ``ONE_DOC_PER_FILE`` - Each file is considered a separate document. Use this option
            when you are processing large documents, such as newspaper articles or scientific
            papers.

            * ``ONE_DOC_PER_LINE`` - Each line in a file is considered a separate document. Use this
            option when you are processing many short documents, such as text messages.

        :type OutputDataConfig: dict
        :param OutputDataConfig: **[REQUIRED]**

          Specifies where to send the output files.

          - **S3Uri** *(string) --* **[REQUIRED]**

            When you use the ``OutputDataConfig`` object with asynchronous operations, you specify
            the Amazon S3 location where you want to write the output data. The URI must be in the
            same region as the API endpoint that you are calling. The location is used as the prefix
            for the actual location of the output file.

            When the topic detection job is finished, the service creates an output file in a
            directory specific to the job. The ``S3Uri`` field contains the location of the output
            file, called ``output.tar.gz`` . It is a compressed archive that contains the ouput of
            the operation.

          - **KmsKeyId** *(string) --*

            ID for the AWS Key Management Service (KMS) key that Amazon Comprehend uses to encrypt
            the output results from an analysis job. The KmsKeyId can be one of the following
            formats:

            * KMS Key ID: ``"1234abcd-12ab-34cd-56ef-1234567890ab"``

            * Amazon Resource Name (ARN) of a KMS Key:
            ``"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"``

            * KMS Key Alias: ``"alias/ExampleAlias"``

            * ARN of a KMS Key Alias: ``"arn:aws:kms:us-west-2:111122223333:alias/ExampleAlias"``

        :type DataAccessRoleArn: string
        :param DataAccessRoleArn: **[REQUIRED]**

          The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that
          grants Amazon Comprehend read access to your input data.

        :type ClientRequestToken: string
        :param ClientRequestToken:

          A unique identifier for the request. If you do not set the client request token, Amazon
          Comprehend generates one.

          This field is autopopulated if not provided.

        :type VolumeKmsKeyId: string
        :param VolumeKmsKeyId:

          ID for the AWS Key Management Service (KMS) key that Amazon Comprehend uses to encrypt
          data on the storage volume attached to the ML compute instance(s) that process the
          analysis job. The VolumeKmsKeyId can be either of the following formats:

          * KMS Key ID: ``"1234abcd-12ab-34cd-56ef-1234567890ab"``

          * Amazon Resource Name (ARN) of a KMS Key:
          ``"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"``

        :type VpcConfig: dict
        :param VpcConfig:

          Configuration parameters for an optional private Virtual Private Cloud (VPC) containing
          the resources you are using for your document classification job. For more information,
          see `Amazon VPC
          <https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html>`__ .

          - **SecurityGroupIds** *(list) --* **[REQUIRED]**

            The ID number for a security group on an instance of your private VPC. Security groups
            on your VPC function serve as a virtual firewall to control inbound and outbound traffic
            and provides security for the resources that you’ll be accessing on the VPC. This ID
            number is preceded by "sg-", for instance: "sg-03b388029b0a285ea". For more information,
            see `Security Groups for your VPC
            <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html>`__ .

            - *(string) --*

          - **Subnets** *(list) --* **[REQUIRED]**

            The ID for each subnet being used in your private VPC. This subnet is a subset of the a
            range of IPv4 addresses used by the VPC and is specific to a given availability zone in
            the VPC’s region. This ID number is preceded by "subnet-", for instance:
            "subnet-04ccf456919e69055". For more information, see `VPCs and Subnets
            <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html>`__ .

            - *(string) --*

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'JobId': 'string',
                'JobStatus':
                'SUBMITTED'|'IN_PROGRESS'|'COMPLETED'|'FAILED'|'STOP_REQUESTED'|'STOPPED'
            }
          **Response Structure**

          - *(dict) --*

            - **JobId** *(string) --*

              The identifier generated for the job. To get the status of the job, use this
              identifier with the operation.

            - **JobStatus** *(string) --*

              The status of the job:

              * SUBMITTED - The job has been received and queued for processing.

              * IN_PROGRESS - Amazon Comprehend is processing the job.

              * COMPLETED - The job was successfully completed and the output is available.

              * FAILED - The job did not complete. For details, use the operation.

              * STOP_REQUESTED - Amazon Comprehend has received a stop request for the job and is
              processing the request.

              * STOPPED - The job was successfully stopped without completing.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def start_dominant_language_detection_job(
        self,
        InputDataConfig: ClientStartDominantLanguageDetectionJobInputDataConfigTypeDef,
        OutputDataConfig: ClientStartDominantLanguageDetectionJobOutputDataConfigTypeDef,
        DataAccessRoleArn: str,
        JobName: str = None,
        ClientRequestToken: str = None,
        VolumeKmsKeyId: str = None,
        VpcConfig: ClientStartDominantLanguageDetectionJobVpcConfigTypeDef = None,
    ) -> ClientStartDominantLanguageDetectionJobResponseTypeDef:
        """
        Starts an asynchronous dominant language detection job for a collection of documents. Use
        the operation to track the status of a job.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/comprehend-2017-11-27/StartDominantLanguageDetectionJob>`_

        **Request Syntax**
        ::

          response = client.start_dominant_language_detection_job(
              InputDataConfig={
                  'S3Uri': 'string',
                  'InputFormat': 'ONE_DOC_PER_FILE'|'ONE_DOC_PER_LINE'
              },
              OutputDataConfig={
                  'S3Uri': 'string',
                  'KmsKeyId': 'string'
              },
              DataAccessRoleArn='string',
              JobName='string',
              ClientRequestToken='string',
              VolumeKmsKeyId='string',
              VpcConfig={
                  'SecurityGroupIds': [
                      'string',
                  ],
                  'Subnets': [
                      'string',
                  ]
              }
          )
        :type InputDataConfig: dict
        :param InputDataConfig: **[REQUIRED]**

          Specifies the format and location of the input data for the job.

          - **S3Uri** *(string) --* **[REQUIRED]**

            The Amazon S3 URI for the input data. The URI must be in same region as the API endpoint
            that you are calling. The URI can point to a single input file or it can provide the
            prefix for a collection of data files.

            For example, if you use the URI ``S3://bucketName/prefix`` , if the prefix is a single
            file, Amazon Comprehend uses that file as input. If more than one file begins with the
            prefix, Amazon Comprehend uses all of them as input.

          - **InputFormat** *(string) --*

            Specifies how the text in an input file should be processed:

            * ``ONE_DOC_PER_FILE`` - Each file is considered a separate document. Use this option
            when you are processing large documents, such as newspaper articles or scientific
            papers.

            * ``ONE_DOC_PER_LINE`` - Each line in a file is considered a separate document. Use this
            option when you are processing many short documents, such as text messages.

        :type OutputDataConfig: dict
        :param OutputDataConfig: **[REQUIRED]**

          Specifies where to send the output files.

          - **S3Uri** *(string) --* **[REQUIRED]**

            When you use the ``OutputDataConfig`` object with asynchronous operations, you specify
            the Amazon S3 location where you want to write the output data. The URI must be in the
            same region as the API endpoint that you are calling. The location is used as the prefix
            for the actual location of the output file.

            When the topic detection job is finished, the service creates an output file in a
            directory specific to the job. The ``S3Uri`` field contains the location of the output
            file, called ``output.tar.gz`` . It is a compressed archive that contains the ouput of
            the operation.

          - **KmsKeyId** *(string) --*

            ID for the AWS Key Management Service (KMS) key that Amazon Comprehend uses to encrypt
            the output results from an analysis job. The KmsKeyId can be one of the following
            formats:

            * KMS Key ID: ``"1234abcd-12ab-34cd-56ef-1234567890ab"``

            * Amazon Resource Name (ARN) of a KMS Key:
            ``"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"``

            * KMS Key Alias: ``"alias/ExampleAlias"``

            * ARN of a KMS Key Alias: ``"arn:aws:kms:us-west-2:111122223333:alias/ExampleAlias"``

        :type DataAccessRoleArn: string
        :param DataAccessRoleArn: **[REQUIRED]**

          The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that
          grants Amazon Comprehend read access to your input data. For more information, see
          `https\\://docs.aws.amazon.com/comprehend/latest/dg/access-control-managing-permissions.html#auth-role-permissions
          <https://docs.aws.amazon.com/comprehend/latest/dg/access-control-managing-permissions.html#auth-role-permissions>`__
          .

        :type JobName: string
        :param JobName:

          An identifier for the job.

        :type ClientRequestToken: string
        :param ClientRequestToken:

          A unique identifier for the request. If you do not set the client request token, Amazon
          Comprehend generates one.

          This field is autopopulated if not provided.

        :type VolumeKmsKeyId: string
        :param VolumeKmsKeyId:

          ID for the AWS Key Management Service (KMS) key that Amazon Comprehend uses to encrypt
          data on the storage volume attached to the ML compute instance(s) that process the
          analysis job. The VolumeKmsKeyId can be either of the following formats:

          * KMS Key ID: ``"1234abcd-12ab-34cd-56ef-1234567890ab"``

          * Amazon Resource Name (ARN) of a KMS Key:
          ``"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"``

        :type VpcConfig: dict
        :param VpcConfig:

          Configuration parameters for an optional private Virtual Private Cloud (VPC) containing
          the resources you are using for your dominant language detection job. For more
          information, see `Amazon VPC
          <https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html>`__ .

          - **SecurityGroupIds** *(list) --* **[REQUIRED]**

            The ID number for a security group on an instance of your private VPC. Security groups
            on your VPC function serve as a virtual firewall to control inbound and outbound traffic
            and provides security for the resources that you’ll be accessing on the VPC. This ID
            number is preceded by "sg-", for instance: "sg-03b388029b0a285ea". For more information,
            see `Security Groups for your VPC
            <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html>`__ .

            - *(string) --*

          - **Subnets** *(list) --* **[REQUIRED]**

            The ID for each subnet being used in your private VPC. This subnet is a subset of the a
            range of IPv4 addresses used by the VPC and is specific to a given availability zone in
            the VPC’s region. This ID number is preceded by "subnet-", for instance:
            "subnet-04ccf456919e69055". For more information, see `VPCs and Subnets
            <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html>`__ .

            - *(string) --*

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'JobId': 'string',
                'JobStatus':
                'SUBMITTED'|'IN_PROGRESS'|'COMPLETED'|'FAILED'|'STOP_REQUESTED'|'STOPPED'
            }
          **Response Structure**

          - *(dict) --*

            - **JobId** *(string) --*

              The identifier generated for the job. To get the status of a job, use this identifier
              with the operation.

            - **JobStatus** *(string) --*

              The status of the job.

              * SUBMITTED - The job has been received and is queued for processing.

              * IN_PROGRESS - Amazon Comprehend is processing the job.

              * COMPLETED - The job was successfully completed and the output is available.

              * FAILED - The job did not complete. To get details, use the operation.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def start_entities_detection_job(
        self,
        InputDataConfig: ClientStartEntitiesDetectionJobInputDataConfigTypeDef,
        OutputDataConfig: ClientStartEntitiesDetectionJobOutputDataConfigTypeDef,
        DataAccessRoleArn: str,
        LanguageCode: Literal[
            "en", "es", "fr", "de", "it", "pt", "ar", "hi", "ja", "ko", "zh", "zh-TW"
        ],
        JobName: str = None,
        EntityRecognizerArn: str = None,
        ClientRequestToken: str = None,
        VolumeKmsKeyId: str = None,
        VpcConfig: ClientStartEntitiesDetectionJobVpcConfigTypeDef = None,
    ) -> ClientStartEntitiesDetectionJobResponseTypeDef:
        """
        Starts an asynchronous entity detection job for a collection of documents. Use the operation
        to track the status of a job.

        This API can be used for either standard entity detection or custom entity recognition. In
        order to be used for custom entity recognition, the optional ``EntityRecognizerArn`` must be
        used in order to provide access to the recognizer being used to detect the custom entity.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/comprehend-2017-11-27/StartEntitiesDetectionJob>`_

        **Request Syntax**
        ::

          response = client.start_entities_detection_job(
              InputDataConfig={
                  'S3Uri': 'string',
                  'InputFormat': 'ONE_DOC_PER_FILE'|'ONE_DOC_PER_LINE'
              },
              OutputDataConfig={
                  'S3Uri': 'string',
                  'KmsKeyId': 'string'
              },
              DataAccessRoleArn='string',
              JobName='string',
              EntityRecognizerArn='string',
              LanguageCode='en'|'es'|'fr'|'de'|'it'|'pt'|'ar'|'hi'|'ja'|'ko'|'zh'|'zh-TW',
              ClientRequestToken='string',
              VolumeKmsKeyId='string',
              VpcConfig={
                  'SecurityGroupIds': [
                      'string',
                  ],
                  'Subnets': [
                      'string',
                  ]
              }
          )
        :type InputDataConfig: dict
        :param InputDataConfig: **[REQUIRED]**

          Specifies the format and location of the input data for the job.

          - **S3Uri** *(string) --* **[REQUIRED]**

            The Amazon S3 URI for the input data. The URI must be in same region as the API endpoint
            that you are calling. The URI can point to a single input file or it can provide the
            prefix for a collection of data files.

            For example, if you use the URI ``S3://bucketName/prefix`` , if the prefix is a single
            file, Amazon Comprehend uses that file as input. If more than one file begins with the
            prefix, Amazon Comprehend uses all of them as input.

          - **InputFormat** *(string) --*

            Specifies how the text in an input file should be processed:

            * ``ONE_DOC_PER_FILE`` - Each file is considered a separate document. Use this option
            when you are processing large documents, such as newspaper articles or scientific
            papers.

            * ``ONE_DOC_PER_LINE`` - Each line in a file is considered a separate document. Use this
            option when you are processing many short documents, such as text messages.

        :type OutputDataConfig: dict
        :param OutputDataConfig: **[REQUIRED]**

          Specifies where to send the output files.

          - **S3Uri** *(string) --* **[REQUIRED]**

            When you use the ``OutputDataConfig`` object with asynchronous operations, you specify
            the Amazon S3 location where you want to write the output data. The URI must be in the
            same region as the API endpoint that you are calling. The location is used as the prefix
            for the actual location of the output file.

            When the topic detection job is finished, the service creates an output file in a
            directory specific to the job. The ``S3Uri`` field contains the location of the output
            file, called ``output.tar.gz`` . It is a compressed archive that contains the ouput of
            the operation.

          - **KmsKeyId** *(string) --*

            ID for the AWS Key Management Service (KMS) key that Amazon Comprehend uses to encrypt
            the output results from an analysis job. The KmsKeyId can be one of the following
            formats:

            * KMS Key ID: ``"1234abcd-12ab-34cd-56ef-1234567890ab"``

            * Amazon Resource Name (ARN) of a KMS Key:
            ``"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"``

            * KMS Key Alias: ``"alias/ExampleAlias"``

            * ARN of a KMS Key Alias: ``"arn:aws:kms:us-west-2:111122223333:alias/ExampleAlias"``

        :type DataAccessRoleArn: string
        :param DataAccessRoleArn: **[REQUIRED]**

          The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that
          grants Amazon Comprehend read access to your input data. For more information, see
          `https\\://docs.aws.amazon.com/comprehend/latest/dg/access-control-managing-permissions.html#auth-role-permissions
          <https://docs.aws.amazon.com/comprehend/latest/dg/access-control-managing-permissions.html#auth-role-permissions>`__
          .

        :type JobName: string
        :param JobName:

          The identifier of the job.

        :type EntityRecognizerArn: string
        :param EntityRecognizerArn:

          The Amazon Resource Name (ARN) that identifies the specific entity recognizer to be used
          by the ``StartEntitiesDetectionJob`` . This ARN is optional and is only used for a custom
          entity recognition job.

        :type LanguageCode: string
        :param LanguageCode: **[REQUIRED]**

          The language of the input documents. All documents must be in the same language. You can
          specify any of the languages supported by Amazon Comprehend. If custom entities
          recognition is used, this parameter is ignored and the language used for training the
          model is used instead.

        :type ClientRequestToken: string
        :param ClientRequestToken:

          A unique identifier for the request. If you don't set the client request token, Amazon
          Comprehend generates one.

          This field is autopopulated if not provided.

        :type VolumeKmsKeyId: string
        :param VolumeKmsKeyId:

          ID for the AWS Key Management Service (KMS) key that Amazon Comprehend uses to encrypt
          data on the storage volume attached to the ML compute instance(s) that process the
          analysis job. The VolumeKmsKeyId can be either of the following formats:

          * KMS Key ID: ``"1234abcd-12ab-34cd-56ef-1234567890ab"``

          * Amazon Resource Name (ARN) of a KMS Key:
          ``"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"``

        :type VpcConfig: dict
        :param VpcConfig:

          Configuration parameters for an optional private Virtual Private Cloud (VPC) containing
          the resources you are using for your entity detection job. For more information, see
          `Amazon VPC <https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html>`__
          .

          - **SecurityGroupIds** *(list) --* **[REQUIRED]**

            The ID number for a security group on an instance of your private VPC. Security groups
            on your VPC function serve as a virtual firewall to control inbound and outbound traffic
            and provides security for the resources that you’ll be accessing on the VPC. This ID
            number is preceded by "sg-", for instance: "sg-03b388029b0a285ea". For more information,
            see `Security Groups for your VPC
            <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html>`__ .

            - *(string) --*

          - **Subnets** *(list) --* **[REQUIRED]**

            The ID for each subnet being used in your private VPC. This subnet is a subset of the a
            range of IPv4 addresses used by the VPC and is specific to a given availability zone in
            the VPC’s region. This ID number is preceded by "subnet-", for instance:
            "subnet-04ccf456919e69055". For more information, see `VPCs and Subnets
            <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html>`__ .

            - *(string) --*

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'JobId': 'string',
                'JobStatus':
                'SUBMITTED'|'IN_PROGRESS'|'COMPLETED'|'FAILED'|'STOP_REQUESTED'|'STOPPED'
            }
          **Response Structure**

          - *(dict) --*

            - **JobId** *(string) --*

              The identifier generated for the job. To get the status of job, use this identifier
              with the operation.

            - **JobStatus** *(string) --*

              The status of the job.

              * SUBMITTED - The job has been received and is queued for processing.

              * IN_PROGRESS - Amazon Comprehend is processing the job.

              * COMPLETED - The job was successfully completed and the output is available.

              * FAILED - The job did not complete. To get details, use the operation.

              * STOP_REQUESTED - Amazon Comprehend has received a stop request for the job and is
              processing the request.

              * STOPPED - The job was successfully stopped without completing.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def start_key_phrases_detection_job(
        self,
        InputDataConfig: ClientStartKeyPhrasesDetectionJobInputDataConfigTypeDef,
        OutputDataConfig: ClientStartKeyPhrasesDetectionJobOutputDataConfigTypeDef,
        DataAccessRoleArn: str,
        LanguageCode: Literal[
            "en", "es", "fr", "de", "it", "pt", "ar", "hi", "ja", "ko", "zh", "zh-TW"
        ],
        JobName: str = None,
        ClientRequestToken: str = None,
        VolumeKmsKeyId: str = None,
        VpcConfig: ClientStartKeyPhrasesDetectionJobVpcConfigTypeDef = None,
    ) -> ClientStartKeyPhrasesDetectionJobResponseTypeDef:
        """
        Starts an asynchronous key phrase detection job for a collection of documents. Use the
        operation to track the status of a job.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/comprehend-2017-11-27/StartKeyPhrasesDetectionJob>`_

        **Request Syntax**
        ::

          response = client.start_key_phrases_detection_job(
              InputDataConfig={
                  'S3Uri': 'string',
                  'InputFormat': 'ONE_DOC_PER_FILE'|'ONE_DOC_PER_LINE'
              },
              OutputDataConfig={
                  'S3Uri': 'string',
                  'KmsKeyId': 'string'
              },
              DataAccessRoleArn='string',
              JobName='string',
              LanguageCode='en'|'es'|'fr'|'de'|'it'|'pt'|'ar'|'hi'|'ja'|'ko'|'zh'|'zh-TW',
              ClientRequestToken='string',
              VolumeKmsKeyId='string',
              VpcConfig={
                  'SecurityGroupIds': [
                      'string',
                  ],
                  'Subnets': [
                      'string',
                  ]
              }
          )
        :type InputDataConfig: dict
        :param InputDataConfig: **[REQUIRED]**

          Specifies the format and location of the input data for the job.

          - **S3Uri** *(string) --* **[REQUIRED]**

            The Amazon S3 URI for the input data. The URI must be in same region as the API endpoint
            that you are calling. The URI can point to a single input file or it can provide the
            prefix for a collection of data files.

            For example, if you use the URI ``S3://bucketName/prefix`` , if the prefix is a single
            file, Amazon Comprehend uses that file as input. If more than one file begins with the
            prefix, Amazon Comprehend uses all of them as input.

          - **InputFormat** *(string) --*

            Specifies how the text in an input file should be processed:

            * ``ONE_DOC_PER_FILE`` - Each file is considered a separate document. Use this option
            when you are processing large documents, such as newspaper articles or scientific
            papers.

            * ``ONE_DOC_PER_LINE`` - Each line in a file is considered a separate document. Use this
            option when you are processing many short documents, such as text messages.

        :type OutputDataConfig: dict
        :param OutputDataConfig: **[REQUIRED]**

          Specifies where to send the output files.

          - **S3Uri** *(string) --* **[REQUIRED]**

            When you use the ``OutputDataConfig`` object with asynchronous operations, you specify
            the Amazon S3 location where you want to write the output data. The URI must be in the
            same region as the API endpoint that you are calling. The location is used as the prefix
            for the actual location of the output file.

            When the topic detection job is finished, the service creates an output file in a
            directory specific to the job. The ``S3Uri`` field contains the location of the output
            file, called ``output.tar.gz`` . It is a compressed archive that contains the ouput of
            the operation.

          - **KmsKeyId** *(string) --*

            ID for the AWS Key Management Service (KMS) key that Amazon Comprehend uses to encrypt
            the output results from an analysis job. The KmsKeyId can be one of the following
            formats:

            * KMS Key ID: ``"1234abcd-12ab-34cd-56ef-1234567890ab"``

            * Amazon Resource Name (ARN) of a KMS Key:
            ``"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"``

            * KMS Key Alias: ``"alias/ExampleAlias"``

            * ARN of a KMS Key Alias: ``"arn:aws:kms:us-west-2:111122223333:alias/ExampleAlias"``

        :type DataAccessRoleArn: string
        :param DataAccessRoleArn: **[REQUIRED]**

          The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that
          grants Amazon Comprehend read access to your input data. For more information, see
          `https\\://docs.aws.amazon.com/comprehend/latest/dg/access-control-managing-permissions.html#auth-role-permissions
          <https://docs.aws.amazon.com/comprehend/latest/dg/access-control-managing-permissions.html#auth-role-permissions>`__
          .

        :type JobName: string
        :param JobName:

          The identifier of the job.

        :type LanguageCode: string
        :param LanguageCode: **[REQUIRED]**

          The language of the input documents. You can specify any of the primary languages
          supported by Amazon Comprehend. All documents must be in the same language.

        :type ClientRequestToken: string
        :param ClientRequestToken:

          A unique identifier for the request. If you don't set the client request token, Amazon
          Comprehend generates one.

          This field is autopopulated if not provided.

        :type VolumeKmsKeyId: string
        :param VolumeKmsKeyId:

          ID for the AWS Key Management Service (KMS) key that Amazon Comprehend uses to encrypt
          data on the storage volume attached to the ML compute instance(s) that process the
          analysis job. The VolumeKmsKeyId can be either of the following formats:

          * KMS Key ID: ``"1234abcd-12ab-34cd-56ef-1234567890ab"``

          * Amazon Resource Name (ARN) of a KMS Key:
          ``"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"``

        :type VpcConfig: dict
        :param VpcConfig:

          Configuration parameters for an optional private Virtual Private Cloud (VPC) containing
          the resources you are using for your key phrases detection job. For more information, see
          `Amazon VPC <https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html>`__
          .

          - **SecurityGroupIds** *(list) --* **[REQUIRED]**

            The ID number for a security group on an instance of your private VPC. Security groups
            on your VPC function serve as a virtual firewall to control inbound and outbound traffic
            and provides security for the resources that you’ll be accessing on the VPC. This ID
            number is preceded by "sg-", for instance: "sg-03b388029b0a285ea". For more information,
            see `Security Groups for your VPC
            <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html>`__ .

            - *(string) --*

          - **Subnets** *(list) --* **[REQUIRED]**

            The ID for each subnet being used in your private VPC. This subnet is a subset of the a
            range of IPv4 addresses used by the VPC and is specific to a given availability zone in
            the VPC’s region. This ID number is preceded by "subnet-", for instance:
            "subnet-04ccf456919e69055". For more information, see `VPCs and Subnets
            <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html>`__ .

            - *(string) --*

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'JobId': 'string',
                'JobStatus':
                'SUBMITTED'|'IN_PROGRESS'|'COMPLETED'|'FAILED'|'STOP_REQUESTED'|'STOPPED'
            }
          **Response Structure**

          - *(dict) --*

            - **JobId** *(string) --*

              The identifier generated for the job. To get the status of a job, use this identifier
              with the operation.

            - **JobStatus** *(string) --*

              The status of the job.

              * SUBMITTED - The job has been received and is queued for processing.

              * IN_PROGRESS - Amazon Comprehend is processing the job.

              * COMPLETED - The job was successfully completed and the output is available.

              * FAILED - The job did not complete. To get details, use the operation.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def start_sentiment_detection_job(
        self,
        InputDataConfig: ClientStartSentimentDetectionJobInputDataConfigTypeDef,
        OutputDataConfig: ClientStartSentimentDetectionJobOutputDataConfigTypeDef,
        DataAccessRoleArn: str,
        LanguageCode: Literal[
            "en", "es", "fr", "de", "it", "pt", "ar", "hi", "ja", "ko", "zh", "zh-TW"
        ],
        JobName: str = None,
        ClientRequestToken: str = None,
        VolumeKmsKeyId: str = None,
        VpcConfig: ClientStartSentimentDetectionJobVpcConfigTypeDef = None,
    ) -> ClientStartSentimentDetectionJobResponseTypeDef:
        """
        Starts an asynchronous sentiment detection job for a collection of documents. use the
        operation to track the status of a job.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/comprehend-2017-11-27/StartSentimentDetectionJob>`_

        **Request Syntax**
        ::

          response = client.start_sentiment_detection_job(
              InputDataConfig={
                  'S3Uri': 'string',
                  'InputFormat': 'ONE_DOC_PER_FILE'|'ONE_DOC_PER_LINE'
              },
              OutputDataConfig={
                  'S3Uri': 'string',
                  'KmsKeyId': 'string'
              },
              DataAccessRoleArn='string',
              JobName='string',
              LanguageCode='en'|'es'|'fr'|'de'|'it'|'pt'|'ar'|'hi'|'ja'|'ko'|'zh'|'zh-TW',
              ClientRequestToken='string',
              VolumeKmsKeyId='string',
              VpcConfig={
                  'SecurityGroupIds': [
                      'string',
                  ],
                  'Subnets': [
                      'string',
                  ]
              }
          )
        :type InputDataConfig: dict
        :param InputDataConfig: **[REQUIRED]**

          Specifies the format and location of the input data for the job.

          - **S3Uri** *(string) --* **[REQUIRED]**

            The Amazon S3 URI for the input data. The URI must be in same region as the API endpoint
            that you are calling. The URI can point to a single input file or it can provide the
            prefix for a collection of data files.

            For example, if you use the URI ``S3://bucketName/prefix`` , if the prefix is a single
            file, Amazon Comprehend uses that file as input. If more than one file begins with the
            prefix, Amazon Comprehend uses all of them as input.

          - **InputFormat** *(string) --*

            Specifies how the text in an input file should be processed:

            * ``ONE_DOC_PER_FILE`` - Each file is considered a separate document. Use this option
            when you are processing large documents, such as newspaper articles or scientific
            papers.

            * ``ONE_DOC_PER_LINE`` - Each line in a file is considered a separate document. Use this
            option when you are processing many short documents, such as text messages.

        :type OutputDataConfig: dict
        :param OutputDataConfig: **[REQUIRED]**

          Specifies where to send the output files.

          - **S3Uri** *(string) --* **[REQUIRED]**

            When you use the ``OutputDataConfig`` object with asynchronous operations, you specify
            the Amazon S3 location where you want to write the output data. The URI must be in the
            same region as the API endpoint that you are calling. The location is used as the prefix
            for the actual location of the output file.

            When the topic detection job is finished, the service creates an output file in a
            directory specific to the job. The ``S3Uri`` field contains the location of the output
            file, called ``output.tar.gz`` . It is a compressed archive that contains the ouput of
            the operation.

          - **KmsKeyId** *(string) --*

            ID for the AWS Key Management Service (KMS) key that Amazon Comprehend uses to encrypt
            the output results from an analysis job. The KmsKeyId can be one of the following
            formats:

            * KMS Key ID: ``"1234abcd-12ab-34cd-56ef-1234567890ab"``

            * Amazon Resource Name (ARN) of a KMS Key:
            ``"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"``

            * KMS Key Alias: ``"alias/ExampleAlias"``

            * ARN of a KMS Key Alias: ``"arn:aws:kms:us-west-2:111122223333:alias/ExampleAlias"``

        :type DataAccessRoleArn: string
        :param DataAccessRoleArn: **[REQUIRED]**

          The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that
          grants Amazon Comprehend read access to your input data. For more information, see
          `https\\://docs.aws.amazon.com/comprehend/latest/dg/access-control-managing-permissions.html#auth-role-permissions
          <https://docs.aws.amazon.com/comprehend/latest/dg/access-control-managing-permissions.html#auth-role-permissions>`__
          .

        :type JobName: string
        :param JobName:

          The identifier of the job.

        :type LanguageCode: string
        :param LanguageCode: **[REQUIRED]**

          The language of the input documents. You can specify any of the primary languages
          supported by Amazon Comprehend. All documents must be in the same language.

        :type ClientRequestToken: string
        :param ClientRequestToken:

          A unique identifier for the request. If you don't set the client request token, Amazon
          Comprehend generates one.

          This field is autopopulated if not provided.

        :type VolumeKmsKeyId: string
        :param VolumeKmsKeyId:

          ID for the AWS Key Management Service (KMS) key that Amazon Comprehend uses to encrypt
          data on the storage volume attached to the ML compute instance(s) that process the
          analysis job. The VolumeKmsKeyId can be either of the following formats:

          * KMS Key ID: ``"1234abcd-12ab-34cd-56ef-1234567890ab"``

          * Amazon Resource Name (ARN) of a KMS Key:
          ``"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"``

        :type VpcConfig: dict
        :param VpcConfig:

          Configuration parameters for an optional private Virtual Private Cloud (VPC) containing
          the resources you are using for your sentiment detection job. For more information, see
          `Amazon VPC <https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html>`__
          .

          - **SecurityGroupIds** *(list) --* **[REQUIRED]**

            The ID number for a security group on an instance of your private VPC. Security groups
            on your VPC function serve as a virtual firewall to control inbound and outbound traffic
            and provides security for the resources that you’ll be accessing on the VPC. This ID
            number is preceded by "sg-", for instance: "sg-03b388029b0a285ea". For more information,
            see `Security Groups for your VPC
            <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html>`__ .

            - *(string) --*

          - **Subnets** *(list) --* **[REQUIRED]**

            The ID for each subnet being used in your private VPC. This subnet is a subset of the a
            range of IPv4 addresses used by the VPC and is specific to a given availability zone in
            the VPC’s region. This ID number is preceded by "subnet-", for instance:
            "subnet-04ccf456919e69055". For more information, see `VPCs and Subnets
            <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html>`__ .

            - *(string) --*

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'JobId': 'string',
                'JobStatus':
                'SUBMITTED'|'IN_PROGRESS'|'COMPLETED'|'FAILED'|'STOP_REQUESTED'|'STOPPED'
            }
          **Response Structure**

          - *(dict) --*

            - **JobId** *(string) --*

              The identifier generated for the job. To get the status of a job, use this identifier
              with the operation.

            - **JobStatus** *(string) --*

              The status of the job.

              * SUBMITTED - The job has been received and is queued for processing.

              * IN_PROGRESS - Amazon Comprehend is processing the job.

              * COMPLETED - The job was successfully completed and the output is available.

              * FAILED - The job did not complete. To get details, use the operation.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def start_topics_detection_job(
        self,
        InputDataConfig: ClientStartTopicsDetectionJobInputDataConfigTypeDef,
        OutputDataConfig: ClientStartTopicsDetectionJobOutputDataConfigTypeDef,
        DataAccessRoleArn: str,
        JobName: str = None,
        NumberOfTopics: int = None,
        ClientRequestToken: str = None,
        VolumeKmsKeyId: str = None,
        VpcConfig: ClientStartTopicsDetectionJobVpcConfigTypeDef = None,
    ) -> ClientStartTopicsDetectionJobResponseTypeDef:
        """
        Starts an asynchronous topic detection job. Use the ``DescribeTopicDetectionJob`` operation
        to track the status of a job.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/comprehend-2017-11-27/StartTopicsDetectionJob>`_

        **Request Syntax**
        ::

          response = client.start_topics_detection_job(
              InputDataConfig={
                  'S3Uri': 'string',
                  'InputFormat': 'ONE_DOC_PER_FILE'|'ONE_DOC_PER_LINE'
              },
              OutputDataConfig={
                  'S3Uri': 'string',
                  'KmsKeyId': 'string'
              },
              DataAccessRoleArn='string',
              JobName='string',
              NumberOfTopics=123,
              ClientRequestToken='string',
              VolumeKmsKeyId='string',
              VpcConfig={
                  'SecurityGroupIds': [
                      'string',
                  ],
                  'Subnets': [
                      'string',
                  ]
              }
          )
        :type InputDataConfig: dict
        :param InputDataConfig: **[REQUIRED]**

          Specifies the format and location of the input data for the job.

          - **S3Uri** *(string) --* **[REQUIRED]**

            The Amazon S3 URI for the input data. The URI must be in same region as the API endpoint
            that you are calling. The URI can point to a single input file or it can provide the
            prefix for a collection of data files.

            For example, if you use the URI ``S3://bucketName/prefix`` , if the prefix is a single
            file, Amazon Comprehend uses that file as input. If more than one file begins with the
            prefix, Amazon Comprehend uses all of them as input.

          - **InputFormat** *(string) --*

            Specifies how the text in an input file should be processed:

            * ``ONE_DOC_PER_FILE`` - Each file is considered a separate document. Use this option
            when you are processing large documents, such as newspaper articles or scientific
            papers.

            * ``ONE_DOC_PER_LINE`` - Each line in a file is considered a separate document. Use this
            option when you are processing many short documents, such as text messages.

        :type OutputDataConfig: dict
        :param OutputDataConfig: **[REQUIRED]**

          Specifies where to send the output files. The output is a compressed archive with two
          files, ``topic-terms.csv`` that lists the terms associated with each topic, and
          ``doc-topics.csv`` that lists the documents associated with each topic

          - **S3Uri** *(string) --* **[REQUIRED]**

            When you use the ``OutputDataConfig`` object with asynchronous operations, you specify
            the Amazon S3 location where you want to write the output data. The URI must be in the
            same region as the API endpoint that you are calling. The location is used as the prefix
            for the actual location of the output file.

            When the topic detection job is finished, the service creates an output file in a
            directory specific to the job. The ``S3Uri`` field contains the location of the output
            file, called ``output.tar.gz`` . It is a compressed archive that contains the ouput of
            the operation.

          - **KmsKeyId** *(string) --*

            ID for the AWS Key Management Service (KMS) key that Amazon Comprehend uses to encrypt
            the output results from an analysis job. The KmsKeyId can be one of the following
            formats:

            * KMS Key ID: ``"1234abcd-12ab-34cd-56ef-1234567890ab"``

            * Amazon Resource Name (ARN) of a KMS Key:
            ``"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"``

            * KMS Key Alias: ``"alias/ExampleAlias"``

            * ARN of a KMS Key Alias: ``"arn:aws:kms:us-west-2:111122223333:alias/ExampleAlias"``

        :type DataAccessRoleArn: string
        :param DataAccessRoleArn: **[REQUIRED]**

          The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that
          grants Amazon Comprehend read access to your input data. For more information, see
          `https\\://docs.aws.amazon.com/comprehend/latest/dg/access-control-managing-permissions.html#auth-role-permissions
          <https://docs.aws.amazon.com/comprehend/latest/dg/access-control-managing-permissions.html#auth-role-permissions>`__
          .

        :type JobName: string
        :param JobName:

          The identifier of the job.

        :type NumberOfTopics: integer
        :param NumberOfTopics:

          The number of topics to detect.

        :type ClientRequestToken: string
        :param ClientRequestToken:

          A unique identifier for the request. If you do not set the client request token, Amazon
          Comprehend generates one.

          This field is autopopulated if not provided.

        :type VolumeKmsKeyId: string
        :param VolumeKmsKeyId:

          ID for the AWS Key Management Service (KMS) key that Amazon Comprehend uses to encrypt
          data on the storage volume attached to the ML compute instance(s) that process the
          analysis job. The VolumeKmsKeyId can be either of the following formats:

          * KMS Key ID: ``"1234abcd-12ab-34cd-56ef-1234567890ab"``

          * Amazon Resource Name (ARN) of a KMS Key:
          ``"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"``

        :type VpcConfig: dict
        :param VpcConfig:

          Configuration parameters for an optional private Virtual Private Cloud (VPC) containing
          the resources you are using for your topic detection job. For more information, see
          `Amazon VPC <https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html>`__
          .

          - **SecurityGroupIds** *(list) --* **[REQUIRED]**

            The ID number for a security group on an instance of your private VPC. Security groups
            on your VPC function serve as a virtual firewall to control inbound and outbound traffic
            and provides security for the resources that you’ll be accessing on the VPC. This ID
            number is preceded by "sg-", for instance: "sg-03b388029b0a285ea". For more information,
            see `Security Groups for your VPC
            <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html>`__ .

            - *(string) --*

          - **Subnets** *(list) --* **[REQUIRED]**

            The ID for each subnet being used in your private VPC. This subnet is a subset of the a
            range of IPv4 addresses used by the VPC and is specific to a given availability zone in
            the VPC’s region. This ID number is preceded by "subnet-", for instance:
            "subnet-04ccf456919e69055". For more information, see `VPCs and Subnets
            <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html>`__ .

            - *(string) --*

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'JobId': 'string',
                'JobStatus':
                'SUBMITTED'|'IN_PROGRESS'|'COMPLETED'|'FAILED'|'STOP_REQUESTED'|'STOPPED'
            }
          **Response Structure**

          - *(dict) --*

            - **JobId** *(string) --*

              The identifier generated for the job. To get the status of the job, use this
              identifier with the ``DescribeTopicDetectionJob`` operation.

            - **JobStatus** *(string) --*

              The status of the job:

              * SUBMITTED - The job has been received and is queued for processing.

              * IN_PROGRESS - Amazon Comprehend is processing the job.

              * COMPLETED - The job was successfully completed and the output is available.

              * FAILED - The job did not complete. To get details, use the
              ``DescribeTopicDetectionJob`` operation.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def stop_dominant_language_detection_job(
        self, JobId: str
    ) -> ClientStopDominantLanguageDetectionJobResponseTypeDef:
        """
        Stops a dominant language detection job in progress.

        If the job state is ``IN_PROGRESS`` the job is marked for termination and put into the
        ``STOP_REQUESTED`` state. If the job completes before it can be stopped, it is put into the
        ``COMPLETED`` state; otherwise the job is stopped and put into the ``STOPPED`` state.

        If the job is in the ``COMPLETED`` or ``FAILED`` state when you call the
        ``StopDominantLanguageDetectionJob`` operation, the operation returns a 400 Internal Request
        Exception.

        When a job is stopped, any documents already processed are written to the output location.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/comprehend-2017-11-27/StopDominantLanguageDetectionJob>`_

        **Request Syntax**
        ::

          response = client.stop_dominant_language_detection_job(
              JobId='string'
          )
        :type JobId: string
        :param JobId: **[REQUIRED]**

          The identifier of the dominant language detection job to stop.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'JobId': 'string',
                'JobStatus':
                'SUBMITTED'|'IN_PROGRESS'|'COMPLETED'|'FAILED'|'STOP_REQUESTED'|'STOPPED'
            }
          **Response Structure**

          - *(dict) --*

            - **JobId** *(string) --*

              The identifier of the dominant language detection job to stop.

            - **JobStatus** *(string) --*

              Either ``STOP_REQUESTED`` if the job is currently running, or ``STOPPED`` if the job
              was previously stopped with the ``StopDominantLanguageDetectionJob`` operation.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def stop_entities_detection_job(
        self, JobId: str
    ) -> ClientStopEntitiesDetectionJobResponseTypeDef:
        """
        Stops an entities detection job in progress.

        If the job state is ``IN_PROGRESS`` the job is marked for termination and put into the
        ``STOP_REQUESTED`` state. If the job completes before it can be stopped, it is put into the
        ``COMPLETED`` state; otherwise the job is stopped and put into the ``STOPPED`` state.

        If the job is in the ``COMPLETED`` or ``FAILED`` state when you call the
        ``StopDominantLanguageDetectionJob`` operation, the operation returns a 400 Internal Request
        Exception.

        When a job is stopped, any documents already processed are written to the output location.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/comprehend-2017-11-27/StopEntitiesDetectionJob>`_

        **Request Syntax**
        ::

          response = client.stop_entities_detection_job(
              JobId='string'
          )
        :type JobId: string
        :param JobId: **[REQUIRED]**

          The identifier of the entities detection job to stop.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'JobId': 'string',
                'JobStatus':
                'SUBMITTED'|'IN_PROGRESS'|'COMPLETED'|'FAILED'|'STOP_REQUESTED'|'STOPPED'
            }
          **Response Structure**

          - *(dict) --*

            - **JobId** *(string) --*

              The identifier of the entities detection job to stop.

            - **JobStatus** *(string) --*

              Either ``STOP_REQUESTED`` if the job is currently running, or ``STOPPED`` if the job
              was previously stopped with the ``StopEntitiesDetectionJob`` operation.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def stop_key_phrases_detection_job(
        self, JobId: str
    ) -> ClientStopKeyPhrasesDetectionJobResponseTypeDef:
        """
        Stops a key phrases detection job in progress.

        If the job state is ``IN_PROGRESS`` the job is marked for termination and put into the
        ``STOP_REQUESTED`` state. If the job completes before it can be stopped, it is put into the
        ``COMPLETED`` state; otherwise the job is stopped and put into the ``STOPPED`` state.

        If the job is in the ``COMPLETED`` or ``FAILED`` state when you call the
        ``StopDominantLanguageDetectionJob`` operation, the operation returns a 400 Internal Request
        Exception.

        When a job is stopped, any documents already processed are written to the output location.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/comprehend-2017-11-27/StopKeyPhrasesDetectionJob>`_

        **Request Syntax**
        ::

          response = client.stop_key_phrases_detection_job(
              JobId='string'
          )
        :type JobId: string
        :param JobId: **[REQUIRED]**

          The identifier of the key phrases detection job to stop.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'JobId': 'string',
                'JobStatus':
                'SUBMITTED'|'IN_PROGRESS'|'COMPLETED'|'FAILED'|'STOP_REQUESTED'|'STOPPED'
            }
          **Response Structure**

          - *(dict) --*

            - **JobId** *(string) --*

              The identifier of the key phrases detection job to stop.

            - **JobStatus** *(string) --*

              Either ``STOP_REQUESTED`` if the job is currently running, or ``STOPPED`` if the job
              was previously stopped with the ``StopKeyPhrasesDetectionJob`` operation.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def stop_sentiment_detection_job(
        self, JobId: str
    ) -> ClientStopSentimentDetectionJobResponseTypeDef:
        """
        Stops a sentiment detection job in progress.

        If the job state is ``IN_PROGRESS`` the job is marked for termination and put into the
        ``STOP_REQUESTED`` state. If the job completes before it can be stopped, it is put into the
        ``COMPLETED`` state; otherwise the job is be stopped and put into the ``STOPPED`` state.

        If the job is in the ``COMPLETED`` or ``FAILED`` state when you call the
        ``StopDominantLanguageDetectionJob`` operation, the operation returns a 400 Internal Request
        Exception.

        When a job is stopped, any documents already processed are written to the output location.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/comprehend-2017-11-27/StopSentimentDetectionJob>`_

        **Request Syntax**
        ::

          response = client.stop_sentiment_detection_job(
              JobId='string'
          )
        :type JobId: string
        :param JobId: **[REQUIRED]**

          The identifier of the sentiment detection job to stop.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'JobId': 'string',
                'JobStatus':
                'SUBMITTED'|'IN_PROGRESS'|'COMPLETED'|'FAILED'|'STOP_REQUESTED'|'STOPPED'
            }
          **Response Structure**

          - *(dict) --*

            - **JobId** *(string) --*

              The identifier of the sentiment detection job to stop.

            - **JobStatus** *(string) --*

              Either ``STOP_REQUESTED`` if the job is currently running, or ``STOPPED`` if the job
              was previously stopped with the ``StopSentimentDetectionJob`` operation.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def stop_training_document_classifier(self, DocumentClassifierArn: str) -> Dict[str, Any]:
        """
        Stops a document classifier training job while in progress.

        If the training job state is ``TRAINING`` , the job is marked for termination and put into
        the ``STOP_REQUESTED`` state. If the training job completes before it can be stopped, it is
        put into the ``TRAINED`` ; otherwise the training job is stopped and put into the
        ``STOPPED`` state and the service sends back an HTTP 200 response with an empty HTTP body.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/comprehend-2017-11-27/StopTrainingDocumentClassifier>`_

        **Request Syntax**
        ::

          response = client.stop_training_document_classifier(
              DocumentClassifierArn='string'
          )
        :type DocumentClassifierArn: string
        :param DocumentClassifierArn: **[REQUIRED]**

          The Amazon Resource Name (ARN) that identifies the document classifier currently being
          trained.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {}
          **Response Structure**

          - *(dict) --*
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def stop_training_entity_recognizer(self, EntityRecognizerArn: str) -> Dict[str, Any]:
        """
        Stops an entity recognizer training job while in progress.

        If the training job state is ``TRAINING`` , the job is marked for termination and put into
        the ``STOP_REQUESTED`` state. If the training job completes before it can be stopped, it is
        put into the ``TRAINED`` ; otherwise the training job is stopped and putted into the
        ``STOPPED`` state and the service sends back an HTTP 200 response with an empty HTTP body.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/comprehend-2017-11-27/StopTrainingEntityRecognizer>`_

        **Request Syntax**
        ::

          response = client.stop_training_entity_recognizer(
              EntityRecognizerArn='string'
          )
        :type EntityRecognizerArn: string
        :param EntityRecognizerArn: **[REQUIRED]**

          The Amazon Resource Name (ARN) that identifies the entity recognizer currently being
          trained.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {}
          **Response Structure**

          - *(dict) --*
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def tag_resource(
        self, ResourceArn: str, Tags: List[ClientTagResourceTagsTypeDef]
    ) -> Dict[str, Any]:
        """
        Associates a specific tag with an Amazon Comprehend resource. A tag is a key-value pair that
        adds as a metadata to a resource used by Amazon Comprehend. For example, a tag with "Sales"
        as the key might be added to a resource to indicate its use by the sales department.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/comprehend-2017-11-27/TagResource>`_

        **Request Syntax**
        ::

          response = client.tag_resource(
              ResourceArn='string',
              Tags=[
                  {
                      'Key': 'string',
                      'Value': 'string'
                  },
              ]
          )
        :type ResourceArn: string
        :param ResourceArn: **[REQUIRED]**

          The Amazon Resource Name (ARN) of the given Amazon Comprehend resource to which you want
          to associate the tags.

        :type Tags: list
        :param Tags: **[REQUIRED]**

          Tags being associated with a specific Amazon Comprehend resource. There can be a maximum
          of 50 tags (both existing and pending) associated with a specific resource.

          - *(dict) --*

            A key-value pair that adds as a metadata to a resource used by Amazon Comprehend. For
            example, a tag with the key-value pair ‘Department’:’Sales’ might be added to a resource
            to indicate its use by a particular department.

            - **Key** *(string) --* **[REQUIRED]**

              The initial part of a key-value pair that forms a tag associated with a given
              resource. For instance, if you want to show which resources are used by which
              departments, you might use “Department” as the key portion of the pair, with multiple
              possible values such as “sales,” “legal,” and “administration.”

            - **Value** *(string) --*

              The second part of a key-value pair that forms a tag associated with a given resource.
              For instance, if you want to show which resources are used by which departments, you
              might use “Department” as the initial (key) portion of the pair, with a value of
              “sales” to indicate the sales department.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {}
          **Response Structure**

          - *(dict) --*
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def untag_resource(self, ResourceArn: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        Removes a specific tag associated with an Amazon Comprehend resource.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/comprehend-2017-11-27/UntagResource>`_

        **Request Syntax**
        ::

          response = client.untag_resource(
              ResourceArn='string',
              TagKeys=[
                  'string',
              ]
          )
        :type ResourceArn: string
        :param ResourceArn: **[REQUIRED]**

          The Amazon Resource Name (ARN) of the given Amazon Comprehend resource from which you want
          to remove the tags.

        :type TagKeys: list
        :param TagKeys: **[REQUIRED]**

          The initial part of a key-value pair that forms a tag being removed from a given resource.
          For example, a tag with "Sales" as the key might be added to a resource to indicate its
          use by the sales department. Keys must be unique and cannot be duplicated for a particular
          resource.

          - *(string) --*

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {}
          **Response Structure**

          - *(dict) --*
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_endpoint(self, EndpointArn: str, DesiredInferenceUnits: int) -> Dict[str, Any]:
        """
        Updates information about the specified endpoint.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/comprehend-2017-11-27/UpdateEndpoint>`_

        **Request Syntax**
        ::

          response = client.update_endpoint(
              EndpointArn='string',
              DesiredInferenceUnits=123
          )
        :type EndpointArn: string
        :param EndpointArn: **[REQUIRED]**

          The Amazon Resource Number (ARN) of the endpoint being updated.

        :type DesiredInferenceUnits: integer
        :param DesiredInferenceUnits: **[REQUIRED]**

          The desired number of inference units to be used by the model using this endpoint. Each
          inference unit represents of a throughput of 100 characters per second.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {}
          **Response Structure**

          - *(dict) --*
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_document_classification_jobs"]
    ) -> paginator_scope.ListDocumentClassificationJobsPaginator:
        """
        Get Paginator for `list_document_classification_jobs` operation.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_document_classifiers"]
    ) -> paginator_scope.ListDocumentClassifiersPaginator:
        """
        Get Paginator for `list_document_classifiers` operation.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_dominant_language_detection_jobs"]
    ) -> paginator_scope.ListDominantLanguageDetectionJobsPaginator:
        """
        Get Paginator for `list_dominant_language_detection_jobs` operation.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_entities_detection_jobs"]
    ) -> paginator_scope.ListEntitiesDetectionJobsPaginator:
        """
        Get Paginator for `list_entities_detection_jobs` operation.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_entity_recognizers"]
    ) -> paginator_scope.ListEntityRecognizersPaginator:
        """
        Get Paginator for `list_entity_recognizers` operation.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_key_phrases_detection_jobs"]
    ) -> paginator_scope.ListKeyPhrasesDetectionJobsPaginator:
        """
        Get Paginator for `list_key_phrases_detection_jobs` operation.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_sentiment_detection_jobs"]
    ) -> paginator_scope.ListSentimentDetectionJobsPaginator:
        """
        Get Paginator for `list_sentiment_detection_jobs` operation.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_topics_detection_jobs"]
    ) -> paginator_scope.ListTopicsDetectionJobsPaginator:
        """
        Get Paginator for `list_topics_detection_jobs` operation.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(self, operation_name: str) -> Boto3Paginator:
        """
        Create a paginator for an operation.

        :type operation_name: string
        :param operation_name: The operation name.  This is the same name
            as the method name on the client.  For example, if the
            method name is ``create_foo``, and you'd normally invoke the
            operation as ``client.create_foo(**kwargs)``, if the
            ``create_foo`` operation can be paginated, you can use the
            call ``client.get_paginator("create_foo")``.

        :raise OperationNotPageableError: Raised if the operation is not
            pageable.  You can use the ``client.can_paginate`` method to
            check if an operation is pageable.

        :rtype: L{botocore.paginate.Paginator}
        :return: A paginator object.
        """


class Exceptions:
    BatchSizeLimitExceededException: Boto3ClientError
    ClientError: Boto3ClientError
    ConcurrentModificationException: Boto3ClientError
    InternalServerException: Boto3ClientError
    InvalidFilterException: Boto3ClientError
    InvalidRequestException: Boto3ClientError
    JobNotFoundException: Boto3ClientError
    KmsKeyValidationException: Boto3ClientError
    ResourceInUseException: Boto3ClientError
    ResourceLimitExceededException: Boto3ClientError
    ResourceNotFoundException: Boto3ClientError
    ResourceUnavailableException: Boto3ClientError
    TextSizeLimitExceededException: Boto3ClientError
    TooManyRequestsException: Boto3ClientError
    TooManyTagKeysException: Boto3ClientError
    TooManyTagsException: Boto3ClientError
    UnsupportedLanguageException: Boto3ClientError
