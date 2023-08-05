"Main interface for codebuild service Client"
from __future__ import annotations

from typing import Any, Dict, List
from botocore.client import BaseClient
from botocore.exceptions import ClientError as Boto3ClientError
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3.type_defs import Literal, overload

# pylint: disable=import-self
import mypy_boto3_codebuild.client as client_scope

# pylint: disable=import-self
import mypy_boto3_codebuild.paginator as paginator_scope
from mypy_boto3_codebuild.type_defs import (
    ClientBatchDeleteBuildsResponseTypeDef,
    ClientBatchGetBuildsResponseTypeDef,
    ClientBatchGetProjectsResponseTypeDef,
    ClientBatchGetReportGroupsResponseTypeDef,
    ClientBatchGetReportsResponseTypeDef,
    ClientCreateProjectArtifactsTypeDef,
    ClientCreateProjectCacheTypeDef,
    ClientCreateProjectEnvironmentTypeDef,
    ClientCreateProjectLogsConfigTypeDef,
    ClientCreateProjectResponseTypeDef,
    ClientCreateProjectSecondaryArtifactsTypeDef,
    ClientCreateProjectSecondarySourceVersionsTypeDef,
    ClientCreateProjectSecondarySourcesTypeDef,
    ClientCreateProjectSourceTypeDef,
    ClientCreateProjectTagsTypeDef,
    ClientCreateProjectVpcConfigTypeDef,
    ClientCreateReportGroupExportConfigTypeDef,
    ClientCreateReportGroupResponseTypeDef,
    ClientCreateWebhookFilterGroupsTypeDef,
    ClientCreateWebhookResponseTypeDef,
    ClientDeleteSourceCredentialsResponseTypeDef,
    ClientDescribeTestCasesFilterTypeDef,
    ClientDescribeTestCasesResponseTypeDef,
    ClientImportSourceCredentialsResponseTypeDef,
    ClientListBuildsForProjectResponseTypeDef,
    ClientListBuildsResponseTypeDef,
    ClientListCuratedEnvironmentImagesResponseTypeDef,
    ClientListProjectsResponseTypeDef,
    ClientListReportGroupsResponseTypeDef,
    ClientListReportsFilterTypeDef,
    ClientListReportsForReportGroupFilterTypeDef,
    ClientListReportsForReportGroupResponseTypeDef,
    ClientListReportsResponseTypeDef,
    ClientListSourceCredentialsResponseTypeDef,
    ClientStartBuildArtifactsOverrideTypeDef,
    ClientStartBuildCacheOverrideTypeDef,
    ClientStartBuildEnvironmentVariablesOverrideTypeDef,
    ClientStartBuildGitSubmodulesConfigOverrideTypeDef,
    ClientStartBuildLogsConfigOverrideTypeDef,
    ClientStartBuildRegistryCredentialOverrideTypeDef,
    ClientStartBuildResponseTypeDef,
    ClientStartBuildSecondaryArtifactsOverrideTypeDef,
    ClientStartBuildSecondarySourcesOverrideTypeDef,
    ClientStartBuildSecondarySourcesVersionOverrideTypeDef,
    ClientStartBuildSourceAuthOverrideTypeDef,
    ClientStopBuildResponseTypeDef,
    ClientUpdateProjectArtifactsTypeDef,
    ClientUpdateProjectCacheTypeDef,
    ClientUpdateProjectEnvironmentTypeDef,
    ClientUpdateProjectLogsConfigTypeDef,
    ClientUpdateProjectResponseTypeDef,
    ClientUpdateProjectSecondaryArtifactsTypeDef,
    ClientUpdateProjectSecondarySourceVersionsTypeDef,
    ClientUpdateProjectSecondarySourcesTypeDef,
    ClientUpdateProjectSourceTypeDef,
    ClientUpdateProjectTagsTypeDef,
    ClientUpdateProjectVpcConfigTypeDef,
    ClientUpdateReportGroupExportConfigTypeDef,
    ClientUpdateReportGroupResponseTypeDef,
    ClientUpdateWebhookFilterGroupsTypeDef,
    ClientUpdateWebhookResponseTypeDef,
)


__all__ = ("Client",)


class Client(BaseClient):
    exceptions: client_scope.Exceptions

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def batch_delete_builds(self, ids: List[str]) -> ClientBatchDeleteBuildsResponseTypeDef:
        """
        Deletes one or more builds.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/codebuild-2016-10-06/BatchDeleteBuilds>`_

        **Request Syntax**
        ::

          response = client.batch_delete_builds(
              ids=[
                  'string',
              ]
          )
        :type ids: list
        :param ids: **[REQUIRED]**

          The IDs of the builds to delete.

          - *(string) --*

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'buildsDeleted': [
                    'string',
                ],
                'buildsNotDeleted': [
                    {
                        'id': 'string',
                        'statusCode': 'string'
                    },
                ]
            }
          **Response Structure**

          - *(dict) --*

            - **buildsDeleted** *(list) --*

              The IDs of the builds that were successfully deleted.

              - *(string) --*

            - **buildsNotDeleted** *(list) --*

              Information about any builds that could not be successfully deleted.

              - *(dict) --*

                Information about a build that could not be successfully deleted.

                - **id** *(string) --*

                  The ID of the build that could not be successfully deleted.

                - **statusCode** *(string) --*

                  Additional information about the build that could not be successfully deleted.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def batch_get_builds(self, ids: List[str]) -> ClientBatchGetBuildsResponseTypeDef:
        """
        Gets information about one or more builds.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/codebuild-2016-10-06/BatchGetBuilds>`_

        **Request Syntax**
        ::

          response = client.batch_get_builds(
              ids=[
                  'string',
              ]
          )
        :type ids: list
        :param ids: **[REQUIRED]**

          The IDs of the builds.

          - *(string) --*

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'builds': [
                    {
                        'id': 'string',
                        'arn': 'string',
                        'buildNumber': 123,
                        'startTime': datetime(2015, 1, 1),
                        'endTime': datetime(2015, 1, 1),
                        'currentPhase': 'string',
                        'buildStatus':
                        'SUCCEEDED'|'FAILED'|'FAULT'|'TIMED_OUT'|'IN_PROGRESS'
                        |'STOPPED',
                        'sourceVersion': 'string',
                        'resolvedSourceVersion': 'string',
                        'projectName': 'string',
                        'phases': [
                            {
                                'phaseType':
                                'SUBMITTED'|'QUEUED'|'PROVISIONING'
                                |'DOWNLOAD_SOURCE'|'INSTALL'|'PRE_BUILD'
                                |'BUILD'|'POST_BUILD'|'UPLOAD_ARTIFACTS'
                                |'FINALIZING'|'COMPLETED',
                                'phaseStatus':
                                'SUCCEEDED'|'FAILED'|'FAULT'|'TIMED_OUT'
                                |'IN_PROGRESS'|'STOPPED',
                                'startTime': datetime(2015, 1, 1),
                                'endTime': datetime(2015, 1, 1),
                                'durationInSeconds': 123,
                                'contexts': [
                                    {
                                        'statusCode': 'string',
                                        'message': 'string'
                                    },
                                ]
                            },
                        ],
                        'source': {
                            'type':
                            'CODECOMMIT'|'CODEPIPELINE'|'GITHUB'|'S3'
                            |'BITBUCKET'|'GITHUB_ENTERPRISE'|'NO_SOURCE',
                            'location': 'string',
                            'gitCloneDepth': 123,
                            'gitSubmodulesConfig': {
                                'fetchSubmodules': True|False
                            },
                            'buildspec': 'string',
                            'auth': {
                                'type': 'OAUTH',
                                'resource': 'string'
                            },
                            'reportBuildStatus': True|False,
                            'insecureSsl': True|False,
                            'sourceIdentifier': 'string'
                        },
                        'secondarySources': [
                            {
                                'type':
                                'CODECOMMIT'|'CODEPIPELINE'|'GITHUB'|'S3'
                                |'BITBUCKET'|'GITHUB_ENTERPRISE'
                                |'NO_SOURCE',
                                'location': 'string',
                                'gitCloneDepth': 123,
                                'gitSubmodulesConfig': {
                                    'fetchSubmodules': True|False
                                },
                                'buildspec': 'string',
                                'auth': {
                                    'type': 'OAUTH',
                                    'resource': 'string'
                                },
                                'reportBuildStatus': True|False,
                                'insecureSsl': True|False,
                                'sourceIdentifier': 'string'
                            },
                        ],
                        'secondarySourceVersions': [
                            {
                                'sourceIdentifier': 'string',
                                'sourceVersion': 'string'
                            },
                        ],
                        'artifacts': {
                            'location': 'string',
                            'sha256sum': 'string',
                            'md5sum': 'string',
                            'overrideArtifactName': True|False,
                            'encryptionDisabled': True|False,
                            'artifactIdentifier': 'string'
                        },
                        'secondaryArtifacts': [
                            {
                                'location': 'string',
                                'sha256sum': 'string',
                                'md5sum': 'string',
                                'overrideArtifactName': True|False,
                                'encryptionDisabled': True|False,
                                'artifactIdentifier': 'string'
                            },
                        ],
                        'cache': {
                            'type': 'NO_CACHE'|'S3'|'LOCAL',
                            'location': 'string',
                            'modes': [
                                'LOCAL_DOCKER_LAYER_CACHE'|'LOCAL_SOURCE_CACHE'
                                |'LOCAL_CUSTOM_CACHE',
                            ]
                        },
                        'environment': {
                            'type':
                            'WINDOWS_CONTAINER'|'LINUX_CONTAINER'
                            |'LINUX_GPU_CONTAINER'|'ARM_CONTAINER',
                            'image': 'string',
                            'computeType':
                            'BUILD_GENERAL1_SMALL'|'BUILD_GENERAL1_MEDIUM'
                            |'BUILD_GENERAL1_LARGE'|'BUILD_GENERAL1_2XLARGE',
                            'environmentVariables': [
                                {
                                    'name': 'string',
                                    'value': 'string',
                                    'type': 'PLAINTEXT'|'PARAMETER_STORE'|'SECRETS_MANAGER'
                                },
                            ],
                            'privilegedMode': True|False,
                            'certificate': 'string',
                            'registryCredential': {
                                'credential': 'string',
                                'credentialProvider': 'SECRETS_MANAGER'
                            },
                            'imagePullCredentialsType': 'CODEBUILD'|'SERVICE_ROLE'
                        },
                        'serviceRole': 'string',
                        'logs': {
                            'groupName': 'string',
                            'streamName': 'string',
                            'deepLink': 'string',
                            's3DeepLink': 'string',
                            'cloudWatchLogsArn': 'string',
                            's3LogsArn': 'string',
                            'cloudWatchLogs': {
                                'status': 'ENABLED'|'DISABLED',
                                'groupName': 'string',
                                'streamName': 'string'
                            },
                            's3Logs': {
                                'status': 'ENABLED'|'DISABLED',
                                'location': 'string',
                                'encryptionDisabled': True|False
                            }
                        },
                        'timeoutInMinutes': 123,
                        'queuedTimeoutInMinutes': 123,
                        'buildComplete': True|False,
                        'initiator': 'string',
                        'vpcConfig': {
                            'vpcId': 'string',
                            'subnets': [
                                'string',
                            ],
                            'securityGroupIds': [
                                'string',
                            ]
                        },
                        'networkInterface': {
                            'subnetId': 'string',
                            'networkInterfaceId': 'string'
                        },
                        'encryptionKey': 'string',
                        'exportedEnvironmentVariables': [
                            {
                                'name': 'string',
                                'value': 'string'
                            },
                        ],
                        'reportArns': [
                            'string',
                        ]
                    },
                ],
                'buildsNotFound': [
                    'string',
                ]
            }
          **Response Structure**

          - *(dict) --*

            - **builds** *(list) --*

              Information about the requested builds.

              - *(dict) --*

                Information about a build.

                - **id** *(string) --*

                  The unique ID for the build.

                - **arn** *(string) --*

                  The Amazon Resource Name (ARN) of the build.

                - **buildNumber** *(integer) --*

                  The number of the build. For each project, the ``buildNumber`` of its first build
                  is ``1`` . The ``buildNumber`` of each subsequent build is incremented by ``1`` .
                  If a build is deleted, the ``buildNumber`` of other builds does not change.

                - **startTime** *(datetime) --*

                  When the build process started, expressed in Unix time format.

                - **endTime** *(datetime) --*

                  When the build process ended, expressed in Unix time format.

                - **currentPhase** *(string) --*

                  The current build phase.

                - **buildStatus** *(string) --*

                  The current status of the build. Valid values include:

                  * ``FAILED`` : The build failed.

                  * ``FAULT`` : The build faulted.

                  * ``IN_PROGRESS`` : The build is still in progress.

                  * ``STOPPED`` : The build stopped.

                  * ``SUCCEEDED`` : The build succeeded.

                  * ``TIMED_OUT`` : The build timed out.

                - **sourceVersion** *(string) --*

                  Any version identifier for the version of the source code to be built. If
                  ``sourceVersion`` is specified at the project level, then this ``sourceVersion``
                  (at the build level) takes precedence.

                  For more information, see `Source Version Sample with CodeBuild
                  <https://docs.aws.amazon.com/codebuild/latest/userguide/sample-source-version.html>`__
                  in the *AWS CodeBuild User Guide* .

                - **resolvedSourceVersion** *(string) --*

                  An identifier for the version of this build's source code.

                  * For AWS CodeCommit, GitHub, GitHub Enterprise, and BitBucket, the commit ID.

                  * For AWS CodePipeline, the source revision provided by AWS CodePipeline.

                  * For Amazon Simple Storage Service (Amazon S3), this does not apply.

                - **projectName** *(string) --*

                  The name of the AWS CodeBuild project.

                - **phases** *(list) --*

                  Information about all previous build phases that are complete and information
                  about any current build phase that is not yet complete.

                  - *(dict) --*

                    Information about a stage for a build.

                    - **phaseType** *(string) --*

                      The name of the build phase. Valid values include:

                      * ``BUILD`` : Core build activities typically occur in this build phase.

                      * ``COMPLETED`` : The build has been completed.

                      * ``DOWNLOAD_SOURCE`` : Source code is being downloaded in this build phase.

                      * ``FINALIZING`` : The build process is completing in this build phase.

                      * ``INSTALL`` : Installation activities typically occur in this build phase.

                      * ``POST_BUILD`` : Post-build activities typically occur in this build phase.

                      * ``PRE_BUILD`` : Pre-build activities typically occur in this build phase.

                      * ``PROVISIONING`` : The build environment is being set up.

                      * ``QUEUED`` : The build has been submitted and is queued behind other
                      submitted builds.

                      * ``SUBMITTED`` : The build has been submitted.

                      * ``UPLOAD_ARTIFACTS`` : Build output artifacts are being uploaded to the
                      output location.

                    - **phaseStatus** *(string) --*

                      The current status of the build phase. Valid values include:

                      * ``FAILED`` : The build phase failed.

                      * ``FAULT`` : The build phase faulted.

                      * ``IN_PROGRESS`` : The build phase is still in progress.

                      * ``QUEUED`` : The build has been submitted and is queued behind other
                      submitted builds.

                      * ``STOPPED`` : The build phase stopped.

                      * ``SUCCEEDED`` : The build phase succeeded.

                      * ``TIMED_OUT`` : The build phase timed out.

                    - **startTime** *(datetime) --*

                      When the build phase started, expressed in Unix time format.

                    - **endTime** *(datetime) --*

                      When the build phase ended, expressed in Unix time format.

                    - **durationInSeconds** *(integer) --*

                      How long, in seconds, between the starting and ending times of the build's
                      phase.

                    - **contexts** *(list) --*

                      Additional information about a build phase, especially to help troubleshoot a
                      failed build.

                      - *(dict) --*

                        Additional information about a build phase that has an error. You can use
                        this information for troubleshooting.

                        - **statusCode** *(string) --*

                          The status code for the context of the build phase.

                        - **message** *(string) --*

                          An explanation of the build phase's context. This might include a command
                          ID and an exit code.

                - **source** *(dict) --*

                  Information about the source code to be built.

                  - **type** *(string) --*

                    The type of repository that contains the source code to be built. Valid values
                    include:

                    * ``BITBUCKET`` : The source code is in a Bitbucket repository.

                    * ``CODECOMMIT`` : The source code is in an AWS CodeCommit repository.

                    * ``CODEPIPELINE`` : The source code settings are specified in the source action
                    of a pipeline in AWS CodePipeline.

                    * ``GITHUB`` : The source code is in a GitHub repository.

                    * ``GITHUB_ENTERPRISE`` : The source code is in a GitHub Enterprise repository.

                    * ``NO_SOURCE`` : The project does not have input source code.

                    * ``S3`` : The source code is in an Amazon Simple Storage Service (Amazon S3)
                    input bucket.

                  - **location** *(string) --*

                    Information about the location of the source code to be built. Valid values
                    include:

                    * For source code settings that are specified in the source action of a pipeline
                    in AWS CodePipeline, ``location`` should not be specified. If it is specified,
                    AWS CodePipeline ignores it. This is because AWS CodePipeline uses the settings
                    in a pipeline's source action instead of this value.

                    * For source code in an AWS CodeCommit repository, the HTTPS clone URL to the
                    repository that contains the source code and the build spec (for example,
                    ``https://git-codecommit.*region-ID* .amazonaws.com/v1/repos/*repo-name* `` ).

                    * For source code in an Amazon Simple Storage Service (Amazon S3) input bucket,
                    one of the following.

                      * The path to the ZIP file that contains the source code (for example, ``
                      *bucket-name* /*path* /*to* /*object-name* .zip`` ).

                      * The path to the folder that contains the source code (for example, ``
                      *bucket-name* /*path* /*to* /*source-code* /*folder* /`` ).

                    * For source code in a GitHub repository, the HTTPS clone URL to the repository
                    that contains the source and the build spec. You must connect your AWS account
                    to your GitHub account. Use the AWS CodeBuild console to start creating a build
                    project. When you use the console to connect (or reconnect) with GitHub, on the
                    GitHub **Authorize application** page, for **Organization access** , choose
                    **Request access** next to each repository you want to allow AWS CodeBuild to
                    have access to, and then choose **Authorize application** . (After you have
                    connected to your GitHub account, you do not need to finish creating the build
                    project. You can leave the AWS CodeBuild console.) To instruct AWS CodeBuild to
                    use this connection, in the ``source`` object, set the ``auth`` object's
                    ``type`` value to ``OAUTH`` .

                    * For source code in a Bitbucket repository, the HTTPS clone URL to the
                    repository that contains the source and the build spec. You must connect your
                    AWS account to your Bitbucket account. Use the AWS CodeBuild console to start
                    creating a build project. When you use the console to connect (or reconnect)
                    with Bitbucket, on the Bitbucket **Confirm access to your account** page, choose
                    **Grant access** . (After you have connected to your Bitbucket account, you do
                    not need to finish creating the build project. You can leave the AWS CodeBuild
                    console.) To instruct AWS CodeBuild to use this connection, in the ``source``
                    object, set the ``auth`` object's ``type`` value to ``OAUTH`` .

                  - **gitCloneDepth** *(integer) --*

                    Information about the Git clone depth for the build project.

                  - **gitSubmodulesConfig** *(dict) --*

                    Information about the Git submodules configuration for the build project.

                    - **fetchSubmodules** *(boolean) --*

                      Set to true to fetch Git submodules for your AWS CodeBuild build project.

                  - **buildspec** *(string) --*

                    The build spec declaration to use for the builds in this build project.

                    If this value is not specified, a build spec must be included along with the
                    source code to be built.

                  - **auth** *(dict) --*

                    Information about the authorization settings for AWS CodeBuild to access the
                    source code to be built.

                    This information is for the AWS CodeBuild console's use only. Your code should
                    not get or set this information directly.

                    - **type** *(string) --*

                      .. note::

                        This data type is deprecated and is no longer accurate or used.

                      The authorization type to use. The only valid value is ``OAUTH`` , which
                      represents the OAuth authorization type.

                    - **resource** *(string) --*

                      The resource value that applies to the specified authorization type.

                  - **reportBuildStatus** *(boolean) --*

                    Set to true to report the status of a build's start and finish to your source
                    provider. This option is valid only when your source provider is GitHub, GitHub
                    Enterprise, or Bitbucket. If this is set and you use a different source
                    provider, an invalidInputException is thrown.

                    .. note::

                      The status of a build triggered by a webhook is always reported to your source
                      provider.

                  - **insecureSsl** *(boolean) --*

                    Enable this flag to ignore SSL warnings while connecting to the project source
                    code.

                  - **sourceIdentifier** *(string) --*

                    An identifier for this project source.

                - **secondarySources** *(list) --*

                  An array of ``ProjectSource`` objects.

                  - *(dict) --*

                    Information about the build input source code for the build project.

                    - **type** *(string) --*

                      The type of repository that contains the source code to be built. Valid values
                      include:

                      * ``BITBUCKET`` : The source code is in a Bitbucket repository.

                      * ``CODECOMMIT`` : The source code is in an AWS CodeCommit repository.

                      * ``CODEPIPELINE`` : The source code settings are specified in the source
                      action of a pipeline in AWS CodePipeline.

                      * ``GITHUB`` : The source code is in a GitHub repository.

                      * ``GITHUB_ENTERPRISE`` : The source code is in a GitHub Enterprise
                      repository.

                      * ``NO_SOURCE`` : The project does not have input source code.

                      * ``S3`` : The source code is in an Amazon Simple Storage Service (Amazon S3)
                      input bucket.

                    - **location** *(string) --*

                      Information about the location of the source code to be built. Valid values
                      include:

                      * For source code settings that are specified in the source action of a
                      pipeline in AWS CodePipeline, ``location`` should not be specified. If it is
                      specified, AWS CodePipeline ignores it. This is because AWS CodePipeline uses
                      the settings in a pipeline's source action instead of this value.

                      * For source code in an AWS CodeCommit repository, the HTTPS clone URL to the
                      repository that contains the source code and the build spec (for example,
                      ``https://git-codecommit.*region-ID* .amazonaws.com/v1/repos/*repo-name* `` ).

                      * For source code in an Amazon Simple Storage Service (Amazon S3) input
                      bucket, one of the following.

                        * The path to the ZIP file that contains the source code (for example, ``
                        *bucket-name* /*path* /*to* /*object-name* .zip`` ).

                        * The path to the folder that contains the source code (for example, ``
                        *bucket-name* /*path* /*to* /*source-code* /*folder* /`` ).

                      * For source code in a GitHub repository, the HTTPS clone URL to the
                      repository that contains the source and the build spec. You must connect your
                      AWS account to your GitHub account. Use the AWS CodeBuild console to start
                      creating a build project. When you use the console to connect (or reconnect)
                      with GitHub, on the GitHub **Authorize application** page, for **Organization
                      access** , choose **Request access** next to each repository you want to allow
                      AWS CodeBuild to have access to, and then choose **Authorize application** .
                      (After you have connected to your GitHub account, you do not need to finish
                      creating the build project. You can leave the AWS CodeBuild console.) To
                      instruct AWS CodeBuild to use this connection, in the ``source`` object, set
                      the ``auth`` object's ``type`` value to ``OAUTH`` .

                      * For source code in a Bitbucket repository, the HTTPS clone URL to the
                      repository that contains the source and the build spec. You must connect your
                      AWS account to your Bitbucket account. Use the AWS CodeBuild console to start
                      creating a build project. When you use the console to connect (or reconnect)
                      with Bitbucket, on the Bitbucket **Confirm access to your account** page,
                      choose **Grant access** . (After you have connected to your Bitbucket account,
                      you do not need to finish creating the build project. You can leave the AWS
                      CodeBuild console.) To instruct AWS CodeBuild to use this connection, in the
                      ``source`` object, set the ``auth`` object's ``type`` value to ``OAUTH`` .

                    - **gitCloneDepth** *(integer) --*

                      Information about the Git clone depth for the build project.

                    - **gitSubmodulesConfig** *(dict) --*

                      Information about the Git submodules configuration for the build project.

                      - **fetchSubmodules** *(boolean) --*

                        Set to true to fetch Git submodules for your AWS CodeBuild build project.

                    - **buildspec** *(string) --*

                      The build spec declaration to use for the builds in this build project.

                      If this value is not specified, a build spec must be included along with the
                      source code to be built.

                    - **auth** *(dict) --*

                      Information about the authorization settings for AWS CodeBuild to access the
                      source code to be built.

                      This information is for the AWS CodeBuild console's use only. Your code should
                      not get or set this information directly.

                      - **type** *(string) --*

                        .. note::

                          This data type is deprecated and is no longer accurate or used.

                        The authorization type to use. The only valid value is ``OAUTH`` , which
                        represents the OAuth authorization type.

                      - **resource** *(string) --*

                        The resource value that applies to the specified authorization type.

                    - **reportBuildStatus** *(boolean) --*

                      Set to true to report the status of a build's start and finish to your source
                      provider. This option is valid only when your source provider is GitHub,
                      GitHub Enterprise, or Bitbucket. If this is set and you use a different source
                      provider, an invalidInputException is thrown.

                      .. note::

                        The status of a build triggered by a webhook is always reported to your
                        source provider.

                    - **insecureSsl** *(boolean) --*

                      Enable this flag to ignore SSL warnings while connecting to the project source
                      code.

                    - **sourceIdentifier** *(string) --*

                      An identifier for this project source.

                - **secondarySourceVersions** *(list) --*

                  An array of ``ProjectSourceVersion`` objects. Each ``ProjectSourceVersion`` must
                  be one of:

                  * For AWS CodeCommit: the commit ID, branch, or Git tag to use.

                  * For GitHub: the commit ID, pull request ID, branch name, or tag name that
                  corresponds to the version of the source code you want to build. If a pull request
                  ID is specified, it must use the format ``pr/pull-request-ID`` (for example,
                  ``pr/25`` ). If a branch name is specified, the branch's HEAD commit ID is used.
                  If not specified, the default branch's HEAD commit ID is used.

                  * For Bitbucket: the commit ID, branch name, or tag name that corresponds to the
                  version of the source code you want to build. If a branch name is specified, the
                  branch's HEAD commit ID is used. If not specified, the default branch's HEAD
                  commit ID is used.

                  * For Amazon Simple Storage Service (Amazon S3): the version ID of the object that
                  represents the build input ZIP file to use.

                  - *(dict) --*

                    A source identifier and its corresponding version.

                    - **sourceIdentifier** *(string) --*

                      An identifier for a source in the build project.

                    - **sourceVersion** *(string) --*

                      The source version for the corresponding source identifier. If specified, must
                      be one of:

                      * For AWS CodeCommit: the commit ID, branch, or Git tag to use.

                      * For GitHub: the commit ID, pull request ID, branch name, or tag name that
                      corresponds to the version of the source code you want to build. If a pull
                      request ID is specified, it must use the format ``pr/pull-request-ID`` (for
                      example, ``pr/25`` ). If a branch name is specified, the branch's HEAD commit
                      ID is used. If not specified, the default branch's HEAD commit ID is used.

                      * For Bitbucket: the commit ID, branch name, or tag name that corresponds to
                      the version of the source code you want to build. If a branch name is
                      specified, the branch's HEAD commit ID is used. If not specified, the default
                      branch's HEAD commit ID is used.

                      * For Amazon Simple Storage Service (Amazon S3): the version ID of the object
                      that represents the build input ZIP file to use.

                      For more information, see `Source Version Sample with CodeBuild
                      <https://docs.aws.amazon.com/codebuild/latest/userguide/sample-source-version.html>`__
                      in the *AWS CodeBuild User Guide* .

                - **artifacts** *(dict) --*

                  Information about the output artifacts for the build.

                  - **location** *(string) --*

                    Information about the location of the build artifacts.

                  - **sha256sum** *(string) --*

                    The SHA-256 hash of the build artifact.

                    You can use this hash along with a checksum tool to confirm file integrity and
                    authenticity.

                    .. note::

                      This value is available only if the build project's ``packaging`` value is set
                      to ``ZIP`` .

                  - **md5sum** *(string) --*

                    The MD5 hash of the build artifact.

                    You can use this hash along with a checksum tool to confirm file integrity and
                    authenticity.

                    .. note::

                      This value is available only if the build project's ``packaging`` value is set
                      to ``ZIP`` .

                  - **overrideArtifactName** *(boolean) --*

                    If this flag is set, a name specified in the build spec file overrides the
                    artifact name. The name specified in a build spec file is calculated at build
                    time and uses the Shell Command Language. For example, you can append a date and
                    time to your artifact name so that it is always unique.

                  - **encryptionDisabled** *(boolean) --*

                    Information that tells you if encryption for build artifacts is disabled.

                  - **artifactIdentifier** *(string) --*

                    An identifier for this artifact definition.

                - **secondaryArtifacts** *(list) --*

                  An array of ``ProjectArtifacts`` objects.

                  - *(dict) --*

                    Information about build output artifacts.

                    - **location** *(string) --*

                      Information about the location of the build artifacts.

                    - **sha256sum** *(string) --*

                      The SHA-256 hash of the build artifact.

                      You can use this hash along with a checksum tool to confirm file integrity and
                      authenticity.

                      .. note::

                        This value is available only if the build project's ``packaging`` value is
                        set to ``ZIP`` .

                    - **md5sum** *(string) --*

                      The MD5 hash of the build artifact.

                      You can use this hash along with a checksum tool to confirm file integrity and
                      authenticity.

                      .. note::

                        This value is available only if the build project's ``packaging`` value is
                        set to ``ZIP`` .

                    - **overrideArtifactName** *(boolean) --*

                      If this flag is set, a name specified in the build spec file overrides the
                      artifact name. The name specified in a build spec file is calculated at build
                      time and uses the Shell Command Language. For example, you can append a date
                      and time to your artifact name so that it is always unique.

                    - **encryptionDisabled** *(boolean) --*

                      Information that tells you if encryption for build artifacts is disabled.

                    - **artifactIdentifier** *(string) --*

                      An identifier for this artifact definition.

                - **cache** *(dict) --*

                  Information about the cache for the build.

                  - **type** *(string) --*

                    The type of cache used by the build project. Valid values include:

                    * ``NO_CACHE`` : The build project does not use any cache.

                    * ``S3`` : The build project reads and writes from and to S3.

                    * ``LOCAL`` : The build project stores a cache locally on a build host that is
                    only available to that build host.

                  - **location** *(string) --*

                    Information about the cache location:

                    * ``NO_CACHE`` or ``LOCAL`` : This value is ignored.

                    * ``S3`` : This is the S3 bucket name/prefix.

                  - **modes** *(list) --*

                    If you use a ``LOCAL`` cache, the local cache mode. You can use one or more
                    local cache modes at the same time.

                    * ``LOCAL_SOURCE_CACHE`` mode caches Git metadata for primary and secondary
                    sources. After the cache is created, subsequent builds pull only the change
                    between commits. This mode is a good choice for projects with a clean working
                    directory and a source that is a large Git repository. If you choose this option
                    and your project does not use a Git repository (GitHub, GitHub Enterprise, or
                    Bitbucket), the option is ignored.

                    * ``LOCAL_DOCKER_LAYER_CACHE`` mode caches existing Docker layers. This mode is
                    a good choice for projects that build or pull large Docker images. It can
                    prevent the performance issues caused by pulling large Docker images down from
                    the network.

                    .. note::

                        * You can use a Docker layer cache in the Linux environment only.

                        * The ``privileged`` flag must be set so that your project has the required
                        Docker permissions.

                        * You should consider the security implications before you use a Docker
                        layer cache.

                    * ``LOCAL_CUSTOM_CACHE`` mode caches directories you specify in the buildspec
                    file. This mode is a good choice if your build scenario is not suited to one of
                    the other three local cache modes. If you use a custom cache:

                      * Only directories can be specified for caching. You cannot specify individual
                      files.

                      * Symlinks are used to reference cached directories.

                      * Cached directories are linked to your build before it downloads its project
                      sources. Cached items are overridden if a source item has the same name.
                      Directories are specified using cache paths in the buildspec file.

                    - *(string) --*

                - **environment** *(dict) --*

                  Information about the build environment for this build.

                  - **type** *(string) --*

                    The type of build environment to use for related builds.

                    * The environment type ``ARM_CONTAINER`` is available only in regions US East
                    (N. Virginia), US East (Ohio), US West (Oregon), EU (Ireland), Asia Pacific
                    (Mumbai), Asia Pacific (Tokyo), Asia Pacific (Sydney), and EU (Frankfurt).

                    * The environment type ``LINUX_CONTAINER`` with compute type
                    ``build.general1.2xlarge`` is available only in regions US East (N. Virginia),
                    US East (N. Virginia), US West (Oregon), Canada (Central), EU (Ireland), EU
                    (London), EU (Frankfurt), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia
                    Pacific (Singapore), Asia Pacific (Sydney), China (Beijing), and China
                    (Ningxia).

                    * The environment type ``LINUX_GPU_CONTAINER`` is available only in regions US
                    East (N. Virginia), US East (N. Virginia), US West (Oregon), Canada (Central),
                    EU (Ireland), EU (London), EU (Frankfurt), Asia Pacific (Tokyo), Asia Pacific
                    (Seoul), Asia Pacific (Singapore), Asia Pacific (Sydney) , China (Beijing), and
                    China (Ningxia).

                  - **image** *(string) --*

                    The image tag or image digest that identifies the Docker image to use for this
                    build project. Use the following formats:

                    * For an image tag: ``registry/repository:tag`` . For example, to specify an
                    image with the tag "latest," use ``registry/repository:latest`` .

                    * For an image digest: ``registry/repository@digest`` . For example, to specify
                    an image with the digest
                    "sha256:cbbf2f9a99b47fc460d422812b6a5adff7dfee951d8fa2e4a98caa0382cfbdbf," use
                    ``registry/repository@sha256:cbbf2f9a99b47fc460d422812b6a5adff7dfee951d8fa2e4a98caa0382cfbdbf``
                    .

                  - **computeType** *(string) --*

                    Information about the compute resources the build project uses. Available values
                    include:

                    * ``BUILD_GENERAL1_SMALL`` : Use up to 3 GB memory and 2 vCPUs for builds.

                    * ``BUILD_GENERAL1_MEDIUM`` : Use up to 7 GB memory and 4 vCPUs for builds.

                    * ``BUILD_GENERAL1_LARGE`` : Use up to 16 GB memory and 8 vCPUs for builds,
                    depending on your environment type.

                    * ``BUILD_GENERAL1_2XLARGE`` : Use up to 145 GB memory, 72 vCPUs, and 824 GB of
                    SSD storage for builds. This compute type supports Docker images up to 100 GB
                    uncompressed.

                    If you use ``BUILD_GENERAL1_LARGE`` :

                    * For environment type ``LINUX_CONTAINER`` , you can use up to 15 GB memory and
                    8 vCPUs for builds.

                    * For environment type ``LINUX_GPU_CONTAINER`` , you can use up to 255 GB
                    memory, 32 vCPUs, and 4 NVIDIA Tesla V100 GPUs for builds.

                    * For environment type ``ARM_CONTAINER`` , you can use up to 16 GB memory and 8
                    vCPUs on ARM-based processors for builds.

                    For more information, see `Build Environment Compute Types
                    <https://docs.aws.amazon.com/codebuild/latest/userguide/build-env-ref-compute-types.html>`__
                    in the *AWS CodeBuild User Guide.*

                  - **environmentVariables** *(list) --*

                    A set of environment variables to make available to builds for this build
                    project.

                    - *(dict) --*

                      Information about an environment variable for a build project or a build.

                      - **name** *(string) --*

                        The name or key of the environment variable.

                      - **value** *(string) --*

                        The value of the environment variable.

                        .. warning::

                          We strongly discourage the use of environment variables to store sensitive
                          values, especially AWS secret key IDs and secret access keys. Environment
                          variables can be displayed in plain text using the AWS CodeBuild console
                          and the AWS Command Line Interface (AWS CLI).

                      - **type** *(string) --*

                        The type of environment variable. Valid values include:

                        * ``PARAMETER_STORE`` : An environment variable stored in Amazon EC2 Systems
                        Manager Parameter Store.

                        * ``PLAINTEXT`` : An environment variable in plain text format.

                        * ``SECRETS_MANAGER`` : An environment variable stored in AWS Secrets
                        Manager.

                  - **privilegedMode** *(boolean) --*

                    Enables running the Docker daemon inside a Docker container. Set to true only if
                    the build project is used to build Docker images. Otherwise, a build that
                    attempts to interact with the Docker daemon fails. The default setting is
                    ``false`` .

                    You can initialize the Docker daemon during the install phase of your build by
                    adding one of the following sets of commands to the install phase of your
                    buildspec file:

                    If the operating system's base image is Ubuntu Linux:

                     ``- nohup /usr/local/bin/dockerd --host=
                         unix:///var/run/docker.sock
                     --host=tcp://0.0.0.0:2375 --storage-driver=overlay&``

                     ``- timeout 15 sh -c "until docker info; do echo .; sleep 1; done"``

                    If the operating system's base image is Alpine Linux and the previous command
                    does not work, add the ``-t`` argument to ``timeout`` :

                     ``- nohup /usr/local/bin/dockerd --host=
                         unix:///var/run/docker.sock
                     --host=tcp://0.0.0.0:2375 --storage-driver=overlay&``

                     ``- timeout -t 15 sh -c "until docker info; do echo .; sleep 1; done"``

                  - **certificate** *(string) --*

                    The certificate to use with this build project.

                  - **registryCredential** *(dict) --*

                    The credentials for access to a private registry.

                    - **credential** *(string) --*

                      The Amazon Resource Name (ARN) or name of credentials created using AWS
                      Secrets Manager.

                      .. note::

                        The ``credential`` can use the name of the credentials only if they exist in
                        your current region.

                    - **credentialProvider** *(string) --*

                      The service that created the credentials to access a private Docker registry.
                      The valid value, SECRETS_MANAGER, is for AWS Secrets Manager.

                  - **imagePullCredentialsType** *(string) --*

                    The type of credentials AWS CodeBuild uses to pull images in your build. There
                    are two valid values:

                    * ``CODEBUILD`` specifies that AWS CodeBuild uses its own credentials. This
                    requires that you modify your ECR repository policy to trust AWS CodeBuild's
                    service principal.

                    * ``SERVICE_ROLE`` specifies that AWS CodeBuild uses your build project's
                    service role.

                    When you use a cross-account or private registry image, you must use
                    SERVICE_ROLE credentials. When you use an AWS CodeBuild curated image, you must
                    use CODEBUILD credentials.

                - **serviceRole** *(string) --*

                  The name of a service role used for this build.

                - **logs** *(dict) --*

                  Information about the build's logs in Amazon CloudWatch Logs.

                  - **groupName** *(string) --*

                    The name of the Amazon CloudWatch Logs group for the build logs.

                  - **streamName** *(string) --*

                    The name of the Amazon CloudWatch Logs stream for the build logs.

                  - **deepLink** *(string) --*

                    The URL to an individual build log in Amazon CloudWatch Logs.

                  - **s3DeepLink** *(string) --*

                    The URL to a build log in an S3 bucket.

                  - **cloudWatchLogsArn** *(string) --*

                    The ARN of Amazon CloudWatch Logs for a build project. Its format is
                    ``arn:${Partition}:logs:${Region}:${Account}:log-group:${LogGroupName}:log-stream:${LogStreamName}``
                    . For more information, see `Resources Defined by Amazon CloudWatch Logs
                    <https://docs.aws.amazon.com/IAM/latest/UserGuide/list_amazoncloudwatchlogs.html#amazoncloudwatchlogs-resources-for-iam-policies>`__
                    .

                  - **s3LogsArn** *(string) --*

                    The ARN of S3 logs for a build project. Its format is
                    ``arn:${Partition}:s3:::${BucketName}/${ObjectName}`` . For more information,
                    see `Resources Defined by Amazon S3
                    <https://docs.aws.amazon.com/IAM/latest/UserGuide/list_amazons3.html#amazons3-resources-for-iam-policies>`__
                    .

                  - **cloudWatchLogs** *(dict) --*

                    Information about Amazon CloudWatch Logs for a build project.

                    - **status** *(string) --*

                      The current status of the logs in Amazon CloudWatch Logs for a build project.
                      Valid values are:

                      * ``ENABLED`` : Amazon CloudWatch Logs are enabled for this build project.

                      * ``DISABLED`` : Amazon CloudWatch Logs are not enabled for this build
                      project.

                    - **groupName** *(string) --*

                      The group name of the logs in Amazon CloudWatch Logs. For more information,
                      see `Working with Log Groups and Log Streams
                      <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html>`__
                      .

                    - **streamName** *(string) --*

                      The prefix of the stream name of the Amazon CloudWatch Logs. For more
                      information, see `Working with Log Groups and Log Streams
                      <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html>`__
                      .

                  - **s3Logs** *(dict) --*

                    Information about S3 logs for a build project.

                    - **status** *(string) --*

                      The current status of the S3 build logs. Valid values are:

                      * ``ENABLED`` : S3 build logs are enabled for this build project.

                      * ``DISABLED`` : S3 build logs are not enabled for this build project.

                    - **location** *(string) --*

                      The ARN of an S3 bucket and the path prefix for S3 logs. If your Amazon S3
                      bucket name is ``my-bucket`` , and your path prefix is ``build-log`` , then
                      acceptable formats are ``my-bucket/build-log`` or
                      ``arn:aws:s3:::my-bucket/build-log`` .

                    - **encryptionDisabled** *(boolean) --*

                      Set to true if you do not want your S3 build log output encrypted. By default
                      S3 build logs are encrypted.

                - **timeoutInMinutes** *(integer) --*

                  How long, in minutes, for AWS CodeBuild to wait before timing out this build if it
                  does not get marked as completed.

                - **queuedTimeoutInMinutes** *(integer) --*

                  The number of minutes a build is allowed to be queued before it times out.

                - **buildComplete** *(boolean) --*

                  Whether the build is complete. True if complete; otherwise, false.

                - **initiator** *(string) --*

                  The entity that started the build. Valid values include:

                  * If AWS CodePipeline started the build, the pipeline's name (for example,
                  ``codepipeline/my-demo-pipeline`` ).

                  * If an AWS Identity and Access Management (IAM) user started the build, the
                  user's name (for example, ``MyUserName`` ).

                  * If the Jenkins plugin for AWS CodeBuild started the build, the string
                  ``CodeBuild-Jenkins-Plugin`` .

                - **vpcConfig** *(dict) --*

                  If your AWS CodeBuild project accesses resources in an Amazon VPC, you provide
                  this parameter that identifies the VPC ID and the list of security group IDs and
                  subnet IDs. The security groups and subnets must belong to the same VPC. You must
                  provide at least one security group and one subnet ID.

                  - **vpcId** *(string) --*

                    The ID of the Amazon VPC.

                  - **subnets** *(list) --*

                    A list of one or more subnet IDs in your Amazon VPC.

                    - *(string) --*

                  - **securityGroupIds** *(list) --*

                    A list of one or more security groups IDs in your Amazon VPC.

                    - *(string) --*

                - **networkInterface** *(dict) --*

                  Describes a network interface.

                  - **subnetId** *(string) --*

                    The ID of the subnet.

                  - **networkInterfaceId** *(string) --*

                    The ID of the network interface.

                - **encryptionKey** *(string) --*

                  The AWS Key Management Service (AWS KMS) customer master key (CMK) to be used for
                  encrypting the build output artifacts.

                  .. note::

                    You can use a cross-account KMS key to encrypt the build output artifacts if
                    your service role has permission to that key.

                  You can specify either the Amazon Resource Name (ARN) of the CMK or, if available,
                  the CMK's alias (using the format ``alias/*alias-name* `` ).

                - **exportedEnvironmentVariables** *(list) --*

                  A list of exported environment variables for this build.

                  - *(dict) --*

                    Information about an exported environment variable.

                    - **name** *(string) --*

                      The name of this exported environment variable.

                    - **value** *(string) --*

                      The value assigned to this exported environment variable.

                      .. note::

                        During a build, the value of a variable is available starting with the
                        ``install`` phase. It can be updated between the start of the ``install``
                        phase and the end of the ``post_build`` phase. After the ``post_build``
                        phase ends, the value of exported variables cannot change.

                - **reportArns** *(list) --*

                  An array of the ARNs associated with this build's reports.

                  - *(string) --*

            - **buildsNotFound** *(list) --*

              The IDs of builds for which information could not be found.

              - *(string) --*
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def batch_get_projects(self, names: List[str]) -> ClientBatchGetProjectsResponseTypeDef:
        """
        Gets information about one or more build projects.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/codebuild-2016-10-06/BatchGetProjects>`_

        **Request Syntax**
        ::

          response = client.batch_get_projects(
              names=[
                  'string',
              ]
          )
        :type names: list
        :param names: **[REQUIRED]**

          The names of the build projects.

          - *(string) --*

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'projects': [
                    {
                        'name': 'string',
                        'arn': 'string',
                        'description': 'string',
                        'source': {
                            'type':
                            'CODECOMMIT'|'CODEPIPELINE'|'GITHUB'|'S3'
                            |'BITBUCKET'|'GITHUB_ENTERPRISE'|'NO_SOURCE',
                            'location': 'string',
                            'gitCloneDepth': 123,
                            'gitSubmodulesConfig': {
                                'fetchSubmodules': True|False
                            },
                            'buildspec': 'string',
                            'auth': {
                                'type': 'OAUTH',
                                'resource': 'string'
                            },
                            'reportBuildStatus': True|False,
                            'insecureSsl': True|False,
                            'sourceIdentifier': 'string'
                        },
                        'secondarySources': [
                            {
                                'type':
                                'CODECOMMIT'|'CODEPIPELINE'|'GITHUB'|'S3'
                                |'BITBUCKET'|'GITHUB_ENTERPRISE'
                                |'NO_SOURCE',
                                'location': 'string',
                                'gitCloneDepth': 123,
                                'gitSubmodulesConfig': {
                                    'fetchSubmodules': True|False
                                },
                                'buildspec': 'string',
                                'auth': {
                                    'type': 'OAUTH',
                                    'resource': 'string'
                                },
                                'reportBuildStatus': True|False,
                                'insecureSsl': True|False,
                                'sourceIdentifier': 'string'
                            },
                        ],
                        'sourceVersion': 'string',
                        'secondarySourceVersions': [
                            {
                                'sourceIdentifier': 'string',
                                'sourceVersion': 'string'
                            },
                        ],
                        'artifacts': {
                            'type': 'CODEPIPELINE'|'S3'|'NO_ARTIFACTS',
                            'location': 'string',
                            'path': 'string',
                            'namespaceType': 'NONE'|'BUILD_ID',
                            'name': 'string',
                            'packaging': 'NONE'|'ZIP',
                            'overrideArtifactName': True|False,
                            'encryptionDisabled': True|False,
                            'artifactIdentifier': 'string'
                        },
                        'secondaryArtifacts': [
                            {
                                'type': 'CODEPIPELINE'|'S3'|'NO_ARTIFACTS',
                                'location': 'string',
                                'path': 'string',
                                'namespaceType': 'NONE'|'BUILD_ID',
                                'name': 'string',
                                'packaging': 'NONE'|'ZIP',
                                'overrideArtifactName': True|False,
                                'encryptionDisabled': True|False,
                                'artifactIdentifier': 'string'
                            },
                        ],
                        'cache': {
                            'type': 'NO_CACHE'|'S3'|'LOCAL',
                            'location': 'string',
                            'modes': [
                                'LOCAL_DOCKER_LAYER_CACHE'|'LOCAL_SOURCE_CACHE'
                                |'LOCAL_CUSTOM_CACHE',
                            ]
                        },
                        'environment': {
                            'type':
                            'WINDOWS_CONTAINER'|'LINUX_CONTAINER'
                            |'LINUX_GPU_CONTAINER'|'ARM_CONTAINER',
                            'image': 'string',
                            'computeType':
                            'BUILD_GENERAL1_SMALL'|'BUILD_GENERAL1_MEDIUM'
                            |'BUILD_GENERAL1_LARGE'|'BUILD_GENERAL1_2XLARGE',
                            'environmentVariables': [
                                {
                                    'name': 'string',
                                    'value': 'string',
                                    'type': 'PLAINTEXT'|'PARAMETER_STORE'|'SECRETS_MANAGER'
                                },
                            ],
                            'privilegedMode': True|False,
                            'certificate': 'string',
                            'registryCredential': {
                                'credential': 'string',
                                'credentialProvider': 'SECRETS_MANAGER'
                            },
                            'imagePullCredentialsType': 'CODEBUILD'|'SERVICE_ROLE'
                        },
                        'serviceRole': 'string',
                        'timeoutInMinutes': 123,
                        'queuedTimeoutInMinutes': 123,
                        'encryptionKey': 'string',
                        'tags': [
                            {
                                'key': 'string',
                                'value': 'string'
                            },
                        ],
                        'created': datetime(2015, 1, 1),
                        'lastModified': datetime(2015, 1, 1),
                        'webhook': {
                            'url': 'string',
                            'payloadUrl': 'string',
                            'secret': 'string',
                            'branchFilter': 'string',
                            'filterGroups': [
                                [
                                    {
                                        'type':
                                        'EVENT'|'BASE_REF'
                                        |'HEAD_REF'
                                        |'ACTOR_ACCOUNT_ID'
                                        |'FILE_PATH',
                                        'pattern': 'string',
                                        'excludeMatchedPattern': True|False
                                    },
                                ],
                            ],
                            'lastModifiedSecret': datetime(2015, 1, 1)
                        },
                        'vpcConfig': {
                            'vpcId': 'string',
                            'subnets': [
                                'string',
                            ],
                            'securityGroupIds': [
                                'string',
                            ]
                        },
                        'badge': {
                            'badgeEnabled': True|False,
                            'badgeRequestUrl': 'string'
                        },
                        'logsConfig': {
                            'cloudWatchLogs': {
                                'status': 'ENABLED'|'DISABLED',
                                'groupName': 'string',
                                'streamName': 'string'
                            },
                            's3Logs': {
                                'status': 'ENABLED'|'DISABLED',
                                'location': 'string',
                                'encryptionDisabled': True|False
                            }
                        }
                    },
                ],
                'projectsNotFound': [
                    'string',
                ]
            }
          **Response Structure**

          - *(dict) --*

            - **projects** *(list) --*

              Information about the requested build projects.

              - *(dict) --*

                Information about a build project.

                - **name** *(string) --*

                  The name of the build project.

                - **arn** *(string) --*

                  The Amazon Resource Name (ARN) of the build project.

                - **description** *(string) --*

                  A description that makes the build project easy to identify.

                - **source** *(dict) --*

                  Information about the build input source code for this build project.

                  - **type** *(string) --*

                    The type of repository that contains the source code to be built. Valid values
                    include:

                    * ``BITBUCKET`` : The source code is in a Bitbucket repository.

                    * ``CODECOMMIT`` : The source code is in an AWS CodeCommit repository.

                    * ``CODEPIPELINE`` : The source code settings are specified in the source action
                    of a pipeline in AWS CodePipeline.

                    * ``GITHUB`` : The source code is in a GitHub repository.

                    * ``GITHUB_ENTERPRISE`` : The source code is in a GitHub Enterprise repository.

                    * ``NO_SOURCE`` : The project does not have input source code.

                    * ``S3`` : The source code is in an Amazon Simple Storage Service (Amazon S3)
                    input bucket.

                  - **location** *(string) --*

                    Information about the location of the source code to be built. Valid values
                    include:

                    * For source code settings that are specified in the source action of a pipeline
                    in AWS CodePipeline, ``location`` should not be specified. If it is specified,
                    AWS CodePipeline ignores it. This is because AWS CodePipeline uses the settings
                    in a pipeline's source action instead of this value.

                    * For source code in an AWS CodeCommit repository, the HTTPS clone URL to the
                    repository that contains the source code and the build spec (for example,
                    ``https://git-codecommit.*region-ID* .amazonaws.com/v1/repos/*repo-name* `` ).

                    * For source code in an Amazon Simple Storage Service (Amazon S3) input bucket,
                    one of the following.

                      * The path to the ZIP file that contains the source code (for example, ``
                      *bucket-name* /*path* /*to* /*object-name* .zip`` ).

                      * The path to the folder that contains the source code (for example, ``
                      *bucket-name* /*path* /*to* /*source-code* /*folder* /`` ).

                    * For source code in a GitHub repository, the HTTPS clone URL to the repository
                    that contains the source and the build spec. You must connect your AWS account
                    to your GitHub account. Use the AWS CodeBuild console to start creating a build
                    project. When you use the console to connect (or reconnect) with GitHub, on the
                    GitHub **Authorize application** page, for **Organization access** , choose
                    **Request access** next to each repository you want to allow AWS CodeBuild to
                    have access to, and then choose **Authorize application** . (After you have
                    connected to your GitHub account, you do not need to finish creating the build
                    project. You can leave the AWS CodeBuild console.) To instruct AWS CodeBuild to
                    use this connection, in the ``source`` object, set the ``auth`` object's
                    ``type`` value to ``OAUTH`` .

                    * For source code in a Bitbucket repository, the HTTPS clone URL to the
                    repository that contains the source and the build spec. You must connect your
                    AWS account to your Bitbucket account. Use the AWS CodeBuild console to start
                    creating a build project. When you use the console to connect (or reconnect)
                    with Bitbucket, on the Bitbucket **Confirm access to your account** page, choose
                    **Grant access** . (After you have connected to your Bitbucket account, you do
                    not need to finish creating the build project. You can leave the AWS CodeBuild
                    console.) To instruct AWS CodeBuild to use this connection, in the ``source``
                    object, set the ``auth`` object's ``type`` value to ``OAUTH`` .

                  - **gitCloneDepth** *(integer) --*

                    Information about the Git clone depth for the build project.

                  - **gitSubmodulesConfig** *(dict) --*

                    Information about the Git submodules configuration for the build project.

                    - **fetchSubmodules** *(boolean) --*

                      Set to true to fetch Git submodules for your AWS CodeBuild build project.

                  - **buildspec** *(string) --*

                    The build spec declaration to use for the builds in this build project.

                    If this value is not specified, a build spec must be included along with the
                    source code to be built.

                  - **auth** *(dict) --*

                    Information about the authorization settings for AWS CodeBuild to access the
                    source code to be built.

                    This information is for the AWS CodeBuild console's use only. Your code should
                    not get or set this information directly.

                    - **type** *(string) --*

                      .. note::

                        This data type is deprecated and is no longer accurate or used.

                      The authorization type to use. The only valid value is ``OAUTH`` , which
                      represents the OAuth authorization type.

                    - **resource** *(string) --*

                      The resource value that applies to the specified authorization type.

                  - **reportBuildStatus** *(boolean) --*

                    Set to true to report the status of a build's start and finish to your source
                    provider. This option is valid only when your source provider is GitHub, GitHub
                    Enterprise, or Bitbucket. If this is set and you use a different source
                    provider, an invalidInputException is thrown.

                    .. note::

                      The status of a build triggered by a webhook is always reported to your source
                      provider.

                  - **insecureSsl** *(boolean) --*

                    Enable this flag to ignore SSL warnings while connecting to the project source
                    code.

                  - **sourceIdentifier** *(string) --*

                    An identifier for this project source.

                - **secondarySources** *(list) --*

                  An array of ``ProjectSource`` objects.

                  - *(dict) --*

                    Information about the build input source code for the build project.

                    - **type** *(string) --*

                      The type of repository that contains the source code to be built. Valid values
                      include:

                      * ``BITBUCKET`` : The source code is in a Bitbucket repository.

                      * ``CODECOMMIT`` : The source code is in an AWS CodeCommit repository.

                      * ``CODEPIPELINE`` : The source code settings are specified in the source
                      action of a pipeline in AWS CodePipeline.

                      * ``GITHUB`` : The source code is in a GitHub repository.

                      * ``GITHUB_ENTERPRISE`` : The source code is in a GitHub Enterprise
                      repository.

                      * ``NO_SOURCE`` : The project does not have input source code.

                      * ``S3`` : The source code is in an Amazon Simple Storage Service (Amazon S3)
                      input bucket.

                    - **location** *(string) --*

                      Information about the location of the source code to be built. Valid values
                      include:

                      * For source code settings that are specified in the source action of a
                      pipeline in AWS CodePipeline, ``location`` should not be specified. If it is
                      specified, AWS CodePipeline ignores it. This is because AWS CodePipeline uses
                      the settings in a pipeline's source action instead of this value.

                      * For source code in an AWS CodeCommit repository, the HTTPS clone URL to the
                      repository that contains the source code and the build spec (for example,
                      ``https://git-codecommit.*region-ID* .amazonaws.com/v1/repos/*repo-name* `` ).

                      * For source code in an Amazon Simple Storage Service (Amazon S3) input
                      bucket, one of the following.

                        * The path to the ZIP file that contains the source code (for example, ``
                        *bucket-name* /*path* /*to* /*object-name* .zip`` ).

                        * The path to the folder that contains the source code (for example, ``
                        *bucket-name* /*path* /*to* /*source-code* /*folder* /`` ).

                      * For source code in a GitHub repository, the HTTPS clone URL to the
                      repository that contains the source and the build spec. You must connect your
                      AWS account to your GitHub account. Use the AWS CodeBuild console to start
                      creating a build project. When you use the console to connect (or reconnect)
                      with GitHub, on the GitHub **Authorize application** page, for **Organization
                      access** , choose **Request access** next to each repository you want to allow
                      AWS CodeBuild to have access to, and then choose **Authorize application** .
                      (After you have connected to your GitHub account, you do not need to finish
                      creating the build project. You can leave the AWS CodeBuild console.) To
                      instruct AWS CodeBuild to use this connection, in the ``source`` object, set
                      the ``auth`` object's ``type`` value to ``OAUTH`` .

                      * For source code in a Bitbucket repository, the HTTPS clone URL to the
                      repository that contains the source and the build spec. You must connect your
                      AWS account to your Bitbucket account. Use the AWS CodeBuild console to start
                      creating a build project. When you use the console to connect (or reconnect)
                      with Bitbucket, on the Bitbucket **Confirm access to your account** page,
                      choose **Grant access** . (After you have connected to your Bitbucket account,
                      you do not need to finish creating the build project. You can leave the AWS
                      CodeBuild console.) To instruct AWS CodeBuild to use this connection, in the
                      ``source`` object, set the ``auth`` object's ``type`` value to ``OAUTH`` .

                    - **gitCloneDepth** *(integer) --*

                      Information about the Git clone depth for the build project.

                    - **gitSubmodulesConfig** *(dict) --*

                      Information about the Git submodules configuration for the build project.

                      - **fetchSubmodules** *(boolean) --*

                        Set to true to fetch Git submodules for your AWS CodeBuild build project.

                    - **buildspec** *(string) --*

                      The build spec declaration to use for the builds in this build project.

                      If this value is not specified, a build spec must be included along with the
                      source code to be built.

                    - **auth** *(dict) --*

                      Information about the authorization settings for AWS CodeBuild to access the
                      source code to be built.

                      This information is for the AWS CodeBuild console's use only. Your code should
                      not get or set this information directly.

                      - **type** *(string) --*

                        .. note::

                          This data type is deprecated and is no longer accurate or used.

                        The authorization type to use. The only valid value is ``OAUTH`` , which
                        represents the OAuth authorization type.

                      - **resource** *(string) --*

                        The resource value that applies to the specified authorization type.

                    - **reportBuildStatus** *(boolean) --*

                      Set to true to report the status of a build's start and finish to your source
                      provider. This option is valid only when your source provider is GitHub,
                      GitHub Enterprise, or Bitbucket. If this is set and you use a different source
                      provider, an invalidInputException is thrown.

                      .. note::

                        The status of a build triggered by a webhook is always reported to your
                        source provider.

                    - **insecureSsl** *(boolean) --*

                      Enable this flag to ignore SSL warnings while connecting to the project source
                      code.

                    - **sourceIdentifier** *(string) --*

                      An identifier for this project source.

                - **sourceVersion** *(string) --*

                  A version of the build input to be built for this project. If not specified, the
                  latest version is used. If specified, it must be one of:

                  * For AWS CodeCommit: the commit ID, branch, or Git tag to use.

                  * For GitHub: the commit ID, pull request ID, branch name, or tag name that
                  corresponds to the version of the source code you want to build. If a pull request
                  ID is specified, it must use the format ``pr/pull-request-ID`` (for example
                  ``pr/25`` ). If a branch name is specified, the branch's HEAD commit ID is used.
                  If not specified, the default branch's HEAD commit ID is used.

                  * For Bitbucket: the commit ID, branch name, or tag name that corresponds to the
                  version of the source code you want to build. If a branch name is specified, the
                  branch's HEAD commit ID is used. If not specified, the default branch's HEAD
                  commit ID is used.

                  * For Amazon Simple Storage Service (Amazon S3): the version ID of the object that
                  represents the build input ZIP file to use.

                  If ``sourceVersion`` is specified at the build level, then that version takes
                  precedence over this ``sourceVersion`` (at the project level).

                  For more information, see `Source Version Sample with CodeBuild
                  <https://docs.aws.amazon.com/codebuild/latest/userguide/sample-source-version.html>`__
                  in the *AWS CodeBuild User Guide* .

                - **secondarySourceVersions** *(list) --*

                  An array of ``ProjectSourceVersion`` objects. If ``secondarySourceVersions`` is
                  specified at the build level, then they take over these
                  ``secondarySourceVersions`` (at the project level).

                  - *(dict) --*

                    A source identifier and its corresponding version.

                    - **sourceIdentifier** *(string) --*

                      An identifier for a source in the build project.

                    - **sourceVersion** *(string) --*

                      The source version for the corresponding source identifier. If specified, must
                      be one of:

                      * For AWS CodeCommit: the commit ID, branch, or Git tag to use.

                      * For GitHub: the commit ID, pull request ID, branch name, or tag name that
                      corresponds to the version of the source code you want to build. If a pull
                      request ID is specified, it must use the format ``pr/pull-request-ID`` (for
                      example, ``pr/25`` ). If a branch name is specified, the branch's HEAD commit
                      ID is used. If not specified, the default branch's HEAD commit ID is used.

                      * For Bitbucket: the commit ID, branch name, or tag name that corresponds to
                      the version of the source code you want to build. If a branch name is
                      specified, the branch's HEAD commit ID is used. If not specified, the default
                      branch's HEAD commit ID is used.

                      * For Amazon Simple Storage Service (Amazon S3): the version ID of the object
                      that represents the build input ZIP file to use.

                      For more information, see `Source Version Sample with CodeBuild
                      <https://docs.aws.amazon.com/codebuild/latest/userguide/sample-source-version.html>`__
                      in the *AWS CodeBuild User Guide* .

                - **artifacts** *(dict) --*

                  Information about the build output artifacts for the build project.

                  - **type** *(string) --*

                    The type of build output artifact. Valid values include:

                    * ``CODEPIPELINE`` : The build project has build output generated through AWS
                    CodePipeline.

                    .. note::

                       The ``CODEPIPELINE`` type is not supported for ``secondaryArtifacts`` .

                    * ``NO_ARTIFACTS`` : The build project does not produce any build output.

                    * ``S3`` : The build project stores build output in Amazon Simple Storage
                    Service (Amazon S3).

                  - **location** *(string) --*

                    Information about the build output artifact location:

                    * If ``type`` is set to ``CODEPIPELINE`` , AWS CodePipeline ignores this value
                    if specified. This is because AWS CodePipeline manages its build output
                    locations instead of AWS CodeBuild.

                    * If ``type`` is set to ``NO_ARTIFACTS`` , this value is ignored if specified,
                    because no build output is produced.

                    * If ``type`` is set to ``S3`` , this is the name of the output bucket.

                  - **path** *(string) --*

                    Along with ``namespaceType`` and ``name`` , the pattern that AWS CodeBuild uses
                    to name and store the output artifact:

                    * If ``type`` is set to ``CODEPIPELINE`` , AWS CodePipeline ignores this value
                    if specified. This is because AWS CodePipeline manages its build output names
                    instead of AWS CodeBuild.

                    * If ``type`` is set to ``NO_ARTIFACTS`` , this value is ignored if specified,
                    because no build output is produced.

                    * If ``type`` is set to ``S3`` , this is the path to the output artifact. If
                    ``path`` is not specified, ``path`` is not used.

                    For example, if ``path`` is set to ``MyArtifacts`` , ``namespaceType`` is set to
                    ``NONE`` , and ``name`` is set to ``MyArtifact.zip`` , the output artifact is
                    stored in the output bucket at ``MyArtifacts/MyArtifact.zip`` .

                  - **namespaceType** *(string) --*

                    Along with ``path`` and ``name`` , the pattern that AWS CodeBuild uses to
                    determine the name and location to store the output artifact:

                    * If ``type`` is set to ``CODEPIPELINE`` , AWS CodePipeline ignores this value
                    if specified. This is because AWS CodePipeline manages its build output names
                    instead of AWS CodeBuild.

                    * If ``type`` is set to ``NO_ARTIFACTS`` , this value is ignored if specified,
                    because no build output is produced.

                    * If ``type`` is set to ``S3`` , valid values include:

                      * ``BUILD_ID`` : Include the build ID in the location of the build output
                      artifact.

                      * ``NONE`` : Do not include the build ID. This is the default if
                      ``namespaceType`` is not specified.

                    For example, if ``path`` is set to ``MyArtifacts`` , ``namespaceType`` is set to
                    ``BUILD_ID`` , and ``name`` is set to ``MyArtifact.zip`` , the output artifact
                    is stored in ``MyArtifacts/*build-ID* /MyArtifact.zip`` .

                  - **name** *(string) --*

                    Along with ``path`` and ``namespaceType`` , the pattern that AWS CodeBuild uses
                    to name and store the output artifact:

                    * If ``type`` is set to ``CODEPIPELINE`` , AWS CodePipeline ignores this value
                    if specified. This is because AWS CodePipeline manages its build output names
                    instead of AWS CodeBuild.

                    * If ``type`` is set to ``NO_ARTIFACTS`` , this value is ignored if specified,
                    because no build output is produced.

                    * If ``type`` is set to ``S3`` , this is the name of the output artifact object.
                    If you set the name to be a forward slash ("/"), the artifact is stored in the
                    root of the output bucket.

                    For example:

                    * If ``path`` is set to ``MyArtifacts`` , ``namespaceType`` is set to
                    ``BUILD_ID`` , and ``name`` is set to ``MyArtifact.zip`` , then the output
                    artifact is stored in ``MyArtifacts/*build-ID* /MyArtifact.zip`` .

                    * If ``path`` is empty, ``namespaceType`` is set to ``NONE`` , and ``name`` is
                    set to "``/`` ", the output artifact is stored in the root of the output bucket.

                    * If ``path`` is set to ``MyArtifacts`` , ``namespaceType`` is set to
                    ``BUILD_ID`` , and ``name`` is set to "``/`` ", the output artifact is stored in
                    ``MyArtifacts/*build-ID* `` .

                  - **packaging** *(string) --*

                    The type of build output artifact to create:

                    * If ``type`` is set to ``CODEPIPELINE`` , AWS CodePipeline ignores this value
                    if specified. This is because AWS CodePipeline manages its build output
                    artifacts instead of AWS CodeBuild.

                    * If ``type`` is set to ``NO_ARTIFACTS`` , this value is ignored if specified,
                    because no build output is produced.

                    * If ``type`` is set to ``S3`` , valid values include:

                      * ``NONE`` : AWS CodeBuild creates in the output bucket a folder that contains
                      the build output. This is the default if ``packaging`` is not specified.

                      * ``ZIP`` : AWS CodeBuild creates in the output bucket a ZIP file that
                      contains the build output.

                  - **overrideArtifactName** *(boolean) --*

                    If this flag is set, a name specified in the build spec file overrides the
                    artifact name. The name specified in a build spec file is calculated at build
                    time and uses the Shell Command Language. For example, you can append a date and
                    time to your artifact name so that it is always unique.

                  - **encryptionDisabled** *(boolean) --*

                    Set to true if you do not want your output artifacts encrypted. This option is
                    valid only if your artifacts type is Amazon Simple Storage Service (Amazon S3).
                    If this is set with another artifacts type, an invalidInputException is thrown.

                  - **artifactIdentifier** *(string) --*

                    An identifier for this artifact definition.

                - **secondaryArtifacts** *(list) --*

                  An array of ``ProjectArtifacts`` objects.

                  - *(dict) --*

                    Information about the build output artifacts for the build project.

                    - **type** *(string) --*

                      The type of build output artifact. Valid values include:

                      * ``CODEPIPELINE`` : The build project has build output generated through AWS
                      CodePipeline.

                      .. note::

                         The ``CODEPIPELINE`` type is not supported for ``secondaryArtifacts`` .

                      * ``NO_ARTIFACTS`` : The build project does not produce any build output.

                      * ``S3`` : The build project stores build output in Amazon Simple Storage
                      Service (Amazon S3).

                    - **location** *(string) --*

                      Information about the build output artifact location:

                      * If ``type`` is set to ``CODEPIPELINE`` , AWS CodePipeline ignores this value
                      if specified. This is because AWS CodePipeline manages its build output
                      locations instead of AWS CodeBuild.

                      * If ``type`` is set to ``NO_ARTIFACTS`` , this value is ignored if specified,
                      because no build output is produced.

                      * If ``type`` is set to ``S3`` , this is the name of the output bucket.

                    - **path** *(string) --*

                      Along with ``namespaceType`` and ``name`` , the pattern that AWS CodeBuild
                      uses to name and store the output artifact:

                      * If ``type`` is set to ``CODEPIPELINE`` , AWS CodePipeline ignores this value
                      if specified. This is because AWS CodePipeline manages its build output names
                      instead of AWS CodeBuild.

                      * If ``type`` is set to ``NO_ARTIFACTS`` , this value is ignored if specified,
                      because no build output is produced.

                      * If ``type`` is set to ``S3`` , this is the path to the output artifact. If
                      ``path`` is not specified, ``path`` is not used.

                      For example, if ``path`` is set to ``MyArtifacts`` , ``namespaceType`` is set
                      to ``NONE`` , and ``name`` is set to ``MyArtifact.zip`` , the output artifact
                      is stored in the output bucket at ``MyArtifacts/MyArtifact.zip`` .

                    - **namespaceType** *(string) --*

                      Along with ``path`` and ``name`` , the pattern that AWS CodeBuild uses to
                      determine the name and location to store the output artifact:

                      * If ``type`` is set to ``CODEPIPELINE`` , AWS CodePipeline ignores this value
                      if specified. This is because AWS CodePipeline manages its build output names
                      instead of AWS CodeBuild.

                      * If ``type`` is set to ``NO_ARTIFACTS`` , this value is ignored if specified,
                      because no build output is produced.

                      * If ``type`` is set to ``S3`` , valid values include:

                        * ``BUILD_ID`` : Include the build ID in the location of the build output
                        artifact.

                        * ``NONE`` : Do not include the build ID. This is the default if
                        ``namespaceType`` is not specified.

                      For example, if ``path`` is set to ``MyArtifacts`` , ``namespaceType`` is set
                      to ``BUILD_ID`` , and ``name`` is set to ``MyArtifact.zip`` , the output
                      artifact is stored in ``MyArtifacts/*build-ID* /MyArtifact.zip`` .

                    - **name** *(string) --*

                      Along with ``path`` and ``namespaceType`` , the pattern that AWS CodeBuild
                      uses to name and store the output artifact:

                      * If ``type`` is set to ``CODEPIPELINE`` , AWS CodePipeline ignores this value
                      if specified. This is because AWS CodePipeline manages its build output names
                      instead of AWS CodeBuild.

                      * If ``type`` is set to ``NO_ARTIFACTS`` , this value is ignored if specified,
                      because no build output is produced.

                      * If ``type`` is set to ``S3`` , this is the name of the output artifact
                      object. If you set the name to be a forward slash ("/"), the artifact is
                      stored in the root of the output bucket.

                      For example:

                      * If ``path`` is set to ``MyArtifacts`` , ``namespaceType`` is set to
                      ``BUILD_ID`` , and ``name`` is set to ``MyArtifact.zip`` , then the output
                      artifact is stored in ``MyArtifacts/*build-ID* /MyArtifact.zip`` .

                      * If ``path`` is empty, ``namespaceType`` is set to ``NONE`` , and ``name`` is
                      set to "``/`` ", the output artifact is stored in the root of the output
                      bucket.

                      * If ``path`` is set to ``MyArtifacts`` , ``namespaceType`` is set to
                      ``BUILD_ID`` , and ``name`` is set to "``/`` ", the output artifact is stored
                      in ``MyArtifacts/*build-ID* `` .

                    - **packaging** *(string) --*

                      The type of build output artifact to create:

                      * If ``type`` is set to ``CODEPIPELINE`` , AWS CodePipeline ignores this value
                      if specified. This is because AWS CodePipeline manages its build output
                      artifacts instead of AWS CodeBuild.

                      * If ``type`` is set to ``NO_ARTIFACTS`` , this value is ignored if specified,
                      because no build output is produced.

                      * If ``type`` is set to ``S3`` , valid values include:

                        * ``NONE`` : AWS CodeBuild creates in the output bucket a folder that
                        contains the build output. This is the default if ``packaging`` is not
                        specified.

                        * ``ZIP`` : AWS CodeBuild creates in the output bucket a ZIP file that
                        contains the build output.

                    - **overrideArtifactName** *(boolean) --*

                      If this flag is set, a name specified in the build spec file overrides the
                      artifact name. The name specified in a build spec file is calculated at build
                      time and uses the Shell Command Language. For example, you can append a date
                      and time to your artifact name so that it is always unique.

                    - **encryptionDisabled** *(boolean) --*

                      Set to true if you do not want your output artifacts encrypted. This option is
                      valid only if your artifacts type is Amazon Simple Storage Service (Amazon
                      S3). If this is set with another artifacts type, an invalidInputException is
                      thrown.

                    - **artifactIdentifier** *(string) --*

                      An identifier for this artifact definition.

                - **cache** *(dict) --*

                  Information about the cache for the build project.

                  - **type** *(string) --*

                    The type of cache used by the build project. Valid values include:

                    * ``NO_CACHE`` : The build project does not use any cache.

                    * ``S3`` : The build project reads and writes from and to S3.

                    * ``LOCAL`` : The build project stores a cache locally on a build host that is
                    only available to that build host.

                  - **location** *(string) --*

                    Information about the cache location:

                    * ``NO_CACHE`` or ``LOCAL`` : This value is ignored.

                    * ``S3`` : This is the S3 bucket name/prefix.

                  - **modes** *(list) --*

                    If you use a ``LOCAL`` cache, the local cache mode. You can use one or more
                    local cache modes at the same time.

                    * ``LOCAL_SOURCE_CACHE`` mode caches Git metadata for primary and secondary
                    sources. After the cache is created, subsequent builds pull only the change
                    between commits. This mode is a good choice for projects with a clean working
                    directory and a source that is a large Git repository. If you choose this option
                    and your project does not use a Git repository (GitHub, GitHub Enterprise, or
                    Bitbucket), the option is ignored.

                    * ``LOCAL_DOCKER_LAYER_CACHE`` mode caches existing Docker layers. This mode is
                    a good choice for projects that build or pull large Docker images. It can
                    prevent the performance issues caused by pulling large Docker images down from
                    the network.

                    .. note::

                        * You can use a Docker layer cache in the Linux environment only.

                        * The ``privileged`` flag must be set so that your project has the required
                        Docker permissions.

                        * You should consider the security implications before you use a Docker
                        layer cache.

                    * ``LOCAL_CUSTOM_CACHE`` mode caches directories you specify in the buildspec
                    file. This mode is a good choice if your build scenario is not suited to one of
                    the other three local cache modes. If you use a custom cache:

                      * Only directories can be specified for caching. You cannot specify individual
                      files.

                      * Symlinks are used to reference cached directories.

                      * Cached directories are linked to your build before it downloads its project
                      sources. Cached items are overridden if a source item has the same name.
                      Directories are specified using cache paths in the buildspec file.

                    - *(string) --*

                - **environment** *(dict) --*

                  Information about the build environment for this build project.

                  - **type** *(string) --*

                    The type of build environment to use for related builds.

                    * The environment type ``ARM_CONTAINER`` is available only in regions US East
                    (N. Virginia), US East (Ohio), US West (Oregon), EU (Ireland), Asia Pacific
                    (Mumbai), Asia Pacific (Tokyo), Asia Pacific (Sydney), and EU (Frankfurt).

                    * The environment type ``LINUX_CONTAINER`` with compute type
                    ``build.general1.2xlarge`` is available only in regions US East (N. Virginia),
                    US East (N. Virginia), US West (Oregon), Canada (Central), EU (Ireland), EU
                    (London), EU (Frankfurt), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia
                    Pacific (Singapore), Asia Pacific (Sydney), China (Beijing), and China
                    (Ningxia).

                    * The environment type ``LINUX_GPU_CONTAINER`` is available only in regions US
                    East (N. Virginia), US East (N. Virginia), US West (Oregon), Canada (Central),
                    EU (Ireland), EU (London), EU (Frankfurt), Asia Pacific (Tokyo), Asia Pacific
                    (Seoul), Asia Pacific (Singapore), Asia Pacific (Sydney) , China (Beijing), and
                    China (Ningxia).

                  - **image** *(string) --*

                    The image tag or image digest that identifies the Docker image to use for this
                    build project. Use the following formats:

                    * For an image tag: ``registry/repository:tag`` . For example, to specify an
                    image with the tag "latest," use ``registry/repository:latest`` .

                    * For an image digest: ``registry/repository@digest`` . For example, to specify
                    an image with the digest
                    "sha256:cbbf2f9a99b47fc460d422812b6a5adff7dfee951d8fa2e4a98caa0382cfbdbf," use
                    ``registry/repository@sha256:cbbf2f9a99b47fc460d422812b6a5adff7dfee951d8fa2e4a98caa0382cfbdbf``
                    .

                  - **computeType** *(string) --*

                    Information about the compute resources the build project uses. Available values
                    include:

                    * ``BUILD_GENERAL1_SMALL`` : Use up to 3 GB memory and 2 vCPUs for builds.

                    * ``BUILD_GENERAL1_MEDIUM`` : Use up to 7 GB memory and 4 vCPUs for builds.

                    * ``BUILD_GENERAL1_LARGE`` : Use up to 16 GB memory and 8 vCPUs for builds,
                    depending on your environment type.

                    * ``BUILD_GENERAL1_2XLARGE`` : Use up to 145 GB memory, 72 vCPUs, and 824 GB of
                    SSD storage for builds. This compute type supports Docker images up to 100 GB
                    uncompressed.

                    If you use ``BUILD_GENERAL1_LARGE`` :

                    * For environment type ``LINUX_CONTAINER`` , you can use up to 15 GB memory and
                    8 vCPUs for builds.

                    * For environment type ``LINUX_GPU_CONTAINER`` , you can use up to 255 GB
                    memory, 32 vCPUs, and 4 NVIDIA Tesla V100 GPUs for builds.

                    * For environment type ``ARM_CONTAINER`` , you can use up to 16 GB memory and 8
                    vCPUs on ARM-based processors for builds.

                    For more information, see `Build Environment Compute Types
                    <https://docs.aws.amazon.com/codebuild/latest/userguide/build-env-ref-compute-types.html>`__
                    in the *AWS CodeBuild User Guide.*

                  - **environmentVariables** *(list) --*

                    A set of environment variables to make available to builds for this build
                    project.

                    - *(dict) --*

                      Information about an environment variable for a build project or a build.

                      - **name** *(string) --*

                        The name or key of the environment variable.

                      - **value** *(string) --*

                        The value of the environment variable.

                        .. warning::

                          We strongly discourage the use of environment variables to store sensitive
                          values, especially AWS secret key IDs and secret access keys. Environment
                          variables can be displayed in plain text using the AWS CodeBuild console
                          and the AWS Command Line Interface (AWS CLI).

                      - **type** *(string) --*

                        The type of environment variable. Valid values include:

                        * ``PARAMETER_STORE`` : An environment variable stored in Amazon EC2 Systems
                        Manager Parameter Store.

                        * ``PLAINTEXT`` : An environment variable in plain text format.

                        * ``SECRETS_MANAGER`` : An environment variable stored in AWS Secrets
                        Manager.

                  - **privilegedMode** *(boolean) --*

                    Enables running the Docker daemon inside a Docker container. Set to true only if
                    the build project is used to build Docker images. Otherwise, a build that
                    attempts to interact with the Docker daemon fails. The default setting is
                    ``false`` .

                    You can initialize the Docker daemon during the install phase of your build by
                    adding one of the following sets of commands to the install phase of your
                    buildspec file:

                    If the operating system's base image is Ubuntu Linux:

                     ``- nohup /usr/local/bin/dockerd --host=
                         unix:///var/run/docker.sock
                     --host=tcp://0.0.0.0:2375 --storage-driver=overlay&``

                     ``- timeout 15 sh -c "until docker info; do echo .; sleep 1; done"``

                    If the operating system's base image is Alpine Linux and the previous command
                    does not work, add the ``-t`` argument to ``timeout`` :

                     ``- nohup /usr/local/bin/dockerd --host=
                         unix:///var/run/docker.sock
                     --host=tcp://0.0.0.0:2375 --storage-driver=overlay&``

                     ``- timeout -t 15 sh -c "until docker info; do echo .; sleep 1; done"``

                  - **certificate** *(string) --*

                    The certificate to use with this build project.

                  - **registryCredential** *(dict) --*

                    The credentials for access to a private registry.

                    - **credential** *(string) --*

                      The Amazon Resource Name (ARN) or name of credentials created using AWS
                      Secrets Manager.

                      .. note::

                        The ``credential`` can use the name of the credentials only if they exist in
                        your current region.

                    - **credentialProvider** *(string) --*

                      The service that created the credentials to access a private Docker registry.
                      The valid value, SECRETS_MANAGER, is for AWS Secrets Manager.

                  - **imagePullCredentialsType** *(string) --*

                    The type of credentials AWS CodeBuild uses to pull images in your build. There
                    are two valid values:

                    * ``CODEBUILD`` specifies that AWS CodeBuild uses its own credentials. This
                    requires that you modify your ECR repository policy to trust AWS CodeBuild's
                    service principal.

                    * ``SERVICE_ROLE`` specifies that AWS CodeBuild uses your build project's
                    service role.

                    When you use a cross-account or private registry image, you must use
                    SERVICE_ROLE credentials. When you use an AWS CodeBuild curated image, you must
                    use CODEBUILD credentials.

                - **serviceRole** *(string) --*

                  The ARN of the AWS Identity and Access Management (IAM) role that enables AWS
                  CodeBuild to interact with dependent AWS services on behalf of the AWS account.

                - **timeoutInMinutes** *(integer) --*

                  How long, in minutes, from 5 to 480 (8 hours), for AWS CodeBuild to wait before
                  timing out any related build that did not get marked as completed. The default is
                  60 minutes.

                - **queuedTimeoutInMinutes** *(integer) --*

                  The number of minutes a build is allowed to be queued before it times out.

                - **encryptionKey** *(string) --*

                  The AWS Key Management Service (AWS KMS) customer master key (CMK) to be used for
                  encrypting the build output artifacts.

                  .. note::

                    You can use a cross-account KMS key to encrypt the build output artifacts if
                    your service role has permission to that key.

                  You can specify either the Amazon Resource Name (ARN) of the CMK or, if available,
                  the CMK's alias (using the format ``alias/*alias-name* `` ).

                - **tags** *(list) --*

                  The tags for this build project.

                  These tags are available for use by AWS services that support AWS CodeBuild build
                  project tags.

                  - *(dict) --*

                    A tag, consisting of a key and a value.

                    This tag is available for use by AWS services that support tags in AWS
                    CodeBuild.

                    - **key** *(string) --*

                      The tag's key.

                    - **value** *(string) --*

                      The tag's value.

                - **created** *(datetime) --*

                  When the build project was created, expressed in Unix time format.

                - **lastModified** *(datetime) --*

                  When the build project's settings were last modified, expressed in Unix time
                  format.

                - **webhook** *(dict) --*

                  Information about a webhook that connects repository events to a build project in
                  AWS CodeBuild.

                  - **url** *(string) --*

                    The URL to the webhook.

                  - **payloadUrl** *(string) --*

                    The AWS CodeBuild endpoint where webhook events are sent.

                  - **secret** *(string) --*

                    The secret token of the associated repository.

                    .. note::

                      A Bitbucket webhook does not support ``secret`` .

                  - **branchFilter** *(string) --*

                    A regular expression used to determine which repository branches are built when
                    a webhook is triggered. If the name of a branch matches the regular expression,
                    then it is built. If ``branchFilter`` is empty, then all branches are built.

                    .. note::

                      It is recommended that you use ``filterGroups`` instead of ``branchFilter`` .

                  - **filterGroups** *(list) --*

                    An array of arrays of ``WebhookFilter`` objects used to determine which webhooks
                    are triggered. At least one ``WebhookFilter`` in the array must specify
                    ``EVENT`` as its ``type`` .

                    For a build to be triggered, at least one filter group in the ``filterGroups``
                    array must pass. For a filter group to pass, each of its filters must pass.

                    - *(list) --*

                      - *(dict) --*

                        A filter used to determine which webhooks trigger a build.

                        - **type** *(string) --*

                          The type of webhook filter. There are five webhook filter types: ``EVENT``
                          , ``ACTOR_ACCOUNT_ID`` , ``HEAD_REF`` , ``BASE_REF`` , and ``FILE_PATH`` .

                            EVENT

                          A webhook event triggers a build when the provided ``pattern`` matches one
                          of four event types: ``PUSH`` , ``PULL_REQUEST_CREATED`` ,
                          ``PULL_REQUEST_UPDATED`` , and ``PULL_REQUEST_REOPENED`` . The ``EVENT``
                          patterns are specified as a comma-separated string. For example, ``PUSH,
                          PULL_REQUEST_CREATED, PULL_REQUEST_UPDATED`` filters all push, pull
                          request created, and pull request updated events.

                          .. note::

                            The ``PULL_REQUEST_REOPENED`` works with GitHub and GitHub Enterprise
                            only.

                            ACTOR_ACCOUNT_ID

                          A webhook event triggers a build when a GitHub, GitHub Enterprise, or
                          Bitbucket account ID matches the regular expression ``pattern`` .

                            HEAD_REF

                          A webhook event triggers a build when the head reference matches the
                          regular expression ``pattern`` . For example, ``refs/heads/branch-name``
                          and ``refs/tags/tag-name`` .

                          Works with GitHub and GitHub Enterprise push, GitHub and GitHub Enterprise
                          pull request, Bitbucket push, and Bitbucket pull request events.

                            BASE_REF

                          A webhook event triggers a build when the base reference matches the
                          regular expression ``pattern`` . For example, ``refs/heads/branch-name`` .

                          .. note::

                            Works with pull request events only.

                            FILE_PATH

                          A webhook triggers a build when the path of a changed file matches the
                          regular expression ``pattern`` .

                          .. note::

                            Works with GitHub and GitHub Enterprise push events only.

                        - **pattern** *(string) --*

                          For a ``WebHookFilter`` that uses ``EVENT`` type, a comma-separated string
                          that specifies one or more events. For example, the webhook filter ``PUSH,
                          PULL_REQUEST_CREATED, PULL_REQUEST_UPDATED`` allows all push, pull request
                          created, and pull request updated events to trigger a build.

                          For a ``WebHookFilter`` that uses any of the other filter types, a regular
                          expression pattern. For example, a ``WebHookFilter`` that uses
                          ``HEAD_REF`` for its ``type`` and the pattern ``^refs/heads/`` triggers a
                          build when the head reference is a branch with a reference name
                          ``refs/heads/branch-name`` .

                        - **excludeMatchedPattern** *(boolean) --*

                          Used to indicate that the ``pattern`` determines which webhook events do
                          not trigger a build. If true, then a webhook event that does not match the
                          ``pattern`` triggers a build. If false, then a webhook event that matches
                          the ``pattern`` triggers a build.

                  - **lastModifiedSecret** *(datetime) --*

                    A timestamp that indicates the last time a repository's secret token was
                    modified.

                - **vpcConfig** *(dict) --*

                  Information about the VPC configuration that AWS CodeBuild accesses.

                  - **vpcId** *(string) --*

                    The ID of the Amazon VPC.

                  - **subnets** *(list) --*

                    A list of one or more subnet IDs in your Amazon VPC.

                    - *(string) --*

                  - **securityGroupIds** *(list) --*

                    A list of one or more security groups IDs in your Amazon VPC.

                    - *(string) --*

                - **badge** *(dict) --*

                  Information about the build badge for the build project.

                  - **badgeEnabled** *(boolean) --*

                    Set this to true to generate a publicly accessible URL for your project's build
                    badge.

                  - **badgeRequestUrl** *(string) --*

                    The publicly-accessible URL through which you can access the build badge for
                    your project.

                    The publicly accessible URL through which you can access the build badge for
                    your project.

                - **logsConfig** *(dict) --*

                  Information about logs for the build project. A project can create logs in Amazon
                  CloudWatch Logs, an S3 bucket, or both.

                  - **cloudWatchLogs** *(dict) --*

                    Information about Amazon CloudWatch Logs for a build project. Amazon CloudWatch
                    Logs are enabled by default.

                    - **status** *(string) --*

                      The current status of the logs in Amazon CloudWatch Logs for a build project.
                      Valid values are:

                      * ``ENABLED`` : Amazon CloudWatch Logs are enabled for this build project.

                      * ``DISABLED`` : Amazon CloudWatch Logs are not enabled for this build
                      project.

                    - **groupName** *(string) --*

                      The group name of the logs in Amazon CloudWatch Logs. For more information,
                      see `Working with Log Groups and Log Streams
                      <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html>`__
                      .

                    - **streamName** *(string) --*

                      The prefix of the stream name of the Amazon CloudWatch Logs. For more
                      information, see `Working with Log Groups and Log Streams
                      <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html>`__
                      .

                  - **s3Logs** *(dict) --*

                    Information about logs built to an S3 bucket for a build project. S3 logs are
                    not enabled by default.

                    - **status** *(string) --*

                      The current status of the S3 build logs. Valid values are:

                      * ``ENABLED`` : S3 build logs are enabled for this build project.

                      * ``DISABLED`` : S3 build logs are not enabled for this build project.

                    - **location** *(string) --*

                      The ARN of an S3 bucket and the path prefix for S3 logs. If your Amazon S3
                      bucket name is ``my-bucket`` , and your path prefix is ``build-log`` , then
                      acceptable formats are ``my-bucket/build-log`` or
                      ``arn:aws:s3:::my-bucket/build-log`` .

                    - **encryptionDisabled** *(boolean) --*

                      Set to true if you do not want your S3 build log output encrypted. By default
                      S3 build logs are encrypted.

            - **projectsNotFound** *(list) --*

              The names of build projects for which information could not be found.

              - *(string) --*
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def batch_get_report_groups(
        self, reportGroupArns: List[str]
    ) -> ClientBatchGetReportGroupsResponseTypeDef:
        """
        Returns an array of report groups.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/codebuild-2016-10-06/BatchGetReportGroups>`_

        **Request Syntax**
        ::

          response = client.batch_get_report_groups(
              reportGroupArns=[
                  'string',
              ]
          )
        :type reportGroupArns: list
        :param reportGroupArns: **[REQUIRED]**

          An array of report group ARNs that identify the report groups to return.

          - *(string) --*

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'reportGroups': [
                    {
                        'arn': 'string',
                        'name': 'string',
                        'type': 'TEST',
                        'exportConfig': {
                            'exportConfigType': 'S3'|'NO_EXPORT',
                            's3Destination': {
                                'bucket': 'string',
                                'path': 'string',
                                'packaging': 'ZIP'|'NONE',
                                'encryptionKey': 'string',
                                'encryptionDisabled': True|False
                            }
                        },
                        'created': datetime(2015, 1, 1),
                        'lastModified': datetime(2015, 1, 1)
                    },
                ],
                'reportGroupsNotFound': [
                    'string',
                ]
            }
          **Response Structure**

          - *(dict) --*

            - **reportGroups** *(list) --*

              The array of report groups returned by ``BatchGetReportGroups`` .

              - *(dict) --*

                A series of reports. Each report contains information about the results from running
                a series of test cases. You specify the test cases for a report group in the
                buildspec for a build project using one or more paths to the test case files.

                - **arn** *(string) --*

                  The ARN of a ``ReportGroup`` .

                - **name** *(string) --*

                  The name of a ``ReportGroup`` .

                - **type** *(string) --*

                  The type of the ``ReportGroup`` . The one valid value is ``TEST`` .

                - **exportConfig** *(dict) --*

                  Information about the destination where the raw data of this ``ReportGroup`` is
                  exported.

                  - **exportConfigType** *(string) --*

                    The export configuration type. Valid values are:

                    * ``S3`` : The report results are exported to an S3 bucket.

                    * ``NO_EXPORT`` : The report results are not exported.

                  - **s3Destination** *(dict) --*

                    A ``S3ReportExportConfig`` object that contains information about the S3 bucket
                    where the run of a report is exported.

                    - **bucket** *(string) --*

                      The name of the S3 bucket where the raw data of a report are exported.

                    - **path** *(string) --*

                      The path to the exported report's raw data results.

                    - **packaging** *(string) --*

                      The type of build output artifact to create. Valid values include:

                      * ``NONE`` : AWS CodeBuild creates the raw data in the output bucket. This is
                      the default if packaging is not specified.

                      * ``ZIP`` : AWS CodeBuild creates a ZIP file with the raw data in the output
                      bucket.

                    - **encryptionKey** *(string) --*

                      The encryption key for the report's encrypted raw data.

                    - **encryptionDisabled** *(boolean) --*

                      A boolean value that specifies if the results of a report are encrypted.

                - **created** *(datetime) --*

                  The date and time this ``ReportGroup`` was created.

                - **lastModified** *(datetime) --*

                  The date and time this ``ReportGroup`` was last modified.

            - **reportGroupsNotFound** *(list) --*

              An array of ARNs passed to ``BatchGetReportGroups`` that are not associated with a
              ``ReportGroup`` .

              - *(string) --*
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def batch_get_reports(self, reportArns: List[str]) -> ClientBatchGetReportsResponseTypeDef:
        """
        Returns an array of reports.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/codebuild-2016-10-06/BatchGetReports>`_

        **Request Syntax**
        ::

          response = client.batch_get_reports(
              reportArns=[
                  'string',
              ]
          )
        :type reportArns: list
        :param reportArns: **[REQUIRED]**

          An array of ARNs that identify the ``Report`` objects to return.

          - *(string) --*

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'reports': [
                    {
                        'arn': 'string',
                        'type': 'TEST',
                        'name': 'string',
                        'reportGroupArn': 'string',
                        'executionId': 'string',
                        'status': 'GENERATING'|'SUCCEEDED'|'FAILED'|'INCOMPLETE'|'DELETING',
                        'created': datetime(2015, 1, 1),
                        'expired': datetime(2015, 1, 1),
                        'exportConfig': {
                            'exportConfigType': 'S3'|'NO_EXPORT',
                            's3Destination': {
                                'bucket': 'string',
                                'path': 'string',
                                'packaging': 'ZIP'|'NONE',
                                'encryptionKey': 'string',
                                'encryptionDisabled': True|False
                            }
                        },
                        'truncated': True|False,
                        'testSummary': {
                            'total': 123,
                            'statusCounts': {
                                'string': 123
                            },
                            'durationInNanoSeconds': 123
                        }
                    },
                ],
                'reportsNotFound': [
                    'string',
                ]
            }
          **Response Structure**

          - *(dict) --*

            - **reports** *(list) --*

              The array of ``Report`` objects returned by ``BatchGetReports`` .

              - *(dict) --*

                Information about the results from running a series of test cases during the run of
                a build project. The test cases are specified in the buildspec for the build project
                using one or more paths to the test case files. You can specify any type of tests
                you want, such as unit tests, integration tests, and functional tests.

                - **arn** *(string) --*

                  The ARN of the report run.

                - **type** *(string) --*

                  The type of the report that was run.

                - **name** *(string) --*

                  The name of the report that was run.

                - **reportGroupArn** *(string) --*

                  The ARN of the report group associated with this report.

                - **executionId** *(string) --*

                  The ARN of the build run that generated this report.

                - **status** *(string) --*

                  The status of this report.

                - **created** *(datetime) --*

                  The date and time this report run occurred.

                - **expired** *(datetime) --*

                  The date and time a report expires. A report expires 30 days after it is created.
                  An expired report is not available to view in CodeBuild.

                - **exportConfig** *(dict) --*

                  Information about where the raw data used to generate this report was exported.

                  - **exportConfigType** *(string) --*

                    The export configuration type. Valid values are:

                    * ``S3`` : The report results are exported to an S3 bucket.

                    * ``NO_EXPORT`` : The report results are not exported.

                  - **s3Destination** *(dict) --*

                    A ``S3ReportExportConfig`` object that contains information about the S3 bucket
                    where the run of a report is exported.

                    - **bucket** *(string) --*

                      The name of the S3 bucket where the raw data of a report are exported.

                    - **path** *(string) --*

                      The path to the exported report's raw data results.

                    - **packaging** *(string) --*

                      The type of build output artifact to create. Valid values include:

                      * ``NONE`` : AWS CodeBuild creates the raw data in the output bucket. This is
                      the default if packaging is not specified.

                      * ``ZIP`` : AWS CodeBuild creates a ZIP file with the raw data in the output
                      bucket.

                    - **encryptionKey** *(string) --*

                      The encryption key for the report's encrypted raw data.

                    - **encryptionDisabled** *(boolean) --*

                      A boolean value that specifies if the results of a report are encrypted.

                - **truncated** *(boolean) --*

                  A boolean that specifies if this report run is truncated. The list of test cases
                  is truncated after the maximum number of test cases is reached.

                - **testSummary** *(dict) --*

                  A ``TestReportSummary`` object that contains information about this test report.

                  - **total** *(integer) --*

                    The number of test cases in this ``TestReportSummary`` . The total includes
                    truncated test cases.

                  - **statusCounts** *(dict) --*

                    A map that contains the number of each type of status returned by the test
                    results in this ``TestReportSummary`` .

                    - *(string) --*

                      - *(integer) --*

                  - **durationInNanoSeconds** *(integer) --*

                    The number of nanoseconds it took to run all of the test cases in this report.

            - **reportsNotFound** *(list) --*

              An array of ARNs passed to ``BatchGetReportGroups`` that are not associated with a
              ``Report`` .

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
    def create_project(
        self,
        name: str,
        source: ClientCreateProjectSourceTypeDef,
        artifacts: ClientCreateProjectArtifactsTypeDef,
        environment: ClientCreateProjectEnvironmentTypeDef,
        serviceRole: str,
        description: str = None,
        secondarySources: List[ClientCreateProjectSecondarySourcesTypeDef] = None,
        sourceVersion: str = None,
        secondarySourceVersions: List[ClientCreateProjectSecondarySourceVersionsTypeDef] = None,
        secondaryArtifacts: List[ClientCreateProjectSecondaryArtifactsTypeDef] = None,
        cache: ClientCreateProjectCacheTypeDef = None,
        timeoutInMinutes: int = None,
        queuedTimeoutInMinutes: int = None,
        encryptionKey: str = None,
        tags: List[ClientCreateProjectTagsTypeDef] = None,
        vpcConfig: ClientCreateProjectVpcConfigTypeDef = None,
        badgeEnabled: bool = None,
        logsConfig: ClientCreateProjectLogsConfigTypeDef = None,
    ) -> ClientCreateProjectResponseTypeDef:
        """
        Creates a build project.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/codebuild-2016-10-06/CreateProject>`_

        **Request Syntax**
        ::

          response = client.create_project(
              name='string',
              description='string',
              source={
                  'type':
                  'CODECOMMIT'|'CODEPIPELINE'|'GITHUB'|'S3'|'BITBUCKET'
                  |'GITHUB_ENTERPRISE'|'NO_SOURCE',
                  'location': 'string',
                  'gitCloneDepth': 123,
                  'gitSubmodulesConfig': {
                      'fetchSubmodules': True|False
                  },
                  'buildspec': 'string',
                  'auth': {
                      'type': 'OAUTH',
                      'resource': 'string'
                  },
                  'reportBuildStatus': True|False,
                  'insecureSsl': True|False,
                  'sourceIdentifier': 'string'
              },
              secondarySources=[
                  {
                      'type':
                      'CODECOMMIT'|'CODEPIPELINE'|'GITHUB'|'S3'|'BITBUCKET'
                      |'GITHUB_ENTERPRISE'|'NO_SOURCE',
                      'location': 'string',
                      'gitCloneDepth': 123,
                      'gitSubmodulesConfig': {
                          'fetchSubmodules': True|False
                      },
                      'buildspec': 'string',
                      'auth': {
                          'type': 'OAUTH',
                          'resource': 'string'
                      },
                      'reportBuildStatus': True|False,
                      'insecureSsl': True|False,
                      'sourceIdentifier': 'string'
                  },
              ],
              sourceVersion='string',
              secondarySourceVersions=[
                  {
                      'sourceIdentifier': 'string',
                      'sourceVersion': 'string'
                  },
              ],
              artifacts={
                  'type': 'CODEPIPELINE'|'S3'|'NO_ARTIFACTS',
                  'location': 'string',
                  'path': 'string',
                  'namespaceType': 'NONE'|'BUILD_ID',
                  'name': 'string',
                  'packaging': 'NONE'|'ZIP',
                  'overrideArtifactName': True|False,
                  'encryptionDisabled': True|False,
                  'artifactIdentifier': 'string'
              },
              secondaryArtifacts=[
                  {
                      'type': 'CODEPIPELINE'|'S3'|'NO_ARTIFACTS',
                      'location': 'string',
                      'path': 'string',
                      'namespaceType': 'NONE'|'BUILD_ID',
                      'name': 'string',
                      'packaging': 'NONE'|'ZIP',
                      'overrideArtifactName': True|False,
                      'encryptionDisabled': True|False,
                      'artifactIdentifier': 'string'
                  },
              ],
              cache={
                  'type': 'NO_CACHE'|'S3'|'LOCAL',
                  'location': 'string',
                  'modes': [
                      'LOCAL_DOCKER_LAYER_CACHE'|'LOCAL_SOURCE_CACHE'|'LOCAL_CUSTOM_CACHE',
                  ]
              },
              environment={
                  'type':
                  'WINDOWS_CONTAINER'|'LINUX_CONTAINER'|'LINUX_GPU_CONTAINER'
                  |'ARM_CONTAINER',
                  'image': 'string',
                  'computeType':
                  'BUILD_GENERAL1_SMALL'|'BUILD_GENERAL1_MEDIUM'|'BUILD_GENERAL1_LARGE'
                  |'BUILD_GENERAL1_2XLARGE',
                  'environmentVariables': [
                      {
                          'name': 'string',
                          'value': 'string',
                          'type': 'PLAINTEXT'|'PARAMETER_STORE'|'SECRETS_MANAGER'
                      },
                  ],
                  'privilegedMode': True|False,
                  'certificate': 'string',
                  'registryCredential': {
                      'credential': 'string',
                      'credentialProvider': 'SECRETS_MANAGER'
                  },
                  'imagePullCredentialsType': 'CODEBUILD'|'SERVICE_ROLE'
              },
              serviceRole='string',
              timeoutInMinutes=123,
              queuedTimeoutInMinutes=123,
              encryptionKey='string',
              tags=[
                  {
                      'key': 'string',
                      'value': 'string'
                  },
              ],
              vpcConfig={
                  'vpcId': 'string',
                  'subnets': [
                      'string',
                  ],
                  'securityGroupIds': [
                      'string',
                  ]
              },
              badgeEnabled=True|False,
              logsConfig={
                  'cloudWatchLogs': {
                      'status': 'ENABLED'|'DISABLED',
                      'groupName': 'string',
                      'streamName': 'string'
                  },
                  's3Logs': {
                      'status': 'ENABLED'|'DISABLED',
                      'location': 'string',
                      'encryptionDisabled': True|False
                  }
              }
          )
        :type name: string
        :param name: **[REQUIRED]**

          The name of the build project.

        :type description: string
        :param description:

          A description that makes the build project easy to identify.

        :type source: dict
        :param source: **[REQUIRED]**

          Information about the build input source code for the build project.

          - **type** *(string) --* **[REQUIRED]**

            The type of repository that contains the source code to be built. Valid values include:

            * ``BITBUCKET`` : The source code is in a Bitbucket repository.

            * ``CODECOMMIT`` : The source code is in an AWS CodeCommit repository.

            * ``CODEPIPELINE`` : The source code settings are specified in the source action of a
            pipeline in AWS CodePipeline.

            * ``GITHUB`` : The source code is in a GitHub repository.

            * ``GITHUB_ENTERPRISE`` : The source code is in a GitHub Enterprise repository.

            * ``NO_SOURCE`` : The project does not have input source code.

            * ``S3`` : The source code is in an Amazon Simple Storage Service (Amazon S3) input
            bucket.

          - **location** *(string) --*

            Information about the location of the source code to be built. Valid values include:

            * For source code settings that are specified in the source action of a pipeline in AWS
            CodePipeline, ``location`` should not be specified. If it is specified, AWS CodePipeline
            ignores it. This is because AWS CodePipeline uses the settings in a pipeline's source
            action instead of this value.

            * For source code in an AWS CodeCommit repository, the HTTPS clone URL to the repository
            that contains the source code and the build spec (for example,
            ``https://git-codecommit.*region-ID* .amazonaws.com/v1/repos/*repo-name* `` ).

            * For source code in an Amazon Simple Storage Service (Amazon S3) input bucket, one of
            the following.

              * The path to the ZIP file that contains the source code (for example, ``
              *bucket-name* /*path* /*to* /*object-name* .zip`` ).

              * The path to the folder that contains the source code (for example, `` *bucket-name*
              /*path* /*to* /*source-code* /*folder* /`` ).

            * For source code in a GitHub repository, the HTTPS clone URL to the repository that
            contains the source and the build spec. You must connect your AWS account to your GitHub
            account. Use the AWS CodeBuild console to start creating a build project. When you use
            the console to connect (or reconnect) with GitHub, on the GitHub **Authorize
            application** page, for **Organization access** , choose **Request access** next to each
            repository you want to allow AWS CodeBuild to have access to, and then choose
            **Authorize application** . (After you have connected to your GitHub account, you do not
            need to finish creating the build project. You can leave the AWS CodeBuild console.) To
            instruct AWS CodeBuild to use this connection, in the ``source`` object, set the
            ``auth`` object's ``type`` value to ``OAUTH`` .

            * For source code in a Bitbucket repository, the HTTPS clone URL to the repository that
            contains the source and the build spec. You must connect your AWS account to your
            Bitbucket account. Use the AWS CodeBuild console to start creating a build project. When
            you use the console to connect (or reconnect) with Bitbucket, on the Bitbucket **Confirm
            access to your account** page, choose **Grant access** . (After you have connected to
            your Bitbucket account, you do not need to finish creating the build project. You can
            leave the AWS CodeBuild console.) To instruct AWS CodeBuild to use this connection, in
            the ``source`` object, set the ``auth`` object's ``type`` value to ``OAUTH`` .

          - **gitCloneDepth** *(integer) --*

            Information about the Git clone depth for the build project.

          - **gitSubmodulesConfig** *(dict) --*

            Information about the Git submodules configuration for the build project.

            - **fetchSubmodules** *(boolean) --* **[REQUIRED]**

              Set to true to fetch Git submodules for your AWS CodeBuild build project.

          - **buildspec** *(string) --*

            The build spec declaration to use for the builds in this build project.

            If this value is not specified, a build spec must be included along with the source code
            to be built.

          - **auth** *(dict) --*

            Information about the authorization settings for AWS CodeBuild to access the source code
            to be built.

            This information is for the AWS CodeBuild console's use only. Your code should not get
            or set this information directly.

            - **type** *(string) --* **[REQUIRED]**

              .. note::

                This data type is deprecated and is no longer accurate or used.

              The authorization type to use. The only valid value is ``OAUTH`` , which represents
              the OAuth authorization type.

            - **resource** *(string) --*

              The resource value that applies to the specified authorization type.

          - **reportBuildStatus** *(boolean) --*

            Set to true to report the status of a build's start and finish to your source provider.
            This option is valid only when your source provider is GitHub, GitHub Enterprise, or
            Bitbucket. If this is set and you use a different source provider, an
            invalidInputException is thrown.

            .. note::

              The status of a build triggered by a webhook is always reported to your source
              provider.

          - **insecureSsl** *(boolean) --*

            Enable this flag to ignore SSL warnings while connecting to the project source code.

          - **sourceIdentifier** *(string) --*

            An identifier for this project source.

        :type secondarySources: list
        :param secondarySources:

          An array of ``ProjectSource`` objects.

          - *(dict) --*

            Information about the build input source code for the build project.

            - **type** *(string) --* **[REQUIRED]**

              The type of repository that contains the source code to be built. Valid values
              include:

              * ``BITBUCKET`` : The source code is in a Bitbucket repository.

              * ``CODECOMMIT`` : The source code is in an AWS CodeCommit repository.

              * ``CODEPIPELINE`` : The source code settings are specified in the source action of a
              pipeline in AWS CodePipeline.

              * ``GITHUB`` : The source code is in a GitHub repository.

              * ``GITHUB_ENTERPRISE`` : The source code is in a GitHub Enterprise repository.

              * ``NO_SOURCE`` : The project does not have input source code.

              * ``S3`` : The source code is in an Amazon Simple Storage Service (Amazon S3) input
              bucket.

            - **location** *(string) --*

              Information about the location of the source code to be built. Valid values include:

              * For source code settings that are specified in the source action of a pipeline in
              AWS CodePipeline, ``location`` should not be specified. If it is specified, AWS
              CodePipeline ignores it. This is because AWS CodePipeline uses the settings in a
              pipeline's source action instead of this value.

              * For source code in an AWS CodeCommit repository, the HTTPS clone URL to the
              repository that contains the source code and the build spec (for example,
              ``https://git-codecommit.*region-ID* .amazonaws.com/v1/repos/*repo-name* `` ).

              * For source code in an Amazon Simple Storage Service (Amazon S3) input bucket, one of
              the following.

                * The path to the ZIP file that contains the source code (for example, ``
                *bucket-name* /*path* /*to* /*object-name* .zip`` ).

                * The path to the folder that contains the source code (for example, ``
                *bucket-name* /*path* /*to* /*source-code* /*folder* /`` ).

              * For source code in a GitHub repository, the HTTPS clone URL to the repository that
              contains the source and the build spec. You must connect your AWS account to your
              GitHub account. Use the AWS CodeBuild console to start creating a build project. When
              you use the console to connect (or reconnect) with GitHub, on the GitHub **Authorize
              application** page, for **Organization access** , choose **Request access** next to
              each repository you want to allow AWS CodeBuild to have access to, and then choose
              **Authorize application** . (After you have connected to your GitHub account, you do
              not need to finish creating the build project. You can leave the AWS CodeBuild
              console.) To instruct AWS CodeBuild to use this connection, in the ``source`` object,
              set the ``auth`` object's ``type`` value to ``OAUTH`` .

              * For source code in a Bitbucket repository, the HTTPS clone URL to the repository
              that contains the source and the build spec. You must connect your AWS account to your
              Bitbucket account. Use the AWS CodeBuild console to start creating a build project.
              When you use the console to connect (or reconnect) with Bitbucket, on the Bitbucket
              **Confirm access to your account** page, choose **Grant access** . (After you have
              connected to your Bitbucket account, you do not need to finish creating the build
              project. You can leave the AWS CodeBuild console.) To instruct AWS CodeBuild to use
              this connection, in the ``source`` object, set the ``auth`` object's ``type`` value to
              ``OAUTH`` .

            - **gitCloneDepth** *(integer) --*

              Information about the Git clone depth for the build project.

            - **gitSubmodulesConfig** *(dict) --*

              Information about the Git submodules configuration for the build project.

              - **fetchSubmodules** *(boolean) --* **[REQUIRED]**

                Set to true to fetch Git submodules for your AWS CodeBuild build project.

            - **buildspec** *(string) --*

              The build spec declaration to use for the builds in this build project.

              If this value is not specified, a build spec must be included along with the source
              code to be built.

            - **auth** *(dict) --*

              Information about the authorization settings for AWS CodeBuild to access the source
              code to be built.

              This information is for the AWS CodeBuild console's use only. Your code should not get
              or set this information directly.

              - **type** *(string) --* **[REQUIRED]**

                .. note::

                  This data type is deprecated and is no longer accurate or used.

                The authorization type to use. The only valid value is ``OAUTH`` , which represents
                the OAuth authorization type.

              - **resource** *(string) --*

                The resource value that applies to the specified authorization type.

            - **reportBuildStatus** *(boolean) --*

              Set to true to report the status of a build's start and finish to your source
              provider. This option is valid only when your source provider is GitHub, GitHub
              Enterprise, or Bitbucket. If this is set and you use a different source provider, an
              invalidInputException is thrown.

              .. note::

                The status of a build triggered by a webhook is always reported to your source
                provider.

            - **insecureSsl** *(boolean) --*

              Enable this flag to ignore SSL warnings while connecting to the project source code.

            - **sourceIdentifier** *(string) --*

              An identifier for this project source.

        :type sourceVersion: string
        :param sourceVersion:

          A version of the build input to be built for this project. If not specified, the latest
          version is used. If specified, it must be one of:

          * For AWS CodeCommit: the commit ID, branch, or Git tag to use.

          * For GitHub: the commit ID, pull request ID, branch name, or tag name that corresponds to
          the version of the source code you want to build. If a pull request ID is specified, it
          must use the format ``pr/pull-request-ID`` (for example ``pr/25`` ). If a branch name is
          specified, the branch's HEAD commit ID is used. If not specified, the default branch's
          HEAD commit ID is used.

          * For Bitbucket: the commit ID, branch name, or tag name that corresponds to the version
          of the source code you want to build. If a branch name is specified, the branch's HEAD
          commit ID is used. If not specified, the default branch's HEAD commit ID is used.

          * For Amazon Simple Storage Service (Amazon S3): the version ID of the object that
          represents the build input ZIP file to use.

          If ``sourceVersion`` is specified at the build level, then that version takes precedence
          over this ``sourceVersion`` (at the project level).

          For more information, see `Source Version Sample with CodeBuild
          <https://docs.aws.amazon.com/codebuild/latest/userguide/sample-source-version.html>`__ in
          the *AWS CodeBuild User Guide* .

        :type secondarySourceVersions: list
        :param secondarySourceVersions:

          An array of ``ProjectSourceVersion`` objects. If ``secondarySourceVersions`` is specified
          at the build level, then they take precedence over these ``secondarySourceVersions`` (at
          the project level).

          - *(dict) --*

            A source identifier and its corresponding version.

            - **sourceIdentifier** *(string) --* **[REQUIRED]**

              An identifier for a source in the build project.

            - **sourceVersion** *(string) --* **[REQUIRED]**

              The source version for the corresponding source identifier. If specified, must be one
              of:

              * For AWS CodeCommit: the commit ID, branch, or Git tag to use.

              * For GitHub: the commit ID, pull request ID, branch name, or tag name that
              corresponds to the version of the source code you want to build. If a pull request ID
              is specified, it must use the format ``pr/pull-request-ID`` (for example, ``pr/25`` ).
              If a branch name is specified, the branch's HEAD commit ID is used. If not specified,
              the default branch's HEAD commit ID is used.

              * For Bitbucket: the commit ID, branch name, or tag name that corresponds to the
              version of the source code you want to build. If a branch name is specified, the
              branch's HEAD commit ID is used. If not specified, the default branch's HEAD commit ID
              is used.

              * For Amazon Simple Storage Service (Amazon S3): the version ID of the object that
              represents the build input ZIP file to use.

              For more information, see `Source Version Sample with CodeBuild
              <https://docs.aws.amazon.com/codebuild/latest/userguide/sample-source-version.html>`__
              in the *AWS CodeBuild User Guide* .

        :type artifacts: dict
        :param artifacts: **[REQUIRED]**

          Information about the build output artifacts for the build project.

          - **type** *(string) --* **[REQUIRED]**

            The type of build output artifact. Valid values include:

            * ``CODEPIPELINE`` : The build project has build output generated through AWS
            CodePipeline.

            .. note::

               The ``CODEPIPELINE`` type is not supported for ``secondaryArtifacts`` .

            * ``NO_ARTIFACTS`` : The build project does not produce any build output.

            * ``S3`` : The build project stores build output in Amazon Simple Storage Service
            (Amazon S3).

          - **location** *(string) --*

            Information about the build output artifact location:

            * If ``type`` is set to ``CODEPIPELINE`` , AWS CodePipeline ignores this value if
            specified. This is because AWS CodePipeline manages its build output locations instead
            of AWS CodeBuild.

            * If ``type`` is set to ``NO_ARTIFACTS`` , this value is ignored if specified, because
            no build output is produced.

            * If ``type`` is set to ``S3`` , this is the name of the output bucket.

          - **path** *(string) --*

            Along with ``namespaceType`` and ``name`` , the pattern that AWS CodeBuild uses to name
            and store the output artifact:

            * If ``type`` is set to ``CODEPIPELINE`` , AWS CodePipeline ignores this value if
            specified. This is because AWS CodePipeline manages its build output names instead of
            AWS CodeBuild.

            * If ``type`` is set to ``NO_ARTIFACTS`` , this value is ignored if specified, because
            no build output is produced.

            * If ``type`` is set to ``S3`` , this is the path to the output artifact. If ``path`` is
            not specified, ``path`` is not used.

            For example, if ``path`` is set to ``MyArtifacts`` , ``namespaceType`` is set to
            ``NONE`` , and ``name`` is set to ``MyArtifact.zip`` , the output artifact is stored in
            the output bucket at ``MyArtifacts/MyArtifact.zip`` .

          - **namespaceType** *(string) --*

            Along with ``path`` and ``name`` , the pattern that AWS CodeBuild uses to determine the
            name and location to store the output artifact:

            * If ``type`` is set to ``CODEPIPELINE`` , AWS CodePipeline ignores this value if
            specified. This is because AWS CodePipeline manages its build output names instead of
            AWS CodeBuild.

            * If ``type`` is set to ``NO_ARTIFACTS`` , this value is ignored if specified, because
            no build output is produced.

            * If ``type`` is set to ``S3`` , valid values include:

              * ``BUILD_ID`` : Include the build ID in the location of the build output artifact.

              * ``NONE`` : Do not include the build ID. This is the default if ``namespaceType`` is
              not specified.

            For example, if ``path`` is set to ``MyArtifacts`` , ``namespaceType`` is set to
            ``BUILD_ID`` , and ``name`` is set to ``MyArtifact.zip`` , the output artifact is stored
            in ``MyArtifacts/*build-ID* /MyArtifact.zip`` .

          - **name** *(string) --*

            Along with ``path`` and ``namespaceType`` , the pattern that AWS CodeBuild uses to name
            and store the output artifact:

            * If ``type`` is set to ``CODEPIPELINE`` , AWS CodePipeline ignores this value if
            specified. This is because AWS CodePipeline manages its build output names instead of
            AWS CodeBuild.

            * If ``type`` is set to ``NO_ARTIFACTS`` , this value is ignored if specified, because
            no build output is produced.

            * If ``type`` is set to ``S3`` , this is the name of the output artifact object. If you
            set the name to be a forward slash ("/"), the artifact is stored in the root of the
            output bucket.

            For example:

            * If ``path`` is set to ``MyArtifacts`` , ``namespaceType`` is set to ``BUILD_ID`` , and
            ``name`` is set to ``MyArtifact.zip`` , then the output artifact is stored in
            ``MyArtifacts/*build-ID* /MyArtifact.zip`` .

            * If ``path`` is empty, ``namespaceType`` is set to ``NONE`` , and ``name`` is set to
            "``/`` ", the output artifact is stored in the root of the output bucket.

            * If ``path`` is set to ``MyArtifacts`` , ``namespaceType`` is set to ``BUILD_ID`` , and
            ``name`` is set to "``/`` ", the output artifact is stored in ``MyArtifacts/*build-ID*
            `` .

          - **packaging** *(string) --*

            The type of build output artifact to create:

            * If ``type`` is set to ``CODEPIPELINE`` , AWS CodePipeline ignores this value if
            specified. This is because AWS CodePipeline manages its build output artifacts instead
            of AWS CodeBuild.

            * If ``type`` is set to ``NO_ARTIFACTS`` , this value is ignored if specified, because
            no build output is produced.

            * If ``type`` is set to ``S3`` , valid values include:

              * ``NONE`` : AWS CodeBuild creates in the output bucket a folder that contains the
              build output. This is the default if ``packaging`` is not specified.

              * ``ZIP`` : AWS CodeBuild creates in the output bucket a ZIP file that contains the
              build output.

          - **overrideArtifactName** *(boolean) --*

            If this flag is set, a name specified in the build spec file overrides the artifact
            name. The name specified in a build spec file is calculated at build time and uses the
            Shell Command Language. For example, you can append a date and time to your artifact
            name so that it is always unique.

          - **encryptionDisabled** *(boolean) --*

            Set to true if you do not want your output artifacts encrypted. This option is valid
            only if your artifacts type is Amazon Simple Storage Service (Amazon S3). If this is set
            with another artifacts type, an invalidInputException is thrown.

          - **artifactIdentifier** *(string) --*

            An identifier for this artifact definition.

        :type secondaryArtifacts: list
        :param secondaryArtifacts:

          An array of ``ProjectArtifacts`` objects.

          - *(dict) --*

            Information about the build output artifacts for the build project.

            - **type** *(string) --* **[REQUIRED]**

              The type of build output artifact. Valid values include:

              * ``CODEPIPELINE`` : The build project has build output generated through AWS
              CodePipeline.

              .. note::

                 The ``CODEPIPELINE`` type is not supported for ``secondaryArtifacts`` .

              * ``NO_ARTIFACTS`` : The build project does not produce any build output.

              * ``S3`` : The build project stores build output in Amazon Simple Storage Service
              (Amazon S3).

            - **location** *(string) --*

              Information about the build output artifact location:

              * If ``type`` is set to ``CODEPIPELINE`` , AWS CodePipeline ignores this value if
              specified. This is because AWS CodePipeline manages its build output locations instead
              of AWS CodeBuild.

              * If ``type`` is set to ``NO_ARTIFACTS`` , this value is ignored if specified, because
              no build output is produced.

              * If ``type`` is set to ``S3`` , this is the name of the output bucket.

            - **path** *(string) --*

              Along with ``namespaceType`` and ``name`` , the pattern that AWS CodeBuild uses to
              name and store the output artifact:

              * If ``type`` is set to ``CODEPIPELINE`` , AWS CodePipeline ignores this value if
              specified. This is because AWS CodePipeline manages its build output names instead of
              AWS CodeBuild.

              * If ``type`` is set to ``NO_ARTIFACTS`` , this value is ignored if specified, because
              no build output is produced.

              * If ``type`` is set to ``S3`` , this is the path to the output artifact. If ``path``
              is not specified, ``path`` is not used.

              For example, if ``path`` is set to ``MyArtifacts`` , ``namespaceType`` is set to
              ``NONE`` , and ``name`` is set to ``MyArtifact.zip`` , the output artifact is stored
              in the output bucket at ``MyArtifacts/MyArtifact.zip`` .

            - **namespaceType** *(string) --*

              Along with ``path`` and ``name`` , the pattern that AWS CodeBuild uses to determine
              the name and location to store the output artifact:

              * If ``type`` is set to ``CODEPIPELINE`` , AWS CodePipeline ignores this value if
              specified. This is because AWS CodePipeline manages its build output names instead of
              AWS CodeBuild.

              * If ``type`` is set to ``NO_ARTIFACTS`` , this value is ignored if specified, because
              no build output is produced.

              * If ``type`` is set to ``S3`` , valid values include:

                * ``BUILD_ID`` : Include the build ID in the location of the build output artifact.

                * ``NONE`` : Do not include the build ID. This is the default if ``namespaceType``
                is not specified.

              For example, if ``path`` is set to ``MyArtifacts`` , ``namespaceType`` is set to
              ``BUILD_ID`` , and ``name`` is set to ``MyArtifact.zip`` , the output artifact is
              stored in ``MyArtifacts/*build-ID* /MyArtifact.zip`` .

            - **name** *(string) --*

              Along with ``path`` and ``namespaceType`` , the pattern that AWS CodeBuild uses to
              name and store the output artifact:

              * If ``type`` is set to ``CODEPIPELINE`` , AWS CodePipeline ignores this value if
              specified. This is because AWS CodePipeline manages its build output names instead of
              AWS CodeBuild.

              * If ``type`` is set to ``NO_ARTIFACTS`` , this value is ignored if specified, because
              no build output is produced.

              * If ``type`` is set to ``S3`` , this is the name of the output artifact object. If
              you set the name to be a forward slash ("/"), the artifact is stored in the root of
              the output bucket.

              For example:

              * If ``path`` is set to ``MyArtifacts`` , ``namespaceType`` is set to ``BUILD_ID`` ,
              and ``name`` is set to ``MyArtifact.zip`` , then the output artifact is stored in
              ``MyArtifacts/*build-ID* /MyArtifact.zip`` .

              * If ``path`` is empty, ``namespaceType`` is set to ``NONE`` , and ``name`` is set to
              "``/`` ", the output artifact is stored in the root of the output bucket.

              * If ``path`` is set to ``MyArtifacts`` , ``namespaceType`` is set to ``BUILD_ID`` ,
              and ``name`` is set to "``/`` ", the output artifact is stored in
              ``MyArtifacts/*build-ID* `` .

            - **packaging** *(string) --*

              The type of build output artifact to create:

              * If ``type`` is set to ``CODEPIPELINE`` , AWS CodePipeline ignores this value if
              specified. This is because AWS CodePipeline manages its build output artifacts instead
              of AWS CodeBuild.

              * If ``type`` is set to ``NO_ARTIFACTS`` , this value is ignored if specified, because
              no build output is produced.

              * If ``type`` is set to ``S3`` , valid values include:

                * ``NONE`` : AWS CodeBuild creates in the output bucket a folder that contains the
                build output. This is the default if ``packaging`` is not specified.

                * ``ZIP`` : AWS CodeBuild creates in the output bucket a ZIP file that contains the
                build output.

            - **overrideArtifactName** *(boolean) --*

              If this flag is set, a name specified in the build spec file overrides the artifact
              name. The name specified in a build spec file is calculated at build time and uses the
              Shell Command Language. For example, you can append a date and time to your artifact
              name so that it is always unique.

            - **encryptionDisabled** *(boolean) --*

              Set to true if you do not want your output artifacts encrypted. This option is valid
              only if your artifacts type is Amazon Simple Storage Service (Amazon S3). If this is
              set with another artifacts type, an invalidInputException is thrown.

            - **artifactIdentifier** *(string) --*

              An identifier for this artifact definition.

        :type cache: dict
        :param cache:

          Stores recently used information so that it can be quickly accessed at a later time.

          - **type** *(string) --* **[REQUIRED]**

            The type of cache used by the build project. Valid values include:

            * ``NO_CACHE`` : The build project does not use any cache.

            * ``S3`` : The build project reads and writes from and to S3.

            * ``LOCAL`` : The build project stores a cache locally on a build host that is only
            available to that build host.

          - **location** *(string) --*

            Information about the cache location:

            * ``NO_CACHE`` or ``LOCAL`` : This value is ignored.

            * ``S3`` : This is the S3 bucket name/prefix.

          - **modes** *(list) --*

            If you use a ``LOCAL`` cache, the local cache mode. You can use one or more local cache
            modes at the same time.

            * ``LOCAL_SOURCE_CACHE`` mode caches Git metadata for primary and secondary sources.
            After the cache is created, subsequent builds pull only the change between commits. This
            mode is a good choice for projects with a clean working directory and a source that is a
            large Git repository. If you choose this option and your project does not use a Git
            repository (GitHub, GitHub Enterprise, or Bitbucket), the option is ignored.

            * ``LOCAL_DOCKER_LAYER_CACHE`` mode caches existing Docker layers. This mode is a good
            choice for projects that build or pull large Docker images. It can prevent the
            performance issues caused by pulling large Docker images down from the network.

            .. note::

                * You can use a Docker layer cache in the Linux environment only.

                * The ``privileged`` flag must be set so that your project has the required Docker
                permissions.

                * You should consider the security implications before you use a Docker layer cache.

            * ``LOCAL_CUSTOM_CACHE`` mode caches directories you specify in the buildspec file. This
            mode is a good choice if your build scenario is not suited to one of the other three
            local cache modes. If you use a custom cache:

              * Only directories can be specified for caching. You cannot specify individual files.

              * Symlinks are used to reference cached directories.

              * Cached directories are linked to your build before it downloads its project sources.
              Cached items are overridden if a source item has the same name. Directories are
              specified using cache paths in the buildspec file.

            - *(string) --*

        :type environment: dict
        :param environment: **[REQUIRED]**

          Information about the build environment for the build project.

          - **type** *(string) --* **[REQUIRED]**

            The type of build environment to use for related builds.

            * The environment type ``ARM_CONTAINER`` is available only in regions US East (N.
            Virginia), US East (Ohio), US West (Oregon), EU (Ireland), Asia Pacific (Mumbai), Asia
            Pacific (Tokyo), Asia Pacific (Sydney), and EU (Frankfurt).

            * The environment type ``LINUX_CONTAINER`` with compute type ``build.general1.2xlarge``
            is available only in regions US East (N. Virginia), US East (N. Virginia), US West
            (Oregon), Canada (Central), EU (Ireland), EU (London), EU (Frankfurt), Asia Pacific
            (Tokyo), Asia Pacific (Seoul), Asia Pacific (Singapore), Asia Pacific (Sydney), China
            (Beijing), and China (Ningxia).

            * The environment type ``LINUX_GPU_CONTAINER`` is available only in regions US East (N.
            Virginia), US East (N. Virginia), US West (Oregon), Canada (Central), EU (Ireland), EU
            (London), EU (Frankfurt), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific
            (Singapore), Asia Pacific (Sydney) , China (Beijing), and China (Ningxia).

          - **image** *(string) --* **[REQUIRED]**

            The image tag or image digest that identifies the Docker image to use for this build
            project. Use the following formats:

            * For an image tag: ``registry/repository:tag`` . For example, to specify an image with
            the tag "latest," use ``registry/repository:latest`` .

            * For an image digest: ``registry/repository@digest`` . For example, to specify an image
            with the digest
            "sha256:cbbf2f9a99b47fc460d422812b6a5adff7dfee951d8fa2e4a98caa0382cfbdbf," use
            ``registry/repository@sha256:cbbf2f9a99b47fc460d422812b6a5adff7dfee951d8fa2e4a98caa0382cfbdbf``
            .

          - **computeType** *(string) --* **[REQUIRED]**

            Information about the compute resources the build project uses. Available values
            include:

            * ``BUILD_GENERAL1_SMALL`` : Use up to 3 GB memory and 2 vCPUs for builds.

            * ``BUILD_GENERAL1_MEDIUM`` : Use up to 7 GB memory and 4 vCPUs for builds.

            * ``BUILD_GENERAL1_LARGE`` : Use up to 16 GB memory and 8 vCPUs for builds, depending on
            your environment type.

            * ``BUILD_GENERAL1_2XLARGE`` : Use up to 145 GB memory, 72 vCPUs, and 824 GB of SSD
            storage for builds. This compute type supports Docker images up to 100 GB uncompressed.

            If you use ``BUILD_GENERAL1_LARGE`` :

            * For environment type ``LINUX_CONTAINER`` , you can use up to 15 GB memory and 8 vCPUs
            for builds.

            * For environment type ``LINUX_GPU_CONTAINER`` , you can use up to 255 GB memory, 32
            vCPUs, and 4 NVIDIA Tesla V100 GPUs for builds.

            * For environment type ``ARM_CONTAINER`` , you can use up to 16 GB memory and 8 vCPUs on
            ARM-based processors for builds.

            For more information, see `Build Environment Compute Types
            <https://docs.aws.amazon.com/codebuild/latest/userguide/build-env-ref-compute-types.html>`__
            in the *AWS CodeBuild User Guide.*

          - **environmentVariables** *(list) --*

            A set of environment variables to make available to builds for this build project.

            - *(dict) --*

              Information about an environment variable for a build project or a build.

              - **name** *(string) --* **[REQUIRED]**

                The name or key of the environment variable.

              - **value** *(string) --* **[REQUIRED]**

                The value of the environment variable.

                .. warning::

                  We strongly discourage the use of environment variables to store sensitive values,
                  especially AWS secret key IDs and secret access keys. Environment variables can be
                  displayed in plain text using the AWS CodeBuild console and the AWS Command Line
                  Interface (AWS CLI).

              - **type** *(string) --*

                The type of environment variable. Valid values include:

                * ``PARAMETER_STORE`` : An environment variable stored in Amazon EC2 Systems Manager
                Parameter Store.

                * ``PLAINTEXT`` : An environment variable in plain text format.

                * ``SECRETS_MANAGER`` : An environment variable stored in AWS Secrets Manager.

          - **privilegedMode** *(boolean) --*

            Enables running the Docker daemon inside a Docker container. Set to true only if the
            build project is used to build Docker images. Otherwise, a build that attempts to
            interact with the Docker daemon fails. The default setting is ``false`` .

            You can initialize the Docker daemon during the install phase of your build by adding
            one of the following sets of commands to the install phase of your buildspec file:

            If the operating system's base image is Ubuntu Linux:

             ``- nohup /usr/local/bin/dockerd --host=unix:///var/run/docker.sock
             --host=tcp://0.0.0.0:2375 --storage-driver=overlay&``

             ``- timeout 15 sh -c "until docker info; do echo .; sleep 1; done"``

            If the operating system's base image is Alpine Linux and the previous command does not
            work, add the ``-t`` argument to ``timeout`` :

             ``- nohup /usr/local/bin/dockerd --host=unix:///var/run/docker.sock
             --host=tcp://0.0.0.0:2375 --storage-driver=overlay&``

             ``- timeout -t 15 sh -c "until docker info; do echo .; sleep 1; done"``

          - **certificate** *(string) --*

            The certificate to use with this build project.

          - **registryCredential** *(dict) --*

            The credentials for access to a private registry.

            - **credential** *(string) --* **[REQUIRED]**

              The Amazon Resource Name (ARN) or name of credentials created using AWS Secrets
              Manager.

              .. note::

                The ``credential`` can use the name of the credentials only if they exist in your
                current region.

            - **credentialProvider** *(string) --* **[REQUIRED]**

              The service that created the credentials to access a private Docker registry. The
              valid value, SECRETS_MANAGER, is for AWS Secrets Manager.

          - **imagePullCredentialsType** *(string) --*

            The type of credentials AWS CodeBuild uses to pull images in your build. There are two
            valid values:

            * ``CODEBUILD`` specifies that AWS CodeBuild uses its own credentials. This requires
            that you modify your ECR repository policy to trust AWS CodeBuild's service principal.

            * ``SERVICE_ROLE`` specifies that AWS CodeBuild uses your build project's service role.

            When you use a cross-account or private registry image, you must use SERVICE_ROLE
            credentials. When you use an AWS CodeBuild curated image, you must use CODEBUILD
            credentials.

        :type serviceRole: string
        :param serviceRole: **[REQUIRED]**

          The ARN of the AWS Identity and Access Management (IAM) role that enables AWS CodeBuild to
          interact with dependent AWS services on behalf of the AWS account.

        :type timeoutInMinutes: integer
        :param timeoutInMinutes:

          How long, in minutes, from 5 to 480 (8 hours), for AWS CodeBuild to wait before it times
          out any build that has not been marked as completed. The default is 60 minutes.

        :type queuedTimeoutInMinutes: integer
        :param queuedTimeoutInMinutes:

          The number of minutes a build is allowed to be queued before it times out.

        :type encryptionKey: string
        :param encryptionKey:

          The AWS Key Management Service (AWS KMS) customer master key (CMK) to be used for
          encrypting the build output artifacts.

          .. note::

            You can use a cross-account KMS key to encrypt the build output artifacts if your
            service role has permission to that key.

          You can specify either the Amazon Resource Name (ARN) of the CMK or, if available, the
          CMK's alias (using the format ``alias/*alias-name* `` ).

        :type tags: list
        :param tags:

          A set of tags for this build project.

          These tags are available for use by AWS services that support AWS CodeBuild build project
          tags.

          - *(dict) --*

            A tag, consisting of a key and a value.

            This tag is available for use by AWS services that support tags in AWS CodeBuild.

            - **key** *(string) --*

              The tag's key.

            - **value** *(string) --*

              The tag's value.

        :type vpcConfig: dict
        :param vpcConfig:

          VpcConfig enables AWS CodeBuild to access resources in an Amazon VPC.

          - **vpcId** *(string) --*

            The ID of the Amazon VPC.

          - **subnets** *(list) --*

            A list of one or more subnet IDs in your Amazon VPC.

            - *(string) --*

          - **securityGroupIds** *(list) --*

            A list of one or more security groups IDs in your Amazon VPC.

            - *(string) --*

        :type badgeEnabled: boolean
        :param badgeEnabled:

          Set this to true to generate a publicly accessible URL for your project's build badge.

        :type logsConfig: dict
        :param logsConfig:

          Information about logs for the build project. These can be logs in Amazon CloudWatch Logs,
          logs uploaded to a specified S3 bucket, or both.

          - **cloudWatchLogs** *(dict) --*

            Information about Amazon CloudWatch Logs for a build project. Amazon CloudWatch Logs are
            enabled by default.

            - **status** *(string) --* **[REQUIRED]**

              The current status of the logs in Amazon CloudWatch Logs for a build project. Valid
              values are:

              * ``ENABLED`` : Amazon CloudWatch Logs are enabled for this build project.

              * ``DISABLED`` : Amazon CloudWatch Logs are not enabled for this build project.

            - **groupName** *(string) --*

              The group name of the logs in Amazon CloudWatch Logs. For more information, see
              `Working with Log Groups and Log Streams
              <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html>`__
              .

            - **streamName** *(string) --*

              The prefix of the stream name of the Amazon CloudWatch Logs. For more information, see
              `Working with Log Groups and Log Streams
              <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html>`__
              .

          - **s3Logs** *(dict) --*

            Information about logs built to an S3 bucket for a build project. S3 logs are not
            enabled by default.

            - **status** *(string) --* **[REQUIRED]**

              The current status of the S3 build logs. Valid values are:

              * ``ENABLED`` : S3 build logs are enabled for this build project.

              * ``DISABLED`` : S3 build logs are not enabled for this build project.

            - **location** *(string) --*

              The ARN of an S3 bucket and the path prefix for S3 logs. If your Amazon S3 bucket name
              is ``my-bucket`` , and your path prefix is ``build-log`` , then acceptable formats are
              ``my-bucket/build-log`` or ``arn:aws:s3:::my-bucket/build-log`` .

            - **encryptionDisabled** *(boolean) --*

              Set to true if you do not want your S3 build log output encrypted. By default S3 build
              logs are encrypted.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'project': {
                    'name': 'string',
                    'arn': 'string',
                    'description': 'string',
                    'source': {
                        'type':
                        'CODECOMMIT'|'CODEPIPELINE'|'GITHUB'|'S3'|'BITBUCKET'
                        |'GITHUB_ENTERPRISE'|'NO_SOURCE',
                        'location': 'string',
                        'gitCloneDepth': 123,
                        'gitSubmodulesConfig': {
                            'fetchSubmodules': True|False
                        },
                        'buildspec': 'string',
                        'auth': {
                            'type': 'OAUTH',
                            'resource': 'string'
                        },
                        'reportBuildStatus': True|False,
                        'insecureSsl': True|False,
                        'sourceIdentifier': 'string'
                    },
                    'secondarySources': [
                        {
                            'type':
                            'CODECOMMIT'|'CODEPIPELINE'|'GITHUB'|'S3'
                            |'BITBUCKET'|'GITHUB_ENTERPRISE'|'NO_SOURCE',
                            'location': 'string',
                            'gitCloneDepth': 123,
                            'gitSubmodulesConfig': {
                                'fetchSubmodules': True|False
                            },
                            'buildspec': 'string',
                            'auth': {
                                'type': 'OAUTH',
                                'resource': 'string'
                            },
                            'reportBuildStatus': True|False,
                            'insecureSsl': True|False,
                            'sourceIdentifier': 'string'
                        },
                    ],
                    'sourceVersion': 'string',
                    'secondarySourceVersions': [
                        {
                            'sourceIdentifier': 'string',
                            'sourceVersion': 'string'
                        },
                    ],
                    'artifacts': {
                        'type': 'CODEPIPELINE'|'S3'|'NO_ARTIFACTS',
                        'location': 'string',
                        'path': 'string',
                        'namespaceType': 'NONE'|'BUILD_ID',
                        'name': 'string',
                        'packaging': 'NONE'|'ZIP',
                        'overrideArtifactName': True|False,
                        'encryptionDisabled': True|False,
                        'artifactIdentifier': 'string'
                    },
                    'secondaryArtifacts': [
                        {
                            'type': 'CODEPIPELINE'|'S3'|'NO_ARTIFACTS',
                            'location': 'string',
                            'path': 'string',
                            'namespaceType': 'NONE'|'BUILD_ID',
                            'name': 'string',
                            'packaging': 'NONE'|'ZIP',
                            'overrideArtifactName': True|False,
                            'encryptionDisabled': True|False,
                            'artifactIdentifier': 'string'
                        },
                    ],
                    'cache': {
                        'type': 'NO_CACHE'|'S3'|'LOCAL',
                        'location': 'string',
                        'modes': [
                            'LOCAL_DOCKER_LAYER_CACHE'|'LOCAL_SOURCE_CACHE'|'LOCAL_CUSTOM_CACHE',
                        ]
                    },
                    'environment': {
                        'type':
                        'WINDOWS_CONTAINER'|'LINUX_CONTAINER'|'LINUX_GPU_CONTAINER'
                        |'ARM_CONTAINER',
                        'image': 'string',
                        'computeType':
                        'BUILD_GENERAL1_SMALL'|'BUILD_GENERAL1_MEDIUM'
                        |'BUILD_GENERAL1_LARGE'|'BUILD_GENERAL1_2XLARGE',
                        'environmentVariables': [
                            {
                                'name': 'string',
                                'value': 'string',
                                'type': 'PLAINTEXT'|'PARAMETER_STORE'|'SECRETS_MANAGER'
                            },
                        ],
                        'privilegedMode': True|False,
                        'certificate': 'string',
                        'registryCredential': {
                            'credential': 'string',
                            'credentialProvider': 'SECRETS_MANAGER'
                        },
                        'imagePullCredentialsType': 'CODEBUILD'|'SERVICE_ROLE'
                    },
                    'serviceRole': 'string',
                    'timeoutInMinutes': 123,
                    'queuedTimeoutInMinutes': 123,
                    'encryptionKey': 'string',
                    'tags': [
                        {
                            'key': 'string',
                            'value': 'string'
                        },
                    ],
                    'created': datetime(2015, 1, 1),
                    'lastModified': datetime(2015, 1, 1),
                    'webhook': {
                        'url': 'string',
                        'payloadUrl': 'string',
                        'secret': 'string',
                        'branchFilter': 'string',
                        'filterGroups': [
                            [
                                {
                                    'type':
                                    'EVENT'|'BASE_REF'|'HEAD_REF'
                                    |'ACTOR_ACCOUNT_ID'|'FILE_PATH',
                                    'pattern': 'string',
                                    'excludeMatchedPattern': True|False
                                },
                            ],
                        ],
                        'lastModifiedSecret': datetime(2015, 1, 1)
                    },
                    'vpcConfig': {
                        'vpcId': 'string',
                        'subnets': [
                            'string',
                        ],
                        'securityGroupIds': [
                            'string',
                        ]
                    },
                    'badge': {
                        'badgeEnabled': True|False,
                        'badgeRequestUrl': 'string'
                    },
                    'logsConfig': {
                        'cloudWatchLogs': {
                            'status': 'ENABLED'|'DISABLED',
                            'groupName': 'string',
                            'streamName': 'string'
                        },
                        's3Logs': {
                            'status': 'ENABLED'|'DISABLED',
                            'location': 'string',
                            'encryptionDisabled': True|False
                        }
                    }
                }
            }
          **Response Structure**

          - *(dict) --*

            - **project** *(dict) --*

              Information about the build project that was created.

              - **name** *(string) --*

                The name of the build project.

              - **arn** *(string) --*

                The Amazon Resource Name (ARN) of the build project.

              - **description** *(string) --*

                A description that makes the build project easy to identify.

              - **source** *(dict) --*

                Information about the build input source code for this build project.

                - **type** *(string) --*

                  The type of repository that contains the source code to be built. Valid values
                  include:

                  * ``BITBUCKET`` : The source code is in a Bitbucket repository.

                  * ``CODECOMMIT`` : The source code is in an AWS CodeCommit repository.

                  * ``CODEPIPELINE`` : The source code settings are specified in the source action
                  of a pipeline in AWS CodePipeline.

                  * ``GITHUB`` : The source code is in a GitHub repository.

                  * ``GITHUB_ENTERPRISE`` : The source code is in a GitHub Enterprise repository.

                  * ``NO_SOURCE`` : The project does not have input source code.

                  * ``S3`` : The source code is in an Amazon Simple Storage Service (Amazon S3)
                  input bucket.

                - **location** *(string) --*

                  Information about the location of the source code to be built. Valid values
                  include:

                  * For source code settings that are specified in the source action of a pipeline
                  in AWS CodePipeline, ``location`` should not be specified. If it is specified, AWS
                  CodePipeline ignores it. This is because AWS CodePipeline uses the settings in a
                  pipeline's source action instead of this value.

                  * For source code in an AWS CodeCommit repository, the HTTPS clone URL to the
                  repository that contains the source code and the build spec (for example,
                  ``https://git-codecommit.*region-ID* .amazonaws.com/v1/repos/*repo-name* `` ).

                  * For source code in an Amazon Simple Storage Service (Amazon S3) input bucket,
                  one of the following.

                    * The path to the ZIP file that contains the source code (for example, ``
                    *bucket-name* /*path* /*to* /*object-name* .zip`` ).

                    * The path to the folder that contains the source code (for example, ``
                    *bucket-name* /*path* /*to* /*source-code* /*folder* /`` ).

                  * For source code in a GitHub repository, the HTTPS clone URL to the repository
                  that contains the source and the build spec. You must connect your AWS account to
                  your GitHub account. Use the AWS CodeBuild console to start creating a build
                  project. When you use the console to connect (or reconnect) with GitHub, on the
                  GitHub **Authorize application** page, for **Organization access** , choose
                  **Request access** next to each repository you want to allow AWS CodeBuild to have
                  access to, and then choose **Authorize application** . (After you have connected
                  to your GitHub account, you do not need to finish creating the build project. You
                  can leave the AWS CodeBuild console.) To instruct AWS CodeBuild to use this
                  connection, in the ``source`` object, set the ``auth`` object's ``type`` value to
                  ``OAUTH`` .

                  * For source code in a Bitbucket repository, the HTTPS clone URL to the repository
                  that contains the source and the build spec. You must connect your AWS account to
                  your Bitbucket account. Use the AWS CodeBuild console to start creating a build
                  project. When you use the console to connect (or reconnect) with Bitbucket, on the
                  Bitbucket **Confirm access to your account** page, choose **Grant access** .
                  (After you have connected to your Bitbucket account, you do not need to finish
                  creating the build project. You can leave the AWS CodeBuild console.) To instruct
                  AWS CodeBuild to use this connection, in the ``source`` object, set the ``auth``
                  object's ``type`` value to ``OAUTH`` .

                - **gitCloneDepth** *(integer) --*

                  Information about the Git clone depth for the build project.

                - **gitSubmodulesConfig** *(dict) --*

                  Information about the Git submodules configuration for the build project.

                  - **fetchSubmodules** *(boolean) --*

                    Set to true to fetch Git submodules for your AWS CodeBuild build project.

                - **buildspec** *(string) --*

                  The build spec declaration to use for the builds in this build project.

                  If this value is not specified, a build spec must be included along with the
                  source code to be built.

                - **auth** *(dict) --*

                  Information about the authorization settings for AWS CodeBuild to access the
                  source code to be built.

                  This information is for the AWS CodeBuild console's use only. Your code should not
                  get or set this information directly.

                  - **type** *(string) --*

                    .. note::

                      This data type is deprecated and is no longer accurate or used.

                    The authorization type to use. The only valid value is ``OAUTH`` , which
                    represents the OAuth authorization type.

                  - **resource** *(string) --*

                    The resource value that applies to the specified authorization type.

                - **reportBuildStatus** *(boolean) --*

                  Set to true to report the status of a build's start and finish to your source
                  provider. This option is valid only when your source provider is GitHub, GitHub
                  Enterprise, or Bitbucket. If this is set and you use a different source provider,
                  an invalidInputException is thrown.

                  .. note::

                    The status of a build triggered by a webhook is always reported to your source
                    provider.

                - **insecureSsl** *(boolean) --*

                  Enable this flag to ignore SSL warnings while connecting to the project source
                  code.

                - **sourceIdentifier** *(string) --*

                  An identifier for this project source.

              - **secondarySources** *(list) --*

                An array of ``ProjectSource`` objects.

                - *(dict) --*

                  Information about the build input source code for the build project.

                  - **type** *(string) --*

                    The type of repository that contains the source code to be built. Valid values
                    include:

                    * ``BITBUCKET`` : The source code is in a Bitbucket repository.

                    * ``CODECOMMIT`` : The source code is in an AWS CodeCommit repository.

                    * ``CODEPIPELINE`` : The source code settings are specified in the source action
                    of a pipeline in AWS CodePipeline.

                    * ``GITHUB`` : The source code is in a GitHub repository.

                    * ``GITHUB_ENTERPRISE`` : The source code is in a GitHub Enterprise repository.

                    * ``NO_SOURCE`` : The project does not have input source code.

                    * ``S3`` : The source code is in an Amazon Simple Storage Service (Amazon S3)
                    input bucket.

                  - **location** *(string) --*

                    Information about the location of the source code to be built. Valid values
                    include:

                    * For source code settings that are specified in the source action of a pipeline
                    in AWS CodePipeline, ``location`` should not be specified. If it is specified,
                    AWS CodePipeline ignores it. This is because AWS CodePipeline uses the settings
                    in a pipeline's source action instead of this value.

                    * For source code in an AWS CodeCommit repository, the HTTPS clone URL to the
                    repository that contains the source code and the build spec (for example,
                    ``https://git-codecommit.*region-ID* .amazonaws.com/v1/repos/*repo-name* `` ).

                    * For source code in an Amazon Simple Storage Service (Amazon S3) input bucket,
                    one of the following.

                      * The path to the ZIP file that contains the source code (for example, ``
                      *bucket-name* /*path* /*to* /*object-name* .zip`` ).

                      * The path to the folder that contains the source code (for example, ``
                      *bucket-name* /*path* /*to* /*source-code* /*folder* /`` ).

                    * For source code in a GitHub repository, the HTTPS clone URL to the repository
                    that contains the source and the build spec. You must connect your AWS account
                    to your GitHub account. Use the AWS CodeBuild console to start creating a build
                    project. When you use the console to connect (or reconnect) with GitHub, on the
                    GitHub **Authorize application** page, for **Organization access** , choose
                    **Request access** next to each repository you want to allow AWS CodeBuild to
                    have access to, and then choose **Authorize application** . (After you have
                    connected to your GitHub account, you do not need to finish creating the build
                    project. You can leave the AWS CodeBuild console.) To instruct AWS CodeBuild to
                    use this connection, in the ``source`` object, set the ``auth`` object's
                    ``type`` value to ``OAUTH`` .

                    * For source code in a Bitbucket repository, the HTTPS clone URL to the
                    repository that contains the source and the build spec. You must connect your
                    AWS account to your Bitbucket account. Use the AWS CodeBuild console to start
                    creating a build project. When you use the console to connect (or reconnect)
                    with Bitbucket, on the Bitbucket **Confirm access to your account** page, choose
                    **Grant access** . (After you have connected to your Bitbucket account, you do
                    not need to finish creating the build project. You can leave the AWS CodeBuild
                    console.) To instruct AWS CodeBuild to use this connection, in the ``source``
                    object, set the ``auth`` object's ``type`` value to ``OAUTH`` .

                  - **gitCloneDepth** *(integer) --*

                    Information about the Git clone depth for the build project.

                  - **gitSubmodulesConfig** *(dict) --*

                    Information about the Git submodules configuration for the build project.

                    - **fetchSubmodules** *(boolean) --*

                      Set to true to fetch Git submodules for your AWS CodeBuild build project.

                  - **buildspec** *(string) --*

                    The build spec declaration to use for the builds in this build project.

                    If this value is not specified, a build spec must be included along with the
                    source code to be built.

                  - **auth** *(dict) --*

                    Information about the authorization settings for AWS CodeBuild to access the
                    source code to be built.

                    This information is for the AWS CodeBuild console's use only. Your code should
                    not get or set this information directly.

                    - **type** *(string) --*

                      .. note::

                        This data type is deprecated and is no longer accurate or used.

                      The authorization type to use. The only valid value is ``OAUTH`` , which
                      represents the OAuth authorization type.

                    - **resource** *(string) --*

                      The resource value that applies to the specified authorization type.

                  - **reportBuildStatus** *(boolean) --*

                    Set to true to report the status of a build's start and finish to your source
                    provider. This option is valid only when your source provider is GitHub, GitHub
                    Enterprise, or Bitbucket. If this is set and you use a different source
                    provider, an invalidInputException is thrown.

                    .. note::

                      The status of a build triggered by a webhook is always reported to your source
                      provider.

                  - **insecureSsl** *(boolean) --*

                    Enable this flag to ignore SSL warnings while connecting to the project source
                    code.

                  - **sourceIdentifier** *(string) --*

                    An identifier for this project source.

              - **sourceVersion** *(string) --*

                A version of the build input to be built for this project. If not specified, the
                latest version is used. If specified, it must be one of:

                * For AWS CodeCommit: the commit ID, branch, or Git tag to use.

                * For GitHub: the commit ID, pull request ID, branch name, or tag name that
                corresponds to the version of the source code you want to build. If a pull request
                ID is specified, it must use the format ``pr/pull-request-ID`` (for example
                ``pr/25`` ). If a branch name is specified, the branch's HEAD commit ID is used. If
                not specified, the default branch's HEAD commit ID is used.

                * For Bitbucket: the commit ID, branch name, or tag name that corresponds to the
                version of the source code you want to build. If a branch name is specified, the
                branch's HEAD commit ID is used. If not specified, the default branch's HEAD commit
                ID is used.

                * For Amazon Simple Storage Service (Amazon S3): the version ID of the object that
                represents the build input ZIP file to use.

                If ``sourceVersion`` is specified at the build level, then that version takes
                precedence over this ``sourceVersion`` (at the project level).

                For more information, see `Source Version Sample with CodeBuild
                <https://docs.aws.amazon.com/codebuild/latest/userguide/sample-source-version.html>`__
                in the *AWS CodeBuild User Guide* .

              - **secondarySourceVersions** *(list) --*

                An array of ``ProjectSourceVersion`` objects. If ``secondarySourceVersions`` is
                specified at the build level, then they take over these ``secondarySourceVersions``
                (at the project level).

                - *(dict) --*

                  A source identifier and its corresponding version.

                  - **sourceIdentifier** *(string) --*

                    An identifier for a source in the build project.

                  - **sourceVersion** *(string) --*

                    The source version for the corresponding source identifier. If specified, must
                    be one of:

                    * For AWS CodeCommit: the commit ID, branch, or Git tag to use.

                    * For GitHub: the commit ID, pull request ID, branch name, or tag name that
                    corresponds to the version of the source code you want to build. If a pull
                    request ID is specified, it must use the format ``pr/pull-request-ID`` (for
                    example, ``pr/25`` ). If a branch name is specified, the branch's HEAD commit ID
                    is used. If not specified, the default branch's HEAD commit ID is used.

                    * For Bitbucket: the commit ID, branch name, or tag name that corresponds to the
                    version of the source code you want to build. If a branch name is specified, the
                    branch's HEAD commit ID is used. If not specified, the default branch's HEAD
                    commit ID is used.

                    * For Amazon Simple Storage Service (Amazon S3): the version ID of the object
                    that represents the build input ZIP file to use.

                    For more information, see `Source Version Sample with CodeBuild
                    <https://docs.aws.amazon.com/codebuild/latest/userguide/sample-source-version.html>`__
                    in the *AWS CodeBuild User Guide* .

              - **artifacts** *(dict) --*

                Information about the build output artifacts for the build project.

                - **type** *(string) --*

                  The type of build output artifact. Valid values include:

                  * ``CODEPIPELINE`` : The build project has build output generated through AWS
                  CodePipeline.

                  .. note::

                     The ``CODEPIPELINE`` type is not supported for ``secondaryArtifacts`` .

                  * ``NO_ARTIFACTS`` : The build project does not produce any build output.

                  * ``S3`` : The build project stores build output in Amazon Simple Storage Service
                  (Amazon S3).

                - **location** *(string) --*

                  Information about the build output artifact location:

                  * If ``type`` is set to ``CODEPIPELINE`` , AWS CodePipeline ignores this value if
                  specified. This is because AWS CodePipeline manages its build output locations
                  instead of AWS CodeBuild.

                  * If ``type`` is set to ``NO_ARTIFACTS`` , this value is ignored if specified,
                  because no build output is produced.

                  * If ``type`` is set to ``S3`` , this is the name of the output bucket.

                - **path** *(string) --*

                  Along with ``namespaceType`` and ``name`` , the pattern that AWS CodeBuild uses to
                  name and store the output artifact:

                  * If ``type`` is set to ``CODEPIPELINE`` , AWS CodePipeline ignores this value if
                  specified. This is because AWS CodePipeline manages its build output names instead
                  of AWS CodeBuild.

                  * If ``type`` is set to ``NO_ARTIFACTS`` , this value is ignored if specified,
                  because no build output is produced.

                  * If ``type`` is set to ``S3`` , this is the path to the output artifact. If
                  ``path`` is not specified, ``path`` is not used.

                  For example, if ``path`` is set to ``MyArtifacts`` , ``namespaceType`` is set to
                  ``NONE`` , and ``name`` is set to ``MyArtifact.zip`` , the output artifact is
                  stored in the output bucket at ``MyArtifacts/MyArtifact.zip`` .

                - **namespaceType** *(string) --*

                  Along with ``path`` and ``name`` , the pattern that AWS CodeBuild uses to
                  determine the name and location to store the output artifact:

                  * If ``type`` is set to ``CODEPIPELINE`` , AWS CodePipeline ignores this value if
                  specified. This is because AWS CodePipeline manages its build output names instead
                  of AWS CodeBuild.

                  * If ``type`` is set to ``NO_ARTIFACTS`` , this value is ignored if specified,
                  because no build output is produced.

                  * If ``type`` is set to ``S3`` , valid values include:

                    * ``BUILD_ID`` : Include the build ID in the location of the build output
                    artifact.

                    * ``NONE`` : Do not include the build ID. This is the default if
                    ``namespaceType`` is not specified.

                  For example, if ``path`` is set to ``MyArtifacts`` , ``namespaceType`` is set to
                  ``BUILD_ID`` , and ``name`` is set to ``MyArtifact.zip`` , the output artifact is
                  stored in ``MyArtifacts/*build-ID* /MyArtifact.zip`` .

                - **name** *(string) --*

                  Along with ``path`` and ``namespaceType`` , the pattern that AWS CodeBuild uses to
                  name and store the output artifact:

                  * If ``type`` is set to ``CODEPIPELINE`` , AWS CodePipeline ignores this value if
                  specified. This is because AWS CodePipeline manages its build output names instead
                  of AWS CodeBuild.

                  * If ``type`` is set to ``NO_ARTIFACTS`` , this value is ignored if specified,
                  because no build output is produced.

                  * If ``type`` is set to ``S3`` , this is the name of the output artifact object.
                  If you set the name to be a forward slash ("/"), the artifact is stored in the
                  root of the output bucket.

                  For example:

                  * If ``path`` is set to ``MyArtifacts`` , ``namespaceType`` is set to ``BUILD_ID``
                  , and ``name`` is set to ``MyArtifact.zip`` , then the output artifact is stored
                  in ``MyArtifacts/*build-ID* /MyArtifact.zip`` .

                  * If ``path`` is empty, ``namespaceType`` is set to ``NONE`` , and ``name`` is set
                  to "``/`` ", the output artifact is stored in the root of the output bucket.

                  * If ``path`` is set to ``MyArtifacts`` , ``namespaceType`` is set to ``BUILD_ID``
                  , and ``name`` is set to "``/`` ", the output artifact is stored in
                  ``MyArtifacts/*build-ID* `` .

                - **packaging** *(string) --*

                  The type of build output artifact to create:

                  * If ``type`` is set to ``CODEPIPELINE`` , AWS CodePipeline ignores this value if
                  specified. This is because AWS CodePipeline manages its build output artifacts
                  instead of AWS CodeBuild.

                  * If ``type`` is set to ``NO_ARTIFACTS`` , this value is ignored if specified,
                  because no build output is produced.

                  * If ``type`` is set to ``S3`` , valid values include:

                    * ``NONE`` : AWS CodeBuild creates in the output bucket a folder that contains
                    the build output. This is the default if ``packaging`` is not specified.

                    * ``ZIP`` : AWS CodeBuild creates in the output bucket a ZIP file that contains
                    the build output.

                - **overrideArtifactName** *(boolean) --*

                  If this flag is set, a name specified in the build spec file overrides the
                  artifact name. The name specified in a build spec file is calculated at build time
                  and uses the Shell Command Language. For example, you can append a date and time
                  to your artifact name so that it is always unique.

                - **encryptionDisabled** *(boolean) --*

                  Set to true if you do not want your output artifacts encrypted. This option is
                  valid only if your artifacts type is Amazon Simple Storage Service (Amazon S3). If
                  this is set with another artifacts type, an invalidInputException is thrown.

                - **artifactIdentifier** *(string) --*

                  An identifier for this artifact definition.

              - **secondaryArtifacts** *(list) --*

                An array of ``ProjectArtifacts`` objects.

                - *(dict) --*

                  Information about the build output artifacts for the build project.

                  - **type** *(string) --*

                    The type of build output artifact. Valid values include:

                    * ``CODEPIPELINE`` : The build project has build output generated through AWS
                    CodePipeline.

                    .. note::

                       The ``CODEPIPELINE`` type is not supported for ``secondaryArtifacts`` .

                    * ``NO_ARTIFACTS`` : The build project does not produce any build output.

                    * ``S3`` : The build project stores build output in Amazon Simple Storage
                    Service (Amazon S3).

                  - **location** *(string) --*

                    Information about the build output artifact location:

                    * If ``type`` is set to ``CODEPIPELINE`` , AWS CodePipeline ignores this value
                    if specified. This is because AWS CodePipeline manages its build output
                    locations instead of AWS CodeBuild.

                    * If ``type`` is set to ``NO_ARTIFACTS`` , this value is ignored if specified,
                    because no build output is produced.

                    * If ``type`` is set to ``S3`` , this is the name of the output bucket.

                  - **path** *(string) --*

                    Along with ``namespaceType`` and ``name`` , the pattern that AWS CodeBuild uses
                    to name and store the output artifact:

                    * If ``type`` is set to ``CODEPIPELINE`` , AWS CodePipeline ignores this value
                    if specified. This is because AWS CodePipeline manages its build output names
                    instead of AWS CodeBuild.

                    * If ``type`` is set to ``NO_ARTIFACTS`` , this value is ignored if specified,
                    because no build output is produced.

                    * If ``type`` is set to ``S3`` , this is the path to the output artifact. If
                    ``path`` is not specified, ``path`` is not used.

                    For example, if ``path`` is set to ``MyArtifacts`` , ``namespaceType`` is set to
                    ``NONE`` , and ``name`` is set to ``MyArtifact.zip`` , the output artifact is
                    stored in the output bucket at ``MyArtifacts/MyArtifact.zip`` .

                  - **namespaceType** *(string) --*

                    Along with ``path`` and ``name`` , the pattern that AWS CodeBuild uses to
                    determine the name and location to store the output artifact:

                    * If ``type`` is set to ``CODEPIPELINE`` , AWS CodePipeline ignores this value
                    if specified. This is because AWS CodePipeline manages its build output names
                    instead of AWS CodeBuild.

                    * If ``type`` is set to ``NO_ARTIFACTS`` , this value is ignored if specified,
                    because no build output is produced.

                    * If ``type`` is set to ``S3`` , valid values include:

                      * ``BUILD_ID`` : Include the build ID in the location of the build output
                      artifact.

                      * ``NONE`` : Do not include the build ID. This is the default if
                      ``namespaceType`` is not specified.

                    For example, if ``path`` is set to ``MyArtifacts`` , ``namespaceType`` is set to
                    ``BUILD_ID`` , and ``name`` is set to ``MyArtifact.zip`` , the output artifact
                    is stored in ``MyArtifacts/*build-ID* /MyArtifact.zip`` .

                  - **name** *(string) --*

                    Along with ``path`` and ``namespaceType`` , the pattern that AWS CodeBuild uses
                    to name and store the output artifact:

                    * If ``type`` is set to ``CODEPIPELINE`` , AWS CodePipeline ignores this value
                    if specified. This is because AWS CodePipeline manages its build output names
                    instead of AWS CodeBuild.

                    * If ``type`` is set to ``NO_ARTIFACTS`` , this value is ignored if specified,
                    because no build output is produced.

                    * If ``type`` is set to ``S3`` , this is the name of the output artifact object.
                    If you set the name to be a forward slash ("/"), the artifact is stored in the
                    root of the output bucket.

                    For example:

                    * If ``path`` is set to ``MyArtifacts`` , ``namespaceType`` is set to
                    ``BUILD_ID`` , and ``name`` is set to ``MyArtifact.zip`` , then the output
                    artifact is stored in ``MyArtifacts/*build-ID* /MyArtifact.zip`` .

                    * If ``path`` is empty, ``namespaceType`` is set to ``NONE`` , and ``name`` is
                    set to "``/`` ", the output artifact is stored in the root of the output bucket.

                    * If ``path`` is set to ``MyArtifacts`` , ``namespaceType`` is set to
                    ``BUILD_ID`` , and ``name`` is set to "``/`` ", the output artifact is stored in
                    ``MyArtifacts/*build-ID* `` .

                  - **packaging** *(string) --*

                    The type of build output artifact to create:

                    * If ``type`` is set to ``CODEPIPELINE`` , AWS CodePipeline ignores this value
                    if specified. This is because AWS CodePipeline manages its build output
                    artifacts instead of AWS CodeBuild.

                    * If ``type`` is set to ``NO_ARTIFACTS`` , this value is ignored if specified,
                    because no build output is produced.

                    * If ``type`` is set to ``S3`` , valid values include:

                      * ``NONE`` : AWS CodeBuild creates in the output bucket a folder that contains
                      the build output. This is the default if ``packaging`` is not specified.

                      * ``ZIP`` : AWS CodeBuild creates in the output bucket a ZIP file that
                      contains the build output.

                  - **overrideArtifactName** *(boolean) --*

                    If this flag is set, a name specified in the build spec file overrides the
                    artifact name. The name specified in a build spec file is calculated at build
                    time and uses the Shell Command Language. For example, you can append a date and
                    time to your artifact name so that it is always unique.

                  - **encryptionDisabled** *(boolean) --*

                    Set to true if you do not want your output artifacts encrypted. This option is
                    valid only if your artifacts type is Amazon Simple Storage Service (Amazon S3).
                    If this is set with another artifacts type, an invalidInputException is thrown.

                  - **artifactIdentifier** *(string) --*

                    An identifier for this artifact definition.

              - **cache** *(dict) --*

                Information about the cache for the build project.

                - **type** *(string) --*

                  The type of cache used by the build project. Valid values include:

                  * ``NO_CACHE`` : The build project does not use any cache.

                  * ``S3`` : The build project reads and writes from and to S3.

                  * ``LOCAL`` : The build project stores a cache locally on a build host that is
                  only available to that build host.

                - **location** *(string) --*

                  Information about the cache location:

                  * ``NO_CACHE`` or ``LOCAL`` : This value is ignored.

                  * ``S3`` : This is the S3 bucket name/prefix.

                - **modes** *(list) --*

                  If you use a ``LOCAL`` cache, the local cache mode. You can use one or more local
                  cache modes at the same time.

                  * ``LOCAL_SOURCE_CACHE`` mode caches Git metadata for primary and secondary
                  sources. After the cache is created, subsequent builds pull only the change
                  between commits. This mode is a good choice for projects with a clean working
                  directory and a source that is a large Git repository. If you choose this option
                  and your project does not use a Git repository (GitHub, GitHub Enterprise, or
                  Bitbucket), the option is ignored.

                  * ``LOCAL_DOCKER_LAYER_CACHE`` mode caches existing Docker layers. This mode is a
                  good choice for projects that build or pull large Docker images. It can prevent
                  the performance issues caused by pulling large Docker images down from the
                  network.

                  .. note::

                      * You can use a Docker layer cache in the Linux environment only.

                      * The ``privileged`` flag must be set so that your project has the required
                      Docker permissions.

                      * You should consider the security implications before you use a Docker layer
                      cache.

                  * ``LOCAL_CUSTOM_CACHE`` mode caches directories you specify in the buildspec
                  file. This mode is a good choice if your build scenario is not suited to one of
                  the other three local cache modes. If you use a custom cache:

                    * Only directories can be specified for caching. You cannot specify individual
                    files.

                    * Symlinks are used to reference cached directories.

                    * Cached directories are linked to your build before it downloads its project
                    sources. Cached items are overridden if a source item has the same name.
                    Directories are specified using cache paths in the buildspec file.

                  - *(string) --*

              - **environment** *(dict) --*

                Information about the build environment for this build project.

                - **type** *(string) --*

                  The type of build environment to use for related builds.

                  * The environment type ``ARM_CONTAINER`` is available only in regions US East (N.
                  Virginia), US East (Ohio), US West (Oregon), EU (Ireland), Asia Pacific (Mumbai),
                  Asia Pacific (Tokyo), Asia Pacific (Sydney), and EU (Frankfurt).

                  * The environment type ``LINUX_CONTAINER`` with compute type
                  ``build.general1.2xlarge`` is available only in regions US East (N. Virginia), US
                  East (N. Virginia), US West (Oregon), Canada (Central), EU (Ireland), EU (London),
                  EU (Frankfurt), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific
                  (Singapore), Asia Pacific (Sydney), China (Beijing), and China (Ningxia).

                  * The environment type ``LINUX_GPU_CONTAINER`` is available only in regions US
                  East (N. Virginia), US East (N. Virginia), US West (Oregon), Canada (Central), EU
                  (Ireland), EU (London), EU (Frankfurt), Asia Pacific (Tokyo), Asia Pacific
                  (Seoul), Asia Pacific (Singapore), Asia Pacific (Sydney) , China (Beijing), and
                  China (Ningxia).

                - **image** *(string) --*

                  The image tag or image digest that identifies the Docker image to use for this
                  build project. Use the following formats:

                  * For an image tag: ``registry/repository:tag`` . For example, to specify an image
                  with the tag "latest," use ``registry/repository:latest`` .

                  * For an image digest: ``registry/repository@digest`` . For example, to specify an
                  image with the digest
                  "sha256:cbbf2f9a99b47fc460d422812b6a5adff7dfee951d8fa2e4a98caa0382cfbdbf," use
                  ``registry/repository@sha256:cbbf2f9a99b47fc460d422812b6a5adff7dfee951d8fa2e4a98caa0382cfbdbf``
                  .

                - **computeType** *(string) --*

                  Information about the compute resources the build project uses. Available values
                  include:

                  * ``BUILD_GENERAL1_SMALL`` : Use up to 3 GB memory and 2 vCPUs for builds.

                  * ``BUILD_GENERAL1_MEDIUM`` : Use up to 7 GB memory and 4 vCPUs for builds.

                  * ``BUILD_GENERAL1_LARGE`` : Use up to 16 GB memory and 8 vCPUs for builds,
                  depending on your environment type.

                  * ``BUILD_GENERAL1_2XLARGE`` : Use up to 145 GB memory, 72 vCPUs, and 824 GB of
                  SSD storage for builds. This compute type supports Docker images up to 100 GB
                  uncompressed.

                  If you use ``BUILD_GENERAL1_LARGE`` :

                  * For environment type ``LINUX_CONTAINER`` , you can use up to 15 GB memory and 8
                  vCPUs for builds.

                  * For environment type ``LINUX_GPU_CONTAINER`` , you can use up to 255 GB memory,
                  32 vCPUs, and 4 NVIDIA Tesla V100 GPUs for builds.

                  * For environment type ``ARM_CONTAINER`` , you can use up to 16 GB memory and 8
                  vCPUs on ARM-based processors for builds.

                  For more information, see `Build Environment Compute Types
                  <https://docs.aws.amazon.com/codebuild/latest/userguide/build-env-ref-compute-types.html>`__
                  in the *AWS CodeBuild User Guide.*

                - **environmentVariables** *(list) --*

                  A set of environment variables to make available to builds for this build project.

                  - *(dict) --*

                    Information about an environment variable for a build project or a build.

                    - **name** *(string) --*

                      The name or key of the environment variable.

                    - **value** *(string) --*

                      The value of the environment variable.

                      .. warning::

                        We strongly discourage the use of environment variables to store sensitive
                        values, especially AWS secret key IDs and secret access keys. Environment
                        variables can be displayed in plain text using the AWS CodeBuild console and
                        the AWS Command Line Interface (AWS CLI).

                    - **type** *(string) --*

                      The type of environment variable. Valid values include:

                      * ``PARAMETER_STORE`` : An environment variable stored in Amazon EC2 Systems
                      Manager Parameter Store.

                      * ``PLAINTEXT`` : An environment variable in plain text format.

                      * ``SECRETS_MANAGER`` : An environment variable stored in AWS Secrets Manager.

                - **privilegedMode** *(boolean) --*

                  Enables running the Docker daemon inside a Docker container. Set to true only if
                  the build project is used to build Docker images. Otherwise, a build that attempts
                  to interact with the Docker daemon fails. The default setting is ``false`` .

                  You can initialize the Docker daemon during the install phase of your build by
                  adding one of the following sets of commands to the install phase of your
                  buildspec file:

                  If the operating system's base image is Ubuntu Linux:

                   ``- nohup /usr/local/bin/dockerd --host=unix:///var/run/docker.sock
                   --host=tcp://0.0.0.0:2375 --storage-driver=overlay&``

                   ``- timeout 15 sh -c "until docker info; do echo .; sleep 1; done"``

                  If the operating system's base image is Alpine Linux and the previous command does
                  not work, add the ``-t`` argument to ``timeout`` :

                   ``- nohup /usr/local/bin/dockerd --host=unix:///var/run/docker.sock
                   --host=tcp://0.0.0.0:2375 --storage-driver=overlay&``

                   ``- timeout -t 15 sh -c "until docker info; do echo .; sleep 1; done"``

                - **certificate** *(string) --*

                  The certificate to use with this build project.

                - **registryCredential** *(dict) --*

                  The credentials for access to a private registry.

                  - **credential** *(string) --*

                    The Amazon Resource Name (ARN) or name of credentials created using AWS Secrets
                    Manager.

                    .. note::

                      The ``credential`` can use the name of the credentials only if they exist in
                      your current region.

                  - **credentialProvider** *(string) --*

                    The service that created the credentials to access a private Docker registry.
                    The valid value, SECRETS_MANAGER, is for AWS Secrets Manager.

                - **imagePullCredentialsType** *(string) --*

                  The type of credentials AWS CodeBuild uses to pull images in your build. There are
                  two valid values:

                  * ``CODEBUILD`` specifies that AWS CodeBuild uses its own credentials. This
                  requires that you modify your ECR repository policy to trust AWS CodeBuild's
                  service principal.

                  * ``SERVICE_ROLE`` specifies that AWS CodeBuild uses your build project's service
                  role.

                  When you use a cross-account or private registry image, you must use SERVICE_ROLE
                  credentials. When you use an AWS CodeBuild curated image, you must use CODEBUILD
                  credentials.

              - **serviceRole** *(string) --*

                The ARN of the AWS Identity and Access Management (IAM) role that enables AWS
                CodeBuild to interact with dependent AWS services on behalf of the AWS account.

              - **timeoutInMinutes** *(integer) --*

                How long, in minutes, from 5 to 480 (8 hours), for AWS CodeBuild to wait before
                timing out any related build that did not get marked as completed. The default is 60
                minutes.

              - **queuedTimeoutInMinutes** *(integer) --*

                The number of minutes a build is allowed to be queued before it times out.

              - **encryptionKey** *(string) --*

                The AWS Key Management Service (AWS KMS) customer master key (CMK) to be used for
                encrypting the build output artifacts.

                .. note::

                  You can use a cross-account KMS key to encrypt the build output artifacts if your
                  service role has permission to that key.

                You can specify either the Amazon Resource Name (ARN) of the CMK or, if available,
                the CMK's alias (using the format ``alias/*alias-name* `` ).

              - **tags** *(list) --*

                The tags for this build project.

                These tags are available for use by AWS services that support AWS CodeBuild build
                project tags.

                - *(dict) --*

                  A tag, consisting of a key and a value.

                  This tag is available for use by AWS services that support tags in AWS CodeBuild.

                  - **key** *(string) --*

                    The tag's key.

                  - **value** *(string) --*

                    The tag's value.

              - **created** *(datetime) --*

                When the build project was created, expressed in Unix time format.

              - **lastModified** *(datetime) --*

                When the build project's settings were last modified, expressed in Unix time format.

              - **webhook** *(dict) --*

                Information about a webhook that connects repository events to a build project in
                AWS CodeBuild.

                - **url** *(string) --*

                  The URL to the webhook.

                - **payloadUrl** *(string) --*

                  The AWS CodeBuild endpoint where webhook events are sent.

                - **secret** *(string) --*

                  The secret token of the associated repository.

                  .. note::

                    A Bitbucket webhook does not support ``secret`` .

                - **branchFilter** *(string) --*

                  A regular expression used to determine which repository branches are built when a
                  webhook is triggered. If the name of a branch matches the regular expression, then
                  it is built. If ``branchFilter`` is empty, then all branches are built.

                  .. note::

                    It is recommended that you use ``filterGroups`` instead of ``branchFilter`` .

                - **filterGroups** *(list) --*

                  An array of arrays of ``WebhookFilter`` objects used to determine which webhooks
                  are triggered. At least one ``WebhookFilter`` in the array must specify ``EVENT``
                  as its ``type`` .

                  For a build to be triggered, at least one filter group in the ``filterGroups``
                  array must pass. For a filter group to pass, each of its filters must pass.

                  - *(list) --*

                    - *(dict) --*

                      A filter used to determine which webhooks trigger a build.

                      - **type** *(string) --*

                        The type of webhook filter. There are five webhook filter types: ``EVENT`` ,
                        ``ACTOR_ACCOUNT_ID`` , ``HEAD_REF`` , ``BASE_REF`` , and ``FILE_PATH`` .

                          EVENT

                        A webhook event triggers a build when the provided ``pattern`` matches one
                        of four event types: ``PUSH`` , ``PULL_REQUEST_CREATED`` ,
                        ``PULL_REQUEST_UPDATED`` , and ``PULL_REQUEST_REOPENED`` . The ``EVENT``
                        patterns are specified as a comma-separated string. For example, ``PUSH,
                        PULL_REQUEST_CREATED, PULL_REQUEST_UPDATED`` filters all push, pull request
                        created, and pull request updated events.

                        .. note::

                          The ``PULL_REQUEST_REOPENED`` works with GitHub and GitHub Enterprise
                          only.

                          ACTOR_ACCOUNT_ID

                        A webhook event triggers a build when a GitHub, GitHub Enterprise, or
                        Bitbucket account ID matches the regular expression ``pattern`` .

                          HEAD_REF

                        A webhook event triggers a build when the head reference matches the regular
                        expression ``pattern`` . For example, ``refs/heads/branch-name`` and
                        ``refs/tags/tag-name`` .

                        Works with GitHub and GitHub Enterprise push, GitHub and GitHub Enterprise
                        pull request, Bitbucket push, and Bitbucket pull request events.

                          BASE_REF

                        A webhook event triggers a build when the base reference matches the regular
                        expression ``pattern`` . For example, ``refs/heads/branch-name`` .

                        .. note::

                          Works with pull request events only.

                          FILE_PATH

                        A webhook triggers a build when the path of a changed file matches the
                        regular expression ``pattern`` .

                        .. note::

                          Works with GitHub and GitHub Enterprise push events only.

                      - **pattern** *(string) --*

                        For a ``WebHookFilter`` that uses ``EVENT`` type, a comma-separated string
                        that specifies one or more events. For example, the webhook filter ``PUSH,
                        PULL_REQUEST_CREATED, PULL_REQUEST_UPDATED`` allows all push, pull request
                        created, and pull request updated events to trigger a build.

                        For a ``WebHookFilter`` that uses any of the other filter types, a regular
                        expression pattern. For example, a ``WebHookFilter`` that uses ``HEAD_REF``
                        for its ``type`` and the pattern ``^refs/heads/`` triggers a build when the
                        head reference is a branch with a reference name ``refs/heads/branch-name``
                        .

                      - **excludeMatchedPattern** *(boolean) --*

                        Used to indicate that the ``pattern`` determines which webhook events do not
                        trigger a build. If true, then a webhook event that does not match the
                        ``pattern`` triggers a build. If false, then a webhook event that matches
                        the ``pattern`` triggers a build.

                - **lastModifiedSecret** *(datetime) --*

                  A timestamp that indicates the last time a repository's secret token was modified.

              - **vpcConfig** *(dict) --*

                Information about the VPC configuration that AWS CodeBuild accesses.

                - **vpcId** *(string) --*

                  The ID of the Amazon VPC.

                - **subnets** *(list) --*

                  A list of one or more subnet IDs in your Amazon VPC.

                  - *(string) --*

                - **securityGroupIds** *(list) --*

                  A list of one or more security groups IDs in your Amazon VPC.

                  - *(string) --*

              - **badge** *(dict) --*

                Information about the build badge for the build project.

                - **badgeEnabled** *(boolean) --*

                  Set this to true to generate a publicly accessible URL for your project's build
                  badge.

                - **badgeRequestUrl** *(string) --*

                  The publicly-accessible URL through which you can access the build badge for your
                  project.

                  The publicly accessible URL through which you can access the build badge for your
                  project.

              - **logsConfig** *(dict) --*

                Information about logs for the build project. A project can create logs in Amazon
                CloudWatch Logs, an S3 bucket, or both.

                - **cloudWatchLogs** *(dict) --*

                  Information about Amazon CloudWatch Logs for a build project. Amazon CloudWatch
                  Logs are enabled by default.

                  - **status** *(string) --*

                    The current status of the logs in Amazon CloudWatch Logs for a build project.
                    Valid values are:

                    * ``ENABLED`` : Amazon CloudWatch Logs are enabled for this build project.

                    * ``DISABLED`` : Amazon CloudWatch Logs are not enabled for this build project.

                  - **groupName** *(string) --*

                    The group name of the logs in Amazon CloudWatch Logs. For more information, see
                    `Working with Log Groups and Log Streams
                    <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html>`__
                    .

                  - **streamName** *(string) --*

                    The prefix of the stream name of the Amazon CloudWatch Logs. For more
                    information, see `Working with Log Groups and Log Streams
                    <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html>`__
                    .

                - **s3Logs** *(dict) --*

                  Information about logs built to an S3 bucket for a build project. S3 logs are not
                  enabled by default.

                  - **status** *(string) --*

                    The current status of the S3 build logs. Valid values are:

                    * ``ENABLED`` : S3 build logs are enabled for this build project.

                    * ``DISABLED`` : S3 build logs are not enabled for this build project.

                  - **location** *(string) --*

                    The ARN of an S3 bucket and the path prefix for S3 logs. If your Amazon S3
                    bucket name is ``my-bucket`` , and your path prefix is ``build-log`` , then
                    acceptable formats are ``my-bucket/build-log`` or
                    ``arn:aws:s3:::my-bucket/build-log`` .

                  - **encryptionDisabled** *(boolean) --*

                    Set to true if you do not want your S3 build log output encrypted. By default S3
                    build logs are encrypted.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_report_group(
        self, name: str, type: str, exportConfig: ClientCreateReportGroupExportConfigTypeDef
    ) -> ClientCreateReportGroupResponseTypeDef:
        """
        Creates a report group. A report group contains a collection of reports.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/codebuild-2016-10-06/CreateReportGroup>`_

        **Request Syntax**
        ::

          response = client.create_report_group(
              name='string',
              type='TEST',
              exportConfig={
                  'exportConfigType': 'S3'|'NO_EXPORT',
                  's3Destination': {
                      'bucket': 'string',
                      'path': 'string',
                      'packaging': 'ZIP'|'NONE',
                      'encryptionKey': 'string',
                      'encryptionDisabled': True|False
                  }
              }
          )
        :type name: string
        :param name: **[REQUIRED]**

          The name of the report group.

        :type type: string
        :param type: **[REQUIRED]**

          The type of report group.

        :type exportConfig: dict
        :param exportConfig: **[REQUIRED]**

          A ``ReportExportConfig`` object that contains information about where the report group
          test results are exported.

          - **exportConfigType** *(string) --*

            The export configuration type. Valid values are:

            * ``S3`` : The report results are exported to an S3 bucket.

            * ``NO_EXPORT`` : The report results are not exported.

          - **s3Destination** *(dict) --*

            A ``S3ReportExportConfig`` object that contains information about the S3 bucket where
            the run of a report is exported.

            - **bucket** *(string) --*

              The name of the S3 bucket where the raw data of a report are exported.

            - **path** *(string) --*

              The path to the exported report's raw data results.

            - **packaging** *(string) --*

              The type of build output artifact to create. Valid values include:

              * ``NONE`` : AWS CodeBuild creates the raw data in the output bucket. This is the
              default if packaging is not specified.

              * ``ZIP`` : AWS CodeBuild creates a ZIP file with the raw data in the output bucket.

            - **encryptionKey** *(string) --*

              The encryption key for the report's encrypted raw data.

            - **encryptionDisabled** *(boolean) --*

              A boolean value that specifies if the results of a report are encrypted.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'reportGroup': {
                    'arn': 'string',
                    'name': 'string',
                    'type': 'TEST',
                    'exportConfig': {
                        'exportConfigType': 'S3'|'NO_EXPORT',
                        's3Destination': {
                            'bucket': 'string',
                            'path': 'string',
                            'packaging': 'ZIP'|'NONE',
                            'encryptionKey': 'string',
                            'encryptionDisabled': True|False
                        }
                    },
                    'created': datetime(2015, 1, 1),
                    'lastModified': datetime(2015, 1, 1)
                }
            }
          **Response Structure**

          - *(dict) --*

            - **reportGroup** *(dict) --*

              Information about the report group that was created.

              - **arn** *(string) --*

                The ARN of a ``ReportGroup`` .

              - **name** *(string) --*

                The name of a ``ReportGroup`` .

              - **type** *(string) --*

                The type of the ``ReportGroup`` . The one valid value is ``TEST`` .

              - **exportConfig** *(dict) --*

                Information about the destination where the raw data of this ``ReportGroup`` is
                exported.

                - **exportConfigType** *(string) --*

                  The export configuration type. Valid values are:

                  * ``S3`` : The report results are exported to an S3 bucket.

                  * ``NO_EXPORT`` : The report results are not exported.

                - **s3Destination** *(dict) --*

                  A ``S3ReportExportConfig`` object that contains information about the S3 bucket
                  where the run of a report is exported.

                  - **bucket** *(string) --*

                    The name of the S3 bucket where the raw data of a report are exported.

                  - **path** *(string) --*

                    The path to the exported report's raw data results.

                  - **packaging** *(string) --*

                    The type of build output artifact to create. Valid values include:

                    * ``NONE`` : AWS CodeBuild creates the raw data in the output bucket. This is
                    the default if packaging is not specified.

                    * ``ZIP`` : AWS CodeBuild creates a ZIP file with the raw data in the output
                    bucket.

                  - **encryptionKey** *(string) --*

                    The encryption key for the report's encrypted raw data.

                  - **encryptionDisabled** *(boolean) --*

                    A boolean value that specifies if the results of a report are encrypted.

              - **created** *(datetime) --*

                The date and time this ``ReportGroup`` was created.

              - **lastModified** *(datetime) --*

                The date and time this ``ReportGroup`` was last modified.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_webhook(
        self,
        projectName: str,
        branchFilter: str = None,
        filterGroups: List[List[ClientCreateWebhookFilterGroupsTypeDef]] = None,
    ) -> ClientCreateWebhookResponseTypeDef:
        """
        For an existing AWS CodeBuild build project that has its source code stored in a GitHub or
        Bitbucket repository, enables AWS CodeBuild to start rebuilding the source code every time a
        code change is pushed to the repository.

        .. warning::

          If you enable webhooks for an AWS CodeBuild project, and the project is used as a build
          step in AWS CodePipeline, then two identical builds are created for each commit. One build
          is triggered through webhooks, and one through AWS CodePipeline. Because billing is on a
          per-build basis, you are billed for both builds. Therefore, if you are using AWS
          CodePipeline, we recommend that you disable webhooks in AWS CodeBuild. In the AWS
          CodeBuild console, clear the Webhook box. For more information, see step 5 in `Change a
          Build Project's Settings
          <https://docs.aws.amazon.com/codebuild/latest/userguide/change-project.html#change-project-console>`__
          .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/codebuild-2016-10-06/CreateWebhook>`_

        **Request Syntax**
        ::

          response = client.create_webhook(
              projectName='string',
              branchFilter='string',
              filterGroups=[
                  [
                      {
                          'type': 'EVENT'|'BASE_REF'|'HEAD_REF'|'ACTOR_ACCOUNT_ID'|'FILE_PATH',
                          'pattern': 'string',
                          'excludeMatchedPattern': True|False
                      },
                  ],
              ]
          )
        :type projectName: string
        :param projectName: **[REQUIRED]**

          The name of the AWS CodeBuild project.

        :type branchFilter: string
        :param branchFilter:

          A regular expression used to determine which repository branches are built when a webhook
          is triggered. If the name of a branch matches the regular expression, then it is built. If
          ``branchFilter`` is empty, then all branches are built.

          .. note::

            It is recommended that you use ``filterGroups`` instead of ``branchFilter`` .

        :type filterGroups: list
        :param filterGroups:

          An array of arrays of ``WebhookFilter`` objects used to determine which webhooks are
          triggered. At least one ``WebhookFilter`` in the array must specify ``EVENT`` as its
          ``type`` .

          For a build to be triggered, at least one filter group in the ``filterGroups`` array must
          pass. For a filter group to pass, each of its filters must pass.

          - *(list) --*

            - *(dict) --*

              A filter used to determine which webhooks trigger a build.

              - **type** *(string) --* **[REQUIRED]**

                The type of webhook filter. There are five webhook filter types: ``EVENT`` ,
                ``ACTOR_ACCOUNT_ID`` , ``HEAD_REF`` , ``BASE_REF`` , and ``FILE_PATH`` .

                  EVENT

                A webhook event triggers a build when the provided ``pattern`` matches one of four
                event types: ``PUSH`` , ``PULL_REQUEST_CREATED`` , ``PULL_REQUEST_UPDATED`` , and
                ``PULL_REQUEST_REOPENED`` . The ``EVENT`` patterns are specified as a
                comma-separated string. For example, ``PUSH, PULL_REQUEST_CREATED,
                PULL_REQUEST_UPDATED`` filters all push, pull request created, and pull request
                updated events.

                .. note::

                  The ``PULL_REQUEST_REOPENED`` works with GitHub and GitHub Enterprise only.

                  ACTOR_ACCOUNT_ID

                A webhook event triggers a build when a GitHub, GitHub Enterprise, or Bitbucket
                account ID matches the regular expression ``pattern`` .

                  HEAD_REF

                A webhook event triggers a build when the head reference matches the regular
                expression ``pattern`` . For example, ``refs/heads/branch-name`` and
                ``refs/tags/tag-name`` .

                Works with GitHub and GitHub Enterprise push, GitHub and GitHub Enterprise pull
                request, Bitbucket push, and Bitbucket pull request events.

                  BASE_REF

                A webhook event triggers a build when the base reference matches the regular
                expression ``pattern`` . For example, ``refs/heads/branch-name`` .

                .. note::

                  Works with pull request events only.

                  FILE_PATH

                A webhook triggers a build when the path of a changed file matches the regular
                expression ``pattern`` .

                .. note::

                  Works with GitHub and GitHub Enterprise push events only.

              - **pattern** *(string) --* **[REQUIRED]**

                For a ``WebHookFilter`` that uses ``EVENT`` type, a comma-separated string that
                specifies one or more events. For example, the webhook filter ``PUSH,
                PULL_REQUEST_CREATED, PULL_REQUEST_UPDATED`` allows all push, pull request created,
                and pull request updated events to trigger a build.

                For a ``WebHookFilter`` that uses any of the other filter types, a regular
                expression pattern. For example, a ``WebHookFilter`` that uses ``HEAD_REF`` for its
                ``type`` and the pattern ``^refs/heads/`` triggers a build when the head reference
                is a branch with a reference name ``refs/heads/branch-name`` .

              - **excludeMatchedPattern** *(boolean) --*

                Used to indicate that the ``pattern`` determines which webhook events do not trigger
                a build. If true, then a webhook event that does not match the ``pattern`` triggers
                a build. If false, then a webhook event that matches the ``pattern`` triggers a
                build.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'webhook': {
                    'url': 'string',
                    'payloadUrl': 'string',
                    'secret': 'string',
                    'branchFilter': 'string',
                    'filterGroups': [
                        [
                            {
                                'type':
                                'EVENT'|'BASE_REF'|'HEAD_REF'
                                |'ACTOR_ACCOUNT_ID'|'FILE_PATH',
                                'pattern': 'string',
                                'excludeMatchedPattern': True|False
                            },
                        ],
                    ],
                    'lastModifiedSecret': datetime(2015, 1, 1)
                }
            }
          **Response Structure**

          - *(dict) --*

            - **webhook** *(dict) --*

              Information about a webhook that connects repository events to a build project in AWS
              CodeBuild.

              - **url** *(string) --*

                The URL to the webhook.

              - **payloadUrl** *(string) --*

                The AWS CodeBuild endpoint where webhook events are sent.

              - **secret** *(string) --*

                The secret token of the associated repository.

                .. note::

                  A Bitbucket webhook does not support ``secret`` .

              - **branchFilter** *(string) --*

                A regular expression used to determine which repository branches are built when a
                webhook is triggered. If the name of a branch matches the regular expression, then
                it is built. If ``branchFilter`` is empty, then all branches are built.

                .. note::

                  It is recommended that you use ``filterGroups`` instead of ``branchFilter`` .

              - **filterGroups** *(list) --*

                An array of arrays of ``WebhookFilter`` objects used to determine which webhooks are
                triggered. At least one ``WebhookFilter`` in the array must specify ``EVENT`` as its
                ``type`` .

                For a build to be triggered, at least one filter group in the ``filterGroups`` array
                must pass. For a filter group to pass, each of its filters must pass.

                - *(list) --*

                  - *(dict) --*

                    A filter used to determine which webhooks trigger a build.

                    - **type** *(string) --*

                      The type of webhook filter. There are five webhook filter types: ``EVENT`` ,
                      ``ACTOR_ACCOUNT_ID`` , ``HEAD_REF`` , ``BASE_REF`` , and ``FILE_PATH`` .

                        EVENT

                      A webhook event triggers a build when the provided ``pattern`` matches one of
                      four event types: ``PUSH`` , ``PULL_REQUEST_CREATED`` ,
                      ``PULL_REQUEST_UPDATED`` , and ``PULL_REQUEST_REOPENED`` . The ``EVENT``
                      patterns are specified as a comma-separated string. For example, ``PUSH,
                      PULL_REQUEST_CREATED, PULL_REQUEST_UPDATED`` filters all push, pull request
                      created, and pull request updated events.

                      .. note::

                        The ``PULL_REQUEST_REOPENED`` works with GitHub and GitHub Enterprise only.

                        ACTOR_ACCOUNT_ID

                      A webhook event triggers a build when a GitHub, GitHub Enterprise, or
                      Bitbucket account ID matches the regular expression ``pattern`` .

                        HEAD_REF

                      A webhook event triggers a build when the head reference matches the regular
                      expression ``pattern`` . For example, ``refs/heads/branch-name`` and
                      ``refs/tags/tag-name`` .

                      Works with GitHub and GitHub Enterprise push, GitHub and GitHub Enterprise
                      pull request, Bitbucket push, and Bitbucket pull request events.

                        BASE_REF

                      A webhook event triggers a build when the base reference matches the regular
                      expression ``pattern`` . For example, ``refs/heads/branch-name`` .

                      .. note::

                        Works with pull request events only.

                        FILE_PATH

                      A webhook triggers a build when the path of a changed file matches the regular
                      expression ``pattern`` .

                      .. note::

                        Works with GitHub and GitHub Enterprise push events only.

                    - **pattern** *(string) --*

                      For a ``WebHookFilter`` that uses ``EVENT`` type, a comma-separated string
                      that specifies one or more events. For example, the webhook filter ``PUSH,
                      PULL_REQUEST_CREATED, PULL_REQUEST_UPDATED`` allows all push, pull request
                      created, and pull request updated events to trigger a build.

                      For a ``WebHookFilter`` that uses any of the other filter types, a regular
                      expression pattern. For example, a ``WebHookFilter`` that uses ``HEAD_REF``
                      for its ``type`` and the pattern ``^refs/heads/`` triggers a build when the
                      head reference is a branch with a reference name ``refs/heads/branch-name`` .

                    - **excludeMatchedPattern** *(boolean) --*

                      Used to indicate that the ``pattern`` determines which webhook events do not
                      trigger a build. If true, then a webhook event that does not match the
                      ``pattern`` triggers a build. If false, then a webhook event that matches the
                      ``pattern`` triggers a build.

              - **lastModifiedSecret** *(datetime) --*

                A timestamp that indicates the last time a repository's secret token was modified.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_project(self, name: str) -> Dict[str, Any]:
        """
        Deletes a build project. When you delete a project, its builds are not deleted.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/codebuild-2016-10-06/DeleteProject>`_

        **Request Syntax**
        ::

          response = client.delete_project(
              name='string'
          )
        :type name: string
        :param name: **[REQUIRED]**

          The name of the build project.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {}
          **Response Structure**

          - *(dict) --*
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_report(self, arn: str) -> Dict[str, Any]:
        """
        Deletes a report.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/codebuild-2016-10-06/DeleteReport>`_

        **Request Syntax**
        ::

          response = client.delete_report(
              arn='string'
          )
        :type arn: string
        :param arn: **[REQUIRED]**

          The ARN of the report to delete.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {}
          **Response Structure**

          - *(dict) --*
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_report_group(self, arn: str) -> Dict[str, Any]:
        """
         ``DeleteReportGroup`` : Deletes a report group. Before you delete a report group, you must
         delete its reports. Use `ListReportsForReportGroup
         <https://docs.aws.amazon.com/codebuild/latest/APIReference/API_ListReportsForReportGroup.html>`__
         to get the reports in a report group. Use `DeleteReport
         <https://docs.aws.amazon.com/codebuild/latest/APIReference/API_DeleteReport.html>`__ to
         delete the reports. If you call ``DeleteReportGroup`` for a report group that contains one
         or more reports, an exception is thrown.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/codebuild-2016-10-06/DeleteReportGroup>`_

        **Request Syntax**
        ::

          response = client.delete_report_group(
              arn='string'
          )
        :type arn: string
        :param arn: **[REQUIRED]**

          The ARN of the report group to delete.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {}
          **Response Structure**

          - *(dict) --*
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_source_credentials(self, arn: str) -> ClientDeleteSourceCredentialsResponseTypeDef:
        """
        Deletes a set of GitHub, GitHub Enterprise, or Bitbucket source credentials.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/codebuild-2016-10-06/DeleteSourceCredentials>`_

        **Request Syntax**
        ::

          response = client.delete_source_credentials(
              arn='string'
          )
        :type arn: string
        :param arn: **[REQUIRED]**

          The Amazon Resource Name (ARN) of the token.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'arn': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **arn** *(string) --*

              The Amazon Resource Name (ARN) of the token.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_webhook(self, projectName: str) -> Dict[str, Any]:
        """
        For an existing AWS CodeBuild build project that has its source code stored in a GitHub or
        Bitbucket repository, stops AWS CodeBuild from rebuilding the source code every time a code
        change is pushed to the repository.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/codebuild-2016-10-06/DeleteWebhook>`_

        **Request Syntax**
        ::

          response = client.delete_webhook(
              projectName='string'
          )
        :type projectName: string
        :param projectName: **[REQUIRED]**

          The name of the AWS CodeBuild project.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {}
          **Response Structure**

          - *(dict) --*
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_test_cases(
        self,
        reportArn: str,
        nextToken: str = None,
        maxResults: int = None,
        filter: ClientDescribeTestCasesFilterTypeDef = None,
    ) -> ClientDescribeTestCasesResponseTypeDef:
        """
        Returns a list of details about test cases for a report.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/codebuild-2016-10-06/DescribeTestCases>`_

        **Request Syntax**
        ::

          response = client.describe_test_cases(
              reportArn='string',
              nextToken='string',
              maxResults=123,
              filter={
                  'status': 'string'
              }
          )
        :type reportArn: string
        :param reportArn: **[REQUIRED]**

          The ARN of the report for which test cases are returned.

        :type nextToken: string
        :param nextToken:

          During a previous call, the maximum number of items that can be returned is the value
          specified in ``maxResults`` . If there more items in the list, then a unique string called
          a *nextToken* is returned. To get the next batch of items in the list, call this operation
          again, adding the next token to the call. To get all of the items in the list, keep
          calling this operation with each subsequent next token that is returned, until no more
          next tokens are returned.

        :type maxResults: integer
        :param maxResults:

          The maximum number of paginated test cases returned per response. Use ``nextToken`` to
          iterate pages in the list of returned ``TestCase`` objects. The default value is 100.

        :type filter: dict
        :param filter:

          A ``TestCaseFilter`` object used to filter the returned reports.

          - **status** *(string) --*

            The status used to filter test cases. Valid statuses are ``SUCCEEDED`` , ``FAILED`` ,
            ``ERROR`` , ``SKIPPED`` , and ``UNKNOWN`` . A ``TestCaseFilter`` can have one status.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'nextToken': 'string',
                'testCases': [
                    {
                        'reportArn': 'string',
                        'testRawDataPath': 'string',
                        'prefix': 'string',
                        'name': 'string',
                        'status': 'string',
                        'durationInNanoSeconds': 123,
                        'message': 'string',
                        'expired': datetime(2015, 1, 1)
                    },
                ]
            }
          **Response Structure**

          - *(dict) --*

            - **nextToken** *(string) --*

              During a previous call, the maximum number of items that can be returned is the value
              specified in ``maxResults`` . If there more items in the list, then a unique string
              called a *nextToken* is returned. To get the next batch of items in the list, call
              this operation again, adding the next token to the call. To get all of the items in
              the list, keep calling this operation with each subsequent next token that is
              returned, until no more next tokens are returned.

            - **testCases** *(list) --*

              The returned list of test cases.

              - *(dict) --*

                Information about a test case created using a framework such as NUnit or Cucumber. A
                test case might be a unit test or a configuration test.

                - **reportArn** *(string) --*

                  The ARN of the report to which the test case belongs.

                - **testRawDataPath** *(string) --*

                  The path to the raw data file that contains the test result.

                - **prefix** *(string) --*

                  A string that is applied to a series of related test cases. CodeBuild generates
                  the prefix. The prefix depends on the framework used to generate the tests.

                - **name** *(string) --*

                  The name of the test case.

                - **status** *(string) --*

                  The status returned by the test case after it was run. Valid statuses are
                  ``SUCCEEDED`` , ``FAILED`` , ``ERROR`` , ``SKIPPED`` , and ``UNKNOWN`` .

                - **durationInNanoSeconds** *(integer) --*

                  The number of nanoseconds it took to run this test case.

                - **message** *(string) --*

                  A message associated with a test case. For example, an error message or stack
                  trace.

                - **expired** *(datetime) --*

                  The date and time a test case expires. A test case expires 30 days after it is
                  created. An expired test case is not available to view in CodeBuild.
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
    def import_source_credentials(
        self,
        token: str,
        serverType: Literal["GITHUB", "BITBUCKET", "GITHUB_ENTERPRISE"],
        authType: Literal["OAUTH", "BASIC_AUTH", "PERSONAL_ACCESS_TOKEN"],
        username: str = None,
        shouldOverwrite: bool = None,
    ) -> ClientImportSourceCredentialsResponseTypeDef:
        """
        Imports the source repository credentials for an AWS CodeBuild project that has its source
        code stored in a GitHub, GitHub Enterprise, or Bitbucket repository.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/codebuild-2016-10-06/ImportSourceCredentials>`_

        **Request Syntax**
        ::

          response = client.import_source_credentials(
              username='string',
              token='string',
              serverType='GITHUB'|'BITBUCKET'|'GITHUB_ENTERPRISE',
              authType='OAUTH'|'BASIC_AUTH'|'PERSONAL_ACCESS_TOKEN',
              shouldOverwrite=True|False
          )
        :type username: string
        :param username:

          The Bitbucket username when the ``authType`` is BASIC_AUTH. This parameter is not valid
          for other types of source providers or connections.

        :type token: string
        :param token: **[REQUIRED]**

          For GitHub or GitHub Enterprise, this is the personal access token. For Bitbucket, this is
          the app password.

        :type serverType: string
        :param serverType: **[REQUIRED]**

          The source provider used for this project.

        :type authType: string
        :param authType: **[REQUIRED]**

          The type of authentication used to connect to a GitHub, GitHub Enterprise, or Bitbucket
          repository. An OAUTH connection is not supported by the API and must be created using the
          AWS CodeBuild console.

        :type shouldOverwrite: boolean
        :param shouldOverwrite:

          Set to ``false`` to prevent overwriting the repository source credentials. Set to ``true``
          to overwrite the repository source credentials. The default value is ``true`` .

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'arn': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **arn** *(string) --*

              The Amazon Resource Name (ARN) of the token.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def invalidate_project_cache(self, projectName: str) -> Dict[str, Any]:
        """
        Resets the cache for a project.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/codebuild-2016-10-06/InvalidateProjectCache>`_

        **Request Syntax**
        ::

          response = client.invalidate_project_cache(
              projectName='string'
          )
        :type projectName: string
        :param projectName: **[REQUIRED]**

          The name of the AWS CodeBuild build project that the cache is reset for.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {}
          **Response Structure**

          - *(dict) --*
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_builds(
        self, sortOrder: Literal["ASCENDING", "DESCENDING"] = None, nextToken: str = None
    ) -> ClientListBuildsResponseTypeDef:
        """
        Gets a list of build IDs, with each build ID representing a single build.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/codebuild-2016-10-06/ListBuilds>`_

        **Request Syntax**
        ::

          response = client.list_builds(
              sortOrder='ASCENDING'|'DESCENDING',
              nextToken='string'
          )
        :type sortOrder: string
        :param sortOrder:

          The order to list build IDs. Valid values include:

          * ``ASCENDING`` : List the build IDs in ascending order by build ID.

          * ``DESCENDING`` : List the build IDs in descending order by build ID.

        :type nextToken: string
        :param nextToken:

          During a previous call, if there are more than 100 items in the list, only the first 100
          items are returned, along with a unique string called a *nextToken* . To get the next
          batch of items in the list, call this operation again, adding the next token to the call.
          To get all of the items in the list, keep calling this operation with each subsequent next
          token that is returned, until no more next tokens are returned.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'ids': [
                    'string',
                ],
                'nextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **ids** *(list) --*

              A list of build IDs, with each build ID representing a single build.

              - *(string) --*

            - **nextToken** *(string) --*

              If there are more than 100 items in the list, only the first 100 items are returned,
              along with a unique string called a *nextToken* . To get the next batch of items in
              the list, call this operation again, adding the next token to the call.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_builds_for_project(
        self,
        projectName: str,
        sortOrder: Literal["ASCENDING", "DESCENDING"] = None,
        nextToken: str = None,
    ) -> ClientListBuildsForProjectResponseTypeDef:
        """
        Gets a list of build IDs for the specified build project, with each build ID representing a
        single build.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/codebuild-2016-10-06/ListBuildsForProject>`_

        **Request Syntax**
        ::

          response = client.list_builds_for_project(
              projectName='string',
              sortOrder='ASCENDING'|'DESCENDING',
              nextToken='string'
          )
        :type projectName: string
        :param projectName: **[REQUIRED]**

          The name of the AWS CodeBuild project.

        :type sortOrder: string
        :param sortOrder:

          The order to list build IDs. Valid values include:

          * ``ASCENDING`` : List the build IDs in ascending order by build ID.

          * ``DESCENDING`` : List the build IDs in descending order by build ID.

        :type nextToken: string
        :param nextToken:

          During a previous call, if there are more than 100 items in the list, only the first 100
          items are returned, along with a unique string called a *nextToken* . To get the next
          batch of items in the list, call this operation again, adding the next token to the call.
          To get all of the items in the list, keep calling this operation with each subsequent next
          token that is returned, until no more next tokens are returned.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'ids': [
                    'string',
                ],
                'nextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **ids** *(list) --*

              A list of build IDs for the specified build project, with each build ID representing a
              single build.

              - *(string) --*

            - **nextToken** *(string) --*

              If there are more than 100 items in the list, only the first 100 items are returned,
              along with a unique string called a *nextToken* . To get the next batch of items in
              the list, call this operation again, adding the next token to the call.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_curated_environment_images(
        self, *args: Any, **kwargs: Any
    ) -> ClientListCuratedEnvironmentImagesResponseTypeDef:
        """
        Gets information about Docker images that are managed by AWS CodeBuild.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/codebuild-2016-10-06/ListCuratedEnvironmentImages>`_

        **Request Syntax**
        ::

          response = client.list_curated_environment_images()

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'platforms': [
                    {
                        'platform': 'DEBIAN'|'AMAZON_LINUX'|'UBUNTU'|'WINDOWS_SERVER',
                        'languages': [
                            {
                                'language':
                                'JAVA'|'PYTHON'|'NODE_JS'|'RUBY'|'GOLANG'
                                |'DOCKER'|'ANDROID'|'DOTNET'|'BASE'|'PHP',
                                'images': [
                                    {
                                        'name': 'string',
                                        'description': 'string',
                                        'versions': [
                                            'string',
                                        ]
                                    },
                                ]
                            },
                        ]
                    },
                ]
            }
          **Response Structure**

          - *(dict) --*

            - **platforms** *(list) --*

              Information about supported platforms for Docker images that are managed by AWS
              CodeBuild.

              - *(dict) --*

                A set of Docker images that are related by platform and are managed by AWS
                CodeBuild.

                - **platform** *(string) --*

                  The platform's name.

                - **languages** *(list) --*

                  The list of programming languages that are available for the specified platform.

                  - *(dict) --*

                    A set of Docker images that are related by programming language and are managed
                    by AWS CodeBuild.

                    - **language** *(string) --*

                      The programming language for the Docker images.

                    - **images** *(list) --*

                      The list of Docker images that are related by the specified programming
                      language.

                      - *(dict) --*

                        Information about a Docker image that is managed by AWS CodeBuild.

                        - **name** *(string) --*

                          The name of the Docker image.

                        - **description** *(string) --*

                          The description of the Docker image.

                        - **versions** *(list) --*

                          A list of environment image versions.

                          - *(string) --*
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_projects(
        self,
        sortBy: Literal["NAME", "CREATED_TIME", "LAST_MODIFIED_TIME"] = None,
        sortOrder: Literal["ASCENDING", "DESCENDING"] = None,
        nextToken: str = None,
    ) -> ClientListProjectsResponseTypeDef:
        """
        Gets a list of build project names, with each build project name representing a single build
        project.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/codebuild-2016-10-06/ListProjects>`_

        **Request Syntax**
        ::

          response = client.list_projects(
              sortBy='NAME'|'CREATED_TIME'|'LAST_MODIFIED_TIME',
              sortOrder='ASCENDING'|'DESCENDING',
              nextToken='string'
          )
        :type sortBy: string
        :param sortBy:

          The criterion to be used to list build project names. Valid values include:

          * ``CREATED_TIME`` : List based on when each build project was created.

          * ``LAST_MODIFIED_TIME`` : List based on when information about each build project was
          last changed.

          * ``NAME`` : List based on each build project's name.

          Use ``sortOrder`` to specify in what order to list the build project names based on the
          preceding criteria.

        :type sortOrder: string
        :param sortOrder:

          The order in which to list build projects. Valid values include:

          * ``ASCENDING`` : List in ascending order.

          * ``DESCENDING`` : List in descending order.

          Use ``sortBy`` to specify the criterion to be used to list build project names.

        :type nextToken: string
        :param nextToken:

          During a previous call, if there are more than 100 items in the list, only the first 100
          items are returned, along with a unique string called a *nextToken* . To get the next
          batch of items in the list, call this operation again, adding the next token to the call.
          To get all of the items in the list, keep calling this operation with each subsequent next
          token that is returned, until no more next tokens are returned.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'nextToken': 'string',
                'projects': [
                    'string',
                ]
            }
          **Response Structure**

          - *(dict) --*

            - **nextToken** *(string) --*

              If there are more than 100 items in the list, only the first 100 items are returned,
              along with a unique string called a *nextToken* . To get the next batch of items in
              the list, call this operation again, adding the next token to the call.

            - **projects** *(list) --*

              The list of build project names, with each build project name representing a single
              build project.

              - *(string) --*
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_report_groups(
        self,
        sortOrder: Literal["ASCENDING", "DESCENDING"] = None,
        sortBy: Literal["NAME", "CREATED_TIME", "LAST_MODIFIED_TIME"] = None,
        nextToken: str = None,
        maxResults: int = None,
    ) -> ClientListReportGroupsResponseTypeDef:
        """
        Gets a list ARNs for the report groups in the current AWS account.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/codebuild-2016-10-06/ListReportGroups>`_

        **Request Syntax**
        ::

          response = client.list_report_groups(
              sortOrder='ASCENDING'|'DESCENDING',
              sortBy='NAME'|'CREATED_TIME'|'LAST_MODIFIED_TIME',
              nextToken='string',
              maxResults=123
          )
        :type sortOrder: string
        :param sortOrder:

          Used to specify the order to sort the list of returned report groups. Valid values are
          ``ASCENDING`` and ``DESCENDING`` .

        :type sortBy: string
        :param sortBy:

          The criterion to be used to list build report groups. Valid values include:

          * ``CREATED_TIME`` : List based on when each report group was created.

          * ``LAST_MODIFIED_TIME`` : List based on when each report group was last changed.

          * ``NAME`` : List based on each report group's name.

        :type nextToken: string
        :param nextToken:

          During a previous call, the maximum number of items that can be returned is the value
          specified in ``maxResults`` . If there more items in the list, then a unique string called
          a *nextToken* is returned. To get the next batch of items in the list, call this operation
          again, adding the next token to the call. To get all of the items in the list, keep
          calling this operation with each subsequent next token that is returned, until no more
          next tokens are returned.

        :type maxResults: integer
        :param maxResults:

          The maximum number of paginated report groups returned per response. Use ``nextToken`` to
          iterate pages in the list of returned ``ReportGroup`` objects. The default value is 100.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'nextToken': 'string',
                'reportGroups': [
                    'string',
                ]
            }
          **Response Structure**

          - *(dict) --*

            - **nextToken** *(string) --*

              During a previous call, the maximum number of items that can be returned is the value
              specified in ``maxResults`` . If there more items in the list, then a unique string
              called a *nextToken* is returned. To get the next batch of items in the list, call
              this operation again, adding the next token to the call. To get all of the items in
              the list, keep calling this operation with each subsequent next token that is
              returned, until no more next tokens are returned.

            - **reportGroups** *(list) --*

              The list of ARNs for the report groups in the current AWS account.

              - *(string) --*
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_reports(
        self,
        sortOrder: Literal["ASCENDING", "DESCENDING"] = None,
        nextToken: str = None,
        maxResults: int = None,
        filter: ClientListReportsFilterTypeDef = None,
    ) -> ClientListReportsResponseTypeDef:
        """
        Returns a list of ARNs for the reports in the current AWS account.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/codebuild-2016-10-06/ListReports>`_

        **Request Syntax**
        ::

          response = client.list_reports(
              sortOrder='ASCENDING'|'DESCENDING',
              nextToken='string',
              maxResults=123,
              filter={
                  'status': 'GENERATING'|'SUCCEEDED'|'FAILED'|'INCOMPLETE'|'DELETING'
              }
          )
        :type sortOrder: string
        :param sortOrder:

          Specifies the sort order for the list of returned reports. Valid values are:

          * ``ASCENDING`` : return reports in chronological order based on their creation date.

          * ``DESCENDING`` : return reports in the reverse chronological order based on their
          creation date.

        :type nextToken: string
        :param nextToken:

          During a previous call, the maximum number of items that can be returned is the value
          specified in ``maxResults`` . If there more items in the list, then a unique string called
          a *nextToken* is returned. To get the next batch of items in the list, call this operation
          again, adding the next token to the call. To get all of the items in the list, keep
          calling this operation with each subsequent next token that is returned, until no more
          next tokens are returned.

        :type maxResults: integer
        :param maxResults:

          The maximum number of paginated reports returned per response. Use ``nextToken`` to
          iterate pages in the list of returned ``Report`` objects. The default value is 100.

        :type filter: dict
        :param filter:

          A ``ReportFilter`` object used to filter the returned reports.

          - **status** *(string) --*

            The status used to filter reports. You can filter using one status only.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'nextToken': 'string',
                'reports': [
                    'string',
                ]
            }
          **Response Structure**

          - *(dict) --*

            - **nextToken** *(string) --*

              During a previous call, the maximum number of items that can be returned is the value
              specified in ``maxResults`` . If there more items in the list, then a unique string
              called a *nextToken* is returned. To get the next batch of items in the list, call
              this operation again, adding the next token to the call. To get all of the items in
              the list, keep calling this operation with each subsequent next token that is
              returned, until no more next tokens are returned.

            - **reports** *(list) --*

              The list of returned ARNs for the reports in the current AWS account.

              - *(string) --*
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_reports_for_report_group(
        self,
        reportGroupArn: str,
        nextToken: str = None,
        sortOrder: Literal["ASCENDING", "DESCENDING"] = None,
        maxResults: int = None,
        filter: ClientListReportsForReportGroupFilterTypeDef = None,
    ) -> ClientListReportsForReportGroupResponseTypeDef:
        """
        Returns a list of ARNs for the reports that belong to a ``ReportGroup`` .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/codebuild-2016-10-06/ListReportsForReportGroup>`_

        **Request Syntax**
        ::

          response = client.list_reports_for_report_group(
              reportGroupArn='string',
              nextToken='string',
              sortOrder='ASCENDING'|'DESCENDING',
              maxResults=123,
              filter={
                  'status': 'GENERATING'|'SUCCEEDED'|'FAILED'|'INCOMPLETE'|'DELETING'
              }
          )
        :type reportGroupArn: string
        :param reportGroupArn: **[REQUIRED]**

          The ARN of the report group for which you want to return report ARNs.

        :type nextToken: string
        :param nextToken:

          During a previous call, the maximum number of items that can be returned is the value
          specified in ``maxResults`` . If there more items in the list, then a unique string called
          a *nextToken* is returned. To get the next batch of items in the list, call this operation
          again, adding the next token to the call. To get all of the items in the list, keep
          calling this operation with each subsequent next token that is returned, until no more
          next tokens are returned.

        :type sortOrder: string
        :param sortOrder:

          Use to specify whether the results are returned in ascending or descending order.

        :type maxResults: integer
        :param maxResults:

          The maximum number of paginated reports in this report group returned per response. Use
          ``nextToken`` to iterate pages in the list of returned ``Report`` objects. The default
          value is 100.

        :type filter: dict
        :param filter:

          A ``ReportFilter`` object used to filter the returned reports.

          - **status** *(string) --*

            The status used to filter reports. You can filter using one status only.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'nextToken': 'string',
                'reports': [
                    'string',
                ]
            }
          **Response Structure**

          - *(dict) --*

            - **nextToken** *(string) --*

              During a previous call, the maximum number of items that can be returned is the value
              specified in ``maxResults`` . If there more items in the list, then a unique string
              called a *nextToken* is returned. To get the next batch of items in the list, call
              this operation again, adding the next token to the call. To get all of the items in
              the list, keep calling this operation with each subsequent next token that is
              returned, until no more next tokens are returned.

            - **reports** *(list) --*

              The list of returned report group ARNs.

              - *(string) --*
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_source_credentials(
        self, *args: Any, **kwargs: Any
    ) -> ClientListSourceCredentialsResponseTypeDef:
        """
        Returns a list of ``SourceCredentialsInfo`` objects.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/codebuild-2016-10-06/ListSourceCredentials>`_

        **Request Syntax**
        ::

          response = client.list_source_credentials()

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'sourceCredentialsInfos': [
                    {
                        'arn': 'string',
                        'serverType': 'GITHUB'|'BITBUCKET'|'GITHUB_ENTERPRISE',
                        'authType': 'OAUTH'|'BASIC_AUTH'|'PERSONAL_ACCESS_TOKEN'
                    },
                ]
            }
          **Response Structure**

          - *(dict) --*

            - **sourceCredentialsInfos** *(list) --*

              A list of ``SourceCredentialsInfo`` objects. Each ``SourceCredentialsInfo`` object
              includes the authentication type, token ARN, and type of source provider for one set
              of credentials.

              - *(dict) --*

                Information about the credentials for a GitHub, GitHub Enterprise, or Bitbucket
                repository.

                - **arn** *(string) --*

                  The Amazon Resource Name (ARN) of the token.

                - **serverType** *(string) --*

                  The type of source provider. The valid options are GITHUB, GITHUB_ENTERPRISE, or
                  BITBUCKET.

                - **authType** *(string) --*

                  The type of authentication used by the credentials. Valid options are OAUTH,
                  BASIC_AUTH, or PERSONAL_ACCESS_TOKEN.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def start_build(
        self,
        projectName: str,
        secondarySourcesOverride: List[ClientStartBuildSecondarySourcesOverrideTypeDef] = None,
        secondarySourcesVersionOverride: List[
            ClientStartBuildSecondarySourcesVersionOverrideTypeDef
        ] = None,
        sourceVersion: str = None,
        artifactsOverride: ClientStartBuildArtifactsOverrideTypeDef = None,
        secondaryArtifactsOverride: List[ClientStartBuildSecondaryArtifactsOverrideTypeDef] = None,
        environmentVariablesOverride: List[
            ClientStartBuildEnvironmentVariablesOverrideTypeDef
        ] = None,
        sourceTypeOverride: Literal[
            "CODECOMMIT",
            "CODEPIPELINE",
            "GITHUB",
            "S3",
            "BITBUCKET",
            "GITHUB_ENTERPRISE",
            "NO_SOURCE",
        ] = None,
        sourceLocationOverride: str = None,
        sourceAuthOverride: ClientStartBuildSourceAuthOverrideTypeDef = None,
        gitCloneDepthOverride: int = None,
        gitSubmodulesConfigOverride: ClientStartBuildGitSubmodulesConfigOverrideTypeDef = None,
        buildspecOverride: str = None,
        insecureSslOverride: bool = None,
        reportBuildStatusOverride: bool = None,
        environmentTypeOverride: Literal[
            "WINDOWS_CONTAINER", "LINUX_CONTAINER", "LINUX_GPU_CONTAINER", "ARM_CONTAINER"
        ] = None,
        imageOverride: str = None,
        computeTypeOverride: Literal[
            "BUILD_GENERAL1_SMALL",
            "BUILD_GENERAL1_MEDIUM",
            "BUILD_GENERAL1_LARGE",
            "BUILD_GENERAL1_2XLARGE",
        ] = None,
        certificateOverride: str = None,
        cacheOverride: ClientStartBuildCacheOverrideTypeDef = None,
        serviceRoleOverride: str = None,
        privilegedModeOverride: bool = None,
        timeoutInMinutesOverride: int = None,
        queuedTimeoutInMinutesOverride: int = None,
        idempotencyToken: str = None,
        logsConfigOverride: ClientStartBuildLogsConfigOverrideTypeDef = None,
        registryCredentialOverride: ClientStartBuildRegistryCredentialOverrideTypeDef = None,
        imagePullCredentialsTypeOverride: Literal["CODEBUILD", "SERVICE_ROLE"] = None,
    ) -> ClientStartBuildResponseTypeDef:
        """
        Starts running a build.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/codebuild-2016-10-06/StartBuild>`_

        **Request Syntax**
        ::

          response = client.start_build(
              projectName='string',
              secondarySourcesOverride=[
                  {
                      'type':
                      'CODECOMMIT'|'CODEPIPELINE'|'GITHUB'|'S3'|'BITBUCKET'
                      |'GITHUB_ENTERPRISE'|'NO_SOURCE',
                      'location': 'string',
                      'gitCloneDepth': 123,
                      'gitSubmodulesConfig': {
                          'fetchSubmodules': True|False
                      },
                      'buildspec': 'string',
                      'auth': {
                          'type': 'OAUTH',
                          'resource': 'string'
                      },
                      'reportBuildStatus': True|False,
                      'insecureSsl': True|False,
                      'sourceIdentifier': 'string'
                  },
              ],
              secondarySourcesVersionOverride=[
                  {
                      'sourceIdentifier': 'string',
                      'sourceVersion': 'string'
                  },
              ],
              sourceVersion='string',
              artifactsOverride={
                  'type': 'CODEPIPELINE'|'S3'|'NO_ARTIFACTS',
                  'location': 'string',
                  'path': 'string',
                  'namespaceType': 'NONE'|'BUILD_ID',
                  'name': 'string',
                  'packaging': 'NONE'|'ZIP',
                  'overrideArtifactName': True|False,
                  'encryptionDisabled': True|False,
                  'artifactIdentifier': 'string'
              },
              secondaryArtifactsOverride=[
                  {
                      'type': 'CODEPIPELINE'|'S3'|'NO_ARTIFACTS',
                      'location': 'string',
                      'path': 'string',
                      'namespaceType': 'NONE'|'BUILD_ID',
                      'name': 'string',
                      'packaging': 'NONE'|'ZIP',
                      'overrideArtifactName': True|False,
                      'encryptionDisabled': True|False,
                      'artifactIdentifier': 'string'
                  },
              ],
              environmentVariablesOverride=[
                  {
                      'name': 'string',
                      'value': 'string',
                      'type': 'PLAINTEXT'|'PARAMETER_STORE'|'SECRETS_MANAGER'
                  },
              ],
              sourceTypeOverride=
                  'CODECOMMIT'|'CODEPIPELINE'|'GITHUB'|'S3'|'BITBUCKET'|'GITHUB_ENTERPRISE'
                  |'NO_SOURCE',
              sourceLocationOverride='string',
              sourceAuthOverride={
                  'type': 'OAUTH',
                  'resource': 'string'
              },
              gitCloneDepthOverride=123,
              gitSubmodulesConfigOverride={
                  'fetchSubmodules': True|False
              },
              buildspecOverride='string',
              insecureSslOverride=True|False,
              reportBuildStatusOverride=True|False,
              environmentTypeOverride=
                  'WINDOWS_CONTAINER'|'LINUX_CONTAINER'|'LINUX_GPU_CONTAINER'|'ARM_CONTAINER',
              imageOverride='string',
              computeTypeOverride=
                  'BUILD_GENERAL1_SMALL'|'BUILD_GENERAL1_MEDIUM'|'BUILD_GENERAL1_LARGE'
                  |'BUILD_GENERAL1_2XLARGE',
              certificateOverride='string',
              cacheOverride={
                  'type': 'NO_CACHE'|'S3'|'LOCAL',
                  'location': 'string',
                  'modes': [
                      'LOCAL_DOCKER_LAYER_CACHE'|'LOCAL_SOURCE_CACHE'|'LOCAL_CUSTOM_CACHE',
                  ]
              },
              serviceRoleOverride='string',
              privilegedModeOverride=True|False,
              timeoutInMinutesOverride=123,
              queuedTimeoutInMinutesOverride=123,
              idempotencyToken='string',
              logsConfigOverride={
                  'cloudWatchLogs': {
                      'status': 'ENABLED'|'DISABLED',
                      'groupName': 'string',
                      'streamName': 'string'
                  },
                  's3Logs': {
                      'status': 'ENABLED'|'DISABLED',
                      'location': 'string',
                      'encryptionDisabled': True|False
                  }
              },
              registryCredentialOverride={
                  'credential': 'string',
                  'credentialProvider': 'SECRETS_MANAGER'
              },
              imagePullCredentialsTypeOverride='CODEBUILD'|'SERVICE_ROLE'
          )
        :type projectName: string
        :param projectName: **[REQUIRED]**

          The name of the AWS CodeBuild build project to start running a build.

        :type secondarySourcesOverride: list
        :param secondarySourcesOverride:

          An array of ``ProjectSource`` objects.

          - *(dict) --*

            Information about the build input source code for the build project.

            - **type** *(string) --* **[REQUIRED]**

              The type of repository that contains the source code to be built. Valid values
              include:

              * ``BITBUCKET`` : The source code is in a Bitbucket repository.

              * ``CODECOMMIT`` : The source code is in an AWS CodeCommit repository.

              * ``CODEPIPELINE`` : The source code settings are specified in the source action of a
              pipeline in AWS CodePipeline.

              * ``GITHUB`` : The source code is in a GitHub repository.

              * ``GITHUB_ENTERPRISE`` : The source code is in a GitHub Enterprise repository.

              * ``NO_SOURCE`` : The project does not have input source code.

              * ``S3`` : The source code is in an Amazon Simple Storage Service (Amazon S3) input
              bucket.

            - **location** *(string) --*

              Information about the location of the source code to be built. Valid values include:

              * For source code settings that are specified in the source action of a pipeline in
              AWS CodePipeline, ``location`` should not be specified. If it is specified, AWS
              CodePipeline ignores it. This is because AWS CodePipeline uses the settings in a
              pipeline's source action instead of this value.

              * For source code in an AWS CodeCommit repository, the HTTPS clone URL to the
              repository that contains the source code and the build spec (for example,
              ``https://git-codecommit.*region-ID* .amazonaws.com/v1/repos/*repo-name* `` ).

              * For source code in an Amazon Simple Storage Service (Amazon S3) input bucket, one of
              the following.

                * The path to the ZIP file that contains the source code (for example, ``
                *bucket-name* /*path* /*to* /*object-name* .zip`` ).

                * The path to the folder that contains the source code (for example, ``
                *bucket-name* /*path* /*to* /*source-code* /*folder* /`` ).

              * For source code in a GitHub repository, the HTTPS clone URL to the repository that
              contains the source and the build spec. You must connect your AWS account to your
              GitHub account. Use the AWS CodeBuild console to start creating a build project. When
              you use the console to connect (or reconnect) with GitHub, on the GitHub **Authorize
              application** page, for **Organization access** , choose **Request access** next to
              each repository you want to allow AWS CodeBuild to have access to, and then choose
              **Authorize application** . (After you have connected to your GitHub account, you do
              not need to finish creating the build project. You can leave the AWS CodeBuild
              console.) To instruct AWS CodeBuild to use this connection, in the ``source`` object,
              set the ``auth`` object's ``type`` value to ``OAUTH`` .

              * For source code in a Bitbucket repository, the HTTPS clone URL to the repository
              that contains the source and the build spec. You must connect your AWS account to your
              Bitbucket account. Use the AWS CodeBuild console to start creating a build project.
              When you use the console to connect (or reconnect) with Bitbucket, on the Bitbucket
              **Confirm access to your account** page, choose **Grant access** . (After you have
              connected to your Bitbucket account, you do not need to finish creating the build
              project. You can leave the AWS CodeBuild console.) To instruct AWS CodeBuild to use
              this connection, in the ``source`` object, set the ``auth`` object's ``type`` value to
              ``OAUTH`` .

            - **gitCloneDepth** *(integer) --*

              Information about the Git clone depth for the build project.

            - **gitSubmodulesConfig** *(dict) --*

              Information about the Git submodules configuration for the build project.

              - **fetchSubmodules** *(boolean) --* **[REQUIRED]**

                Set to true to fetch Git submodules for your AWS CodeBuild build project.

            - **buildspec** *(string) --*

              The build spec declaration to use for the builds in this build project.

              If this value is not specified, a build spec must be included along with the source
              code to be built.

            - **auth** *(dict) --*

              Information about the authorization settings for AWS CodeBuild to access the source
              code to be built.

              This information is for the AWS CodeBuild console's use only. Your code should not get
              or set this information directly.

              - **type** *(string) --* **[REQUIRED]**

                .. note::

                  This data type is deprecated and is no longer accurate or used.

                The authorization type to use. The only valid value is ``OAUTH`` , which represents
                the OAuth authorization type.

              - **resource** *(string) --*

                The resource value that applies to the specified authorization type.

            - **reportBuildStatus** *(boolean) --*

              Set to true to report the status of a build's start and finish to your source
              provider. This option is valid only when your source provider is GitHub, GitHub
              Enterprise, or Bitbucket. If this is set and you use a different source provider, an
              invalidInputException is thrown.

              .. note::

                The status of a build triggered by a webhook is always reported to your source
                provider.

            - **insecureSsl** *(boolean) --*

              Enable this flag to ignore SSL warnings while connecting to the project source code.

            - **sourceIdentifier** *(string) --*

              An identifier for this project source.

        :type secondarySourcesVersionOverride: list
        :param secondarySourcesVersionOverride:

          An array of ``ProjectSourceVersion`` objects that specify one or more versions of the
          project's secondary sources to be used for this build only.

          - *(dict) --*

            A source identifier and its corresponding version.

            - **sourceIdentifier** *(string) --* **[REQUIRED]**

              An identifier for a source in the build project.

            - **sourceVersion** *(string) --* **[REQUIRED]**

              The source version for the corresponding source identifier. If specified, must be one
              of:

              * For AWS CodeCommit: the commit ID, branch, or Git tag to use.

              * For GitHub: the commit ID, pull request ID, branch name, or tag name that
              corresponds to the version of the source code you want to build. If a pull request ID
              is specified, it must use the format ``pr/pull-request-ID`` (for example, ``pr/25`` ).
              If a branch name is specified, the branch's HEAD commit ID is used. If not specified,
              the default branch's HEAD commit ID is used.

              * For Bitbucket: the commit ID, branch name, or tag name that corresponds to the
              version of the source code you want to build. If a branch name is specified, the
              branch's HEAD commit ID is used. If not specified, the default branch's HEAD commit ID
              is used.

              * For Amazon Simple Storage Service (Amazon S3): the version ID of the object that
              represents the build input ZIP file to use.

              For more information, see `Source Version Sample with CodeBuild
              <https://docs.aws.amazon.com/codebuild/latest/userguide/sample-source-version.html>`__
              in the *AWS CodeBuild User Guide* .

        :type sourceVersion: string
        :param sourceVersion:

          A version of the build input to be built, for this build only. If not specified, the
          latest version is used. If specified, must be one of:

          * For AWS CodeCommit: the commit ID, branch, or Git tag to use.

          * For GitHub: the commit ID, pull request ID, branch name, or tag name that corresponds to
          the version of the source code you want to build. If a pull request ID is specified, it
          must use the format ``pr/pull-request-ID`` (for example ``pr/25`` ). If a branch name is
          specified, the branch's HEAD commit ID is used. If not specified, the default branch's
          HEAD commit ID is used.

          * For Bitbucket: the commit ID, branch name, or tag name that corresponds to the version
          of the source code you want to build. If a branch name is specified, the branch's HEAD
          commit ID is used. If not specified, the default branch's HEAD commit ID is used.

          * For Amazon Simple Storage Service (Amazon S3): the version ID of the object that
          represents the build input ZIP file to use.

          If ``sourceVersion`` is specified at the project level, then this ``sourceVersion`` (at
          the build level) takes precedence.

          For more information, see `Source Version Sample with CodeBuild
          <https://docs.aws.amazon.com/codebuild/latest/userguide/sample-source-version.html>`__ in
          the *AWS CodeBuild User Guide* .

        :type artifactsOverride: dict
        :param artifactsOverride:

          Build output artifact settings that override, for this build only, the latest ones already
          defined in the build project.

          - **type** *(string) --* **[REQUIRED]**

            The type of build output artifact. Valid values include:

            * ``CODEPIPELINE`` : The build project has build output generated through AWS
            CodePipeline.

            .. note::

               The ``CODEPIPELINE`` type is not supported for ``secondaryArtifacts`` .

            * ``NO_ARTIFACTS`` : The build project does not produce any build output.

            * ``S3`` : The build project stores build output in Amazon Simple Storage Service
            (Amazon S3).

          - **location** *(string) --*

            Information about the build output artifact location:

            * If ``type`` is set to ``CODEPIPELINE`` , AWS CodePipeline ignores this value if
            specified. This is because AWS CodePipeline manages its build output locations instead
            of AWS CodeBuild.

            * If ``type`` is set to ``NO_ARTIFACTS`` , this value is ignored if specified, because
            no build output is produced.

            * If ``type`` is set to ``S3`` , this is the name of the output bucket.

          - **path** *(string) --*

            Along with ``namespaceType`` and ``name`` , the pattern that AWS CodeBuild uses to name
            and store the output artifact:

            * If ``type`` is set to ``CODEPIPELINE`` , AWS CodePipeline ignores this value if
            specified. This is because AWS CodePipeline manages its build output names instead of
            AWS CodeBuild.

            * If ``type`` is set to ``NO_ARTIFACTS`` , this value is ignored if specified, because
            no build output is produced.

            * If ``type`` is set to ``S3`` , this is the path to the output artifact. If ``path`` is
            not specified, ``path`` is not used.

            For example, if ``path`` is set to ``MyArtifacts`` , ``namespaceType`` is set to
            ``NONE`` , and ``name`` is set to ``MyArtifact.zip`` , the output artifact is stored in
            the output bucket at ``MyArtifacts/MyArtifact.zip`` .

          - **namespaceType** *(string) --*

            Along with ``path`` and ``name`` , the pattern that AWS CodeBuild uses to determine the
            name and location to store the output artifact:

            * If ``type`` is set to ``CODEPIPELINE`` , AWS CodePipeline ignores this value if
            specified. This is because AWS CodePipeline manages its build output names instead of
            AWS CodeBuild.

            * If ``type`` is set to ``NO_ARTIFACTS`` , this value is ignored if specified, because
            no build output is produced.

            * If ``type`` is set to ``S3`` , valid values include:

              * ``BUILD_ID`` : Include the build ID in the location of the build output artifact.

              * ``NONE`` : Do not include the build ID. This is the default if ``namespaceType`` is
              not specified.

            For example, if ``path`` is set to ``MyArtifacts`` , ``namespaceType`` is set to
            ``BUILD_ID`` , and ``name`` is set to ``MyArtifact.zip`` , the output artifact is stored
            in ``MyArtifacts/*build-ID* /MyArtifact.zip`` .

          - **name** *(string) --*

            Along with ``path`` and ``namespaceType`` , the pattern that AWS CodeBuild uses to name
            and store the output artifact:

            * If ``type`` is set to ``CODEPIPELINE`` , AWS CodePipeline ignores this value if
            specified. This is because AWS CodePipeline manages its build output names instead of
            AWS CodeBuild.

            * If ``type`` is set to ``NO_ARTIFACTS`` , this value is ignored if specified, because
            no build output is produced.

            * If ``type`` is set to ``S3`` , this is the name of the output artifact object. If you
            set the name to be a forward slash ("/"), the artifact is stored in the root of the
            output bucket.

            For example:

            * If ``path`` is set to ``MyArtifacts`` , ``namespaceType`` is set to ``BUILD_ID`` , and
            ``name`` is set to ``MyArtifact.zip`` , then the output artifact is stored in
            ``MyArtifacts/*build-ID* /MyArtifact.zip`` .

            * If ``path`` is empty, ``namespaceType`` is set to ``NONE`` , and ``name`` is set to
            "``/`` ", the output artifact is stored in the root of the output bucket.

            * If ``path`` is set to ``MyArtifacts`` , ``namespaceType`` is set to ``BUILD_ID`` , and
            ``name`` is set to "``/`` ", the output artifact is stored in ``MyArtifacts/*build-ID*
            `` .

          - **packaging** *(string) --*

            The type of build output artifact to create:

            * If ``type`` is set to ``CODEPIPELINE`` , AWS CodePipeline ignores this value if
            specified. This is because AWS CodePipeline manages its build output artifacts instead
            of AWS CodeBuild.

            * If ``type`` is set to ``NO_ARTIFACTS`` , this value is ignored if specified, because
            no build output is produced.

            * If ``type`` is set to ``S3`` , valid values include:

              * ``NONE`` : AWS CodeBuild creates in the output bucket a folder that contains the
              build output. This is the default if ``packaging`` is not specified.

              * ``ZIP`` : AWS CodeBuild creates in the output bucket a ZIP file that contains the
              build output.

          - **overrideArtifactName** *(boolean) --*

            If this flag is set, a name specified in the build spec file overrides the artifact
            name. The name specified in a build spec file is calculated at build time and uses the
            Shell Command Language. For example, you can append a date and time to your artifact
            name so that it is always unique.

          - **encryptionDisabled** *(boolean) --*

            Set to true if you do not want your output artifacts encrypted. This option is valid
            only if your artifacts type is Amazon Simple Storage Service (Amazon S3). If this is set
            with another artifacts type, an invalidInputException is thrown.

          - **artifactIdentifier** *(string) --*

            An identifier for this artifact definition.

        :type secondaryArtifactsOverride: list
        :param secondaryArtifactsOverride:

          An array of ``ProjectArtifacts`` objects.

          - *(dict) --*

            Information about the build output artifacts for the build project.

            - **type** *(string) --* **[REQUIRED]**

              The type of build output artifact. Valid values include:

              * ``CODEPIPELINE`` : The build project has build output generated through AWS
              CodePipeline.

              .. note::

                 The ``CODEPIPELINE`` type is not supported for ``secondaryArtifacts`` .

              * ``NO_ARTIFACTS`` : The build project does not produce any build output.

              * ``S3`` : The build project stores build output in Amazon Simple Storage Service
              (Amazon S3).

            - **location** *(string) --*

              Information about the build output artifact location:

              * If ``type`` is set to ``CODEPIPELINE`` , AWS CodePipeline ignores this value if
              specified. This is because AWS CodePipeline manages its build output locations instead
              of AWS CodeBuild.

              * If ``type`` is set to ``NO_ARTIFACTS`` , this value is ignored if specified, because
              no build output is produced.

              * If ``type`` is set to ``S3`` , this is the name of the output bucket.

            - **path** *(string) --*

              Along with ``namespaceType`` and ``name`` , the pattern that AWS CodeBuild uses to
              name and store the output artifact:

              * If ``type`` is set to ``CODEPIPELINE`` , AWS CodePipeline ignores this value if
              specified. This is because AWS CodePipeline manages its build output names instead of
              AWS CodeBuild.

              * If ``type`` is set to ``NO_ARTIFACTS`` , this value is ignored if specified, because
              no build output is produced.

              * If ``type`` is set to ``S3`` , this is the path to the output artifact. If ``path``
              is not specified, ``path`` is not used.

              For example, if ``path`` is set to ``MyArtifacts`` , ``namespaceType`` is set to
              ``NONE`` , and ``name`` is set to ``MyArtifact.zip`` , the output artifact is stored
              in the output bucket at ``MyArtifacts/MyArtifact.zip`` .

            - **namespaceType** *(string) --*

              Along with ``path`` and ``name`` , the pattern that AWS CodeBuild uses to determine
              the name and location to store the output artifact:

              * If ``type`` is set to ``CODEPIPELINE`` , AWS CodePipeline ignores this value if
              specified. This is because AWS CodePipeline manages its build output names instead of
              AWS CodeBuild.

              * If ``type`` is set to ``NO_ARTIFACTS`` , this value is ignored if specified, because
              no build output is produced.

              * If ``type`` is set to ``S3`` , valid values include:

                * ``BUILD_ID`` : Include the build ID in the location of the build output artifact.

                * ``NONE`` : Do not include the build ID. This is the default if ``namespaceType``
                is not specified.

              For example, if ``path`` is set to ``MyArtifacts`` , ``namespaceType`` is set to
              ``BUILD_ID`` , and ``name`` is set to ``MyArtifact.zip`` , the output artifact is
              stored in ``MyArtifacts/*build-ID* /MyArtifact.zip`` .

            - **name** *(string) --*

              Along with ``path`` and ``namespaceType`` , the pattern that AWS CodeBuild uses to
              name and store the output artifact:

              * If ``type`` is set to ``CODEPIPELINE`` , AWS CodePipeline ignores this value if
              specified. This is because AWS CodePipeline manages its build output names instead of
              AWS CodeBuild.

              * If ``type`` is set to ``NO_ARTIFACTS`` , this value is ignored if specified, because
              no build output is produced.

              * If ``type`` is set to ``S3`` , this is the name of the output artifact object. If
              you set the name to be a forward slash ("/"), the artifact is stored in the root of
              the output bucket.

              For example:

              * If ``path`` is set to ``MyArtifacts`` , ``namespaceType`` is set to ``BUILD_ID`` ,
              and ``name`` is set to ``MyArtifact.zip`` , then the output artifact is stored in
              ``MyArtifacts/*build-ID* /MyArtifact.zip`` .

              * If ``path`` is empty, ``namespaceType`` is set to ``NONE`` , and ``name`` is set to
              "``/`` ", the output artifact is stored in the root of the output bucket.

              * If ``path`` is set to ``MyArtifacts`` , ``namespaceType`` is set to ``BUILD_ID`` ,
              and ``name`` is set to "``/`` ", the output artifact is stored in
              ``MyArtifacts/*build-ID* `` .

            - **packaging** *(string) --*

              The type of build output artifact to create:

              * If ``type`` is set to ``CODEPIPELINE`` , AWS CodePipeline ignores this value if
              specified. This is because AWS CodePipeline manages its build output artifacts instead
              of AWS CodeBuild.

              * If ``type`` is set to ``NO_ARTIFACTS`` , this value is ignored if specified, because
              no build output is produced.

              * If ``type`` is set to ``S3`` , valid values include:

                * ``NONE`` : AWS CodeBuild creates in the output bucket a folder that contains the
                build output. This is the default if ``packaging`` is not specified.

                * ``ZIP`` : AWS CodeBuild creates in the output bucket a ZIP file that contains the
                build output.

            - **overrideArtifactName** *(boolean) --*

              If this flag is set, a name specified in the build spec file overrides the artifact
              name. The name specified in a build spec file is calculated at build time and uses the
              Shell Command Language. For example, you can append a date and time to your artifact
              name so that it is always unique.

            - **encryptionDisabled** *(boolean) --*

              Set to true if you do not want your output artifacts encrypted. This option is valid
              only if your artifacts type is Amazon Simple Storage Service (Amazon S3). If this is
              set with another artifacts type, an invalidInputException is thrown.

            - **artifactIdentifier** *(string) --*

              An identifier for this artifact definition.

        :type environmentVariablesOverride: list
        :param environmentVariablesOverride:

          A set of environment variables that overrides, for this build only, the latest ones
          already defined in the build project.

          - *(dict) --*

            Information about an environment variable for a build project or a build.

            - **name** *(string) --* **[REQUIRED]**

              The name or key of the environment variable.

            - **value** *(string) --* **[REQUIRED]**

              The value of the environment variable.

              .. warning::

                We strongly discourage the use of environment variables to store sensitive values,
                especially AWS secret key IDs and secret access keys. Environment variables can be
                displayed in plain text using the AWS CodeBuild console and the AWS Command Line
                Interface (AWS CLI).

            - **type** *(string) --*

              The type of environment variable. Valid values include:

              * ``PARAMETER_STORE`` : An environment variable stored in Amazon EC2 Systems Manager
              Parameter Store.

              * ``PLAINTEXT`` : An environment variable in plain text format.

              * ``SECRETS_MANAGER`` : An environment variable stored in AWS Secrets Manager.

        :type sourceTypeOverride: string
        :param sourceTypeOverride:

          A source input type, for this build, that overrides the source input defined in the build
          project.

        :type sourceLocationOverride: string
        :param sourceLocationOverride:

          A location that overrides, for this build, the source location for the one defined in the
          build project.

        :type sourceAuthOverride: dict
        :param sourceAuthOverride:

          An authorization type for this build that overrides the one defined in the build project.
          This override applies only if the build project's source is BitBucket or GitHub.

          - **type** *(string) --* **[REQUIRED]**

            .. note::

              This data type is deprecated and is no longer accurate or used.

            The authorization type to use. The only valid value is ``OAUTH`` , which represents the
            OAuth authorization type.

          - **resource** *(string) --*

            The resource value that applies to the specified authorization type.

        :type gitCloneDepthOverride: integer
        :param gitCloneDepthOverride:

          The user-defined depth of history, with a minimum value of 0, that overrides, for this
          build only, any previous depth of history defined in the build project.

        :type gitSubmodulesConfigOverride: dict
        :param gitSubmodulesConfigOverride:

          Information about the Git submodules configuration for this build of an AWS CodeBuild
          build project.

          - **fetchSubmodules** *(boolean) --* **[REQUIRED]**

            Set to true to fetch Git submodules for your AWS CodeBuild build project.

        :type buildspecOverride: string
        :param buildspecOverride:

          A build spec declaration that overrides, for this build only, the latest one already
          defined in the build project.

        :type insecureSslOverride: boolean
        :param insecureSslOverride:

          Enable this flag to override the insecure SSL setting that is specified in the build
          project. The insecure SSL setting determines whether to ignore SSL warnings while
          connecting to the project source code. This override applies only if the build's source is
          GitHub Enterprise.

        :type reportBuildStatusOverride: boolean
        :param reportBuildStatusOverride:

          Set to true to report to your source provider the status of a build's start and
          completion. If you use this option with a source provider other than GitHub, GitHub
          Enterprise, or Bitbucket, an invalidInputException is thrown.

          .. note::

            The status of a build triggered by a webhook is always reported to your source provider.

        :type environmentTypeOverride: string
        :param environmentTypeOverride:

          A container type for this build that overrides the one specified in the build project.

        :type imageOverride: string
        :param imageOverride:

          The name of an image for this build that overrides the one specified in the build project.

        :type computeTypeOverride: string
        :param computeTypeOverride:

          The name of a compute type for this build that overrides the one specified in the build
          project.

        :type certificateOverride: string
        :param certificateOverride:

          The name of a certificate for this build that overrides the one specified in the build
          project.

        :type cacheOverride: dict
        :param cacheOverride:

          A ProjectCache object specified for this build that overrides the one defined in the build
          project.

          - **type** *(string) --* **[REQUIRED]**

            The type of cache used by the build project. Valid values include:

            * ``NO_CACHE`` : The build project does not use any cache.

            * ``S3`` : The build project reads and writes from and to S3.

            * ``LOCAL`` : The build project stores a cache locally on a build host that is only
            available to that build host.

          - **location** *(string) --*

            Information about the cache location:

            * ``NO_CACHE`` or ``LOCAL`` : This value is ignored.

            * ``S3`` : This is the S3 bucket name/prefix.

          - **modes** *(list) --*

            If you use a ``LOCAL`` cache, the local cache mode. You can use one or more local cache
            modes at the same time.

            * ``LOCAL_SOURCE_CACHE`` mode caches Git metadata for primary and secondary sources.
            After the cache is created, subsequent builds pull only the change between commits. This
            mode is a good choice for projects with a clean working directory and a source that is a
            large Git repository. If you choose this option and your project does not use a Git
            repository (GitHub, GitHub Enterprise, or Bitbucket), the option is ignored.

            * ``LOCAL_DOCKER_LAYER_CACHE`` mode caches existing Docker layers. This mode is a good
            choice for projects that build or pull large Docker images. It can prevent the
            performance issues caused by pulling large Docker images down from the network.

            .. note::

                * You can use a Docker layer cache in the Linux environment only.

                * The ``privileged`` flag must be set so that your project has the required Docker
                permissions.

                * You should consider the security implications before you use a Docker layer cache.

            * ``LOCAL_CUSTOM_CACHE`` mode caches directories you specify in the buildspec file. This
            mode is a good choice if your build scenario is not suited to one of the other three
            local cache modes. If you use a custom cache:

              * Only directories can be specified for caching. You cannot specify individual files.

              * Symlinks are used to reference cached directories.

              * Cached directories are linked to your build before it downloads its project sources.
              Cached items are overridden if a source item has the same name. Directories are
              specified using cache paths in the buildspec file.

            - *(string) --*

        :type serviceRoleOverride: string
        :param serviceRoleOverride:

          The name of a service role for this build that overrides the one specified in the build
          project.

        :type privilegedModeOverride: boolean
        :param privilegedModeOverride:

          Enable this flag to override privileged mode in the build project.

        :type timeoutInMinutesOverride: integer
        :param timeoutInMinutesOverride:

          The number of build timeout minutes, from 5 to 480 (8 hours), that overrides, for this
          build only, the latest setting already defined in the build project.

        :type queuedTimeoutInMinutesOverride: integer
        :param queuedTimeoutInMinutesOverride:

          The number of minutes a build is allowed to be queued before it times out.

        :type idempotencyToken: string
        :param idempotencyToken:

          A unique, case sensitive identifier you provide to ensure the idempotency of the
          StartBuild request. The token is included in the StartBuild request and is valid for 12
          hours. If you repeat the StartBuild request with the same token, but change a parameter,
          AWS CodeBuild returns a parameter mismatch error.

        :type logsConfigOverride: dict
        :param logsConfigOverride:

          Log settings for this build that override the log settings defined in the build project.

          - **cloudWatchLogs** *(dict) --*

            Information about Amazon CloudWatch Logs for a build project. Amazon CloudWatch Logs are
            enabled by default.

            - **status** *(string) --* **[REQUIRED]**

              The current status of the logs in Amazon CloudWatch Logs for a build project. Valid
              values are:

              * ``ENABLED`` : Amazon CloudWatch Logs are enabled for this build project.

              * ``DISABLED`` : Amazon CloudWatch Logs are not enabled for this build project.

            - **groupName** *(string) --*

              The group name of the logs in Amazon CloudWatch Logs. For more information, see
              `Working with Log Groups and Log Streams
              <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html>`__
              .

            - **streamName** *(string) --*

              The prefix of the stream name of the Amazon CloudWatch Logs. For more information, see
              `Working with Log Groups and Log Streams
              <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html>`__
              .

          - **s3Logs** *(dict) --*

            Information about logs built to an S3 bucket for a build project. S3 logs are not
            enabled by default.

            - **status** *(string) --* **[REQUIRED]**

              The current status of the S3 build logs. Valid values are:

              * ``ENABLED`` : S3 build logs are enabled for this build project.

              * ``DISABLED`` : S3 build logs are not enabled for this build project.

            - **location** *(string) --*

              The ARN of an S3 bucket and the path prefix for S3 logs. If your Amazon S3 bucket name
              is ``my-bucket`` , and your path prefix is ``build-log`` , then acceptable formats are
              ``my-bucket/build-log`` or ``arn:aws:s3:::my-bucket/build-log`` .

            - **encryptionDisabled** *(boolean) --*

              Set to true if you do not want your S3 build log output encrypted. By default S3 build
              logs are encrypted.

        :type registryCredentialOverride: dict
        :param registryCredentialOverride:

          The credentials for access to a private registry.

          - **credential** *(string) --* **[REQUIRED]**

            The Amazon Resource Name (ARN) or name of credentials created using AWS Secrets Manager.

            .. note::

              The ``credential`` can use the name of the credentials only if they exist in your
              current region.

          - **credentialProvider** *(string) --* **[REQUIRED]**

            The service that created the credentials to access a private Docker registry. The valid
            value, SECRETS_MANAGER, is for AWS Secrets Manager.

        :type imagePullCredentialsTypeOverride: string
        :param imagePullCredentialsTypeOverride:

          The type of credentials AWS CodeBuild uses to pull images in your build. There are two
          valid values:

          * ``CODEBUILD`` specifies that AWS CodeBuild uses its own credentials. This requires that
          you modify your ECR repository policy to trust AWS CodeBuild's service principal.

          * ``SERVICE_ROLE`` specifies that AWS CodeBuild uses your build project's service role.

          When using a cross-account or private registry image, you must use SERVICE_ROLE
          credentials. When using an AWS CodeBuild curated image, you must use CODEBUILD
          credentials.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'build': {
                    'id': 'string',
                    'arn': 'string',
                    'buildNumber': 123,
                    'startTime': datetime(2015, 1, 1),
                    'endTime': datetime(2015, 1, 1),
                    'currentPhase': 'string',
                    'buildStatus': 'SUCCEEDED'|'FAILED'|'FAULT'|'TIMED_OUT'|'IN_PROGRESS'|'STOPPED',
                    'sourceVersion': 'string',
                    'resolvedSourceVersion': 'string',
                    'projectName': 'string',
                    'phases': [
                        {
                            'phaseType':
                            'SUBMITTED'|'QUEUED'|'PROVISIONING'
                            |'DOWNLOAD_SOURCE'|'INSTALL'|'PRE_BUILD'|'BUILD'
                            |'POST_BUILD'|'UPLOAD_ARTIFACTS'|'FINALIZING'
                            |'COMPLETED',
                            'phaseStatus':
                            'SUCCEEDED'|'FAILED'|'FAULT'|'TIMED_OUT'
                            |'IN_PROGRESS'|'STOPPED',
                            'startTime': datetime(2015, 1, 1),
                            'endTime': datetime(2015, 1, 1),
                            'durationInSeconds': 123,
                            'contexts': [
                                {
                                    'statusCode': 'string',
                                    'message': 'string'
                                },
                            ]
                        },
                    ],
                    'source': {
                        'type':
                        'CODECOMMIT'|'CODEPIPELINE'|'GITHUB'|'S3'|'BITBUCKET'
                        |'GITHUB_ENTERPRISE'|'NO_SOURCE',
                        'location': 'string',
                        'gitCloneDepth': 123,
                        'gitSubmodulesConfig': {
                            'fetchSubmodules': True|False
                        },
                        'buildspec': 'string',
                        'auth': {
                            'type': 'OAUTH',
                            'resource': 'string'
                        },
                        'reportBuildStatus': True|False,
                        'insecureSsl': True|False,
                        'sourceIdentifier': 'string'
                    },
                    'secondarySources': [
                        {
                            'type':
                            'CODECOMMIT'|'CODEPIPELINE'|'GITHUB'|'S3'
                            |'BITBUCKET'|'GITHUB_ENTERPRISE'|'NO_SOURCE',
                            'location': 'string',
                            'gitCloneDepth': 123,
                            'gitSubmodulesConfig': {
                                'fetchSubmodules': True|False
                            },
                            'buildspec': 'string',
                            'auth': {
                                'type': 'OAUTH',
                                'resource': 'string'
                            },
                            'reportBuildStatus': True|False,
                            'insecureSsl': True|False,
                            'sourceIdentifier': 'string'
                        },
                    ],
                    'secondarySourceVersions': [
                        {
                            'sourceIdentifier': 'string',
                            'sourceVersion': 'string'
                        },
                    ],
                    'artifacts': {
                        'location': 'string',
                        'sha256sum': 'string',
                        'md5sum': 'string',
                        'overrideArtifactName': True|False,
                        'encryptionDisabled': True|False,
                        'artifactIdentifier': 'string'
                    },
                    'secondaryArtifacts': [
                        {
                            'location': 'string',
                            'sha256sum': 'string',
                            'md5sum': 'string',
                            'overrideArtifactName': True|False,
                            'encryptionDisabled': True|False,
                            'artifactIdentifier': 'string'
                        },
                    ],
                    'cache': {
                        'type': 'NO_CACHE'|'S3'|'LOCAL',
                        'location': 'string',
                        'modes': [
                            'LOCAL_DOCKER_LAYER_CACHE'|'LOCAL_SOURCE_CACHE'|'LOCAL_CUSTOM_CACHE',
                        ]
                    },
                    'environment': {
                        'type':
                        'WINDOWS_CONTAINER'|'LINUX_CONTAINER'|'LINUX_GPU_CONTAINER'
                        |'ARM_CONTAINER',
                        'image': 'string',
                        'computeType':
                        'BUILD_GENERAL1_SMALL'|'BUILD_GENERAL1_MEDIUM'
                        |'BUILD_GENERAL1_LARGE'|'BUILD_GENERAL1_2XLARGE',
                        'environmentVariables': [
                            {
                                'name': 'string',
                                'value': 'string',
                                'type': 'PLAINTEXT'|'PARAMETER_STORE'|'SECRETS_MANAGER'
                            },
                        ],
                        'privilegedMode': True|False,
                        'certificate': 'string',
                        'registryCredential': {
                            'credential': 'string',
                            'credentialProvider': 'SECRETS_MANAGER'
                        },
                        'imagePullCredentialsType': 'CODEBUILD'|'SERVICE_ROLE'
                    },
                    'serviceRole': 'string',
                    'logs': {
                        'groupName': 'string',
                        'streamName': 'string',
                        'deepLink': 'string',
                        's3DeepLink': 'string',
                        'cloudWatchLogsArn': 'string',
                        's3LogsArn': 'string',
                        'cloudWatchLogs': {
                            'status': 'ENABLED'|'DISABLED',
                            'groupName': 'string',
                            'streamName': 'string'
                        },
                        's3Logs': {
                            'status': 'ENABLED'|'DISABLED',
                            'location': 'string',
                            'encryptionDisabled': True|False
                        }
                    },
                    'timeoutInMinutes': 123,
                    'queuedTimeoutInMinutes': 123,
                    'buildComplete': True|False,
                    'initiator': 'string',
                    'vpcConfig': {
                        'vpcId': 'string',
                        'subnets': [
                            'string',
                        ],
                        'securityGroupIds': [
                            'string',
                        ]
                    },
                    'networkInterface': {
                        'subnetId': 'string',
                        'networkInterfaceId': 'string'
                    },
                    'encryptionKey': 'string',
                    'exportedEnvironmentVariables': [
                        {
                            'name': 'string',
                            'value': 'string'
                        },
                    ],
                    'reportArns': [
                        'string',
                    ]
                }
            }
          **Response Structure**

          - *(dict) --*

            - **build** *(dict) --*

              Information about the build to be run.

              - **id** *(string) --*

                The unique ID for the build.

              - **arn** *(string) --*

                The Amazon Resource Name (ARN) of the build.

              - **buildNumber** *(integer) --*

                The number of the build. For each project, the ``buildNumber`` of its first build is
                ``1`` . The ``buildNumber`` of each subsequent build is incremented by ``1`` . If a
                build is deleted, the ``buildNumber`` of other builds does not change.

              - **startTime** *(datetime) --*

                When the build process started, expressed in Unix time format.

              - **endTime** *(datetime) --*

                When the build process ended, expressed in Unix time format.

              - **currentPhase** *(string) --*

                The current build phase.

              - **buildStatus** *(string) --*

                The current status of the build. Valid values include:

                * ``FAILED`` : The build failed.

                * ``FAULT`` : The build faulted.

                * ``IN_PROGRESS`` : The build is still in progress.

                * ``STOPPED`` : The build stopped.

                * ``SUCCEEDED`` : The build succeeded.

                * ``TIMED_OUT`` : The build timed out.

              - **sourceVersion** *(string) --*

                Any version identifier for the version of the source code to be built. If
                ``sourceVersion`` is specified at the project level, then this ``sourceVersion`` (at
                the build level) takes precedence.

                For more information, see `Source Version Sample with CodeBuild
                <https://docs.aws.amazon.com/codebuild/latest/userguide/sample-source-version.html>`__
                in the *AWS CodeBuild User Guide* .

              - **resolvedSourceVersion** *(string) --*

                An identifier for the version of this build's source code.

                * For AWS CodeCommit, GitHub, GitHub Enterprise, and BitBucket, the commit ID.

                * For AWS CodePipeline, the source revision provided by AWS CodePipeline.

                * For Amazon Simple Storage Service (Amazon S3), this does not apply.

              - **projectName** *(string) --*

                The name of the AWS CodeBuild project.

              - **phases** *(list) --*

                Information about all previous build phases that are complete and information about
                any current build phase that is not yet complete.

                - *(dict) --*

                  Information about a stage for a build.

                  - **phaseType** *(string) --*

                    The name of the build phase. Valid values include:

                    * ``BUILD`` : Core build activities typically occur in this build phase.

                    * ``COMPLETED`` : The build has been completed.

                    * ``DOWNLOAD_SOURCE`` : Source code is being downloaded in this build phase.

                    * ``FINALIZING`` : The build process is completing in this build phase.

                    * ``INSTALL`` : Installation activities typically occur in this build phase.

                    * ``POST_BUILD`` : Post-build activities typically occur in this build phase.

                    * ``PRE_BUILD`` : Pre-build activities typically occur in this build phase.

                    * ``PROVISIONING`` : The build environment is being set up.

                    * ``QUEUED`` : The build has been submitted and is queued behind other submitted
                    builds.

                    * ``SUBMITTED`` : The build has been submitted.

                    * ``UPLOAD_ARTIFACTS`` : Build output artifacts are being uploaded to the output
                    location.

                  - **phaseStatus** *(string) --*

                    The current status of the build phase. Valid values include:

                    * ``FAILED`` : The build phase failed.

                    * ``FAULT`` : The build phase faulted.

                    * ``IN_PROGRESS`` : The build phase is still in progress.

                    * ``QUEUED`` : The build has been submitted and is queued behind other submitted
                    builds.

                    * ``STOPPED`` : The build phase stopped.

                    * ``SUCCEEDED`` : The build phase succeeded.

                    * ``TIMED_OUT`` : The build phase timed out.

                  - **startTime** *(datetime) --*

                    When the build phase started, expressed in Unix time format.

                  - **endTime** *(datetime) --*

                    When the build phase ended, expressed in Unix time format.

                  - **durationInSeconds** *(integer) --*

                    How long, in seconds, between the starting and ending times of the build's
                    phase.

                  - **contexts** *(list) --*

                    Additional information about a build phase, especially to help troubleshoot a
                    failed build.

                    - *(dict) --*

                      Additional information about a build phase that has an error. You can use this
                      information for troubleshooting.

                      - **statusCode** *(string) --*

                        The status code for the context of the build phase.

                      - **message** *(string) --*

                        An explanation of the build phase's context. This might include a command ID
                        and an exit code.

              - **source** *(dict) --*

                Information about the source code to be built.

                - **type** *(string) --*

                  The type of repository that contains the source code to be built. Valid values
                  include:

                  * ``BITBUCKET`` : The source code is in a Bitbucket repository.

                  * ``CODECOMMIT`` : The source code is in an AWS CodeCommit repository.

                  * ``CODEPIPELINE`` : The source code settings are specified in the source action
                  of a pipeline in AWS CodePipeline.

                  * ``GITHUB`` : The source code is in a GitHub repository.

                  * ``GITHUB_ENTERPRISE`` : The source code is in a GitHub Enterprise repository.

                  * ``NO_SOURCE`` : The project does not have input source code.

                  * ``S3`` : The source code is in an Amazon Simple Storage Service (Amazon S3)
                  input bucket.

                - **location** *(string) --*

                  Information about the location of the source code to be built. Valid values
                  include:

                  * For source code settings that are specified in the source action of a pipeline
                  in AWS CodePipeline, ``location`` should not be specified. If it is specified, AWS
                  CodePipeline ignores it. This is because AWS CodePipeline uses the settings in a
                  pipeline's source action instead of this value.

                  * For source code in an AWS CodeCommit repository, the HTTPS clone URL to the
                  repository that contains the source code and the build spec (for example,
                  ``https://git-codecommit.*region-ID* .amazonaws.com/v1/repos/*repo-name* `` ).

                  * For source code in an Amazon Simple Storage Service (Amazon S3) input bucket,
                  one of the following.

                    * The path to the ZIP file that contains the source code (for example, ``
                    *bucket-name* /*path* /*to* /*object-name* .zip`` ).

                    * The path to the folder that contains the source code (for example, ``
                    *bucket-name* /*path* /*to* /*source-code* /*folder* /`` ).

                  * For source code in a GitHub repository, the HTTPS clone URL to the repository
                  that contains the source and the build spec. You must connect your AWS account to
                  your GitHub account. Use the AWS CodeBuild console to start creating a build
                  project. When you use the console to connect (or reconnect) with GitHub, on the
                  GitHub **Authorize application** page, for **Organization access** , choose
                  **Request access** next to each repository you want to allow AWS CodeBuild to have
                  access to, and then choose **Authorize application** . (After you have connected
                  to your GitHub account, you do not need to finish creating the build project. You
                  can leave the AWS CodeBuild console.) To instruct AWS CodeBuild to use this
                  connection, in the ``source`` object, set the ``auth`` object's ``type`` value to
                  ``OAUTH`` .

                  * For source code in a Bitbucket repository, the HTTPS clone URL to the repository
                  that contains the source and the build spec. You must connect your AWS account to
                  your Bitbucket account. Use the AWS CodeBuild console to start creating a build
                  project. When you use the console to connect (or reconnect) with Bitbucket, on the
                  Bitbucket **Confirm access to your account** page, choose **Grant access** .
                  (After you have connected to your Bitbucket account, you do not need to finish
                  creating the build project. You can leave the AWS CodeBuild console.) To instruct
                  AWS CodeBuild to use this connection, in the ``source`` object, set the ``auth``
                  object's ``type`` value to ``OAUTH`` .

                - **gitCloneDepth** *(integer) --*

                  Information about the Git clone depth for the build project.

                - **gitSubmodulesConfig** *(dict) --*

                  Information about the Git submodules configuration for the build project.

                  - **fetchSubmodules** *(boolean) --*

                    Set to true to fetch Git submodules for your AWS CodeBuild build project.

                - **buildspec** *(string) --*

                  The build spec declaration to use for the builds in this build project.

                  If this value is not specified, a build spec must be included along with the
                  source code to be built.

                - **auth** *(dict) --*

                  Information about the authorization settings for AWS CodeBuild to access the
                  source code to be built.

                  This information is for the AWS CodeBuild console's use only. Your code should not
                  get or set this information directly.

                  - **type** *(string) --*

                    .. note::

                      This data type is deprecated and is no longer accurate or used.

                    The authorization type to use. The only valid value is ``OAUTH`` , which
                    represents the OAuth authorization type.

                  - **resource** *(string) --*

                    The resource value that applies to the specified authorization type.

                - **reportBuildStatus** *(boolean) --*

                  Set to true to report the status of a build's start and finish to your source
                  provider. This option is valid only when your source provider is GitHub, GitHub
                  Enterprise, or Bitbucket. If this is set and you use a different source provider,
                  an invalidInputException is thrown.

                  .. note::

                    The status of a build triggered by a webhook is always reported to your source
                    provider.

                - **insecureSsl** *(boolean) --*

                  Enable this flag to ignore SSL warnings while connecting to the project source
                  code.

                - **sourceIdentifier** *(string) --*

                  An identifier for this project source.

              - **secondarySources** *(list) --*

                An array of ``ProjectSource`` objects.

                - *(dict) --*

                  Information about the build input source code for the build project.

                  - **type** *(string) --*

                    The type of repository that contains the source code to be built. Valid values
                    include:

                    * ``BITBUCKET`` : The source code is in a Bitbucket repository.

                    * ``CODECOMMIT`` : The source code is in an AWS CodeCommit repository.

                    * ``CODEPIPELINE`` : The source code settings are specified in the source action
                    of a pipeline in AWS CodePipeline.

                    * ``GITHUB`` : The source code is in a GitHub repository.

                    * ``GITHUB_ENTERPRISE`` : The source code is in a GitHub Enterprise repository.

                    * ``NO_SOURCE`` : The project does not have input source code.

                    * ``S3`` : The source code is in an Amazon Simple Storage Service (Amazon S3)
                    input bucket.

                  - **location** *(string) --*

                    Information about the location of the source code to be built. Valid values
                    include:

                    * For source code settings that are specified in the source action of a pipeline
                    in AWS CodePipeline, ``location`` should not be specified. If it is specified,
                    AWS CodePipeline ignores it. This is because AWS CodePipeline uses the settings
                    in a pipeline's source action instead of this value.

                    * For source code in an AWS CodeCommit repository, the HTTPS clone URL to the
                    repository that contains the source code and the build spec (for example,
                    ``https://git-codecommit.*region-ID* .amazonaws.com/v1/repos/*repo-name* `` ).

                    * For source code in an Amazon Simple Storage Service (Amazon S3) input bucket,
                    one of the following.

                      * The path to the ZIP file that contains the source code (for example, ``
                      *bucket-name* /*path* /*to* /*object-name* .zip`` ).

                      * The path to the folder that contains the source code (for example, ``
                      *bucket-name* /*path* /*to* /*source-code* /*folder* /`` ).

                    * For source code in a GitHub repository, the HTTPS clone URL to the repository
                    that contains the source and the build spec. You must connect your AWS account
                    to your GitHub account. Use the AWS CodeBuild console to start creating a build
                    project. When you use the console to connect (or reconnect) with GitHub, on the
                    GitHub **Authorize application** page, for **Organization access** , choose
                    **Request access** next to each repository you want to allow AWS CodeBuild to
                    have access to, and then choose **Authorize application** . (After you have
                    connected to your GitHub account, you do not need to finish creating the build
                    project. You can leave the AWS CodeBuild console.) To instruct AWS CodeBuild to
                    use this connection, in the ``source`` object, set the ``auth`` object's
                    ``type`` value to ``OAUTH`` .

                    * For source code in a Bitbucket repository, the HTTPS clone URL to the
                    repository that contains the source and the build spec. You must connect your
                    AWS account to your Bitbucket account. Use the AWS CodeBuild console to start
                    creating a build project. When you use the console to connect (or reconnect)
                    with Bitbucket, on the Bitbucket **Confirm access to your account** page, choose
                    **Grant access** . (After you have connected to your Bitbucket account, you do
                    not need to finish creating the build project. You can leave the AWS CodeBuild
                    console.) To instruct AWS CodeBuild to use this connection, in the ``source``
                    object, set the ``auth`` object's ``type`` value to ``OAUTH`` .

                  - **gitCloneDepth** *(integer) --*

                    Information about the Git clone depth for the build project.

                  - **gitSubmodulesConfig** *(dict) --*

                    Information about the Git submodules configuration for the build project.

                    - **fetchSubmodules** *(boolean) --*

                      Set to true to fetch Git submodules for your AWS CodeBuild build project.

                  - **buildspec** *(string) --*

                    The build spec declaration to use for the builds in this build project.

                    If this value is not specified, a build spec must be included along with the
                    source code to be built.

                  - **auth** *(dict) --*

                    Information about the authorization settings for AWS CodeBuild to access the
                    source code to be built.

                    This information is for the AWS CodeBuild console's use only. Your code should
                    not get or set this information directly.

                    - **type** *(string) --*

                      .. note::

                        This data type is deprecated and is no longer accurate or used.

                      The authorization type to use. The only valid value is ``OAUTH`` , which
                      represents the OAuth authorization type.

                    - **resource** *(string) --*

                      The resource value that applies to the specified authorization type.

                  - **reportBuildStatus** *(boolean) --*

                    Set to true to report the status of a build's start and finish to your source
                    provider. This option is valid only when your source provider is GitHub, GitHub
                    Enterprise, or Bitbucket. If this is set and you use a different source
                    provider, an invalidInputException is thrown.

                    .. note::

                      The status of a build triggered by a webhook is always reported to your source
                      provider.

                  - **insecureSsl** *(boolean) --*

                    Enable this flag to ignore SSL warnings while connecting to the project source
                    code.

                  - **sourceIdentifier** *(string) --*

                    An identifier for this project source.

              - **secondarySourceVersions** *(list) --*

                An array of ``ProjectSourceVersion`` objects. Each ``ProjectSourceVersion`` must be
                one of:

                * For AWS CodeCommit: the commit ID, branch, or Git tag to use.

                * For GitHub: the commit ID, pull request ID, branch name, or tag name that
                corresponds to the version of the source code you want to build. If a pull request
                ID is specified, it must use the format ``pr/pull-request-ID`` (for example,
                ``pr/25`` ). If a branch name is specified, the branch's HEAD commit ID is used. If
                not specified, the default branch's HEAD commit ID is used.

                * For Bitbucket: the commit ID, branch name, or tag name that corresponds to the
                version of the source code you want to build. If a branch name is specified, the
                branch's HEAD commit ID is used. If not specified, the default branch's HEAD commit
                ID is used.

                * For Amazon Simple Storage Service (Amazon S3): the version ID of the object that
                represents the build input ZIP file to use.

                - *(dict) --*

                  A source identifier and its corresponding version.

                  - **sourceIdentifier** *(string) --*

                    An identifier for a source in the build project.

                  - **sourceVersion** *(string) --*

                    The source version for the corresponding source identifier. If specified, must
                    be one of:

                    * For AWS CodeCommit: the commit ID, branch, or Git tag to use.

                    * For GitHub: the commit ID, pull request ID, branch name, or tag name that
                    corresponds to the version of the source code you want to build. If a pull
                    request ID is specified, it must use the format ``pr/pull-request-ID`` (for
                    example, ``pr/25`` ). If a branch name is specified, the branch's HEAD commit ID
                    is used. If not specified, the default branch's HEAD commit ID is used.

                    * For Bitbucket: the commit ID, branch name, or tag name that corresponds to the
                    version of the source code you want to build. If a branch name is specified, the
                    branch's HEAD commit ID is used. If not specified, the default branch's HEAD
                    commit ID is used.

                    * For Amazon Simple Storage Service (Amazon S3): the version ID of the object
                    that represents the build input ZIP file to use.

                    For more information, see `Source Version Sample with CodeBuild
                    <https://docs.aws.amazon.com/codebuild/latest/userguide/sample-source-version.html>`__
                    in the *AWS CodeBuild User Guide* .

              - **artifacts** *(dict) --*

                Information about the output artifacts for the build.

                - **location** *(string) --*

                  Information about the location of the build artifacts.

                - **sha256sum** *(string) --*

                  The SHA-256 hash of the build artifact.

                  You can use this hash along with a checksum tool to confirm file integrity and
                  authenticity.

                  .. note::

                    This value is available only if the build project's ``packaging`` value is set
                    to ``ZIP`` .

                - **md5sum** *(string) --*

                  The MD5 hash of the build artifact.

                  You can use this hash along with a checksum tool to confirm file integrity and
                  authenticity.

                  .. note::

                    This value is available only if the build project's ``packaging`` value is set
                    to ``ZIP`` .

                - **overrideArtifactName** *(boolean) --*

                  If this flag is set, a name specified in the build spec file overrides the
                  artifact name. The name specified in a build spec file is calculated at build time
                  and uses the Shell Command Language. For example, you can append a date and time
                  to your artifact name so that it is always unique.

                - **encryptionDisabled** *(boolean) --*

                  Information that tells you if encryption for build artifacts is disabled.

                - **artifactIdentifier** *(string) --*

                  An identifier for this artifact definition.

              - **secondaryArtifacts** *(list) --*

                An array of ``ProjectArtifacts`` objects.

                - *(dict) --*

                  Information about build output artifacts.

                  - **location** *(string) --*

                    Information about the location of the build artifacts.

                  - **sha256sum** *(string) --*

                    The SHA-256 hash of the build artifact.

                    You can use this hash along with a checksum tool to confirm file integrity and
                    authenticity.

                    .. note::

                      This value is available only if the build project's ``packaging`` value is set
                      to ``ZIP`` .

                  - **md5sum** *(string) --*

                    The MD5 hash of the build artifact.

                    You can use this hash along with a checksum tool to confirm file integrity and
                    authenticity.

                    .. note::

                      This value is available only if the build project's ``packaging`` value is set
                      to ``ZIP`` .

                  - **overrideArtifactName** *(boolean) --*

                    If this flag is set, a name specified in the build spec file overrides the
                    artifact name. The name specified in a build spec file is calculated at build
                    time and uses the Shell Command Language. For example, you can append a date and
                    time to your artifact name so that it is always unique.

                  - **encryptionDisabled** *(boolean) --*

                    Information that tells you if encryption for build artifacts is disabled.

                  - **artifactIdentifier** *(string) --*

                    An identifier for this artifact definition.

              - **cache** *(dict) --*

                Information about the cache for the build.

                - **type** *(string) --*

                  The type of cache used by the build project. Valid values include:

                  * ``NO_CACHE`` : The build project does not use any cache.

                  * ``S3`` : The build project reads and writes from and to S3.

                  * ``LOCAL`` : The build project stores a cache locally on a build host that is
                  only available to that build host.

                - **location** *(string) --*

                  Information about the cache location:

                  * ``NO_CACHE`` or ``LOCAL`` : This value is ignored.

                  * ``S3`` : This is the S3 bucket name/prefix.

                - **modes** *(list) --*

                  If you use a ``LOCAL`` cache, the local cache mode. You can use one or more local
                  cache modes at the same time.

                  * ``LOCAL_SOURCE_CACHE`` mode caches Git metadata for primary and secondary
                  sources. After the cache is created, subsequent builds pull only the change
                  between commits. This mode is a good choice for projects with a clean working
                  directory and a source that is a large Git repository. If you choose this option
                  and your project does not use a Git repository (GitHub, GitHub Enterprise, or
                  Bitbucket), the option is ignored.

                  * ``LOCAL_DOCKER_LAYER_CACHE`` mode caches existing Docker layers. This mode is a
                  good choice for projects that build or pull large Docker images. It can prevent
                  the performance issues caused by pulling large Docker images down from the
                  network.

                  .. note::

                      * You can use a Docker layer cache in the Linux environment only.

                      * The ``privileged`` flag must be set so that your project has the required
                      Docker permissions.

                      * You should consider the security implications before you use a Docker layer
                      cache.

                  * ``LOCAL_CUSTOM_CACHE`` mode caches directories you specify in the buildspec
                  file. This mode is a good choice if your build scenario is not suited to one of
                  the other three local cache modes. If you use a custom cache:

                    * Only directories can be specified for caching. You cannot specify individual
                    files.

                    * Symlinks are used to reference cached directories.

                    * Cached directories are linked to your build before it downloads its project
                    sources. Cached items are overridden if a source item has the same name.
                    Directories are specified using cache paths in the buildspec file.

                  - *(string) --*

              - **environment** *(dict) --*

                Information about the build environment for this build.

                - **type** *(string) --*

                  The type of build environment to use for related builds.

                  * The environment type ``ARM_CONTAINER`` is available only in regions US East (N.
                  Virginia), US East (Ohio), US West (Oregon), EU (Ireland), Asia Pacific (Mumbai),
                  Asia Pacific (Tokyo), Asia Pacific (Sydney), and EU (Frankfurt).

                  * The environment type ``LINUX_CONTAINER`` with compute type
                  ``build.general1.2xlarge`` is available only in regions US East (N. Virginia), US
                  East (N. Virginia), US West (Oregon), Canada (Central), EU (Ireland), EU (London),
                  EU (Frankfurt), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific
                  (Singapore), Asia Pacific (Sydney), China (Beijing), and China (Ningxia).

                  * The environment type ``LINUX_GPU_CONTAINER`` is available only in regions US
                  East (N. Virginia), US East (N. Virginia), US West (Oregon), Canada (Central), EU
                  (Ireland), EU (London), EU (Frankfurt), Asia Pacific (Tokyo), Asia Pacific
                  (Seoul), Asia Pacific (Singapore), Asia Pacific (Sydney) , China (Beijing), and
                  China (Ningxia).

                - **image** *(string) --*

                  The image tag or image digest that identifies the Docker image to use for this
                  build project. Use the following formats:

                  * For an image tag: ``registry/repository:tag`` . For example, to specify an image
                  with the tag "latest," use ``registry/repository:latest`` .

                  * For an image digest: ``registry/repository@digest`` . For example, to specify an
                  image with the digest
                  "sha256:cbbf2f9a99b47fc460d422812b6a5adff7dfee951d8fa2e4a98caa0382cfbdbf," use
                  ``registry/repository@sha256:cbbf2f9a99b47fc460d422812b6a5adff7dfee951d8fa2e4a98caa0382cfbdbf``
                  .

                - **computeType** *(string) --*

                  Information about the compute resources the build project uses. Available values
                  include:

                  * ``BUILD_GENERAL1_SMALL`` : Use up to 3 GB memory and 2 vCPUs for builds.

                  * ``BUILD_GENERAL1_MEDIUM`` : Use up to 7 GB memory and 4 vCPUs for builds.

                  * ``BUILD_GENERAL1_LARGE`` : Use up to 16 GB memory and 8 vCPUs for builds,
                  depending on your environment type.

                  * ``BUILD_GENERAL1_2XLARGE`` : Use up to 145 GB memory, 72 vCPUs, and 824 GB of
                  SSD storage for builds. This compute type supports Docker images up to 100 GB
                  uncompressed.

                  If you use ``BUILD_GENERAL1_LARGE`` :

                  * For environment type ``LINUX_CONTAINER`` , you can use up to 15 GB memory and 8
                  vCPUs for builds.

                  * For environment type ``LINUX_GPU_CONTAINER`` , you can use up to 255 GB memory,
                  32 vCPUs, and 4 NVIDIA Tesla V100 GPUs for builds.

                  * For environment type ``ARM_CONTAINER`` , you can use up to 16 GB memory and 8
                  vCPUs on ARM-based processors for builds.

                  For more information, see `Build Environment Compute Types
                  <https://docs.aws.amazon.com/codebuild/latest/userguide/build-env-ref-compute-types.html>`__
                  in the *AWS CodeBuild User Guide.*

                - **environmentVariables** *(list) --*

                  A set of environment variables to make available to builds for this build project.

                  - *(dict) --*

                    Information about an environment variable for a build project or a build.

                    - **name** *(string) --*

                      The name or key of the environment variable.

                    - **value** *(string) --*

                      The value of the environment variable.

                      .. warning::

                        We strongly discourage the use of environment variables to store sensitive
                        values, especially AWS secret key IDs and secret access keys. Environment
                        variables can be displayed in plain text using the AWS CodeBuild console and
                        the AWS Command Line Interface (AWS CLI).

                    - **type** *(string) --*

                      The type of environment variable. Valid values include:

                      * ``PARAMETER_STORE`` : An environment variable stored in Amazon EC2 Systems
                      Manager Parameter Store.

                      * ``PLAINTEXT`` : An environment variable in plain text format.

                      * ``SECRETS_MANAGER`` : An environment variable stored in AWS Secrets Manager.

                - **privilegedMode** *(boolean) --*

                  Enables running the Docker daemon inside a Docker container. Set to true only if
                  the build project is used to build Docker images. Otherwise, a build that attempts
                  to interact with the Docker daemon fails. The default setting is ``false`` .

                  You can initialize the Docker daemon during the install phase of your build by
                  adding one of the following sets of commands to the install phase of your
                  buildspec file:

                  If the operating system's base image is Ubuntu Linux:

                   ``- nohup /usr/local/bin/dockerd --host=unix:///var/run/docker.sock
                   --host=tcp://0.0.0.0:2375 --storage-driver=overlay&``

                   ``- timeout 15 sh -c "until docker info; do echo .; sleep 1; done"``

                  If the operating system's base image is Alpine Linux and the previous command does
                  not work, add the ``-t`` argument to ``timeout`` :

                   ``- nohup /usr/local/bin/dockerd --host=unix:///var/run/docker.sock
                   --host=tcp://0.0.0.0:2375 --storage-driver=overlay&``

                   ``- timeout -t 15 sh -c "until docker info; do echo .; sleep 1; done"``

                - **certificate** *(string) --*

                  The certificate to use with this build project.

                - **registryCredential** *(dict) --*

                  The credentials for access to a private registry.

                  - **credential** *(string) --*

                    The Amazon Resource Name (ARN) or name of credentials created using AWS Secrets
                    Manager.

                    .. note::

                      The ``credential`` can use the name of the credentials only if they exist in
                      your current region.

                  - **credentialProvider** *(string) --*

                    The service that created the credentials to access a private Docker registry.
                    The valid value, SECRETS_MANAGER, is for AWS Secrets Manager.

                - **imagePullCredentialsType** *(string) --*

                  The type of credentials AWS CodeBuild uses to pull images in your build. There are
                  two valid values:

                  * ``CODEBUILD`` specifies that AWS CodeBuild uses its own credentials. This
                  requires that you modify your ECR repository policy to trust AWS CodeBuild's
                  service principal.

                  * ``SERVICE_ROLE`` specifies that AWS CodeBuild uses your build project's service
                  role.

                  When you use a cross-account or private registry image, you must use SERVICE_ROLE
                  credentials. When you use an AWS CodeBuild curated image, you must use CODEBUILD
                  credentials.

              - **serviceRole** *(string) --*

                The name of a service role used for this build.

              - **logs** *(dict) --*

                Information about the build's logs in Amazon CloudWatch Logs.

                - **groupName** *(string) --*

                  The name of the Amazon CloudWatch Logs group for the build logs.

                - **streamName** *(string) --*

                  The name of the Amazon CloudWatch Logs stream for the build logs.

                - **deepLink** *(string) --*

                  The URL to an individual build log in Amazon CloudWatch Logs.

                - **s3DeepLink** *(string) --*

                  The URL to a build log in an S3 bucket.

                - **cloudWatchLogsArn** *(string) --*

                  The ARN of Amazon CloudWatch Logs for a build project. Its format is
                  ``arn:${Partition}:logs:${Region}:${Account}:log-group:${LogGroupName}:log-stream:${LogStreamName}``
                  . For more information, see `Resources Defined by Amazon CloudWatch Logs
                  <https://docs.aws.amazon.com/IAM/latest/UserGuide/list_amazoncloudwatchlogs.html#amazoncloudwatchlogs-resources-for-iam-policies>`__
                  .

                - **s3LogsArn** *(string) --*

                  The ARN of S3 logs for a build project. Its format is
                  ``arn:${Partition}:s3:::${BucketName}/${ObjectName}`` . For more information, see
                  `Resources Defined by Amazon S3
                  <https://docs.aws.amazon.com/IAM/latest/UserGuide/list_amazons3.html#amazons3-resources-for-iam-policies>`__
                  .

                - **cloudWatchLogs** *(dict) --*

                  Information about Amazon CloudWatch Logs for a build project.

                  - **status** *(string) --*

                    The current status of the logs in Amazon CloudWatch Logs for a build project.
                    Valid values are:

                    * ``ENABLED`` : Amazon CloudWatch Logs are enabled for this build project.

                    * ``DISABLED`` : Amazon CloudWatch Logs are not enabled for this build project.

                  - **groupName** *(string) --*

                    The group name of the logs in Amazon CloudWatch Logs. For more information, see
                    `Working with Log Groups and Log Streams
                    <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html>`__
                    .

                  - **streamName** *(string) --*

                    The prefix of the stream name of the Amazon CloudWatch Logs. For more
                    information, see `Working with Log Groups and Log Streams
                    <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html>`__
                    .

                - **s3Logs** *(dict) --*

                  Information about S3 logs for a build project.

                  - **status** *(string) --*

                    The current status of the S3 build logs. Valid values are:

                    * ``ENABLED`` : S3 build logs are enabled for this build project.

                    * ``DISABLED`` : S3 build logs are not enabled for this build project.

                  - **location** *(string) --*

                    The ARN of an S3 bucket and the path prefix for S3 logs. If your Amazon S3
                    bucket name is ``my-bucket`` , and your path prefix is ``build-log`` , then
                    acceptable formats are ``my-bucket/build-log`` or
                    ``arn:aws:s3:::my-bucket/build-log`` .

                  - **encryptionDisabled** *(boolean) --*

                    Set to true if you do not want your S3 build log output encrypted. By default S3
                    build logs are encrypted.

              - **timeoutInMinutes** *(integer) --*

                How long, in minutes, for AWS CodeBuild to wait before timing out this build if it
                does not get marked as completed.

              - **queuedTimeoutInMinutes** *(integer) --*

                The number of minutes a build is allowed to be queued before it times out.

              - **buildComplete** *(boolean) --*

                Whether the build is complete. True if complete; otherwise, false.

              - **initiator** *(string) --*

                The entity that started the build. Valid values include:

                * If AWS CodePipeline started the build, the pipeline's name (for example,
                ``codepipeline/my-demo-pipeline`` ).

                * If an AWS Identity and Access Management (IAM) user started the build, the user's
                name (for example, ``MyUserName`` ).

                * If the Jenkins plugin for AWS CodeBuild started the build, the string
                ``CodeBuild-Jenkins-Plugin`` .

              - **vpcConfig** *(dict) --*

                If your AWS CodeBuild project accesses resources in an Amazon VPC, you provide this
                parameter that identifies the VPC ID and the list of security group IDs and subnet
                IDs. The security groups and subnets must belong to the same VPC. You must provide
                at least one security group and one subnet ID.

                - **vpcId** *(string) --*

                  The ID of the Amazon VPC.

                - **subnets** *(list) --*

                  A list of one or more subnet IDs in your Amazon VPC.

                  - *(string) --*

                - **securityGroupIds** *(list) --*

                  A list of one or more security groups IDs in your Amazon VPC.

                  - *(string) --*

              - **networkInterface** *(dict) --*

                Describes a network interface.

                - **subnetId** *(string) --*

                  The ID of the subnet.

                - **networkInterfaceId** *(string) --*

                  The ID of the network interface.

              - **encryptionKey** *(string) --*

                The AWS Key Management Service (AWS KMS) customer master key (CMK) to be used for
                encrypting the build output artifacts.

                .. note::

                  You can use a cross-account KMS key to encrypt the build output artifacts if your
                  service role has permission to that key.

                You can specify either the Amazon Resource Name (ARN) of the CMK or, if available,
                the CMK's alias (using the format ``alias/*alias-name* `` ).

              - **exportedEnvironmentVariables** *(list) --*

                A list of exported environment variables for this build.

                - *(dict) --*

                  Information about an exported environment variable.

                  - **name** *(string) --*

                    The name of this exported environment variable.

                  - **value** *(string) --*

                    The value assigned to this exported environment variable.

                    .. note::

                      During a build, the value of a variable is available starting with the
                      ``install`` phase. It can be updated between the start of the ``install``
                      phase and the end of the ``post_build`` phase. After the ``post_build`` phase
                      ends, the value of exported variables cannot change.

              - **reportArns** *(list) --*

                An array of the ARNs associated with this build's reports.

                - *(string) --*
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def stop_build(self, id: str) -> ClientStopBuildResponseTypeDef:
        """
        Attempts to stop running a build.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/codebuild-2016-10-06/StopBuild>`_

        **Request Syntax**
        ::

          response = client.stop_build(
              id='string'
          )
        :type id: string
        :param id: **[REQUIRED]**

          The ID of the build.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'build': {
                    'id': 'string',
                    'arn': 'string',
                    'buildNumber': 123,
                    'startTime': datetime(2015, 1, 1),
                    'endTime': datetime(2015, 1, 1),
                    'currentPhase': 'string',
                    'buildStatus': 'SUCCEEDED'|'FAILED'|'FAULT'|'TIMED_OUT'|'IN_PROGRESS'|'STOPPED',
                    'sourceVersion': 'string',
                    'resolvedSourceVersion': 'string',
                    'projectName': 'string',
                    'phases': [
                        {
                            'phaseType':
                            'SUBMITTED'|'QUEUED'|'PROVISIONING'
                            |'DOWNLOAD_SOURCE'|'INSTALL'|'PRE_BUILD'|'BUILD'
                            |'POST_BUILD'|'UPLOAD_ARTIFACTS'|'FINALIZING'
                            |'COMPLETED',
                            'phaseStatus':
                            'SUCCEEDED'|'FAILED'|'FAULT'|'TIMED_OUT'
                            |'IN_PROGRESS'|'STOPPED',
                            'startTime': datetime(2015, 1, 1),
                            'endTime': datetime(2015, 1, 1),
                            'durationInSeconds': 123,
                            'contexts': [
                                {
                                    'statusCode': 'string',
                                    'message': 'string'
                                },
                            ]
                        },
                    ],
                    'source': {
                        'type':
                        'CODECOMMIT'|'CODEPIPELINE'|'GITHUB'|'S3'|'BITBUCKET'
                        |'GITHUB_ENTERPRISE'|'NO_SOURCE',
                        'location': 'string',
                        'gitCloneDepth': 123,
                        'gitSubmodulesConfig': {
                            'fetchSubmodules': True|False
                        },
                        'buildspec': 'string',
                        'auth': {
                            'type': 'OAUTH',
                            'resource': 'string'
                        },
                        'reportBuildStatus': True|False,
                        'insecureSsl': True|False,
                        'sourceIdentifier': 'string'
                    },
                    'secondarySources': [
                        {
                            'type':
                            'CODECOMMIT'|'CODEPIPELINE'|'GITHUB'|'S3'
                            |'BITBUCKET'|'GITHUB_ENTERPRISE'|'NO_SOURCE',
                            'location': 'string',
                            'gitCloneDepth': 123,
                            'gitSubmodulesConfig': {
                                'fetchSubmodules': True|False
                            },
                            'buildspec': 'string',
                            'auth': {
                                'type': 'OAUTH',
                                'resource': 'string'
                            },
                            'reportBuildStatus': True|False,
                            'insecureSsl': True|False,
                            'sourceIdentifier': 'string'
                        },
                    ],
                    'secondarySourceVersions': [
                        {
                            'sourceIdentifier': 'string',
                            'sourceVersion': 'string'
                        },
                    ],
                    'artifacts': {
                        'location': 'string',
                        'sha256sum': 'string',
                        'md5sum': 'string',
                        'overrideArtifactName': True|False,
                        'encryptionDisabled': True|False,
                        'artifactIdentifier': 'string'
                    },
                    'secondaryArtifacts': [
                        {
                            'location': 'string',
                            'sha256sum': 'string',
                            'md5sum': 'string',
                            'overrideArtifactName': True|False,
                            'encryptionDisabled': True|False,
                            'artifactIdentifier': 'string'
                        },
                    ],
                    'cache': {
                        'type': 'NO_CACHE'|'S3'|'LOCAL',
                        'location': 'string',
                        'modes': [
                            'LOCAL_DOCKER_LAYER_CACHE'|'LOCAL_SOURCE_CACHE'|'LOCAL_CUSTOM_CACHE',
                        ]
                    },
                    'environment': {
                        'type':
                        'WINDOWS_CONTAINER'|'LINUX_CONTAINER'|'LINUX_GPU_CONTAINER'
                        |'ARM_CONTAINER',
                        'image': 'string',
                        'computeType':
                        'BUILD_GENERAL1_SMALL'|'BUILD_GENERAL1_MEDIUM'
                        |'BUILD_GENERAL1_LARGE'|'BUILD_GENERAL1_2XLARGE',
                        'environmentVariables': [
                            {
                                'name': 'string',
                                'value': 'string',
                                'type': 'PLAINTEXT'|'PARAMETER_STORE'|'SECRETS_MANAGER'
                            },
                        ],
                        'privilegedMode': True|False,
                        'certificate': 'string',
                        'registryCredential': {
                            'credential': 'string',
                            'credentialProvider': 'SECRETS_MANAGER'
                        },
                        'imagePullCredentialsType': 'CODEBUILD'|'SERVICE_ROLE'
                    },
                    'serviceRole': 'string',
                    'logs': {
                        'groupName': 'string',
                        'streamName': 'string',
                        'deepLink': 'string',
                        's3DeepLink': 'string',
                        'cloudWatchLogsArn': 'string',
                        's3LogsArn': 'string',
                        'cloudWatchLogs': {
                            'status': 'ENABLED'|'DISABLED',
                            'groupName': 'string',
                            'streamName': 'string'
                        },
                        's3Logs': {
                            'status': 'ENABLED'|'DISABLED',
                            'location': 'string',
                            'encryptionDisabled': True|False
                        }
                    },
                    'timeoutInMinutes': 123,
                    'queuedTimeoutInMinutes': 123,
                    'buildComplete': True|False,
                    'initiator': 'string',
                    'vpcConfig': {
                        'vpcId': 'string',
                        'subnets': [
                            'string',
                        ],
                        'securityGroupIds': [
                            'string',
                        ]
                    },
                    'networkInterface': {
                        'subnetId': 'string',
                        'networkInterfaceId': 'string'
                    },
                    'encryptionKey': 'string',
                    'exportedEnvironmentVariables': [
                        {
                            'name': 'string',
                            'value': 'string'
                        },
                    ],
                    'reportArns': [
                        'string',
                    ]
                }
            }
          **Response Structure**

          - *(dict) --*

            - **build** *(dict) --*

              Information about the build.

              - **id** *(string) --*

                The unique ID for the build.

              - **arn** *(string) --*

                The Amazon Resource Name (ARN) of the build.

              - **buildNumber** *(integer) --*

                The number of the build. For each project, the ``buildNumber`` of its first build is
                ``1`` . The ``buildNumber`` of each subsequent build is incremented by ``1`` . If a
                build is deleted, the ``buildNumber`` of other builds does not change.

              - **startTime** *(datetime) --*

                When the build process started, expressed in Unix time format.

              - **endTime** *(datetime) --*

                When the build process ended, expressed in Unix time format.

              - **currentPhase** *(string) --*

                The current build phase.

              - **buildStatus** *(string) --*

                The current status of the build. Valid values include:

                * ``FAILED`` : The build failed.

                * ``FAULT`` : The build faulted.

                * ``IN_PROGRESS`` : The build is still in progress.

                * ``STOPPED`` : The build stopped.

                * ``SUCCEEDED`` : The build succeeded.

                * ``TIMED_OUT`` : The build timed out.

              - **sourceVersion** *(string) --*

                Any version identifier for the version of the source code to be built. If
                ``sourceVersion`` is specified at the project level, then this ``sourceVersion`` (at
                the build level) takes precedence.

                For more information, see `Source Version Sample with CodeBuild
                <https://docs.aws.amazon.com/codebuild/latest/userguide/sample-source-version.html>`__
                in the *AWS CodeBuild User Guide* .

              - **resolvedSourceVersion** *(string) --*

                An identifier for the version of this build's source code.

                * For AWS CodeCommit, GitHub, GitHub Enterprise, and BitBucket, the commit ID.

                * For AWS CodePipeline, the source revision provided by AWS CodePipeline.

                * For Amazon Simple Storage Service (Amazon S3), this does not apply.

              - **projectName** *(string) --*

                The name of the AWS CodeBuild project.

              - **phases** *(list) --*

                Information about all previous build phases that are complete and information about
                any current build phase that is not yet complete.

                - *(dict) --*

                  Information about a stage for a build.

                  - **phaseType** *(string) --*

                    The name of the build phase. Valid values include:

                    * ``BUILD`` : Core build activities typically occur in this build phase.

                    * ``COMPLETED`` : The build has been completed.

                    * ``DOWNLOAD_SOURCE`` : Source code is being downloaded in this build phase.

                    * ``FINALIZING`` : The build process is completing in this build phase.

                    * ``INSTALL`` : Installation activities typically occur in this build phase.

                    * ``POST_BUILD`` : Post-build activities typically occur in this build phase.

                    * ``PRE_BUILD`` : Pre-build activities typically occur in this build phase.

                    * ``PROVISIONING`` : The build environment is being set up.

                    * ``QUEUED`` : The build has been submitted and is queued behind other submitted
                    builds.

                    * ``SUBMITTED`` : The build has been submitted.

                    * ``UPLOAD_ARTIFACTS`` : Build output artifacts are being uploaded to the output
                    location.

                  - **phaseStatus** *(string) --*

                    The current status of the build phase. Valid values include:

                    * ``FAILED`` : The build phase failed.

                    * ``FAULT`` : The build phase faulted.

                    * ``IN_PROGRESS`` : The build phase is still in progress.

                    * ``QUEUED`` : The build has been submitted and is queued behind other submitted
                    builds.

                    * ``STOPPED`` : The build phase stopped.

                    * ``SUCCEEDED`` : The build phase succeeded.

                    * ``TIMED_OUT`` : The build phase timed out.

                  - **startTime** *(datetime) --*

                    When the build phase started, expressed in Unix time format.

                  - **endTime** *(datetime) --*

                    When the build phase ended, expressed in Unix time format.

                  - **durationInSeconds** *(integer) --*

                    How long, in seconds, between the starting and ending times of the build's
                    phase.

                  - **contexts** *(list) --*

                    Additional information about a build phase, especially to help troubleshoot a
                    failed build.

                    - *(dict) --*

                      Additional information about a build phase that has an error. You can use this
                      information for troubleshooting.

                      - **statusCode** *(string) --*

                        The status code for the context of the build phase.

                      - **message** *(string) --*

                        An explanation of the build phase's context. This might include a command ID
                        and an exit code.

              - **source** *(dict) --*

                Information about the source code to be built.

                - **type** *(string) --*

                  The type of repository that contains the source code to be built. Valid values
                  include:

                  * ``BITBUCKET`` : The source code is in a Bitbucket repository.

                  * ``CODECOMMIT`` : The source code is in an AWS CodeCommit repository.

                  * ``CODEPIPELINE`` : The source code settings are specified in the source action
                  of a pipeline in AWS CodePipeline.

                  * ``GITHUB`` : The source code is in a GitHub repository.

                  * ``GITHUB_ENTERPRISE`` : The source code is in a GitHub Enterprise repository.

                  * ``NO_SOURCE`` : The project does not have input source code.

                  * ``S3`` : The source code is in an Amazon Simple Storage Service (Amazon S3)
                  input bucket.

                - **location** *(string) --*

                  Information about the location of the source code to be built. Valid values
                  include:

                  * For source code settings that are specified in the source action of a pipeline
                  in AWS CodePipeline, ``location`` should not be specified. If it is specified, AWS
                  CodePipeline ignores it. This is because AWS CodePipeline uses the settings in a
                  pipeline's source action instead of this value.

                  * For source code in an AWS CodeCommit repository, the HTTPS clone URL to the
                  repository that contains the source code and the build spec (for example,
                  ``https://git-codecommit.*region-ID* .amazonaws.com/v1/repos/*repo-name* `` ).

                  * For source code in an Amazon Simple Storage Service (Amazon S3) input bucket,
                  one of the following.

                    * The path to the ZIP file that contains the source code (for example, ``
                    *bucket-name* /*path* /*to* /*object-name* .zip`` ).

                    * The path to the folder that contains the source code (for example, ``
                    *bucket-name* /*path* /*to* /*source-code* /*folder* /`` ).

                  * For source code in a GitHub repository, the HTTPS clone URL to the repository
                  that contains the source and the build spec. You must connect your AWS account to
                  your GitHub account. Use the AWS CodeBuild console to start creating a build
                  project. When you use the console to connect (or reconnect) with GitHub, on the
                  GitHub **Authorize application** page, for **Organization access** , choose
                  **Request access** next to each repository you want to allow AWS CodeBuild to have
                  access to, and then choose **Authorize application** . (After you have connected
                  to your GitHub account, you do not need to finish creating the build project. You
                  can leave the AWS CodeBuild console.) To instruct AWS CodeBuild to use this
                  connection, in the ``source`` object, set the ``auth`` object's ``type`` value to
                  ``OAUTH`` .

                  * For source code in a Bitbucket repository, the HTTPS clone URL to the repository
                  that contains the source and the build spec. You must connect your AWS account to
                  your Bitbucket account. Use the AWS CodeBuild console to start creating a build
                  project. When you use the console to connect (or reconnect) with Bitbucket, on the
                  Bitbucket **Confirm access to your account** page, choose **Grant access** .
                  (After you have connected to your Bitbucket account, you do not need to finish
                  creating the build project. You can leave the AWS CodeBuild console.) To instruct
                  AWS CodeBuild to use this connection, in the ``source`` object, set the ``auth``
                  object's ``type`` value to ``OAUTH`` .

                - **gitCloneDepth** *(integer) --*

                  Information about the Git clone depth for the build project.

                - **gitSubmodulesConfig** *(dict) --*

                  Information about the Git submodules configuration for the build project.

                  - **fetchSubmodules** *(boolean) --*

                    Set to true to fetch Git submodules for your AWS CodeBuild build project.

                - **buildspec** *(string) --*

                  The build spec declaration to use for the builds in this build project.

                  If this value is not specified, a build spec must be included along with the
                  source code to be built.

                - **auth** *(dict) --*

                  Information about the authorization settings for AWS CodeBuild to access the
                  source code to be built.

                  This information is for the AWS CodeBuild console's use only. Your code should not
                  get or set this information directly.

                  - **type** *(string) --*

                    .. note::

                      This data type is deprecated and is no longer accurate or used.

                    The authorization type to use. The only valid value is ``OAUTH`` , which
                    represents the OAuth authorization type.

                  - **resource** *(string) --*

                    The resource value that applies to the specified authorization type.

                - **reportBuildStatus** *(boolean) --*

                  Set to true to report the status of a build's start and finish to your source
                  provider. This option is valid only when your source provider is GitHub, GitHub
                  Enterprise, or Bitbucket. If this is set and you use a different source provider,
                  an invalidInputException is thrown.

                  .. note::

                    The status of a build triggered by a webhook is always reported to your source
                    provider.

                - **insecureSsl** *(boolean) --*

                  Enable this flag to ignore SSL warnings while connecting to the project source
                  code.

                - **sourceIdentifier** *(string) --*

                  An identifier for this project source.

              - **secondarySources** *(list) --*

                An array of ``ProjectSource`` objects.

                - *(dict) --*

                  Information about the build input source code for the build project.

                  - **type** *(string) --*

                    The type of repository that contains the source code to be built. Valid values
                    include:

                    * ``BITBUCKET`` : The source code is in a Bitbucket repository.

                    * ``CODECOMMIT`` : The source code is in an AWS CodeCommit repository.

                    * ``CODEPIPELINE`` : The source code settings are specified in the source action
                    of a pipeline in AWS CodePipeline.

                    * ``GITHUB`` : The source code is in a GitHub repository.

                    * ``GITHUB_ENTERPRISE`` : The source code is in a GitHub Enterprise repository.

                    * ``NO_SOURCE`` : The project does not have input source code.

                    * ``S3`` : The source code is in an Amazon Simple Storage Service (Amazon S3)
                    input bucket.

                  - **location** *(string) --*

                    Information about the location of the source code to be built. Valid values
                    include:

                    * For source code settings that are specified in the source action of a pipeline
                    in AWS CodePipeline, ``location`` should not be specified. If it is specified,
                    AWS CodePipeline ignores it. This is because AWS CodePipeline uses the settings
                    in a pipeline's source action instead of this value.

                    * For source code in an AWS CodeCommit repository, the HTTPS clone URL to the
                    repository that contains the source code and the build spec (for example,
                    ``https://git-codecommit.*region-ID* .amazonaws.com/v1/repos/*repo-name* `` ).

                    * For source code in an Amazon Simple Storage Service (Amazon S3) input bucket,
                    one of the following.

                      * The path to the ZIP file that contains the source code (for example, ``
                      *bucket-name* /*path* /*to* /*object-name* .zip`` ).

                      * The path to the folder that contains the source code (for example, ``
                      *bucket-name* /*path* /*to* /*source-code* /*folder* /`` ).

                    * For source code in a GitHub repository, the HTTPS clone URL to the repository
                    that contains the source and the build spec. You must connect your AWS account
                    to your GitHub account. Use the AWS CodeBuild console to start creating a build
                    project. When you use the console to connect (or reconnect) with GitHub, on the
                    GitHub **Authorize application** page, for **Organization access** , choose
                    **Request access** next to each repository you want to allow AWS CodeBuild to
                    have access to, and then choose **Authorize application** . (After you have
                    connected to your GitHub account, you do not need to finish creating the build
                    project. You can leave the AWS CodeBuild console.) To instruct AWS CodeBuild to
                    use this connection, in the ``source`` object, set the ``auth`` object's
                    ``type`` value to ``OAUTH`` .

                    * For source code in a Bitbucket repository, the HTTPS clone URL to the
                    repository that contains the source and the build spec. You must connect your
                    AWS account to your Bitbucket account. Use the AWS CodeBuild console to start
                    creating a build project. When you use the console to connect (or reconnect)
                    with Bitbucket, on the Bitbucket **Confirm access to your account** page, choose
                    **Grant access** . (After you have connected to your Bitbucket account, you do
                    not need to finish creating the build project. You can leave the AWS CodeBuild
                    console.) To instruct AWS CodeBuild to use this connection, in the ``source``
                    object, set the ``auth`` object's ``type`` value to ``OAUTH`` .

                  - **gitCloneDepth** *(integer) --*

                    Information about the Git clone depth for the build project.

                  - **gitSubmodulesConfig** *(dict) --*

                    Information about the Git submodules configuration for the build project.

                    - **fetchSubmodules** *(boolean) --*

                      Set to true to fetch Git submodules for your AWS CodeBuild build project.

                  - **buildspec** *(string) --*

                    The build spec declaration to use for the builds in this build project.

                    If this value is not specified, a build spec must be included along with the
                    source code to be built.

                  - **auth** *(dict) --*

                    Information about the authorization settings for AWS CodeBuild to access the
                    source code to be built.

                    This information is for the AWS CodeBuild console's use only. Your code should
                    not get or set this information directly.

                    - **type** *(string) --*

                      .. note::

                        This data type is deprecated and is no longer accurate or used.

                      The authorization type to use. The only valid value is ``OAUTH`` , which
                      represents the OAuth authorization type.

                    - **resource** *(string) --*

                      The resource value that applies to the specified authorization type.

                  - **reportBuildStatus** *(boolean) --*

                    Set to true to report the status of a build's start and finish to your source
                    provider. This option is valid only when your source provider is GitHub, GitHub
                    Enterprise, or Bitbucket. If this is set and you use a different source
                    provider, an invalidInputException is thrown.

                    .. note::

                      The status of a build triggered by a webhook is always reported to your source
                      provider.

                  - **insecureSsl** *(boolean) --*

                    Enable this flag to ignore SSL warnings while connecting to the project source
                    code.

                  - **sourceIdentifier** *(string) --*

                    An identifier for this project source.

              - **secondarySourceVersions** *(list) --*

                An array of ``ProjectSourceVersion`` objects. Each ``ProjectSourceVersion`` must be
                one of:

                * For AWS CodeCommit: the commit ID, branch, or Git tag to use.

                * For GitHub: the commit ID, pull request ID, branch name, or tag name that
                corresponds to the version of the source code you want to build. If a pull request
                ID is specified, it must use the format ``pr/pull-request-ID`` (for example,
                ``pr/25`` ). If a branch name is specified, the branch's HEAD commit ID is used. If
                not specified, the default branch's HEAD commit ID is used.

                * For Bitbucket: the commit ID, branch name, or tag name that corresponds to the
                version of the source code you want to build. If a branch name is specified, the
                branch's HEAD commit ID is used. If not specified, the default branch's HEAD commit
                ID is used.

                * For Amazon Simple Storage Service (Amazon S3): the version ID of the object that
                represents the build input ZIP file to use.

                - *(dict) --*

                  A source identifier and its corresponding version.

                  - **sourceIdentifier** *(string) --*

                    An identifier for a source in the build project.

                  - **sourceVersion** *(string) --*

                    The source version for the corresponding source identifier. If specified, must
                    be one of:

                    * For AWS CodeCommit: the commit ID, branch, or Git tag to use.

                    * For GitHub: the commit ID, pull request ID, branch name, or tag name that
                    corresponds to the version of the source code you want to build. If a pull
                    request ID is specified, it must use the format ``pr/pull-request-ID`` (for
                    example, ``pr/25`` ). If a branch name is specified, the branch's HEAD commit ID
                    is used. If not specified, the default branch's HEAD commit ID is used.

                    * For Bitbucket: the commit ID, branch name, or tag name that corresponds to the
                    version of the source code you want to build. If a branch name is specified, the
                    branch's HEAD commit ID is used. If not specified, the default branch's HEAD
                    commit ID is used.

                    * For Amazon Simple Storage Service (Amazon S3): the version ID of the object
                    that represents the build input ZIP file to use.

                    For more information, see `Source Version Sample with CodeBuild
                    <https://docs.aws.amazon.com/codebuild/latest/userguide/sample-source-version.html>`__
                    in the *AWS CodeBuild User Guide* .

              - **artifacts** *(dict) --*

                Information about the output artifacts for the build.

                - **location** *(string) --*

                  Information about the location of the build artifacts.

                - **sha256sum** *(string) --*

                  The SHA-256 hash of the build artifact.

                  You can use this hash along with a checksum tool to confirm file integrity and
                  authenticity.

                  .. note::

                    This value is available only if the build project's ``packaging`` value is set
                    to ``ZIP`` .

                - **md5sum** *(string) --*

                  The MD5 hash of the build artifact.

                  You can use this hash along with a checksum tool to confirm file integrity and
                  authenticity.

                  .. note::

                    This value is available only if the build project's ``packaging`` value is set
                    to ``ZIP`` .

                - **overrideArtifactName** *(boolean) --*

                  If this flag is set, a name specified in the build spec file overrides the
                  artifact name. The name specified in a build spec file is calculated at build time
                  and uses the Shell Command Language. For example, you can append a date and time
                  to your artifact name so that it is always unique.

                - **encryptionDisabled** *(boolean) --*

                  Information that tells you if encryption for build artifacts is disabled.

                - **artifactIdentifier** *(string) --*

                  An identifier for this artifact definition.

              - **secondaryArtifacts** *(list) --*

                An array of ``ProjectArtifacts`` objects.

                - *(dict) --*

                  Information about build output artifacts.

                  - **location** *(string) --*

                    Information about the location of the build artifacts.

                  - **sha256sum** *(string) --*

                    The SHA-256 hash of the build artifact.

                    You can use this hash along with a checksum tool to confirm file integrity and
                    authenticity.

                    .. note::

                      This value is available only if the build project's ``packaging`` value is set
                      to ``ZIP`` .

                  - **md5sum** *(string) --*

                    The MD5 hash of the build artifact.

                    You can use this hash along with a checksum tool to confirm file integrity and
                    authenticity.

                    .. note::

                      This value is available only if the build project's ``packaging`` value is set
                      to ``ZIP`` .

                  - **overrideArtifactName** *(boolean) --*

                    If this flag is set, a name specified in the build spec file overrides the
                    artifact name. The name specified in a build spec file is calculated at build
                    time and uses the Shell Command Language. For example, you can append a date and
                    time to your artifact name so that it is always unique.

                  - **encryptionDisabled** *(boolean) --*

                    Information that tells you if encryption for build artifacts is disabled.

                  - **artifactIdentifier** *(string) --*

                    An identifier for this artifact definition.

              - **cache** *(dict) --*

                Information about the cache for the build.

                - **type** *(string) --*

                  The type of cache used by the build project. Valid values include:

                  * ``NO_CACHE`` : The build project does not use any cache.

                  * ``S3`` : The build project reads and writes from and to S3.

                  * ``LOCAL`` : The build project stores a cache locally on a build host that is
                  only available to that build host.

                - **location** *(string) --*

                  Information about the cache location:

                  * ``NO_CACHE`` or ``LOCAL`` : This value is ignored.

                  * ``S3`` : This is the S3 bucket name/prefix.

                - **modes** *(list) --*

                  If you use a ``LOCAL`` cache, the local cache mode. You can use one or more local
                  cache modes at the same time.

                  * ``LOCAL_SOURCE_CACHE`` mode caches Git metadata for primary and secondary
                  sources. After the cache is created, subsequent builds pull only the change
                  between commits. This mode is a good choice for projects with a clean working
                  directory and a source that is a large Git repository. If you choose this option
                  and your project does not use a Git repository (GitHub, GitHub Enterprise, or
                  Bitbucket), the option is ignored.

                  * ``LOCAL_DOCKER_LAYER_CACHE`` mode caches existing Docker layers. This mode is a
                  good choice for projects that build or pull large Docker images. It can prevent
                  the performance issues caused by pulling large Docker images down from the
                  network.

                  .. note::

                      * You can use a Docker layer cache in the Linux environment only.

                      * The ``privileged`` flag must be set so that your project has the required
                      Docker permissions.

                      * You should consider the security implications before you use a Docker layer
                      cache.

                  * ``LOCAL_CUSTOM_CACHE`` mode caches directories you specify in the buildspec
                  file. This mode is a good choice if your build scenario is not suited to one of
                  the other three local cache modes. If you use a custom cache:

                    * Only directories can be specified for caching. You cannot specify individual
                    files.

                    * Symlinks are used to reference cached directories.

                    * Cached directories are linked to your build before it downloads its project
                    sources. Cached items are overridden if a source item has the same name.
                    Directories are specified using cache paths in the buildspec file.

                  - *(string) --*

              - **environment** *(dict) --*

                Information about the build environment for this build.

                - **type** *(string) --*

                  The type of build environment to use for related builds.

                  * The environment type ``ARM_CONTAINER`` is available only in regions US East (N.
                  Virginia), US East (Ohio), US West (Oregon), EU (Ireland), Asia Pacific (Mumbai),
                  Asia Pacific (Tokyo), Asia Pacific (Sydney), and EU (Frankfurt).

                  * The environment type ``LINUX_CONTAINER`` with compute type
                  ``build.general1.2xlarge`` is available only in regions US East (N. Virginia), US
                  East (N. Virginia), US West (Oregon), Canada (Central), EU (Ireland), EU (London),
                  EU (Frankfurt), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific
                  (Singapore), Asia Pacific (Sydney), China (Beijing), and China (Ningxia).

                  * The environment type ``LINUX_GPU_CONTAINER`` is available only in regions US
                  East (N. Virginia), US East (N. Virginia), US West (Oregon), Canada (Central), EU
                  (Ireland), EU (London), EU (Frankfurt), Asia Pacific (Tokyo), Asia Pacific
                  (Seoul), Asia Pacific (Singapore), Asia Pacific (Sydney) , China (Beijing), and
                  China (Ningxia).

                - **image** *(string) --*

                  The image tag or image digest that identifies the Docker image to use for this
                  build project. Use the following formats:

                  * For an image tag: ``registry/repository:tag`` . For example, to specify an image
                  with the tag "latest," use ``registry/repository:latest`` .

                  * For an image digest: ``registry/repository@digest`` . For example, to specify an
                  image with the digest
                  "sha256:cbbf2f9a99b47fc460d422812b6a5adff7dfee951d8fa2e4a98caa0382cfbdbf," use
                  ``registry/repository@sha256:cbbf2f9a99b47fc460d422812b6a5adff7dfee951d8fa2e4a98caa0382cfbdbf``
                  .

                - **computeType** *(string) --*

                  Information about the compute resources the build project uses. Available values
                  include:

                  * ``BUILD_GENERAL1_SMALL`` : Use up to 3 GB memory and 2 vCPUs for builds.

                  * ``BUILD_GENERAL1_MEDIUM`` : Use up to 7 GB memory and 4 vCPUs for builds.

                  * ``BUILD_GENERAL1_LARGE`` : Use up to 16 GB memory and 8 vCPUs for builds,
                  depending on your environment type.

                  * ``BUILD_GENERAL1_2XLARGE`` : Use up to 145 GB memory, 72 vCPUs, and 824 GB of
                  SSD storage for builds. This compute type supports Docker images up to 100 GB
                  uncompressed.

                  If you use ``BUILD_GENERAL1_LARGE`` :

                  * For environment type ``LINUX_CONTAINER`` , you can use up to 15 GB memory and 8
                  vCPUs for builds.

                  * For environment type ``LINUX_GPU_CONTAINER`` , you can use up to 255 GB memory,
                  32 vCPUs, and 4 NVIDIA Tesla V100 GPUs for builds.

                  * For environment type ``ARM_CONTAINER`` , you can use up to 16 GB memory and 8
                  vCPUs on ARM-based processors for builds.

                  For more information, see `Build Environment Compute Types
                  <https://docs.aws.amazon.com/codebuild/latest/userguide/build-env-ref-compute-types.html>`__
                  in the *AWS CodeBuild User Guide.*

                - **environmentVariables** *(list) --*

                  A set of environment variables to make available to builds for this build project.

                  - *(dict) --*

                    Information about an environment variable for a build project or a build.

                    - **name** *(string) --*

                      The name or key of the environment variable.

                    - **value** *(string) --*

                      The value of the environment variable.

                      .. warning::

                        We strongly discourage the use of environment variables to store sensitive
                        values, especially AWS secret key IDs and secret access keys. Environment
                        variables can be displayed in plain text using the AWS CodeBuild console and
                        the AWS Command Line Interface (AWS CLI).

                    - **type** *(string) --*

                      The type of environment variable. Valid values include:

                      * ``PARAMETER_STORE`` : An environment variable stored in Amazon EC2 Systems
                      Manager Parameter Store.

                      * ``PLAINTEXT`` : An environment variable in plain text format.

                      * ``SECRETS_MANAGER`` : An environment variable stored in AWS Secrets Manager.

                - **privilegedMode** *(boolean) --*

                  Enables running the Docker daemon inside a Docker container. Set to true only if
                  the build project is used to build Docker images. Otherwise, a build that attempts
                  to interact with the Docker daemon fails. The default setting is ``false`` .

                  You can initialize the Docker daemon during the install phase of your build by
                  adding one of the following sets of commands to the install phase of your
                  buildspec file:

                  If the operating system's base image is Ubuntu Linux:

                   ``- nohup /usr/local/bin/dockerd --host=unix:///var/run/docker.sock
                   --host=tcp://0.0.0.0:2375 --storage-driver=overlay&``

                   ``- timeout 15 sh -c "until docker info; do echo .; sleep 1; done"``

                  If the operating system's base image is Alpine Linux and the previous command does
                  not work, add the ``-t`` argument to ``timeout`` :

                   ``- nohup /usr/local/bin/dockerd --host=unix:///var/run/docker.sock
                   --host=tcp://0.0.0.0:2375 --storage-driver=overlay&``

                   ``- timeout -t 15 sh -c "until docker info; do echo .; sleep 1; done"``

                - **certificate** *(string) --*

                  The certificate to use with this build project.

                - **registryCredential** *(dict) --*

                  The credentials for access to a private registry.

                  - **credential** *(string) --*

                    The Amazon Resource Name (ARN) or name of credentials created using AWS Secrets
                    Manager.

                    .. note::

                      The ``credential`` can use the name of the credentials only if they exist in
                      your current region.

                  - **credentialProvider** *(string) --*

                    The service that created the credentials to access a private Docker registry.
                    The valid value, SECRETS_MANAGER, is for AWS Secrets Manager.

                - **imagePullCredentialsType** *(string) --*

                  The type of credentials AWS CodeBuild uses to pull images in your build. There are
                  two valid values:

                  * ``CODEBUILD`` specifies that AWS CodeBuild uses its own credentials. This
                  requires that you modify your ECR repository policy to trust AWS CodeBuild's
                  service principal.

                  * ``SERVICE_ROLE`` specifies that AWS CodeBuild uses your build project's service
                  role.

                  When you use a cross-account or private registry image, you must use SERVICE_ROLE
                  credentials. When you use an AWS CodeBuild curated image, you must use CODEBUILD
                  credentials.

              - **serviceRole** *(string) --*

                The name of a service role used for this build.

              - **logs** *(dict) --*

                Information about the build's logs in Amazon CloudWatch Logs.

                - **groupName** *(string) --*

                  The name of the Amazon CloudWatch Logs group for the build logs.

                - **streamName** *(string) --*

                  The name of the Amazon CloudWatch Logs stream for the build logs.

                - **deepLink** *(string) --*

                  The URL to an individual build log in Amazon CloudWatch Logs.

                - **s3DeepLink** *(string) --*

                  The URL to a build log in an S3 bucket.

                - **cloudWatchLogsArn** *(string) --*

                  The ARN of Amazon CloudWatch Logs for a build project. Its format is
                  ``arn:${Partition}:logs:${Region}:${Account}:log-group:${LogGroupName}:log-stream:${LogStreamName}``
                  . For more information, see `Resources Defined by Amazon CloudWatch Logs
                  <https://docs.aws.amazon.com/IAM/latest/UserGuide/list_amazoncloudwatchlogs.html#amazoncloudwatchlogs-resources-for-iam-policies>`__
                  .

                - **s3LogsArn** *(string) --*

                  The ARN of S3 logs for a build project. Its format is
                  ``arn:${Partition}:s3:::${BucketName}/${ObjectName}`` . For more information, see
                  `Resources Defined by Amazon S3
                  <https://docs.aws.amazon.com/IAM/latest/UserGuide/list_amazons3.html#amazons3-resources-for-iam-policies>`__
                  .

                - **cloudWatchLogs** *(dict) --*

                  Information about Amazon CloudWatch Logs for a build project.

                  - **status** *(string) --*

                    The current status of the logs in Amazon CloudWatch Logs for a build project.
                    Valid values are:

                    * ``ENABLED`` : Amazon CloudWatch Logs are enabled for this build project.

                    * ``DISABLED`` : Amazon CloudWatch Logs are not enabled for this build project.

                  - **groupName** *(string) --*

                    The group name of the logs in Amazon CloudWatch Logs. For more information, see
                    `Working with Log Groups and Log Streams
                    <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html>`__
                    .

                  - **streamName** *(string) --*

                    The prefix of the stream name of the Amazon CloudWatch Logs. For more
                    information, see `Working with Log Groups and Log Streams
                    <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html>`__
                    .

                - **s3Logs** *(dict) --*

                  Information about S3 logs for a build project.

                  - **status** *(string) --*

                    The current status of the S3 build logs. Valid values are:

                    * ``ENABLED`` : S3 build logs are enabled for this build project.

                    * ``DISABLED`` : S3 build logs are not enabled for this build project.

                  - **location** *(string) --*

                    The ARN of an S3 bucket and the path prefix for S3 logs. If your Amazon S3
                    bucket name is ``my-bucket`` , and your path prefix is ``build-log`` , then
                    acceptable formats are ``my-bucket/build-log`` or
                    ``arn:aws:s3:::my-bucket/build-log`` .

                  - **encryptionDisabled** *(boolean) --*

                    Set to true if you do not want your S3 build log output encrypted. By default S3
                    build logs are encrypted.

              - **timeoutInMinutes** *(integer) --*

                How long, in minutes, for AWS CodeBuild to wait before timing out this build if it
                does not get marked as completed.

              - **queuedTimeoutInMinutes** *(integer) --*

                The number of minutes a build is allowed to be queued before it times out.

              - **buildComplete** *(boolean) --*

                Whether the build is complete. True if complete; otherwise, false.

              - **initiator** *(string) --*

                The entity that started the build. Valid values include:

                * If AWS CodePipeline started the build, the pipeline's name (for example,
                ``codepipeline/my-demo-pipeline`` ).

                * If an AWS Identity and Access Management (IAM) user started the build, the user's
                name (for example, ``MyUserName`` ).

                * If the Jenkins plugin for AWS CodeBuild started the build, the string
                ``CodeBuild-Jenkins-Plugin`` .

              - **vpcConfig** *(dict) --*

                If your AWS CodeBuild project accesses resources in an Amazon VPC, you provide this
                parameter that identifies the VPC ID and the list of security group IDs and subnet
                IDs. The security groups and subnets must belong to the same VPC. You must provide
                at least one security group and one subnet ID.

                - **vpcId** *(string) --*

                  The ID of the Amazon VPC.

                - **subnets** *(list) --*

                  A list of one or more subnet IDs in your Amazon VPC.

                  - *(string) --*

                - **securityGroupIds** *(list) --*

                  A list of one or more security groups IDs in your Amazon VPC.

                  - *(string) --*

              - **networkInterface** *(dict) --*

                Describes a network interface.

                - **subnetId** *(string) --*

                  The ID of the subnet.

                - **networkInterfaceId** *(string) --*

                  The ID of the network interface.

              - **encryptionKey** *(string) --*

                The AWS Key Management Service (AWS KMS) customer master key (CMK) to be used for
                encrypting the build output artifacts.

                .. note::

                  You can use a cross-account KMS key to encrypt the build output artifacts if your
                  service role has permission to that key.

                You can specify either the Amazon Resource Name (ARN) of the CMK or, if available,
                the CMK's alias (using the format ``alias/*alias-name* `` ).

              - **exportedEnvironmentVariables** *(list) --*

                A list of exported environment variables for this build.

                - *(dict) --*

                  Information about an exported environment variable.

                  - **name** *(string) --*

                    The name of this exported environment variable.

                  - **value** *(string) --*

                    The value assigned to this exported environment variable.

                    .. note::

                      During a build, the value of a variable is available starting with the
                      ``install`` phase. It can be updated between the start of the ``install``
                      phase and the end of the ``post_build`` phase. After the ``post_build`` phase
                      ends, the value of exported variables cannot change.

              - **reportArns** *(list) --*

                An array of the ARNs associated with this build's reports.

                - *(string) --*
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_project(
        self,
        name: str,
        description: str = None,
        source: ClientUpdateProjectSourceTypeDef = None,
        secondarySources: List[ClientUpdateProjectSecondarySourcesTypeDef] = None,
        sourceVersion: str = None,
        secondarySourceVersions: List[ClientUpdateProjectSecondarySourceVersionsTypeDef] = None,
        artifacts: ClientUpdateProjectArtifactsTypeDef = None,
        secondaryArtifacts: List[ClientUpdateProjectSecondaryArtifactsTypeDef] = None,
        cache: ClientUpdateProjectCacheTypeDef = None,
        environment: ClientUpdateProjectEnvironmentTypeDef = None,
        serviceRole: str = None,
        timeoutInMinutes: int = None,
        queuedTimeoutInMinutes: int = None,
        encryptionKey: str = None,
        tags: List[ClientUpdateProjectTagsTypeDef] = None,
        vpcConfig: ClientUpdateProjectVpcConfigTypeDef = None,
        badgeEnabled: bool = None,
        logsConfig: ClientUpdateProjectLogsConfigTypeDef = None,
    ) -> ClientUpdateProjectResponseTypeDef:
        """
        Changes the settings of a build project.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/codebuild-2016-10-06/UpdateProject>`_

        **Request Syntax**
        ::

          response = client.update_project(
              name='string',
              description='string',
              source={
                  'type':
                  'CODECOMMIT'|'CODEPIPELINE'|'GITHUB'|'S3'|'BITBUCKET'
                  |'GITHUB_ENTERPRISE'|'NO_SOURCE',
                  'location': 'string',
                  'gitCloneDepth': 123,
                  'gitSubmodulesConfig': {
                      'fetchSubmodules': True|False
                  },
                  'buildspec': 'string',
                  'auth': {
                      'type': 'OAUTH',
                      'resource': 'string'
                  },
                  'reportBuildStatus': True|False,
                  'insecureSsl': True|False,
                  'sourceIdentifier': 'string'
              },
              secondarySources=[
                  {
                      'type':
                      'CODECOMMIT'|'CODEPIPELINE'|'GITHUB'|'S3'|'BITBUCKET'
                      |'GITHUB_ENTERPRISE'|'NO_SOURCE',
                      'location': 'string',
                      'gitCloneDepth': 123,
                      'gitSubmodulesConfig': {
                          'fetchSubmodules': True|False
                      },
                      'buildspec': 'string',
                      'auth': {
                          'type': 'OAUTH',
                          'resource': 'string'
                      },
                      'reportBuildStatus': True|False,
                      'insecureSsl': True|False,
                      'sourceIdentifier': 'string'
                  },
              ],
              sourceVersion='string',
              secondarySourceVersions=[
                  {
                      'sourceIdentifier': 'string',
                      'sourceVersion': 'string'
                  },
              ],
              artifacts={
                  'type': 'CODEPIPELINE'|'S3'|'NO_ARTIFACTS',
                  'location': 'string',
                  'path': 'string',
                  'namespaceType': 'NONE'|'BUILD_ID',
                  'name': 'string',
                  'packaging': 'NONE'|'ZIP',
                  'overrideArtifactName': True|False,
                  'encryptionDisabled': True|False,
                  'artifactIdentifier': 'string'
              },
              secondaryArtifacts=[
                  {
                      'type': 'CODEPIPELINE'|'S3'|'NO_ARTIFACTS',
                      'location': 'string',
                      'path': 'string',
                      'namespaceType': 'NONE'|'BUILD_ID',
                      'name': 'string',
                      'packaging': 'NONE'|'ZIP',
                      'overrideArtifactName': True|False,
                      'encryptionDisabled': True|False,
                      'artifactIdentifier': 'string'
                  },
              ],
              cache={
                  'type': 'NO_CACHE'|'S3'|'LOCAL',
                  'location': 'string',
                  'modes': [
                      'LOCAL_DOCKER_LAYER_CACHE'|'LOCAL_SOURCE_CACHE'|'LOCAL_CUSTOM_CACHE',
                  ]
              },
              environment={
                  'type':
                  'WINDOWS_CONTAINER'|'LINUX_CONTAINER'|'LINUX_GPU_CONTAINER'
                  |'ARM_CONTAINER',
                  'image': 'string',
                  'computeType':
                  'BUILD_GENERAL1_SMALL'|'BUILD_GENERAL1_MEDIUM'|'BUILD_GENERAL1_LARGE'
                  |'BUILD_GENERAL1_2XLARGE',
                  'environmentVariables': [
                      {
                          'name': 'string',
                          'value': 'string',
                          'type': 'PLAINTEXT'|'PARAMETER_STORE'|'SECRETS_MANAGER'
                      },
                  ],
                  'privilegedMode': True|False,
                  'certificate': 'string',
                  'registryCredential': {
                      'credential': 'string',
                      'credentialProvider': 'SECRETS_MANAGER'
                  },
                  'imagePullCredentialsType': 'CODEBUILD'|'SERVICE_ROLE'
              },
              serviceRole='string',
              timeoutInMinutes=123,
              queuedTimeoutInMinutes=123,
              encryptionKey='string',
              tags=[
                  {
                      'key': 'string',
                      'value': 'string'
                  },
              ],
              vpcConfig={
                  'vpcId': 'string',
                  'subnets': [
                      'string',
                  ],
                  'securityGroupIds': [
                      'string',
                  ]
              },
              badgeEnabled=True|False,
              logsConfig={
                  'cloudWatchLogs': {
                      'status': 'ENABLED'|'DISABLED',
                      'groupName': 'string',
                      'streamName': 'string'
                  },
                  's3Logs': {
                      'status': 'ENABLED'|'DISABLED',
                      'location': 'string',
                      'encryptionDisabled': True|False
                  }
              }
          )
        :type name: string
        :param name: **[REQUIRED]**

          The name of the build project.

          .. note::

            You cannot change a build project's name.

        :type description: string
        :param description:

          A new or replacement description of the build project.

        :type source: dict
        :param source:

          Information to be changed about the build input source code for the build project.

          - **type** *(string) --* **[REQUIRED]**

            The type of repository that contains the source code to be built. Valid values include:

            * ``BITBUCKET`` : The source code is in a Bitbucket repository.

            * ``CODECOMMIT`` : The source code is in an AWS CodeCommit repository.

            * ``CODEPIPELINE`` : The source code settings are specified in the source action of a
            pipeline in AWS CodePipeline.

            * ``GITHUB`` : The source code is in a GitHub repository.

            * ``GITHUB_ENTERPRISE`` : The source code is in a GitHub Enterprise repository.

            * ``NO_SOURCE`` : The project does not have input source code.

            * ``S3`` : The source code is in an Amazon Simple Storage Service (Amazon S3) input
            bucket.

          - **location** *(string) --*

            Information about the location of the source code to be built. Valid values include:

            * For source code settings that are specified in the source action of a pipeline in AWS
            CodePipeline, ``location`` should not be specified. If it is specified, AWS CodePipeline
            ignores it. This is because AWS CodePipeline uses the settings in a pipeline's source
            action instead of this value.

            * For source code in an AWS CodeCommit repository, the HTTPS clone URL to the repository
            that contains the source code and the build spec (for example,
            ``https://git-codecommit.*region-ID* .amazonaws.com/v1/repos/*repo-name* `` ).

            * For source code in an Amazon Simple Storage Service (Amazon S3) input bucket, one of
            the following.

              * The path to the ZIP file that contains the source code (for example, ``
              *bucket-name* /*path* /*to* /*object-name* .zip`` ).

              * The path to the folder that contains the source code (for example, `` *bucket-name*
              /*path* /*to* /*source-code* /*folder* /`` ).

            * For source code in a GitHub repository, the HTTPS clone URL to the repository that
            contains the source and the build spec. You must connect your AWS account to your GitHub
            account. Use the AWS CodeBuild console to start creating a build project. When you use
            the console to connect (or reconnect) with GitHub, on the GitHub **Authorize
            application** page, for **Organization access** , choose **Request access** next to each
            repository you want to allow AWS CodeBuild to have access to, and then choose
            **Authorize application** . (After you have connected to your GitHub account, you do not
            need to finish creating the build project. You can leave the AWS CodeBuild console.) To
            instruct AWS CodeBuild to use this connection, in the ``source`` object, set the
            ``auth`` object's ``type`` value to ``OAUTH`` .

            * For source code in a Bitbucket repository, the HTTPS clone URL to the repository that
            contains the source and the build spec. You must connect your AWS account to your
            Bitbucket account. Use the AWS CodeBuild console to start creating a build project. When
            you use the console to connect (or reconnect) with Bitbucket, on the Bitbucket **Confirm
            access to your account** page, choose **Grant access** . (After you have connected to
            your Bitbucket account, you do not need to finish creating the build project. You can
            leave the AWS CodeBuild console.) To instruct AWS CodeBuild to use this connection, in
            the ``source`` object, set the ``auth`` object's ``type`` value to ``OAUTH`` .

          - **gitCloneDepth** *(integer) --*

            Information about the Git clone depth for the build project.

          - **gitSubmodulesConfig** *(dict) --*

            Information about the Git submodules configuration for the build project.

            - **fetchSubmodules** *(boolean) --* **[REQUIRED]**

              Set to true to fetch Git submodules for your AWS CodeBuild build project.

          - **buildspec** *(string) --*

            The build spec declaration to use for the builds in this build project.

            If this value is not specified, a build spec must be included along with the source code
            to be built.

          - **auth** *(dict) --*

            Information about the authorization settings for AWS CodeBuild to access the source code
            to be built.

            This information is for the AWS CodeBuild console's use only. Your code should not get
            or set this information directly.

            - **type** *(string) --* **[REQUIRED]**

              .. note::

                This data type is deprecated and is no longer accurate or used.

              The authorization type to use. The only valid value is ``OAUTH`` , which represents
              the OAuth authorization type.

            - **resource** *(string) --*

              The resource value that applies to the specified authorization type.

          - **reportBuildStatus** *(boolean) --*

            Set to true to report the status of a build's start and finish to your source provider.
            This option is valid only when your source provider is GitHub, GitHub Enterprise, or
            Bitbucket. If this is set and you use a different source provider, an
            invalidInputException is thrown.

            .. note::

              The status of a build triggered by a webhook is always reported to your source
              provider.

          - **insecureSsl** *(boolean) --*

            Enable this flag to ignore SSL warnings while connecting to the project source code.

          - **sourceIdentifier** *(string) --*

            An identifier for this project source.

        :type secondarySources: list
        :param secondarySources:

          An array of ``ProjectSource`` objects.

          - *(dict) --*

            Information about the build input source code for the build project.

            - **type** *(string) --* **[REQUIRED]**

              The type of repository that contains the source code to be built. Valid values
              include:

              * ``BITBUCKET`` : The source code is in a Bitbucket repository.

              * ``CODECOMMIT`` : The source code is in an AWS CodeCommit repository.

              * ``CODEPIPELINE`` : The source code settings are specified in the source action of a
              pipeline in AWS CodePipeline.

              * ``GITHUB`` : The source code is in a GitHub repository.

              * ``GITHUB_ENTERPRISE`` : The source code is in a GitHub Enterprise repository.

              * ``NO_SOURCE`` : The project does not have input source code.

              * ``S3`` : The source code is in an Amazon Simple Storage Service (Amazon S3) input
              bucket.

            - **location** *(string) --*

              Information about the location of the source code to be built. Valid values include:

              * For source code settings that are specified in the source action of a pipeline in
              AWS CodePipeline, ``location`` should not be specified. If it is specified, AWS
              CodePipeline ignores it. This is because AWS CodePipeline uses the settings in a
              pipeline's source action instead of this value.

              * For source code in an AWS CodeCommit repository, the HTTPS clone URL to the
              repository that contains the source code and the build spec (for example,
              ``https://git-codecommit.*region-ID* .amazonaws.com/v1/repos/*repo-name* `` ).

              * For source code in an Amazon Simple Storage Service (Amazon S3) input bucket, one of
              the following.

                * The path to the ZIP file that contains the source code (for example, ``
                *bucket-name* /*path* /*to* /*object-name* .zip`` ).

                * The path to the folder that contains the source code (for example, ``
                *bucket-name* /*path* /*to* /*source-code* /*folder* /`` ).

              * For source code in a GitHub repository, the HTTPS clone URL to the repository that
              contains the source and the build spec. You must connect your AWS account to your
              GitHub account. Use the AWS CodeBuild console to start creating a build project. When
              you use the console to connect (or reconnect) with GitHub, on the GitHub **Authorize
              application** page, for **Organization access** , choose **Request access** next to
              each repository you want to allow AWS CodeBuild to have access to, and then choose
              **Authorize application** . (After you have connected to your GitHub account, you do
              not need to finish creating the build project. You can leave the AWS CodeBuild
              console.) To instruct AWS CodeBuild to use this connection, in the ``source`` object,
              set the ``auth`` object's ``type`` value to ``OAUTH`` .

              * For source code in a Bitbucket repository, the HTTPS clone URL to the repository
              that contains the source and the build spec. You must connect your AWS account to your
              Bitbucket account. Use the AWS CodeBuild console to start creating a build project.
              When you use the console to connect (or reconnect) with Bitbucket, on the Bitbucket
              **Confirm access to your account** page, choose **Grant access** . (After you have
              connected to your Bitbucket account, you do not need to finish creating the build
              project. You can leave the AWS CodeBuild console.) To instruct AWS CodeBuild to use
              this connection, in the ``source`` object, set the ``auth`` object's ``type`` value to
              ``OAUTH`` .

            - **gitCloneDepth** *(integer) --*

              Information about the Git clone depth for the build project.

            - **gitSubmodulesConfig** *(dict) --*

              Information about the Git submodules configuration for the build project.

              - **fetchSubmodules** *(boolean) --* **[REQUIRED]**

                Set to true to fetch Git submodules for your AWS CodeBuild build project.

            - **buildspec** *(string) --*

              The build spec declaration to use for the builds in this build project.

              If this value is not specified, a build spec must be included along with the source
              code to be built.

            - **auth** *(dict) --*

              Information about the authorization settings for AWS CodeBuild to access the source
              code to be built.

              This information is for the AWS CodeBuild console's use only. Your code should not get
              or set this information directly.

              - **type** *(string) --* **[REQUIRED]**

                .. note::

                  This data type is deprecated and is no longer accurate or used.

                The authorization type to use. The only valid value is ``OAUTH`` , which represents
                the OAuth authorization type.

              - **resource** *(string) --*

                The resource value that applies to the specified authorization type.

            - **reportBuildStatus** *(boolean) --*

              Set to true to report the status of a build's start and finish to your source
              provider. This option is valid only when your source provider is GitHub, GitHub
              Enterprise, or Bitbucket. If this is set and you use a different source provider, an
              invalidInputException is thrown.

              .. note::

                The status of a build triggered by a webhook is always reported to your source
                provider.

            - **insecureSsl** *(boolean) --*

              Enable this flag to ignore SSL warnings while connecting to the project source code.

            - **sourceIdentifier** *(string) --*

              An identifier for this project source.

        :type sourceVersion: string
        :param sourceVersion:

          A version of the build input to be built for this project. If not specified, the latest
          version is used. If specified, it must be one of:

          * For AWS CodeCommit: the commit ID, branch, or Git tag to use.

          * For GitHub: the commit ID, pull request ID, branch name, or tag name that corresponds to
          the version of the source code you want to build. If a pull request ID is specified, it
          must use the format ``pr/pull-request-ID`` (for example ``pr/25`` ). If a branch name is
          specified, the branch's HEAD commit ID is used. If not specified, the default branch's
          HEAD commit ID is used.

          * For Bitbucket: the commit ID, branch name, or tag name that corresponds to the version
          of the source code you want to build. If a branch name is specified, the branch's HEAD
          commit ID is used. If not specified, the default branch's HEAD commit ID is used.

          * For Amazon Simple Storage Service (Amazon S3): the version ID of the object that
          represents the build input ZIP file to use.

          If ``sourceVersion`` is specified at the build level, then that version takes precedence
          over this ``sourceVersion`` (at the project level).

          For more information, see `Source Version Sample with CodeBuild
          <https://docs.aws.amazon.com/codebuild/latest/userguide/sample-source-version.html>`__ in
          the *AWS CodeBuild User Guide* .

        :type secondarySourceVersions: list
        :param secondarySourceVersions:

          An array of ``ProjectSourceVersion`` objects. If ``secondarySourceVersions`` is specified
          at the build level, then they take over these ``secondarySourceVersions`` (at the project
          level).

          - *(dict) --*

            A source identifier and its corresponding version.

            - **sourceIdentifier** *(string) --* **[REQUIRED]**

              An identifier for a source in the build project.

            - **sourceVersion** *(string) --* **[REQUIRED]**

              The source version for the corresponding source identifier. If specified, must be one
              of:

              * For AWS CodeCommit: the commit ID, branch, or Git tag to use.

              * For GitHub: the commit ID, pull request ID, branch name, or tag name that
              corresponds to the version of the source code you want to build. If a pull request ID
              is specified, it must use the format ``pr/pull-request-ID`` (for example, ``pr/25`` ).
              If a branch name is specified, the branch's HEAD commit ID is used. If not specified,
              the default branch's HEAD commit ID is used.

              * For Bitbucket: the commit ID, branch name, or tag name that corresponds to the
              version of the source code you want to build. If a branch name is specified, the
              branch's HEAD commit ID is used. If not specified, the default branch's HEAD commit ID
              is used.

              * For Amazon Simple Storage Service (Amazon S3): the version ID of the object that
              represents the build input ZIP file to use.

              For more information, see `Source Version Sample with CodeBuild
              <https://docs.aws.amazon.com/codebuild/latest/userguide/sample-source-version.html>`__
              in the *AWS CodeBuild User Guide* .

        :type artifacts: dict
        :param artifacts:

          Information to be changed about the build output artifacts for the build project.

          - **type** *(string) --* **[REQUIRED]**

            The type of build output artifact. Valid values include:

            * ``CODEPIPELINE`` : The build project has build output generated through AWS
            CodePipeline.

            .. note::

               The ``CODEPIPELINE`` type is not supported for ``secondaryArtifacts`` .

            * ``NO_ARTIFACTS`` : The build project does not produce any build output.

            * ``S3`` : The build project stores build output in Amazon Simple Storage Service
            (Amazon S3).

          - **location** *(string) --*

            Information about the build output artifact location:

            * If ``type`` is set to ``CODEPIPELINE`` , AWS CodePipeline ignores this value if
            specified. This is because AWS CodePipeline manages its build output locations instead
            of AWS CodeBuild.

            * If ``type`` is set to ``NO_ARTIFACTS`` , this value is ignored if specified, because
            no build output is produced.

            * If ``type`` is set to ``S3`` , this is the name of the output bucket.

          - **path** *(string) --*

            Along with ``namespaceType`` and ``name`` , the pattern that AWS CodeBuild uses to name
            and store the output artifact:

            * If ``type`` is set to ``CODEPIPELINE`` , AWS CodePipeline ignores this value if
            specified. This is because AWS CodePipeline manages its build output names instead of
            AWS CodeBuild.

            * If ``type`` is set to ``NO_ARTIFACTS`` , this value is ignored if specified, because
            no build output is produced.

            * If ``type`` is set to ``S3`` , this is the path to the output artifact. If ``path`` is
            not specified, ``path`` is not used.

            For example, if ``path`` is set to ``MyArtifacts`` , ``namespaceType`` is set to
            ``NONE`` , and ``name`` is set to ``MyArtifact.zip`` , the output artifact is stored in
            the output bucket at ``MyArtifacts/MyArtifact.zip`` .

          - **namespaceType** *(string) --*

            Along with ``path`` and ``name`` , the pattern that AWS CodeBuild uses to determine the
            name and location to store the output artifact:

            * If ``type`` is set to ``CODEPIPELINE`` , AWS CodePipeline ignores this value if
            specified. This is because AWS CodePipeline manages its build output names instead of
            AWS CodeBuild.

            * If ``type`` is set to ``NO_ARTIFACTS`` , this value is ignored if specified, because
            no build output is produced.

            * If ``type`` is set to ``S3`` , valid values include:

              * ``BUILD_ID`` : Include the build ID in the location of the build output artifact.

              * ``NONE`` : Do not include the build ID. This is the default if ``namespaceType`` is
              not specified.

            For example, if ``path`` is set to ``MyArtifacts`` , ``namespaceType`` is set to
            ``BUILD_ID`` , and ``name`` is set to ``MyArtifact.zip`` , the output artifact is stored
            in ``MyArtifacts/*build-ID* /MyArtifact.zip`` .

          - **name** *(string) --*

            Along with ``path`` and ``namespaceType`` , the pattern that AWS CodeBuild uses to name
            and store the output artifact:

            * If ``type`` is set to ``CODEPIPELINE`` , AWS CodePipeline ignores this value if
            specified. This is because AWS CodePipeline manages its build output names instead of
            AWS CodeBuild.

            * If ``type`` is set to ``NO_ARTIFACTS`` , this value is ignored if specified, because
            no build output is produced.

            * If ``type`` is set to ``S3`` , this is the name of the output artifact object. If you
            set the name to be a forward slash ("/"), the artifact is stored in the root of the
            output bucket.

            For example:

            * If ``path`` is set to ``MyArtifacts`` , ``namespaceType`` is set to ``BUILD_ID`` , and
            ``name`` is set to ``MyArtifact.zip`` , then the output artifact is stored in
            ``MyArtifacts/*build-ID* /MyArtifact.zip`` .

            * If ``path`` is empty, ``namespaceType`` is set to ``NONE`` , and ``name`` is set to
            "``/`` ", the output artifact is stored in the root of the output bucket.

            * If ``path`` is set to ``MyArtifacts`` , ``namespaceType`` is set to ``BUILD_ID`` , and
            ``name`` is set to "``/`` ", the output artifact is stored in ``MyArtifacts/*build-ID*
            `` .

          - **packaging** *(string) --*

            The type of build output artifact to create:

            * If ``type`` is set to ``CODEPIPELINE`` , AWS CodePipeline ignores this value if
            specified. This is because AWS CodePipeline manages its build output artifacts instead
            of AWS CodeBuild.

            * If ``type`` is set to ``NO_ARTIFACTS`` , this value is ignored if specified, because
            no build output is produced.

            * If ``type`` is set to ``S3`` , valid values include:

              * ``NONE`` : AWS CodeBuild creates in the output bucket a folder that contains the
              build output. This is the default if ``packaging`` is not specified.

              * ``ZIP`` : AWS CodeBuild creates in the output bucket a ZIP file that contains the
              build output.

          - **overrideArtifactName** *(boolean) --*

            If this flag is set, a name specified in the build spec file overrides the artifact
            name. The name specified in a build spec file is calculated at build time and uses the
            Shell Command Language. For example, you can append a date and time to your artifact
            name so that it is always unique.

          - **encryptionDisabled** *(boolean) --*

            Set to true if you do not want your output artifacts encrypted. This option is valid
            only if your artifacts type is Amazon Simple Storage Service (Amazon S3). If this is set
            with another artifacts type, an invalidInputException is thrown.

          - **artifactIdentifier** *(string) --*

            An identifier for this artifact definition.

        :type secondaryArtifacts: list
        :param secondaryArtifacts:

          An array of ``ProjectSource`` objects.

          - *(dict) --*

            Information about the build output artifacts for the build project.

            - **type** *(string) --* **[REQUIRED]**

              The type of build output artifact. Valid values include:

              * ``CODEPIPELINE`` : The build project has build output generated through AWS
              CodePipeline.

              .. note::

                 The ``CODEPIPELINE`` type is not supported for ``secondaryArtifacts`` .

              * ``NO_ARTIFACTS`` : The build project does not produce any build output.

              * ``S3`` : The build project stores build output in Amazon Simple Storage Service
              (Amazon S3).

            - **location** *(string) --*

              Information about the build output artifact location:

              * If ``type`` is set to ``CODEPIPELINE`` , AWS CodePipeline ignores this value if
              specified. This is because AWS CodePipeline manages its build output locations instead
              of AWS CodeBuild.

              * If ``type`` is set to ``NO_ARTIFACTS`` , this value is ignored if specified, because
              no build output is produced.

              * If ``type`` is set to ``S3`` , this is the name of the output bucket.

            - **path** *(string) --*

              Along with ``namespaceType`` and ``name`` , the pattern that AWS CodeBuild uses to
              name and store the output artifact:

              * If ``type`` is set to ``CODEPIPELINE`` , AWS CodePipeline ignores this value if
              specified. This is because AWS CodePipeline manages its build output names instead of
              AWS CodeBuild.

              * If ``type`` is set to ``NO_ARTIFACTS`` , this value is ignored if specified, because
              no build output is produced.

              * If ``type`` is set to ``S3`` , this is the path to the output artifact. If ``path``
              is not specified, ``path`` is not used.

              For example, if ``path`` is set to ``MyArtifacts`` , ``namespaceType`` is set to
              ``NONE`` , and ``name`` is set to ``MyArtifact.zip`` , the output artifact is stored
              in the output bucket at ``MyArtifacts/MyArtifact.zip`` .

            - **namespaceType** *(string) --*

              Along with ``path`` and ``name`` , the pattern that AWS CodeBuild uses to determine
              the name and location to store the output artifact:

              * If ``type`` is set to ``CODEPIPELINE`` , AWS CodePipeline ignores this value if
              specified. This is because AWS CodePipeline manages its build output names instead of
              AWS CodeBuild.

              * If ``type`` is set to ``NO_ARTIFACTS`` , this value is ignored if specified, because
              no build output is produced.

              * If ``type`` is set to ``S3`` , valid values include:

                * ``BUILD_ID`` : Include the build ID in the location of the build output artifact.

                * ``NONE`` : Do not include the build ID. This is the default if ``namespaceType``
                is not specified.

              For example, if ``path`` is set to ``MyArtifacts`` , ``namespaceType`` is set to
              ``BUILD_ID`` , and ``name`` is set to ``MyArtifact.zip`` , the output artifact is
              stored in ``MyArtifacts/*build-ID* /MyArtifact.zip`` .

            - **name** *(string) --*

              Along with ``path`` and ``namespaceType`` , the pattern that AWS CodeBuild uses to
              name and store the output artifact:

              * If ``type`` is set to ``CODEPIPELINE`` , AWS CodePipeline ignores this value if
              specified. This is because AWS CodePipeline manages its build output names instead of
              AWS CodeBuild.

              * If ``type`` is set to ``NO_ARTIFACTS`` , this value is ignored if specified, because
              no build output is produced.

              * If ``type`` is set to ``S3`` , this is the name of the output artifact object. If
              you set the name to be a forward slash ("/"), the artifact is stored in the root of
              the output bucket.

              For example:

              * If ``path`` is set to ``MyArtifacts`` , ``namespaceType`` is set to ``BUILD_ID`` ,
              and ``name`` is set to ``MyArtifact.zip`` , then the output artifact is stored in
              ``MyArtifacts/*build-ID* /MyArtifact.zip`` .

              * If ``path`` is empty, ``namespaceType`` is set to ``NONE`` , and ``name`` is set to
              "``/`` ", the output artifact is stored in the root of the output bucket.

              * If ``path`` is set to ``MyArtifacts`` , ``namespaceType`` is set to ``BUILD_ID`` ,
              and ``name`` is set to "``/`` ", the output artifact is stored in
              ``MyArtifacts/*build-ID* `` .

            - **packaging** *(string) --*

              The type of build output artifact to create:

              * If ``type`` is set to ``CODEPIPELINE`` , AWS CodePipeline ignores this value if
              specified. This is because AWS CodePipeline manages its build output artifacts instead
              of AWS CodeBuild.

              * If ``type`` is set to ``NO_ARTIFACTS`` , this value is ignored if specified, because
              no build output is produced.

              * If ``type`` is set to ``S3`` , valid values include:

                * ``NONE`` : AWS CodeBuild creates in the output bucket a folder that contains the
                build output. This is the default if ``packaging`` is not specified.

                * ``ZIP`` : AWS CodeBuild creates in the output bucket a ZIP file that contains the
                build output.

            - **overrideArtifactName** *(boolean) --*

              If this flag is set, a name specified in the build spec file overrides the artifact
              name. The name specified in a build spec file is calculated at build time and uses the
              Shell Command Language. For example, you can append a date and time to your artifact
              name so that it is always unique.

            - **encryptionDisabled** *(boolean) --*

              Set to true if you do not want your output artifacts encrypted. This option is valid
              only if your artifacts type is Amazon Simple Storage Service (Amazon S3). If this is
              set with another artifacts type, an invalidInputException is thrown.

            - **artifactIdentifier** *(string) --*

              An identifier for this artifact definition.

        :type cache: dict
        :param cache:

          Stores recently used information so that it can be quickly accessed at a later time.

          - **type** *(string) --* **[REQUIRED]**

            The type of cache used by the build project. Valid values include:

            * ``NO_CACHE`` : The build project does not use any cache.

            * ``S3`` : The build project reads and writes from and to S3.

            * ``LOCAL`` : The build project stores a cache locally on a build host that is only
            available to that build host.

          - **location** *(string) --*

            Information about the cache location:

            * ``NO_CACHE`` or ``LOCAL`` : This value is ignored.

            * ``S3`` : This is the S3 bucket name/prefix.

          - **modes** *(list) --*

            If you use a ``LOCAL`` cache, the local cache mode. You can use one or more local cache
            modes at the same time.

            * ``LOCAL_SOURCE_CACHE`` mode caches Git metadata for primary and secondary sources.
            After the cache is created, subsequent builds pull only the change between commits. This
            mode is a good choice for projects with a clean working directory and a source that is a
            large Git repository. If you choose this option and your project does not use a Git
            repository (GitHub, GitHub Enterprise, or Bitbucket), the option is ignored.

            * ``LOCAL_DOCKER_LAYER_CACHE`` mode caches existing Docker layers. This mode is a good
            choice for projects that build or pull large Docker images. It can prevent the
            performance issues caused by pulling large Docker images down from the network.

            .. note::

                * You can use a Docker layer cache in the Linux environment only.

                * The ``privileged`` flag must be set so that your project has the required Docker
                permissions.

                * You should consider the security implications before you use a Docker layer cache.

            * ``LOCAL_CUSTOM_CACHE`` mode caches directories you specify in the buildspec file. This
            mode is a good choice if your build scenario is not suited to one of the other three
            local cache modes. If you use a custom cache:

              * Only directories can be specified for caching. You cannot specify individual files.

              * Symlinks are used to reference cached directories.

              * Cached directories are linked to your build before it downloads its project sources.
              Cached items are overridden if a source item has the same name. Directories are
              specified using cache paths in the buildspec file.

            - *(string) --*

        :type environment: dict
        :param environment:

          Information to be changed about the build environment for the build project.

          - **type** *(string) --* **[REQUIRED]**

            The type of build environment to use for related builds.

            * The environment type ``ARM_CONTAINER`` is available only in regions US East (N.
            Virginia), US East (Ohio), US West (Oregon), EU (Ireland), Asia Pacific (Mumbai), Asia
            Pacific (Tokyo), Asia Pacific (Sydney), and EU (Frankfurt).

            * The environment type ``LINUX_CONTAINER`` with compute type ``build.general1.2xlarge``
            is available only in regions US East (N. Virginia), US East (N. Virginia), US West
            (Oregon), Canada (Central), EU (Ireland), EU (London), EU (Frankfurt), Asia Pacific
            (Tokyo), Asia Pacific (Seoul), Asia Pacific (Singapore), Asia Pacific (Sydney), China
            (Beijing), and China (Ningxia).

            * The environment type ``LINUX_GPU_CONTAINER`` is available only in regions US East (N.
            Virginia), US East (N. Virginia), US West (Oregon), Canada (Central), EU (Ireland), EU
            (London), EU (Frankfurt), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific
            (Singapore), Asia Pacific (Sydney) , China (Beijing), and China (Ningxia).

          - **image** *(string) --* **[REQUIRED]**

            The image tag or image digest that identifies the Docker image to use for this build
            project. Use the following formats:

            * For an image tag: ``registry/repository:tag`` . For example, to specify an image with
            the tag "latest," use ``registry/repository:latest`` .

            * For an image digest: ``registry/repository@digest`` . For example, to specify an image
            with the digest
            "sha256:cbbf2f9a99b47fc460d422812b6a5adff7dfee951d8fa2e4a98caa0382cfbdbf," use
            ``registry/repository@sha256:cbbf2f9a99b47fc460d422812b6a5adff7dfee951d8fa2e4a98caa0382cfbdbf``
            .

          - **computeType** *(string) --* **[REQUIRED]**

            Information about the compute resources the build project uses. Available values
            include:

            * ``BUILD_GENERAL1_SMALL`` : Use up to 3 GB memory and 2 vCPUs for builds.

            * ``BUILD_GENERAL1_MEDIUM`` : Use up to 7 GB memory and 4 vCPUs for builds.

            * ``BUILD_GENERAL1_LARGE`` : Use up to 16 GB memory and 8 vCPUs for builds, depending on
            your environment type.

            * ``BUILD_GENERAL1_2XLARGE`` : Use up to 145 GB memory, 72 vCPUs, and 824 GB of SSD
            storage for builds. This compute type supports Docker images up to 100 GB uncompressed.

            If you use ``BUILD_GENERAL1_LARGE`` :

            * For environment type ``LINUX_CONTAINER`` , you can use up to 15 GB memory and 8 vCPUs
            for builds.

            * For environment type ``LINUX_GPU_CONTAINER`` , you can use up to 255 GB memory, 32
            vCPUs, and 4 NVIDIA Tesla V100 GPUs for builds.

            * For environment type ``ARM_CONTAINER`` , you can use up to 16 GB memory and 8 vCPUs on
            ARM-based processors for builds.

            For more information, see `Build Environment Compute Types
            <https://docs.aws.amazon.com/codebuild/latest/userguide/build-env-ref-compute-types.html>`__
            in the *AWS CodeBuild User Guide.*

          - **environmentVariables** *(list) --*

            A set of environment variables to make available to builds for this build project.

            - *(dict) --*

              Information about an environment variable for a build project or a build.

              - **name** *(string) --* **[REQUIRED]**

                The name or key of the environment variable.

              - **value** *(string) --* **[REQUIRED]**

                The value of the environment variable.

                .. warning::

                  We strongly discourage the use of environment variables to store sensitive values,
                  especially AWS secret key IDs and secret access keys. Environment variables can be
                  displayed in plain text using the AWS CodeBuild console and the AWS Command Line
                  Interface (AWS CLI).

              - **type** *(string) --*

                The type of environment variable. Valid values include:

                * ``PARAMETER_STORE`` : An environment variable stored in Amazon EC2 Systems Manager
                Parameter Store.

                * ``PLAINTEXT`` : An environment variable in plain text format.

                * ``SECRETS_MANAGER`` : An environment variable stored in AWS Secrets Manager.

          - **privilegedMode** *(boolean) --*

            Enables running the Docker daemon inside a Docker container. Set to true only if the
            build project is used to build Docker images. Otherwise, a build that attempts to
            interact with the Docker daemon fails. The default setting is ``false`` .

            You can initialize the Docker daemon during the install phase of your build by adding
            one of the following sets of commands to the install phase of your buildspec file:

            If the operating system's base image is Ubuntu Linux:

             ``- nohup /usr/local/bin/dockerd --host=unix:///var/run/docker.sock
             --host=tcp://0.0.0.0:2375 --storage-driver=overlay&``

             ``- timeout 15 sh -c "until docker info; do echo .; sleep 1; done"``

            If the operating system's base image is Alpine Linux and the previous command does not
            work, add the ``-t`` argument to ``timeout`` :

             ``- nohup /usr/local/bin/dockerd --host=unix:///var/run/docker.sock
             --host=tcp://0.0.0.0:2375 --storage-driver=overlay&``

             ``- timeout -t 15 sh -c "until docker info; do echo .; sleep 1; done"``

          - **certificate** *(string) --*

            The certificate to use with this build project.

          - **registryCredential** *(dict) --*

            The credentials for access to a private registry.

            - **credential** *(string) --* **[REQUIRED]**

              The Amazon Resource Name (ARN) or name of credentials created using AWS Secrets
              Manager.

              .. note::

                The ``credential`` can use the name of the credentials only if they exist in your
                current region.

            - **credentialProvider** *(string) --* **[REQUIRED]**

              The service that created the credentials to access a private Docker registry. The
              valid value, SECRETS_MANAGER, is for AWS Secrets Manager.

          - **imagePullCredentialsType** *(string) --*

            The type of credentials AWS CodeBuild uses to pull images in your build. There are two
            valid values:

            * ``CODEBUILD`` specifies that AWS CodeBuild uses its own credentials. This requires
            that you modify your ECR repository policy to trust AWS CodeBuild's service principal.

            * ``SERVICE_ROLE`` specifies that AWS CodeBuild uses your build project's service role.

            When you use a cross-account or private registry image, you must use SERVICE_ROLE
            credentials. When you use an AWS CodeBuild curated image, you must use CODEBUILD
            credentials.

        :type serviceRole: string
        :param serviceRole:

          The replacement ARN of the AWS Identity and Access Management (IAM) role that enables AWS
          CodeBuild to interact with dependent AWS services on behalf of the AWS account.

        :type timeoutInMinutes: integer
        :param timeoutInMinutes:

          The replacement value in minutes, from 5 to 480 (8 hours), for AWS CodeBuild to wait
          before timing out any related build that did not get marked as completed.

        :type queuedTimeoutInMinutes: integer
        :param queuedTimeoutInMinutes:

          The number of minutes a build is allowed to be queued before it times out.

        :type encryptionKey: string
        :param encryptionKey:

          The AWS Key Management Service (AWS KMS) customer master key (CMK) to be used for
          encrypting the build output artifacts.

          .. note::

            You can use a cross-account KMS key to encrypt the build output artifacts if your
            service role has permission to that key.

          You can specify either the Amazon Resource Name (ARN) of the CMK or, if available, the
          CMK's alias (using the format ``alias/*alias-name* `` ).

        :type tags: list
        :param tags:

          The replacement set of tags for this build project.

          These tags are available for use by AWS services that support AWS CodeBuild build project
          tags.

          - *(dict) --*

            A tag, consisting of a key and a value.

            This tag is available for use by AWS services that support tags in AWS CodeBuild.

            - **key** *(string) --*

              The tag's key.

            - **value** *(string) --*

              The tag's value.

        :type vpcConfig: dict
        :param vpcConfig:

          VpcConfig enables AWS CodeBuild to access resources in an Amazon VPC.

          - **vpcId** *(string) --*

            The ID of the Amazon VPC.

          - **subnets** *(list) --*

            A list of one or more subnet IDs in your Amazon VPC.

            - *(string) --*

          - **securityGroupIds** *(list) --*

            A list of one or more security groups IDs in your Amazon VPC.

            - *(string) --*

        :type badgeEnabled: boolean
        :param badgeEnabled:

          Set this to true to generate a publicly accessible URL for your project's build badge.

        :type logsConfig: dict
        :param logsConfig:

          Information about logs for the build project. A project can create logs in Amazon
          CloudWatch Logs, logs in an S3 bucket, or both.

          - **cloudWatchLogs** *(dict) --*

            Information about Amazon CloudWatch Logs for a build project. Amazon CloudWatch Logs are
            enabled by default.

            - **status** *(string) --* **[REQUIRED]**

              The current status of the logs in Amazon CloudWatch Logs for a build project. Valid
              values are:

              * ``ENABLED`` : Amazon CloudWatch Logs are enabled for this build project.

              * ``DISABLED`` : Amazon CloudWatch Logs are not enabled for this build project.

            - **groupName** *(string) --*

              The group name of the logs in Amazon CloudWatch Logs. For more information, see
              `Working with Log Groups and Log Streams
              <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html>`__
              .

            - **streamName** *(string) --*

              The prefix of the stream name of the Amazon CloudWatch Logs. For more information, see
              `Working with Log Groups and Log Streams
              <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html>`__
              .

          - **s3Logs** *(dict) --*

            Information about logs built to an S3 bucket for a build project. S3 logs are not
            enabled by default.

            - **status** *(string) --* **[REQUIRED]**

              The current status of the S3 build logs. Valid values are:

              * ``ENABLED`` : S3 build logs are enabled for this build project.

              * ``DISABLED`` : S3 build logs are not enabled for this build project.

            - **location** *(string) --*

              The ARN of an S3 bucket and the path prefix for S3 logs. If your Amazon S3 bucket name
              is ``my-bucket`` , and your path prefix is ``build-log`` , then acceptable formats are
              ``my-bucket/build-log`` or ``arn:aws:s3:::my-bucket/build-log`` .

            - **encryptionDisabled** *(boolean) --*

              Set to true if you do not want your S3 build log output encrypted. By default S3 build
              logs are encrypted.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'project': {
                    'name': 'string',
                    'arn': 'string',
                    'description': 'string',
                    'source': {
                        'type':
                        'CODECOMMIT'|'CODEPIPELINE'|'GITHUB'|'S3'|'BITBUCKET'
                        |'GITHUB_ENTERPRISE'|'NO_SOURCE',
                        'location': 'string',
                        'gitCloneDepth': 123,
                        'gitSubmodulesConfig': {
                            'fetchSubmodules': True|False
                        },
                        'buildspec': 'string',
                        'auth': {
                            'type': 'OAUTH',
                            'resource': 'string'
                        },
                        'reportBuildStatus': True|False,
                        'insecureSsl': True|False,
                        'sourceIdentifier': 'string'
                    },
                    'secondarySources': [
                        {
                            'type':
                            'CODECOMMIT'|'CODEPIPELINE'|'GITHUB'|'S3'
                            |'BITBUCKET'|'GITHUB_ENTERPRISE'|'NO_SOURCE',
                            'location': 'string',
                            'gitCloneDepth': 123,
                            'gitSubmodulesConfig': {
                                'fetchSubmodules': True|False
                            },
                            'buildspec': 'string',
                            'auth': {
                                'type': 'OAUTH',
                                'resource': 'string'
                            },
                            'reportBuildStatus': True|False,
                            'insecureSsl': True|False,
                            'sourceIdentifier': 'string'
                        },
                    ],
                    'sourceVersion': 'string',
                    'secondarySourceVersions': [
                        {
                            'sourceIdentifier': 'string',
                            'sourceVersion': 'string'
                        },
                    ],
                    'artifacts': {
                        'type': 'CODEPIPELINE'|'S3'|'NO_ARTIFACTS',
                        'location': 'string',
                        'path': 'string',
                        'namespaceType': 'NONE'|'BUILD_ID',
                        'name': 'string',
                        'packaging': 'NONE'|'ZIP',
                        'overrideArtifactName': True|False,
                        'encryptionDisabled': True|False,
                        'artifactIdentifier': 'string'
                    },
                    'secondaryArtifacts': [
                        {
                            'type': 'CODEPIPELINE'|'S3'|'NO_ARTIFACTS',
                            'location': 'string',
                            'path': 'string',
                            'namespaceType': 'NONE'|'BUILD_ID',
                            'name': 'string',
                            'packaging': 'NONE'|'ZIP',
                            'overrideArtifactName': True|False,
                            'encryptionDisabled': True|False,
                            'artifactIdentifier': 'string'
                        },
                    ],
                    'cache': {
                        'type': 'NO_CACHE'|'S3'|'LOCAL',
                        'location': 'string',
                        'modes': [
                            'LOCAL_DOCKER_LAYER_CACHE'|'LOCAL_SOURCE_CACHE'|'LOCAL_CUSTOM_CACHE',
                        ]
                    },
                    'environment': {
                        'type':
                        'WINDOWS_CONTAINER'|'LINUX_CONTAINER'|'LINUX_GPU_CONTAINER'
                        |'ARM_CONTAINER',
                        'image': 'string',
                        'computeType':
                        'BUILD_GENERAL1_SMALL'|'BUILD_GENERAL1_MEDIUM'
                        |'BUILD_GENERAL1_LARGE'|'BUILD_GENERAL1_2XLARGE',
                        'environmentVariables': [
                            {
                                'name': 'string',
                                'value': 'string',
                                'type': 'PLAINTEXT'|'PARAMETER_STORE'|'SECRETS_MANAGER'
                            },
                        ],
                        'privilegedMode': True|False,
                        'certificate': 'string',
                        'registryCredential': {
                            'credential': 'string',
                            'credentialProvider': 'SECRETS_MANAGER'
                        },
                        'imagePullCredentialsType': 'CODEBUILD'|'SERVICE_ROLE'
                    },
                    'serviceRole': 'string',
                    'timeoutInMinutes': 123,
                    'queuedTimeoutInMinutes': 123,
                    'encryptionKey': 'string',
                    'tags': [
                        {
                            'key': 'string',
                            'value': 'string'
                        },
                    ],
                    'created': datetime(2015, 1, 1),
                    'lastModified': datetime(2015, 1, 1),
                    'webhook': {
                        'url': 'string',
                        'payloadUrl': 'string',
                        'secret': 'string',
                        'branchFilter': 'string',
                        'filterGroups': [
                            [
                                {
                                    'type':
                                    'EVENT'|'BASE_REF'|'HEAD_REF'
                                    |'ACTOR_ACCOUNT_ID'|'FILE_PATH',
                                    'pattern': 'string',
                                    'excludeMatchedPattern': True|False
                                },
                            ],
                        ],
                        'lastModifiedSecret': datetime(2015, 1, 1)
                    },
                    'vpcConfig': {
                        'vpcId': 'string',
                        'subnets': [
                            'string',
                        ],
                        'securityGroupIds': [
                            'string',
                        ]
                    },
                    'badge': {
                        'badgeEnabled': True|False,
                        'badgeRequestUrl': 'string'
                    },
                    'logsConfig': {
                        'cloudWatchLogs': {
                            'status': 'ENABLED'|'DISABLED',
                            'groupName': 'string',
                            'streamName': 'string'
                        },
                        's3Logs': {
                            'status': 'ENABLED'|'DISABLED',
                            'location': 'string',
                            'encryptionDisabled': True|False
                        }
                    }
                }
            }
          **Response Structure**

          - *(dict) --*

            - **project** *(dict) --*

              Information about the build project that was changed.

              - **name** *(string) --*

                The name of the build project.

              - **arn** *(string) --*

                The Amazon Resource Name (ARN) of the build project.

              - **description** *(string) --*

                A description that makes the build project easy to identify.

              - **source** *(dict) --*

                Information about the build input source code for this build project.

                - **type** *(string) --*

                  The type of repository that contains the source code to be built. Valid values
                  include:

                  * ``BITBUCKET`` : The source code is in a Bitbucket repository.

                  * ``CODECOMMIT`` : The source code is in an AWS CodeCommit repository.

                  * ``CODEPIPELINE`` : The source code settings are specified in the source action
                  of a pipeline in AWS CodePipeline.

                  * ``GITHUB`` : The source code is in a GitHub repository.

                  * ``GITHUB_ENTERPRISE`` : The source code is in a GitHub Enterprise repository.

                  * ``NO_SOURCE`` : The project does not have input source code.

                  * ``S3`` : The source code is in an Amazon Simple Storage Service (Amazon S3)
                  input bucket.

                - **location** *(string) --*

                  Information about the location of the source code to be built. Valid values
                  include:

                  * For source code settings that are specified in the source action of a pipeline
                  in AWS CodePipeline, ``location`` should not be specified. If it is specified, AWS
                  CodePipeline ignores it. This is because AWS CodePipeline uses the settings in a
                  pipeline's source action instead of this value.

                  * For source code in an AWS CodeCommit repository, the HTTPS clone URL to the
                  repository that contains the source code and the build spec (for example,
                  ``https://git-codecommit.*region-ID* .amazonaws.com/v1/repos/*repo-name* `` ).

                  * For source code in an Amazon Simple Storage Service (Amazon S3) input bucket,
                  one of the following.

                    * The path to the ZIP file that contains the source code (for example, ``
                    *bucket-name* /*path* /*to* /*object-name* .zip`` ).

                    * The path to the folder that contains the source code (for example, ``
                    *bucket-name* /*path* /*to* /*source-code* /*folder* /`` ).

                  * For source code in a GitHub repository, the HTTPS clone URL to the repository
                  that contains the source and the build spec. You must connect your AWS account to
                  your GitHub account. Use the AWS CodeBuild console to start creating a build
                  project. When you use the console to connect (or reconnect) with GitHub, on the
                  GitHub **Authorize application** page, for **Organization access** , choose
                  **Request access** next to each repository you want to allow AWS CodeBuild to have
                  access to, and then choose **Authorize application** . (After you have connected
                  to your GitHub account, you do not need to finish creating the build project. You
                  can leave the AWS CodeBuild console.) To instruct AWS CodeBuild to use this
                  connection, in the ``source`` object, set the ``auth`` object's ``type`` value to
                  ``OAUTH`` .

                  * For source code in a Bitbucket repository, the HTTPS clone URL to the repository
                  that contains the source and the build spec. You must connect your AWS account to
                  your Bitbucket account. Use the AWS CodeBuild console to start creating a build
                  project. When you use the console to connect (or reconnect) with Bitbucket, on the
                  Bitbucket **Confirm access to your account** page, choose **Grant access** .
                  (After you have connected to your Bitbucket account, you do not need to finish
                  creating the build project. You can leave the AWS CodeBuild console.) To instruct
                  AWS CodeBuild to use this connection, in the ``source`` object, set the ``auth``
                  object's ``type`` value to ``OAUTH`` .

                - **gitCloneDepth** *(integer) --*

                  Information about the Git clone depth for the build project.

                - **gitSubmodulesConfig** *(dict) --*

                  Information about the Git submodules configuration for the build project.

                  - **fetchSubmodules** *(boolean) --*

                    Set to true to fetch Git submodules for your AWS CodeBuild build project.

                - **buildspec** *(string) --*

                  The build spec declaration to use for the builds in this build project.

                  If this value is not specified, a build spec must be included along with the
                  source code to be built.

                - **auth** *(dict) --*

                  Information about the authorization settings for AWS CodeBuild to access the
                  source code to be built.

                  This information is for the AWS CodeBuild console's use only. Your code should not
                  get or set this information directly.

                  - **type** *(string) --*

                    .. note::

                      This data type is deprecated and is no longer accurate or used.

                    The authorization type to use. The only valid value is ``OAUTH`` , which
                    represents the OAuth authorization type.

                  - **resource** *(string) --*

                    The resource value that applies to the specified authorization type.

                - **reportBuildStatus** *(boolean) --*

                  Set to true to report the status of a build's start and finish to your source
                  provider. This option is valid only when your source provider is GitHub, GitHub
                  Enterprise, or Bitbucket. If this is set and you use a different source provider,
                  an invalidInputException is thrown.

                  .. note::

                    The status of a build triggered by a webhook is always reported to your source
                    provider.

                - **insecureSsl** *(boolean) --*

                  Enable this flag to ignore SSL warnings while connecting to the project source
                  code.

                - **sourceIdentifier** *(string) --*

                  An identifier for this project source.

              - **secondarySources** *(list) --*

                An array of ``ProjectSource`` objects.

                - *(dict) --*

                  Information about the build input source code for the build project.

                  - **type** *(string) --*

                    The type of repository that contains the source code to be built. Valid values
                    include:

                    * ``BITBUCKET`` : The source code is in a Bitbucket repository.

                    * ``CODECOMMIT`` : The source code is in an AWS CodeCommit repository.

                    * ``CODEPIPELINE`` : The source code settings are specified in the source action
                    of a pipeline in AWS CodePipeline.

                    * ``GITHUB`` : The source code is in a GitHub repository.

                    * ``GITHUB_ENTERPRISE`` : The source code is in a GitHub Enterprise repository.

                    * ``NO_SOURCE`` : The project does not have input source code.

                    * ``S3`` : The source code is in an Amazon Simple Storage Service (Amazon S3)
                    input bucket.

                  - **location** *(string) --*

                    Information about the location of the source code to be built. Valid values
                    include:

                    * For source code settings that are specified in the source action of a pipeline
                    in AWS CodePipeline, ``location`` should not be specified. If it is specified,
                    AWS CodePipeline ignores it. This is because AWS CodePipeline uses the settings
                    in a pipeline's source action instead of this value.

                    * For source code in an AWS CodeCommit repository, the HTTPS clone URL to the
                    repository that contains the source code and the build spec (for example,
                    ``https://git-codecommit.*region-ID* .amazonaws.com/v1/repos/*repo-name* `` ).

                    * For source code in an Amazon Simple Storage Service (Amazon S3) input bucket,
                    one of the following.

                      * The path to the ZIP file that contains the source code (for example, ``
                      *bucket-name* /*path* /*to* /*object-name* .zip`` ).

                      * The path to the folder that contains the source code (for example, ``
                      *bucket-name* /*path* /*to* /*source-code* /*folder* /`` ).

                    * For source code in a GitHub repository, the HTTPS clone URL to the repository
                    that contains the source and the build spec. You must connect your AWS account
                    to your GitHub account. Use the AWS CodeBuild console to start creating a build
                    project. When you use the console to connect (or reconnect) with GitHub, on the
                    GitHub **Authorize application** page, for **Organization access** , choose
                    **Request access** next to each repository you want to allow AWS CodeBuild to
                    have access to, and then choose **Authorize application** . (After you have
                    connected to your GitHub account, you do not need to finish creating the build
                    project. You can leave the AWS CodeBuild console.) To instruct AWS CodeBuild to
                    use this connection, in the ``source`` object, set the ``auth`` object's
                    ``type`` value to ``OAUTH`` .

                    * For source code in a Bitbucket repository, the HTTPS clone URL to the
                    repository that contains the source and the build spec. You must connect your
                    AWS account to your Bitbucket account. Use the AWS CodeBuild console to start
                    creating a build project. When you use the console to connect (or reconnect)
                    with Bitbucket, on the Bitbucket **Confirm access to your account** page, choose
                    **Grant access** . (After you have connected to your Bitbucket account, you do
                    not need to finish creating the build project. You can leave the AWS CodeBuild
                    console.) To instruct AWS CodeBuild to use this connection, in the ``source``
                    object, set the ``auth`` object's ``type`` value to ``OAUTH`` .

                  - **gitCloneDepth** *(integer) --*

                    Information about the Git clone depth for the build project.

                  - **gitSubmodulesConfig** *(dict) --*

                    Information about the Git submodules configuration for the build project.

                    - **fetchSubmodules** *(boolean) --*

                      Set to true to fetch Git submodules for your AWS CodeBuild build project.

                  - **buildspec** *(string) --*

                    The build spec declaration to use for the builds in this build project.

                    If this value is not specified, a build spec must be included along with the
                    source code to be built.

                  - **auth** *(dict) --*

                    Information about the authorization settings for AWS CodeBuild to access the
                    source code to be built.

                    This information is for the AWS CodeBuild console's use only. Your code should
                    not get or set this information directly.

                    - **type** *(string) --*

                      .. note::

                        This data type is deprecated and is no longer accurate or used.

                      The authorization type to use. The only valid value is ``OAUTH`` , which
                      represents the OAuth authorization type.

                    - **resource** *(string) --*

                      The resource value that applies to the specified authorization type.

                  - **reportBuildStatus** *(boolean) --*

                    Set to true to report the status of a build's start and finish to your source
                    provider. This option is valid only when your source provider is GitHub, GitHub
                    Enterprise, or Bitbucket. If this is set and you use a different source
                    provider, an invalidInputException is thrown.

                    .. note::

                      The status of a build triggered by a webhook is always reported to your source
                      provider.

                  - **insecureSsl** *(boolean) --*

                    Enable this flag to ignore SSL warnings while connecting to the project source
                    code.

                  - **sourceIdentifier** *(string) --*

                    An identifier for this project source.

              - **sourceVersion** *(string) --*

                A version of the build input to be built for this project. If not specified, the
                latest version is used. If specified, it must be one of:

                * For AWS CodeCommit: the commit ID, branch, or Git tag to use.

                * For GitHub: the commit ID, pull request ID, branch name, or tag name that
                corresponds to the version of the source code you want to build. If a pull request
                ID is specified, it must use the format ``pr/pull-request-ID`` (for example
                ``pr/25`` ). If a branch name is specified, the branch's HEAD commit ID is used. If
                not specified, the default branch's HEAD commit ID is used.

                * For Bitbucket: the commit ID, branch name, or tag name that corresponds to the
                version of the source code you want to build. If a branch name is specified, the
                branch's HEAD commit ID is used. If not specified, the default branch's HEAD commit
                ID is used.

                * For Amazon Simple Storage Service (Amazon S3): the version ID of the object that
                represents the build input ZIP file to use.

                If ``sourceVersion`` is specified at the build level, then that version takes
                precedence over this ``sourceVersion`` (at the project level).

                For more information, see `Source Version Sample with CodeBuild
                <https://docs.aws.amazon.com/codebuild/latest/userguide/sample-source-version.html>`__
                in the *AWS CodeBuild User Guide* .

              - **secondarySourceVersions** *(list) --*

                An array of ``ProjectSourceVersion`` objects. If ``secondarySourceVersions`` is
                specified at the build level, then they take over these ``secondarySourceVersions``
                (at the project level).

                - *(dict) --*

                  A source identifier and its corresponding version.

                  - **sourceIdentifier** *(string) --*

                    An identifier for a source in the build project.

                  - **sourceVersion** *(string) --*

                    The source version for the corresponding source identifier. If specified, must
                    be one of:

                    * For AWS CodeCommit: the commit ID, branch, or Git tag to use.

                    * For GitHub: the commit ID, pull request ID, branch name, or tag name that
                    corresponds to the version of the source code you want to build. If a pull
                    request ID is specified, it must use the format ``pr/pull-request-ID`` (for
                    example, ``pr/25`` ). If a branch name is specified, the branch's HEAD commit ID
                    is used. If not specified, the default branch's HEAD commit ID is used.

                    * For Bitbucket: the commit ID, branch name, or tag name that corresponds to the
                    version of the source code you want to build. If a branch name is specified, the
                    branch's HEAD commit ID is used. If not specified, the default branch's HEAD
                    commit ID is used.

                    * For Amazon Simple Storage Service (Amazon S3): the version ID of the object
                    that represents the build input ZIP file to use.

                    For more information, see `Source Version Sample with CodeBuild
                    <https://docs.aws.amazon.com/codebuild/latest/userguide/sample-source-version.html>`__
                    in the *AWS CodeBuild User Guide* .

              - **artifacts** *(dict) --*

                Information about the build output artifacts for the build project.

                - **type** *(string) --*

                  The type of build output artifact. Valid values include:

                  * ``CODEPIPELINE`` : The build project has build output generated through AWS
                  CodePipeline.

                  .. note::

                     The ``CODEPIPELINE`` type is not supported for ``secondaryArtifacts`` .

                  * ``NO_ARTIFACTS`` : The build project does not produce any build output.

                  * ``S3`` : The build project stores build output in Amazon Simple Storage Service
                  (Amazon S3).

                - **location** *(string) --*

                  Information about the build output artifact location:

                  * If ``type`` is set to ``CODEPIPELINE`` , AWS CodePipeline ignores this value if
                  specified. This is because AWS CodePipeline manages its build output locations
                  instead of AWS CodeBuild.

                  * If ``type`` is set to ``NO_ARTIFACTS`` , this value is ignored if specified,
                  because no build output is produced.

                  * If ``type`` is set to ``S3`` , this is the name of the output bucket.

                - **path** *(string) --*

                  Along with ``namespaceType`` and ``name`` , the pattern that AWS CodeBuild uses to
                  name and store the output artifact:

                  * If ``type`` is set to ``CODEPIPELINE`` , AWS CodePipeline ignores this value if
                  specified. This is because AWS CodePipeline manages its build output names instead
                  of AWS CodeBuild.

                  * If ``type`` is set to ``NO_ARTIFACTS`` , this value is ignored if specified,
                  because no build output is produced.

                  * If ``type`` is set to ``S3`` , this is the path to the output artifact. If
                  ``path`` is not specified, ``path`` is not used.

                  For example, if ``path`` is set to ``MyArtifacts`` , ``namespaceType`` is set to
                  ``NONE`` , and ``name`` is set to ``MyArtifact.zip`` , the output artifact is
                  stored in the output bucket at ``MyArtifacts/MyArtifact.zip`` .

                - **namespaceType** *(string) --*

                  Along with ``path`` and ``name`` , the pattern that AWS CodeBuild uses to
                  determine the name and location to store the output artifact:

                  * If ``type`` is set to ``CODEPIPELINE`` , AWS CodePipeline ignores this value if
                  specified. This is because AWS CodePipeline manages its build output names instead
                  of AWS CodeBuild.

                  * If ``type`` is set to ``NO_ARTIFACTS`` , this value is ignored if specified,
                  because no build output is produced.

                  * If ``type`` is set to ``S3`` , valid values include:

                    * ``BUILD_ID`` : Include the build ID in the location of the build output
                    artifact.

                    * ``NONE`` : Do not include the build ID. This is the default if
                    ``namespaceType`` is not specified.

                  For example, if ``path`` is set to ``MyArtifacts`` , ``namespaceType`` is set to
                  ``BUILD_ID`` , and ``name`` is set to ``MyArtifact.zip`` , the output artifact is
                  stored in ``MyArtifacts/*build-ID* /MyArtifact.zip`` .

                - **name** *(string) --*

                  Along with ``path`` and ``namespaceType`` , the pattern that AWS CodeBuild uses to
                  name and store the output artifact:

                  * If ``type`` is set to ``CODEPIPELINE`` , AWS CodePipeline ignores this value if
                  specified. This is because AWS CodePipeline manages its build output names instead
                  of AWS CodeBuild.

                  * If ``type`` is set to ``NO_ARTIFACTS`` , this value is ignored if specified,
                  because no build output is produced.

                  * If ``type`` is set to ``S3`` , this is the name of the output artifact object.
                  If you set the name to be a forward slash ("/"), the artifact is stored in the
                  root of the output bucket.

                  For example:

                  * If ``path`` is set to ``MyArtifacts`` , ``namespaceType`` is set to ``BUILD_ID``
                  , and ``name`` is set to ``MyArtifact.zip`` , then the output artifact is stored
                  in ``MyArtifacts/*build-ID* /MyArtifact.zip`` .

                  * If ``path`` is empty, ``namespaceType`` is set to ``NONE`` , and ``name`` is set
                  to "``/`` ", the output artifact is stored in the root of the output bucket.

                  * If ``path`` is set to ``MyArtifacts`` , ``namespaceType`` is set to ``BUILD_ID``
                  , and ``name`` is set to "``/`` ", the output artifact is stored in
                  ``MyArtifacts/*build-ID* `` .

                - **packaging** *(string) --*

                  The type of build output artifact to create:

                  * If ``type`` is set to ``CODEPIPELINE`` , AWS CodePipeline ignores this value if
                  specified. This is because AWS CodePipeline manages its build output artifacts
                  instead of AWS CodeBuild.

                  * If ``type`` is set to ``NO_ARTIFACTS`` , this value is ignored if specified,
                  because no build output is produced.

                  * If ``type`` is set to ``S3`` , valid values include:

                    * ``NONE`` : AWS CodeBuild creates in the output bucket a folder that contains
                    the build output. This is the default if ``packaging`` is not specified.

                    * ``ZIP`` : AWS CodeBuild creates in the output bucket a ZIP file that contains
                    the build output.

                - **overrideArtifactName** *(boolean) --*

                  If this flag is set, a name specified in the build spec file overrides the
                  artifact name. The name specified in a build spec file is calculated at build time
                  and uses the Shell Command Language. For example, you can append a date and time
                  to your artifact name so that it is always unique.

                - **encryptionDisabled** *(boolean) --*

                  Set to true if you do not want your output artifacts encrypted. This option is
                  valid only if your artifacts type is Amazon Simple Storage Service (Amazon S3). If
                  this is set with another artifacts type, an invalidInputException is thrown.

                - **artifactIdentifier** *(string) --*

                  An identifier for this artifact definition.

              - **secondaryArtifacts** *(list) --*

                An array of ``ProjectArtifacts`` objects.

                - *(dict) --*

                  Information about the build output artifacts for the build project.

                  - **type** *(string) --*

                    The type of build output artifact. Valid values include:

                    * ``CODEPIPELINE`` : The build project has build output generated through AWS
                    CodePipeline.

                    .. note::

                       The ``CODEPIPELINE`` type is not supported for ``secondaryArtifacts`` .

                    * ``NO_ARTIFACTS`` : The build project does not produce any build output.

                    * ``S3`` : The build project stores build output in Amazon Simple Storage
                    Service (Amazon S3).

                  - **location** *(string) --*

                    Information about the build output artifact location:

                    * If ``type`` is set to ``CODEPIPELINE`` , AWS CodePipeline ignores this value
                    if specified. This is because AWS CodePipeline manages its build output
                    locations instead of AWS CodeBuild.

                    * If ``type`` is set to ``NO_ARTIFACTS`` , this value is ignored if specified,
                    because no build output is produced.

                    * If ``type`` is set to ``S3`` , this is the name of the output bucket.

                  - **path** *(string) --*

                    Along with ``namespaceType`` and ``name`` , the pattern that AWS CodeBuild uses
                    to name and store the output artifact:

                    * If ``type`` is set to ``CODEPIPELINE`` , AWS CodePipeline ignores this value
                    if specified. This is because AWS CodePipeline manages its build output names
                    instead of AWS CodeBuild.

                    * If ``type`` is set to ``NO_ARTIFACTS`` , this value is ignored if specified,
                    because no build output is produced.

                    * If ``type`` is set to ``S3`` , this is the path to the output artifact. If
                    ``path`` is not specified, ``path`` is not used.

                    For example, if ``path`` is set to ``MyArtifacts`` , ``namespaceType`` is set to
                    ``NONE`` , and ``name`` is set to ``MyArtifact.zip`` , the output artifact is
                    stored in the output bucket at ``MyArtifacts/MyArtifact.zip`` .

                  - **namespaceType** *(string) --*

                    Along with ``path`` and ``name`` , the pattern that AWS CodeBuild uses to
                    determine the name and location to store the output artifact:

                    * If ``type`` is set to ``CODEPIPELINE`` , AWS CodePipeline ignores this value
                    if specified. This is because AWS CodePipeline manages its build output names
                    instead of AWS CodeBuild.

                    * If ``type`` is set to ``NO_ARTIFACTS`` , this value is ignored if specified,
                    because no build output is produced.

                    * If ``type`` is set to ``S3`` , valid values include:

                      * ``BUILD_ID`` : Include the build ID in the location of the build output
                      artifact.

                      * ``NONE`` : Do not include the build ID. This is the default if
                      ``namespaceType`` is not specified.

                    For example, if ``path`` is set to ``MyArtifacts`` , ``namespaceType`` is set to
                    ``BUILD_ID`` , and ``name`` is set to ``MyArtifact.zip`` , the output artifact
                    is stored in ``MyArtifacts/*build-ID* /MyArtifact.zip`` .

                  - **name** *(string) --*

                    Along with ``path`` and ``namespaceType`` , the pattern that AWS CodeBuild uses
                    to name and store the output artifact:

                    * If ``type`` is set to ``CODEPIPELINE`` , AWS CodePipeline ignores this value
                    if specified. This is because AWS CodePipeline manages its build output names
                    instead of AWS CodeBuild.

                    * If ``type`` is set to ``NO_ARTIFACTS`` , this value is ignored if specified,
                    because no build output is produced.

                    * If ``type`` is set to ``S3`` , this is the name of the output artifact object.
                    If you set the name to be a forward slash ("/"), the artifact is stored in the
                    root of the output bucket.

                    For example:

                    * If ``path`` is set to ``MyArtifacts`` , ``namespaceType`` is set to
                    ``BUILD_ID`` , and ``name`` is set to ``MyArtifact.zip`` , then the output
                    artifact is stored in ``MyArtifacts/*build-ID* /MyArtifact.zip`` .

                    * If ``path`` is empty, ``namespaceType`` is set to ``NONE`` , and ``name`` is
                    set to "``/`` ", the output artifact is stored in the root of the output bucket.

                    * If ``path`` is set to ``MyArtifacts`` , ``namespaceType`` is set to
                    ``BUILD_ID`` , and ``name`` is set to "``/`` ", the output artifact is stored in
                    ``MyArtifacts/*build-ID* `` .

                  - **packaging** *(string) --*

                    The type of build output artifact to create:

                    * If ``type`` is set to ``CODEPIPELINE`` , AWS CodePipeline ignores this value
                    if specified. This is because AWS CodePipeline manages its build output
                    artifacts instead of AWS CodeBuild.

                    * If ``type`` is set to ``NO_ARTIFACTS`` , this value is ignored if specified,
                    because no build output is produced.

                    * If ``type`` is set to ``S3`` , valid values include:

                      * ``NONE`` : AWS CodeBuild creates in the output bucket a folder that contains
                      the build output. This is the default if ``packaging`` is not specified.

                      * ``ZIP`` : AWS CodeBuild creates in the output bucket a ZIP file that
                      contains the build output.

                  - **overrideArtifactName** *(boolean) --*

                    If this flag is set, a name specified in the build spec file overrides the
                    artifact name. The name specified in a build spec file is calculated at build
                    time and uses the Shell Command Language. For example, you can append a date and
                    time to your artifact name so that it is always unique.

                  - **encryptionDisabled** *(boolean) --*

                    Set to true if you do not want your output artifacts encrypted. This option is
                    valid only if your artifacts type is Amazon Simple Storage Service (Amazon S3).
                    If this is set with another artifacts type, an invalidInputException is thrown.

                  - **artifactIdentifier** *(string) --*

                    An identifier for this artifact definition.

              - **cache** *(dict) --*

                Information about the cache for the build project.

                - **type** *(string) --*

                  The type of cache used by the build project. Valid values include:

                  * ``NO_CACHE`` : The build project does not use any cache.

                  * ``S3`` : The build project reads and writes from and to S3.

                  * ``LOCAL`` : The build project stores a cache locally on a build host that is
                  only available to that build host.

                - **location** *(string) --*

                  Information about the cache location:

                  * ``NO_CACHE`` or ``LOCAL`` : This value is ignored.

                  * ``S3`` : This is the S3 bucket name/prefix.

                - **modes** *(list) --*

                  If you use a ``LOCAL`` cache, the local cache mode. You can use one or more local
                  cache modes at the same time.

                  * ``LOCAL_SOURCE_CACHE`` mode caches Git metadata for primary and secondary
                  sources. After the cache is created, subsequent builds pull only the change
                  between commits. This mode is a good choice for projects with a clean working
                  directory and a source that is a large Git repository. If you choose this option
                  and your project does not use a Git repository (GitHub, GitHub Enterprise, or
                  Bitbucket), the option is ignored.

                  * ``LOCAL_DOCKER_LAYER_CACHE`` mode caches existing Docker layers. This mode is a
                  good choice for projects that build or pull large Docker images. It can prevent
                  the performance issues caused by pulling large Docker images down from the
                  network.

                  .. note::

                      * You can use a Docker layer cache in the Linux environment only.

                      * The ``privileged`` flag must be set so that your project has the required
                      Docker permissions.

                      * You should consider the security implications before you use a Docker layer
                      cache.

                  * ``LOCAL_CUSTOM_CACHE`` mode caches directories you specify in the buildspec
                  file. This mode is a good choice if your build scenario is not suited to one of
                  the other three local cache modes. If you use a custom cache:

                    * Only directories can be specified for caching. You cannot specify individual
                    files.

                    * Symlinks are used to reference cached directories.

                    * Cached directories are linked to your build before it downloads its project
                    sources. Cached items are overridden if a source item has the same name.
                    Directories are specified using cache paths in the buildspec file.

                  - *(string) --*

              - **environment** *(dict) --*

                Information about the build environment for this build project.

                - **type** *(string) --*

                  The type of build environment to use for related builds.

                  * The environment type ``ARM_CONTAINER`` is available only in regions US East (N.
                  Virginia), US East (Ohio), US West (Oregon), EU (Ireland), Asia Pacific (Mumbai),
                  Asia Pacific (Tokyo), Asia Pacific (Sydney), and EU (Frankfurt).

                  * The environment type ``LINUX_CONTAINER`` with compute type
                  ``build.general1.2xlarge`` is available only in regions US East (N. Virginia), US
                  East (N. Virginia), US West (Oregon), Canada (Central), EU (Ireland), EU (London),
                  EU (Frankfurt), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific
                  (Singapore), Asia Pacific (Sydney), China (Beijing), and China (Ningxia).

                  * The environment type ``LINUX_GPU_CONTAINER`` is available only in regions US
                  East (N. Virginia), US East (N. Virginia), US West (Oregon), Canada (Central), EU
                  (Ireland), EU (London), EU (Frankfurt), Asia Pacific (Tokyo), Asia Pacific
                  (Seoul), Asia Pacific (Singapore), Asia Pacific (Sydney) , China (Beijing), and
                  China (Ningxia).

                - **image** *(string) --*

                  The image tag or image digest that identifies the Docker image to use for this
                  build project. Use the following formats:

                  * For an image tag: ``registry/repository:tag`` . For example, to specify an image
                  with the tag "latest," use ``registry/repository:latest`` .

                  * For an image digest: ``registry/repository@digest`` . For example, to specify an
                  image with the digest
                  "sha256:cbbf2f9a99b47fc460d422812b6a5adff7dfee951d8fa2e4a98caa0382cfbdbf," use
                  ``registry/repository@sha256:cbbf2f9a99b47fc460d422812b6a5adff7dfee951d8fa2e4a98caa0382cfbdbf``
                  .

                - **computeType** *(string) --*

                  Information about the compute resources the build project uses. Available values
                  include:

                  * ``BUILD_GENERAL1_SMALL`` : Use up to 3 GB memory and 2 vCPUs for builds.

                  * ``BUILD_GENERAL1_MEDIUM`` : Use up to 7 GB memory and 4 vCPUs for builds.

                  * ``BUILD_GENERAL1_LARGE`` : Use up to 16 GB memory and 8 vCPUs for builds,
                  depending on your environment type.

                  * ``BUILD_GENERAL1_2XLARGE`` : Use up to 145 GB memory, 72 vCPUs, and 824 GB of
                  SSD storage for builds. This compute type supports Docker images up to 100 GB
                  uncompressed.

                  If you use ``BUILD_GENERAL1_LARGE`` :

                  * For environment type ``LINUX_CONTAINER`` , you can use up to 15 GB memory and 8
                  vCPUs for builds.

                  * For environment type ``LINUX_GPU_CONTAINER`` , you can use up to 255 GB memory,
                  32 vCPUs, and 4 NVIDIA Tesla V100 GPUs for builds.

                  * For environment type ``ARM_CONTAINER`` , you can use up to 16 GB memory and 8
                  vCPUs on ARM-based processors for builds.

                  For more information, see `Build Environment Compute Types
                  <https://docs.aws.amazon.com/codebuild/latest/userguide/build-env-ref-compute-types.html>`__
                  in the *AWS CodeBuild User Guide.*

                - **environmentVariables** *(list) --*

                  A set of environment variables to make available to builds for this build project.

                  - *(dict) --*

                    Information about an environment variable for a build project or a build.

                    - **name** *(string) --*

                      The name or key of the environment variable.

                    - **value** *(string) --*

                      The value of the environment variable.

                      .. warning::

                        We strongly discourage the use of environment variables to store sensitive
                        values, especially AWS secret key IDs and secret access keys. Environment
                        variables can be displayed in plain text using the AWS CodeBuild console and
                        the AWS Command Line Interface (AWS CLI).

                    - **type** *(string) --*

                      The type of environment variable. Valid values include:

                      * ``PARAMETER_STORE`` : An environment variable stored in Amazon EC2 Systems
                      Manager Parameter Store.

                      * ``PLAINTEXT`` : An environment variable in plain text format.

                      * ``SECRETS_MANAGER`` : An environment variable stored in AWS Secrets Manager.

                - **privilegedMode** *(boolean) --*

                  Enables running the Docker daemon inside a Docker container. Set to true only if
                  the build project is used to build Docker images. Otherwise, a build that attempts
                  to interact with the Docker daemon fails. The default setting is ``false`` .

                  You can initialize the Docker daemon during the install phase of your build by
                  adding one of the following sets of commands to the install phase of your
                  buildspec file:

                  If the operating system's base image is Ubuntu Linux:

                   ``- nohup /usr/local/bin/dockerd --host=unix:///var/run/docker.sock
                   --host=tcp://0.0.0.0:2375 --storage-driver=overlay&``

                   ``- timeout 15 sh -c "until docker info; do echo .; sleep 1; done"``

                  If the operating system's base image is Alpine Linux and the previous command does
                  not work, add the ``-t`` argument to ``timeout`` :

                   ``- nohup /usr/local/bin/dockerd --host=unix:///var/run/docker.sock
                   --host=tcp://0.0.0.0:2375 --storage-driver=overlay&``

                   ``- timeout -t 15 sh -c "until docker info; do echo .; sleep 1; done"``

                - **certificate** *(string) --*

                  The certificate to use with this build project.

                - **registryCredential** *(dict) --*

                  The credentials for access to a private registry.

                  - **credential** *(string) --*

                    The Amazon Resource Name (ARN) or name of credentials created using AWS Secrets
                    Manager.

                    .. note::

                      The ``credential`` can use the name of the credentials only if they exist in
                      your current region.

                  - **credentialProvider** *(string) --*

                    The service that created the credentials to access a private Docker registry.
                    The valid value, SECRETS_MANAGER, is for AWS Secrets Manager.

                - **imagePullCredentialsType** *(string) --*

                  The type of credentials AWS CodeBuild uses to pull images in your build. There are
                  two valid values:

                  * ``CODEBUILD`` specifies that AWS CodeBuild uses its own credentials. This
                  requires that you modify your ECR repository policy to trust AWS CodeBuild's
                  service principal.

                  * ``SERVICE_ROLE`` specifies that AWS CodeBuild uses your build project's service
                  role.

                  When you use a cross-account or private registry image, you must use SERVICE_ROLE
                  credentials. When you use an AWS CodeBuild curated image, you must use CODEBUILD
                  credentials.

              - **serviceRole** *(string) --*

                The ARN of the AWS Identity and Access Management (IAM) role that enables AWS
                CodeBuild to interact with dependent AWS services on behalf of the AWS account.

              - **timeoutInMinutes** *(integer) --*

                How long, in minutes, from 5 to 480 (8 hours), for AWS CodeBuild to wait before
                timing out any related build that did not get marked as completed. The default is 60
                minutes.

              - **queuedTimeoutInMinutes** *(integer) --*

                The number of minutes a build is allowed to be queued before it times out.

              - **encryptionKey** *(string) --*

                The AWS Key Management Service (AWS KMS) customer master key (CMK) to be used for
                encrypting the build output artifacts.

                .. note::

                  You can use a cross-account KMS key to encrypt the build output artifacts if your
                  service role has permission to that key.

                You can specify either the Amazon Resource Name (ARN) of the CMK or, if available,
                the CMK's alias (using the format ``alias/*alias-name* `` ).

              - **tags** *(list) --*

                The tags for this build project.

                These tags are available for use by AWS services that support AWS CodeBuild build
                project tags.

                - *(dict) --*

                  A tag, consisting of a key and a value.

                  This tag is available for use by AWS services that support tags in AWS CodeBuild.

                  - **key** *(string) --*

                    The tag's key.

                  - **value** *(string) --*

                    The tag's value.

              - **created** *(datetime) --*

                When the build project was created, expressed in Unix time format.

              - **lastModified** *(datetime) --*

                When the build project's settings were last modified, expressed in Unix time format.

              - **webhook** *(dict) --*

                Information about a webhook that connects repository events to a build project in
                AWS CodeBuild.

                - **url** *(string) --*

                  The URL to the webhook.

                - **payloadUrl** *(string) --*

                  The AWS CodeBuild endpoint where webhook events are sent.

                - **secret** *(string) --*

                  The secret token of the associated repository.

                  .. note::

                    A Bitbucket webhook does not support ``secret`` .

                - **branchFilter** *(string) --*

                  A regular expression used to determine which repository branches are built when a
                  webhook is triggered. If the name of a branch matches the regular expression, then
                  it is built. If ``branchFilter`` is empty, then all branches are built.

                  .. note::

                    It is recommended that you use ``filterGroups`` instead of ``branchFilter`` .

                - **filterGroups** *(list) --*

                  An array of arrays of ``WebhookFilter`` objects used to determine which webhooks
                  are triggered. At least one ``WebhookFilter`` in the array must specify ``EVENT``
                  as its ``type`` .

                  For a build to be triggered, at least one filter group in the ``filterGroups``
                  array must pass. For a filter group to pass, each of its filters must pass.

                  - *(list) --*

                    - *(dict) --*

                      A filter used to determine which webhooks trigger a build.

                      - **type** *(string) --*

                        The type of webhook filter. There are five webhook filter types: ``EVENT`` ,
                        ``ACTOR_ACCOUNT_ID`` , ``HEAD_REF`` , ``BASE_REF`` , and ``FILE_PATH`` .

                          EVENT

                        A webhook event triggers a build when the provided ``pattern`` matches one
                        of four event types: ``PUSH`` , ``PULL_REQUEST_CREATED`` ,
                        ``PULL_REQUEST_UPDATED`` , and ``PULL_REQUEST_REOPENED`` . The ``EVENT``
                        patterns are specified as a comma-separated string. For example, ``PUSH,
                        PULL_REQUEST_CREATED, PULL_REQUEST_UPDATED`` filters all push, pull request
                        created, and pull request updated events.

                        .. note::

                          The ``PULL_REQUEST_REOPENED`` works with GitHub and GitHub Enterprise
                          only.

                          ACTOR_ACCOUNT_ID

                        A webhook event triggers a build when a GitHub, GitHub Enterprise, or
                        Bitbucket account ID matches the regular expression ``pattern`` .

                          HEAD_REF

                        A webhook event triggers a build when the head reference matches the regular
                        expression ``pattern`` . For example, ``refs/heads/branch-name`` and
                        ``refs/tags/tag-name`` .

                        Works with GitHub and GitHub Enterprise push, GitHub and GitHub Enterprise
                        pull request, Bitbucket push, and Bitbucket pull request events.

                          BASE_REF

                        A webhook event triggers a build when the base reference matches the regular
                        expression ``pattern`` . For example, ``refs/heads/branch-name`` .

                        .. note::

                          Works with pull request events only.

                          FILE_PATH

                        A webhook triggers a build when the path of a changed file matches the
                        regular expression ``pattern`` .

                        .. note::

                          Works with GitHub and GitHub Enterprise push events only.

                      - **pattern** *(string) --*

                        For a ``WebHookFilter`` that uses ``EVENT`` type, a comma-separated string
                        that specifies one or more events. For example, the webhook filter ``PUSH,
                        PULL_REQUEST_CREATED, PULL_REQUEST_UPDATED`` allows all push, pull request
                        created, and pull request updated events to trigger a build.

                        For a ``WebHookFilter`` that uses any of the other filter types, a regular
                        expression pattern. For example, a ``WebHookFilter`` that uses ``HEAD_REF``
                        for its ``type`` and the pattern ``^refs/heads/`` triggers a build when the
                        head reference is a branch with a reference name ``refs/heads/branch-name``
                        .

                      - **excludeMatchedPattern** *(boolean) --*

                        Used to indicate that the ``pattern`` determines which webhook events do not
                        trigger a build. If true, then a webhook event that does not match the
                        ``pattern`` triggers a build. If false, then a webhook event that matches
                        the ``pattern`` triggers a build.

                - **lastModifiedSecret** *(datetime) --*

                  A timestamp that indicates the last time a repository's secret token was modified.

              - **vpcConfig** *(dict) --*

                Information about the VPC configuration that AWS CodeBuild accesses.

                - **vpcId** *(string) --*

                  The ID of the Amazon VPC.

                - **subnets** *(list) --*

                  A list of one or more subnet IDs in your Amazon VPC.

                  - *(string) --*

                - **securityGroupIds** *(list) --*

                  A list of one or more security groups IDs in your Amazon VPC.

                  - *(string) --*

              - **badge** *(dict) --*

                Information about the build badge for the build project.

                - **badgeEnabled** *(boolean) --*

                  Set this to true to generate a publicly accessible URL for your project's build
                  badge.

                - **badgeRequestUrl** *(string) --*

                  The publicly-accessible URL through which you can access the build badge for your
                  project.

                  The publicly accessible URL through which you can access the build badge for your
                  project.

              - **logsConfig** *(dict) --*

                Information about logs for the build project. A project can create logs in Amazon
                CloudWatch Logs, an S3 bucket, or both.

                - **cloudWatchLogs** *(dict) --*

                  Information about Amazon CloudWatch Logs for a build project. Amazon CloudWatch
                  Logs are enabled by default.

                  - **status** *(string) --*

                    The current status of the logs in Amazon CloudWatch Logs for a build project.
                    Valid values are:

                    * ``ENABLED`` : Amazon CloudWatch Logs are enabled for this build project.

                    * ``DISABLED`` : Amazon CloudWatch Logs are not enabled for this build project.

                  - **groupName** *(string) --*

                    The group name of the logs in Amazon CloudWatch Logs. For more information, see
                    `Working with Log Groups and Log Streams
                    <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html>`__
                    .

                  - **streamName** *(string) --*

                    The prefix of the stream name of the Amazon CloudWatch Logs. For more
                    information, see `Working with Log Groups and Log Streams
                    <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html>`__
                    .

                - **s3Logs** *(dict) --*

                  Information about logs built to an S3 bucket for a build project. S3 logs are not
                  enabled by default.

                  - **status** *(string) --*

                    The current status of the S3 build logs. Valid values are:

                    * ``ENABLED`` : S3 build logs are enabled for this build project.

                    * ``DISABLED`` : S3 build logs are not enabled for this build project.

                  - **location** *(string) --*

                    The ARN of an S3 bucket and the path prefix for S3 logs. If your Amazon S3
                    bucket name is ``my-bucket`` , and your path prefix is ``build-log`` , then
                    acceptable formats are ``my-bucket/build-log`` or
                    ``arn:aws:s3:::my-bucket/build-log`` .

                  - **encryptionDisabled** *(boolean) --*

                    Set to true if you do not want your S3 build log output encrypted. By default S3
                    build logs are encrypted.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_report_group(
        self, arn: str, exportConfig: ClientUpdateReportGroupExportConfigTypeDef = None
    ) -> ClientUpdateReportGroupResponseTypeDef:
        """
        Updates a report group.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/codebuild-2016-10-06/UpdateReportGroup>`_

        **Request Syntax**
        ::

          response = client.update_report_group(
              arn='string',
              exportConfig={
                  'exportConfigType': 'S3'|'NO_EXPORT',
                  's3Destination': {
                      'bucket': 'string',
                      'path': 'string',
                      'packaging': 'ZIP'|'NONE',
                      'encryptionKey': 'string',
                      'encryptionDisabled': True|False
                  }
              }
          )
        :type arn: string
        :param arn: **[REQUIRED]**

          The ARN of the report group to update.

        :type exportConfig: dict
        :param exportConfig:

          Used to specify an updated export type. Valid values are:

          * ``S3`` : The report results are exported to an S3 bucket.

          * ``NO_EXPORT`` : The report results are not exported.

          - **exportConfigType** *(string) --*

            The export configuration type. Valid values are:

            * ``S3`` : The report results are exported to an S3 bucket.

            * ``NO_EXPORT`` : The report results are not exported.

          - **s3Destination** *(dict) --*

            A ``S3ReportExportConfig`` object that contains information about the S3 bucket where
            the run of a report is exported.

            - **bucket** *(string) --*

              The name of the S3 bucket where the raw data of a report are exported.

            - **path** *(string) --*

              The path to the exported report's raw data results.

            - **packaging** *(string) --*

              The type of build output artifact to create. Valid values include:

              * ``NONE`` : AWS CodeBuild creates the raw data in the output bucket. This is the
              default if packaging is not specified.

              * ``ZIP`` : AWS CodeBuild creates a ZIP file with the raw data in the output bucket.

            - **encryptionKey** *(string) --*

              The encryption key for the report's encrypted raw data.

            - **encryptionDisabled** *(boolean) --*

              A boolean value that specifies if the results of a report are encrypted.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'reportGroup': {
                    'arn': 'string',
                    'name': 'string',
                    'type': 'TEST',
                    'exportConfig': {
                        'exportConfigType': 'S3'|'NO_EXPORT',
                        's3Destination': {
                            'bucket': 'string',
                            'path': 'string',
                            'packaging': 'ZIP'|'NONE',
                            'encryptionKey': 'string',
                            'encryptionDisabled': True|False
                        }
                    },
                    'created': datetime(2015, 1, 1),
                    'lastModified': datetime(2015, 1, 1)
                }
            }
          **Response Structure**

          - *(dict) --*

            - **reportGroup** *(dict) --*

              Information about the updated report group.

              - **arn** *(string) --*

                The ARN of a ``ReportGroup`` .

              - **name** *(string) --*

                The name of a ``ReportGroup`` .

              - **type** *(string) --*

                The type of the ``ReportGroup`` . The one valid value is ``TEST`` .

              - **exportConfig** *(dict) --*

                Information about the destination where the raw data of this ``ReportGroup`` is
                exported.

                - **exportConfigType** *(string) --*

                  The export configuration type. Valid values are:

                  * ``S3`` : The report results are exported to an S3 bucket.

                  * ``NO_EXPORT`` : The report results are not exported.

                - **s3Destination** *(dict) --*

                  A ``S3ReportExportConfig`` object that contains information about the S3 bucket
                  where the run of a report is exported.

                  - **bucket** *(string) --*

                    The name of the S3 bucket where the raw data of a report are exported.

                  - **path** *(string) --*

                    The path to the exported report's raw data results.

                  - **packaging** *(string) --*

                    The type of build output artifact to create. Valid values include:

                    * ``NONE`` : AWS CodeBuild creates the raw data in the output bucket. This is
                    the default if packaging is not specified.

                    * ``ZIP`` : AWS CodeBuild creates a ZIP file with the raw data in the output
                    bucket.

                  - **encryptionKey** *(string) --*

                    The encryption key for the report's encrypted raw data.

                  - **encryptionDisabled** *(boolean) --*

                    A boolean value that specifies if the results of a report are encrypted.

              - **created** *(datetime) --*

                The date and time this ``ReportGroup`` was created.

              - **lastModified** *(datetime) --*

                The date and time this ``ReportGroup`` was last modified.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_webhook(
        self,
        projectName: str,
        branchFilter: str = None,
        rotateSecret: bool = None,
        filterGroups: List[List[ClientUpdateWebhookFilterGroupsTypeDef]] = None,
    ) -> ClientUpdateWebhookResponseTypeDef:
        """
        Updates the webhook associated with an AWS CodeBuild build project.

        .. note::

          If you use Bitbucket for your repository, ``rotateSecret`` is ignored.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/codebuild-2016-10-06/UpdateWebhook>`_

        **Request Syntax**
        ::

          response = client.update_webhook(
              projectName='string',
              branchFilter='string',
              rotateSecret=True|False,
              filterGroups=[
                  [
                      {
                          'type': 'EVENT'|'BASE_REF'|'HEAD_REF'|'ACTOR_ACCOUNT_ID'|'FILE_PATH',
                          'pattern': 'string',
                          'excludeMatchedPattern': True|False
                      },
                  ],
              ]
          )
        :type projectName: string
        :param projectName: **[REQUIRED]**

          The name of the AWS CodeBuild project.

        :type branchFilter: string
        :param branchFilter:

          A regular expression used to determine which repository branches are built when a webhook
          is triggered. If the name of a branch matches the regular expression, then it is built. If
          ``branchFilter`` is empty, then all branches are built.

          .. note::

            It is recommended that you use ``filterGroups`` instead of ``branchFilter`` .

        :type rotateSecret: boolean
        :param rotateSecret:

          A boolean value that specifies whether the associated GitHub repository's secret token
          should be updated. If you use Bitbucket for your repository, ``rotateSecret`` is ignored.

        :type filterGroups: list
        :param filterGroups:

          An array of arrays of ``WebhookFilter`` objects used to determine if a webhook event can
          trigger a build. A filter group must contain at least one ``EVENT``  ``WebhookFilter`` .

          - *(list) --*

            - *(dict) --*

              A filter used to determine which webhooks trigger a build.

              - **type** *(string) --* **[REQUIRED]**

                The type of webhook filter. There are five webhook filter types: ``EVENT`` ,
                ``ACTOR_ACCOUNT_ID`` , ``HEAD_REF`` , ``BASE_REF`` , and ``FILE_PATH`` .

                  EVENT

                A webhook event triggers a build when the provided ``pattern`` matches one of four
                event types: ``PUSH`` , ``PULL_REQUEST_CREATED`` , ``PULL_REQUEST_UPDATED`` , and
                ``PULL_REQUEST_REOPENED`` . The ``EVENT`` patterns are specified as a
                comma-separated string. For example, ``PUSH, PULL_REQUEST_CREATED,
                PULL_REQUEST_UPDATED`` filters all push, pull request created, and pull request
                updated events.

                .. note::

                  The ``PULL_REQUEST_REOPENED`` works with GitHub and GitHub Enterprise only.

                  ACTOR_ACCOUNT_ID

                A webhook event triggers a build when a GitHub, GitHub Enterprise, or Bitbucket
                account ID matches the regular expression ``pattern`` .

                  HEAD_REF

                A webhook event triggers a build when the head reference matches the regular
                expression ``pattern`` . For example, ``refs/heads/branch-name`` and
                ``refs/tags/tag-name`` .

                Works with GitHub and GitHub Enterprise push, GitHub and GitHub Enterprise pull
                request, Bitbucket push, and Bitbucket pull request events.

                  BASE_REF

                A webhook event triggers a build when the base reference matches the regular
                expression ``pattern`` . For example, ``refs/heads/branch-name`` .

                .. note::

                  Works with pull request events only.

                  FILE_PATH

                A webhook triggers a build when the path of a changed file matches the regular
                expression ``pattern`` .

                .. note::

                  Works with GitHub and GitHub Enterprise push events only.

              - **pattern** *(string) --* **[REQUIRED]**

                For a ``WebHookFilter`` that uses ``EVENT`` type, a comma-separated string that
                specifies one or more events. For example, the webhook filter ``PUSH,
                PULL_REQUEST_CREATED, PULL_REQUEST_UPDATED`` allows all push, pull request created,
                and pull request updated events to trigger a build.

                For a ``WebHookFilter`` that uses any of the other filter types, a regular
                expression pattern. For example, a ``WebHookFilter`` that uses ``HEAD_REF`` for its
                ``type`` and the pattern ``^refs/heads/`` triggers a build when the head reference
                is a branch with a reference name ``refs/heads/branch-name`` .

              - **excludeMatchedPattern** *(boolean) --*

                Used to indicate that the ``pattern`` determines which webhook events do not trigger
                a build. If true, then a webhook event that does not match the ``pattern`` triggers
                a build. If false, then a webhook event that matches the ``pattern`` triggers a
                build.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'webhook': {
                    'url': 'string',
                    'payloadUrl': 'string',
                    'secret': 'string',
                    'branchFilter': 'string',
                    'filterGroups': [
                        [
                            {
                                'type':
                                'EVENT'|'BASE_REF'|'HEAD_REF'
                                |'ACTOR_ACCOUNT_ID'|'FILE_PATH',
                                'pattern': 'string',
                                'excludeMatchedPattern': True|False
                            },
                        ],
                    ],
                    'lastModifiedSecret': datetime(2015, 1, 1)
                }
            }
          **Response Structure**

          - *(dict) --*

            - **webhook** *(dict) --*

              Information about a repository's webhook that is associated with a project in AWS
              CodeBuild.

              - **url** *(string) --*

                The URL to the webhook.

              - **payloadUrl** *(string) --*

                The AWS CodeBuild endpoint where webhook events are sent.

              - **secret** *(string) --*

                The secret token of the associated repository.

                .. note::

                  A Bitbucket webhook does not support ``secret`` .

              - **branchFilter** *(string) --*

                A regular expression used to determine which repository branches are built when a
                webhook is triggered. If the name of a branch matches the regular expression, then
                it is built. If ``branchFilter`` is empty, then all branches are built.

                .. note::

                  It is recommended that you use ``filterGroups`` instead of ``branchFilter`` .

              - **filterGroups** *(list) --*

                An array of arrays of ``WebhookFilter`` objects used to determine which webhooks are
                triggered. At least one ``WebhookFilter`` in the array must specify ``EVENT`` as its
                ``type`` .

                For a build to be triggered, at least one filter group in the ``filterGroups`` array
                must pass. For a filter group to pass, each of its filters must pass.

                - *(list) --*

                  - *(dict) --*

                    A filter used to determine which webhooks trigger a build.

                    - **type** *(string) --*

                      The type of webhook filter. There are five webhook filter types: ``EVENT`` ,
                      ``ACTOR_ACCOUNT_ID`` , ``HEAD_REF`` , ``BASE_REF`` , and ``FILE_PATH`` .

                        EVENT

                      A webhook event triggers a build when the provided ``pattern`` matches one of
                      four event types: ``PUSH`` , ``PULL_REQUEST_CREATED`` ,
                      ``PULL_REQUEST_UPDATED`` , and ``PULL_REQUEST_REOPENED`` . The ``EVENT``
                      patterns are specified as a comma-separated string. For example, ``PUSH,
                      PULL_REQUEST_CREATED, PULL_REQUEST_UPDATED`` filters all push, pull request
                      created, and pull request updated events.

                      .. note::

                        The ``PULL_REQUEST_REOPENED`` works with GitHub and GitHub Enterprise only.

                        ACTOR_ACCOUNT_ID

                      A webhook event triggers a build when a GitHub, GitHub Enterprise, or
                      Bitbucket account ID matches the regular expression ``pattern`` .

                        HEAD_REF

                      A webhook event triggers a build when the head reference matches the regular
                      expression ``pattern`` . For example, ``refs/heads/branch-name`` and
                      ``refs/tags/tag-name`` .

                      Works with GitHub and GitHub Enterprise push, GitHub and GitHub Enterprise
                      pull request, Bitbucket push, and Bitbucket pull request events.

                        BASE_REF

                      A webhook event triggers a build when the base reference matches the regular
                      expression ``pattern`` . For example, ``refs/heads/branch-name`` .

                      .. note::

                        Works with pull request events only.

                        FILE_PATH

                      A webhook triggers a build when the path of a changed file matches the regular
                      expression ``pattern`` .

                      .. note::

                        Works with GitHub and GitHub Enterprise push events only.

                    - **pattern** *(string) --*

                      For a ``WebHookFilter`` that uses ``EVENT`` type, a comma-separated string
                      that specifies one or more events. For example, the webhook filter ``PUSH,
                      PULL_REQUEST_CREATED, PULL_REQUEST_UPDATED`` allows all push, pull request
                      created, and pull request updated events to trigger a build.

                      For a ``WebHookFilter`` that uses any of the other filter types, a regular
                      expression pattern. For example, a ``WebHookFilter`` that uses ``HEAD_REF``
                      for its ``type`` and the pattern ``^refs/heads/`` triggers a build when the
                      head reference is a branch with a reference name ``refs/heads/branch-name`` .

                    - **excludeMatchedPattern** *(boolean) --*

                      Used to indicate that the ``pattern`` determines which webhook events do not
                      trigger a build. If true, then a webhook event that does not match the
                      ``pattern`` triggers a build. If false, then a webhook event that matches the
                      ``pattern`` triggers a build.

              - **lastModifiedSecret** *(datetime) --*

                A timestamp that indicates the last time a repository's secret token was modified.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_builds"]
    ) -> paginator_scope.ListBuildsPaginator:
        """
        Get Paginator for `list_builds` operation.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_builds_for_project"]
    ) -> paginator_scope.ListBuildsForProjectPaginator:
        """
        Get Paginator for `list_builds_for_project` operation.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_projects"]
    ) -> paginator_scope.ListProjectsPaginator:
        """
        Get Paginator for `list_projects` operation.
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
    AccountLimitExceededException: Boto3ClientError
    ClientError: Boto3ClientError
    InvalidInputException: Boto3ClientError
    OAuthProviderException: Boto3ClientError
    ResourceAlreadyExistsException: Boto3ClientError
    ResourceNotFoundException: Boto3ClientError
