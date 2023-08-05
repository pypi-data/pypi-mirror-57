"Main interface for comprehend service Paginators"
from __future__ import annotations

from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_comprehend.type_defs import (
    ListDocumentClassificationJobsPaginateFilterTypeDef,
    ListDocumentClassificationJobsPaginatePaginationConfigTypeDef,
    ListDocumentClassificationJobsPaginateResponseTypeDef,
    ListDocumentClassifiersPaginateFilterTypeDef,
    ListDocumentClassifiersPaginatePaginationConfigTypeDef,
    ListDocumentClassifiersPaginateResponseTypeDef,
    ListDominantLanguageDetectionJobsPaginateFilterTypeDef,
    ListDominantLanguageDetectionJobsPaginatePaginationConfigTypeDef,
    ListDominantLanguageDetectionJobsPaginateResponseTypeDef,
    ListEntitiesDetectionJobsPaginateFilterTypeDef,
    ListEntitiesDetectionJobsPaginatePaginationConfigTypeDef,
    ListEntitiesDetectionJobsPaginateResponseTypeDef,
    ListEntityRecognizersPaginateFilterTypeDef,
    ListEntityRecognizersPaginatePaginationConfigTypeDef,
    ListEntityRecognizersPaginateResponseTypeDef,
    ListKeyPhrasesDetectionJobsPaginateFilterTypeDef,
    ListKeyPhrasesDetectionJobsPaginatePaginationConfigTypeDef,
    ListKeyPhrasesDetectionJobsPaginateResponseTypeDef,
    ListSentimentDetectionJobsPaginateFilterTypeDef,
    ListSentimentDetectionJobsPaginatePaginationConfigTypeDef,
    ListSentimentDetectionJobsPaginateResponseTypeDef,
    ListTopicsDetectionJobsPaginateFilterTypeDef,
    ListTopicsDetectionJobsPaginatePaginationConfigTypeDef,
    ListTopicsDetectionJobsPaginateResponseTypeDef,
)


__all__ = (
    "ListDocumentClassificationJobsPaginator",
    "ListDocumentClassifiersPaginator",
    "ListDominantLanguageDetectionJobsPaginator",
    "ListEntitiesDetectionJobsPaginator",
    "ListEntityRecognizersPaginator",
    "ListKeyPhrasesDetectionJobsPaginator",
    "ListSentimentDetectionJobsPaginator",
    "ListTopicsDetectionJobsPaginator",
)


class ListDocumentClassificationJobsPaginator(Boto3Paginator):
    """
    Paginator for `list_document_classification_jobs`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Filter: ListDocumentClassificationJobsPaginateFilterTypeDef = None,
        PaginationConfig: ListDocumentClassificationJobsPaginatePaginationConfigTypeDef = None,
    ) -> ListDocumentClassificationJobsPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`Comprehend.Client.list_document_classification_jobs`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/comprehend-2017-11-27/ListDocumentClassificationJobs>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              Filter={
                  'JobName': 'string',
                  'JobStatus':
                  'SUBMITTED'|'IN_PROGRESS'|'COMPLETED'|'FAILED'|'STOP_REQUESTED'
                  |'STOPPED',
                  'SubmitTimeBefore': datetime(2015, 1, 1),
                  'SubmitTimeAfter': datetime(2015, 1, 1)
              },
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
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

        :type PaginationConfig: dict
        :param PaginationConfig:

          A dictionary that provides parameters to control pagination.

          - **MaxItems** *(integer) --*

            The total number of items to return. If the total number of items available is more than
            the value specified in max-items then a ``NextToken`` will be provided in the output
            that you can use to resume pagination.

          - **PageSize** *(integer) --*

            The size of each page.

          - **StartingToken** *(string) --*

            A token to specify where to start paginating. This is the ``NextToken`` from a previous
            response.

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
        """


class ListDocumentClassifiersPaginator(Boto3Paginator):
    """
    Paginator for `list_document_classifiers`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Filter: ListDocumentClassifiersPaginateFilterTypeDef = None,
        PaginationConfig: ListDocumentClassifiersPaginatePaginationConfigTypeDef = None,
    ) -> ListDocumentClassifiersPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`Comprehend.Client.list_document_classifiers`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/comprehend-2017-11-27/ListDocumentClassifiers>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              Filter={
                  'Status':
                  'SUBMITTED'|'TRAINING'|'DELETING'|'STOP_REQUESTED'|'STOPPED'|'IN_ERROR'
                  |'TRAINED',
                  'SubmitTimeBefore': datetime(2015, 1, 1),
                  'SubmitTimeAfter': datetime(2015, 1, 1)
              },
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
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

        :type PaginationConfig: dict
        :param PaginationConfig:

          A dictionary that provides parameters to control pagination.

          - **MaxItems** *(integer) --*

            The total number of items to return. If the total number of items available is more than
            the value specified in max-items then a ``NextToken`` will be provided in the output
            that you can use to resume pagination.

          - **PageSize** *(integer) --*

            The size of each page.

          - **StartingToken** *(string) --*

            A token to specify where to start paginating. This is the ``NextToken`` from a previous
            response.

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
        """


class ListDominantLanguageDetectionJobsPaginator(Boto3Paginator):
    """
    Paginator for `list_dominant_language_detection_jobs`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Filter: ListDominantLanguageDetectionJobsPaginateFilterTypeDef = None,
        PaginationConfig: ListDominantLanguageDetectionJobsPaginatePaginationConfigTypeDef = None,
    ) -> ListDominantLanguageDetectionJobsPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`Comprehend.Client.list_dominant_language_detection_jobs`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/comprehend-2017-11-27/ListDominantLanguageDetectionJobs>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              Filter={
                  'JobName': 'string',
                  'JobStatus':
                  'SUBMITTED'|'IN_PROGRESS'|'COMPLETED'|'FAILED'|'STOP_REQUESTED'
                  |'STOPPED',
                  'SubmitTimeBefore': datetime(2015, 1, 1),
                  'SubmitTimeAfter': datetime(2015, 1, 1)
              },
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
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

        :type PaginationConfig: dict
        :param PaginationConfig:

          A dictionary that provides parameters to control pagination.

          - **MaxItems** *(integer) --*

            The total number of items to return. If the total number of items available is more than
            the value specified in max-items then a ``NextToken`` will be provided in the output
            that you can use to resume pagination.

          - **PageSize** *(integer) --*

            The size of each page.

          - **StartingToken** *(string) --*

            A token to specify where to start paginating. This is the ``NextToken`` from a previous
            response.

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
        """


class ListEntitiesDetectionJobsPaginator(Boto3Paginator):
    """
    Paginator for `list_entities_detection_jobs`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Filter: ListEntitiesDetectionJobsPaginateFilterTypeDef = None,
        PaginationConfig: ListEntitiesDetectionJobsPaginatePaginationConfigTypeDef = None,
    ) -> ListEntitiesDetectionJobsPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`Comprehend.Client.list_entities_detection_jobs`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/comprehend-2017-11-27/ListEntitiesDetectionJobs>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              Filter={
                  'JobName': 'string',
                  'JobStatus':
                  'SUBMITTED'|'IN_PROGRESS'|'COMPLETED'|'FAILED'|'STOP_REQUESTED'
                  |'STOPPED',
                  'SubmitTimeBefore': datetime(2015, 1, 1),
                  'SubmitTimeAfter': datetime(2015, 1, 1)
              },
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
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

        :type PaginationConfig: dict
        :param PaginationConfig:

          A dictionary that provides parameters to control pagination.

          - **MaxItems** *(integer) --*

            The total number of items to return. If the total number of items available is more than
            the value specified in max-items then a ``NextToken`` will be provided in the output
            that you can use to resume pagination.

          - **PageSize** *(integer) --*

            The size of each page.

          - **StartingToken** *(string) --*

            A token to specify where to start paginating. This is the ``NextToken`` from a previous
            response.

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
        """


class ListEntityRecognizersPaginator(Boto3Paginator):
    """
    Paginator for `list_entity_recognizers`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Filter: ListEntityRecognizersPaginateFilterTypeDef = None,
        PaginationConfig: ListEntityRecognizersPaginatePaginationConfigTypeDef = None,
    ) -> ListEntityRecognizersPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`Comprehend.Client.list_entity_recognizers`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/comprehend-2017-11-27/ListEntityRecognizers>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              Filter={
                  'Status':
                  'SUBMITTED'|'TRAINING'|'DELETING'|'STOP_REQUESTED'|'STOPPED'|'IN_ERROR'
                  |'TRAINED',
                  'SubmitTimeBefore': datetime(2015, 1, 1),
                  'SubmitTimeAfter': datetime(2015, 1, 1)
              },
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
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

        :type PaginationConfig: dict
        :param PaginationConfig:

          A dictionary that provides parameters to control pagination.

          - **MaxItems** *(integer) --*

            The total number of items to return. If the total number of items available is more than
            the value specified in max-items then a ``NextToken`` will be provided in the output
            that you can use to resume pagination.

          - **PageSize** *(integer) --*

            The size of each page.

          - **StartingToken** *(string) --*

            A token to specify where to start paginating. This is the ``NextToken`` from a previous
            response.

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
        """


class ListKeyPhrasesDetectionJobsPaginator(Boto3Paginator):
    """
    Paginator for `list_key_phrases_detection_jobs`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Filter: ListKeyPhrasesDetectionJobsPaginateFilterTypeDef = None,
        PaginationConfig: ListKeyPhrasesDetectionJobsPaginatePaginationConfigTypeDef = None,
    ) -> ListKeyPhrasesDetectionJobsPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`Comprehend.Client.list_key_phrases_detection_jobs`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/comprehend-2017-11-27/ListKeyPhrasesDetectionJobs>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              Filter={
                  'JobName': 'string',
                  'JobStatus':
                  'SUBMITTED'|'IN_PROGRESS'|'COMPLETED'|'FAILED'|'STOP_REQUESTED'
                  |'STOPPED',
                  'SubmitTimeBefore': datetime(2015, 1, 1),
                  'SubmitTimeAfter': datetime(2015, 1, 1)
              },
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
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

        :type PaginationConfig: dict
        :param PaginationConfig:

          A dictionary that provides parameters to control pagination.

          - **MaxItems** *(integer) --*

            The total number of items to return. If the total number of items available is more than
            the value specified in max-items then a ``NextToken`` will be provided in the output
            that you can use to resume pagination.

          - **PageSize** *(integer) --*

            The size of each page.

          - **StartingToken** *(string) --*

            A token to specify where to start paginating. This is the ``NextToken`` from a previous
            response.

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
        """


class ListSentimentDetectionJobsPaginator(Boto3Paginator):
    """
    Paginator for `list_sentiment_detection_jobs`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Filter: ListSentimentDetectionJobsPaginateFilterTypeDef = None,
        PaginationConfig: ListSentimentDetectionJobsPaginatePaginationConfigTypeDef = None,
    ) -> ListSentimentDetectionJobsPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`Comprehend.Client.list_sentiment_detection_jobs`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/comprehend-2017-11-27/ListSentimentDetectionJobs>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              Filter={
                  'JobName': 'string',
                  'JobStatus':
                  'SUBMITTED'|'IN_PROGRESS'|'COMPLETED'|'FAILED'|'STOP_REQUESTED'
                  |'STOPPED',
                  'SubmitTimeBefore': datetime(2015, 1, 1),
                  'SubmitTimeAfter': datetime(2015, 1, 1)
              },
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
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

        :type PaginationConfig: dict
        :param PaginationConfig:

          A dictionary that provides parameters to control pagination.

          - **MaxItems** *(integer) --*

            The total number of items to return. If the total number of items available is more than
            the value specified in max-items then a ``NextToken`` will be provided in the output
            that you can use to resume pagination.

          - **PageSize** *(integer) --*

            The size of each page.

          - **StartingToken** *(string) --*

            A token to specify where to start paginating. This is the ``NextToken`` from a previous
            response.

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
        """


class ListTopicsDetectionJobsPaginator(Boto3Paginator):
    """
    Paginator for `list_topics_detection_jobs`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Filter: ListTopicsDetectionJobsPaginateFilterTypeDef = None,
        PaginationConfig: ListTopicsDetectionJobsPaginatePaginationConfigTypeDef = None,
    ) -> ListTopicsDetectionJobsPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`Comprehend.Client.list_topics_detection_jobs`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/comprehend-2017-11-27/ListTopicsDetectionJobs>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              Filter={
                  'JobName': 'string',
                  'JobStatus':
                  'SUBMITTED'|'IN_PROGRESS'|'COMPLETED'|'FAILED'|'STOP_REQUESTED'
                  |'STOPPED',
                  'SubmitTimeBefore': datetime(2015, 1, 1),
                  'SubmitTimeAfter': datetime(2015, 1, 1)
              },
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
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

        :type PaginationConfig: dict
        :param PaginationConfig:

          A dictionary that provides parameters to control pagination.

          - **MaxItems** *(integer) --*

            The total number of items to return. If the total number of items available is more than
            the value specified in max-items then a ``NextToken`` will be provided in the output
            that you can use to resume pagination.

          - **PageSize** *(integer) --*

            The size of each page.

          - **StartingToken** *(string) --*

            A token to specify where to start paginating. This is the ``NextToken`` from a previous
            response.

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
        """
