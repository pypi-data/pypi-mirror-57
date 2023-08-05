"Main interface for codecommit service Client"
from __future__ import annotations

from typing import Any, Dict, List
from botocore.client import BaseClient
from botocore.exceptions import ClientError as Boto3ClientError
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3.type_defs import Literal, overload

# pylint: disable=import-self
import mypy_boto3_codecommit.client as client_scope

# pylint: disable=import-self
import mypy_boto3_codecommit.paginator as paginator_scope
from mypy_boto3_codecommit.type_defs import (
    ClientBatchAssociateApprovalRuleTemplateWithRepositoriesResponseTypeDef,
    ClientBatchDescribeMergeConflictsResponseTypeDef,
    ClientBatchDisassociateApprovalRuleTemplateFromRepositoriesResponseTypeDef,
    ClientBatchGetCommitsResponseTypeDef,
    ClientBatchGetRepositoriesResponseTypeDef,
    ClientCreateApprovalRuleTemplateResponseTypeDef,
    ClientCreateCommitDeleteFilesTypeDef,
    ClientCreateCommitPutFilesTypeDef,
    ClientCreateCommitResponseTypeDef,
    ClientCreateCommitSetFileModesTypeDef,
    ClientCreatePullRequestApprovalRuleResponseTypeDef,
    ClientCreatePullRequestResponseTypeDef,
    ClientCreatePullRequestTargetsTypeDef,
    ClientCreateRepositoryResponseTypeDef,
    ClientCreateUnreferencedMergeCommitConflictResolutionTypeDef,
    ClientCreateUnreferencedMergeCommitResponseTypeDef,
    ClientDeleteApprovalRuleTemplateResponseTypeDef,
    ClientDeleteBranchResponseTypeDef,
    ClientDeleteCommentContentResponseTypeDef,
    ClientDeleteFileResponseTypeDef,
    ClientDeletePullRequestApprovalRuleResponseTypeDef,
    ClientDeleteRepositoryResponseTypeDef,
    ClientDescribeMergeConflictsResponseTypeDef,
    ClientDescribePullRequestEventsResponseTypeDef,
    ClientEvaluatePullRequestApprovalRulesResponseTypeDef,
    ClientGetApprovalRuleTemplateResponseTypeDef,
    ClientGetBlobResponseTypeDef,
    ClientGetBranchResponseTypeDef,
    ClientGetCommentResponseTypeDef,
    ClientGetCommentsForComparedCommitResponseTypeDef,
    ClientGetCommentsForPullRequestResponseTypeDef,
    ClientGetCommitResponseTypeDef,
    ClientGetDifferencesResponseTypeDef,
    ClientGetFileResponseTypeDef,
    ClientGetFolderResponseTypeDef,
    ClientGetMergeCommitResponseTypeDef,
    ClientGetMergeConflictsResponseTypeDef,
    ClientGetMergeOptionsResponseTypeDef,
    ClientGetPullRequestApprovalStatesResponseTypeDef,
    ClientGetPullRequestOverrideStateResponseTypeDef,
    ClientGetPullRequestResponseTypeDef,
    ClientGetRepositoryResponseTypeDef,
    ClientGetRepositoryTriggersResponseTypeDef,
    ClientListApprovalRuleTemplatesResponseTypeDef,
    ClientListAssociatedApprovalRuleTemplatesForRepositoryResponseTypeDef,
    ClientListBranchesResponseTypeDef,
    ClientListPullRequestsResponseTypeDef,
    ClientListRepositoriesForApprovalRuleTemplateResponseTypeDef,
    ClientListRepositoriesResponseTypeDef,
    ClientListTagsForResourceResponseTypeDef,
    ClientMergeBranchesByFastForwardResponseTypeDef,
    ClientMergeBranchesBySquashConflictResolutionTypeDef,
    ClientMergeBranchesBySquashResponseTypeDef,
    ClientMergeBranchesByThreeWayConflictResolutionTypeDef,
    ClientMergeBranchesByThreeWayResponseTypeDef,
    ClientMergePullRequestByFastForwardResponseTypeDef,
    ClientMergePullRequestBySquashConflictResolutionTypeDef,
    ClientMergePullRequestBySquashResponseTypeDef,
    ClientMergePullRequestByThreeWayConflictResolutionTypeDef,
    ClientMergePullRequestByThreeWayResponseTypeDef,
    ClientPostCommentForComparedCommitLocationTypeDef,
    ClientPostCommentForComparedCommitResponseTypeDef,
    ClientPostCommentForPullRequestLocationTypeDef,
    ClientPostCommentForPullRequestResponseTypeDef,
    ClientPostCommentReplyResponseTypeDef,
    ClientPutFileResponseTypeDef,
    ClientPutRepositoryTriggersResponseTypeDef,
    ClientPutRepositoryTriggersTriggersTypeDef,
    ClientTestRepositoryTriggersResponseTypeDef,
    ClientTestRepositoryTriggersTriggersTypeDef,
    ClientUpdateApprovalRuleTemplateContentResponseTypeDef,
    ClientUpdateApprovalRuleTemplateDescriptionResponseTypeDef,
    ClientUpdateApprovalRuleTemplateNameResponseTypeDef,
    ClientUpdateCommentResponseTypeDef,
    ClientUpdatePullRequestApprovalRuleContentResponseTypeDef,
    ClientUpdatePullRequestDescriptionResponseTypeDef,
    ClientUpdatePullRequestStatusResponseTypeDef,
    ClientUpdatePullRequestTitleResponseTypeDef,
)


__all__ = ("Client",)


class Client(BaseClient):
    exceptions: client_scope.Exceptions

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def associate_approval_rule_template_with_repository(
        self, approvalRuleTemplateName: str, repositoryName: str
    ) -> None:
        """
        Creates an association between an approval rule template and a specified repository. Then,
        the next time a pull request is created in the repository where the destination reference
        (if specified) matches the destination reference (branch) for the pull request, an approval
        rule that matches the template conditions is automatically created for that pull request. If
        no destination references are specified in the template, an approval rule that matches the
        template contents is created for all pull requests in that repository.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/codecommit-2015-04-13/AssociateApprovalRuleTemplateWithRepository>`_

        **Request Syntax**
        ::

          response = client.associate_approval_rule_template_with_repository(
              approvalRuleTemplateName='string',
              repositoryName='string'
          )
        :type approvalRuleTemplateName: string
        :param approvalRuleTemplateName: **[REQUIRED]**

          The name for the approval rule template.

        :type repositoryName: string
        :param repositoryName: **[REQUIRED]**

          The name of the repository that you want to associate with the template.

        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def batch_associate_approval_rule_template_with_repositories(
        self, approvalRuleTemplateName: str, repositoryNames: List[str]
    ) -> ClientBatchAssociateApprovalRuleTemplateWithRepositoriesResponseTypeDef:
        """
        Creates an association between an approval rule template and one or more specified
        repositories.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/codecommit-2015-04-13/BatchAssociateApprovalRuleTemplateWithRepositories>`_

        **Request Syntax**
        ::

          response = client.batch_associate_approval_rule_template_with_repositories(
              approvalRuleTemplateName='string',
              repositoryNames=[
                  'string',
              ]
          )
        :type approvalRuleTemplateName: string
        :param approvalRuleTemplateName: **[REQUIRED]**

          The name of the template you want to associate with one or more repositories.

        :type repositoryNames: list
        :param repositoryNames: **[REQUIRED]**

          The names of the repositories you want to associate with the template.

          .. note::

            The length constraint limit is for each string in the array. The array itself can be
            empty.

          - *(string) --*

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'associatedRepositoryNames': [
                    'string',
                ],
                'errors': [
                    {
                        'repositoryName': 'string',
                        'errorCode': 'string',
                        'errorMessage': 'string'
                    },
                ]
            }
          **Response Structure**

          - *(dict) --*

            - **associatedRepositoryNames** *(list) --*

              A list of names of the repositories that have been associated with the template.

              - *(string) --*

            - **errors** *(list) --*

              A list of any errors that might have occurred while attempting to create the
              association between the template and the repositories.

              - *(dict) --*

                Returns information about errors in a
                BatchAssociateApprovalRuleTemplateWithRepositories operation.

                - **repositoryName** *(string) --*

                  The name of the repository where the association was not made.

                - **errorCode** *(string) --*

                  An error code that specifies whether the repository name was not valid or not
                  found.

                - **errorMessage** *(string) --*

                  An error message that provides details about why the repository name was not found
                  or not valid.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def batch_describe_merge_conflicts(
        self,
        repositoryName: str,
        destinationCommitSpecifier: str,
        sourceCommitSpecifier: str,
        mergeOption: Literal["FAST_FORWARD_MERGE", "SQUASH_MERGE", "THREE_WAY_MERGE"],
        maxMergeHunks: int = None,
        maxConflictFiles: int = None,
        filePaths: List[str] = None,
        conflictDetailLevel: Literal["FILE_LEVEL", "LINE_LEVEL"] = None,
        conflictResolutionStrategy: Literal[
            "NONE", "ACCEPT_SOURCE", "ACCEPT_DESTINATION", "AUTOMERGE"
        ] = None,
        nextToken: str = None,
    ) -> ClientBatchDescribeMergeConflictsResponseTypeDef:
        """
        Returns information about one or more merge conflicts in the attempted merge of two commit
        specifiers using the squash or three-way merge strategy.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/codecommit-2015-04-13/BatchDescribeMergeConflicts>`_

        **Request Syntax**
        ::

          response = client.batch_describe_merge_conflicts(
              repositoryName='string',
              destinationCommitSpecifier='string',
              sourceCommitSpecifier='string',
              mergeOption='FAST_FORWARD_MERGE'|'SQUASH_MERGE'|'THREE_WAY_MERGE',
              maxMergeHunks=123,
              maxConflictFiles=123,
              filePaths=[
                  'string',
              ],
              conflictDetailLevel='FILE_LEVEL'|'LINE_LEVEL',
              conflictResolutionStrategy='NONE'|'ACCEPT_SOURCE'|'ACCEPT_DESTINATION'|'AUTOMERGE',
              nextToken='string'
          )
        :type repositoryName: string
        :param repositoryName: **[REQUIRED]**

          The name of the repository that contains the merge conflicts you want to review.

        :type destinationCommitSpecifier: string
        :param destinationCommitSpecifier: **[REQUIRED]**

          The branch, tag, HEAD, or other fully qualified reference used to identify a commit (for
          example, a branch name or a full commit ID).

        :type sourceCommitSpecifier: string
        :param sourceCommitSpecifier: **[REQUIRED]**

          The branch, tag, HEAD, or other fully qualified reference used to identify a commit (for
          example, a branch name or a full commit ID).

        :type mergeOption: string
        :param mergeOption: **[REQUIRED]**

          The merge option or strategy you want to use to merge the code.

        :type maxMergeHunks: integer
        :param maxMergeHunks:

          The maximum number of merge hunks to include in the output.

        :type maxConflictFiles: integer
        :param maxConflictFiles:

          The maximum number of files to include in the output.

        :type filePaths: list
        :param filePaths:

          The path of the target files used to describe the conflicts. If not specified, the default
          is all conflict files.

          - *(string) --*

        :type conflictDetailLevel: string
        :param conflictDetailLevel:

          The level of conflict detail to use. If unspecified, the default FILE_LEVEL is used, which
          returns a not-mergeable result if the same file has differences in both branches. If
          LINE_LEVEL is specified, a conflict is considered not mergeable if the same file in both
          branches has differences on the same line.

        :type conflictResolutionStrategy: string
        :param conflictResolutionStrategy:

          Specifies which branch to use when resolving conflicts, or whether to attempt
          automatically merging two versions of a file. The default is NONE, which requires any
          conflicts to be resolved manually before the merge operation is successful.

        :type nextToken: string
        :param nextToken:

          An enumeration token that, when provided in a request, returns the next batch of the
          results.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'conflicts': [
                    {
                        'conflictMetadata': {
                            'filePath': 'string',
                            'fileSizes': {
                                'source': 123,
                                'destination': 123,
                                'base': 123
                            },
                            'fileModes': {
                                'source': 'EXECUTABLE'|'NORMAL'|'SYMLINK',
                                'destination': 'EXECUTABLE'|'NORMAL'|'SYMLINK',
                                'base': 'EXECUTABLE'|'NORMAL'|'SYMLINK'
                            },
                            'objectTypes': {
                                'source': 'FILE'|'DIRECTORY'|'GIT_LINK'|'SYMBOLIC_LINK',
                                'destination': 'FILE'|'DIRECTORY'|'GIT_LINK'|'SYMBOLIC_LINK',
                                'base': 'FILE'|'DIRECTORY'|'GIT_LINK'|'SYMBOLIC_LINK'
                            },
                            'numberOfConflicts': 123,
                            'isBinaryFile': {
                                'source': True|False,
                                'destination': True|False,
                                'base': True|False
                            },
                            'contentConflict': True|False,
                            'fileModeConflict': True|False,
                            'objectTypeConflict': True|False,
                            'mergeOperations': {
                                'source': 'A'|'M'|'D',
                                'destination': 'A'|'M'|'D'
                            }
                        },
                        'mergeHunks': [
                            {
                                'isConflict': True|False,
                                'source': {
                                    'startLine': 123,
                                    'endLine': 123,
                                    'hunkContent': 'string'
                                },
                                'destination': {
                                    'startLine': 123,
                                    'endLine': 123,
                                    'hunkContent': 'string'
                                },
                                'base': {
                                    'startLine': 123,
                                    'endLine': 123,
                                    'hunkContent': 'string'
                                }
                            },
                        ]
                    },
                ],
                'nextToken': 'string',
                'errors': [
                    {
                        'filePath': 'string',
                        'exceptionName': 'string',
                        'message': 'string'
                    },
                ],
                'destinationCommitId': 'string',
                'sourceCommitId': 'string',
                'baseCommitId': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **conflicts** *(list) --*

              A list of conflicts for each file, including the conflict metadata and the hunks of
              the differences between the files.

              - *(dict) --*

                Information about conflicts in a merge operation.

                - **conflictMetadata** *(dict) --*

                  Metadata about a conflict in a merge operation.

                  - **filePath** *(string) --*

                    The path of the file that contains conflicts.

                  - **fileSizes** *(dict) --*

                    The file sizes of the file in the source, destination, and base of the merge.

                    - **source** *(integer) --*

                      The size of a file in the source of a merge or pull request.

                    - **destination** *(integer) --*

                      The size of a file in the destination of a merge or pull request.

                    - **base** *(integer) --*

                      The size of a file in the base of a merge or pull request.

                  - **fileModes** *(dict) --*

                    The file modes of the file in the source, destination, and base of the merge.

                    - **source** *(string) --*

                      The file mode of a file in the source of a merge or pull request.

                    - **destination** *(string) --*

                      The file mode of a file in the destination of a merge or pull request.

                    - **base** *(string) --*

                      The file mode of a file in the base of a merge or pull request.

                  - **objectTypes** *(dict) --*

                    Information about any object type conflicts in a merge operation.

                    - **source** *(string) --*

                      The type of the object in the source branch.

                    - **destination** *(string) --*

                      The type of the object in the destination branch.

                    - **base** *(string) --*

                      The type of the object in the base commit of the merge.

                  - **numberOfConflicts** *(integer) --*

                    The number of conflicts, including both hunk conflicts and metadata conflicts.

                  - **isBinaryFile** *(dict) --*

                    A boolean value (true or false) indicating whether the file is binary or textual
                    in the source, destination, and base of the merge.

                    - **source** *(boolean) --*

                      The binary or non-binary status of file in the source of a merge or pull
                      request.

                    - **destination** *(boolean) --*

                      The binary or non-binary status of a file in the destination of a merge or
                      pull request.

                    - **base** *(boolean) --*

                      The binary or non-binary status of a file in the base of a merge or pull
                      request.

                  - **contentConflict** *(boolean) --*

                    A boolean value indicating whether there are conflicts in the content of a file.

                  - **fileModeConflict** *(boolean) --*

                    A boolean value indicating whether there are conflicts in the file mode of a
                    file.

                  - **objectTypeConflict** *(boolean) --*

                    A boolean value (true or false) indicating whether there are conflicts between
                    the branches in the object type of a file, folder, or submodule.

                  - **mergeOperations** *(dict) --*

                    Whether an add, modify, or delete operation caused the conflict between the
                    source and destination of the merge.

                    - **source** *(string) --*

                      The operation (add, modify, or delete) on a file in the source of a merge or
                      pull request.

                    - **destination** *(string) --*

                      The operation on a file in the destination of a merge or pull request.

                - **mergeHunks** *(list) --*

                  A list of hunks that contain the differences between files or lines causing the
                  conflict.

                  - *(dict) --*

                    Information about merge hunks in a merge or pull request operation.

                    - **isConflict** *(boolean) --*

                      A Boolean value indicating whether a combination of hunks contains a conflict.
                      Conflicts occur when the same file or the same lines in a file were modified
                      in both the source and destination of a merge or pull request. Valid values
                      include true, false, and null. True when the hunk represents a conflict and
                      one or more files contains a line conflict. File mode conflicts in a merge do
                      not set this to true.

                    - **source** *(dict) --*

                      Information about the merge hunk in the source of a merge or pull request.

                      - **startLine** *(integer) --*

                        The start position of the hunk in the merge result.

                      - **endLine** *(integer) --*

                        The end position of the hunk in the merge result.

                      - **hunkContent** *(string) --*

                        The base-64 encoded content of the hunk merged region that might contain a
                        conflict.

                    - **destination** *(dict) --*

                      Information about the merge hunk in the destination of a merge or pull
                      request.

                      - **startLine** *(integer) --*

                        The start position of the hunk in the merge result.

                      - **endLine** *(integer) --*

                        The end position of the hunk in the merge result.

                      - **hunkContent** *(string) --*

                        The base-64 encoded content of the hunk merged region that might contain a
                        conflict.

                    - **base** *(dict) --*

                      Information about the merge hunk in the base of a merge or pull request.

                      - **startLine** *(integer) --*

                        The start position of the hunk in the merge result.

                      - **endLine** *(integer) --*

                        The end position of the hunk in the merge result.

                      - **hunkContent** *(string) --*

                        The base-64 encoded content of the hunk merged region that might contain a
                        conflict.

            - **nextToken** *(string) --*

              An enumeration token that can be used in a request to return the next batch of the
              results.

            - **errors** *(list) --*

              A list of any errors returned while describing the merge conflicts for each file.

              - *(dict) --*

                Returns information about errors in a BatchDescribeMergeConflicts operation.

                - **filePath** *(string) --*

                  The path to the file.

                - **exceptionName** *(string) --*

                  The name of the exception.

                - **message** *(string) --*

                  The message provided by the exception.

            - **destinationCommitId** *(string) --*

              The commit ID of the destination commit specifier that was used in the merge
              evaluation.

            - **sourceCommitId** *(string) --*

              The commit ID of the source commit specifier that was used in the merge evaluation.

            - **baseCommitId** *(string) --*

              The commit ID of the merge base.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def batch_disassociate_approval_rule_template_from_repositories(
        self, approvalRuleTemplateName: str, repositoryNames: List[str]
    ) -> ClientBatchDisassociateApprovalRuleTemplateFromRepositoriesResponseTypeDef:
        """
        Removes the association between an approval rule template and one or more specified
        repositories.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/codecommit-2015-04-13/BatchDisassociateApprovalRuleTemplateFromRepositories>`_

        **Request Syntax**
        ::

          response = client.batch_disassociate_approval_rule_template_from_repositories(
              approvalRuleTemplateName='string',
              repositoryNames=[
                  'string',
              ]
          )
        :type approvalRuleTemplateName: string
        :param approvalRuleTemplateName: **[REQUIRED]**

          The name of the template that you want to disassociate from one or more repositories.

        :type repositoryNames: list
        :param repositoryNames: **[REQUIRED]**

          The repository names that you want to disassociate from the approval rule template.

          .. note::

            The length constraint limit is for each string in the array. The array itself can be
            empty.

          - *(string) --*

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'disassociatedRepositoryNames': [
                    'string',
                ],
                'errors': [
                    {
                        'repositoryName': 'string',
                        'errorCode': 'string',
                        'errorMessage': 'string'
                    },
                ]
            }
          **Response Structure**

          - *(dict) --*

            - **disassociatedRepositoryNames** *(list) --*

              A list of repository names that have had their association with the template removed.

              - *(string) --*

            - **errors** *(list) --*

              A list of any errors that might have occurred while attempting to remove the
              association between the template and the repositories.

              - *(dict) --*

                Returns information about errors in a
                BatchDisassociateApprovalRuleTemplateFromRepositories operation.

                - **repositoryName** *(string) --*

                  The name of the repository where the association with the template was not able to
                  be removed.

                - **errorCode** *(string) --*

                  An error code that specifies whether the repository name was not valid or not
                  found.

                - **errorMessage** *(string) --*

                  An error message that provides details about why the repository name was either
                  not found or not valid.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def batch_get_commits(
        self, commitIds: List[str], repositoryName: str
    ) -> ClientBatchGetCommitsResponseTypeDef:
        """
        Returns information about the contents of one or more commits in a repository.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/codecommit-2015-04-13/BatchGetCommits>`_

        **Request Syntax**
        ::

          response = client.batch_get_commits(
              commitIds=[
                  'string',
              ],
              repositoryName='string'
          )
        :type commitIds: list
        :param commitIds: **[REQUIRED]**

          The full commit IDs of the commits to get information about.

          .. note::

            You must supply the full SHA IDs of each commit. You cannot use shortened SHA IDs.

          - *(string) --*

        :type repositoryName: string
        :param repositoryName: **[REQUIRED]**

          The name of the repository that contains the commits.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'commits': [
                    {
                        'commitId': 'string',
                        'treeId': 'string',
                        'parents': [
                            'string',
                        ],
                        'message': 'string',
                        'author': {
                            'name': 'string',
                            'email': 'string',
                            'date': 'string'
                        },
                        'committer': {
                            'name': 'string',
                            'email': 'string',
                            'date': 'string'
                        },
                        'additionalData': 'string'
                    },
                ],
                'errors': [
                    {
                        'commitId': 'string',
                        'errorCode': 'string',
                        'errorMessage': 'string'
                    },
                ]
            }
          **Response Structure**

          - *(dict) --*

            - **commits** *(list) --*

              An array of commit data type objects, each of which contains information about a
              specified commit.

              - *(dict) --*

                Returns information about a specific commit.

                - **commitId** *(string) --*

                  The full SHA ID of the specified commit.

                - **treeId** *(string) --*

                  Tree information for the specified commit.

                - **parents** *(list) --*

                  A list of parent commits for the specified commit. Each parent commit ID is the
                  full commit ID.

                  - *(string) --*

                - **message** *(string) --*

                  The commit message associated with the specified commit.

                - **author** *(dict) --*

                  Information about the author of the specified commit. Information includes the
                  date in timestamp format with GMT offset, the name of the author, and the email
                  address for the author, as configured in Git.

                  - **name** *(string) --*

                    The name of the user who made the specified commit.

                  - **email** *(string) --*

                    The email address associated with the user who made the commit, if any.

                  - **date** *(string) --*

                    The date when the specified commit was commited, in timestamp format with GMT
                    offset.

                - **committer** *(dict) --*

                  Information about the person who committed the specified commit, also known as the
                  committer. Information includes the date in timestamp format with GMT offset, the
                  name of the committer, and the email address for the committer, as configured in
                  Git.

                  For more information about the difference between an author and a committer in
                  Git, see `Viewing the Commit History <http://git-scm.com/book/ch2-3.html>`__ in
                  Pro Git by Scott Chacon and Ben Straub.

                  - **name** *(string) --*

                    The name of the user who made the specified commit.

                  - **email** *(string) --*

                    The email address associated with the user who made the commit, if any.

                  - **date** *(string) --*

                    The date when the specified commit was commited, in timestamp format with GMT
                    offset.

                - **additionalData** *(string) --*

                  Any other data associated with the specified commit.

            - **errors** *(list) --*

              Returns any commit IDs for which information could not be found. For example, if one
              of the commit IDs was a shortened SHA ID or that commit was not found in the specified
              repository, the ID returns an error object with more information.

              - *(dict) --*

                Returns information about errors in a BatchGetCommits operation.

                - **commitId** *(string) --*

                  A commit ID that either could not be found or was not in a valid format.

                - **errorCode** *(string) --*

                  An error code that specifies whether the commit ID was not valid or not found.

                - **errorMessage** *(string) --*

                  An error message that provides detail about why the commit ID either was not found
                  or was not valid.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def batch_get_repositories(
        self, repositoryNames: List[str]
    ) -> ClientBatchGetRepositoriesResponseTypeDef:
        """
        Returns information about one or more repositories.

        .. note::

          The description field for a repository accepts all HTML characters and all valid Unicode
          characters. Applications that do not HTML-encode the description and display it in a
          webpage can expose users to potentially malicious code. Make sure that you HTML-encode the
          description field in any application that uses this API to display the repository
          description on a webpage.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/codecommit-2015-04-13/BatchGetRepositories>`_

        **Request Syntax**
        ::

          response = client.batch_get_repositories(
              repositoryNames=[
                  'string',
              ]
          )
        :type repositoryNames: list
        :param repositoryNames: **[REQUIRED]**

          The names of the repositories to get information about.

          .. note::

            The length constraint limit is for each string in the array. The array itself can be
            empty.

          - *(string) --*

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'repositories': [
                    {
                        'accountId': 'string',
                        'repositoryId': 'string',
                        'repositoryName': 'string',
                        'repositoryDescription': 'string',
                        'defaultBranch': 'string',
                        'lastModifiedDate': datetime(2015, 1, 1),
                        'creationDate': datetime(2015, 1, 1),
                        'cloneUrlHttp': 'string',
                        'cloneUrlSsh': 'string',
                        'Arn': 'string'
                    },
                ],
                'repositoriesNotFound': [
                    'string',
                ]
            }
          **Response Structure**

          - *(dict) --*

            Represents the output of a batch get repositories operation.

            - **repositories** *(list) --*

              A list of repositories returned by the batch get repositories operation.

              - *(dict) --*

                Information about a repository.

                - **accountId** *(string) --*

                  The ID of the AWS account associated with the repository.

                - **repositoryId** *(string) --*

                  The ID of the repository.

                - **repositoryName** *(string) --*

                  The repository's name.

                - **repositoryDescription** *(string) --*

                  A comment or description about the repository.

                - **defaultBranch** *(string) --*

                  The repository's default branch name.

                - **lastModifiedDate** *(datetime) --*

                  The date and time the repository was last modified, in timestamp format.

                - **creationDate** *(datetime) --*

                  The date and time the repository was created, in timestamp format.

                - **cloneUrlHttp** *(string) --*

                  The URL to use for cloning the repository over HTTPS.

                - **cloneUrlSsh** *(string) --*

                  The URL to use for cloning the repository over SSH.

                - **Arn** *(string) --*

                  The Amazon Resource Name (ARN) of the repository.

            - **repositoriesNotFound** *(list) --*

              Returns a list of repository names for which information could not be found.

              - *(string) --*
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
    def create_approval_rule_template(
        self,
        approvalRuleTemplateName: str,
        approvalRuleTemplateContent: str,
        approvalRuleTemplateDescription: str = None,
    ) -> ClientCreateApprovalRuleTemplateResponseTypeDef:
        """
        Creates a template for approval rules that can then be associated with one or more
        repositories in your AWS account. When you associate a template with a repository, AWS
        CodeCommit creates an approval rule that matches the conditions of the template for all pull
        requests that meet the conditions of the template. For more information, see
        AssociateApprovalRuleTemplateWithRepository .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/codecommit-2015-04-13/CreateApprovalRuleTemplate>`_

        **Request Syntax**
        ::

          response = client.create_approval_rule_template(
              approvalRuleTemplateName='string',
              approvalRuleTemplateContent='string',
              approvalRuleTemplateDescription='string'
          )
        :type approvalRuleTemplateName: string
        :param approvalRuleTemplateName: **[REQUIRED]**

          The name of the approval rule template. Provide descriptive names, because this name is
          applied to the approval rules created automatically in associated repositories.

        :type approvalRuleTemplateContent: string
        :param approvalRuleTemplateContent: **[REQUIRED]**

          The content of the approval rule that is created on pull requests in associated
          repositories. If you specify one or more destination references (branches), approval rules
          are created in an associated repository only if their destination references (branches)
          match those specified in the template.

          .. note::

            When you create the content of the approval rule template, you can specify approvers in
            an approval pool in one of two ways:

            * **CodeCommitApprovers** : This option only requires an AWS account and a resource. It
            can be used for both IAM users and federated access users whose name matches the
            provided resource name. This is a very powerful option that offers a great deal of
            flexibility. For example, if you specify the AWS account *123456789012* and *Mary_Major*
            , all of the following are counted as approvals coming from that user:

              * An IAM user in the account (arn:aws:iam::*123456789012* :user/*Mary_Major* )

              * A federated user identified in IAM as Mary_Major (arn:aws:sts::*123456789012*
              :federated-user/*Mary_Major* )

            This option does not recognize an active session of someone assuming the role of
            CodeCommitReview with a role session name of *Mary_Major* (arn:aws:sts::*123456789012*
            :assumed-role/CodeCommitReview/*Mary_Major* ) unless you include a wildcard
            (*Mary_Major).

            * **Fully qualified ARN** : This option allows you to specify the fully qualified Amazon
            Resource Name (ARN) of the IAM user or role.

            For more information about IAM ARNs, wildcards, and formats, see `IAM Identifiers
            <https://docs.aws.amazon.com/iam/latest/UserGuide/reference_identifiers.html>`__ in the
            *IAM User Guide* .

        :type approvalRuleTemplateDescription: string
        :param approvalRuleTemplateDescription:

          The description of the approval rule template. Consider providing a description that
          explains what this template does and when it might be appropriate to associate it with
          repositories.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'approvalRuleTemplate': {
                    'approvalRuleTemplateId': 'string',
                    'approvalRuleTemplateName': 'string',
                    'approvalRuleTemplateDescription': 'string',
                    'approvalRuleTemplateContent': 'string',
                    'ruleContentSha256': 'string',
                    'lastModifiedDate': datetime(2015, 1, 1),
                    'creationDate': datetime(2015, 1, 1),
                    'lastModifiedUser': 'string'
                }
            }
          **Response Structure**

          - *(dict) --*

            - **approvalRuleTemplate** *(dict) --*

              The content and structure of the created approval rule template.

              - **approvalRuleTemplateId** *(string) --*

                The system-generated ID of the approval rule template.

              - **approvalRuleTemplateName** *(string) --*

                The name of the approval rule template.

              - **approvalRuleTemplateDescription** *(string) --*

                The description of the approval rule template.

              - **approvalRuleTemplateContent** *(string) --*

                The content of the approval rule template.

              - **ruleContentSha256** *(string) --*

                The SHA-256 hash signature for the content of the approval rule template.

              - **lastModifiedDate** *(datetime) --*

                The date the approval rule template was most recently changed, in timestamp format.

              - **creationDate** *(datetime) --*

                The date the approval rule template was created, in timestamp format.

              - **lastModifiedUser** *(string) --*

                The Amazon Resource Name (ARN) of the user who made the most recent changes to the
                approval rule template.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_branch(self, repositoryName: str, branchName: str, commitId: str) -> None:
        """
        Creates a branch in a repository and points the branch to a commit.

        .. note::

          Calling the create branch operation does not set a repository's default branch. To do
          this, call the update default branch operation.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/codecommit-2015-04-13/CreateBranch>`_

        **Request Syntax**
        ::

          response = client.create_branch(
              repositoryName='string',
              branchName='string',
              commitId='string'
          )
        :type repositoryName: string
        :param repositoryName: **[REQUIRED]**

          The name of the repository in which you want to create the new branch.

        :type branchName: string
        :param branchName: **[REQUIRED]**

          The name of the new branch to create.

        :type commitId: string
        :param commitId: **[REQUIRED]**

          The ID of the commit to point the new branch to.

        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_commit(
        self,
        repositoryName: str,
        branchName: str,
        parentCommitId: str = None,
        authorName: str = None,
        email: str = None,
        commitMessage: str = None,
        keepEmptyFolders: bool = None,
        putFiles: List[ClientCreateCommitPutFilesTypeDef] = None,
        deleteFiles: List[ClientCreateCommitDeleteFilesTypeDef] = None,
        setFileModes: List[ClientCreateCommitSetFileModesTypeDef] = None,
    ) -> ClientCreateCommitResponseTypeDef:
        """
        Creates a commit for a repository on the tip of a specified branch.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/codecommit-2015-04-13/CreateCommit>`_

        **Request Syntax**
        ::

          response = client.create_commit(
              repositoryName='string',
              branchName='string',
              parentCommitId='string',
              authorName='string',
              email='string',
              commitMessage='string',
              keepEmptyFolders=True|False,
              putFiles=[
                  {
                      'filePath': 'string',
                      'fileMode': 'EXECUTABLE'|'NORMAL'|'SYMLINK',
                      'fileContent': b'bytes',
                      'sourceFile': {
                          'filePath': 'string',
                          'isMove': True|False
                      }
                  },
              ],
              deleteFiles=[
                  {
                      'filePath': 'string'
                  },
              ],
              setFileModes=[
                  {
                      'filePath': 'string',
                      'fileMode': 'EXECUTABLE'|'NORMAL'|'SYMLINK'
                  },
              ]
          )
        :type repositoryName: string
        :param repositoryName: **[REQUIRED]**

          The name of the repository where you create the commit.

        :type branchName: string
        :param branchName: **[REQUIRED]**

          The name of the branch where you create the commit.

        :type parentCommitId: string
        :param parentCommitId:

          The ID of the commit that is the parent of the commit you create. Not required if this is
          an empty repository.

        :type authorName: string
        :param authorName:

          The name of the author who created the commit. This information is used as both the author
          and committer for the commit.

        :type email: string
        :param email:

          The email address of the person who created the commit.

        :type commitMessage: string
        :param commitMessage:

          The commit message you want to include in the commit. Commit messages are limited to 256
          KB. If no message is specified, a default message is used.

        :type keepEmptyFolders: boolean
        :param keepEmptyFolders:

          If the commit contains deletions, whether to keep a folder or folder structure if the
          changes leave the folders empty. If true, a ..gitkeep file is created for empty folders.
          The default is false.

        :type putFiles: list
        :param putFiles:

          The files to add or update in this commit.

          - *(dict) --*

            Information about a file added or updated as part of a commit.

            - **filePath** *(string) --* **[REQUIRED]**

              The full path to the file in the repository, including the name of the file.

            - **fileMode** *(string) --*

              The extrapolated file mode permissions for the file. Valid values include EXECUTABLE
              and NORMAL.

            - **fileContent** *(bytes) --*

              The content of the file, if a source file is not specified.

            - **sourceFile** *(dict) --*

              The name and full path of the file that contains the changes you want to make as part
              of the commit, if you are not providing the file content directly.

              - **filePath** *(string) --* **[REQUIRED]**

                The full path to the file, including the name of the file.

              - **isMove** *(boolean) --*

                Whether to remove the source file from the parent commit.

        :type deleteFiles: list
        :param deleteFiles:

          The files to delete in this commit. These files still exist in earlier commits.

          - *(dict) --*

            A file that is deleted as part of a commit.

            - **filePath** *(string) --* **[REQUIRED]**

              The full path of the file to be deleted, including the name of the file.

        :type setFileModes: list
        :param setFileModes:

          The file modes to update for files in this commit.

          - *(dict) --*

            Information about the file mode changes.

            - **filePath** *(string) --* **[REQUIRED]**

              The full path to the file, including the name of the file.

            - **fileMode** *(string) --* **[REQUIRED]**

              The file mode for the file.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'commitId': 'string',
                'treeId': 'string',
                'filesAdded': [
                    {
                        'absolutePath': 'string',
                        'blobId': 'string',
                        'fileMode': 'EXECUTABLE'|'NORMAL'|'SYMLINK'
                    },
                ],
                'filesUpdated': [
                    {
                        'absolutePath': 'string',
                        'blobId': 'string',
                        'fileMode': 'EXECUTABLE'|'NORMAL'|'SYMLINK'
                    },
                ],
                'filesDeleted': [
                    {
                        'absolutePath': 'string',
                        'blobId': 'string',
                        'fileMode': 'EXECUTABLE'|'NORMAL'|'SYMLINK'
                    },
                ]
            }
          **Response Structure**

          - *(dict) --*

            - **commitId** *(string) --*

              The full commit ID of the commit that contains your committed file changes.

            - **treeId** *(string) --*

              The full SHA-1 pointer of the tree information for the commit that contains the
              commited file changes.

            - **filesAdded** *(list) --*

              The files added as part of the committed file changes.

              - *(dict) --*

                A file to be added, updated, or deleted as part of a commit.

                - **absolutePath** *(string) --*

                  The full path to the file to be added or updated, including the name of the file.

                - **blobId** *(string) --*

                  The blob ID that contains the file information.

                - **fileMode** *(string) --*

                  The extrapolated file mode permissions for the file. Valid values include
                  EXECUTABLE and NORMAL.

            - **filesUpdated** *(list) --*

              The files updated as part of the commited file changes.

              - *(dict) --*

                A file to be added, updated, or deleted as part of a commit.

                - **absolutePath** *(string) --*

                  The full path to the file to be added or updated, including the name of the file.

                - **blobId** *(string) --*

                  The blob ID that contains the file information.

                - **fileMode** *(string) --*

                  The extrapolated file mode permissions for the file. Valid values include
                  EXECUTABLE and NORMAL.

            - **filesDeleted** *(list) --*

              The files deleted as part of the committed file changes.

              - *(dict) --*

                A file to be added, updated, or deleted as part of a commit.

                - **absolutePath** *(string) --*

                  The full path to the file to be added or updated, including the name of the file.

                - **blobId** *(string) --*

                  The blob ID that contains the file information.

                - **fileMode** *(string) --*

                  The extrapolated file mode permissions for the file. Valid values include
                  EXECUTABLE and NORMAL.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_pull_request(
        self,
        title: str,
        targets: List[ClientCreatePullRequestTargetsTypeDef],
        description: str = None,
        clientRequestToken: str = None,
    ) -> ClientCreatePullRequestResponseTypeDef:
        """
        Creates a pull request in the specified repository.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/codecommit-2015-04-13/CreatePullRequest>`_

        **Request Syntax**
        ::

          response = client.create_pull_request(
              title='string',
              description='string',
              targets=[
                  {
                      'repositoryName': 'string',
                      'sourceReference': 'string',
                      'destinationReference': 'string'
                  },
              ],
              clientRequestToken='string'
          )
        :type title: string
        :param title: **[REQUIRED]**

          The title of the pull request. This title is used to identify the pull request to other
          users in the repository.

        :type description: string
        :param description:

          A description of the pull request.

        :type targets: list
        :param targets: **[REQUIRED]**

          The targets for the pull request, including the source of the code to be reviewed (the
          source branch) and the destination where the creator of the pull request intends the code
          to be merged after the pull request is closed (the destination branch).

          - *(dict) --*

            Returns information about a target for a pull request.

            - **repositoryName** *(string) --* **[REQUIRED]**

              The name of the repository that contains the pull request.

            - **sourceReference** *(string) --* **[REQUIRED]**

              The branch of the repository that contains the changes for the pull request. Also
              known as the source branch.

            - **destinationReference** *(string) --*

              The branch of the repository where the pull request changes are merged. Also known as
              the destination branch.

        :type clientRequestToken: string
        :param clientRequestToken:

          A unique, client-generated idempotency token that, when provided in a request, ensures the
          request cannot be repeated with a changed parameter. If a request is received with the
          same parameters and a token is included, the request returns information about the initial
          request that used that token.

          .. note::

            The AWS SDKs prepopulate client request tokens. If you are using an AWS SDK, an
            idempotency token is created for you.

          This field is autopopulated if not provided.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'pullRequest': {
                    'pullRequestId': 'string',
                    'title': 'string',
                    'description': 'string',
                    'lastActivityDate': datetime(2015, 1, 1),
                    'creationDate': datetime(2015, 1, 1),
                    'pullRequestStatus': 'OPEN'|'CLOSED',
                    'authorArn': 'string',
                    'pullRequestTargets': [
                        {
                            'repositoryName': 'string',
                            'sourceReference': 'string',
                            'destinationReference': 'string',
                            'destinationCommit': 'string',
                            'sourceCommit': 'string',
                            'mergeBase': 'string',
                            'mergeMetadata': {
                                'isMerged': True|False,
                                'mergedBy': 'string',
                                'mergeCommitId': 'string',
                                'mergeOption': 'FAST_FORWARD_MERGE'|'SQUASH_MERGE'|'THREE_WAY_MERGE'
                            }
                        },
                    ],
                    'clientRequestToken': 'string',
                    'revisionId': 'string',
                    'approvalRules': [
                        {
                            'approvalRuleId': 'string',
                            'approvalRuleName': 'string',
                            'approvalRuleContent': 'string',
                            'ruleContentSha256': 'string',
                            'lastModifiedDate': datetime(2015, 1, 1),
                            'creationDate': datetime(2015, 1, 1),
                            'lastModifiedUser': 'string',
                            'originApprovalRuleTemplate': {
                                'approvalRuleTemplateId': 'string',
                                'approvalRuleTemplateName': 'string'
                            }
                        },
                    ]
                }
            }
          **Response Structure**

          - *(dict) --*

            - **pullRequest** *(dict) --*

              Information about the newly created pull request.

              - **pullRequestId** *(string) --*

                The system-generated ID of the pull request.

              - **title** *(string) --*

                The user-defined title of the pull request. This title is displayed in the list of
                pull requests to other repository users.

              - **description** *(string) --*

                The user-defined description of the pull request. This description can be used to
                clarify what should be reviewed and other details of the request.

              - **lastActivityDate** *(datetime) --*

                The day and time of the last user or system activity on the pull request, in
                timestamp format.

              - **creationDate** *(datetime) --*

                The date and time the pull request was originally created, in timestamp format.

              - **pullRequestStatus** *(string) --*

                The status of the pull request. Pull request status can only change from ``OPEN`` to
                ``CLOSED`` .

              - **authorArn** *(string) --*

                The Amazon Resource Name (ARN) of the user who created the pull request.

              - **pullRequestTargets** *(list) --*

                The targets of the pull request, including the source branch and destination branch
                for the pull request.

                - *(dict) --*

                  Returns information about a pull request target.

                  - **repositoryName** *(string) --*

                    The name of the repository that contains the pull request source and destination
                    branches.

                  - **sourceReference** *(string) --*

                    The branch of the repository that contains the changes for the pull request.
                    Also known as the source branch.

                  - **destinationReference** *(string) --*

                    The branch of the repository where the pull request changes are merged. Also
                    known as the destination branch.

                  - **destinationCommit** *(string) --*

                    The full commit ID that is the tip of the destination branch. This is the commit
                    where the pull request was or will be merged.

                  - **sourceCommit** *(string) --*

                    The full commit ID of the tip of the source branch used to create the pull
                    request. If the pull request branch is updated by a push while the pull request
                    is open, the commit ID changes to reflect the new tip of the branch.

                  - **mergeBase** *(string) --*

                    The commit ID of the most recent commit that the source branch and the
                    destination branch have in common.

                  - **mergeMetadata** *(dict) --*

                    Returns metadata about the state of the merge, including whether the merge has
                    been made.

                    - **isMerged** *(boolean) --*

                      A Boolean value indicating whether the merge has been made.

                    - **mergedBy** *(string) --*

                      The Amazon Resource Name (ARN) of the user who merged the branches.

                    - **mergeCommitId** *(string) --*

                      The commit ID for the merge commit, if any.

                    - **mergeOption** *(string) --*

                      The merge strategy used in the merge.

              - **clientRequestToken** *(string) --*

                A unique, client-generated idempotency token that, when provided in a request,
                ensures the request cannot be repeated with a changed parameter. If a request is
                received with the same parameters and a token is included, the request returns
                information about the initial request that used that token.

              - **revisionId** *(string) --*

                The system-generated revision ID for the pull request.

              - **approvalRules** *(list) --*

                The approval rules applied to the pull request.

                - *(dict) --*

                  Returns information about an approval rule.

                  - **approvalRuleId** *(string) --*

                    The system-generated ID of the approval rule.

                  - **approvalRuleName** *(string) --*

                    The name of the approval rule.

                  - **approvalRuleContent** *(string) --*

                    The content of the approval rule.

                  - **ruleContentSha256** *(string) --*

                    The SHA-256 hash signature for the content of the approval rule.

                  - **lastModifiedDate** *(datetime) --*

                    The date the approval rule was most recently changed, in timestamp format.

                  - **creationDate** *(datetime) --*

                    The date the approval rule was created, in timestamp format.

                  - **lastModifiedUser** *(string) --*

                    The Amazon Resource Name (ARN) of the user who made the most recent changes to
                    the approval rule.

                  - **originApprovalRuleTemplate** *(dict) --*

                    The approval rule template used to create the rule.

                    - **approvalRuleTemplateId** *(string) --*

                      The ID of the template that created the approval rule.

                    - **approvalRuleTemplateName** *(string) --*

                      The name of the template that created the approval rule.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_pull_request_approval_rule(
        self, pullRequestId: str, approvalRuleName: str, approvalRuleContent: str
    ) -> ClientCreatePullRequestApprovalRuleResponseTypeDef:
        """
        Creates an approval rule for a pull request.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/codecommit-2015-04-13/CreatePullRequestApprovalRule>`_

        **Request Syntax**
        ::

          response = client.create_pull_request_approval_rule(
              pullRequestId='string',
              approvalRuleName='string',
              approvalRuleContent='string'
          )
        :type pullRequestId: string
        :param pullRequestId: **[REQUIRED]**

          The system-generated ID of the pull request for which you want to create the approval
          rule.

        :type approvalRuleName: string
        :param approvalRuleName: **[REQUIRED]**

          The name for the approval rule.

        :type approvalRuleContent: string
        :param approvalRuleContent: **[REQUIRED]**

          The content of the approval rule, including the number of approvals needed and the
          structure of an approval pool defined for approvals, if any. For more information about
          approval pools, see the AWS CodeCommit User Guide.

          .. note::

            When you create the content of the approval rule, you can specify approvers in an
            approval pool in one of two ways:

            * **CodeCommitApprovers** : This option only requires an AWS account and a resource. It
            can be used for both IAM users and federated access users whose name matches the
            provided resource name. This is a very powerful option that offers a great deal of
            flexibility. For example, if you specify the AWS account *123456789012* and *Mary_Major*
            , all of the following would be counted as approvals coming from that user:

              * An IAM user in the account (arn:aws:iam::*123456789012* :user/*Mary_Major* )

              * A federated user identified in IAM as Mary_Major (arn:aws:sts::*123456789012*
              :federated-user/*Mary_Major* )

            This option does not recognize an active session of someone assuming the role of
            CodeCommitReview with a role session name of *Mary_Major* (arn:aws:sts::*123456789012*
            :assumed-role/CodeCommitReview/*Mary_Major* ) unless you include a wildcard
            (*Mary_Major).

            * **Fully qualified ARN** : This option allows you to specify the fully qualified Amazon
            Resource Name (ARN) of the IAM user or role.

            For more information about IAM ARNs, wildcards, and formats, see `IAM Identifiers
            <https://docs.aws.amazon.com/iam/latest/UserGuide/reference_identifiers.html>`__ in the
            *IAM User Guide* .

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'approvalRule': {
                    'approvalRuleId': 'string',
                    'approvalRuleName': 'string',
                    'approvalRuleContent': 'string',
                    'ruleContentSha256': 'string',
                    'lastModifiedDate': datetime(2015, 1, 1),
                    'creationDate': datetime(2015, 1, 1),
                    'lastModifiedUser': 'string',
                    'originApprovalRuleTemplate': {
                        'approvalRuleTemplateId': 'string',
                        'approvalRuleTemplateName': 'string'
                    }
                }
            }
          **Response Structure**

          - *(dict) --*

            - **approvalRule** *(dict) --*

              Information about the created approval rule.

              - **approvalRuleId** *(string) --*

                The system-generated ID of the approval rule.

              - **approvalRuleName** *(string) --*

                The name of the approval rule.

              - **approvalRuleContent** *(string) --*

                The content of the approval rule.

              - **ruleContentSha256** *(string) --*

                The SHA-256 hash signature for the content of the approval rule.

              - **lastModifiedDate** *(datetime) --*

                The date the approval rule was most recently changed, in timestamp format.

              - **creationDate** *(datetime) --*

                The date the approval rule was created, in timestamp format.

              - **lastModifiedUser** *(string) --*

                The Amazon Resource Name (ARN) of the user who made the most recent changes to the
                approval rule.

              - **originApprovalRuleTemplate** *(dict) --*

                The approval rule template used to create the rule.

                - **approvalRuleTemplateId** *(string) --*

                  The ID of the template that created the approval rule.

                - **approvalRuleTemplateName** *(string) --*

                  The name of the template that created the approval rule.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_repository(
        self, repositoryName: str, repositoryDescription: str = None, tags: Dict[str, str] = None
    ) -> ClientCreateRepositoryResponseTypeDef:
        """
        Creates a new, empty repository.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/codecommit-2015-04-13/CreateRepository>`_

        **Request Syntax**
        ::

          response = client.create_repository(
              repositoryName='string',
              repositoryDescription='string',
              tags={
                  'string': 'string'
              }
          )
        :type repositoryName: string
        :param repositoryName: **[REQUIRED]**

          The name of the new repository to be created.

          .. note::

            The repository name must be unique across the calling AWS account. Repository names are
            limited to 100 alphanumeric, dash, and underscore characters, and cannot include certain
            characters. For more information about the limits on repository names, see `Limits
            <https://docs.aws.amazon.com/codecommit/latest/userguide/limits.html>`__ in the *AWS
            CodeCommit User Guide* . The suffix .git is prohibited.

        :type repositoryDescription: string
        :param repositoryDescription:

          A comment or description about the new repository.

          .. note::

            The description field for a repository accepts all HTML characters and all valid Unicode
            characters. Applications that do not HTML-encode the description and display it in a
            webpage can expose users to potentially malicious code. Make sure that you HTML-encode
            the description field in any application that uses this API to display the repository
            description on a webpage.

        :type tags: dict
        :param tags:

          One or more tag key-value pairs to use when tagging this repository.

          - *(string) --*

            - *(string) --*

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'repositoryMetadata': {
                    'accountId': 'string',
                    'repositoryId': 'string',
                    'repositoryName': 'string',
                    'repositoryDescription': 'string',
                    'defaultBranch': 'string',
                    'lastModifiedDate': datetime(2015, 1, 1),
                    'creationDate': datetime(2015, 1, 1),
                    'cloneUrlHttp': 'string',
                    'cloneUrlSsh': 'string',
                    'Arn': 'string'
                }
            }
          **Response Structure**

          - *(dict) --*

            Represents the output of a create repository operation.

            - **repositoryMetadata** *(dict) --*

              Information about the newly created repository.

              - **accountId** *(string) --*

                The ID of the AWS account associated with the repository.

              - **repositoryId** *(string) --*

                The ID of the repository.

              - **repositoryName** *(string) --*

                The repository's name.

              - **repositoryDescription** *(string) --*

                A comment or description about the repository.

              - **defaultBranch** *(string) --*

                The repository's default branch name.

              - **lastModifiedDate** *(datetime) --*

                The date and time the repository was last modified, in timestamp format.

              - **creationDate** *(datetime) --*

                The date and time the repository was created, in timestamp format.

              - **cloneUrlHttp** *(string) --*

                The URL to use for cloning the repository over HTTPS.

              - **cloneUrlSsh** *(string) --*

                The URL to use for cloning the repository over SSH.

              - **Arn** *(string) --*

                The Amazon Resource Name (ARN) of the repository.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_unreferenced_merge_commit(
        self,
        repositoryName: str,
        sourceCommitSpecifier: str,
        destinationCommitSpecifier: str,
        mergeOption: Literal["FAST_FORWARD_MERGE", "SQUASH_MERGE", "THREE_WAY_MERGE"],
        conflictDetailLevel: Literal["FILE_LEVEL", "LINE_LEVEL"] = None,
        conflictResolutionStrategy: Literal[
            "NONE", "ACCEPT_SOURCE", "ACCEPT_DESTINATION", "AUTOMERGE"
        ] = None,
        authorName: str = None,
        email: str = None,
        commitMessage: str = None,
        keepEmptyFolders: bool = None,
        conflictResolution: ClientCreateUnreferencedMergeCommitConflictResolutionTypeDef = None,
    ) -> ClientCreateUnreferencedMergeCommitResponseTypeDef:
        """
        Creates an unreferenced commit that represents the result of merging two branches using a
        specified merge strategy. This can help you determine the outcome of a potential merge. This
        API cannot be used with the fast-forward merge strategy because that strategy does not
        create a merge commit.

        .. note::

          This unreferenced merge commit can only be accessed using the GetCommit API or through git
          commands such as git fetch. To retrieve this commit, you must specify its commit ID or
          otherwise reference it.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/codecommit-2015-04-13/CreateUnreferencedMergeCommit>`_

        **Request Syntax**
        ::

          response = client.create_unreferenced_merge_commit(
              repositoryName='string',
              sourceCommitSpecifier='string',
              destinationCommitSpecifier='string',
              mergeOption='FAST_FORWARD_MERGE'|'SQUASH_MERGE'|'THREE_WAY_MERGE',
              conflictDetailLevel='FILE_LEVEL'|'LINE_LEVEL',
              conflictResolutionStrategy='NONE'|'ACCEPT_SOURCE'|'ACCEPT_DESTINATION'|'AUTOMERGE',
              authorName='string',
              email='string',
              commitMessage='string',
              keepEmptyFolders=True|False,
              conflictResolution={
                  'replaceContents': [
                      {
                          'filePath': 'string',
                          'replacementType':
                          'KEEP_BASE'|'KEEP_SOURCE'|'KEEP_DESTINATION'
                          |'USE_NEW_CONTENT',
                          'content': b'bytes',
                          'fileMode': 'EXECUTABLE'|'NORMAL'|'SYMLINK'
                      },
                  ],
                  'deleteFiles': [
                      {
                          'filePath': 'string'
                      },
                  ],
                  'setFileModes': [
                      {
                          'filePath': 'string',
                          'fileMode': 'EXECUTABLE'|'NORMAL'|'SYMLINK'
                      },
                  ]
              }
          )
        :type repositoryName: string
        :param repositoryName: **[REQUIRED]**

          The name of the repository where you want to create the unreferenced merge commit.

        :type sourceCommitSpecifier: string
        :param sourceCommitSpecifier: **[REQUIRED]**

          The branch, tag, HEAD, or other fully qualified reference used to identify a commit (for
          example, a branch name or a full commit ID).

        :type destinationCommitSpecifier: string
        :param destinationCommitSpecifier: **[REQUIRED]**

          The branch, tag, HEAD, or other fully qualified reference used to identify a commit (for
          example, a branch name or a full commit ID).

        :type mergeOption: string
        :param mergeOption: **[REQUIRED]**

          The merge option or strategy you want to use to merge the code.

        :type conflictDetailLevel: string
        :param conflictDetailLevel:

          The level of conflict detail to use. If unspecified, the default FILE_LEVEL is used, which
          returns a not-mergeable result if the same file has differences in both branches. If
          LINE_LEVEL is specified, a conflict is considered not mergeable if the same file in both
          branches has differences on the same line.

        :type conflictResolutionStrategy: string
        :param conflictResolutionStrategy:

          Specifies which branch to use when resolving conflicts, or whether to attempt
          automatically merging two versions of a file. The default is NONE, which requires any
          conflicts to be resolved manually before the merge operation is successful.

        :type authorName: string
        :param authorName:

          The name of the author who created the unreferenced commit. This information is used as
          both the author and committer for the commit.

        :type email: string
        :param email:

          The email address for the person who created the unreferenced commit.

        :type commitMessage: string
        :param commitMessage:

          The commit message for the unreferenced commit.

        :type keepEmptyFolders: boolean
        :param keepEmptyFolders:

          If the commit contains deletions, whether to keep a folder or folder structure if the
          changes leave the folders empty. If this is specified as true, a .gitkeep file is created
          for empty folders. The default is false.

        :type conflictResolution: dict
        :param conflictResolution:

          If AUTOMERGE is the conflict resolution strategy, a list of inputs to use when resolving
          conflicts during a merge.

          - **replaceContents** *(list) --*

            Files to have content replaced as part of the merge conflict resolution.

            - *(dict) --*

              Information about a replacement content entry in the conflict of a merge or pull
              request operation.

              - **filePath** *(string) --* **[REQUIRED]**

                The path of the conflicting file.

              - **replacementType** *(string) --* **[REQUIRED]**

                The replacement type to use when determining how to resolve the conflict.

              - **content** *(bytes) --*

                The base-64 encoded content to use when the replacement type is USE_NEW_CONTENT.

              - **fileMode** *(string) --*

                The file mode to apply during conflict resoltion.

          - **deleteFiles** *(list) --*

            Files to be deleted as part of the merge conflict resolution.

            - *(dict) --*

              A file that is deleted as part of a commit.

              - **filePath** *(string) --* **[REQUIRED]**

                The full path of the file to be deleted, including the name of the file.

          - **setFileModes** *(list) --*

            File modes that are set as part of the merge conflict resolution.

            - *(dict) --*

              Information about the file mode changes.

              - **filePath** *(string) --* **[REQUIRED]**

                The full path to the file, including the name of the file.

              - **fileMode** *(string) --* **[REQUIRED]**

                The file mode for the file.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'commitId': 'string',
                'treeId': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **commitId** *(string) --*

              The full commit ID of the commit that contains your merge results.

            - **treeId** *(string) --*

              The full SHA-1 pointer of the tree information for the commit that contains the merge
              results.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_approval_rule_template(
        self, approvalRuleTemplateName: str
    ) -> ClientDeleteApprovalRuleTemplateResponseTypeDef:
        """
        Deletes a specified approval rule template. Deleting a template does not remove approval
        rules on pull requests already created with the template.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/codecommit-2015-04-13/DeleteApprovalRuleTemplate>`_

        **Request Syntax**
        ::

          response = client.delete_approval_rule_template(
              approvalRuleTemplateName='string'
          )
        :type approvalRuleTemplateName: string
        :param approvalRuleTemplateName: **[REQUIRED]**

          The name of the approval rule template to delete.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'approvalRuleTemplateId': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **approvalRuleTemplateId** *(string) --*

              The system-generated ID of the deleted approval rule template. If the template has
              been previously deleted, the only response is a 200 OK.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_branch(
        self, repositoryName: str, branchName: str
    ) -> ClientDeleteBranchResponseTypeDef:
        """
        Deletes a branch from a repository, unless that branch is the default branch for the
        repository.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/codecommit-2015-04-13/DeleteBranch>`_

        **Request Syntax**
        ::

          response = client.delete_branch(
              repositoryName='string',
              branchName='string'
          )
        :type repositoryName: string
        :param repositoryName: **[REQUIRED]**

          The name of the repository that contains the branch to be deleted.

        :type branchName: string
        :param branchName: **[REQUIRED]**

          The name of the branch to delete.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'deletedBranch': {
                    'branchName': 'string',
                    'commitId': 'string'
                }
            }
          **Response Structure**

          - *(dict) --*

            Represents the output of a delete branch operation.

            - **deletedBranch** *(dict) --*

              Information about the branch deleted by the operation, including the branch name and
              the commit ID that was the tip of the branch.

              - **branchName** *(string) --*

                The name of the branch.

              - **commitId** *(string) --*

                The ID of the last commit made to the branch.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_comment_content(self, commentId: str) -> ClientDeleteCommentContentResponseTypeDef:
        """
        Deletes the content of a comment made on a change, file, or commit in a repository.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/codecommit-2015-04-13/DeleteCommentContent>`_

        **Request Syntax**
        ::

          response = client.delete_comment_content(
              commentId='string'
          )
        :type commentId: string
        :param commentId: **[REQUIRED]**

          The unique, system-generated ID of the comment. To get this ID, use
          GetCommentsForComparedCommit or  GetCommentsForPullRequest .

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'comment': {
                    'commentId': 'string',
                    'content': 'string',
                    'inReplyTo': 'string',
                    'creationDate': datetime(2015, 1, 1),
                    'lastModifiedDate': datetime(2015, 1, 1),
                    'authorArn': 'string',
                    'deleted': True|False,
                    'clientRequestToken': 'string'
                }
            }
          **Response Structure**

          - *(dict) --*

            - **comment** *(dict) --*

              Information about the comment you just deleted.

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
                ensures the request cannot be repeated with a changed parameter. If a request is
                received with the same parameters and a token is included, the request returns
                information about the initial request that used that token.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_file(
        self,
        repositoryName: str,
        branchName: str,
        filePath: str,
        parentCommitId: str,
        keepEmptyFolders: bool = None,
        commitMessage: str = None,
        name: str = None,
        email: str = None,
    ) -> ClientDeleteFileResponseTypeDef:
        """
        Deletes a specified file from a specified branch. A commit is created on the branch that
        contains the revision. The file still exists in the commits earlier to the commit that
        contains the deletion.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/codecommit-2015-04-13/DeleteFile>`_

        **Request Syntax**
        ::

          response = client.delete_file(
              repositoryName='string',
              branchName='string',
              filePath='string',
              parentCommitId='string',
              keepEmptyFolders=True|False,
              commitMessage='string',
              name='string',
              email='string'
          )
        :type repositoryName: string
        :param repositoryName: **[REQUIRED]**

          The name of the repository that contains the file to delete.

        :type branchName: string
        :param branchName: **[REQUIRED]**

          The name of the branch where the commit that deletes the file is made.

        :type filePath: string
        :param filePath: **[REQUIRED]**

          The fully qualified path to the file that to be deleted, including the full name and
          extension of that file. For example, /examples/file.md is a fully qualified path to a file
          named file.md in a folder named examples.

        :type parentCommitId: string
        :param parentCommitId: **[REQUIRED]**

          The ID of the commit that is the tip of the branch where you want to create the commit
          that deletes the file. This must be the HEAD commit for the branch. The commit that
          deletes the file is created from this commit ID.

        :type keepEmptyFolders: boolean
        :param keepEmptyFolders:

          If a file is the only object in the folder or directory, specifies whether to delete the
          folder or directory that contains the file. By default, empty folders are deleted. This
          includes empty folders that are part of the directory structure. For example, if the path
          to a file is dir1/dir2/dir3/dir4, and dir2 and dir3 are empty, deleting the last file in
          dir4 also deletes the empty folders dir4, dir3, and dir2.

        :type commitMessage: string
        :param commitMessage:

          The commit message you want to include as part of deleting the file. Commit messages are
          limited to 256 KB. If no message is specified, a default message is used.

        :type name: string
        :param name:

          The name of the author of the commit that deletes the file. If no name is specified, the
          user's ARN is used as the author name and committer name.

        :type email: string
        :param email:

          The email address for the commit that deletes the file. If no email address is specified,
          the email address is left blank.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'commitId': 'string',
                'blobId': 'string',
                'treeId': 'string',
                'filePath': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **commitId** *(string) --*

              The full commit ID of the commit that contains the change that deletes the file.

            - **blobId** *(string) --*

              The blob ID removed from the tree as part of deleting the file.

            - **treeId** *(string) --*

              The full SHA-1 pointer of the tree information for the commit that contains the delete
              file change.

            - **filePath** *(string) --*

              The fully qualified path to the file to be deleted, including the full name and
              extension of that file.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_pull_request_approval_rule(
        self, pullRequestId: str, approvalRuleName: str
    ) -> ClientDeletePullRequestApprovalRuleResponseTypeDef:
        """
        Deletes an approval rule from a specified pull request. Approval rules can be deleted from a
        pull request only if the pull request is open, and if the approval rule was created
        specifically for a pull request and not generated from an approval rule template associated
        with the repository where the pull request was created. You cannot delete an approval rule
        from a merged or closed pull request.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/codecommit-2015-04-13/DeletePullRequestApprovalRule>`_

        **Request Syntax**
        ::

          response = client.delete_pull_request_approval_rule(
              pullRequestId='string',
              approvalRuleName='string'
          )
        :type pullRequestId: string
        :param pullRequestId: **[REQUIRED]**

          The system-generated ID of the pull request that contains the approval rule you want to
          delete.

        :type approvalRuleName: string
        :param approvalRuleName: **[REQUIRED]**

          The name of the approval rule you want to delete.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'approvalRuleId': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **approvalRuleId** *(string) --*

              The ID of the deleted approval rule.

              .. note::

                If the approval rule was deleted in an earlier API call, the response is 200 OK
                without content.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_repository(self, repositoryName: str) -> ClientDeleteRepositoryResponseTypeDef:
        """
        Deletes a repository. If a specified repository was already deleted, a null repository ID is
        returned.

        .. warning::

          Deleting a repository also deletes all associated objects and metadata. After a repository
          is deleted, all future push calls to the deleted repository fail.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/codecommit-2015-04-13/DeleteRepository>`_

        **Request Syntax**
        ::

          response = client.delete_repository(
              repositoryName='string'
          )
        :type repositoryName: string
        :param repositoryName: **[REQUIRED]**

          The name of the repository to delete.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'repositoryId': 'string'
            }
          **Response Structure**

          - *(dict) --*

            Represents the output of a delete repository operation.

            - **repositoryId** *(string) --*

              The ID of the repository that was deleted.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_merge_conflicts(
        self,
        repositoryName: str,
        destinationCommitSpecifier: str,
        sourceCommitSpecifier: str,
        mergeOption: Literal["FAST_FORWARD_MERGE", "SQUASH_MERGE", "THREE_WAY_MERGE"],
        filePath: str,
        maxMergeHunks: int = None,
        conflictDetailLevel: Literal["FILE_LEVEL", "LINE_LEVEL"] = None,
        conflictResolutionStrategy: Literal[
            "NONE", "ACCEPT_SOURCE", "ACCEPT_DESTINATION", "AUTOMERGE"
        ] = None,
        nextToken: str = None,
    ) -> ClientDescribeMergeConflictsResponseTypeDef:
        """
        Returns information about one or more merge conflicts in the attempted merge of two commit
        specifiers using the squash or three-way merge strategy. If the merge option for the
        attempted merge is specified as FAST_FORWARD_MERGE, an exception is thrown.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/codecommit-2015-04-13/DescribeMergeConflicts>`_

        **Request Syntax**
        ::

          response = client.describe_merge_conflicts(
              repositoryName='string',
              destinationCommitSpecifier='string',
              sourceCommitSpecifier='string',
              mergeOption='FAST_FORWARD_MERGE'|'SQUASH_MERGE'|'THREE_WAY_MERGE',
              maxMergeHunks=123,
              filePath='string',
              conflictDetailLevel='FILE_LEVEL'|'LINE_LEVEL',
              conflictResolutionStrategy='NONE'|'ACCEPT_SOURCE'|'ACCEPT_DESTINATION'|'AUTOMERGE',
              nextToken='string'
          )
        :type repositoryName: string
        :param repositoryName: **[REQUIRED]**

          The name of the repository where you want to get information about a merge conflict.

        :type destinationCommitSpecifier: string
        :param destinationCommitSpecifier: **[REQUIRED]**

          The branch, tag, HEAD, or other fully qualified reference used to identify a commit (for
          example, a branch name or a full commit ID).

        :type sourceCommitSpecifier: string
        :param sourceCommitSpecifier: **[REQUIRED]**

          The branch, tag, HEAD, or other fully qualified reference used to identify a commit (for
          example, a branch name or a full commit ID).

        :type mergeOption: string
        :param mergeOption: **[REQUIRED]**

          The merge option or strategy you want to use to merge the code.

        :type maxMergeHunks: integer
        :param maxMergeHunks:

          The maximum number of merge hunks to include in the output.

        :type filePath: string
        :param filePath: **[REQUIRED]**

          The path of the target files used to describe the conflicts.

        :type conflictDetailLevel: string
        :param conflictDetailLevel:

          The level of conflict detail to use. If unspecified, the default FILE_LEVEL is used, which
          returns a not-mergeable result if the same file has differences in both branches. If
          LINE_LEVEL is specified, a conflict is considered not mergeable if the same file in both
          branches has differences on the same line.

        :type conflictResolutionStrategy: string
        :param conflictResolutionStrategy:

          Specifies which branch to use when resolving conflicts, or whether to attempt
          automatically merging two versions of a file. The default is NONE, which requires any
          conflicts to be resolved manually before the merge operation is successful.

        :type nextToken: string
        :param nextToken:

          An enumeration token that, when provided in a request, returns the next batch of the
          results.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'conflictMetadata': {
                    'filePath': 'string',
                    'fileSizes': {
                        'source': 123,
                        'destination': 123,
                        'base': 123
                    },
                    'fileModes': {
                        'source': 'EXECUTABLE'|'NORMAL'|'SYMLINK',
                        'destination': 'EXECUTABLE'|'NORMAL'|'SYMLINK',
                        'base': 'EXECUTABLE'|'NORMAL'|'SYMLINK'
                    },
                    'objectTypes': {
                        'source': 'FILE'|'DIRECTORY'|'GIT_LINK'|'SYMBOLIC_LINK',
                        'destination': 'FILE'|'DIRECTORY'|'GIT_LINK'|'SYMBOLIC_LINK',
                        'base': 'FILE'|'DIRECTORY'|'GIT_LINK'|'SYMBOLIC_LINK'
                    },
                    'numberOfConflicts': 123,
                    'isBinaryFile': {
                        'source': True|False,
                        'destination': True|False,
                        'base': True|False
                    },
                    'contentConflict': True|False,
                    'fileModeConflict': True|False,
                    'objectTypeConflict': True|False,
                    'mergeOperations': {
                        'source': 'A'|'M'|'D',
                        'destination': 'A'|'M'|'D'
                    }
                },
                'mergeHunks': [
                    {
                        'isConflict': True|False,
                        'source': {
                            'startLine': 123,
                            'endLine': 123,
                            'hunkContent': 'string'
                        },
                        'destination': {
                            'startLine': 123,
                            'endLine': 123,
                            'hunkContent': 'string'
                        },
                        'base': {
                            'startLine': 123,
                            'endLine': 123,
                            'hunkContent': 'string'
                        }
                    },
                ],
                'nextToken': 'string',
                'destinationCommitId': 'string',
                'sourceCommitId': 'string',
                'baseCommitId': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **conflictMetadata** *(dict) --*

              Contains metadata about the conflicts found in the merge.

              - **filePath** *(string) --*

                The path of the file that contains conflicts.

              - **fileSizes** *(dict) --*

                The file sizes of the file in the source, destination, and base of the merge.

                - **source** *(integer) --*

                  The size of a file in the source of a merge or pull request.

                - **destination** *(integer) --*

                  The size of a file in the destination of a merge or pull request.

                - **base** *(integer) --*

                  The size of a file in the base of a merge or pull request.

              - **fileModes** *(dict) --*

                The file modes of the file in the source, destination, and base of the merge.

                - **source** *(string) --*

                  The file mode of a file in the source of a merge or pull request.

                - **destination** *(string) --*

                  The file mode of a file in the destination of a merge or pull request.

                - **base** *(string) --*

                  The file mode of a file in the base of a merge or pull request.

              - **objectTypes** *(dict) --*

                Information about any object type conflicts in a merge operation.

                - **source** *(string) --*

                  The type of the object in the source branch.

                - **destination** *(string) --*

                  The type of the object in the destination branch.

                - **base** *(string) --*

                  The type of the object in the base commit of the merge.

              - **numberOfConflicts** *(integer) --*

                The number of conflicts, including both hunk conflicts and metadata conflicts.

              - **isBinaryFile** *(dict) --*

                A boolean value (true or false) indicating whether the file is binary or textual in
                the source, destination, and base of the merge.

                - **source** *(boolean) --*

                  The binary or non-binary status of file in the source of a merge or pull request.

                - **destination** *(boolean) --*

                  The binary or non-binary status of a file in the destination of a merge or pull
                  request.

                - **base** *(boolean) --*

                  The binary or non-binary status of a file in the base of a merge or pull request.

              - **contentConflict** *(boolean) --*

                A boolean value indicating whether there are conflicts in the content of a file.

              - **fileModeConflict** *(boolean) --*

                A boolean value indicating whether there are conflicts in the file mode of a file.

              - **objectTypeConflict** *(boolean) --*

                A boolean value (true or false) indicating whether there are conflicts between the
                branches in the object type of a file, folder, or submodule.

              - **mergeOperations** *(dict) --*

                Whether an add, modify, or delete operation caused the conflict between the source
                and destination of the merge.

                - **source** *(string) --*

                  The operation (add, modify, or delete) on a file in the source of a merge or pull
                  request.

                - **destination** *(string) --*

                  The operation on a file in the destination of a merge or pull request.

            - **mergeHunks** *(list) --*

              A list of merge hunks of the differences between the files or lines.

              - *(dict) --*

                Information about merge hunks in a merge or pull request operation.

                - **isConflict** *(boolean) --*

                  A Boolean value indicating whether a combination of hunks contains a conflict.
                  Conflicts occur when the same file or the same lines in a file were modified in
                  both the source and destination of a merge or pull request. Valid values include
                  true, false, and null. True when the hunk represents a conflict and one or more
                  files contains a line conflict. File mode conflicts in a merge do not set this to
                  true.

                - **source** *(dict) --*

                  Information about the merge hunk in the source of a merge or pull request.

                  - **startLine** *(integer) --*

                    The start position of the hunk in the merge result.

                  - **endLine** *(integer) --*

                    The end position of the hunk in the merge result.

                  - **hunkContent** *(string) --*

                    The base-64 encoded content of the hunk merged region that might contain a
                    conflict.

                - **destination** *(dict) --*

                  Information about the merge hunk in the destination of a merge or pull request.

                  - **startLine** *(integer) --*

                    The start position of the hunk in the merge result.

                  - **endLine** *(integer) --*

                    The end position of the hunk in the merge result.

                  - **hunkContent** *(string) --*

                    The base-64 encoded content of the hunk merged region that might contain a
                    conflict.

                - **base** *(dict) --*

                  Information about the merge hunk in the base of a merge or pull request.

                  - **startLine** *(integer) --*

                    The start position of the hunk in the merge result.

                  - **endLine** *(integer) --*

                    The end position of the hunk in the merge result.

                  - **hunkContent** *(string) --*

                    The base-64 encoded content of the hunk merged region that might contain a
                    conflict.

            - **nextToken** *(string) --*

              An enumeration token that can be used in a request to return the next batch of the
              results.

            - **destinationCommitId** *(string) --*

              The commit ID of the destination commit specifier that was used in the merge
              evaluation.

            - **sourceCommitId** *(string) --*

              The commit ID of the source commit specifier that was used in the merge evaluation.

            - **baseCommitId** *(string) --*

              The commit ID of the merge base.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_pull_request_events(
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
        nextToken: str = None,
        maxResults: int = None,
    ) -> ClientDescribePullRequestEventsResponseTypeDef:
        """
        Returns information about one or more pull request events.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/codecommit-2015-04-13/DescribePullRequestEvents>`_

        **Request Syntax**
        ::

          response = client.describe_pull_request_events(
              pullRequestId='string',
              pullRequestEventType=
                  'PULL_REQUEST_CREATED'|'PULL_REQUEST_STATUS_CHANGED'
                  |'PULL_REQUEST_SOURCE_REFERENCE_UPDATED'|'PULL_REQUEST_MERGE_STATE_CHANGED'
                  |'PULL_REQUEST_APPROVAL_RULE_CREATED'|'PULL_REQUEST_APPROVAL_RULE_UPDATED'
                  |'PULL_REQUEST_APPROVAL_RULE_DELETED'|'PULL_REQUEST_APPROVAL_RULE_OVERRIDDEN'
                  |'PULL_REQUEST_APPROVAL_STATE_CHANGED',
              actorArn='string',
              nextToken='string',
              maxResults=123
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

        :type nextToken: string
        :param nextToken:

          An enumeration token that, when provided in a request, returns the next batch of the
          results.

        :type maxResults: integer
        :param maxResults:

          A non-zero, non-negative integer used to limit the number of returned results. The default
          is 100 events, which is also the maximum number of events that can be returned in a
          result.

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
                'nextToken': 'string'
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

            - **nextToken** *(string) --*

              An enumeration token that can be used in a request to return the next batch of the
              results.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def disassociate_approval_rule_template_from_repository(
        self, approvalRuleTemplateName: str, repositoryName: str
    ) -> None:
        """
        Removes the association between a template and a repository so that approval rules based on
        the template are not automatically created when pull requests are created in the specified
        repository. This does not delete any approval rules previously created for pull requests
        through the template association.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/codecommit-2015-04-13/DisassociateApprovalRuleTemplateFromRepository>`_

        **Request Syntax**
        ::

          response = client.disassociate_approval_rule_template_from_repository(
              approvalRuleTemplateName='string',
              repositoryName='string'
          )
        :type approvalRuleTemplateName: string
        :param approvalRuleTemplateName: **[REQUIRED]**

          The name of the approval rule template to disassociate from a specified repository.

        :type repositoryName: string
        :param repositoryName: **[REQUIRED]**

          The name of the repository you want to disassociate from the template.

        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def evaluate_pull_request_approval_rules(
        self, pullRequestId: str, revisionId: str
    ) -> ClientEvaluatePullRequestApprovalRulesResponseTypeDef:
        """
        Evaluates whether a pull request has met all the conditions specified in its associated
        approval rules.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/codecommit-2015-04-13/EvaluatePullRequestApprovalRules>`_

        **Request Syntax**
        ::

          response = client.evaluate_pull_request_approval_rules(
              pullRequestId='string',
              revisionId='string'
          )
        :type pullRequestId: string
        :param pullRequestId: **[REQUIRED]**

          The system-generated ID of the pull request you want to evaluate.

        :type revisionId: string
        :param revisionId: **[REQUIRED]**

          The system-generated ID for the pull request revision. To retrieve the most recent
          revision ID for a pull request, use  GetPullRequest .

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'evaluation': {
                    'approved': True|False,
                    'overridden': True|False,
                    'approvalRulesSatisfied': [
                        'string',
                    ],
                    'approvalRulesNotSatisfied': [
                        'string',
                    ]
                }
            }
          **Response Structure**

          - *(dict) --*

            - **evaluation** *(dict) --*

              The result of the evaluation, including the names of the rules whose conditions have
              been met (if any), the names of the rules whose conditions have not been met (if any),
              whether the pull request is in the approved state, and whether the pull request
              approval rule has been set aside by an override.

              - **approved** *(boolean) --*

                Whether the state of the pull request is approved.

              - **overridden** *(boolean) --*

                Whether the approval rule requirements for the pull request have been overridden and
                no longer need to be met.

              - **approvalRulesSatisfied** *(list) --*

                The names of the approval rules that have had their conditions met.

                - *(string) --*

              - **approvalRulesNotSatisfied** *(list) --*

                The names of the approval rules that have not had their conditions met.

                - *(string) --*
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
    def get_approval_rule_template(
        self, approvalRuleTemplateName: str
    ) -> ClientGetApprovalRuleTemplateResponseTypeDef:
        """
        Returns information about a specified approval rule template.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/codecommit-2015-04-13/GetApprovalRuleTemplate>`_

        **Request Syntax**
        ::

          response = client.get_approval_rule_template(
              approvalRuleTemplateName='string'
          )
        :type approvalRuleTemplateName: string
        :param approvalRuleTemplateName: **[REQUIRED]**

          The name of the approval rule template for which you want to get information.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'approvalRuleTemplate': {
                    'approvalRuleTemplateId': 'string',
                    'approvalRuleTemplateName': 'string',
                    'approvalRuleTemplateDescription': 'string',
                    'approvalRuleTemplateContent': 'string',
                    'ruleContentSha256': 'string',
                    'lastModifiedDate': datetime(2015, 1, 1),
                    'creationDate': datetime(2015, 1, 1),
                    'lastModifiedUser': 'string'
                }
            }
          **Response Structure**

          - *(dict) --*

            - **approvalRuleTemplate** *(dict) --*

              The content and structure of the approval rule template.

              - **approvalRuleTemplateId** *(string) --*

                The system-generated ID of the approval rule template.

              - **approvalRuleTemplateName** *(string) --*

                The name of the approval rule template.

              - **approvalRuleTemplateDescription** *(string) --*

                The description of the approval rule template.

              - **approvalRuleTemplateContent** *(string) --*

                The content of the approval rule template.

              - **ruleContentSha256** *(string) --*

                The SHA-256 hash signature for the content of the approval rule template.

              - **lastModifiedDate** *(datetime) --*

                The date the approval rule template was most recently changed, in timestamp format.

              - **creationDate** *(datetime) --*

                The date the approval rule template was created, in timestamp format.

              - **lastModifiedUser** *(string) --*

                The Amazon Resource Name (ARN) of the user who made the most recent changes to the
                approval rule template.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_blob(self, repositoryName: str, blobId: str) -> ClientGetBlobResponseTypeDef:
        """
        Returns the base-64 encoded content of an individual blob in a repository.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/codecommit-2015-04-13/GetBlob>`_

        **Request Syntax**
        ::

          response = client.get_blob(
              repositoryName='string',
              blobId='string'
          )
        :type repositoryName: string
        :param repositoryName: **[REQUIRED]**

          The name of the repository that contains the blob.

        :type blobId: string
        :param blobId: **[REQUIRED]**

          The ID of the blob, which is its SHA-1 pointer.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'content': b'bytes'
            }
          **Response Structure**

          - *(dict) --*

            Represents the output of a get blob operation.

            - **content** *(bytes) --*

              The content of the blob, usually a file.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_branch(
        self, repositoryName: str = None, branchName: str = None
    ) -> ClientGetBranchResponseTypeDef:
        """
        Returns information about a repository branch, including its name and the last commit ID.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/codecommit-2015-04-13/GetBranch>`_

        **Request Syntax**
        ::

          response = client.get_branch(
              repositoryName='string',
              branchName='string'
          )
        :type repositoryName: string
        :param repositoryName:

          The name of the repository that contains the branch for which you want to retrieve
          information.

        :type branchName: string
        :param branchName:

          The name of the branch for which you want to retrieve information.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'branch': {
                    'branchName': 'string',
                    'commitId': 'string'
                }
            }
          **Response Structure**

          - *(dict) --*

            Represents the output of a get branch operation.

            - **branch** *(dict) --*

              The name of the branch.

              - **branchName** *(string) --*

                The name of the branch.

              - **commitId** *(string) --*

                The ID of the last commit made to the branch.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_comment(self, commentId: str) -> ClientGetCommentResponseTypeDef:
        """
        Returns the content of a comment made on a change, file, or commit in a repository.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/codecommit-2015-04-13/GetComment>`_

        **Request Syntax**
        ::

          response = client.get_comment(
              commentId='string'
          )
        :type commentId: string
        :param commentId: **[REQUIRED]**

          The unique, system-generated ID of the comment. To get this ID, use
          GetCommentsForComparedCommit or  GetCommentsForPullRequest .

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'comment': {
                    'commentId': 'string',
                    'content': 'string',
                    'inReplyTo': 'string',
                    'creationDate': datetime(2015, 1, 1),
                    'lastModifiedDate': datetime(2015, 1, 1),
                    'authorArn': 'string',
                    'deleted': True|False,
                    'clientRequestToken': 'string'
                }
            }
          **Response Structure**

          - *(dict) --*

            - **comment** *(dict) --*

              The contents of the comment.

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
                ensures the request cannot be repeated with a changed parameter. If a request is
                received with the same parameters and a token is included, the request returns
                information about the initial request that used that token.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_comments_for_compared_commit(
        self,
        repositoryName: str,
        afterCommitId: str,
        beforeCommitId: str = None,
        nextToken: str = None,
        maxResults: int = None,
    ) -> ClientGetCommentsForComparedCommitResponseTypeDef:
        """
        Returns information about comments made on the comparison between two commits.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/codecommit-2015-04-13/GetCommentsForComparedCommit>`_

        **Request Syntax**
        ::

          response = client.get_comments_for_compared_commit(
              repositoryName='string',
              beforeCommitId='string',
              afterCommitId='string',
              nextToken='string',
              maxResults=123
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

        :type nextToken: string
        :param nextToken:

          An enumeration token that when provided in a request, returns the next batch of the
          results.

        :type maxResults: integer
        :param maxResults:

          A non-zero, non-negative integer used to limit the number of returned results. The default
          is 100 comments, but you can configure up to 500.

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
                'nextToken': 'string'
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

            - **nextToken** *(string) --*

              An enumeration token that can be used in a request to return the next batch of the
              results.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_comments_for_pull_request(
        self,
        pullRequestId: str,
        repositoryName: str = None,
        beforeCommitId: str = None,
        afterCommitId: str = None,
        nextToken: str = None,
        maxResults: int = None,
    ) -> ClientGetCommentsForPullRequestResponseTypeDef:
        """
        Returns comments made on a pull request.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/codecommit-2015-04-13/GetCommentsForPullRequest>`_

        **Request Syntax**
        ::

          response = client.get_comments_for_pull_request(
              pullRequestId='string',
              repositoryName='string',
              beforeCommitId='string',
              afterCommitId='string',
              nextToken='string',
              maxResults=123
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

        :type nextToken: string
        :param nextToken:

          An enumeration token that, when provided in a request, returns the next batch of the
          results.

        :type maxResults: integer
        :param maxResults:

          A non-zero, non-negative integer used to limit the number of returned results. The default
          is 100 comments. You can return up to 500 comments with a single request.

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
                'nextToken': 'string'
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

            - **nextToken** *(string) --*

              An enumeration token that can be used in a request to return the next batch of the
              results.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_commit(self, repositoryName: str, commitId: str) -> ClientGetCommitResponseTypeDef:
        """
        Returns information about a commit, including commit message and committer information.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/codecommit-2015-04-13/GetCommit>`_

        **Request Syntax**
        ::

          response = client.get_commit(
              repositoryName='string',
              commitId='string'
          )
        :type repositoryName: string
        :param repositoryName: **[REQUIRED]**

          The name of the repository to which the commit was made.

        :type commitId: string
        :param commitId: **[REQUIRED]**

          The commit ID. Commit IDs are the full SHA ID of the commit.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'commit': {
                    'commitId': 'string',
                    'treeId': 'string',
                    'parents': [
                        'string',
                    ],
                    'message': 'string',
                    'author': {
                        'name': 'string',
                        'email': 'string',
                        'date': 'string'
                    },
                    'committer': {
                        'name': 'string',
                        'email': 'string',
                        'date': 'string'
                    },
                    'additionalData': 'string'
                }
            }
          **Response Structure**

          - *(dict) --*

            Represents the output of a get commit operation.

            - **commit** *(dict) --*

              A commit data type object that contains information about the specified commit.

              - **commitId** *(string) --*

                The full SHA ID of the specified commit.

              - **treeId** *(string) --*

                Tree information for the specified commit.

              - **parents** *(list) --*

                A list of parent commits for the specified commit. Each parent commit ID is the full
                commit ID.

                - *(string) --*

              - **message** *(string) --*

                The commit message associated with the specified commit.

              - **author** *(dict) --*

                Information about the author of the specified commit. Information includes the date
                in timestamp format with GMT offset, the name of the author, and the email address
                for the author, as configured in Git.

                - **name** *(string) --*

                  The name of the user who made the specified commit.

                - **email** *(string) --*

                  The email address associated with the user who made the commit, if any.

                - **date** *(string) --*

                  The date when the specified commit was commited, in timestamp format with GMT
                  offset.

              - **committer** *(dict) --*

                Information about the person who committed the specified commit, also known as the
                committer. Information includes the date in timestamp format with GMT offset, the
                name of the committer, and the email address for the committer, as configured in
                Git.

                For more information about the difference between an author and a committer in Git,
                see `Viewing the Commit History <http://git-scm.com/book/ch2-3.html>`__ in Pro Git
                by Scott Chacon and Ben Straub.

                - **name** *(string) --*

                  The name of the user who made the specified commit.

                - **email** *(string) --*

                  The email address associated with the user who made the commit, if any.

                - **date** *(string) --*

                  The date when the specified commit was commited, in timestamp format with GMT
                  offset.

              - **additionalData** *(string) --*

                Any other data associated with the specified commit.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_differences(
        self,
        repositoryName: str,
        afterCommitSpecifier: str,
        beforeCommitSpecifier: str = None,
        beforePath: str = None,
        afterPath: str = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> ClientGetDifferencesResponseTypeDef:
        """
        Returns information about the differences in a valid commit specifier (such as a branch,
        tag, HEAD, commit ID, or other fully qualified reference). Results can be limited to a
        specified path.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/codecommit-2015-04-13/GetDifferences>`_

        **Request Syntax**
        ::

          response = client.get_differences(
              repositoryName='string',
              beforeCommitSpecifier='string',
              afterCommitSpecifier='string',
              beforePath='string',
              afterPath='string',
              MaxResults=123,
              NextToken='string'
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

        :type MaxResults: integer
        :param MaxResults:

          A non-zero, non-negative integer used to limit the number of returned results.

        :type NextToken: string
        :param NextToken:

          An enumeration token that, when provided in a request, returns the next batch of the
          results.

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
                'NextToken': 'string'
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

            - **NextToken** *(string) --*

              An enumeration token that can be used in a request to return the next batch of the
              results.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_file(
        self, repositoryName: str, filePath: str, commitSpecifier: str = None
    ) -> ClientGetFileResponseTypeDef:
        """
        Returns the base-64 encoded contents of a specified file and its metadata.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/codecommit-2015-04-13/GetFile>`_

        **Request Syntax**
        ::

          response = client.get_file(
              repositoryName='string',
              commitSpecifier='string',
              filePath='string'
          )
        :type repositoryName: string
        :param repositoryName: **[REQUIRED]**

          The name of the repository that contains the file.

        :type commitSpecifier: string
        :param commitSpecifier:

          The fully quaified reference that identifies the commit that contains the file. For
          example, you can specify a full commit ID, a tag, a branch name, or a reference such as
          refs/heads/master. If none is provided, the head commit is used.

        :type filePath: string
        :param filePath: **[REQUIRED]**

          The fully qualified path to the file, including the full name and extension of the file.
          For example, /examples/file.md is the fully qualified path to a file named file.md in a
          folder named examples.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'commitId': 'string',
                'blobId': 'string',
                'filePath': 'string',
                'fileMode': 'EXECUTABLE'|'NORMAL'|'SYMLINK',
                'fileSize': 123,
                'fileContent': b'bytes'
            }
          **Response Structure**

          - *(dict) --*

            - **commitId** *(string) --*

              The full commit ID of the commit that contains the content returned by GetFile.

            - **blobId** *(string) --*

              The blob ID of the object that represents the file content.

            - **filePath** *(string) --*

              The fully qualified path to the specified file. Returns the name and extension of the
              file.

            - **fileMode** *(string) --*

              The extrapolated file mode permissions of the blob. Valid values include strings such
              as EXECUTABLE and not numeric values.

              .. note::

                The file mode permissions returned by this API are not the standard file mode
                permission values, such as 100644, but rather extrapolated values. See the supported
                return values.

            - **fileSize** *(integer) --*

              The size of the contents of the file, in bytes.

            - **fileContent** *(bytes) --*

              The base-64 encoded binary data object that represents the content of the file.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_folder(
        self, repositoryName: str, folderPath: str, commitSpecifier: str = None
    ) -> ClientGetFolderResponseTypeDef:
        """
        Returns the contents of a specified folder in a repository.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/codecommit-2015-04-13/GetFolder>`_

        **Request Syntax**
        ::

          response = client.get_folder(
              repositoryName='string',
              commitSpecifier='string',
              folderPath='string'
          )
        :type repositoryName: string
        :param repositoryName: **[REQUIRED]**

          The name of the repository.

        :type commitSpecifier: string
        :param commitSpecifier:

          A fully qualified reference used to identify a commit that contains the version of the
          folder's content to return. A fully qualified reference can be a commit ID, branch name,
          tag, or reference such as HEAD. If no specifier is provided, the folder content is
          returned as it exists in the HEAD commit.

        :type folderPath: string
        :param folderPath: **[REQUIRED]**

          The fully qualified path to the folder whose contents are returned, including the folder
          name. For example, /examples is a fully-qualified path to a folder named examples that was
          created off of the root directory (/) of a repository.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'commitId': 'string',
                'folderPath': 'string',
                'treeId': 'string',
                'subFolders': [
                    {
                        'treeId': 'string',
                        'absolutePath': 'string',
                        'relativePath': 'string'
                    },
                ],
                'files': [
                    {
                        'blobId': 'string',
                        'absolutePath': 'string',
                        'relativePath': 'string',
                        'fileMode': 'EXECUTABLE'|'NORMAL'|'SYMLINK'
                    },
                ],
                'symbolicLinks': [
                    {
                        'blobId': 'string',
                        'absolutePath': 'string',
                        'relativePath': 'string',
                        'fileMode': 'EXECUTABLE'|'NORMAL'|'SYMLINK'
                    },
                ],
                'subModules': [
                    {
                        'commitId': 'string',
                        'absolutePath': 'string',
                        'relativePath': 'string'
                    },
                ]
            }
          **Response Structure**

          - *(dict) --*

            - **commitId** *(string) --*

              The full commit ID used as a reference for the returned version of the folder content.

            - **folderPath** *(string) --*

              The fully qualified path of the folder whose contents are returned.

            - **treeId** *(string) --*

              The full SHA-1 pointer of the tree information for the commit that contains the
              folder.

            - **subFolders** *(list) --*

              The list of folders that exist under the specified folder, if any.

              - *(dict) --*

                Returns information about a folder in a repository.

                - **treeId** *(string) --*

                  The full SHA-1 pointer of the tree information for the commit that contains the
                  folder.

                - **absolutePath** *(string) --*

                  The fully qualified path of the folder in the repository.

                - **relativePath** *(string) --*

                  The relative path of the specified folder from the folder where the query
                  originated.

            - **files** *(list) --*

              The list of files in the specified folder, if any.

              - *(dict) --*

                Returns information about a file in a repository.

                - **blobId** *(string) --*

                  The blob ID that contains the file information.

                - **absolutePath** *(string) --*

                  The fully qualified path to the file in the repository.

                - **relativePath** *(string) --*

                  The relative path of the file from the folder where the query originated.

                - **fileMode** *(string) --*

                  The extrapolated file mode permissions for the file. Valid values include
                  EXECUTABLE and NORMAL.

            - **symbolicLinks** *(list) --*

              The list of symbolic links to other files and folders in the specified folder, if any.

              - *(dict) --*

                Returns information about a symbolic link in a repository folder.

                - **blobId** *(string) --*

                  The blob ID that contains the information about the symbolic link.

                - **absolutePath** *(string) --*

                  The fully qualified path to the folder that contains the symbolic link.

                - **relativePath** *(string) --*

                  The relative path of the symbolic link from the folder where the query originated.

                - **fileMode** *(string) --*

                  The file mode permissions of the blob that cotains information about the symbolic
                  link.

            - **subModules** *(list) --*

              The list of submodules in the specified folder, if any.

              - *(dict) --*

                Returns information about a submodule reference in a repository folder.

                - **commitId** *(string) --*

                  The commit ID that contains the reference to the submodule.

                - **absolutePath** *(string) --*

                  The fully qualified path to the folder that contains the reference to the
                  submodule.

                - **relativePath** *(string) --*

                  The relative path of the submodule from the folder where the query originated.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_merge_commit(
        self,
        repositoryName: str,
        sourceCommitSpecifier: str,
        destinationCommitSpecifier: str,
        conflictDetailLevel: Literal["FILE_LEVEL", "LINE_LEVEL"] = None,
        conflictResolutionStrategy: Literal[
            "NONE", "ACCEPT_SOURCE", "ACCEPT_DESTINATION", "AUTOMERGE"
        ] = None,
    ) -> ClientGetMergeCommitResponseTypeDef:
        """
        Returns information about a specified merge commit.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/codecommit-2015-04-13/GetMergeCommit>`_

        **Request Syntax**
        ::

          response = client.get_merge_commit(
              repositoryName='string',
              sourceCommitSpecifier='string',
              destinationCommitSpecifier='string',
              conflictDetailLevel='FILE_LEVEL'|'LINE_LEVEL',
              conflictResolutionStrategy='NONE'|'ACCEPT_SOURCE'|'ACCEPT_DESTINATION'|'AUTOMERGE'
          )
        :type repositoryName: string
        :param repositoryName: **[REQUIRED]**

          The name of the repository that contains the merge commit about which you want to get
          information.

        :type sourceCommitSpecifier: string
        :param sourceCommitSpecifier: **[REQUIRED]**

          The branch, tag, HEAD, or other fully qualified reference used to identify a commit (for
          example, a branch name or a full commit ID).

        :type destinationCommitSpecifier: string
        :param destinationCommitSpecifier: **[REQUIRED]**

          The branch, tag, HEAD, or other fully qualified reference used to identify a commit (for
          example, a branch name or a full commit ID).

        :type conflictDetailLevel: string
        :param conflictDetailLevel:

          The level of conflict detail to use. If unspecified, the default FILE_LEVEL is used, which
          returns a not-mergeable result if the same file has differences in both branches. If
          LINE_LEVEL is specified, a conflict is considered not mergeable if the same file in both
          branches has differences on the same line.

        :type conflictResolutionStrategy: string
        :param conflictResolutionStrategy:

          Specifies which branch to use when resolving conflicts, or whether to attempt
          automatically merging two versions of a file. The default is NONE, which requires any
          conflicts to be resolved manually before the merge operation is successful.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'sourceCommitId': 'string',
                'destinationCommitId': 'string',
                'baseCommitId': 'string',
                'mergedCommitId': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **sourceCommitId** *(string) --*

              The commit ID of the source commit specifier that was used in the merge evaluation.

            - **destinationCommitId** *(string) --*

              The commit ID of the destination commit specifier that was used in the merge
              evaluation.

            - **baseCommitId** *(string) --*

              The commit ID of the merge base.

            - **mergedCommitId** *(string) --*

              The commit ID for the merge commit created when the source branch was merged into the
              destination branch. If the fast-forward merge strategy was used, there is no merge
              commit.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_merge_conflicts(
        self,
        repositoryName: str,
        destinationCommitSpecifier: str,
        sourceCommitSpecifier: str,
        mergeOption: Literal["FAST_FORWARD_MERGE", "SQUASH_MERGE", "THREE_WAY_MERGE"],
        conflictDetailLevel: Literal["FILE_LEVEL", "LINE_LEVEL"] = None,
        maxConflictFiles: int = None,
        conflictResolutionStrategy: Literal[
            "NONE", "ACCEPT_SOURCE", "ACCEPT_DESTINATION", "AUTOMERGE"
        ] = None,
        nextToken: str = None,
    ) -> ClientGetMergeConflictsResponseTypeDef:
        """
        Returns information about merge conflicts between the before and after commit IDs for a pull
        request in a repository.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/codecommit-2015-04-13/GetMergeConflicts>`_

        **Request Syntax**
        ::

          response = client.get_merge_conflicts(
              repositoryName='string',
              destinationCommitSpecifier='string',
              sourceCommitSpecifier='string',
              mergeOption='FAST_FORWARD_MERGE'|'SQUASH_MERGE'|'THREE_WAY_MERGE',
              conflictDetailLevel='FILE_LEVEL'|'LINE_LEVEL',
              maxConflictFiles=123,
              conflictResolutionStrategy='NONE'|'ACCEPT_SOURCE'|'ACCEPT_DESTINATION'|'AUTOMERGE',
              nextToken='string'
          )
        :type repositoryName: string
        :param repositoryName: **[REQUIRED]**

          The name of the repository where the pull request was created.

        :type destinationCommitSpecifier: string
        :param destinationCommitSpecifier: **[REQUIRED]**

          The branch, tag, HEAD, or other fully qualified reference used to identify a commit (for
          example, a branch name or a full commit ID).

        :type sourceCommitSpecifier: string
        :param sourceCommitSpecifier: **[REQUIRED]**

          The branch, tag, HEAD, or other fully qualified reference used to identify a commit (for
          example, a branch name or a full commit ID).

        :type mergeOption: string
        :param mergeOption: **[REQUIRED]**

          The merge option or strategy you want to use to merge the code.

        :type conflictDetailLevel: string
        :param conflictDetailLevel:

          The level of conflict detail to use. If unspecified, the default FILE_LEVEL is used, which
          returns a not-mergeable result if the same file has differences in both branches. If
          LINE_LEVEL is specified, a conflict is considered not mergeable if the same file in both
          branches has differences on the same line.

        :type maxConflictFiles: integer
        :param maxConflictFiles:

          The maximum number of files to include in the output.

        :type conflictResolutionStrategy: string
        :param conflictResolutionStrategy:

          Specifies which branch to use when resolving conflicts, or whether to attempt
          automatically merging two versions of a file. The default is NONE, which requires any
          conflicts to be resolved manually before the merge operation is successful.

        :type nextToken: string
        :param nextToken:

          An enumeration token that, when provided in a request, returns the next batch of the
          results.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'mergeable': True|False,
                'destinationCommitId': 'string',
                'sourceCommitId': 'string',
                'baseCommitId': 'string',
                'conflictMetadataList': [
                    {
                        'filePath': 'string',
                        'fileSizes': {
                            'source': 123,
                            'destination': 123,
                            'base': 123
                        },
                        'fileModes': {
                            'source': 'EXECUTABLE'|'NORMAL'|'SYMLINK',
                            'destination': 'EXECUTABLE'|'NORMAL'|'SYMLINK',
                            'base': 'EXECUTABLE'|'NORMAL'|'SYMLINK'
                        },
                        'objectTypes': {
                            'source': 'FILE'|'DIRECTORY'|'GIT_LINK'|'SYMBOLIC_LINK',
                            'destination': 'FILE'|'DIRECTORY'|'GIT_LINK'|'SYMBOLIC_LINK',
                            'base': 'FILE'|'DIRECTORY'|'GIT_LINK'|'SYMBOLIC_LINK'
                        },
                        'numberOfConflicts': 123,
                        'isBinaryFile': {
                            'source': True|False,
                            'destination': True|False,
                            'base': True|False
                        },
                        'contentConflict': True|False,
                        'fileModeConflict': True|False,
                        'objectTypeConflict': True|False,
                        'mergeOperations': {
                            'source': 'A'|'M'|'D',
                            'destination': 'A'|'M'|'D'
                        }
                    },
                ],
                'nextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **mergeable** *(boolean) --*

              A Boolean value that indicates whether the code is mergeable by the specified merge
              option.

            - **destinationCommitId** *(string) --*

              The commit ID of the destination commit specifier that was used in the merge
              evaluation.

            - **sourceCommitId** *(string) --*

              The commit ID of the source commit specifier that was used in the merge evaluation.

            - **baseCommitId** *(string) --*

              The commit ID of the merge base.

            - **conflictMetadataList** *(list) --*

              A list of metadata for any conflicting files. If the specified merge strategy is
              FAST_FORWARD_MERGE, this list is always empty.

              - *(dict) --*

                Information about the metadata for a conflict in a merge operation.

                - **filePath** *(string) --*

                  The path of the file that contains conflicts.

                - **fileSizes** *(dict) --*

                  The file sizes of the file in the source, destination, and base of the merge.

                  - **source** *(integer) --*

                    The size of a file in the source of a merge or pull request.

                  - **destination** *(integer) --*

                    The size of a file in the destination of a merge or pull request.

                  - **base** *(integer) --*

                    The size of a file in the base of a merge or pull request.

                - **fileModes** *(dict) --*

                  The file modes of the file in the source, destination, and base of the merge.

                  - **source** *(string) --*

                    The file mode of a file in the source of a merge or pull request.

                  - **destination** *(string) --*

                    The file mode of a file in the destination of a merge or pull request.

                  - **base** *(string) --*

                    The file mode of a file in the base of a merge or pull request.

                - **objectTypes** *(dict) --*

                  Information about any object type conflicts in a merge operation.

                  - **source** *(string) --*

                    The type of the object in the source branch.

                  - **destination** *(string) --*

                    The type of the object in the destination branch.

                  - **base** *(string) --*

                    The type of the object in the base commit of the merge.

                - **numberOfConflicts** *(integer) --*

                  The number of conflicts, including both hunk conflicts and metadata conflicts.

                - **isBinaryFile** *(dict) --*

                  A boolean value (true or false) indicating whether the file is binary or textual
                  in the source, destination, and base of the merge.

                  - **source** *(boolean) --*

                    The binary or non-binary status of file in the source of a merge or pull
                    request.

                  - **destination** *(boolean) --*

                    The binary or non-binary status of a file in the destination of a merge or pull
                    request.

                  - **base** *(boolean) --*

                    The binary or non-binary status of a file in the base of a merge or pull
                    request.

                - **contentConflict** *(boolean) --*

                  A boolean value indicating whether there are conflicts in the content of a file.

                - **fileModeConflict** *(boolean) --*

                  A boolean value indicating whether there are conflicts in the file mode of a file.

                - **objectTypeConflict** *(boolean) --*

                  A boolean value (true or false) indicating whether there are conflicts between the
                  branches in the object type of a file, folder, or submodule.

                - **mergeOperations** *(dict) --*

                  Whether an add, modify, or delete operation caused the conflict between the source
                  and destination of the merge.

                  - **source** *(string) --*

                    The operation (add, modify, or delete) on a file in the source of a merge or
                    pull request.

                  - **destination** *(string) --*

                    The operation on a file in the destination of a merge or pull request.

            - **nextToken** *(string) --*

              An enumeration token that can be used in a request to return the next batch of the
              results.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_merge_options(
        self,
        repositoryName: str,
        sourceCommitSpecifier: str,
        destinationCommitSpecifier: str,
        conflictDetailLevel: Literal["FILE_LEVEL", "LINE_LEVEL"] = None,
        conflictResolutionStrategy: Literal[
            "NONE", "ACCEPT_SOURCE", "ACCEPT_DESTINATION", "AUTOMERGE"
        ] = None,
    ) -> ClientGetMergeOptionsResponseTypeDef:
        """
        Returns information about the merge options available for merging two specified branches.
        For details about why a merge option is not available, use GetMergeConflicts or
        DescribeMergeConflicts.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/codecommit-2015-04-13/GetMergeOptions>`_

        **Request Syntax**
        ::

          response = client.get_merge_options(
              repositoryName='string',
              sourceCommitSpecifier='string',
              destinationCommitSpecifier='string',
              conflictDetailLevel='FILE_LEVEL'|'LINE_LEVEL',
              conflictResolutionStrategy='NONE'|'ACCEPT_SOURCE'|'ACCEPT_DESTINATION'|'AUTOMERGE'
          )
        :type repositoryName: string
        :param repositoryName: **[REQUIRED]**

          The name of the repository that contains the commits about which you want to get merge
          options.

        :type sourceCommitSpecifier: string
        :param sourceCommitSpecifier: **[REQUIRED]**

          The branch, tag, HEAD, or other fully qualified reference used to identify a commit (for
          example, a branch name or a full commit ID).

        :type destinationCommitSpecifier: string
        :param destinationCommitSpecifier: **[REQUIRED]**

          The branch, tag, HEAD, or other fully qualified reference used to identify a commit (for
          example, a branch name or a full commit ID).

        :type conflictDetailLevel: string
        :param conflictDetailLevel:

          The level of conflict detail to use. If unspecified, the default FILE_LEVEL is used, which
          returns a not-mergeable result if the same file has differences in both branches. If
          LINE_LEVEL is specified, a conflict is considered not mergeable if the same file in both
          branches has differences on the same line.

        :type conflictResolutionStrategy: string
        :param conflictResolutionStrategy:

          Specifies which branch to use when resolving conflicts, or whether to attempt
          automatically merging two versions of a file. The default is NONE, which requires any
          conflicts to be resolved manually before the merge operation is successful.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'mergeOptions': [
                    'FAST_FORWARD_MERGE'|'SQUASH_MERGE'|'THREE_WAY_MERGE',
                ],
                'sourceCommitId': 'string',
                'destinationCommitId': 'string',
                'baseCommitId': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **mergeOptions** *(list) --*

              The merge option or strategy used to merge the code.

              - *(string) --*

            - **sourceCommitId** *(string) --*

              The commit ID of the source commit specifier that was used in the merge evaluation.

            - **destinationCommitId** *(string) --*

              The commit ID of the destination commit specifier that was used in the merge
              evaluation.

            - **baseCommitId** *(string) --*

              The commit ID of the merge base.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_pull_request(self, pullRequestId: str) -> ClientGetPullRequestResponseTypeDef:
        """
        Gets information about a pull request in a specified repository.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/codecommit-2015-04-13/GetPullRequest>`_

        **Request Syntax**
        ::

          response = client.get_pull_request(
              pullRequestId='string'
          )
        :type pullRequestId: string
        :param pullRequestId: **[REQUIRED]**

          The system-generated ID of the pull request. To get this ID, use  ListPullRequests .

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'pullRequest': {
                    'pullRequestId': 'string',
                    'title': 'string',
                    'description': 'string',
                    'lastActivityDate': datetime(2015, 1, 1),
                    'creationDate': datetime(2015, 1, 1),
                    'pullRequestStatus': 'OPEN'|'CLOSED',
                    'authorArn': 'string',
                    'pullRequestTargets': [
                        {
                            'repositoryName': 'string',
                            'sourceReference': 'string',
                            'destinationReference': 'string',
                            'destinationCommit': 'string',
                            'sourceCommit': 'string',
                            'mergeBase': 'string',
                            'mergeMetadata': {
                                'isMerged': True|False,
                                'mergedBy': 'string',
                                'mergeCommitId': 'string',
                                'mergeOption': 'FAST_FORWARD_MERGE'|'SQUASH_MERGE'|'THREE_WAY_MERGE'
                            }
                        },
                    ],
                    'clientRequestToken': 'string',
                    'revisionId': 'string',
                    'approvalRules': [
                        {
                            'approvalRuleId': 'string',
                            'approvalRuleName': 'string',
                            'approvalRuleContent': 'string',
                            'ruleContentSha256': 'string',
                            'lastModifiedDate': datetime(2015, 1, 1),
                            'creationDate': datetime(2015, 1, 1),
                            'lastModifiedUser': 'string',
                            'originApprovalRuleTemplate': {
                                'approvalRuleTemplateId': 'string',
                                'approvalRuleTemplateName': 'string'
                            }
                        },
                    ]
                }
            }
          **Response Structure**

          - *(dict) --*

            - **pullRequest** *(dict) --*

              Information about the specified pull request.

              - **pullRequestId** *(string) --*

                The system-generated ID of the pull request.

              - **title** *(string) --*

                The user-defined title of the pull request. This title is displayed in the list of
                pull requests to other repository users.

              - **description** *(string) --*

                The user-defined description of the pull request. This description can be used to
                clarify what should be reviewed and other details of the request.

              - **lastActivityDate** *(datetime) --*

                The day and time of the last user or system activity on the pull request, in
                timestamp format.

              - **creationDate** *(datetime) --*

                The date and time the pull request was originally created, in timestamp format.

              - **pullRequestStatus** *(string) --*

                The status of the pull request. Pull request status can only change from ``OPEN`` to
                ``CLOSED`` .

              - **authorArn** *(string) --*

                The Amazon Resource Name (ARN) of the user who created the pull request.

              - **pullRequestTargets** *(list) --*

                The targets of the pull request, including the source branch and destination branch
                for the pull request.

                - *(dict) --*

                  Returns information about a pull request target.

                  - **repositoryName** *(string) --*

                    The name of the repository that contains the pull request source and destination
                    branches.

                  - **sourceReference** *(string) --*

                    The branch of the repository that contains the changes for the pull request.
                    Also known as the source branch.

                  - **destinationReference** *(string) --*

                    The branch of the repository where the pull request changes are merged. Also
                    known as the destination branch.

                  - **destinationCommit** *(string) --*

                    The full commit ID that is the tip of the destination branch. This is the commit
                    where the pull request was or will be merged.

                  - **sourceCommit** *(string) --*

                    The full commit ID of the tip of the source branch used to create the pull
                    request. If the pull request branch is updated by a push while the pull request
                    is open, the commit ID changes to reflect the new tip of the branch.

                  - **mergeBase** *(string) --*

                    The commit ID of the most recent commit that the source branch and the
                    destination branch have in common.

                  - **mergeMetadata** *(dict) --*

                    Returns metadata about the state of the merge, including whether the merge has
                    been made.

                    - **isMerged** *(boolean) --*

                      A Boolean value indicating whether the merge has been made.

                    - **mergedBy** *(string) --*

                      The Amazon Resource Name (ARN) of the user who merged the branches.

                    - **mergeCommitId** *(string) --*

                      The commit ID for the merge commit, if any.

                    - **mergeOption** *(string) --*

                      The merge strategy used in the merge.

              - **clientRequestToken** *(string) --*

                A unique, client-generated idempotency token that, when provided in a request,
                ensures the request cannot be repeated with a changed parameter. If a request is
                received with the same parameters and a token is included, the request returns
                information about the initial request that used that token.

              - **revisionId** *(string) --*

                The system-generated revision ID for the pull request.

              - **approvalRules** *(list) --*

                The approval rules applied to the pull request.

                - *(dict) --*

                  Returns information about an approval rule.

                  - **approvalRuleId** *(string) --*

                    The system-generated ID of the approval rule.

                  - **approvalRuleName** *(string) --*

                    The name of the approval rule.

                  - **approvalRuleContent** *(string) --*

                    The content of the approval rule.

                  - **ruleContentSha256** *(string) --*

                    The SHA-256 hash signature for the content of the approval rule.

                  - **lastModifiedDate** *(datetime) --*

                    The date the approval rule was most recently changed, in timestamp format.

                  - **creationDate** *(datetime) --*

                    The date the approval rule was created, in timestamp format.

                  - **lastModifiedUser** *(string) --*

                    The Amazon Resource Name (ARN) of the user who made the most recent changes to
                    the approval rule.

                  - **originApprovalRuleTemplate** *(dict) --*

                    The approval rule template used to create the rule.

                    - **approvalRuleTemplateId** *(string) --*

                      The ID of the template that created the approval rule.

                    - **approvalRuleTemplateName** *(string) --*

                      The name of the template that created the approval rule.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_pull_request_approval_states(
        self, pullRequestId: str, revisionId: str
    ) -> ClientGetPullRequestApprovalStatesResponseTypeDef:
        """
        Gets information about the approval states for a specified pull request. Approval states
        only apply to pull requests that have one or more approval rules applied to them.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/codecommit-2015-04-13/GetPullRequestApprovalStates>`_

        **Request Syntax**
        ::

          response = client.get_pull_request_approval_states(
              pullRequestId='string',
              revisionId='string'
          )
        :type pullRequestId: string
        :param pullRequestId: **[REQUIRED]**

          The system-generated ID for the pull request.

        :type revisionId: string
        :param revisionId: **[REQUIRED]**

          The system-generated ID for the pull request revision.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'approvals': [
                    {
                        'userArn': 'string',
                        'approvalState': 'APPROVE'|'REVOKE'
                    },
                ]
            }
          **Response Structure**

          - *(dict) --*

            - **approvals** *(list) --*

              Information about users who have approved the pull request.

              - *(dict) --*

                Returns information about a specific approval on a pull request.

                - **userArn** *(string) --*

                  The Amazon Resource Name (ARN) of the user.

                - **approvalState** *(string) --*

                  The state of the approval, APPROVE or REVOKE. REVOKE states are not stored.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_pull_request_override_state(
        self, pullRequestId: str, revisionId: str
    ) -> ClientGetPullRequestOverrideStateResponseTypeDef:
        """
        Returns information about whether approval rules have been set aside (overridden) for a pull
        request, and if so, the Amazon Resource Name (ARN) of the user or identity that overrode the
        rules and their requirements for the pull request.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/codecommit-2015-04-13/GetPullRequestOverrideState>`_

        **Request Syntax**
        ::

          response = client.get_pull_request_override_state(
              pullRequestId='string',
              revisionId='string'
          )
        :type pullRequestId: string
        :param pullRequestId: **[REQUIRED]**

          The ID of the pull request for which you want to get information about whether approval
          rules have been set aside (overridden).

        :type revisionId: string
        :param revisionId: **[REQUIRED]**

          The system-generated ID of the revision for the pull request. To retrieve the most recent
          revision ID, use  GetPullRequest .

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'overridden': True|False,
                'overrider': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **overridden** *(boolean) --*

              A Boolean value that indicates whether a pull request has had its rules set aside
              (TRUE) or whether all approval rules still apply (FALSE).

            - **overrider** *(string) --*

              The Amazon Resource Name (ARN) of the user or identity that overrode the rules and
              their requirements for the pull request.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_repository(self, repositoryName: str) -> ClientGetRepositoryResponseTypeDef:
        """
        Returns information about a repository.

        .. note::

          The description field for a repository accepts all HTML characters and all valid Unicode
          characters. Applications that do not HTML-encode the description and display it in a
          webpage can expose users to potentially malicious code. Make sure that you HTML-encode the
          description field in any application that uses this API to display the repository
          description on a webpage.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/codecommit-2015-04-13/GetRepository>`_

        **Request Syntax**
        ::

          response = client.get_repository(
              repositoryName='string'
          )
        :type repositoryName: string
        :param repositoryName: **[REQUIRED]**

          The name of the repository to get information about.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'repositoryMetadata': {
                    'accountId': 'string',
                    'repositoryId': 'string',
                    'repositoryName': 'string',
                    'repositoryDescription': 'string',
                    'defaultBranch': 'string',
                    'lastModifiedDate': datetime(2015, 1, 1),
                    'creationDate': datetime(2015, 1, 1),
                    'cloneUrlHttp': 'string',
                    'cloneUrlSsh': 'string',
                    'Arn': 'string'
                }
            }
          **Response Structure**

          - *(dict) --*

            Represents the output of a get repository operation.

            - **repositoryMetadata** *(dict) --*

              Information about the repository.

              - **accountId** *(string) --*

                The ID of the AWS account associated with the repository.

              - **repositoryId** *(string) --*

                The ID of the repository.

              - **repositoryName** *(string) --*

                The repository's name.

              - **repositoryDescription** *(string) --*

                A comment or description about the repository.

              - **defaultBranch** *(string) --*

                The repository's default branch name.

              - **lastModifiedDate** *(datetime) --*

                The date and time the repository was last modified, in timestamp format.

              - **creationDate** *(datetime) --*

                The date and time the repository was created, in timestamp format.

              - **cloneUrlHttp** *(string) --*

                The URL to use for cloning the repository over HTTPS.

              - **cloneUrlSsh** *(string) --*

                The URL to use for cloning the repository over SSH.

              - **Arn** *(string) --*

                The Amazon Resource Name (ARN) of the repository.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_repository_triggers(
        self, repositoryName: str
    ) -> ClientGetRepositoryTriggersResponseTypeDef:
        """
        Gets information about triggers configured for a repository.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/codecommit-2015-04-13/GetRepositoryTriggers>`_

        **Request Syntax**
        ::

          response = client.get_repository_triggers(
              repositoryName='string'
          )
        :type repositoryName: string
        :param repositoryName: **[REQUIRED]**

          The name of the repository for which the trigger is configured.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'configurationId': 'string',
                'triggers': [
                    {
                        'name': 'string',
                        'destinationArn': 'string',
                        'customData': 'string',
                        'branches': [
                            'string',
                        ],
                        'events': [
                            'all'|'updateReference'|'createReference'|'deleteReference',
                        ]
                    },
                ]
            }
          **Response Structure**

          - *(dict) --*

            Represents the output of a get repository triggers operation.

            - **configurationId** *(string) --*

              The system-generated unique ID for the trigger.

            - **triggers** *(list) --*

              The JSON block of configuration information for each trigger.

              - *(dict) --*

                Information about a trigger for a repository.

                - **name** *(string) --*

                  The name of the trigger.

                - **destinationArn** *(string) --*

                  The ARN of the resource that is the target for a trigger (for example, the ARN of
                  a topic in Amazon SNS).

                - **customData** *(string) --*

                  Any custom data associated with the trigger to be included in the information sent
                  to the target of the trigger.

                - **branches** *(list) --*

                  The branches to be included in the trigger configuration. If you specify an empty
                  array, the trigger applies to all branches.

                  .. note::

                    Although no content is required in the array, you must include the array itself.

                  - *(string) --*

                - **events** *(list) --*

                  The repository events that cause the trigger to run actions in another service,
                  such as sending a notification through Amazon SNS.

                  .. note::

                    The valid value "all" cannot be used with any other values.

                  - *(string) --*
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_approval_rule_templates(
        self, nextToken: str = None, maxResults: int = None
    ) -> ClientListApprovalRuleTemplatesResponseTypeDef:
        """
        Lists all approval rule templates in the specified AWS Region in your AWS account. If an AWS
        Region is not specified, the AWS Region where you are signed in is used.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/codecommit-2015-04-13/ListApprovalRuleTemplates>`_

        **Request Syntax**
        ::

          response = client.list_approval_rule_templates(
              nextToken='string',
              maxResults=123
          )
        :type nextToken: string
        :param nextToken:

          An enumeration token that, when provided in a request, returns the next batch of the
          results.

        :type maxResults: integer
        :param maxResults:

          A non-zero, non-negative integer used to limit the number of returned results.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'approvalRuleTemplateNames': [
                    'string',
                ],
                'nextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **approvalRuleTemplateNames** *(list) --*

              The names of all the approval rule templates found in the AWS Region for your AWS
              account.

              - *(string) --*

            - **nextToken** *(string) --*

              An enumeration token that allows the operation to batch the next results of the
              operation.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_associated_approval_rule_templates_for_repository(
        self, repositoryName: str, nextToken: str = None, maxResults: int = None
    ) -> ClientListAssociatedApprovalRuleTemplatesForRepositoryResponseTypeDef:
        """
        Lists all approval rule templates that are associated with a specified repository.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/codecommit-2015-04-13/ListAssociatedApprovalRuleTemplatesForRepository>`_

        **Request Syntax**
        ::

          response = client.list_associated_approval_rule_templates_for_repository(
              repositoryName='string',
              nextToken='string',
              maxResults=123
          )
        :type repositoryName: string
        :param repositoryName: **[REQUIRED]**

          The name of the repository for which you want to list all associated approval rule
          templates.

        :type nextToken: string
        :param nextToken:

          An enumeration token that, when provided in a request, returns the next batch of the
          results.

        :type maxResults: integer
        :param maxResults:

          A non-zero, non-negative integer used to limit the number of returned results.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'approvalRuleTemplateNames': [
                    'string',
                ],
                'nextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **approvalRuleTemplateNames** *(list) --*

              The names of all approval rule templates associated with the repository.

              - *(string) --*

            - **nextToken** *(string) --*

              An enumeration token that allows the operation to batch the next results of the
              operation.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_branches(
        self, repositoryName: str, nextToken: str = None
    ) -> ClientListBranchesResponseTypeDef:
        """
        Gets information about one or more branches in a repository.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/codecommit-2015-04-13/ListBranches>`_

        **Request Syntax**
        ::

          response = client.list_branches(
              repositoryName='string',
              nextToken='string'
          )
        :type repositoryName: string
        :param repositoryName: **[REQUIRED]**

          The name of the repository that contains the branches.

        :type nextToken: string
        :param nextToken:

          An enumeration token that allows the operation to batch the results.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'branches': [
                    'string',
                ],
                'nextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            Represents the output of a list branches operation.

            - **branches** *(list) --*

              The list of branch names.

              - *(string) --*

            - **nextToken** *(string) --*

              An enumeration token that returns the batch of the results.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_pull_requests(
        self,
        repositoryName: str,
        authorArn: str = None,
        pullRequestStatus: Literal["OPEN", "CLOSED"] = None,
        nextToken: str = None,
        maxResults: int = None,
    ) -> ClientListPullRequestsResponseTypeDef:
        """
        Returns a list of pull requests for a specified repository. The return list can be refined
        by pull request status or pull request author ARN.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/codecommit-2015-04-13/ListPullRequests>`_

        **Request Syntax**
        ::

          response = client.list_pull_requests(
              repositoryName='string',
              authorArn='string',
              pullRequestStatus='OPEN'|'CLOSED',
              nextToken='string',
              maxResults=123
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

        :type nextToken: string
        :param nextToken:

          An enumeration token that, when provided in a request, returns the next batch of the
          results.

        :type maxResults: integer
        :param maxResults:

          A non-zero, non-negative integer used to limit the number of returned results.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'pullRequestIds': [
                    'string',
                ],
                'nextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **pullRequestIds** *(list) --*

              The system-generated IDs of the pull requests.

              - *(string) --*

            - **nextToken** *(string) --*

              An enumeration token that allows the operation to batch the next results of the
              operation.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_repositories(
        self,
        nextToken: str = None,
        sortBy: Literal["repositoryName", "lastModifiedDate"] = None,
        order: Literal["ascending", "descending"] = None,
    ) -> ClientListRepositoriesResponseTypeDef:
        """
        Gets information about one or more repositories.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/codecommit-2015-04-13/ListRepositories>`_

        **Request Syntax**
        ::

          response = client.list_repositories(
              nextToken='string',
              sortBy='repositoryName'|'lastModifiedDate',
              order='ascending'|'descending'
          )
        :type nextToken: string
        :param nextToken:

          An enumeration token that allows the operation to batch the results of the operation.
          Batch sizes are 1,000 for list repository operations. When the client sends the token back
          to AWS CodeCommit, another page of 1,000 records is retrieved.

        :type sortBy: string
        :param sortBy:

          The criteria used to sort the results of a list repositories operation.

        :type order: string
        :param order:

          The order in which to sort the results of a list repositories operation.

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
                'nextToken': 'string'
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

            - **nextToken** *(string) --*

              An enumeration token that allows the operation to batch the results of the operation.
              Batch sizes are 1,000 for list repository operations. When the client sends the token
              back to AWS CodeCommit, another page of 1,000 records is retrieved.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_repositories_for_approval_rule_template(
        self, approvalRuleTemplateName: str, nextToken: str = None, maxResults: int = None
    ) -> ClientListRepositoriesForApprovalRuleTemplateResponseTypeDef:
        """
        Lists all repositories associated with the specified approval rule template.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/codecommit-2015-04-13/ListRepositoriesForApprovalRuleTemplate>`_

        **Request Syntax**
        ::

          response = client.list_repositories_for_approval_rule_template(
              approvalRuleTemplateName='string',
              nextToken='string',
              maxResults=123
          )
        :type approvalRuleTemplateName: string
        :param approvalRuleTemplateName: **[REQUIRED]**

          The name of the approval rule template for which you want to list repositories that are
          associated with that template.

        :type nextToken: string
        :param nextToken:

          An enumeration token that, when provided in a request, returns the next batch of the
          results.

        :type maxResults: integer
        :param maxResults:

          A non-zero, non-negative integer used to limit the number of returned results.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'repositoryNames': [
                    'string',
                ],
                'nextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **repositoryNames** *(list) --*

              A list of repository names that are associated with the specified approval rule
              template.

              - *(string) --*

            - **nextToken** *(string) --*

              An enumeration token that allows the operation to batch the next results of the
              operation.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_tags_for_resource(
        self, resourceArn: str, nextToken: str = None
    ) -> ClientListTagsForResourceResponseTypeDef:
        """
        Gets information about AWS tags for a specified Amazon Resource Name (ARN) in AWS
        CodeCommit. For a list of valid resources in AWS CodeCommit, see `CodeCommit Resources and
        Operations
        <https://docs.aws.amazon.com/codecommit/latest/userguide/auth-and-access-control-iam-access-control-identity-based.html#arn-formats>`__
        in the*AWS CodeCommit User Guide* .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/codecommit-2015-04-13/ListTagsForResource>`_

        **Request Syntax**
        ::

          response = client.list_tags_for_resource(
              resourceArn='string',
              nextToken='string'
          )
        :type resourceArn: string
        :param resourceArn: **[REQUIRED]**

          The Amazon Resource Name (ARN) of the resource for which you want to get information about
          tags, if any.

        :type nextToken: string
        :param nextToken:

          An enumeration token that, when provided in a request, returns the next batch of the
          results.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'tags': {
                    'string': 'string'
                },
                'nextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **tags** *(dict) --*

              A list of tag key and value pairs associated with the specified resource.

              - *(string) --*

                - *(string) --*

            - **nextToken** *(string) --*

              An enumeration token that allows the operation to batch the next results of the
              operation.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def merge_branches_by_fast_forward(
        self,
        repositoryName: str,
        sourceCommitSpecifier: str,
        destinationCommitSpecifier: str,
        targetBranch: str = None,
    ) -> ClientMergeBranchesByFastForwardResponseTypeDef:
        """
        Merges two branches using the fast-forward merge strategy.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/codecommit-2015-04-13/MergeBranchesByFastForward>`_

        **Request Syntax**
        ::

          response = client.merge_branches_by_fast_forward(
              repositoryName='string',
              sourceCommitSpecifier='string',
              destinationCommitSpecifier='string',
              targetBranch='string'
          )
        :type repositoryName: string
        :param repositoryName: **[REQUIRED]**

          The name of the repository where you want to merge two branches.

        :type sourceCommitSpecifier: string
        :param sourceCommitSpecifier: **[REQUIRED]**

          The branch, tag, HEAD, or other fully qualified reference used to identify a commit (for
          example, a branch name or a full commit ID).

        :type destinationCommitSpecifier: string
        :param destinationCommitSpecifier: **[REQUIRED]**

          The branch, tag, HEAD, or other fully qualified reference used to identify a commit (for
          example, a branch name or a full commit ID).

        :type targetBranch: string
        :param targetBranch:

          The branch where the merge is applied.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'commitId': 'string',
                'treeId': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **commitId** *(string) --*

              The commit ID of the merge in the destination or target branch.

            - **treeId** *(string) --*

              The tree ID of the merge in the destination or target branch.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def merge_branches_by_squash(
        self,
        repositoryName: str,
        sourceCommitSpecifier: str,
        destinationCommitSpecifier: str,
        targetBranch: str = None,
        conflictDetailLevel: Literal["FILE_LEVEL", "LINE_LEVEL"] = None,
        conflictResolutionStrategy: Literal[
            "NONE", "ACCEPT_SOURCE", "ACCEPT_DESTINATION", "AUTOMERGE"
        ] = None,
        authorName: str = None,
        email: str = None,
        commitMessage: str = None,
        keepEmptyFolders: bool = None,
        conflictResolution: ClientMergeBranchesBySquashConflictResolutionTypeDef = None,
    ) -> ClientMergeBranchesBySquashResponseTypeDef:
        """
        Merges two branches using the squash merge strategy.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/codecommit-2015-04-13/MergeBranchesBySquash>`_

        **Request Syntax**
        ::

          response = client.merge_branches_by_squash(
              repositoryName='string',
              sourceCommitSpecifier='string',
              destinationCommitSpecifier='string',
              targetBranch='string',
              conflictDetailLevel='FILE_LEVEL'|'LINE_LEVEL',
              conflictResolutionStrategy='NONE'|'ACCEPT_SOURCE'|'ACCEPT_DESTINATION'|'AUTOMERGE',
              authorName='string',
              email='string',
              commitMessage='string',
              keepEmptyFolders=True|False,
              conflictResolution={
                  'replaceContents': [
                      {
                          'filePath': 'string',
                          'replacementType':
                          'KEEP_BASE'|'KEEP_SOURCE'|'KEEP_DESTINATION'
                          |'USE_NEW_CONTENT',
                          'content': b'bytes',
                          'fileMode': 'EXECUTABLE'|'NORMAL'|'SYMLINK'
                      },
                  ],
                  'deleteFiles': [
                      {
                          'filePath': 'string'
                      },
                  ],
                  'setFileModes': [
                      {
                          'filePath': 'string',
                          'fileMode': 'EXECUTABLE'|'NORMAL'|'SYMLINK'
                      },
                  ]
              }
          )
        :type repositoryName: string
        :param repositoryName: **[REQUIRED]**

          The name of the repository where you want to merge two branches.

        :type sourceCommitSpecifier: string
        :param sourceCommitSpecifier: **[REQUIRED]**

          The branch, tag, HEAD, or other fully qualified reference used to identify a commit (for
          example, a branch name or a full commit ID).

        :type destinationCommitSpecifier: string
        :param destinationCommitSpecifier: **[REQUIRED]**

          The branch, tag, HEAD, or other fully qualified reference used to identify a commit (for
          example, a branch name or a full commit ID).

        :type targetBranch: string
        :param targetBranch:

          The branch where the merge is applied.

        :type conflictDetailLevel: string
        :param conflictDetailLevel:

          The level of conflict detail to use. If unspecified, the default FILE_LEVEL is used, which
          returns a not-mergeable result if the same file has differences in both branches. If
          LINE_LEVEL is specified, a conflict is considered not mergeable if the same file in both
          branches has differences on the same line.

        :type conflictResolutionStrategy: string
        :param conflictResolutionStrategy:

          Specifies which branch to use when resolving conflicts, or whether to attempt
          automatically merging two versions of a file. The default is NONE, which requires any
          conflicts to be resolved manually before the merge operation is successful.

        :type authorName: string
        :param authorName:

          The name of the author who created the commit. This information is used as both the author
          and committer for the commit.

        :type email: string
        :param email:

          The email address of the person merging the branches. This information is used in the
          commit information for the merge.

        :type commitMessage: string
        :param commitMessage:

          The commit message for the merge.

        :type keepEmptyFolders: boolean
        :param keepEmptyFolders:

          If the commit contains deletions, whether to keep a folder or folder structure if the
          changes leave the folders empty. If this is specified as true, a .gitkeep file is created
          for empty folders. The default is false.

        :type conflictResolution: dict
        :param conflictResolution:

          If AUTOMERGE is the conflict resolution strategy, a list of inputs to use when resolving
          conflicts during a merge.

          - **replaceContents** *(list) --*

            Files to have content replaced as part of the merge conflict resolution.

            - *(dict) --*

              Information about a replacement content entry in the conflict of a merge or pull
              request operation.

              - **filePath** *(string) --* **[REQUIRED]**

                The path of the conflicting file.

              - **replacementType** *(string) --* **[REQUIRED]**

                The replacement type to use when determining how to resolve the conflict.

              - **content** *(bytes) --*

                The base-64 encoded content to use when the replacement type is USE_NEW_CONTENT.

              - **fileMode** *(string) --*

                The file mode to apply during conflict resoltion.

          - **deleteFiles** *(list) --*

            Files to be deleted as part of the merge conflict resolution.

            - *(dict) --*

              A file that is deleted as part of a commit.

              - **filePath** *(string) --* **[REQUIRED]**

                The full path of the file to be deleted, including the name of the file.

          - **setFileModes** *(list) --*

            File modes that are set as part of the merge conflict resolution.

            - *(dict) --*

              Information about the file mode changes.

              - **filePath** *(string) --* **[REQUIRED]**

                The full path to the file, including the name of the file.

              - **fileMode** *(string) --* **[REQUIRED]**

                The file mode for the file.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'commitId': 'string',
                'treeId': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **commitId** *(string) --*

              The commit ID of the merge in the destination or target branch.

            - **treeId** *(string) --*

              The tree ID of the merge in the destination or target branch.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def merge_branches_by_three_way(
        self,
        repositoryName: str,
        sourceCommitSpecifier: str,
        destinationCommitSpecifier: str,
        targetBranch: str = None,
        conflictDetailLevel: Literal["FILE_LEVEL", "LINE_LEVEL"] = None,
        conflictResolutionStrategy: Literal[
            "NONE", "ACCEPT_SOURCE", "ACCEPT_DESTINATION", "AUTOMERGE"
        ] = None,
        authorName: str = None,
        email: str = None,
        commitMessage: str = None,
        keepEmptyFolders: bool = None,
        conflictResolution: ClientMergeBranchesByThreeWayConflictResolutionTypeDef = None,
    ) -> ClientMergeBranchesByThreeWayResponseTypeDef:
        """
        Merges two specified branches using the three-way merge strategy.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/codecommit-2015-04-13/MergeBranchesByThreeWay>`_

        **Request Syntax**
        ::

          response = client.merge_branches_by_three_way(
              repositoryName='string',
              sourceCommitSpecifier='string',
              destinationCommitSpecifier='string',
              targetBranch='string',
              conflictDetailLevel='FILE_LEVEL'|'LINE_LEVEL',
              conflictResolutionStrategy='NONE'|'ACCEPT_SOURCE'|'ACCEPT_DESTINATION'|'AUTOMERGE',
              authorName='string',
              email='string',
              commitMessage='string',
              keepEmptyFolders=True|False,
              conflictResolution={
                  'replaceContents': [
                      {
                          'filePath': 'string',
                          'replacementType':
                          'KEEP_BASE'|'KEEP_SOURCE'|'KEEP_DESTINATION'
                          |'USE_NEW_CONTENT',
                          'content': b'bytes',
                          'fileMode': 'EXECUTABLE'|'NORMAL'|'SYMLINK'
                      },
                  ],
                  'deleteFiles': [
                      {
                          'filePath': 'string'
                      },
                  ],
                  'setFileModes': [
                      {
                          'filePath': 'string',
                          'fileMode': 'EXECUTABLE'|'NORMAL'|'SYMLINK'
                      },
                  ]
              }
          )
        :type repositoryName: string
        :param repositoryName: **[REQUIRED]**

          The name of the repository where you want to merge two branches.

        :type sourceCommitSpecifier: string
        :param sourceCommitSpecifier: **[REQUIRED]**

          The branch, tag, HEAD, or other fully qualified reference used to identify a commit (for
          example, a branch name or a full commit ID).

        :type destinationCommitSpecifier: string
        :param destinationCommitSpecifier: **[REQUIRED]**

          The branch, tag, HEAD, or other fully qualified reference used to identify a commit (for
          example, a branch name or a full commit ID).

        :type targetBranch: string
        :param targetBranch:

          The branch where the merge is applied.

        :type conflictDetailLevel: string
        :param conflictDetailLevel:

          The level of conflict detail to use. If unspecified, the default FILE_LEVEL is used, which
          returns a not-mergeable result if the same file has differences in both branches. If
          LINE_LEVEL is specified, a conflict is considered not mergeable if the same file in both
          branches has differences on the same line.

        :type conflictResolutionStrategy: string
        :param conflictResolutionStrategy:

          Specifies which branch to use when resolving conflicts, or whether to attempt
          automatically merging two versions of a file. The default is NONE, which requires any
          conflicts to be resolved manually before the merge operation is successful.

        :type authorName: string
        :param authorName:

          The name of the author who created the commit. This information is used as both the author
          and committer for the commit.

        :type email: string
        :param email:

          The email address of the person merging the branches. This information is used in the
          commit information for the merge.

        :type commitMessage: string
        :param commitMessage:

          The commit message to include in the commit information for the merge.

        :type keepEmptyFolders: boolean
        :param keepEmptyFolders:

          If the commit contains deletions, whether to keep a folder or folder structure if the
          changes leave the folders empty. If true, a .gitkeep file is created for empty folders.
          The default is false.

        :type conflictResolution: dict
        :param conflictResolution:

          If AUTOMERGE is the conflict resolution strategy, a list of inputs to use when resolving
          conflicts during a merge.

          - **replaceContents** *(list) --*

            Files to have content replaced as part of the merge conflict resolution.

            - *(dict) --*

              Information about a replacement content entry in the conflict of a merge or pull
              request operation.

              - **filePath** *(string) --* **[REQUIRED]**

                The path of the conflicting file.

              - **replacementType** *(string) --* **[REQUIRED]**

                The replacement type to use when determining how to resolve the conflict.

              - **content** *(bytes) --*

                The base-64 encoded content to use when the replacement type is USE_NEW_CONTENT.

              - **fileMode** *(string) --*

                The file mode to apply during conflict resoltion.

          - **deleteFiles** *(list) --*

            Files to be deleted as part of the merge conflict resolution.

            - *(dict) --*

              A file that is deleted as part of a commit.

              - **filePath** *(string) --* **[REQUIRED]**

                The full path of the file to be deleted, including the name of the file.

          - **setFileModes** *(list) --*

            File modes that are set as part of the merge conflict resolution.

            - *(dict) --*

              Information about the file mode changes.

              - **filePath** *(string) --* **[REQUIRED]**

                The full path to the file, including the name of the file.

              - **fileMode** *(string) --* **[REQUIRED]**

                The file mode for the file.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'commitId': 'string',
                'treeId': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **commitId** *(string) --*

              The commit ID of the merge in the destination or target branch.

            - **treeId** *(string) --*

              The tree ID of the merge in the destination or target branch.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def merge_pull_request_by_fast_forward(
        self, pullRequestId: str, repositoryName: str, sourceCommitId: str = None
    ) -> ClientMergePullRequestByFastForwardResponseTypeDef:
        """
        Attempts to merge the source commit of a pull request into the specified destination branch
        for that pull request at the specified commit using the fast-forward merge strategy. If the
        merge is successful, it closes the pull request.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/codecommit-2015-04-13/MergePullRequestByFastForward>`_

        **Request Syntax**
        ::

          response = client.merge_pull_request_by_fast_forward(
              pullRequestId='string',
              repositoryName='string',
              sourceCommitId='string'
          )
        :type pullRequestId: string
        :param pullRequestId: **[REQUIRED]**

          The system-generated ID of the pull request. To get this ID, use  ListPullRequests .

        :type repositoryName: string
        :param repositoryName: **[REQUIRED]**

          The name of the repository where the pull request was created.

        :type sourceCommitId: string
        :param sourceCommitId:

          The full commit ID of the original or updated commit in the pull request source branch.
          Pass this value if you want an exception thrown if the current commit ID of the tip of the
          source branch does not match this commit ID.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'pullRequest': {
                    'pullRequestId': 'string',
                    'title': 'string',
                    'description': 'string',
                    'lastActivityDate': datetime(2015, 1, 1),
                    'creationDate': datetime(2015, 1, 1),
                    'pullRequestStatus': 'OPEN'|'CLOSED',
                    'authorArn': 'string',
                    'pullRequestTargets': [
                        {
                            'repositoryName': 'string',
                            'sourceReference': 'string',
                            'destinationReference': 'string',
                            'destinationCommit': 'string',
                            'sourceCommit': 'string',
                            'mergeBase': 'string',
                            'mergeMetadata': {
                                'isMerged': True|False,
                                'mergedBy': 'string',
                                'mergeCommitId': 'string',
                                'mergeOption': 'FAST_FORWARD_MERGE'|'SQUASH_MERGE'|'THREE_WAY_MERGE'
                            }
                        },
                    ],
                    'clientRequestToken': 'string',
                    'revisionId': 'string',
                    'approvalRules': [
                        {
                            'approvalRuleId': 'string',
                            'approvalRuleName': 'string',
                            'approvalRuleContent': 'string',
                            'ruleContentSha256': 'string',
                            'lastModifiedDate': datetime(2015, 1, 1),
                            'creationDate': datetime(2015, 1, 1),
                            'lastModifiedUser': 'string',
                            'originApprovalRuleTemplate': {
                                'approvalRuleTemplateId': 'string',
                                'approvalRuleTemplateName': 'string'
                            }
                        },
                    ]
                }
            }
          **Response Structure**

          - *(dict) --*

            - **pullRequest** *(dict) --*

              Information about the specified pull request, including the merge.

              - **pullRequestId** *(string) --*

                The system-generated ID of the pull request.

              - **title** *(string) --*

                The user-defined title of the pull request. This title is displayed in the list of
                pull requests to other repository users.

              - **description** *(string) --*

                The user-defined description of the pull request. This description can be used to
                clarify what should be reviewed and other details of the request.

              - **lastActivityDate** *(datetime) --*

                The day and time of the last user or system activity on the pull request, in
                timestamp format.

              - **creationDate** *(datetime) --*

                The date and time the pull request was originally created, in timestamp format.

              - **pullRequestStatus** *(string) --*

                The status of the pull request. Pull request status can only change from ``OPEN`` to
                ``CLOSED`` .

              - **authorArn** *(string) --*

                The Amazon Resource Name (ARN) of the user who created the pull request.

              - **pullRequestTargets** *(list) --*

                The targets of the pull request, including the source branch and destination branch
                for the pull request.

                - *(dict) --*

                  Returns information about a pull request target.

                  - **repositoryName** *(string) --*

                    The name of the repository that contains the pull request source and destination
                    branches.

                  - **sourceReference** *(string) --*

                    The branch of the repository that contains the changes for the pull request.
                    Also known as the source branch.

                  - **destinationReference** *(string) --*

                    The branch of the repository where the pull request changes are merged. Also
                    known as the destination branch.

                  - **destinationCommit** *(string) --*

                    The full commit ID that is the tip of the destination branch. This is the commit
                    where the pull request was or will be merged.

                  - **sourceCommit** *(string) --*

                    The full commit ID of the tip of the source branch used to create the pull
                    request. If the pull request branch is updated by a push while the pull request
                    is open, the commit ID changes to reflect the new tip of the branch.

                  - **mergeBase** *(string) --*

                    The commit ID of the most recent commit that the source branch and the
                    destination branch have in common.

                  - **mergeMetadata** *(dict) --*

                    Returns metadata about the state of the merge, including whether the merge has
                    been made.

                    - **isMerged** *(boolean) --*

                      A Boolean value indicating whether the merge has been made.

                    - **mergedBy** *(string) --*

                      The Amazon Resource Name (ARN) of the user who merged the branches.

                    - **mergeCommitId** *(string) --*

                      The commit ID for the merge commit, if any.

                    - **mergeOption** *(string) --*

                      The merge strategy used in the merge.

              - **clientRequestToken** *(string) --*

                A unique, client-generated idempotency token that, when provided in a request,
                ensures the request cannot be repeated with a changed parameter. If a request is
                received with the same parameters and a token is included, the request returns
                information about the initial request that used that token.

              - **revisionId** *(string) --*

                The system-generated revision ID for the pull request.

              - **approvalRules** *(list) --*

                The approval rules applied to the pull request.

                - *(dict) --*

                  Returns information about an approval rule.

                  - **approvalRuleId** *(string) --*

                    The system-generated ID of the approval rule.

                  - **approvalRuleName** *(string) --*

                    The name of the approval rule.

                  - **approvalRuleContent** *(string) --*

                    The content of the approval rule.

                  - **ruleContentSha256** *(string) --*

                    The SHA-256 hash signature for the content of the approval rule.

                  - **lastModifiedDate** *(datetime) --*

                    The date the approval rule was most recently changed, in timestamp format.

                  - **creationDate** *(datetime) --*

                    The date the approval rule was created, in timestamp format.

                  - **lastModifiedUser** *(string) --*

                    The Amazon Resource Name (ARN) of the user who made the most recent changes to
                    the approval rule.

                  - **originApprovalRuleTemplate** *(dict) --*

                    The approval rule template used to create the rule.

                    - **approvalRuleTemplateId** *(string) --*

                      The ID of the template that created the approval rule.

                    - **approvalRuleTemplateName** *(string) --*

                      The name of the template that created the approval rule.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def merge_pull_request_by_squash(
        self,
        pullRequestId: str,
        repositoryName: str,
        sourceCommitId: str = None,
        conflictDetailLevel: Literal["FILE_LEVEL", "LINE_LEVEL"] = None,
        conflictResolutionStrategy: Literal[
            "NONE", "ACCEPT_SOURCE", "ACCEPT_DESTINATION", "AUTOMERGE"
        ] = None,
        commitMessage: str = None,
        authorName: str = None,
        email: str = None,
        keepEmptyFolders: bool = None,
        conflictResolution: ClientMergePullRequestBySquashConflictResolutionTypeDef = None,
    ) -> ClientMergePullRequestBySquashResponseTypeDef:
        """
        Attempts to merge the source commit of a pull request into the specified destination branch
        for that pull request at the specified commit using the squash merge strategy. If the merge
        is successful, it closes the pull request.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/codecommit-2015-04-13/MergePullRequestBySquash>`_

        **Request Syntax**
        ::

          response = client.merge_pull_request_by_squash(
              pullRequestId='string',
              repositoryName='string',
              sourceCommitId='string',
              conflictDetailLevel='FILE_LEVEL'|'LINE_LEVEL',
              conflictResolutionStrategy='NONE'|'ACCEPT_SOURCE'|'ACCEPT_DESTINATION'|'AUTOMERGE',
              commitMessage='string',
              authorName='string',
              email='string',
              keepEmptyFolders=True|False,
              conflictResolution={
                  'replaceContents': [
                      {
                          'filePath': 'string',
                          'replacementType':
                          'KEEP_BASE'|'KEEP_SOURCE'|'KEEP_DESTINATION'
                          |'USE_NEW_CONTENT',
                          'content': b'bytes',
                          'fileMode': 'EXECUTABLE'|'NORMAL'|'SYMLINK'
                      },
                  ],
                  'deleteFiles': [
                      {
                          'filePath': 'string'
                      },
                  ],
                  'setFileModes': [
                      {
                          'filePath': 'string',
                          'fileMode': 'EXECUTABLE'|'NORMAL'|'SYMLINK'
                      },
                  ]
              }
          )
        :type pullRequestId: string
        :param pullRequestId: **[REQUIRED]**

          The system-generated ID of the pull request. To get this ID, use  ListPullRequests .

        :type repositoryName: string
        :param repositoryName: **[REQUIRED]**

          The name of the repository where the pull request was created.

        :type sourceCommitId: string
        :param sourceCommitId:

          The full commit ID of the original or updated commit in the pull request source branch.
          Pass this value if you want an exception thrown if the current commit ID of the tip of the
          source branch does not match this commit ID.

        :type conflictDetailLevel: string
        :param conflictDetailLevel:

          The level of conflict detail to use. If unspecified, the default FILE_LEVEL is used, which
          returns a not-mergeable result if the same file has differences in both branches. If
          LINE_LEVEL is specified, a conflict is considered not mergeable if the same file in both
          branches has differences on the same line.

        :type conflictResolutionStrategy: string
        :param conflictResolutionStrategy:

          Specifies which branch to use when resolving conflicts, or whether to attempt
          automatically merging two versions of a file. The default is NONE, which requires any
          conflicts to be resolved manually before the merge operation is successful.

        :type commitMessage: string
        :param commitMessage:

          The commit message to include in the commit information for the merge.

        :type authorName: string
        :param authorName:

          The name of the author who created the commit. This information is used as both the author
          and committer for the commit.

        :type email: string
        :param email:

          The email address of the person merging the branches. This information is used in the
          commit information for the merge.

        :type keepEmptyFolders: boolean
        :param keepEmptyFolders:

          If the commit contains deletions, whether to keep a folder or folder structure if the
          changes leave the folders empty. If true, a .gitkeep file is created for empty folders.
          The default is false.

        :type conflictResolution: dict
        :param conflictResolution:

          If AUTOMERGE is the conflict resolution strategy, a list of inputs to use when resolving
          conflicts during a merge.

          - **replaceContents** *(list) --*

            Files to have content replaced as part of the merge conflict resolution.

            - *(dict) --*

              Information about a replacement content entry in the conflict of a merge or pull
              request operation.

              - **filePath** *(string) --* **[REQUIRED]**

                The path of the conflicting file.

              - **replacementType** *(string) --* **[REQUIRED]**

                The replacement type to use when determining how to resolve the conflict.

              - **content** *(bytes) --*

                The base-64 encoded content to use when the replacement type is USE_NEW_CONTENT.

              - **fileMode** *(string) --*

                The file mode to apply during conflict resoltion.

          - **deleteFiles** *(list) --*

            Files to be deleted as part of the merge conflict resolution.

            - *(dict) --*

              A file that is deleted as part of a commit.

              - **filePath** *(string) --* **[REQUIRED]**

                The full path of the file to be deleted, including the name of the file.

          - **setFileModes** *(list) --*

            File modes that are set as part of the merge conflict resolution.

            - *(dict) --*

              Information about the file mode changes.

              - **filePath** *(string) --* **[REQUIRED]**

                The full path to the file, including the name of the file.

              - **fileMode** *(string) --* **[REQUIRED]**

                The file mode for the file.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'pullRequest': {
                    'pullRequestId': 'string',
                    'title': 'string',
                    'description': 'string',
                    'lastActivityDate': datetime(2015, 1, 1),
                    'creationDate': datetime(2015, 1, 1),
                    'pullRequestStatus': 'OPEN'|'CLOSED',
                    'authorArn': 'string',
                    'pullRequestTargets': [
                        {
                            'repositoryName': 'string',
                            'sourceReference': 'string',
                            'destinationReference': 'string',
                            'destinationCommit': 'string',
                            'sourceCommit': 'string',
                            'mergeBase': 'string',
                            'mergeMetadata': {
                                'isMerged': True|False,
                                'mergedBy': 'string',
                                'mergeCommitId': 'string',
                                'mergeOption': 'FAST_FORWARD_MERGE'|'SQUASH_MERGE'|'THREE_WAY_MERGE'
                            }
                        },
                    ],
                    'clientRequestToken': 'string',
                    'revisionId': 'string',
                    'approvalRules': [
                        {
                            'approvalRuleId': 'string',
                            'approvalRuleName': 'string',
                            'approvalRuleContent': 'string',
                            'ruleContentSha256': 'string',
                            'lastModifiedDate': datetime(2015, 1, 1),
                            'creationDate': datetime(2015, 1, 1),
                            'lastModifiedUser': 'string',
                            'originApprovalRuleTemplate': {
                                'approvalRuleTemplateId': 'string',
                                'approvalRuleTemplateName': 'string'
                            }
                        },
                    ]
                }
            }
          **Response Structure**

          - *(dict) --*

            - **pullRequest** *(dict) --*

              Returns information about a pull request.

              - **pullRequestId** *(string) --*

                The system-generated ID of the pull request.

              - **title** *(string) --*

                The user-defined title of the pull request. This title is displayed in the list of
                pull requests to other repository users.

              - **description** *(string) --*

                The user-defined description of the pull request. This description can be used to
                clarify what should be reviewed and other details of the request.

              - **lastActivityDate** *(datetime) --*

                The day and time of the last user or system activity on the pull request, in
                timestamp format.

              - **creationDate** *(datetime) --*

                The date and time the pull request was originally created, in timestamp format.

              - **pullRequestStatus** *(string) --*

                The status of the pull request. Pull request status can only change from ``OPEN`` to
                ``CLOSED`` .

              - **authorArn** *(string) --*

                The Amazon Resource Name (ARN) of the user who created the pull request.

              - **pullRequestTargets** *(list) --*

                The targets of the pull request, including the source branch and destination branch
                for the pull request.

                - *(dict) --*

                  Returns information about a pull request target.

                  - **repositoryName** *(string) --*

                    The name of the repository that contains the pull request source and destination
                    branches.

                  - **sourceReference** *(string) --*

                    The branch of the repository that contains the changes for the pull request.
                    Also known as the source branch.

                  - **destinationReference** *(string) --*

                    The branch of the repository where the pull request changes are merged. Also
                    known as the destination branch.

                  - **destinationCommit** *(string) --*

                    The full commit ID that is the tip of the destination branch. This is the commit
                    where the pull request was or will be merged.

                  - **sourceCommit** *(string) --*

                    The full commit ID of the tip of the source branch used to create the pull
                    request. If the pull request branch is updated by a push while the pull request
                    is open, the commit ID changes to reflect the new tip of the branch.

                  - **mergeBase** *(string) --*

                    The commit ID of the most recent commit that the source branch and the
                    destination branch have in common.

                  - **mergeMetadata** *(dict) --*

                    Returns metadata about the state of the merge, including whether the merge has
                    been made.

                    - **isMerged** *(boolean) --*

                      A Boolean value indicating whether the merge has been made.

                    - **mergedBy** *(string) --*

                      The Amazon Resource Name (ARN) of the user who merged the branches.

                    - **mergeCommitId** *(string) --*

                      The commit ID for the merge commit, if any.

                    - **mergeOption** *(string) --*

                      The merge strategy used in the merge.

              - **clientRequestToken** *(string) --*

                A unique, client-generated idempotency token that, when provided in a request,
                ensures the request cannot be repeated with a changed parameter. If a request is
                received with the same parameters and a token is included, the request returns
                information about the initial request that used that token.

              - **revisionId** *(string) --*

                The system-generated revision ID for the pull request.

              - **approvalRules** *(list) --*

                The approval rules applied to the pull request.

                - *(dict) --*

                  Returns information about an approval rule.

                  - **approvalRuleId** *(string) --*

                    The system-generated ID of the approval rule.

                  - **approvalRuleName** *(string) --*

                    The name of the approval rule.

                  - **approvalRuleContent** *(string) --*

                    The content of the approval rule.

                  - **ruleContentSha256** *(string) --*

                    The SHA-256 hash signature for the content of the approval rule.

                  - **lastModifiedDate** *(datetime) --*

                    The date the approval rule was most recently changed, in timestamp format.

                  - **creationDate** *(datetime) --*

                    The date the approval rule was created, in timestamp format.

                  - **lastModifiedUser** *(string) --*

                    The Amazon Resource Name (ARN) of the user who made the most recent changes to
                    the approval rule.

                  - **originApprovalRuleTemplate** *(dict) --*

                    The approval rule template used to create the rule.

                    - **approvalRuleTemplateId** *(string) --*

                      The ID of the template that created the approval rule.

                    - **approvalRuleTemplateName** *(string) --*

                      The name of the template that created the approval rule.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def merge_pull_request_by_three_way(
        self,
        pullRequestId: str,
        repositoryName: str,
        sourceCommitId: str = None,
        conflictDetailLevel: Literal["FILE_LEVEL", "LINE_LEVEL"] = None,
        conflictResolutionStrategy: Literal[
            "NONE", "ACCEPT_SOURCE", "ACCEPT_DESTINATION", "AUTOMERGE"
        ] = None,
        commitMessage: str = None,
        authorName: str = None,
        email: str = None,
        keepEmptyFolders: bool = None,
        conflictResolution: ClientMergePullRequestByThreeWayConflictResolutionTypeDef = None,
    ) -> ClientMergePullRequestByThreeWayResponseTypeDef:
        """
        Attempts to merge the source commit of a pull request into the specified destination branch
        for that pull request at the specified commit using the three-way merge strategy. If the
        merge is successful, it closes the pull request.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/codecommit-2015-04-13/MergePullRequestByThreeWay>`_

        **Request Syntax**
        ::

          response = client.merge_pull_request_by_three_way(
              pullRequestId='string',
              repositoryName='string',
              sourceCommitId='string',
              conflictDetailLevel='FILE_LEVEL'|'LINE_LEVEL',
              conflictResolutionStrategy='NONE'|'ACCEPT_SOURCE'|'ACCEPT_DESTINATION'|'AUTOMERGE',
              commitMessage='string',
              authorName='string',
              email='string',
              keepEmptyFolders=True|False,
              conflictResolution={
                  'replaceContents': [
                      {
                          'filePath': 'string',
                          'replacementType':
                          'KEEP_BASE'|'KEEP_SOURCE'|'KEEP_DESTINATION'
                          |'USE_NEW_CONTENT',
                          'content': b'bytes',
                          'fileMode': 'EXECUTABLE'|'NORMAL'|'SYMLINK'
                      },
                  ],
                  'deleteFiles': [
                      {
                          'filePath': 'string'
                      },
                  ],
                  'setFileModes': [
                      {
                          'filePath': 'string',
                          'fileMode': 'EXECUTABLE'|'NORMAL'|'SYMLINK'
                      },
                  ]
              }
          )
        :type pullRequestId: string
        :param pullRequestId: **[REQUIRED]**

          The system-generated ID of the pull request. To get this ID, use  ListPullRequests .

        :type repositoryName: string
        :param repositoryName: **[REQUIRED]**

          The name of the repository where the pull request was created.

        :type sourceCommitId: string
        :param sourceCommitId:

          The full commit ID of the original or updated commit in the pull request source branch.
          Pass this value if you want an exception thrown if the current commit ID of the tip of the
          source branch does not match this commit ID.

        :type conflictDetailLevel: string
        :param conflictDetailLevel:

          The level of conflict detail to use. If unspecified, the default FILE_LEVEL is used, which
          returns a not-mergeable result if the same file has differences in both branches. If
          LINE_LEVEL is specified, a conflict is considered not mergeable if the same file in both
          branches has differences on the same line.

        :type conflictResolutionStrategy: string
        :param conflictResolutionStrategy:

          Specifies which branch to use when resolving conflicts, or whether to attempt
          automatically merging two versions of a file. The default is NONE, which requires any
          conflicts to be resolved manually before the merge operation is successful.

        :type commitMessage: string
        :param commitMessage:

          The commit message to include in the commit information for the merge.

        :type authorName: string
        :param authorName:

          The name of the author who created the commit. This information is used as both the author
          and committer for the commit.

        :type email: string
        :param email:

          The email address of the person merging the branches. This information is used in the
          commit information for the merge.

        :type keepEmptyFolders: boolean
        :param keepEmptyFolders:

          If the commit contains deletions, whether to keep a folder or folder structure if the
          changes leave the folders empty. If true, a .gitkeep file is created for empty folders.
          The default is false.

        :type conflictResolution: dict
        :param conflictResolution:

          If AUTOMERGE is the conflict resolution strategy, a list of inputs to use when resolving
          conflicts during a merge.

          - **replaceContents** *(list) --*

            Files to have content replaced as part of the merge conflict resolution.

            - *(dict) --*

              Information about a replacement content entry in the conflict of a merge or pull
              request operation.

              - **filePath** *(string) --* **[REQUIRED]**

                The path of the conflicting file.

              - **replacementType** *(string) --* **[REQUIRED]**

                The replacement type to use when determining how to resolve the conflict.

              - **content** *(bytes) --*

                The base-64 encoded content to use when the replacement type is USE_NEW_CONTENT.

              - **fileMode** *(string) --*

                The file mode to apply during conflict resoltion.

          - **deleteFiles** *(list) --*

            Files to be deleted as part of the merge conflict resolution.

            - *(dict) --*

              A file that is deleted as part of a commit.

              - **filePath** *(string) --* **[REQUIRED]**

                The full path of the file to be deleted, including the name of the file.

          - **setFileModes** *(list) --*

            File modes that are set as part of the merge conflict resolution.

            - *(dict) --*

              Information about the file mode changes.

              - **filePath** *(string) --* **[REQUIRED]**

                The full path to the file, including the name of the file.

              - **fileMode** *(string) --* **[REQUIRED]**

                The file mode for the file.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'pullRequest': {
                    'pullRequestId': 'string',
                    'title': 'string',
                    'description': 'string',
                    'lastActivityDate': datetime(2015, 1, 1),
                    'creationDate': datetime(2015, 1, 1),
                    'pullRequestStatus': 'OPEN'|'CLOSED',
                    'authorArn': 'string',
                    'pullRequestTargets': [
                        {
                            'repositoryName': 'string',
                            'sourceReference': 'string',
                            'destinationReference': 'string',
                            'destinationCommit': 'string',
                            'sourceCommit': 'string',
                            'mergeBase': 'string',
                            'mergeMetadata': {
                                'isMerged': True|False,
                                'mergedBy': 'string',
                                'mergeCommitId': 'string',
                                'mergeOption': 'FAST_FORWARD_MERGE'|'SQUASH_MERGE'|'THREE_WAY_MERGE'
                            }
                        },
                    ],
                    'clientRequestToken': 'string',
                    'revisionId': 'string',
                    'approvalRules': [
                        {
                            'approvalRuleId': 'string',
                            'approvalRuleName': 'string',
                            'approvalRuleContent': 'string',
                            'ruleContentSha256': 'string',
                            'lastModifiedDate': datetime(2015, 1, 1),
                            'creationDate': datetime(2015, 1, 1),
                            'lastModifiedUser': 'string',
                            'originApprovalRuleTemplate': {
                                'approvalRuleTemplateId': 'string',
                                'approvalRuleTemplateName': 'string'
                            }
                        },
                    ]
                }
            }
          **Response Structure**

          - *(dict) --*

            - **pullRequest** *(dict) --*

              Returns information about a pull request.

              - **pullRequestId** *(string) --*

                The system-generated ID of the pull request.

              - **title** *(string) --*

                The user-defined title of the pull request. This title is displayed in the list of
                pull requests to other repository users.

              - **description** *(string) --*

                The user-defined description of the pull request. This description can be used to
                clarify what should be reviewed and other details of the request.

              - **lastActivityDate** *(datetime) --*

                The day and time of the last user or system activity on the pull request, in
                timestamp format.

              - **creationDate** *(datetime) --*

                The date and time the pull request was originally created, in timestamp format.

              - **pullRequestStatus** *(string) --*

                The status of the pull request. Pull request status can only change from ``OPEN`` to
                ``CLOSED`` .

              - **authorArn** *(string) --*

                The Amazon Resource Name (ARN) of the user who created the pull request.

              - **pullRequestTargets** *(list) --*

                The targets of the pull request, including the source branch and destination branch
                for the pull request.

                - *(dict) --*

                  Returns information about a pull request target.

                  - **repositoryName** *(string) --*

                    The name of the repository that contains the pull request source and destination
                    branches.

                  - **sourceReference** *(string) --*

                    The branch of the repository that contains the changes for the pull request.
                    Also known as the source branch.

                  - **destinationReference** *(string) --*

                    The branch of the repository where the pull request changes are merged. Also
                    known as the destination branch.

                  - **destinationCommit** *(string) --*

                    The full commit ID that is the tip of the destination branch. This is the commit
                    where the pull request was or will be merged.

                  - **sourceCommit** *(string) --*

                    The full commit ID of the tip of the source branch used to create the pull
                    request. If the pull request branch is updated by a push while the pull request
                    is open, the commit ID changes to reflect the new tip of the branch.

                  - **mergeBase** *(string) --*

                    The commit ID of the most recent commit that the source branch and the
                    destination branch have in common.

                  - **mergeMetadata** *(dict) --*

                    Returns metadata about the state of the merge, including whether the merge has
                    been made.

                    - **isMerged** *(boolean) --*

                      A Boolean value indicating whether the merge has been made.

                    - **mergedBy** *(string) --*

                      The Amazon Resource Name (ARN) of the user who merged the branches.

                    - **mergeCommitId** *(string) --*

                      The commit ID for the merge commit, if any.

                    - **mergeOption** *(string) --*

                      The merge strategy used in the merge.

              - **clientRequestToken** *(string) --*

                A unique, client-generated idempotency token that, when provided in a request,
                ensures the request cannot be repeated with a changed parameter. If a request is
                received with the same parameters and a token is included, the request returns
                information about the initial request that used that token.

              - **revisionId** *(string) --*

                The system-generated revision ID for the pull request.

              - **approvalRules** *(list) --*

                The approval rules applied to the pull request.

                - *(dict) --*

                  Returns information about an approval rule.

                  - **approvalRuleId** *(string) --*

                    The system-generated ID of the approval rule.

                  - **approvalRuleName** *(string) --*

                    The name of the approval rule.

                  - **approvalRuleContent** *(string) --*

                    The content of the approval rule.

                  - **ruleContentSha256** *(string) --*

                    The SHA-256 hash signature for the content of the approval rule.

                  - **lastModifiedDate** *(datetime) --*

                    The date the approval rule was most recently changed, in timestamp format.

                  - **creationDate** *(datetime) --*

                    The date the approval rule was created, in timestamp format.

                  - **lastModifiedUser** *(string) --*

                    The Amazon Resource Name (ARN) of the user who made the most recent changes to
                    the approval rule.

                  - **originApprovalRuleTemplate** *(dict) --*

                    The approval rule template used to create the rule.

                    - **approvalRuleTemplateId** *(string) --*

                      The ID of the template that created the approval rule.

                    - **approvalRuleTemplateName** *(string) --*

                      The name of the template that created the approval rule.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def override_pull_request_approval_rules(
        self, pullRequestId: str, revisionId: str, overrideStatus: Literal["OVERRIDE", "REVOKE"]
    ) -> None:
        """
        Sets aside (overrides) all approval rule requirements for a specified pull request.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/codecommit-2015-04-13/OverridePullRequestApprovalRules>`_

        **Request Syntax**
        ::

          response = client.override_pull_request_approval_rules(
              pullRequestId='string',
              revisionId='string',
              overrideStatus='OVERRIDE'|'REVOKE'
          )
        :type pullRequestId: string
        :param pullRequestId: **[REQUIRED]**

          The system-generated ID of the pull request for which you want to override all approval
          rule requirements. To get this information, use  GetPullRequest .

        :type revisionId: string
        :param revisionId: **[REQUIRED]**

          The system-generated ID of the most recent revision of the pull request. You cannot
          override approval rules for anything but the most recent revision of a pull request. To
          get the revision ID, use GetPullRequest.

        :type overrideStatus: string
        :param overrideStatus: **[REQUIRED]**

          Whether you want to set aside approval rule requirements for the pull request (OVERRIDE)
          or revoke a previous override and apply approval rule requirements (REVOKE). REVOKE status
          is not stored.

        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def post_comment_for_compared_commit(
        self,
        repositoryName: str,
        afterCommitId: str,
        content: str,
        beforeCommitId: str = None,
        location: ClientPostCommentForComparedCommitLocationTypeDef = None,
        clientRequestToken: str = None,
    ) -> ClientPostCommentForComparedCommitResponseTypeDef:
        """
        Posts a comment on the comparison between two commits.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/codecommit-2015-04-13/PostCommentForComparedCommit>`_

        **Request Syntax**
        ::

          response = client.post_comment_for_compared_commit(
              repositoryName='string',
              beforeCommitId='string',
              afterCommitId='string',
              location={
                  'filePath': 'string',
                  'filePosition': 123,
                  'relativeFileVersion': 'BEFORE'|'AFTER'
              },
              content='string',
              clientRequestToken='string'
          )
        :type repositoryName: string
        :param repositoryName: **[REQUIRED]**

          The name of the repository where you want to post a comment on the comparison between
          commits.

        :type beforeCommitId: string
        :param beforeCommitId:

          To establish the directionality of the comparison, the full commit ID of the before
          commit. Required for commenting on any commit unless that commit is the initial commit.

        :type afterCommitId: string
        :param afterCommitId: **[REQUIRED]**

          To establish the directionality of the comparison, the full commit ID of the after commit.

        :type location: dict
        :param location:

          The location of the comparison where you want to comment.

          - **filePath** *(string) --*

            The name of the file being compared, including its extension and subdirectory, if any.

          - **filePosition** *(integer) --*

            The position of a change in a compared file, in line number format.

          - **relativeFileVersion** *(string) --*

            In a comparison of commits or a pull request, whether the change is in the before or
            after of that comparison.

        :type content: string
        :param content: **[REQUIRED]**

          The content of the comment you want to make.

        :type clientRequestToken: string
        :param clientRequestToken:

          A unique, client-generated idempotency token that, when provided in a request, ensures the
          request cannot be repeated with a changed parameter. If a request is received with the
          same parameters and a token is included, the request returns information about the initial
          request that used that token.

          This field is autopopulated if not provided.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

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
                'comment': {
                    'commentId': 'string',
                    'content': 'string',
                    'inReplyTo': 'string',
                    'creationDate': datetime(2015, 1, 1),
                    'lastModifiedDate': datetime(2015, 1, 1),
                    'authorArn': 'string',
                    'deleted': True|False,
                    'clientRequestToken': 'string'
                }
            }
          **Response Structure**

          - *(dict) --*

            - **repositoryName** *(string) --*

              The name of the repository where you posted a comment on the comparison between
              commits.

            - **beforeCommitId** *(string) --*

              In the directionality you established, the full commit ID of the before commit.

            - **afterCommitId** *(string) --*

              In the directionality you established, the full commit ID of the after commit.

            - **beforeBlobId** *(string) --*

              In the directionality you established, the blob ID of the before blob.

            - **afterBlobId** *(string) --*

              In the directionality you established, the blob ID of the after blob.

            - **location** *(dict) --*

              The location of the comment in the comparison between the two commits.

              - **filePath** *(string) --*

                The name of the file being compared, including its extension and subdirectory, if
                any.

              - **filePosition** *(integer) --*

                The position of a change in a compared file, in line number format.

              - **relativeFileVersion** *(string) --*

                In a comparison of commits or a pull request, whether the change is in the before or
                after of that comparison.

            - **comment** *(dict) --*

              The content of the comment you posted.

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
                ensures the request cannot be repeated with a changed parameter. If a request is
                received with the same parameters and a token is included, the request returns
                information about the initial request that used that token.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def post_comment_for_pull_request(
        self,
        pullRequestId: str,
        repositoryName: str,
        beforeCommitId: str,
        afterCommitId: str,
        content: str,
        location: ClientPostCommentForPullRequestLocationTypeDef = None,
        clientRequestToken: str = None,
    ) -> ClientPostCommentForPullRequestResponseTypeDef:
        """
        Posts a comment on a pull request.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/codecommit-2015-04-13/PostCommentForPullRequest>`_

        **Request Syntax**
        ::

          response = client.post_comment_for_pull_request(
              pullRequestId='string',
              repositoryName='string',
              beforeCommitId='string',
              afterCommitId='string',
              location={
                  'filePath': 'string',
                  'filePosition': 123,
                  'relativeFileVersion': 'BEFORE'|'AFTER'
              },
              content='string',
              clientRequestToken='string'
          )
        :type pullRequestId: string
        :param pullRequestId: **[REQUIRED]**

          The system-generated ID of the pull request. To get this ID, use  ListPullRequests .

        :type repositoryName: string
        :param repositoryName: **[REQUIRED]**

          The name of the repository where you want to post a comment on a pull request.

        :type beforeCommitId: string
        :param beforeCommitId: **[REQUIRED]**

          The full commit ID of the commit in the destination branch that was the tip of the branch
          at the time the pull request was created.

        :type afterCommitId: string
        :param afterCommitId: **[REQUIRED]**

          The full commit ID of the commit in the source branch that is the current tip of the
          branch for the pull request when you post the comment.

        :type location: dict
        :param location:

          The location of the change where you want to post your comment. If no location is
          provided, the comment is posted as a general comment on the pull request difference
          between the before commit ID and the after commit ID.

          - **filePath** *(string) --*

            The name of the file being compared, including its extension and subdirectory, if any.

          - **filePosition** *(integer) --*

            The position of a change in a compared file, in line number format.

          - **relativeFileVersion** *(string) --*

            In a comparison of commits or a pull request, whether the change is in the before or
            after of that comparison.

        :type content: string
        :param content: **[REQUIRED]**

          The content of your comment on the change.

        :type clientRequestToken: string
        :param clientRequestToken:

          A unique, client-generated idempotency token that, when provided in a request, ensures the
          request cannot be repeated with a changed parameter. If a request is received with the
          same parameters and a token is included, the request returns information about the initial
          request that used that token.

          This field is autopopulated if not provided.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'repositoryName': 'string',
                'pullRequestId': 'string',
                'beforeCommitId': 'string',
                'afterCommitId': 'string',
                'beforeBlobId': 'string',
                'afterBlobId': 'string',
                'location': {
                    'filePath': 'string',
                    'filePosition': 123,
                    'relativeFileVersion': 'BEFORE'|'AFTER'
                },
                'comment': {
                    'commentId': 'string',
                    'content': 'string',
                    'inReplyTo': 'string',
                    'creationDate': datetime(2015, 1, 1),
                    'lastModifiedDate': datetime(2015, 1, 1),
                    'authorArn': 'string',
                    'deleted': True|False,
                    'clientRequestToken': 'string'
                }
            }
          **Response Structure**

          - *(dict) --*

            - **repositoryName** *(string) --*

              The name of the repository where you posted a comment on a pull request.

            - **pullRequestId** *(string) --*

              The system-generated ID of the pull request.

            - **beforeCommitId** *(string) --*

              The full commit ID of the commit in the source branch used to create the pull request,
              or in the case of an updated pull request, the full commit ID of the commit used to
              update the pull request.

            - **afterCommitId** *(string) --*

              The full commit ID of the commit in the destination branch where the pull request is
              merged.

            - **beforeBlobId** *(string) --*

              In the directionality of the pull request, the blob ID of the before blob.

            - **afterBlobId** *(string) --*

              In the directionality of the pull request, the blob ID of the after blob.

            - **location** *(dict) --*

              The location of the change where you posted your comment.

              - **filePath** *(string) --*

                The name of the file being compared, including its extension and subdirectory, if
                any.

              - **filePosition** *(integer) --*

                The position of a change in a compared file, in line number format.

              - **relativeFileVersion** *(string) --*

                In a comparison of commits or a pull request, whether the change is in the before or
                after of that comparison.

            - **comment** *(dict) --*

              The content of the comment you posted.

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
                ensures the request cannot be repeated with a changed parameter. If a request is
                received with the same parameters and a token is included, the request returns
                information about the initial request that used that token.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def post_comment_reply(
        self, inReplyTo: str, content: str, clientRequestToken: str = None
    ) -> ClientPostCommentReplyResponseTypeDef:
        """
        Posts a comment in reply to an existing comment on a comparison between commits or a pull
        request.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/codecommit-2015-04-13/PostCommentReply>`_

        **Request Syntax**
        ::

          response = client.post_comment_reply(
              inReplyTo='string',
              clientRequestToken='string',
              content='string'
          )
        :type inReplyTo: string
        :param inReplyTo: **[REQUIRED]**

          The system-generated ID of the comment to which you want to reply. To get this ID, use
          GetCommentsForComparedCommit or  GetCommentsForPullRequest .

        :type clientRequestToken: string
        :param clientRequestToken:

          A unique, client-generated idempotency token that, when provided in a request, ensures the
          request cannot be repeated with a changed parameter. If a request is received with the
          same parameters and a token is included, the request returns information about the initial
          request that used that token.

          This field is autopopulated if not provided.

        :type content: string
        :param content: **[REQUIRED]**

          The contents of your reply to a comment.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'comment': {
                    'commentId': 'string',
                    'content': 'string',
                    'inReplyTo': 'string',
                    'creationDate': datetime(2015, 1, 1),
                    'lastModifiedDate': datetime(2015, 1, 1),
                    'authorArn': 'string',
                    'deleted': True|False,
                    'clientRequestToken': 'string'
                }
            }
          **Response Structure**

          - *(dict) --*

            - **comment** *(dict) --*

              Information about the reply to a comment.

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
                ensures the request cannot be repeated with a changed parameter. If a request is
                received with the same parameters and a token is included, the request returns
                information about the initial request that used that token.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def put_file(
        self,
        repositoryName: str,
        branchName: str,
        fileContent: bytes,
        filePath: str,
        fileMode: Literal["EXECUTABLE", "NORMAL", "SYMLINK"] = None,
        parentCommitId: str = None,
        commitMessage: str = None,
        name: str = None,
        email: str = None,
    ) -> ClientPutFileResponseTypeDef:
        """
        Adds or updates a file in a branch in an AWS CodeCommit repository, and generates a commit
        for the addition in the specified branch.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/codecommit-2015-04-13/PutFile>`_

        **Request Syntax**
        ::

          response = client.put_file(
              repositoryName='string',
              branchName='string',
              fileContent=b'bytes',
              filePath='string',
              fileMode='EXECUTABLE'|'NORMAL'|'SYMLINK',
              parentCommitId='string',
              commitMessage='string',
              name='string',
              email='string'
          )
        :type repositoryName: string
        :param repositoryName: **[REQUIRED]**

          The name of the repository where you want to add or update the file.

        :type branchName: string
        :param branchName: **[REQUIRED]**

          The name of the branch where you want to add or update the file. If this is an empty
          repository, this branch is created.

        :type fileContent: bytes
        :param fileContent: **[REQUIRED]**

          The content of the file, in binary object format.

        :type filePath: string
        :param filePath: **[REQUIRED]**

          The name of the file you want to add or update, including the relative path to the file in
          the repository.

          .. note::

            If the path does not currently exist in the repository, the path is created as part of
            adding the file.

        :type fileMode: string
        :param fileMode:

          The file mode permissions of the blob. Valid file mode permissions are listed here.

        :type parentCommitId: string
        :param parentCommitId:

          The full commit ID of the head commit in the branch where you want to add or update the
          file. If this is an empty repository, no commit ID is required. If this is not an empty
          repository, a commit ID is required.

          The commit ID must match the ID of the head commit at the time of the operation.
          Otherwise, an error occurs, and the file is not added or updated.

        :type commitMessage: string
        :param commitMessage:

          A message about why this file was added or updated. Although it is optional, a message
          makes the commit history for your repository more useful.

        :type name: string
        :param name:

          The name of the person adding or updating the file. Although it is optional, a name makes
          the commit history for your repository more useful.

        :type email: string
        :param email:

          An email address for the person adding or updating the file.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'commitId': 'string',
                'blobId': 'string',
                'treeId': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **commitId** *(string) --*

              The full SHA ID of the commit that contains this file change.

            - **blobId** *(string) --*

              The ID of the blob, which is its SHA-1 pointer.

            - **treeId** *(string) --*

              The full SHA-1 pointer of the tree information for the commit that contains this file
              change.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def put_repository_triggers(
        self, repositoryName: str, triggers: List[ClientPutRepositoryTriggersTriggersTypeDef]
    ) -> ClientPutRepositoryTriggersResponseTypeDef:
        """
        Replaces all triggers for a repository. Used to create or delete triggers.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/codecommit-2015-04-13/PutRepositoryTriggers>`_

        **Request Syntax**
        ::

          response = client.put_repository_triggers(
              repositoryName='string',
              triggers=[
                  {
                      'name': 'string',
                      'destinationArn': 'string',
                      'customData': 'string',
                      'branches': [
                          'string',
                      ],
                      'events': [
                          'all'|'updateReference'|'createReference'|'deleteReference',
                      ]
                  },
              ]
          )
        :type repositoryName: string
        :param repositoryName: **[REQUIRED]**

          The name of the repository where you want to create or update the trigger.

        :type triggers: list
        :param triggers: **[REQUIRED]**

          The JSON block of configuration information for each trigger.

          - *(dict) --*

            Information about a trigger for a repository.

            - **name** *(string) --* **[REQUIRED]**

              The name of the trigger.

            - **destinationArn** *(string) --* **[REQUIRED]**

              The ARN of the resource that is the target for a trigger (for example, the ARN of a
              topic in Amazon SNS).

            - **customData** *(string) --*

              Any custom data associated with the trigger to be included in the information sent to
              the target of the trigger.

            - **branches** *(list) --*

              The branches to be included in the trigger configuration. If you specify an empty
              array, the trigger applies to all branches.

              .. note::

                Although no content is required in the array, you must include the array itself.

              - *(string) --*

            - **events** *(list) --* **[REQUIRED]**

              The repository events that cause the trigger to run actions in another service, such
              as sending a notification through Amazon SNS.

              .. note::

                The valid value "all" cannot be used with any other values.

              - *(string) --*

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'configurationId': 'string'
            }
          **Response Structure**

          - *(dict) --*

            Represents the output of a put repository triggers operation.

            - **configurationId** *(string) --*

              The system-generated unique ID for the create or update operation.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def tag_resource(self, resourceArn: str, tags: Dict[str, str]) -> None:
        """
        Adds or updates tags for a resource in AWS CodeCommit. For a list of valid resources in AWS
        CodeCommit, see `CodeCommit Resources and Operations
        <https://docs.aws.amazon.com/codecommit/latest/userguide/auth-and-access-control-iam-access-control-identity-based.html#arn-formats>`__
        in the *AWS CodeCommit User Guide* .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/codecommit-2015-04-13/TagResource>`_

        **Request Syntax**
        ::

          response = client.tag_resource(
              resourceArn='string',
              tags={
                  'string': 'string'
              }
          )
        :type resourceArn: string
        :param resourceArn: **[REQUIRED]**

          The Amazon Resource Name (ARN) of the resource to which you want to add or update tags.

        :type tags: dict
        :param tags: **[REQUIRED]**

          The key-value pair to use when tagging this repository.

          - *(string) --*

            - *(string) --*

        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def test_repository_triggers(
        self, repositoryName: str, triggers: List[ClientTestRepositoryTriggersTriggersTypeDef]
    ) -> ClientTestRepositoryTriggersResponseTypeDef:
        """
        Tests the functionality of repository triggers by sending information to the trigger target.
        If real data is available in the repository, the test sends data from the last commit. If no
        data is available, sample data is generated.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/codecommit-2015-04-13/TestRepositoryTriggers>`_

        **Request Syntax**
        ::

          response = client.test_repository_triggers(
              repositoryName='string',
              triggers=[
                  {
                      'name': 'string',
                      'destinationArn': 'string',
                      'customData': 'string',
                      'branches': [
                          'string',
                      ],
                      'events': [
                          'all'|'updateReference'|'createReference'|'deleteReference',
                      ]
                  },
              ]
          )
        :type repositoryName: string
        :param repositoryName: **[REQUIRED]**

          The name of the repository in which to test the triggers.

        :type triggers: list
        :param triggers: **[REQUIRED]**

          The list of triggers to test.

          - *(dict) --*

            Information about a trigger for a repository.

            - **name** *(string) --* **[REQUIRED]**

              The name of the trigger.

            - **destinationArn** *(string) --* **[REQUIRED]**

              The ARN of the resource that is the target for a trigger (for example, the ARN of a
              topic in Amazon SNS).

            - **customData** *(string) --*

              Any custom data associated with the trigger to be included in the information sent to
              the target of the trigger.

            - **branches** *(list) --*

              The branches to be included in the trigger configuration. If you specify an empty
              array, the trigger applies to all branches.

              .. note::

                Although no content is required in the array, you must include the array itself.

              - *(string) --*

            - **events** *(list) --* **[REQUIRED]**

              The repository events that cause the trigger to run actions in another service, such
              as sending a notification through Amazon SNS.

              .. note::

                The valid value "all" cannot be used with any other values.

              - *(string) --*

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'successfulExecutions': [
                    'string',
                ],
                'failedExecutions': [
                    {
                        'trigger': 'string',
                        'failureMessage': 'string'
                    },
                ]
            }
          **Response Structure**

          - *(dict) --*

            Represents the output of a test repository triggers operation.

            - **successfulExecutions** *(list) --*

              The list of triggers that were successfully tested. This list provides the names of
              the triggers that were successfully tested, separated by commas.

              - *(string) --*

            - **failedExecutions** *(list) --*

              The list of triggers that were not tested. This list provides the names of the
              triggers that could not be tested, separated by commas.

              - *(dict) --*

                A trigger failed to run.

                - **trigger** *(string) --*

                  The name of the trigger that did not run.

                - **failureMessage** *(string) --*

                  Message information about the trigger that did not run.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def untag_resource(self, resourceArn: str, tagKeys: List[str]) -> None:
        """
        Removes tags for a resource in AWS CodeCommit. For a list of valid resources in AWS
        CodeCommit, see `CodeCommit Resources and Operations
        <https://docs.aws.amazon.com/codecommit/latest/userguide/auth-and-access-control-iam-access-control-identity-based.html#arn-formats>`__
        in the *AWS CodeCommit User Guide* .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/codecommit-2015-04-13/UntagResource>`_

        **Request Syntax**
        ::

          response = client.untag_resource(
              resourceArn='string',
              tagKeys=[
                  'string',
              ]
          )
        :type resourceArn: string
        :param resourceArn: **[REQUIRED]**

          The Amazon Resource Name (ARN) of the resource to which you want to remove tags.

        :type tagKeys: list
        :param tagKeys: **[REQUIRED]**

          The tag key for each tag that you want to remove from the resource.

          - *(string) --*

        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_approval_rule_template_content(
        self,
        approvalRuleTemplateName: str,
        newRuleContent: str,
        existingRuleContentSha256: str = None,
    ) -> ClientUpdateApprovalRuleTemplateContentResponseTypeDef:
        """
        Updates the content of an approval rule template. You can change the number of required
        approvals, the membership of the approval rule, and whether an approval pool is defined.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/codecommit-2015-04-13/UpdateApprovalRuleTemplateContent>`_

        **Request Syntax**
        ::

          response = client.update_approval_rule_template_content(
              approvalRuleTemplateName='string',
              newRuleContent='string',
              existingRuleContentSha256='string'
          )
        :type approvalRuleTemplateName: string
        :param approvalRuleTemplateName: **[REQUIRED]**

          The name of the approval rule template where you want to update the content of the rule.

        :type newRuleContent: string
        :param newRuleContent: **[REQUIRED]**

          The content that replaces the existing content of the rule. Content statements must be
          complete. You cannot provide only the changes.

        :type existingRuleContentSha256: string
        :param existingRuleContentSha256:

          The SHA-256 hash signature for the content of the approval rule. You can retrieve this
          information by using  GetPullRequest .

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'approvalRuleTemplate': {
                    'approvalRuleTemplateId': 'string',
                    'approvalRuleTemplateName': 'string',
                    'approvalRuleTemplateDescription': 'string',
                    'approvalRuleTemplateContent': 'string',
                    'ruleContentSha256': 'string',
                    'lastModifiedDate': datetime(2015, 1, 1),
                    'creationDate': datetime(2015, 1, 1),
                    'lastModifiedUser': 'string'
                }
            }
          **Response Structure**

          - *(dict) --*

            - **approvalRuleTemplate** *(dict) --*

              Returns information about an approval rule template.

              - **approvalRuleTemplateId** *(string) --*

                The system-generated ID of the approval rule template.

              - **approvalRuleTemplateName** *(string) --*

                The name of the approval rule template.

              - **approvalRuleTemplateDescription** *(string) --*

                The description of the approval rule template.

              - **approvalRuleTemplateContent** *(string) --*

                The content of the approval rule template.

              - **ruleContentSha256** *(string) --*

                The SHA-256 hash signature for the content of the approval rule template.

              - **lastModifiedDate** *(datetime) --*

                The date the approval rule template was most recently changed, in timestamp format.

              - **creationDate** *(datetime) --*

                The date the approval rule template was created, in timestamp format.

              - **lastModifiedUser** *(string) --*

                The Amazon Resource Name (ARN) of the user who made the most recent changes to the
                approval rule template.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_approval_rule_template_description(
        self, approvalRuleTemplateName: str, approvalRuleTemplateDescription: str
    ) -> ClientUpdateApprovalRuleTemplateDescriptionResponseTypeDef:
        """
        Updates the description for a specified approval rule template.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/codecommit-2015-04-13/UpdateApprovalRuleTemplateDescription>`_

        **Request Syntax**
        ::

          response = client.update_approval_rule_template_description(
              approvalRuleTemplateName='string',
              approvalRuleTemplateDescription='string'
          )
        :type approvalRuleTemplateName: string
        :param approvalRuleTemplateName: **[REQUIRED]**

          The name of the template for which you want to update the description.

        :type approvalRuleTemplateDescription: string
        :param approvalRuleTemplateDescription: **[REQUIRED]**

          The updated description of the approval rule template.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'approvalRuleTemplate': {
                    'approvalRuleTemplateId': 'string',
                    'approvalRuleTemplateName': 'string',
                    'approvalRuleTemplateDescription': 'string',
                    'approvalRuleTemplateContent': 'string',
                    'ruleContentSha256': 'string',
                    'lastModifiedDate': datetime(2015, 1, 1),
                    'creationDate': datetime(2015, 1, 1),
                    'lastModifiedUser': 'string'
                }
            }
          **Response Structure**

          - *(dict) --*

            - **approvalRuleTemplate** *(dict) --*

              The structure and content of the updated approval rule template.

              - **approvalRuleTemplateId** *(string) --*

                The system-generated ID of the approval rule template.

              - **approvalRuleTemplateName** *(string) --*

                The name of the approval rule template.

              - **approvalRuleTemplateDescription** *(string) --*

                The description of the approval rule template.

              - **approvalRuleTemplateContent** *(string) --*

                The content of the approval rule template.

              - **ruleContentSha256** *(string) --*

                The SHA-256 hash signature for the content of the approval rule template.

              - **lastModifiedDate** *(datetime) --*

                The date the approval rule template was most recently changed, in timestamp format.

              - **creationDate** *(datetime) --*

                The date the approval rule template was created, in timestamp format.

              - **lastModifiedUser** *(string) --*

                The Amazon Resource Name (ARN) of the user who made the most recent changes to the
                approval rule template.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_approval_rule_template_name(
        self, oldApprovalRuleTemplateName: str, newApprovalRuleTemplateName: str
    ) -> ClientUpdateApprovalRuleTemplateNameResponseTypeDef:
        """
        Updates the name of a specified approval rule template.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/codecommit-2015-04-13/UpdateApprovalRuleTemplateName>`_

        **Request Syntax**
        ::

          response = client.update_approval_rule_template_name(
              oldApprovalRuleTemplateName='string',
              newApprovalRuleTemplateName='string'
          )
        :type oldApprovalRuleTemplateName: string
        :param oldApprovalRuleTemplateName: **[REQUIRED]**

          The current name of the approval rule template.

        :type newApprovalRuleTemplateName: string
        :param newApprovalRuleTemplateName: **[REQUIRED]**

          The new name you want to apply to the approval rule template.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'approvalRuleTemplate': {
                    'approvalRuleTemplateId': 'string',
                    'approvalRuleTemplateName': 'string',
                    'approvalRuleTemplateDescription': 'string',
                    'approvalRuleTemplateContent': 'string',
                    'ruleContentSha256': 'string',
                    'lastModifiedDate': datetime(2015, 1, 1),
                    'creationDate': datetime(2015, 1, 1),
                    'lastModifiedUser': 'string'
                }
            }
          **Response Structure**

          - *(dict) --*

            - **approvalRuleTemplate** *(dict) --*

              The structure and content of the updated approval rule template.

              - **approvalRuleTemplateId** *(string) --*

                The system-generated ID of the approval rule template.

              - **approvalRuleTemplateName** *(string) --*

                The name of the approval rule template.

              - **approvalRuleTemplateDescription** *(string) --*

                The description of the approval rule template.

              - **approvalRuleTemplateContent** *(string) --*

                The content of the approval rule template.

              - **ruleContentSha256** *(string) --*

                The SHA-256 hash signature for the content of the approval rule template.

              - **lastModifiedDate** *(datetime) --*

                The date the approval rule template was most recently changed, in timestamp format.

              - **creationDate** *(datetime) --*

                The date the approval rule template was created, in timestamp format.

              - **lastModifiedUser** *(string) --*

                The Amazon Resource Name (ARN) of the user who made the most recent changes to the
                approval rule template.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_comment(self, commentId: str, content: str) -> ClientUpdateCommentResponseTypeDef:
        """
        Replaces the contents of a comment.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/codecommit-2015-04-13/UpdateComment>`_

        **Request Syntax**
        ::

          response = client.update_comment(
              commentId='string',
              content='string'
          )
        :type commentId: string
        :param commentId: **[REQUIRED]**

          The system-generated ID of the comment you want to update. To get this ID, use
          GetCommentsForComparedCommit or  GetCommentsForPullRequest .

        :type content: string
        :param content: **[REQUIRED]**

          The updated content to replace the existing content of the comment.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'comment': {
                    'commentId': 'string',
                    'content': 'string',
                    'inReplyTo': 'string',
                    'creationDate': datetime(2015, 1, 1),
                    'lastModifiedDate': datetime(2015, 1, 1),
                    'authorArn': 'string',
                    'deleted': True|False,
                    'clientRequestToken': 'string'
                }
            }
          **Response Structure**

          - *(dict) --*

            - **comment** *(dict) --*

              Information about the updated comment.

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
                ensures the request cannot be repeated with a changed parameter. If a request is
                received with the same parameters and a token is included, the request returns
                information about the initial request that used that token.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_default_branch(self, repositoryName: str, defaultBranchName: str) -> None:
        """
        Sets or changes the default branch name for the specified repository.

        .. note::

          If you use this operation to change the default branch name to the current default branch
          name, a success message is returned even though the default branch did not change.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/codecommit-2015-04-13/UpdateDefaultBranch>`_

        **Request Syntax**
        ::

          response = client.update_default_branch(
              repositoryName='string',
              defaultBranchName='string'
          )
        :type repositoryName: string
        :param repositoryName: **[REQUIRED]**

          The name of the repository to set or change the default branch for.

        :type defaultBranchName: string
        :param defaultBranchName: **[REQUIRED]**

          The name of the branch to set as the default.

        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_pull_request_approval_rule_content(
        self,
        pullRequestId: str,
        approvalRuleName: str,
        newRuleContent: str,
        existingRuleContentSha256: str = None,
    ) -> ClientUpdatePullRequestApprovalRuleContentResponseTypeDef:
        """
        Updates the structure of an approval rule created specifically for a pull request. For
        example, you can change the number of required approvers and the approval pool for
        approvers.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/codecommit-2015-04-13/UpdatePullRequestApprovalRuleContent>`_

        **Request Syntax**
        ::

          response = client.update_pull_request_approval_rule_content(
              pullRequestId='string',
              approvalRuleName='string',
              existingRuleContentSha256='string',
              newRuleContent='string'
          )
        :type pullRequestId: string
        :param pullRequestId: **[REQUIRED]**

          The system-generated ID of the pull request.

        :type approvalRuleName: string
        :param approvalRuleName: **[REQUIRED]**

          The name of the approval rule you want to update.

        :type existingRuleContentSha256: string
        :param existingRuleContentSha256:

          The SHA-256 hash signature for the content of the approval rule. You can retrieve this
          information by using  GetPullRequest .

        :type newRuleContent: string
        :param newRuleContent: **[REQUIRED]**

          The updated content for the approval rule.

          .. note::

            When you update the content of the approval rule, you can specify approvers in an
            approval pool in one of two ways:

            * **CodeCommitApprovers** : This option only requires an AWS account and a resource. It
            can be used for both IAM users and federated access users whose name matches the
            provided resource name. This is a very powerful option that offers a great deal of
            flexibility. For example, if you specify the AWS account *123456789012* and *Mary_Major*
            , all of the following are counted as approvals coming from that user:

              * An IAM user in the account (arn:aws:iam::*123456789012* :user/*Mary_Major* )

              * A federated user identified in IAM as Mary_Major (arn:aws:sts::*123456789012*
              :federated-user/*Mary_Major* )

            This option does not recognize an active session of someone assuming the role of
            CodeCommitReview with a role session name of *Mary_Major* (arn:aws:sts::*123456789012*
            :assumed-role/CodeCommitReview/*Mary_Major* ) unless you include a wildcard
            (*Mary_Major).

            * **Fully qualified ARN** : This option allows you to specify the fully qualified Amazon
            Resource Name (ARN) of the IAM user or role.

            For more information about IAM ARNs, wildcards, and formats, see `IAM Identifiers
            <https://docs.aws.amazon.com/iam/latest/UserGuide/reference_identifiers.html>`__ in the
            *IAM User Guide* .

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'approvalRule': {
                    'approvalRuleId': 'string',
                    'approvalRuleName': 'string',
                    'approvalRuleContent': 'string',
                    'ruleContentSha256': 'string',
                    'lastModifiedDate': datetime(2015, 1, 1),
                    'creationDate': datetime(2015, 1, 1),
                    'lastModifiedUser': 'string',
                    'originApprovalRuleTemplate': {
                        'approvalRuleTemplateId': 'string',
                        'approvalRuleTemplateName': 'string'
                    }
                }
            }
          **Response Structure**

          - *(dict) --*

            - **approvalRule** *(dict) --*

              Information about the updated approval rule.

              - **approvalRuleId** *(string) --*

                The system-generated ID of the approval rule.

              - **approvalRuleName** *(string) --*

                The name of the approval rule.

              - **approvalRuleContent** *(string) --*

                The content of the approval rule.

              - **ruleContentSha256** *(string) --*

                The SHA-256 hash signature for the content of the approval rule.

              - **lastModifiedDate** *(datetime) --*

                The date the approval rule was most recently changed, in timestamp format.

              - **creationDate** *(datetime) --*

                The date the approval rule was created, in timestamp format.

              - **lastModifiedUser** *(string) --*

                The Amazon Resource Name (ARN) of the user who made the most recent changes to the
                approval rule.

              - **originApprovalRuleTemplate** *(dict) --*

                The approval rule template used to create the rule.

                - **approvalRuleTemplateId** *(string) --*

                  The ID of the template that created the approval rule.

                - **approvalRuleTemplateName** *(string) --*

                  The name of the template that created the approval rule.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_pull_request_approval_state(
        self, pullRequestId: str, revisionId: str, approvalState: Literal["APPROVE", "REVOKE"]
    ) -> None:
        """
        Updates the state of a user's approval on a pull request. The user is derived from the
        signed-in account when the request is made.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/codecommit-2015-04-13/UpdatePullRequestApprovalState>`_

        **Request Syntax**
        ::

          response = client.update_pull_request_approval_state(
              pullRequestId='string',
              revisionId='string',
              approvalState='APPROVE'|'REVOKE'
          )
        :type pullRequestId: string
        :param pullRequestId: **[REQUIRED]**

          The system-generated ID of the pull request.

        :type revisionId: string
        :param revisionId: **[REQUIRED]**

          The system-generated ID of the revision.

        :type approvalState: string
        :param approvalState: **[REQUIRED]**

          The approval state to associate with the user on the pull request.

        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_pull_request_description(
        self, pullRequestId: str, description: str
    ) -> ClientUpdatePullRequestDescriptionResponseTypeDef:
        """
        Replaces the contents of the description of a pull request.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/codecommit-2015-04-13/UpdatePullRequestDescription>`_

        **Request Syntax**
        ::

          response = client.update_pull_request_description(
              pullRequestId='string',
              description='string'
          )
        :type pullRequestId: string
        :param pullRequestId: **[REQUIRED]**

          The system-generated ID of the pull request. To get this ID, use  ListPullRequests .

        :type description: string
        :param description: **[REQUIRED]**

          The updated content of the description for the pull request. This content replaces the
          existing description.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'pullRequest': {
                    'pullRequestId': 'string',
                    'title': 'string',
                    'description': 'string',
                    'lastActivityDate': datetime(2015, 1, 1),
                    'creationDate': datetime(2015, 1, 1),
                    'pullRequestStatus': 'OPEN'|'CLOSED',
                    'authorArn': 'string',
                    'pullRequestTargets': [
                        {
                            'repositoryName': 'string',
                            'sourceReference': 'string',
                            'destinationReference': 'string',
                            'destinationCommit': 'string',
                            'sourceCommit': 'string',
                            'mergeBase': 'string',
                            'mergeMetadata': {
                                'isMerged': True|False,
                                'mergedBy': 'string',
                                'mergeCommitId': 'string',
                                'mergeOption': 'FAST_FORWARD_MERGE'|'SQUASH_MERGE'|'THREE_WAY_MERGE'
                            }
                        },
                    ],
                    'clientRequestToken': 'string',
                    'revisionId': 'string',
                    'approvalRules': [
                        {
                            'approvalRuleId': 'string',
                            'approvalRuleName': 'string',
                            'approvalRuleContent': 'string',
                            'ruleContentSha256': 'string',
                            'lastModifiedDate': datetime(2015, 1, 1),
                            'creationDate': datetime(2015, 1, 1),
                            'lastModifiedUser': 'string',
                            'originApprovalRuleTemplate': {
                                'approvalRuleTemplateId': 'string',
                                'approvalRuleTemplateName': 'string'
                            }
                        },
                    ]
                }
            }
          **Response Structure**

          - *(dict) --*

            - **pullRequest** *(dict) --*

              Information about the updated pull request.

              - **pullRequestId** *(string) --*

                The system-generated ID of the pull request.

              - **title** *(string) --*

                The user-defined title of the pull request. This title is displayed in the list of
                pull requests to other repository users.

              - **description** *(string) --*

                The user-defined description of the pull request. This description can be used to
                clarify what should be reviewed and other details of the request.

              - **lastActivityDate** *(datetime) --*

                The day and time of the last user or system activity on the pull request, in
                timestamp format.

              - **creationDate** *(datetime) --*

                The date and time the pull request was originally created, in timestamp format.

              - **pullRequestStatus** *(string) --*

                The status of the pull request. Pull request status can only change from ``OPEN`` to
                ``CLOSED`` .

              - **authorArn** *(string) --*

                The Amazon Resource Name (ARN) of the user who created the pull request.

              - **pullRequestTargets** *(list) --*

                The targets of the pull request, including the source branch and destination branch
                for the pull request.

                - *(dict) --*

                  Returns information about a pull request target.

                  - **repositoryName** *(string) --*

                    The name of the repository that contains the pull request source and destination
                    branches.

                  - **sourceReference** *(string) --*

                    The branch of the repository that contains the changes for the pull request.
                    Also known as the source branch.

                  - **destinationReference** *(string) --*

                    The branch of the repository where the pull request changes are merged. Also
                    known as the destination branch.

                  - **destinationCommit** *(string) --*

                    The full commit ID that is the tip of the destination branch. This is the commit
                    where the pull request was or will be merged.

                  - **sourceCommit** *(string) --*

                    The full commit ID of the tip of the source branch used to create the pull
                    request. If the pull request branch is updated by a push while the pull request
                    is open, the commit ID changes to reflect the new tip of the branch.

                  - **mergeBase** *(string) --*

                    The commit ID of the most recent commit that the source branch and the
                    destination branch have in common.

                  - **mergeMetadata** *(dict) --*

                    Returns metadata about the state of the merge, including whether the merge has
                    been made.

                    - **isMerged** *(boolean) --*

                      A Boolean value indicating whether the merge has been made.

                    - **mergedBy** *(string) --*

                      The Amazon Resource Name (ARN) of the user who merged the branches.

                    - **mergeCommitId** *(string) --*

                      The commit ID for the merge commit, if any.

                    - **mergeOption** *(string) --*

                      The merge strategy used in the merge.

              - **clientRequestToken** *(string) --*

                A unique, client-generated idempotency token that, when provided in a request,
                ensures the request cannot be repeated with a changed parameter. If a request is
                received with the same parameters and a token is included, the request returns
                information about the initial request that used that token.

              - **revisionId** *(string) --*

                The system-generated revision ID for the pull request.

              - **approvalRules** *(list) --*

                The approval rules applied to the pull request.

                - *(dict) --*

                  Returns information about an approval rule.

                  - **approvalRuleId** *(string) --*

                    The system-generated ID of the approval rule.

                  - **approvalRuleName** *(string) --*

                    The name of the approval rule.

                  - **approvalRuleContent** *(string) --*

                    The content of the approval rule.

                  - **ruleContentSha256** *(string) --*

                    The SHA-256 hash signature for the content of the approval rule.

                  - **lastModifiedDate** *(datetime) --*

                    The date the approval rule was most recently changed, in timestamp format.

                  - **creationDate** *(datetime) --*

                    The date the approval rule was created, in timestamp format.

                  - **lastModifiedUser** *(string) --*

                    The Amazon Resource Name (ARN) of the user who made the most recent changes to
                    the approval rule.

                  - **originApprovalRuleTemplate** *(dict) --*

                    The approval rule template used to create the rule.

                    - **approvalRuleTemplateId** *(string) --*

                      The ID of the template that created the approval rule.

                    - **approvalRuleTemplateName** *(string) --*

                      The name of the template that created the approval rule.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_pull_request_status(
        self, pullRequestId: str, pullRequestStatus: Literal["OPEN", "CLOSED"]
    ) -> ClientUpdatePullRequestStatusResponseTypeDef:
        """
        Updates the status of a pull request.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/codecommit-2015-04-13/UpdatePullRequestStatus>`_

        **Request Syntax**
        ::

          response = client.update_pull_request_status(
              pullRequestId='string',
              pullRequestStatus='OPEN'|'CLOSED'
          )
        :type pullRequestId: string
        :param pullRequestId: **[REQUIRED]**

          The system-generated ID of the pull request. To get this ID, use  ListPullRequests .

        :type pullRequestStatus: string
        :param pullRequestStatus: **[REQUIRED]**

          The status of the pull request. The only valid operations are to update the status from
          ``OPEN`` to ``OPEN`` , ``OPEN`` to ``CLOSED`` or from ``CLOSED`` to ``CLOSED`` .

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'pullRequest': {
                    'pullRequestId': 'string',
                    'title': 'string',
                    'description': 'string',
                    'lastActivityDate': datetime(2015, 1, 1),
                    'creationDate': datetime(2015, 1, 1),
                    'pullRequestStatus': 'OPEN'|'CLOSED',
                    'authorArn': 'string',
                    'pullRequestTargets': [
                        {
                            'repositoryName': 'string',
                            'sourceReference': 'string',
                            'destinationReference': 'string',
                            'destinationCommit': 'string',
                            'sourceCommit': 'string',
                            'mergeBase': 'string',
                            'mergeMetadata': {
                                'isMerged': True|False,
                                'mergedBy': 'string',
                                'mergeCommitId': 'string',
                                'mergeOption': 'FAST_FORWARD_MERGE'|'SQUASH_MERGE'|'THREE_WAY_MERGE'
                            }
                        },
                    ],
                    'clientRequestToken': 'string',
                    'revisionId': 'string',
                    'approvalRules': [
                        {
                            'approvalRuleId': 'string',
                            'approvalRuleName': 'string',
                            'approvalRuleContent': 'string',
                            'ruleContentSha256': 'string',
                            'lastModifiedDate': datetime(2015, 1, 1),
                            'creationDate': datetime(2015, 1, 1),
                            'lastModifiedUser': 'string',
                            'originApprovalRuleTemplate': {
                                'approvalRuleTemplateId': 'string',
                                'approvalRuleTemplateName': 'string'
                            }
                        },
                    ]
                }
            }
          **Response Structure**

          - *(dict) --*

            - **pullRequest** *(dict) --*

              Information about the pull request.

              - **pullRequestId** *(string) --*

                The system-generated ID of the pull request.

              - **title** *(string) --*

                The user-defined title of the pull request. This title is displayed in the list of
                pull requests to other repository users.

              - **description** *(string) --*

                The user-defined description of the pull request. This description can be used to
                clarify what should be reviewed and other details of the request.

              - **lastActivityDate** *(datetime) --*

                The day and time of the last user or system activity on the pull request, in
                timestamp format.

              - **creationDate** *(datetime) --*

                The date and time the pull request was originally created, in timestamp format.

              - **pullRequestStatus** *(string) --*

                The status of the pull request. Pull request status can only change from ``OPEN`` to
                ``CLOSED`` .

              - **authorArn** *(string) --*

                The Amazon Resource Name (ARN) of the user who created the pull request.

              - **pullRequestTargets** *(list) --*

                The targets of the pull request, including the source branch and destination branch
                for the pull request.

                - *(dict) --*

                  Returns information about a pull request target.

                  - **repositoryName** *(string) --*

                    The name of the repository that contains the pull request source and destination
                    branches.

                  - **sourceReference** *(string) --*

                    The branch of the repository that contains the changes for the pull request.
                    Also known as the source branch.

                  - **destinationReference** *(string) --*

                    The branch of the repository where the pull request changes are merged. Also
                    known as the destination branch.

                  - **destinationCommit** *(string) --*

                    The full commit ID that is the tip of the destination branch. This is the commit
                    where the pull request was or will be merged.

                  - **sourceCommit** *(string) --*

                    The full commit ID of the tip of the source branch used to create the pull
                    request. If the pull request branch is updated by a push while the pull request
                    is open, the commit ID changes to reflect the new tip of the branch.

                  - **mergeBase** *(string) --*

                    The commit ID of the most recent commit that the source branch and the
                    destination branch have in common.

                  - **mergeMetadata** *(dict) --*

                    Returns metadata about the state of the merge, including whether the merge has
                    been made.

                    - **isMerged** *(boolean) --*

                      A Boolean value indicating whether the merge has been made.

                    - **mergedBy** *(string) --*

                      The Amazon Resource Name (ARN) of the user who merged the branches.

                    - **mergeCommitId** *(string) --*

                      The commit ID for the merge commit, if any.

                    - **mergeOption** *(string) --*

                      The merge strategy used in the merge.

              - **clientRequestToken** *(string) --*

                A unique, client-generated idempotency token that, when provided in a request,
                ensures the request cannot be repeated with a changed parameter. If a request is
                received with the same parameters and a token is included, the request returns
                information about the initial request that used that token.

              - **revisionId** *(string) --*

                The system-generated revision ID for the pull request.

              - **approvalRules** *(list) --*

                The approval rules applied to the pull request.

                - *(dict) --*

                  Returns information about an approval rule.

                  - **approvalRuleId** *(string) --*

                    The system-generated ID of the approval rule.

                  - **approvalRuleName** *(string) --*

                    The name of the approval rule.

                  - **approvalRuleContent** *(string) --*

                    The content of the approval rule.

                  - **ruleContentSha256** *(string) --*

                    The SHA-256 hash signature for the content of the approval rule.

                  - **lastModifiedDate** *(datetime) --*

                    The date the approval rule was most recently changed, in timestamp format.

                  - **creationDate** *(datetime) --*

                    The date the approval rule was created, in timestamp format.

                  - **lastModifiedUser** *(string) --*

                    The Amazon Resource Name (ARN) of the user who made the most recent changes to
                    the approval rule.

                  - **originApprovalRuleTemplate** *(dict) --*

                    The approval rule template used to create the rule.

                    - **approvalRuleTemplateId** *(string) --*

                      The ID of the template that created the approval rule.

                    - **approvalRuleTemplateName** *(string) --*

                      The name of the template that created the approval rule.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_pull_request_title(
        self, pullRequestId: str, title: str
    ) -> ClientUpdatePullRequestTitleResponseTypeDef:
        """
        Replaces the title of a pull request.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/codecommit-2015-04-13/UpdatePullRequestTitle>`_

        **Request Syntax**
        ::

          response = client.update_pull_request_title(
              pullRequestId='string',
              title='string'
          )
        :type pullRequestId: string
        :param pullRequestId: **[REQUIRED]**

          The system-generated ID of the pull request. To get this ID, use  ListPullRequests .

        :type title: string
        :param title: **[REQUIRED]**

          The updated title of the pull request. This replaces the existing title.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'pullRequest': {
                    'pullRequestId': 'string',
                    'title': 'string',
                    'description': 'string',
                    'lastActivityDate': datetime(2015, 1, 1),
                    'creationDate': datetime(2015, 1, 1),
                    'pullRequestStatus': 'OPEN'|'CLOSED',
                    'authorArn': 'string',
                    'pullRequestTargets': [
                        {
                            'repositoryName': 'string',
                            'sourceReference': 'string',
                            'destinationReference': 'string',
                            'destinationCommit': 'string',
                            'sourceCommit': 'string',
                            'mergeBase': 'string',
                            'mergeMetadata': {
                                'isMerged': True|False,
                                'mergedBy': 'string',
                                'mergeCommitId': 'string',
                                'mergeOption': 'FAST_FORWARD_MERGE'|'SQUASH_MERGE'|'THREE_WAY_MERGE'
                            }
                        },
                    ],
                    'clientRequestToken': 'string',
                    'revisionId': 'string',
                    'approvalRules': [
                        {
                            'approvalRuleId': 'string',
                            'approvalRuleName': 'string',
                            'approvalRuleContent': 'string',
                            'ruleContentSha256': 'string',
                            'lastModifiedDate': datetime(2015, 1, 1),
                            'creationDate': datetime(2015, 1, 1),
                            'lastModifiedUser': 'string',
                            'originApprovalRuleTemplate': {
                                'approvalRuleTemplateId': 'string',
                                'approvalRuleTemplateName': 'string'
                            }
                        },
                    ]
                }
            }
          **Response Structure**

          - *(dict) --*

            - **pullRequest** *(dict) --*

              Information about the updated pull request.

              - **pullRequestId** *(string) --*

                The system-generated ID of the pull request.

              - **title** *(string) --*

                The user-defined title of the pull request. This title is displayed in the list of
                pull requests to other repository users.

              - **description** *(string) --*

                The user-defined description of the pull request. This description can be used to
                clarify what should be reviewed and other details of the request.

              - **lastActivityDate** *(datetime) --*

                The day and time of the last user or system activity on the pull request, in
                timestamp format.

              - **creationDate** *(datetime) --*

                The date and time the pull request was originally created, in timestamp format.

              - **pullRequestStatus** *(string) --*

                The status of the pull request. Pull request status can only change from ``OPEN`` to
                ``CLOSED`` .

              - **authorArn** *(string) --*

                The Amazon Resource Name (ARN) of the user who created the pull request.

              - **pullRequestTargets** *(list) --*

                The targets of the pull request, including the source branch and destination branch
                for the pull request.

                - *(dict) --*

                  Returns information about a pull request target.

                  - **repositoryName** *(string) --*

                    The name of the repository that contains the pull request source and destination
                    branches.

                  - **sourceReference** *(string) --*

                    The branch of the repository that contains the changes for the pull request.
                    Also known as the source branch.

                  - **destinationReference** *(string) --*

                    The branch of the repository where the pull request changes are merged. Also
                    known as the destination branch.

                  - **destinationCommit** *(string) --*

                    The full commit ID that is the tip of the destination branch. This is the commit
                    where the pull request was or will be merged.

                  - **sourceCommit** *(string) --*

                    The full commit ID of the tip of the source branch used to create the pull
                    request. If the pull request branch is updated by a push while the pull request
                    is open, the commit ID changes to reflect the new tip of the branch.

                  - **mergeBase** *(string) --*

                    The commit ID of the most recent commit that the source branch and the
                    destination branch have in common.

                  - **mergeMetadata** *(dict) --*

                    Returns metadata about the state of the merge, including whether the merge has
                    been made.

                    - **isMerged** *(boolean) --*

                      A Boolean value indicating whether the merge has been made.

                    - **mergedBy** *(string) --*

                      The Amazon Resource Name (ARN) of the user who merged the branches.

                    - **mergeCommitId** *(string) --*

                      The commit ID for the merge commit, if any.

                    - **mergeOption** *(string) --*

                      The merge strategy used in the merge.

              - **clientRequestToken** *(string) --*

                A unique, client-generated idempotency token that, when provided in a request,
                ensures the request cannot be repeated with a changed parameter. If a request is
                received with the same parameters and a token is included, the request returns
                information about the initial request that used that token.

              - **revisionId** *(string) --*

                The system-generated revision ID for the pull request.

              - **approvalRules** *(list) --*

                The approval rules applied to the pull request.

                - *(dict) --*

                  Returns information about an approval rule.

                  - **approvalRuleId** *(string) --*

                    The system-generated ID of the approval rule.

                  - **approvalRuleName** *(string) --*

                    The name of the approval rule.

                  - **approvalRuleContent** *(string) --*

                    The content of the approval rule.

                  - **ruleContentSha256** *(string) --*

                    The SHA-256 hash signature for the content of the approval rule.

                  - **lastModifiedDate** *(datetime) --*

                    The date the approval rule was most recently changed, in timestamp format.

                  - **creationDate** *(datetime) --*

                    The date the approval rule was created, in timestamp format.

                  - **lastModifiedUser** *(string) --*

                    The Amazon Resource Name (ARN) of the user who made the most recent changes to
                    the approval rule.

                  - **originApprovalRuleTemplate** *(dict) --*

                    The approval rule template used to create the rule.

                    - **approvalRuleTemplateId** *(string) --*

                      The ID of the template that created the approval rule.

                    - **approvalRuleTemplateName** *(string) --*

                      The name of the template that created the approval rule.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_repository_description(
        self, repositoryName: str, repositoryDescription: str = None
    ) -> None:
        """
        Sets or changes the comment or description for a repository.

        .. note::

          The description field for a repository accepts all HTML characters and all valid Unicode
          characters. Applications that do not HTML-encode the description and display it in a
          webpage can expose users to potentially malicious code. Make sure that you HTML-encode the
          description field in any application that uses this API to display the repository
          description on a webpage.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/codecommit-2015-04-13/UpdateRepositoryDescription>`_

        **Request Syntax**
        ::

          response = client.update_repository_description(
              repositoryName='string',
              repositoryDescription='string'
          )
        :type repositoryName: string
        :param repositoryName: **[REQUIRED]**

          The name of the repository to set or change the comment or description for.

        :type repositoryDescription: string
        :param repositoryDescription:

          The new comment or description for the specified repository. Repository descriptions are
          limited to 1,000 characters.

        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_repository_name(self, oldName: str, newName: str) -> None:
        """
        Renames a repository. The repository name must be unique across the calling AWS account.
        Repository names are limited to 100 alphanumeric, dash, and underscore characters, and
        cannot include certain characters. The suffix .git is prohibited. For more information about
        the limits on repository names, see `Limits
        <https://docs.aws.amazon.com/codecommit/latest/userguide/limits.html>`__ in the AWS
        CodeCommit User Guide.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/codecommit-2015-04-13/UpdateRepositoryName>`_

        **Request Syntax**
        ::

          response = client.update_repository_name(
              oldName='string',
              newName='string'
          )
        :type oldName: string
        :param oldName: **[REQUIRED]**

          The current name of the repository.

        :type newName: string
        :param newName: **[REQUIRED]**

          The new name for the repository.

        :returns: None
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_pull_request_events"]
    ) -> paginator_scope.DescribePullRequestEventsPaginator:
        """
        Get Paginator for `describe_pull_request_events` operation.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["get_comments_for_compared_commit"]
    ) -> paginator_scope.GetCommentsForComparedCommitPaginator:
        """
        Get Paginator for `get_comments_for_compared_commit` operation.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["get_comments_for_pull_request"]
    ) -> paginator_scope.GetCommentsForPullRequestPaginator:
        """
        Get Paginator for `get_comments_for_pull_request` operation.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["get_differences"]
    ) -> paginator_scope.GetDifferencesPaginator:
        """
        Get Paginator for `get_differences` operation.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_branches"]
    ) -> paginator_scope.ListBranchesPaginator:
        """
        Get Paginator for `list_branches` operation.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_pull_requests"]
    ) -> paginator_scope.ListPullRequestsPaginator:
        """
        Get Paginator for `list_pull_requests` operation.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_repositories"]
    ) -> paginator_scope.ListRepositoriesPaginator:
        """
        Get Paginator for `list_repositories` operation.
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
    ActorDoesNotExistException: Boto3ClientError
    ApprovalRuleContentRequiredException: Boto3ClientError
    ApprovalRuleDoesNotExistException: Boto3ClientError
    ApprovalRuleNameAlreadyExistsException: Boto3ClientError
    ApprovalRuleNameRequiredException: Boto3ClientError
    ApprovalRuleTemplateContentRequiredException: Boto3ClientError
    ApprovalRuleTemplateDoesNotExistException: Boto3ClientError
    ApprovalRuleTemplateInUseException: Boto3ClientError
    ApprovalRuleTemplateNameAlreadyExistsException: Boto3ClientError
    ApprovalRuleTemplateNameRequiredException: Boto3ClientError
    ApprovalStateRequiredException: Boto3ClientError
    AuthorDoesNotExistException: Boto3ClientError
    BeforeCommitIdAndAfterCommitIdAreSameException: Boto3ClientError
    BlobIdDoesNotExistException: Boto3ClientError
    BlobIdRequiredException: Boto3ClientError
    BranchDoesNotExistException: Boto3ClientError
    BranchNameExistsException: Boto3ClientError
    BranchNameIsTagNameException: Boto3ClientError
    BranchNameRequiredException: Boto3ClientError
    CannotDeleteApprovalRuleFromTemplateException: Boto3ClientError
    CannotModifyApprovalRuleFromTemplateException: Boto3ClientError
    ClientError: Boto3ClientError
    ClientRequestTokenRequiredException: Boto3ClientError
    CommentContentRequiredException: Boto3ClientError
    CommentContentSizeLimitExceededException: Boto3ClientError
    CommentDeletedException: Boto3ClientError
    CommentDoesNotExistException: Boto3ClientError
    CommentIdRequiredException: Boto3ClientError
    CommentNotCreatedByCallerException: Boto3ClientError
    CommitDoesNotExistException: Boto3ClientError
    CommitIdDoesNotExistException: Boto3ClientError
    CommitIdRequiredException: Boto3ClientError
    CommitIdsLimitExceededException: Boto3ClientError
    CommitIdsListRequiredException: Boto3ClientError
    CommitMessageLengthExceededException: Boto3ClientError
    CommitRequiredException: Boto3ClientError
    ConcurrentReferenceUpdateException: Boto3ClientError
    DefaultBranchCannotBeDeletedException: Boto3ClientError
    DirectoryNameConflictsWithFileNameException: Boto3ClientError
    EncryptionIntegrityChecksFailedException: Boto3ClientError
    EncryptionKeyAccessDeniedException: Boto3ClientError
    EncryptionKeyDisabledException: Boto3ClientError
    EncryptionKeyNotFoundException: Boto3ClientError
    EncryptionKeyUnavailableException: Boto3ClientError
    FileContentAndSourceFileSpecifiedException: Boto3ClientError
    FileContentRequiredException: Boto3ClientError
    FileContentSizeLimitExceededException: Boto3ClientError
    FileDoesNotExistException: Boto3ClientError
    FileEntryRequiredException: Boto3ClientError
    FileModeRequiredException: Boto3ClientError
    FileNameConflictsWithDirectoryNameException: Boto3ClientError
    FilePathConflictsWithSubmodulePathException: Boto3ClientError
    FileTooLargeException: Boto3ClientError
    FolderContentSizeLimitExceededException: Boto3ClientError
    FolderDoesNotExistException: Boto3ClientError
    IdempotencyParameterMismatchException: Boto3ClientError
    InvalidActorArnException: Boto3ClientError
    InvalidApprovalRuleContentException: Boto3ClientError
    InvalidApprovalRuleNameException: Boto3ClientError
    InvalidApprovalRuleTemplateContentException: Boto3ClientError
    InvalidApprovalRuleTemplateDescriptionException: Boto3ClientError
    InvalidApprovalRuleTemplateNameException: Boto3ClientError
    InvalidApprovalStateException: Boto3ClientError
    InvalidAuthorArnException: Boto3ClientError
    InvalidBlobIdException: Boto3ClientError
    InvalidBranchNameException: Boto3ClientError
    InvalidClientRequestTokenException: Boto3ClientError
    InvalidCommentIdException: Boto3ClientError
    InvalidCommitException: Boto3ClientError
    InvalidCommitIdException: Boto3ClientError
    InvalidConflictDetailLevelException: Boto3ClientError
    InvalidConflictResolutionException: Boto3ClientError
    InvalidConflictResolutionStrategyException: Boto3ClientError
    InvalidContinuationTokenException: Boto3ClientError
    InvalidDeletionParameterException: Boto3ClientError
    InvalidDescriptionException: Boto3ClientError
    InvalidDestinationCommitSpecifierException: Boto3ClientError
    InvalidEmailException: Boto3ClientError
    InvalidFileLocationException: Boto3ClientError
    InvalidFileModeException: Boto3ClientError
    InvalidFilePositionException: Boto3ClientError
    InvalidMaxConflictFilesException: Boto3ClientError
    InvalidMaxMergeHunksException: Boto3ClientError
    InvalidMaxResultsException: Boto3ClientError
    InvalidMergeOptionException: Boto3ClientError
    InvalidOrderException: Boto3ClientError
    InvalidOverrideStatusException: Boto3ClientError
    InvalidParentCommitIdException: Boto3ClientError
    InvalidPathException: Boto3ClientError
    InvalidPullRequestEventTypeException: Boto3ClientError
    InvalidPullRequestIdException: Boto3ClientError
    InvalidPullRequestStatusException: Boto3ClientError
    InvalidPullRequestStatusUpdateException: Boto3ClientError
    InvalidReferenceNameException: Boto3ClientError
    InvalidRelativeFileVersionEnumException: Boto3ClientError
    InvalidReplacementContentException: Boto3ClientError
    InvalidReplacementTypeException: Boto3ClientError
    InvalidRepositoryDescriptionException: Boto3ClientError
    InvalidRepositoryNameException: Boto3ClientError
    InvalidRepositoryTriggerBranchNameException: Boto3ClientError
    InvalidRepositoryTriggerCustomDataException: Boto3ClientError
    InvalidRepositoryTriggerDestinationArnException: Boto3ClientError
    InvalidRepositoryTriggerEventsException: Boto3ClientError
    InvalidRepositoryTriggerNameException: Boto3ClientError
    InvalidRepositoryTriggerRegionException: Boto3ClientError
    InvalidResourceArnException: Boto3ClientError
    InvalidRevisionIdException: Boto3ClientError
    InvalidRuleContentSha256Exception: Boto3ClientError
    InvalidSortByException: Boto3ClientError
    InvalidSourceCommitSpecifierException: Boto3ClientError
    InvalidSystemTagUsageException: Boto3ClientError
    InvalidTagKeysListException: Boto3ClientError
    InvalidTagsMapException: Boto3ClientError
    InvalidTargetBranchException: Boto3ClientError
    InvalidTargetException: Boto3ClientError
    InvalidTargetsException: Boto3ClientError
    InvalidTitleException: Boto3ClientError
    ManualMergeRequiredException: Boto3ClientError
    MaximumBranchesExceededException: Boto3ClientError
    MaximumConflictResolutionEntriesExceededException: Boto3ClientError
    MaximumFileContentToLoadExceededException: Boto3ClientError
    MaximumFileEntriesExceededException: Boto3ClientError
    MaximumItemsToCompareExceededException: Boto3ClientError
    MaximumNumberOfApprovalsExceededException: Boto3ClientError
    MaximumOpenPullRequestsExceededException: Boto3ClientError
    MaximumRepositoryNamesExceededException: Boto3ClientError
    MaximumRepositoryTriggersExceededException: Boto3ClientError
    MaximumRuleTemplatesAssociatedWithRepositoryException: Boto3ClientError
    MergeOptionRequiredException: Boto3ClientError
    MultipleConflictResolutionEntriesException: Boto3ClientError
    MultipleRepositoriesInPullRequestException: Boto3ClientError
    NameLengthExceededException: Boto3ClientError
    NoChangeException: Boto3ClientError
    NumberOfRuleTemplatesExceededException: Boto3ClientError
    NumberOfRulesExceededException: Boto3ClientError
    OverrideAlreadySetException: Boto3ClientError
    OverrideStatusRequiredException: Boto3ClientError
    ParentCommitDoesNotExistException: Boto3ClientError
    ParentCommitIdOutdatedException: Boto3ClientError
    ParentCommitIdRequiredException: Boto3ClientError
    PathDoesNotExistException: Boto3ClientError
    PathRequiredException: Boto3ClientError
    PullRequestAlreadyClosedException: Boto3ClientError
    PullRequestApprovalRulesNotSatisfiedException: Boto3ClientError
    PullRequestCannotBeApprovedByAuthorException: Boto3ClientError
    PullRequestDoesNotExistException: Boto3ClientError
    PullRequestIdRequiredException: Boto3ClientError
    PullRequestStatusRequiredException: Boto3ClientError
    PutFileEntryConflictException: Boto3ClientError
    ReferenceDoesNotExistException: Boto3ClientError
    ReferenceNameRequiredException: Boto3ClientError
    ReferenceTypeNotSupportedException: Boto3ClientError
    ReplacementContentRequiredException: Boto3ClientError
    ReplacementTypeRequiredException: Boto3ClientError
    RepositoryDoesNotExistException: Boto3ClientError
    RepositoryLimitExceededException: Boto3ClientError
    RepositoryNameExistsException: Boto3ClientError
    RepositoryNameRequiredException: Boto3ClientError
    RepositoryNamesRequiredException: Boto3ClientError
    RepositoryNotAssociatedWithPullRequestException: Boto3ClientError
    RepositoryTriggerBranchNameListRequiredException: Boto3ClientError
    RepositoryTriggerDestinationArnRequiredException: Boto3ClientError
    RepositoryTriggerEventsListRequiredException: Boto3ClientError
    RepositoryTriggerNameRequiredException: Boto3ClientError
    RepositoryTriggersListRequiredException: Boto3ClientError
    ResourceArnRequiredException: Boto3ClientError
    RestrictedSourceFileException: Boto3ClientError
    RevisionIdRequiredException: Boto3ClientError
    RevisionNotCurrentException: Boto3ClientError
    SameFileContentException: Boto3ClientError
    SamePathRequestException: Boto3ClientError
    SourceAndDestinationAreSameException: Boto3ClientError
    SourceFileOrContentRequiredException: Boto3ClientError
    TagKeysListRequiredException: Boto3ClientError
    TagPolicyException: Boto3ClientError
    TagsMapRequiredException: Boto3ClientError
    TargetRequiredException: Boto3ClientError
    TargetsRequiredException: Boto3ClientError
    TipOfSourceReferenceIsDifferentException: Boto3ClientError
    TipsDivergenceExceededException: Boto3ClientError
    TitleRequiredException: Boto3ClientError
    TooManyTagsException: Boto3ClientError
