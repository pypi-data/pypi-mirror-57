"Main interface for mgh service Paginators"
from __future__ import annotations

from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_mgh.type_defs import (
    ListCreatedArtifactsPaginatePaginationConfigTypeDef,
    ListCreatedArtifactsPaginateResponseTypeDef,
    ListDiscoveredResourcesPaginatePaginationConfigTypeDef,
    ListDiscoveredResourcesPaginateResponseTypeDef,
    ListMigrationTasksPaginatePaginationConfigTypeDef,
    ListMigrationTasksPaginateResponseTypeDef,
    ListProgressUpdateStreamsPaginatePaginationConfigTypeDef,
    ListProgressUpdateStreamsPaginateResponseTypeDef,
)


__all__ = (
    "ListCreatedArtifactsPaginator",
    "ListDiscoveredResourcesPaginator",
    "ListMigrationTasksPaginator",
    "ListProgressUpdateStreamsPaginator",
)


class ListCreatedArtifactsPaginator(Boto3Paginator):
    """
    Paginator for `list_created_artifacts`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ProgressUpdateStream: str,
        MigrationTaskName: str,
        PaginationConfig: ListCreatedArtifactsPaginatePaginationConfigTypeDef = None,
    ) -> ListCreatedArtifactsPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`MigrationHub.Client.list_created_artifacts`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/AWSMigrationHub-2017-05-31/ListCreatedArtifacts>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              ProgressUpdateStream='string',
              MigrationTaskName='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type ProgressUpdateStream: string
        :param ProgressUpdateStream: **[REQUIRED]**

          The name of the ProgressUpdateStream.

        :type MigrationTaskName: string
        :param MigrationTaskName: **[REQUIRED]**

          Unique identifier that references the migration task. *Do not store personal data in this
          field.*

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
                'CreatedArtifactList': [
                    {
                        'Name': 'string',
                        'Description': 'string'
                    },
                ]
            }
          **Response Structure**

          - *(dict) --*

            - **CreatedArtifactList** *(list) --*

              List of created artifacts up to the maximum number of results specified in the
              request.

              - *(dict) --*

                An ARN of the AWS cloud resource target receiving the migration (e.g., AMI, EC2
                instance, RDS instance, etc.).

                - **Name** *(string) --*

                  An ARN that uniquely identifies the result of a migration task.

                - **Description** *(string) --*

                  A description that can be free-form text to record additional detail about the
                  artifact for clarity or for later reference.
        """


class ListDiscoveredResourcesPaginator(Boto3Paginator):
    """
    Paginator for `list_discovered_resources`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ProgressUpdateStream: str,
        MigrationTaskName: str,
        PaginationConfig: ListDiscoveredResourcesPaginatePaginationConfigTypeDef = None,
    ) -> ListDiscoveredResourcesPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`MigrationHub.Client.list_discovered_resources`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/AWSMigrationHub-2017-05-31/ListDiscoveredResources>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              ProgressUpdateStream='string',
              MigrationTaskName='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type ProgressUpdateStream: string
        :param ProgressUpdateStream: **[REQUIRED]**

          The name of the ProgressUpdateStream.

        :type MigrationTaskName: string
        :param MigrationTaskName: **[REQUIRED]**

          The name of the MigrationTask. *Do not store personal data in this field.*

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
                'DiscoveredResourceList': [
                    {
                        'ConfigurationId': 'string',
                        'Description': 'string'
                    },
                ]
            }
          **Response Structure**

          - *(dict) --*

            - **DiscoveredResourceList** *(list) --*

              Returned list of discovered resources associated with the given MigrationTask.

              - *(dict) --*

                Object representing the on-premises resource being migrated.

                - **ConfigurationId** *(string) --*

                  The configurationId in Application Discovery Service that uniquely identifies the
                  on-premise resource.

                - **Description** *(string) --*

                  A description that can be free-form text to record additional detail about the
                  discovered resource for clarity or later reference.
        """


class ListMigrationTasksPaginator(Boto3Paginator):
    """
    Paginator for `list_migration_tasks`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ResourceName: str = None,
        PaginationConfig: ListMigrationTasksPaginatePaginationConfigTypeDef = None,
    ) -> ListMigrationTasksPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`MigrationHub.Client.list_migration_tasks`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/AWSMigrationHub-2017-05-31/ListMigrationTasks>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              ResourceName='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type ResourceName: string
        :param ResourceName:

          Filter migration tasks by discovered resource name.

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
                'MigrationTaskSummaryList': [
                    {
                        'ProgressUpdateStream': 'string',
                        'MigrationTaskName': 'string',
                        'Status': 'NOT_STARTED'|'IN_PROGRESS'|'FAILED'|'COMPLETED',
                        'ProgressPercent': 123,
                        'StatusDetail': 'string',
                        'UpdateDateTime': datetime(2015, 1, 1)
                    },
                ]
            }
          **Response Structure**

          - *(dict) --*

            - **MigrationTaskSummaryList** *(list) --*

              Lists the migration task's summary which includes: ``MigrationTaskName`` ,
              ``ProgressPercent`` , ``ProgressUpdateStream`` , ``Status`` , and the
              ``UpdateDateTime`` for each task.

              - *(dict) --*

                MigrationTaskSummary includes ``MigrationTaskName`` , ``ProgressPercent`` ,
                ``ProgressUpdateStream`` , ``Status`` , and ``UpdateDateTime`` for each task.

                - **ProgressUpdateStream** *(string) --*

                  An AWS resource used for access control. It should uniquely identify the migration
                  tool as it is used for all updates made by the tool.

                - **MigrationTaskName** *(string) --*

                  Unique identifier that references the migration task. *Do not store personal data
                  in this field.*

                - **Status** *(string) --*

                  Status of the task.

                - **ProgressPercent** *(integer) --*

                  Indication of the percentage completion of the task.

                - **StatusDetail** *(string) --*

                  Detail information of what is being done within the overall status state.

                - **UpdateDateTime** *(datetime) --*

                  The timestamp when the task was gathered.
        """


class ListProgressUpdateStreamsPaginator(Boto3Paginator):
    """
    Paginator for `list_progress_update_streams`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: ListProgressUpdateStreamsPaginatePaginationConfigTypeDef = None
    ) -> ListProgressUpdateStreamsPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`MigrationHub.Client.list_progress_update_streams`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/AWSMigrationHub-2017-05-31/ListProgressUpdateStreams>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
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
                'ProgressUpdateStreamSummaryList': [
                    {
                        'ProgressUpdateStreamName': 'string'
                    },
                ],

            }
          **Response Structure**

          - *(dict) --*

            - **ProgressUpdateStreamSummaryList** *(list) --*

              List of progress update streams up to the max number of results passed in the input.

              - *(dict) --*

                Summary of the AWS resource used for access control that is implicitly linked to
                your AWS account.

                - **ProgressUpdateStreamName** *(string) --*

                  The name of the ProgressUpdateStream. *Do not store personal data in this field.*
        """
