"Main interface for codecommit service Paginators"
from __future__ import annotations

from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3.type_defs import Literal
from mypy_boto3_codecommit.type_defs import (
    DescribePullRequestEventsPaginatePaginationConfigTypeDef,
    DescribePullRequestEventsPaginateResponseTypeDef,
    GetCommentsForComparedCommitPaginatePaginationConfigTypeDef,
    GetCommentsForComparedCommitPaginateResponseTypeDef,
    GetCommentsForPullRequestPaginatePaginationConfigTypeDef,
    GetCommentsForPullRequestPaginateResponseTypeDef,
    GetDifferencesPaginatePaginationConfigTypeDef,
    GetDifferencesPaginateResponseTypeDef,
    ListBranchesPaginatePaginationConfigTypeDef,
    ListBranchesPaginateResponseTypeDef,
    ListPullRequestsPaginatePaginationConfigTypeDef,
    ListPullRequestsPaginateResponseTypeDef,
    ListRepositoriesPaginatePaginationConfigTypeDef,
    ListRepositoriesPaginateResponseTypeDef,
)


__all__ = (
    "DescribePullRequestEventsPaginator",
    "GetCommentsForComparedCommitPaginator",
    "GetCommentsForPullRequestPaginator",
    "GetDifferencesPaginator",
    "ListBranchesPaginator",
    "ListPullRequestsPaginator",
    "ListRepositoriesPaginator",
)


class DescribePullRequestEventsPaginator(Boto3Paginator):
    """
    Paginator for `describe_pull_request_events`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        pullRequestId: str,
        pullRequestEventType: Literal[
            "PULL_REQUEST_CREATED",
            "PULL_REQUEST_STATUS_CHANGED",
            "PULL_REQUEST_SOURCE_REFERENCE_UPDATED",
            "PULL_REQUEST_MERGE_STATE_CHANGED",
            "PULL_REQUEST_APPROVAL_RULE_CREATED",
            "PULL_REQUEST_APPROVAL_RULE_UPDATED",
            "PULL_REQUEST_APPROVAL_RULE_DELETED",
            "PULL_REQUEST_APPROVAL_RULE_OVERRIDDEN",
            "PULL_REQUEST_APPROVAL_STATE_CHANGED",
        ] = None,
        actorArn: str = None,
        PaginationConfig: DescribePullRequestEventsPaginatePaginationConfigTypeDef = None,
    ) -> DescribePullRequestEventsPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`CodeCommit.Client.describe_pull_request_events`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/codecommit-2015-04-13/DescribePullRequestEvents>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              pullRequestId='string',
              pullRequestEventType=
                  'PULL_REQUEST_CREATED'|'PULL_REQUEST_STATUS_CHANGED'
                  |'PULL_REQUEST_SOURCE_REFERENCE_UPDATED'|'PULL_REQUEST_MERGE_STATE_CHANGED'
                  |'PULL_REQUEST_APPROVAL_RULE_CREATED'|'PULL_REQUEST_APPROVAL_RULE_UPDATED'
                  |'PULL_REQUEST_APPROVAL_RULE_DELETED'|'PULL_REQUEST_APPROVAL_RULE_OVERRIDDEN'
                  |'PULL_REQUEST_APPROVAL_STATE_CHANGED',
              actorArn='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type pullRequestId: string
        :param pullRequestId: **[REQUIRED]**

          The system-generated ID of the pull request. To get this ID, use  ListPullRequests .

        :type pullRequestEventType: string
        :param pullRequestEventType:

          Optional. The pull request event type about which you want to return information.

        :type actorArn: string
        :param actorArn:

          The Amazon Resource Name (ARN) of the user whose actions resulted in the event. Examples
          include updating the pull request with more commits or changing the status of a pull
          request.

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
                'pullRequestEvents': [
                    {
                        'pullRequestId': 'string',
                        'eventDate': datetime(2015, 1, 1),
                        'pullRequestEventType':
                        'PULL_REQUEST_CREATED'|'PULL_REQUEST_STATUS_CHANGED'
                        |'PULL_REQUEST_SOURCE_REFERENCE_UPDATED'
                        |'PULL_REQUEST_MERGE_STATE_CHANGED'
                        |'PULL_REQUEST_APPROVAL_RULE_CREATED'
                        |'PULL_REQUEST_APPROVAL_RULE_UPDATED'
                        |'PULL_REQUEST_APPROVAL_RULE_DELETED'
                        |'PULL_REQUEST_APPROVAL_RULE_OVERRIDDEN'
                        |'PULL_REQUEST_APPROVAL_STATE_CHANGED',
                        'actorArn': 'string',
                        'pullRequestCreatedEventMetadata': {
                            'repositoryName': 'string',
                            'sourceCommitId': 'string',
                            'destinationCommitId': 'string',
                            'mergeBase': 'string'
                        },
                        'pullRequestStatusChangedEventMetadata': {
                            'pullRequestStatus': 'OPEN'|'CLOSED'
                        },
                        'pullRequestSourceReferenceUpdatedEventMetadata': {
                            'repositoryName': 'string',
                            'beforeCommitId': 'string',
                            'afterCommitId': 'string',
                            'mergeBase': 'string'
                        },
                        'pullRequestMergedStateChangedEventMetadata': {
                            'repositoryName': 'string',
                            'destinationReference': 'string',
                            'mergeMetadata': {
                                'isMerged': True|False,
                                'mergedBy': 'string',
                                'mergeCommitId': 'string',
                                'mergeOption': 'FAST_FORWARD_MERGE'|'SQUASH_MERGE'|'THREE_WAY_MERGE'
                            }
                        },
                        'approvalRuleEventMetadata': {
                            'approvalRuleName': 'string',
                            'approvalRuleId': 'string',
                            'approvalRuleContent': 'string'
                        },
                        'approvalStateChangedEventMetadata': {
                            'revisionId': 'string',
                            'approvalStatus': 'APPROVE'|'REVOKE'
                        },
                        'approvalRuleOverriddenEventMetadata': {
                            'revisionId': 'string',
                            'overrideStatus': 'OVERRIDE'|'REVOKE'
                        }
                    },
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **pullRequestEvents** *(list) --*

              Information about the pull request events.

              - *(dict) --*

                Returns information about a pull request event.

                - **pullRequestId** *(string) --*

                  The system-generated ID of the pull request.

                - **eventDate** *(datetime) --*

                  The day and time of the pull request event, in timestamp format.

                - **pullRequestEventType** *(string) --*

                  The type of the pull request event (for example, a status change event
                  (PULL_REQUEST_STATUS_CHANGED) or update event
                  (PULL_REQUEST_SOURCE_REFERENCE_UPDATED)).

                - **actorArn** *(string) --*

                  The Amazon Resource Name (ARN) of the user whose actions resulted in the event.
                  Examples include updating the pull request with more commits or changing the
                  status of a pull request.

                - **pullRequestCreatedEventMetadata** *(dict) --*

                  Information about the source and destination branches for the pull request.

                  - **repositoryName** *(string) --*

                    The name of the repository where the pull request was created.

                  - **sourceCommitId** *(string) --*

                    The commit ID on the source branch used when the pull request was created.

                  - **destinationCommitId** *(string) --*

                    The commit ID of the tip of the branch specified as the destination branch when
                    the pull request was created.

                  - **mergeBase** *(string) --*

                    The commit ID of the most recent commit that the source branch and the
                    destination branch have in common.

                - **pullRequestStatusChangedEventMetadata** *(dict) --*

                  Information about the change in status for the pull request event.

                  - **pullRequestStatus** *(string) --*

                    The changed status of the pull request.

                - **pullRequestSourceReferenceUpdatedEventMetadata** *(dict) --*

                  Information about the updated source branch for the pull request event.

                  - **repositoryName** *(string) --*

                    The name of the repository where the pull request was updated.

                  - **beforeCommitId** *(string) --*

                    The full commit ID of the commit in the destination branch that was the tip of
                    the branch at the time the pull request was updated.

                  - **afterCommitId** *(string) --*

                    The full commit ID of the commit in the source branch that was the tip of the
                    branch at the time the pull request was updated.

                  - **mergeBase** *(string) --*

                    The commit ID of the most recent commit that the source branch and the
                    destination branch have in common.

                - **pullRequestMergedStateChangedEventMetadata** *(dict) --*

                  Information about the change in mergability state for the pull request event.

                  - **repositoryName** *(string) --*

                    The name of the repository where the pull request was created.

                  - **destinationReference** *(string) --*

                    The name of the branch that the pull request is merged into.

                  - **mergeMetadata** *(dict) --*

                    Information about the merge state change event.

                    - **isMerged** *(boolean) --*

                      A Boolean value indicating whether the merge has been made.

                    - **mergedBy** *(string) --*

                      The Amazon Resource Name (ARN) of the user who merged the branches.

                    - **mergeCommitId** *(string) --*

                      The commit ID for the merge commit, if any.

                    - **mergeOption** *(string) --*

                      The merge strategy used in the merge.

                - **approvalRuleEventMetadata** *(dict) --*

                  Information about a pull request event.

                  - **approvalRuleName** *(string) --*

                    The name of the approval rule.

                  - **approvalRuleId** *(string) --*

                    The system-generated ID of the approval rule.

                  - **approvalRuleContent** *(string) --*

                    The content of the approval rule.

                - **approvalStateChangedEventMetadata** *(dict) --*

                  Information about an approval state change for a pull request.

                  - **revisionId** *(string) --*

                    The revision ID of the pull request when the approval state changed.

                  - **approvalStatus** *(string) --*

                    The approval status for the pull request.

                - **approvalRuleOverriddenEventMetadata** *(dict) --*

                  Information about an approval rule override event for a pull request.

                  - **revisionId** *(string) --*

                    The revision ID of the pull request when the override event occurred.

                  - **overrideStatus** *(string) --*

                    The status of the override event.

            - **NextToken** *(string) --*

              A token to resume pagination.
        """


class GetCommentsForComparedCommitPaginator(Boto3Paginator):
    """
    Paginator for `get_comments_for_compared_commit`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        repositoryName: str,
        afterCommitId: str,
        beforeCommitId: str = None,
        PaginationConfig: GetCommentsForComparedCommitPaginatePaginationConfigTypeDef = None,
    ) -> GetCommentsForComparedCommitPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`CodeCommit.Client.get_comments_for_compared_commit`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/codecommit-2015-04-13/GetCommentsForComparedCommit>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              repositoryName='string',
              beforeCommitId='string',
              afterCommitId='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type repositoryName: string
        :param repositoryName: **[REQUIRED]**

          The name of the repository where you want to compare commits.

        :type beforeCommitId: string
        :param beforeCommitId:

          To establish the directionality of the comparison, the full commit ID of the before
          commit.

        :type afterCommitId: string
        :param afterCommitId: **[REQUIRED]**

          To establish the directionality of the comparison, the full commit ID of the after commit.

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
                'commentsForComparedCommitData': [
                    {
                        'repositoryName': 'string',
                        'beforeCommitId': 'string',
                        'afterCommitId': 'string',
                        'beforeBlobId': 'string',
                        'afterBlobId': 'string',
                        'location': {
                            'filePath': 'string',
                            'filePosition': 123,
                            'relativeFileVersion': 'BEFORE'|'AFTER'
                        },
                        'comments': [
                            {
                                'commentId': 'string',
                                'content': 'string',
                                'inReplyTo': 'string',
                                'creationDate': datetime(2015, 1, 1),
                                'lastModifiedDate': datetime(2015, 1, 1),
                                'authorArn': 'string',
                                'deleted': True|False,
                                'clientRequestToken': 'string'
                            },
                        ]
                    },
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **commentsForComparedCommitData** *(list) --*

              A list of comment objects on the compared commit.

              - *(dict) --*

                Returns information about comments on the comparison between two commits.

                - **repositoryName** *(string) --*

                  The name of the repository that contains the compared commits.

                - **beforeCommitId** *(string) --*

                  The full commit ID of the commit used to establish the before of the comparison.

                - **afterCommitId** *(string) --*

                  The full commit ID of the commit used to establish the after of the comparison.

                - **beforeBlobId** *(string) --*

                  The full blob ID of the commit used to establish the before of the comparison.

                - **afterBlobId** *(string) --*

                  The full blob ID of the commit used to establish the after of the comparison.

                - **location** *(dict) --*

                  Location information about the comment on the comparison, including the file name,
                  line number, and whether the version of the file where the comment was made is
                  BEFORE or AFTER.

                  - **filePath** *(string) --*

                    The name of the file being compared, including its extension and subdirectory,
                    if any.

                  - **filePosition** *(integer) --*

                    The position of a change in a compared file, in line number format.

                  - **relativeFileVersion** *(string) --*

                    In a comparison of commits or a pull request, whether the change is in the
                    before or after of that comparison.

                - **comments** *(list) --*

                  An array of comment objects. Each comment object contains information about a
                  comment on the comparison between commits.

                  - *(dict) --*

                    Returns information about a specific comment.

                    - **commentId** *(string) --*

                      The system-generated comment ID.

                    - **content** *(string) --*

                      The content of the comment.

                    - **inReplyTo** *(string) --*

                      The ID of the comment for which this comment is a reply, if any.

                    - **creationDate** *(datetime) --*

                      The date and time the comment was created, in timestamp format.

                    - **lastModifiedDate** *(datetime) --*

                      The date and time the comment was most recently modified, in timestamp format.

                    - **authorArn** *(string) --*

                      The Amazon Resource Name (ARN) of the person who posted the comment.

                    - **deleted** *(boolean) --*

                      A Boolean value indicating whether the comment has been deleted.

                    - **clientRequestToken** *(string) --*

                      A unique, client-generated idempotency token that, when provided in a request,
                      ensures the request cannot be repeated with a changed parameter. If a request
                      is received with the same parameters and a token is included, the request
                      returns information about the initial request that used that token.

            - **NextToken** *(string) --*

              A token to resume pagination.
        """


class GetCommentsForPullRequestPaginator(Boto3Paginator):
    """
    Paginator for `get_comments_for_pull_request`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        pullRequestId: str,
        repositoryName: str = None,
        beforeCommitId: str = None,
        afterCommitId: str = None,
        PaginationConfig: GetCommentsForPullRequestPaginatePaginationConfigTypeDef = None,
    ) -> GetCommentsForPullRequestPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`CodeCommit.Client.get_comments_for_pull_request`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/codecommit-2015-04-13/GetCommentsForPullRequest>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              pullRequestId='string',
              repositoryName='string',
              beforeCommitId='string',
              afterCommitId='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type pullRequestId: string
        :param pullRequestId: **[REQUIRED]**

          The system-generated ID of the pull request. To get this ID, use  ListPullRequests .

        :type repositoryName: string
        :param repositoryName:

          The name of the repository that contains the pull request.

        :type beforeCommitId: string
        :param beforeCommitId:

          The full commit ID of the commit in the destination branch that was the tip of the branch
          at the time the pull request was created.

        :type afterCommitId: string
        :param afterCommitId:

          The full commit ID of the commit in the source branch that was the tip of the branch at
          the time the comment was made.

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
                'commentsForPullRequestData': [
                    {
                        'pullRequestId': 'string',
                        'repositoryName': 'string',
                        'beforeCommitId': 'string',
                        'afterCommitId': 'string',
                        'beforeBlobId': 'string',
                        'afterBlobId': 'string',
                        'location': {
                            'filePath': 'string',
                            'filePosition': 123,
                            'relativeFileVersion': 'BEFORE'|'AFTER'
                        },
                        'comments': [
                            {
                                'commentId': 'string',
                                'content': 'string',
                                'inReplyTo': 'string',
                                'creationDate': datetime(2015, 1, 1),
                                'lastModifiedDate': datetime(2015, 1, 1),
                                'authorArn': 'string',
                                'deleted': True|False,
                                'clientRequestToken': 'string'
                            },
                        ]
                    },
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **commentsForPullRequestData** *(list) --*

              An array of comment objects on the pull request.

              - *(dict) --*

                Returns information about comments on a pull request.

                - **pullRequestId** *(string) --*

                  The system-generated ID of the pull request.

                - **repositoryName** *(string) --*

                  The name of the repository that contains the pull request.

                - **beforeCommitId** *(string) --*

                  The full commit ID of the commit that was the tip of the destination branch when
                  the pull request was created. This commit is superceded by the after commit in the
                  source branch when and if you merge the source branch into the destination branch.

                - **afterCommitId** *(string) --*

                  The full commit ID of the commit that was the tip of the source branch at the time
                  the comment was made.

                - **beforeBlobId** *(string) --*

                  The full blob ID of the file on which you want to comment on the destination
                  commit.

                - **afterBlobId** *(string) --*

                  The full blob ID of the file on which you want to comment on the source commit.

                - **location** *(dict) --*

                  Location information about the comment on the pull request, including the file
                  name, line number, and whether the version of the file where the comment was made
                  is BEFORE (destination branch) or AFTER (source branch).

                  - **filePath** *(string) --*

                    The name of the file being compared, including its extension and subdirectory,
                    if any.

                  - **filePosition** *(integer) --*

                    The position of a change in a compared file, in line number format.

                  - **relativeFileVersion** *(string) --*

                    In a comparison of commits or a pull request, whether the change is in the
                    before or after of that comparison.

                - **comments** *(list) --*

                  An array of comment objects. Each comment object contains information about a
                  comment on the pull request.

                  - *(dict) --*

                    Returns information about a specific comment.

                    - **commentId** *(string) --*

                      The system-generated comment ID.

                    - **content** *(string) --*

                      The content of the comment.

                    - **inReplyTo** *(string) --*

                      The ID of the comment for which this comment is a reply, if any.

                    - **creationDate** *(datetime) --*

                      The date and time the comment was created, in timestamp format.

                    - **lastModifiedDate** *(datetime) --*

                      The date and time the comment was most recently modified, in timestamp format.

                    - **authorArn** *(string) --*

                      The Amazon Resource Name (ARN) of the person who posted the comment.

                    - **deleted** *(boolean) --*

                      A Boolean value indicating whether the comment has been deleted.

                    - **clientRequestToken** *(string) --*

                      A unique, client-generated idempotency token that, when provided in a request,
                      ensures the request cannot be repeated with a changed parameter. If a request
                      is received with the same parameters and a token is included, the request
                      returns information about the initial request that used that token.

            - **NextToken** *(string) --*

              A token to resume pagination.
        """


class GetDifferencesPaginator(Boto3Paginator):
    """
    Paginator for `get_differences`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        repositoryName: str,
        afterCommitSpecifier: str,
        beforeCommitSpecifier: str = None,
        beforePath: str = None,
        afterPath: str = None,
        PaginationConfig: GetDifferencesPaginatePaginationConfigTypeDef = None,
    ) -> GetDifferencesPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`CodeCommit.Client.get_differences`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/codecommit-2015-04-13/GetDifferences>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              repositoryName='string',
              beforeCommitSpecifier='string',
              afterCommitSpecifier='string',
              beforePath='string',
              afterPath='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type repositoryName: string
        :param repositoryName: **[REQUIRED]**

          The name of the repository where you want to get differences.

        :type beforeCommitSpecifier: string
        :param beforeCommitSpecifier:

          The branch, tag, HEAD, or other fully qualified reference used to identify a commit (for
          example, the full commit ID). Optional. If not specified, all changes before the
          ``afterCommitSpecifier`` value are shown. If you do not use ``beforeCommitSpecifier`` in
          your request, consider limiting the results with ``maxResults`` .

        :type afterCommitSpecifier: string
        :param afterCommitSpecifier: **[REQUIRED]**

          The branch, tag, HEAD, or other fully qualified reference used to identify a commit.

        :type beforePath: string
        :param beforePath:

          The file path in which to check for differences. Limits the results to this path. Can also
          be used to specify the previous name of a directory or folder. If ``beforePath`` and
          ``afterPath`` are not specified, differences are shown for all paths.

        :type afterPath: string
        :param afterPath:

          The file path in which to check differences. Limits the results to this path. Can also be
          used to specify the changed name of a directory or folder, if it has changed. If not
          specified, differences are shown for all paths.

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
                'differences': [
                    {
                        'beforeBlob': {
                            'blobId': 'string',
                            'path': 'string',
                            'mode': 'string'
                        },
                        'afterBlob': {
                            'blobId': 'string',
                            'path': 'string',
                            'mode': 'string'
                        },
                        'changeType': 'A'|'M'|'D'
                    },
                ],

            }
          **Response Structure**

          - *(dict) --*

            - **differences** *(list) --*

              A data type object that contains information about the differences, including whether
              the difference is added, modified, or deleted (A, D, M).

              - *(dict) --*

                Returns information about a set of differences for a commit specifier.

                - **beforeBlob** *(dict) --*

                  Information about a ``beforeBlob`` data type object, including the ID, the file
                  mode permission code, and the path.

                  - **blobId** *(string) --*

                    The full ID of the blob.

                  - **path** *(string) --*

                    The path to the blob and associated file name, if any.

                  - **mode** *(string) --*

                    The file mode permissions of the blob. File mode permission codes include:

                    * ``100644`` indicates read/write

                    * ``100755`` indicates read/write/execute

                    * ``160000`` indicates a submodule

                    * ``120000`` indicates a symlink

                - **afterBlob** *(dict) --*

                  Information about an ``afterBlob`` data type object, including the ID, the file
                  mode permission code, and the path.

                  - **blobId** *(string) --*

                    The full ID of the blob.

                  - **path** *(string) --*

                    The path to the blob and associated file name, if any.

                  - **mode** *(string) --*

                    The file mode permissions of the blob. File mode permission codes include:

                    * ``100644`` indicates read/write

                    * ``100755`` indicates read/write/execute

                    * ``160000`` indicates a submodule

                    * ``120000`` indicates a symlink

                - **changeType** *(string) --*

                  Whether the change type of the difference is an addition (A), deletion (D), or
                  modification (M).
        """


class ListBranchesPaginator(Boto3Paginator):
    """
    Paginator for `list_branches`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        repositoryName: str,
        PaginationConfig: ListBranchesPaginatePaginationConfigTypeDef = None,
    ) -> ListBranchesPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`CodeCommit.Client.list_branches`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/codecommit-2015-04-13/ListBranches>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              repositoryName='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'StartingToken': 'string'
              }
          )
        :type repositoryName: string
        :param repositoryName: **[REQUIRED]**

          The name of the repository that contains the branches.

        :type PaginationConfig: dict
        :param PaginationConfig:

          A dictionary that provides parameters to control pagination.

          - **MaxItems** *(integer) --*

            The total number of items to return. If the total number of items available is more than
            the value specified in max-items then a ``NextToken`` will be provided in the output
            that you can use to resume pagination.

          - **StartingToken** *(string) --*

            A token to specify where to start paginating. This is the ``NextToken`` from a previous
            response.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'branches': [
                    'string',
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            Represents the output of a list branches operation.

            - **branches** *(list) --*

              The list of branch names.

              - *(string) --*

            - **NextToken** *(string) --*

              A token to resume pagination.
        """


class ListPullRequestsPaginator(Boto3Paginator):
    """
    Paginator for `list_pull_requests`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        repositoryName: str,
        authorArn: str = None,
        pullRequestStatus: Literal["OPEN", "CLOSED"] = None,
        PaginationConfig: ListPullRequestsPaginatePaginationConfigTypeDef = None,
    ) -> ListPullRequestsPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`CodeCommit.Client.list_pull_requests`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/codecommit-2015-04-13/ListPullRequests>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              repositoryName='string',
              authorArn='string',
              pullRequestStatus='OPEN'|'CLOSED',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type repositoryName: string
        :param repositoryName: **[REQUIRED]**

          The name of the repository for which you want to list pull requests.

        :type authorArn: string
        :param authorArn:

          Optional. The Amazon Resource Name (ARN) of the user who created the pull request. If
          used, this filters the results to pull requests created by that user.

        :type pullRequestStatus: string
        :param pullRequestStatus:

          Optional. The status of the pull request. If used, this refines the results to the pull
          requests that match the specified status.

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
                'pullRequestIds': [
                    'string',
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **pullRequestIds** *(list) --*

              The system-generated IDs of the pull requests.

              - *(string) --*

            - **NextToken** *(string) --*

              A token to resume pagination.
        """


class ListRepositoriesPaginator(Boto3Paginator):
    """
    Paginator for `list_repositories`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        sortBy: Literal["repositoryName", "lastModifiedDate"] = None,
        order: Literal["ascending", "descending"] = None,
        PaginationConfig: ListRepositoriesPaginatePaginationConfigTypeDef = None,
    ) -> ListRepositoriesPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`CodeCommit.Client.list_repositories`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/codecommit-2015-04-13/ListRepositories>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              sortBy='repositoryName'|'lastModifiedDate',
              order='ascending'|'descending',
              PaginationConfig={
                  'MaxItems': 123,
                  'StartingToken': 'string'
              }
          )
        :type sortBy: string
        :param sortBy:

          The criteria used to sort the results of a list repositories operation.

        :type order: string
        :param order:

          The order in which to sort the results of a list repositories operation.

        :type PaginationConfig: dict
        :param PaginationConfig:

          A dictionary that provides parameters to control pagination.

          - **MaxItems** *(integer) --*

            The total number of items to return. If the total number of items available is more than
            the value specified in max-items then a ``NextToken`` will be provided in the output
            that you can use to resume pagination.

          - **StartingToken** *(string) --*

            A token to specify where to start paginating. This is the ``NextToken`` from a previous
            response.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'repositories': [
                    {
                        'repositoryName': 'string',
                        'repositoryId': 'string'
                    },
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            Represents the output of a list repositories operation.

            - **repositories** *(list) --*

              Lists the repositories called by the list repositories operation.

              - *(dict) --*

                Information about a repository name and ID.

                - **repositoryName** *(string) --*

                  The name associated with the repository.

                - **repositoryId** *(string) --*

                  The ID associated with the repository.

            - **NextToken** *(string) --*

              A token to resume pagination.
        """
