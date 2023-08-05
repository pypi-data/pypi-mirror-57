"Main interface for cur service Client"
from __future__ import annotations

from typing import Any, Dict
from botocore.client import BaseClient
from botocore.exceptions import ClientError as Boto3ClientError
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3.type_defs import Literal, overload

# pylint: disable=import-self
import mypy_boto3_cur.client as client_scope

# pylint: disable=import-self
import mypy_boto3_cur.paginator as paginator_scope
from mypy_boto3_cur.type_defs import (
    ClientDeleteReportDefinitionResponseTypeDef,
    ClientDescribeReportDefinitionsResponseTypeDef,
    ClientModifyReportDefinitionReportDefinitionTypeDef,
    ClientPutReportDefinitionReportDefinitionTypeDef,
)


__all__ = ("Client",)


class Client(BaseClient):
    exceptions: client_scope.Exceptions

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
    def delete_report_definition(
        self, ReportName: str = None
    ) -> ClientDeleteReportDefinitionResponseTypeDef:
        """
        Deletes the specified report.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/cur-2017-01-06/DeleteReportDefinition>`_

        **Request Syntax**
        ::

          response = client.delete_report_definition(
              ReportName='string'
          )
        :type ReportName: string
        :param ReportName:

          The name of the report that you want to create. The name must be unique, is case
          sensitive, and can't include spaces.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'ResponseMessage': 'string'
            }
          **Response Structure**

          - *(dict) --*

            If the action is successful, the service sends back an HTTP 200 response.

            - **ResponseMessage** *(string) --*

              Whether the deletion was successful or not.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_report_definitions(
        self, MaxResults: int = None, NextToken: str = None
    ) -> ClientDescribeReportDefinitionsResponseTypeDef:
        """
        Lists the AWS Cost and Usage reports available to this account.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/cur-2017-01-06/DescribeReportDefinitions>`_

        **Request Syntax**
        ::

          response = client.describe_report_definitions(
              MaxResults=123,
              NextToken='string'
          )
        :type MaxResults: integer
        :param MaxResults:

          The maximum number of results that AWS returns for the operation.

        :type NextToken: string
        :param NextToken:

          A generic string.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'ReportDefinitions': [
                    {
                        'ReportName': 'string',
                        'TimeUnit': 'HOURLY'|'DAILY',
                        'Format': 'textORcsv'|'Parquet',
                        'Compression': 'ZIP'|'GZIP'|'Parquet',
                        'AdditionalSchemaElements': [
                            'RESOURCES',
                        ],
                        'S3Bucket': 'string',
                        'S3Prefix': 'string',
                        'S3Region':
                        'us-east-1'|'us-west-1'|'us-west-2'|'eu-central-1'
                        |'eu-west-1'|'ap-southeast-1'|'ap-southeast-2'
                        |'ap-northeast-1'|'eu-north-1'|'ap-northeast-3'|'ap-east-1',
                        'AdditionalArtifacts': [
                            'REDSHIFT'|'QUICKSIGHT'|'ATHENA',
                        ],
                        'RefreshClosedReports': True|False,
                        'ReportVersioning': 'CREATE_NEW_REPORT'|'OVERWRITE_REPORT'
                    },
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            If the action is successful, the service sends back an HTTP 200 response.

            - **ReportDefinitions** *(list) --*

              A list of AWS Cost and Usage reports owned by the account.

              - *(dict) --*

                The definition of AWS Cost and Usage Report. You can specify the report name, time
                unit, report format, compression format, S3 bucket, additional artifacts, and schema
                elements in the definition.

                - **ReportName** *(string) --*

                  The name of the report that you want to create. The name must be unique, is case
                  sensitive, and can't include spaces.

                - **TimeUnit** *(string) --*

                  The length of time covered by the report.

                - **Format** *(string) --*

                  The format that AWS saves the report in.

                - **Compression** *(string) --*

                  The compression format that AWS uses for the report.

                - **AdditionalSchemaElements** *(list) --*

                  A list of strings that indicate additional content that Amazon Web Services
                  includes in the report, such as individual resource IDs.

                  - *(string) --*

                    Whether or not AWS includes resource IDs in the report.

                - **S3Bucket** *(string) --*

                  The S3 bucket where AWS delivers the report.

                - **S3Prefix** *(string) --*

                  The prefix that AWS adds to the report name when AWS delivers the report. Your
                  prefix can't include spaces.

                - **S3Region** *(string) --*

                  The region of the S3 bucket that AWS delivers the report into.

                - **AdditionalArtifacts** *(list) --*

                  A list of manifests that you want Amazon Web Services to create for this report.

                  - *(string) --*

                    The types of manifest that you want AWS to create for this report.

                - **RefreshClosedReports** *(boolean) --*

                  Whether you want Amazon Web Services to update your reports after they have been
                  finalized if Amazon Web Services detects charges related to previous months. These
                  charges can include refunds, credits, or support fees.

                - **ReportVersioning** *(string) --*

                  Whether you want Amazon Web Services to overwrite the previous version of each
                  report or to deliver the report in addition to the previous versions.

            - **NextToken** *(string) --*

              A generic string.
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
    def modify_report_definition(
        self, ReportName: str, ReportDefinition: ClientModifyReportDefinitionReportDefinitionTypeDef
    ) -> Dict[str, Any]:
        """
        Allows you to programatically update your report preferences.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/cur-2017-01-06/ModifyReportDefinition>`_

        **Request Syntax**
        ::

          response = client.modify_report_definition(
              ReportName='string',
              ReportDefinition={
                  'ReportName': 'string',
                  'TimeUnit': 'HOURLY'|'DAILY',
                  'Format': 'textORcsv'|'Parquet',
                  'Compression': 'ZIP'|'GZIP'|'Parquet',
                  'AdditionalSchemaElements': [
                      'RESOURCES',
                  ],
                  'S3Bucket': 'string',
                  'S3Prefix': 'string',
                  'S3Region':
                  'us-east-1'|'us-west-1'|'us-west-2'|'eu-central-1'|'eu-west-1'
                  |'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'eu-north-1'
                  |'ap-northeast-3'|'ap-east-1',
                  'AdditionalArtifacts': [
                      'REDSHIFT'|'QUICKSIGHT'|'ATHENA',
                  ],
                  'RefreshClosedReports': True|False,
                  'ReportVersioning': 'CREATE_NEW_REPORT'|'OVERWRITE_REPORT'
              }
          )
        :type ReportName: string
        :param ReportName: **[REQUIRED]**

          The name of the report that you want to create. The name must be unique, is case
          sensitive, and can't include spaces.

        :type ReportDefinition: dict
        :param ReportDefinition: **[REQUIRED]**

          The definition of AWS Cost and Usage Report. You can specify the report name, time unit,
          report format, compression format, S3 bucket, additional artifacts, and schema elements in
          the definition.

          - **ReportName** *(string) --* **[REQUIRED]**

            The name of the report that you want to create. The name must be unique, is case
            sensitive, and can't include spaces.

          - **TimeUnit** *(string) --* **[REQUIRED]**

            The length of time covered by the report.

          - **Format** *(string) --* **[REQUIRED]**

            The format that AWS saves the report in.

          - **Compression** *(string) --* **[REQUIRED]**

            The compression format that AWS uses for the report.

          - **AdditionalSchemaElements** *(list) --* **[REQUIRED]**

            A list of strings that indicate additional content that Amazon Web Services includes in
            the report, such as individual resource IDs.

            - *(string) --*

              Whether or not AWS includes resource IDs in the report.

          - **S3Bucket** *(string) --* **[REQUIRED]**

            The S3 bucket where AWS delivers the report.

          - **S3Prefix** *(string) --* **[REQUIRED]**

            The prefix that AWS adds to the report name when AWS delivers the report. Your prefix
            can't include spaces.

          - **S3Region** *(string) --* **[REQUIRED]**

            The region of the S3 bucket that AWS delivers the report into.

          - **AdditionalArtifacts** *(list) --*

            A list of manifests that you want Amazon Web Services to create for this report.

            - *(string) --*

              The types of manifest that you want AWS to create for this report.

          - **RefreshClosedReports** *(boolean) --*

            Whether you want Amazon Web Services to update your reports after they have been
            finalized if Amazon Web Services detects charges related to previous months. These
            charges can include refunds, credits, or support fees.

          - **ReportVersioning** *(string) --*

            Whether you want Amazon Web Services to overwrite the previous version of each report or
            to deliver the report in addition to the previous versions.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {}
          **Response Structure**

          - *(dict) --*
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def put_report_definition(
        self, ReportDefinition: ClientPutReportDefinitionReportDefinitionTypeDef
    ) -> Dict[str, Any]:
        """
        Creates a new report using the description that you provide.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/cur-2017-01-06/PutReportDefinition>`_

        **Request Syntax**
        ::

          response = client.put_report_definition(
              ReportDefinition={
                  'ReportName': 'string',
                  'TimeUnit': 'HOURLY'|'DAILY',
                  'Format': 'textORcsv'|'Parquet',
                  'Compression': 'ZIP'|'GZIP'|'Parquet',
                  'AdditionalSchemaElements': [
                      'RESOURCES',
                  ],
                  'S3Bucket': 'string',
                  'S3Prefix': 'string',
                  'S3Region':
                  'us-east-1'|'us-west-1'|'us-west-2'|'eu-central-1'|'eu-west-1'
                  |'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'eu-north-1'
                  |'ap-northeast-3'|'ap-east-1',
                  'AdditionalArtifacts': [
                      'REDSHIFT'|'QUICKSIGHT'|'ATHENA',
                  ],
                  'RefreshClosedReports': True|False,
                  'ReportVersioning': 'CREATE_NEW_REPORT'|'OVERWRITE_REPORT'
              }
          )
        :type ReportDefinition: dict
        :param ReportDefinition: **[REQUIRED]**

          Represents the output of the PutReportDefinition operation. The content consists of the
          detailed metadata and data file information.

          - **ReportName** *(string) --* **[REQUIRED]**

            The name of the report that you want to create. The name must be unique, is case
            sensitive, and can't include spaces.

          - **TimeUnit** *(string) --* **[REQUIRED]**

            The length of time covered by the report.

          - **Format** *(string) --* **[REQUIRED]**

            The format that AWS saves the report in.

          - **Compression** *(string) --* **[REQUIRED]**

            The compression format that AWS uses for the report.

          - **AdditionalSchemaElements** *(list) --* **[REQUIRED]**

            A list of strings that indicate additional content that Amazon Web Services includes in
            the report, such as individual resource IDs.

            - *(string) --*

              Whether or not AWS includes resource IDs in the report.

          - **S3Bucket** *(string) --* **[REQUIRED]**

            The S3 bucket where AWS delivers the report.

          - **S3Prefix** *(string) --* **[REQUIRED]**

            The prefix that AWS adds to the report name when AWS delivers the report. Your prefix
            can't include spaces.

          - **S3Region** *(string) --* **[REQUIRED]**

            The region of the S3 bucket that AWS delivers the report into.

          - **AdditionalArtifacts** *(list) --*

            A list of manifests that you want Amazon Web Services to create for this report.

            - *(string) --*

              The types of manifest that you want AWS to create for this report.

          - **RefreshClosedReports** *(boolean) --*

            Whether you want Amazon Web Services to update your reports after they have been
            finalized if Amazon Web Services detects charges related to previous months. These
            charges can include refunds, credits, or support fees.

          - **ReportVersioning** *(string) --*

            Whether you want Amazon Web Services to overwrite the previous version of each report or
            to deliver the report in addition to the previous versions.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {}
          **Response Structure**

          - *(dict) --*

            If the action is successful, the service sends back an HTTP 200 response with an empty
            HTTP body.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_report_definitions"]
    ) -> paginator_scope.DescribeReportDefinitionsPaginator:
        """
        Get Paginator for `describe_report_definitions` operation.
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
    ClientError: Boto3ClientError
    DuplicateReportNameException: Boto3ClientError
    InternalErrorException: Boto3ClientError
    ReportLimitReachedException: Boto3ClientError
    ValidationException: Boto3ClientError
