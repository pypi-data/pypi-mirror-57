"Main interface for codedeploy service Client"
from __future__ import annotations

from typing import Any, Dict, List
from botocore.client import BaseClient
from botocore.exceptions import ClientError as Boto3ClientError
from botocore.paginate import Paginator as Boto3Paginator
from botocore.waiter import Waiter as Boto3Waiter
from mypy_boto3.type_defs import Literal, overload

# pylint: disable=import-self
import mypy_boto3_codedeploy.client as client_scope

# pylint: disable=import-self
import mypy_boto3_codedeploy.paginator as paginator_scope
from mypy_boto3_codedeploy.type_defs import (
    ClientAddTagsToOnPremisesInstancesTagsTypeDef,
    ClientBatchGetApplicationRevisionsResponseTypeDef,
    ClientBatchGetApplicationRevisionsRevisionsTypeDef,
    ClientBatchGetApplicationsResponseTypeDef,
    ClientBatchGetDeploymentGroupsResponseTypeDef,
    ClientBatchGetDeploymentInstancesResponseTypeDef,
    ClientBatchGetDeploymentTargetsResponseTypeDef,
    ClientBatchGetDeploymentsResponseTypeDef,
    ClientBatchGetOnPremisesInstancesResponseTypeDef,
    ClientCreateApplicationResponseTypeDef,
    ClientCreateApplicationTagsTypeDef,
    ClientCreateDeploymentAutoRollbackConfigurationTypeDef,
    ClientCreateDeploymentConfigMinimumHealthyHostsTypeDef,
    ClientCreateDeploymentConfigResponseTypeDef,
    ClientCreateDeploymentConfigTrafficRoutingConfigTypeDef,
    ClientCreateDeploymentGroupAlarmConfigurationTypeDef,
    ClientCreateDeploymentGroupAutoRollbackConfigurationTypeDef,
    ClientCreateDeploymentGroupBlueGreenDeploymentConfigurationTypeDef,
    ClientCreateDeploymentGroupDeploymentStyleTypeDef,
    ClientCreateDeploymentGroupEc2TagFiltersTypeDef,
    ClientCreateDeploymentGroupEc2TagSetTypeDef,
    ClientCreateDeploymentGroupEcsServicesTypeDef,
    ClientCreateDeploymentGroupLoadBalancerInfoTypeDef,
    ClientCreateDeploymentGroupOnPremisesInstanceTagFiltersTypeDef,
    ClientCreateDeploymentGroupOnPremisesTagSetTypeDef,
    ClientCreateDeploymentGroupResponseTypeDef,
    ClientCreateDeploymentGroupTagsTypeDef,
    ClientCreateDeploymentGroupTriggerConfigurationsTypeDef,
    ClientCreateDeploymentResponseTypeDef,
    ClientCreateDeploymentRevisionTypeDef,
    ClientCreateDeploymentTargetInstancesTypeDef,
    ClientDeleteDeploymentGroupResponseTypeDef,
    ClientDeleteGitHubAccountTokenResponseTypeDef,
    ClientGetApplicationResponseTypeDef,
    ClientGetApplicationRevisionResponseTypeDef,
    ClientGetApplicationRevisionRevisionTypeDef,
    ClientGetDeploymentConfigResponseTypeDef,
    ClientGetDeploymentGroupResponseTypeDef,
    ClientGetDeploymentInstanceResponseTypeDef,
    ClientGetDeploymentResponseTypeDef,
    ClientGetDeploymentTargetResponseTypeDef,
    ClientGetOnPremisesInstanceResponseTypeDef,
    ClientListApplicationRevisionsResponseTypeDef,
    ClientListApplicationsResponseTypeDef,
    ClientListDeploymentConfigsResponseTypeDef,
    ClientListDeploymentGroupsResponseTypeDef,
    ClientListDeploymentInstancesResponseTypeDef,
    ClientListDeploymentTargetsResponseTypeDef,
    ClientListDeploymentsCreateTimeRangeTypeDef,
    ClientListDeploymentsResponseTypeDef,
    ClientListGitHubAccountTokenNamesResponseTypeDef,
    ClientListOnPremisesInstancesResponseTypeDef,
    ClientListOnPremisesInstancesTagFiltersTypeDef,
    ClientListTagsForResourceResponseTypeDef,
    ClientPutLifecycleEventHookExecutionStatusResponseTypeDef,
    ClientRegisterApplicationRevisionRevisionTypeDef,
    ClientRemoveTagsFromOnPremisesInstancesTagsTypeDef,
    ClientStopDeploymentResponseTypeDef,
    ClientTagResourceTagsTypeDef,
    ClientUpdateDeploymentGroupAlarmConfigurationTypeDef,
    ClientUpdateDeploymentGroupAutoRollbackConfigurationTypeDef,
    ClientUpdateDeploymentGroupBlueGreenDeploymentConfigurationTypeDef,
    ClientUpdateDeploymentGroupDeploymentStyleTypeDef,
    ClientUpdateDeploymentGroupEc2TagFiltersTypeDef,
    ClientUpdateDeploymentGroupEc2TagSetTypeDef,
    ClientUpdateDeploymentGroupEcsServicesTypeDef,
    ClientUpdateDeploymentGroupLoadBalancerInfoTypeDef,
    ClientUpdateDeploymentGroupOnPremisesInstanceTagFiltersTypeDef,
    ClientUpdateDeploymentGroupOnPremisesTagSetTypeDef,
    ClientUpdateDeploymentGroupResponseTypeDef,
    ClientUpdateDeploymentGroupTriggerConfigurationsTypeDef,
)

# pylint: disable=import-self
import mypy_boto3_codedeploy.waiter as waiter_scope


__all__ = ("Client",)


class Client(BaseClient):
    exceptions: client_scope.Exceptions

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def add_tags_to_on_premises_instances(
        self, tags: List[ClientAddTagsToOnPremisesInstancesTagsTypeDef], instanceNames: List[str]
    ) -> None:
        """
        Adds tags to on-premises instances.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/codedeploy-2014-10-06/AddTagsToOnPremisesInstances>`_

        **Request Syntax**
        ::

          response = client.add_tags_to_on_premises_instances(
              tags=[
                  {
                      'Key': 'string',
                      'Value': 'string'
                  },
              ],
              instanceNames=[
                  'string',
              ]
          )
        :type tags: list
        :param tags: **[REQUIRED]**

          The tag key-value pairs to add to the on-premises instances.

          Keys and values are both required. Keys cannot be null or empty strings. Value-only tags
          are not allowed.

          - *(dict) --*

            Information about a tag.

            - **Key** *(string) --*

              The tag's key.

            - **Value** *(string) --*

              The tag's value.

        :type instanceNames: list
        :param instanceNames: **[REQUIRED]**

          The names of the on-premises instances to which to add tags.

          - *(string) --*

        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def batch_get_application_revisions(
        self,
        applicationName: str,
        revisions: List[ClientBatchGetApplicationRevisionsRevisionsTypeDef],
    ) -> ClientBatchGetApplicationRevisionsResponseTypeDef:
        """
        Gets information about one or more application revisions. The maximum number of application
        revisions that can be returned is 25.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/codedeploy-2014-10-06/BatchGetApplicationRevisions>`_

        **Request Syntax**
        ::

          response = client.batch_get_application_revisions(
              applicationName='string',
              revisions=[
                  {
                      'revisionType': 'S3'|'GitHub'|'String'|'AppSpecContent',
                      's3Location': {
                          'bucket': 'string',
                          'key': 'string',
                          'bundleType': 'tar'|'tgz'|'zip'|'YAML'|'JSON',
                          'version': 'string',
                          'eTag': 'string'
                      },
                      'gitHubLocation': {
                          'repository': 'string',
                          'commitId': 'string'
                      },
                      'string': {
                          'content': 'string',
                          'sha256': 'string'
                      },
                      'appSpecContent': {
                          'content': 'string',
                          'sha256': 'string'
                      }
                  },
              ]
          )
        :type applicationName: string
        :param applicationName: **[REQUIRED]**

          The name of an AWS CodeDeploy application about which to get revision information.

        :type revisions: list
        :param revisions: **[REQUIRED]**

          An array of ``RevisionLocation`` objects that specify information to get about the
          application revisions, including type and location. The maximum number of
          ``RevisionLocation`` objects you can specify is 25.

          - *(dict) --*

            Information about the location of an application revision.

            - **revisionType** *(string) --*

              The type of application revision:

              * S3: An application revision stored in Amazon S3.

              * GitHub: An application revision stored in GitHub (EC2/On-premises deployments only).

              * String: A YAML-formatted or JSON-formatted string (AWS Lambda deployments only).

            - **s3Location** *(dict) --*

              Information about the location of a revision stored in Amazon S3.

              - **bucket** *(string) --*

                The name of the Amazon S3 bucket where the application revision is stored.

              - **key** *(string) --*

                The name of the Amazon S3 object that represents the bundled artifacts for the
                application revision.

              - **bundleType** *(string) --*

                The file type of the application revision. Must be one of the following:

                * tar: A tar archive file.

                * tgz: A compressed tar archive file.

                * zip: A zip archive file.

              - **version** *(string) --*

                A specific version of the Amazon S3 object that represents the bundled artifacts for
                the application revision.

                If the version is not specified, the system uses the most recent version by default.

              - **eTag** *(string) --*

                The ETag of the Amazon S3 object that represents the bundled artifacts for the
                application revision.

                If the ETag is not specified as an input parameter, ETag validation of the object is
                skipped.

            - **gitHubLocation** *(dict) --*

              Information about the location of application artifacts stored in GitHub.

              - **repository** *(string) --*

                The GitHub account and repository pair that stores a reference to the commit that
                represents the bundled artifacts for the application revision.

                Specified as account/repository.

              - **commitId** *(string) --*

                The SHA1 commit ID of the GitHub commit that represents the bundled artifacts for
                the application revision.

            - **string** *(dict) --*

              Information about the location of an AWS Lambda deployment revision stored as a
              RawString.

              - **content** *(string) --*

                The YAML-formatted or JSON-formatted revision string. It includes information about
                which Lambda function to update and optional Lambda functions that validate
                deployment lifecycle events.

              - **sha256** *(string) --*

                The SHA256 hash value of the revision content.

            - **appSpecContent** *(dict) --*

              The content of an AppSpec file for an AWS Lambda or Amazon ECS deployment. The content
              is formatted as JSON or YAML and stored as a RawString.

              - **content** *(string) --*

                The YAML-formatted or JSON-formatted revision string.

                For an AWS Lambda deployment, the content includes a Lambda function name, the alias
                for its original version, and the alias for its replacement version. The deployment
                shifts traffic from the original version of the Lambda function to the replacement
                version.

                For an Amazon ECS deployment, the content includes the task name, information about
                the load balancer that serves traffic to the container, and more.

                For both types of deployments, the content can specify Lambda functions that run at
                specified hooks, such as ``BeforeInstall`` , during a deployment.

              - **sha256** *(string) --*

                The SHA256 hash value of the revision content.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'applicationName': 'string',
                'errorMessage': 'string',
                'revisions': [
                    {
                        'revisionLocation': {
                            'revisionType': 'S3'|'GitHub'|'String'|'AppSpecContent',
                            's3Location': {
                                'bucket': 'string',
                                'key': 'string',
                                'bundleType': 'tar'|'tgz'|'zip'|'YAML'|'JSON',
                                'version': 'string',
                                'eTag': 'string'
                            },
                            'gitHubLocation': {
                                'repository': 'string',
                                'commitId': 'string'
                            },
                            'string': {
                                'content': 'string',
                                'sha256': 'string'
                            },
                            'appSpecContent': {
                                'content': 'string',
                                'sha256': 'string'
                            }
                        },
                        'genericRevisionInfo': {
                            'description': 'string',
                            'deploymentGroups': [
                                'string',
                            ],
                            'firstUsedTime': datetime(2015, 1, 1),
                            'lastUsedTime': datetime(2015, 1, 1),
                            'registerTime': datetime(2015, 1, 1)
                        }
                    },
                ]
            }
          **Response Structure**

          - *(dict) --*

            Represents the output of a BatchGetApplicationRevisions operation.

            - **applicationName** *(string) --*

              The name of the application that corresponds to the revisions.

            - **errorMessage** *(string) --*

              Information about errors that might have occurred during the API call.

            - **revisions** *(list) --*

              Additional information about the revisions, including the type and location.

              - *(dict) --*

                Information about an application revision.

                - **revisionLocation** *(dict) --*

                  Information about the location and type of an application revision.

                  - **revisionType** *(string) --*

                    The type of application revision:

                    * S3: An application revision stored in Amazon S3.

                    * GitHub: An application revision stored in GitHub (EC2/On-premises deployments
                    only).

                    * String: A YAML-formatted or JSON-formatted string (AWS Lambda deployments
                    only).

                  - **s3Location** *(dict) --*

                    Information about the location of a revision stored in Amazon S3.

                    - **bucket** *(string) --*

                      The name of the Amazon S3 bucket where the application revision is stored.

                    - **key** *(string) --*

                      The name of the Amazon S3 object that represents the bundled artifacts for the
                      application revision.

                    - **bundleType** *(string) --*

                      The file type of the application revision. Must be one of the following:

                      * tar: A tar archive file.

                      * tgz: A compressed tar archive file.

                      * zip: A zip archive file.

                    - **version** *(string) --*

                      A specific version of the Amazon S3 object that represents the bundled
                      artifacts for the application revision.

                      If the version is not specified, the system uses the most recent version by
                      default.

                    - **eTag** *(string) --*

                      The ETag of the Amazon S3 object that represents the bundled artifacts for the
                      application revision.

                      If the ETag is not specified as an input parameter, ETag validation of the
                      object is skipped.

                  - **gitHubLocation** *(dict) --*

                    Information about the location of application artifacts stored in GitHub.

                    - **repository** *(string) --*

                      The GitHub account and repository pair that stores a reference to the commit
                      that represents the bundled artifacts for the application revision.

                      Specified as account/repository.

                    - **commitId** *(string) --*

                      The SHA1 commit ID of the GitHub commit that represents the bundled artifacts
                      for the application revision.

                  - **string** *(dict) --*

                    Information about the location of an AWS Lambda deployment revision stored as a
                    RawString.

                    - **content** *(string) --*

                      The YAML-formatted or JSON-formatted revision string. It includes information
                      about which Lambda function to update and optional Lambda functions that
                      validate deployment lifecycle events.

                    - **sha256** *(string) --*

                      The SHA256 hash value of the revision content.

                  - **appSpecContent** *(dict) --*

                    The content of an AppSpec file for an AWS Lambda or Amazon ECS deployment. The
                    content is formatted as JSON or YAML and stored as a RawString.

                    - **content** *(string) --*

                      The YAML-formatted or JSON-formatted revision string.

                      For an AWS Lambda deployment, the content includes a Lambda function name, the
                      alias for its original version, and the alias for its replacement version. The
                      deployment shifts traffic from the original version of the Lambda function to
                      the replacement version.

                      For an Amazon ECS deployment, the content includes the task name, information
                      about the load balancer that serves traffic to the container, and more.

                      For both types of deployments, the content can specify Lambda functions that
                      run at specified hooks, such as ``BeforeInstall`` , during a deployment.

                    - **sha256** *(string) --*

                      The SHA256 hash value of the revision content.

                - **genericRevisionInfo** *(dict) --*

                  Information about an application revision, including usage details and associated
                  deployment groups.

                  - **description** *(string) --*

                    A comment about the revision.

                  - **deploymentGroups** *(list) --*

                    The deployment groups for which this is the current target revision.

                    - *(string) --*

                  - **firstUsedTime** *(datetime) --*

                    When the revision was first used by AWS CodeDeploy.

                  - **lastUsedTime** *(datetime) --*

                    When the revision was last used by AWS CodeDeploy.

                  - **registerTime** *(datetime) --*

                    When the revision was registered with AWS CodeDeploy.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def batch_get_applications(
        self, applicationNames: List[str]
    ) -> ClientBatchGetApplicationsResponseTypeDef:
        """
        Gets information about one or more applications. The maximum number of applications that can
        be returned is 25.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/codedeploy-2014-10-06/BatchGetApplications>`_

        **Request Syntax**
        ::

          response = client.batch_get_applications(
              applicationNames=[
                  'string',
              ]
          )
        :type applicationNames: list
        :param applicationNames: **[REQUIRED]**

          A list of application names separated by spaces. The maximum number of application names
          you can specify is 25.

          - *(string) --*

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'applicationsInfo': [
                    {
                        'applicationId': 'string',
                        'applicationName': 'string',
                        'createTime': datetime(2015, 1, 1),
                        'linkedToGitHub': True|False,
                        'gitHubAccountName': 'string',
                        'computePlatform': 'Server'|'Lambda'|'ECS'
                    },
                ]
            }
          **Response Structure**

          - *(dict) --*

            Represents the output of a BatchGetApplications operation.

            - **applicationsInfo** *(list) --*

              Information about the applications.

              - *(dict) --*

                Information about an application.

                - **applicationId** *(string) --*

                  The application ID.

                - **applicationName** *(string) --*

                  The application name.

                - **createTime** *(datetime) --*

                  The time at which the application was created.

                - **linkedToGitHub** *(boolean) --*

                  True if the user has authenticated with GitHub for the specified application.
                  Otherwise, false.

                - **gitHubAccountName** *(string) --*

                  The name for a connection to a GitHub account.

                - **computePlatform** *(string) --*

                  The destination platform type for deployment of the application (``Lambda`` or
                  ``Server`` ).
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def batch_get_deployment_groups(
        self, applicationName: str, deploymentGroupNames: List[str]
    ) -> ClientBatchGetDeploymentGroupsResponseTypeDef:
        """
        Gets information about one or more deployment groups.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/codedeploy-2014-10-06/BatchGetDeploymentGroups>`_

        **Request Syntax**
        ::

          response = client.batch_get_deployment_groups(
              applicationName='string',
              deploymentGroupNames=[
                  'string',
              ]
          )
        :type applicationName: string
        :param applicationName: **[REQUIRED]**

          The name of an AWS CodeDeploy application associated with the applicable IAM user or AWS
          account.

        :type deploymentGroupNames: list
        :param deploymentGroupNames: **[REQUIRED]**

          The names of the deployment groups.

          - *(string) --*

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'deploymentGroupsInfo': [
                    {
                        'applicationName': 'string',
                        'deploymentGroupId': 'string',
                        'deploymentGroupName': 'string',
                        'deploymentConfigName': 'string',
                        'ec2TagFilters': [
                            {
                                'Key': 'string',
                                'Value': 'string',
                                'Type': 'KEY_ONLY'|'VALUE_ONLY'|'KEY_AND_VALUE'
                            },
                        ],
                        'onPremisesInstanceTagFilters': [
                            {
                                'Key': 'string',
                                'Value': 'string',
                                'Type': 'KEY_ONLY'|'VALUE_ONLY'|'KEY_AND_VALUE'
                            },
                        ],
                        'autoScalingGroups': [
                            {
                                'name': 'string',
                                'hook': 'string'
                            },
                        ],
                        'serviceRoleArn': 'string',
                        'targetRevision': {
                            'revisionType': 'S3'|'GitHub'|'String'|'AppSpecContent',
                            's3Location': {
                                'bucket': 'string',
                                'key': 'string',
                                'bundleType': 'tar'|'tgz'|'zip'|'YAML'|'JSON',
                                'version': 'string',
                                'eTag': 'string'
                            },
                            'gitHubLocation': {
                                'repository': 'string',
                                'commitId': 'string'
                            },
                            'string': {
                                'content': 'string',
                                'sha256': 'string'
                            },
                            'appSpecContent': {
                                'content': 'string',
                                'sha256': 'string'
                            }
                        },
                        'triggerConfigurations': [
                            {
                                'triggerName': 'string',
                                'triggerTargetArn': 'string',
                                'triggerEvents': [
                                    'DeploymentStart'|'DeploymentSuccess'|'DeploymentFailure'
                                    |'DeploymentStop'|'DeploymentRollback'|'DeploymentReady'
                                    |'InstanceStart'|'InstanceSuccess'|'InstanceFailure'
                                    |'InstanceReady',
                                ]
                            },
                        ],
                        'alarmConfiguration': {
                            'enabled': True|False,
                            'ignorePollAlarmFailure': True|False,
                            'alarms': [
                                {
                                    'name': 'string'
                                },
                            ]
                        },
                        'autoRollbackConfiguration': {
                            'enabled': True|False,
                            'events': [
                                'DEPLOYMENT_FAILURE'|'DEPLOYMENT_STOP_ON_ALARM'
                                |'DEPLOYMENT_STOP_ON_REQUEST',
                            ]
                        },
                        'deploymentStyle': {
                            'deploymentType': 'IN_PLACE'|'BLUE_GREEN',
                            'deploymentOption': 'WITH_TRAFFIC_CONTROL'|'WITHOUT_TRAFFIC_CONTROL'
                        },
                        'blueGreenDeploymentConfiguration': {
                            'terminateBlueInstancesOnDeploymentSuccess': {
                                'action': 'TERMINATE'|'KEEP_ALIVE',
                                'terminationWaitTimeInMinutes': 123
                            },
                            'deploymentReadyOption': {
                                'actionOnTimeout': 'CONTINUE_DEPLOYMENT'|'STOP_DEPLOYMENT',
                                'waitTimeInMinutes': 123
                            },
                            'greenFleetProvisioningOption': {
                                'action': 'DISCOVER_EXISTING'|'COPY_AUTO_SCALING_GROUP'
                            }
                        },
                        'loadBalancerInfo': {
                            'elbInfoList': [
                                {
                                    'name': 'string'
                                },
                            ],
                            'targetGroupInfoList': [
                                {
                                    'name': 'string'
                                },
                            ],
                            'targetGroupPairInfoList': [
                                {
                                    'targetGroups': [
                                        {
                                            'name': 'string'
                                        },
                                    ],
                                    'prodTrafficRoute': {
                                        'listenerArns': [
                                            'string',
                                        ]
                                    },
                                    'testTrafficRoute': {
                                        'listenerArns': [
                                            'string',
                                        ]
                                    }
                                },
                            ]
                        },
                        'lastSuccessfulDeployment': {
                            'deploymentId': 'string',
                            'status':
                            'Created'|'Queued'|'InProgress'|'Succeeded'|'Failed'
                            |'Stopped'|'Ready',
                            'endTime': datetime(2015, 1, 1),
                            'createTime': datetime(2015, 1, 1)
                        },
                        'lastAttemptedDeployment': {
                            'deploymentId': 'string',
                            'status':
                            'Created'|'Queued'|'InProgress'|'Succeeded'|'Failed'
                            |'Stopped'|'Ready',
                            'endTime': datetime(2015, 1, 1),
                            'createTime': datetime(2015, 1, 1)
                        },
                        'ec2TagSet': {
                            'ec2TagSetList': [
                                [
                                    {
                                        'Key': 'string',
                                        'Value': 'string',
                                        'Type': 'KEY_ONLY'|'VALUE_ONLY'|'KEY_AND_VALUE'
                                    },
                                ],
                            ]
                        },
                        'onPremisesTagSet': {
                            'onPremisesTagSetList': [
                                [
                                    {
                                        'Key': 'string',
                                        'Value': 'string',
                                        'Type': 'KEY_ONLY'|'VALUE_ONLY'|'KEY_AND_VALUE'
                                    },
                                ],
                            ]
                        },
                        'computePlatform': 'Server'|'Lambda'|'ECS',
                        'ecsServices': [
                            {
                                'serviceName': 'string',
                                'clusterName': 'string'
                            },
                        ]
                    },
                ],
                'errorMessage': 'string'
            }
          **Response Structure**

          - *(dict) --*

            Represents the output of a BatchGetDeploymentGroups operation.

            - **deploymentGroupsInfo** *(list) --*

              Information about the deployment groups.

              - *(dict) --*

                Information about a deployment group.

                - **applicationName** *(string) --*

                  The application name.

                - **deploymentGroupId** *(string) --*

                  The deployment group ID.

                - **deploymentGroupName** *(string) --*

                  The deployment group name.

                - **deploymentConfigName** *(string) --*

                  The deployment configuration name.

                - **ec2TagFilters** *(list) --*

                  The Amazon EC2 tags on which to filter. The deployment group includes EC2
                  instances with any of the specified tags.

                  - *(dict) --*

                    Information about an EC2 tag filter.

                    - **Key** *(string) --*

                      The tag filter key.

                    - **Value** *(string) --*

                      The tag filter value.

                    - **Type** *(string) --*

                      The tag filter type:

                      * KEY_ONLY: Key only.

                      * VALUE_ONLY: Value only.

                      * KEY_AND_VALUE: Key and value.

                - **onPremisesInstanceTagFilters** *(list) --*

                  The on-premises instance tags on which to filter. The deployment group includes
                  on-premises instances with any of the specified tags.

                  - *(dict) --*

                    Information about an on-premises instance tag filter.

                    - **Key** *(string) --*

                      The on-premises instance tag filter key.

                    - **Value** *(string) --*

                      The on-premises instance tag filter value.

                    - **Type** *(string) --*

                      The on-premises instance tag filter type:

                      * KEY_ONLY: Key only.

                      * VALUE_ONLY: Value only.

                      * KEY_AND_VALUE: Key and value.

                - **autoScalingGroups** *(list) --*

                  A list of associated Auto Scaling groups.

                  - *(dict) --*

                    Information about an Auto Scaling group.

                    - **name** *(string) --*

                      The Auto Scaling group name.

                    - **hook** *(string) --*

                      An Auto Scaling lifecycle event hook name.

                - **serviceRoleArn** *(string) --*

                  A service role Amazon Resource Name (ARN) that grants CodeDeploy permission to
                  make calls to AWS services on your behalf. For more information, see `Create a
                  Service Role for AWS CodeDeploy
                  <https://docs.aws.amazon.com/codedeploy/latest/userguide/getting-started-create-service-role.html>`__
                  in the *AWS CodeDeploy User Guide* .

                - **targetRevision** *(dict) --*

                  Information about the deployment group's target revision, including type and
                  location.

                  - **revisionType** *(string) --*

                    The type of application revision:

                    * S3: An application revision stored in Amazon S3.

                    * GitHub: An application revision stored in GitHub (EC2/On-premises deployments
                    only).

                    * String: A YAML-formatted or JSON-formatted string (AWS Lambda deployments
                    only).

                  - **s3Location** *(dict) --*

                    Information about the location of a revision stored in Amazon S3.

                    - **bucket** *(string) --*

                      The name of the Amazon S3 bucket where the application revision is stored.

                    - **key** *(string) --*

                      The name of the Amazon S3 object that represents the bundled artifacts for the
                      application revision.

                    - **bundleType** *(string) --*

                      The file type of the application revision. Must be one of the following:

                      * tar: A tar archive file.

                      * tgz: A compressed tar archive file.

                      * zip: A zip archive file.

                    - **version** *(string) --*

                      A specific version of the Amazon S3 object that represents the bundled
                      artifacts for the application revision.

                      If the version is not specified, the system uses the most recent version by
                      default.

                    - **eTag** *(string) --*

                      The ETag of the Amazon S3 object that represents the bundled artifacts for the
                      application revision.

                      If the ETag is not specified as an input parameter, ETag validation of the
                      object is skipped.

                  - **gitHubLocation** *(dict) --*

                    Information about the location of application artifacts stored in GitHub.

                    - **repository** *(string) --*

                      The GitHub account and repository pair that stores a reference to the commit
                      that represents the bundled artifacts for the application revision.

                      Specified as account/repository.

                    - **commitId** *(string) --*

                      The SHA1 commit ID of the GitHub commit that represents the bundled artifacts
                      for the application revision.

                  - **string** *(dict) --*

                    Information about the location of an AWS Lambda deployment revision stored as a
                    RawString.

                    - **content** *(string) --*

                      The YAML-formatted or JSON-formatted revision string. It includes information
                      about which Lambda function to update and optional Lambda functions that
                      validate deployment lifecycle events.

                    - **sha256** *(string) --*

                      The SHA256 hash value of the revision content.

                  - **appSpecContent** *(dict) --*

                    The content of an AppSpec file for an AWS Lambda or Amazon ECS deployment. The
                    content is formatted as JSON or YAML and stored as a RawString.

                    - **content** *(string) --*

                      The YAML-formatted or JSON-formatted revision string.

                      For an AWS Lambda deployment, the content includes a Lambda function name, the
                      alias for its original version, and the alias for its replacement version. The
                      deployment shifts traffic from the original version of the Lambda function to
                      the replacement version.

                      For an Amazon ECS deployment, the content includes the task name, information
                      about the load balancer that serves traffic to the container, and more.

                      For both types of deployments, the content can specify Lambda functions that
                      run at specified hooks, such as ``BeforeInstall`` , during a deployment.

                    - **sha256** *(string) --*

                      The SHA256 hash value of the revision content.

                - **triggerConfigurations** *(list) --*

                  Information about triggers associated with the deployment group.

                  - *(dict) --*

                    Information about notification triggers for the deployment group.

                    - **triggerName** *(string) --*

                      The name of the notification trigger.

                    - **triggerTargetArn** *(string) --*

                      The ARN of the Amazon Simple Notification Service topic through which
                      notifications about deployment or instance events are sent.

                    - **triggerEvents** *(list) --*

                      The event type or types for which notifications are triggered.

                      - *(string) --*

                - **alarmConfiguration** *(dict) --*

                  A list of alarms associated with the deployment group.

                  - **enabled** *(boolean) --*

                    Indicates whether the alarm configuration is enabled.

                  - **ignorePollAlarmFailure** *(boolean) --*

                    Indicates whether a deployment should continue if information about the current
                    state of alarms cannot be retrieved from Amazon CloudWatch. The default value is
                    false.

                    * true: The deployment proceeds even if alarm status information can't be
                    retrieved from Amazon CloudWatch.

                    * false: The deployment stops if alarm status information can't be retrieved
                    from Amazon CloudWatch.

                  - **alarms** *(list) --*

                    A list of alarms configured for the deployment group. A maximum of 10 alarms can
                    be added to a deployment group.

                    - *(dict) --*

                      Information about an alarm.

                      - **name** *(string) --*

                        The name of the alarm. Maximum length is 255 characters. Each alarm name can
                        be used only once in a list of alarms.

                - **autoRollbackConfiguration** *(dict) --*

                  Information about the automatic rollback configuration associated with the
                  deployment group.

                  - **enabled** *(boolean) --*

                    Indicates whether a defined automatic rollback configuration is currently
                    enabled.

                  - **events** *(list) --*

                    The event type or types that trigger a rollback.

                    - *(string) --*

                - **deploymentStyle** *(dict) --*

                  Information about the type of deployment, either in-place or blue/green, you want
                  to run and whether to route deployment traffic behind a load balancer.

                  - **deploymentType** *(string) --*

                    Indicates whether to run an in-place deployment or a blue/green deployment.

                  - **deploymentOption** *(string) --*

                    Indicates whether to route deployment traffic behind a load balancer.

                - **blueGreenDeploymentConfiguration** *(dict) --*

                  Information about blue/green deployment options for a deployment group.

                  - **terminateBlueInstancesOnDeploymentSuccess** *(dict) --*

                    Information about whether to terminate instances in the original fleet during a
                    blue/green deployment.

                    - **action** *(string) --*

                      The action to take on instances in the original environment after a successful
                      blue/green deployment.

                      * TERMINATE: Instances are terminated after a specified wait time.

                      * KEEP_ALIVE: Instances are left running after they are deregistered from the
                      load balancer and removed from the deployment group.

                    - **terminationWaitTimeInMinutes** *(integer) --*

                      For an Amazon EC2 deployment, the number of minutes to wait after a successful
                      blue/green deployment before terminating instances from the original
                      environment.

                      For an Amazon ECS deployment, the number of minutes before deleting the
                      original (blue) task set. During an Amazon ECS deployment, CodeDeploy shifts
                      traffic from the original (blue) task set to a replacement (green) task set.

                      The maximum setting is 2880 minutes (2 days).

                  - **deploymentReadyOption** *(dict) --*

                    Information about the action to take when newly provisioned instances are ready
                    to receive traffic in a blue/green deployment.

                    - **actionOnTimeout** *(string) --*

                      Information about when to reroute traffic from an original environment to a
                      replacement environment in a blue/green deployment.

                      * CONTINUE_DEPLOYMENT: Register new instances with the load balancer
                      immediately after the new application revision is installed on the instances
                      in the replacement environment.

                      * STOP_DEPLOYMENT: Do not register new instances with a load balancer unless
                      traffic rerouting is started using  ContinueDeployment . If traffic rerouting
                      is not started before the end of the specified wait period, the deployment
                      status is changed to Stopped.

                    - **waitTimeInMinutes** *(integer) --*

                      The number of minutes to wait before the status of a blue/green deployment is
                      changed to Stopped if rerouting is not started manually. Applies only to the
                      STOP_DEPLOYMENT option for actionOnTimeout

                  - **greenFleetProvisioningOption** *(dict) --*

                    Information about how instances are provisioned for a replacement environment in
                    a blue/green deployment.

                    - **action** *(string) --*

                      The method used to add instances to a replacement environment.

                      * DISCOVER_EXISTING: Use instances that already exist or will be created
                      manually.

                      * COPY_AUTO_SCALING_GROUP: Use settings from a specified Auto Scaling group to
                      define and create instances in a new Auto Scaling group.

                - **loadBalancerInfo** *(dict) --*

                  Information about the load balancer to use in a deployment.

                  - **elbInfoList** *(list) --*

                    An array that contains information about the load balancer to use for load
                    balancing in a deployment. In Elastic Load Balancing, load balancers are used
                    with Classic Load Balancers.

                    .. note::

                      Adding more than one load balancer to the array is not supported.

                    - *(dict) --*

                      Information about a load balancer in Elastic Load Balancing to use in a
                      deployment. Instances are registered directly with a load balancer, and
                      traffic is routed to the load balancer.

                      - **name** *(string) --*

                        For blue/green deployments, the name of the load balancer that is used to
                        route traffic from original instances to replacement instances in a
                        blue/green deployment. For in-place deployments, the name of the load
                        balancer that instances are deregistered from so they are not serving
                        traffic during a deployment, and then re-registered with after the
                        deployment is complete.

                  - **targetGroupInfoList** *(list) --*

                    An array that contains information about the target group to use for load
                    balancing in a deployment. In Elastic Load Balancing, target groups are used
                    with Application Load Balancers.

                    .. note::

                      Adding more than one target group to the array is not supported.

                    - *(dict) --*

                      Information about a target group in Elastic Load Balancing to use in a
                      deployment. Instances are registered as targets in a target group, and traffic
                      is routed to the target group.

                      - **name** *(string) --*

                        For blue/green deployments, the name of the target group that instances in
                        the original environment are deregistered from, and instances in the
                        replacement environment are registered with. For in-place deployments, the
                        name of the target group that instances are deregistered from, so they are
                        not serving traffic during a deployment, and then re-registered with after
                        the deployment is complete.

                  - **targetGroupPairInfoList** *(list) --*

                    The target group pair information. This is an array of ``TargeGroupPairInfo``
                    objects with a maximum size of one.

                    - *(dict) --*

                      Information about two target groups and how traffic is routed during an Amazon
                      ECS deployment. An optional test traffic route can be specified.

                      - **targetGroups** *(list) --*

                        One pair of target groups. One is associated with the original task set. The
                        second is associated with the task set that serves traffic after the
                        deployment is complete.

                        - *(dict) --*

                          Information about a target group in Elastic Load Balancing to use in a
                          deployment. Instances are registered as targets in a target group, and
                          traffic is routed to the target group.

                          - **name** *(string) --*

                            For blue/green deployments, the name of the target group that instances
                            in the original environment are deregistered from, and instances in the
                            replacement environment are registered with. For in-place deployments,
                            the name of the target group that instances are deregistered from, so
                            they are not serving traffic during a deployment, and then re-registered
                            with after the deployment is complete.

                      - **prodTrafficRoute** *(dict) --*

                        The path used by a load balancer to route production traffic when an Amazon
                        ECS deployment is complete.

                        - **listenerArns** *(list) --*

                          The ARN of one listener. The listener identifies the route between a
                          target group and a load balancer. This is an array of strings with a
                          maximum size of one.

                          - *(string) --*

                      - **testTrafficRoute** *(dict) --*

                        An optional path used by a load balancer to route test traffic after an
                        Amazon ECS deployment. Validation can occur while test traffic is served
                        during a deployment.

                        - **listenerArns** *(list) --*

                          The ARN of one listener. The listener identifies the route between a
                          target group and a load balancer. This is an array of strings with a
                          maximum size of one.

                          - *(string) --*

                - **lastSuccessfulDeployment** *(dict) --*

                  Information about the most recent successful deployment to the deployment group.

                  - **deploymentId** *(string) --*

                    The unique ID of a deployment.

                  - **status** *(string) --*

                    The status of the most recent deployment.

                  - **endTime** *(datetime) --*

                    A timestamp that indicates when the most recent deployment to the deployment
                    group was complete.

                  - **createTime** *(datetime) --*

                    A timestamp that indicates when the most recent deployment to the deployment
                    group started.

                - **lastAttemptedDeployment** *(dict) --*

                  Information about the most recent attempted deployment to the deployment group.

                  - **deploymentId** *(string) --*

                    The unique ID of a deployment.

                  - **status** *(string) --*

                    The status of the most recent deployment.

                  - **endTime** *(datetime) --*

                    A timestamp that indicates when the most recent deployment to the deployment
                    group was complete.

                  - **createTime** *(datetime) --*

                    A timestamp that indicates when the most recent deployment to the deployment
                    group started.

                - **ec2TagSet** *(dict) --*

                  Information about groups of tags applied to an EC2 instance. The deployment group
                  includes only EC2 instances identified by all of the tag groups. Cannot be used in
                  the same call as ec2TagFilters.

                  - **ec2TagSetList** *(list) --*

                    A list that contains other lists of EC2 instance tag groups. For an instance to
                    be included in the deployment group, it must be identified by all of the tag
                    groups in the list.

                    - *(list) --*

                      - *(dict) --*

                        Information about an EC2 tag filter.

                        - **Key** *(string) --*

                          The tag filter key.

                        - **Value** *(string) --*

                          The tag filter value.

                        - **Type** *(string) --*

                          The tag filter type:

                          * KEY_ONLY: Key only.

                          * VALUE_ONLY: Value only.

                          * KEY_AND_VALUE: Key and value.

                - **onPremisesTagSet** *(dict) --*

                  Information about groups of tags applied to an on-premises instance. The
                  deployment group includes only on-premises instances identified by all the tag
                  groups. Cannot be used in the same call as onPremisesInstanceTagFilters.

                  - **onPremisesTagSetList** *(list) --*

                    A list that contains other lists of on-premises instance tag groups. For an
                    instance to be included in the deployment group, it must be identified by all of
                    the tag groups in the list.

                    - *(list) --*

                      - *(dict) --*

                        Information about an on-premises instance tag filter.

                        - **Key** *(string) --*

                          The on-premises instance tag filter key.

                        - **Value** *(string) --*

                          The on-premises instance tag filter value.

                        - **Type** *(string) --*

                          The on-premises instance tag filter type:

                          * KEY_ONLY: Key only.

                          * VALUE_ONLY: Value only.

                          * KEY_AND_VALUE: Key and value.

                - **computePlatform** *(string) --*

                  The destination platform type for the deployment (``Lambda`` , ``Server`` , or
                  ``ECS`` ).

                - **ecsServices** *(list) --*

                  The target Amazon ECS services in the deployment group. This applies only to
                  deployment groups that use the Amazon ECS compute platform. A target Amazon ECS
                  service is specified as an Amazon ECS cluster and service name pair using the
                  format ``<clustername>:<servicename>`` .

                  - *(dict) --*

                    Contains the service and cluster names used to identify an Amazon ECS
                    deployment's target.

                    - **serviceName** *(string) --*

                      The name of the target Amazon ECS service.

                    - **clusterName** *(string) --*

                      The name of the cluster that the Amazon ECS service is associated with.

            - **errorMessage** *(string) --*

              Information about errors that might have occurred during the API call.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def batch_get_deployment_instances(
        self, deploymentId: str, instanceIds: List[str]
    ) -> ClientBatchGetDeploymentInstancesResponseTypeDef:
        """
        .. note::

          This method works, but is deprecated. Use ``BatchGetDeploymentTargets`` instead.

        Returns an array of one or more instances associated with a deployment. This method works
        with EC2/On-premises and AWS Lambda compute platforms. The newer
        ``BatchGetDeploymentTargets`` works with all compute platforms. The maximum number of
        instances that can be returned is 25.

        .. danger::

            This operation is deprecated and may not function as expected. This operation should not
            be used going forward and is only kept for the purpose of backwards compatiblity.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/codedeploy-2014-10-06/BatchGetDeploymentInstances>`_

        **Request Syntax**
        ::

          response = client.batch_get_deployment_instances(
              deploymentId='string',
              instanceIds=[
                  'string',
              ]
          )
        :type deploymentId: string
        :param deploymentId: **[REQUIRED]**

          The unique ID of a deployment.

        :type instanceIds: list
        :param instanceIds: **[REQUIRED]**

          The unique IDs of instances used in the deployment. The maximum number of instance IDs you
          can specify is 25.

          - *(string) --*

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'instancesSummary': [
                    {
                        'deploymentId': 'string',
                        'instanceId': 'string',
                        'status':
                        'Pending'|'InProgress'|'Succeeded'|'Failed'|'Skipped'
                        |'Unknown'|'Ready',
                        'lastUpdatedAt': datetime(2015, 1, 1),
                        'lifecycleEvents': [
                            {
                                'lifecycleEventName': 'string',
                                'diagnostics': {
                                    'errorCode':
                                    'Success'|'ScriptMissing'
                                    |'ScriptNotExecutable'
                                    |'ScriptTimedOut'|'ScriptFailed'
                                    |'UnknownError',
                                    'scriptName': 'string',
                                    'message': 'string',
                                    'logTail': 'string'
                                },
                                'startTime': datetime(2015, 1, 1),
                                'endTime': datetime(2015, 1, 1),
                                'status':
                                'Pending'|'InProgress'|'Succeeded'|'Failed'
                                |'Skipped'|'Unknown'
                            },
                        ],
                        'instanceType': 'Blue'|'Green'
                    },
                ],
                'errorMessage': 'string'
            }
          **Response Structure**

          - *(dict) --*

            Represents the output of a BatchGetDeploymentInstances operation.

            - **instancesSummary** *(list) --*

              Information about the instance.

              - *(dict) --*

                Information about an instance in a deployment.

                - **deploymentId** *(string) --*

                  The unique ID of a deployment.

                - **instanceId** *(string) --*

                  The instance ID.

                - **status** *(string) --*

                  The deployment status for this instance:

                  * Pending: The deployment is pending for this instance.

                  * In Progress: The deployment is in progress for this instance.

                  * Succeeded: The deployment has succeeded for this instance.

                  * Failed: The deployment has failed for this instance.

                  * Skipped: The deployment has been skipped for this instance.

                  * Unknown: The deployment status is unknown for this instance.

                - **lastUpdatedAt** *(datetime) --*

                  A timestamp that indicaties when the instance information was last updated.

                - **lifecycleEvents** *(list) --*

                  A list of lifecycle events for this instance.

                  - *(dict) --*

                    Information about a deployment lifecycle event.

                    - **lifecycleEventName** *(string) --*

                      The deployment lifecycle event name, such as ApplicationStop, BeforeInstall,
                      AfterInstall, ApplicationStart, or ValidateService.

                    - **diagnostics** *(dict) --*

                      Diagnostic information about the deployment lifecycle event.

                      - **errorCode** *(string) --*

                        The associated error code:

                        * Success: The specified script ran.

                        * ScriptMissing: The specified script was not found in the specified
                        location.

                        * ScriptNotExecutable: The specified script is not a recognized executable
                        file type.

                        * ScriptTimedOut: The specified script did not finish running in the
                        specified time period.

                        * ScriptFailed: The specified script failed to run as expected.

                        * UnknownError: The specified script did not run for an unknown reason.

                      - **scriptName** *(string) --*

                        The name of the script.

                      - **message** *(string) --*

                        The message associated with the error.

                      - **logTail** *(string) --*

                        The last portion of the diagnostic log.

                        If available, AWS CodeDeploy returns up to the last 4 KB of the diagnostic
                        log.

                    - **startTime** *(datetime) --*

                      A timestamp that indicates when the deployment lifecycle event started.

                    - **endTime** *(datetime) --*

                      A timestamp that indicates when the deployment lifecycle event ended.

                    - **status** *(string) --*

                      The deployment lifecycle event status:

                      * Pending: The deployment lifecycle event is pending.

                      * InProgress: The deployment lifecycle event is in progress.

                      * Succeeded: The deployment lifecycle event ran successfully.

                      * Failed: The deployment lifecycle event has failed.

                      * Skipped: The deployment lifecycle event has been skipped.

                      * Unknown: The deployment lifecycle event is unknown.

                - **instanceType** *(string) --*

                  Information about which environment an instance belongs to in a blue/green
                  deployment.

                  * BLUE: The instance is part of the original environment.

                  * GREEN: The instance is part of the replacement environment.

            - **errorMessage** *(string) --*

              Information about errors that might have occurred during the API call.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def batch_get_deployment_targets(
        self, deploymentId: str = None, targetIds: List[str] = None
    ) -> ClientBatchGetDeploymentTargetsResponseTypeDef:
        """
        Returns an array of one or more targets associated with a deployment. This method works with
        all compute types and should be used instead of the deprecated
        ``BatchGetDeploymentInstances`` . The maximum number of targets that can be returned is 25.

        The type of targets returned depends on the deployment's compute platform:

        * **EC2/On-premises** : Information about EC2 instance targets.

        * **AWS Lambda** : Information about Lambda functions targets.

        * **Amazon ECS** : Information about Amazon ECS service targets.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/codedeploy-2014-10-06/BatchGetDeploymentTargets>`_

        **Request Syntax**
        ::

          response = client.batch_get_deployment_targets(
              deploymentId='string',
              targetIds=[
                  'string',
              ]
          )
        :type deploymentId: string
        :param deploymentId:

          The unique ID of a deployment.

        :type targetIds: list
        :param targetIds:

          The unique IDs of the deployment targets. The compute platform of the deployment
          determines the type of the targets and their formats. The maximum number of deployment
          target IDs you can specify is 25.

          * For deployments that use the EC2/On-premises compute platform, the target IDs are EC2 or
          on-premises instances IDs, and their target type is ``instanceTarget`` .

          * For deployments that use the AWS Lambda compute platform, the target IDs are the names
          of Lambda functions, and their target type is ``instanceTarget`` .

          * For deployments that use the Amazon ECS compute platform, the target IDs are pairs of
          Amazon ECS clusters and services specified using the format
          ``<clustername>:<servicename>`` . Their target type is ``ecsTarget`` .

          - *(string) --*

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'deploymentTargets': [
                    {
                        'deploymentTargetType': 'InstanceTarget'|'LambdaTarget'|'ECSTarget',
                        'instanceTarget': {
                            'deploymentId': 'string',
                            'targetId': 'string',
                            'targetArn': 'string',
                            'status':
                            'Pending'|'InProgress'|'Succeeded'|'Failed'
                            |'Skipped'|'Unknown'|'Ready',
                            'lastUpdatedAt': datetime(2015, 1, 1),
                            'lifecycleEvents': [
                                {
                                    'lifecycleEventName': 'string',
                                    'diagnostics': {
                                        'errorCode':
                                        'Success'|'ScriptMissing'
                                        |'ScriptNotExecutable'
                                        |'ScriptTimedOut'
                                        |'ScriptFailed'
                                        |'UnknownError',
                                        'scriptName': 'string',
                                        'message': 'string',
                                        'logTail': 'string'
                                    },
                                    'startTime': datetime(2015, 1, 1),
                                    'endTime': datetime(2015, 1, 1),
                                    'status':
                                    'Pending'|'InProgress'|'Succeeded'
                                    |'Failed'|'Skipped'|'Unknown'
                                },
                            ],
                            'instanceLabel': 'Blue'|'Green'
                        },
                        'lambdaTarget': {
                            'deploymentId': 'string',
                            'targetId': 'string',
                            'targetArn': 'string',
                            'status':
                            'Pending'|'InProgress'|'Succeeded'|'Failed'
                            |'Skipped'|'Unknown'|'Ready',
                            'lastUpdatedAt': datetime(2015, 1, 1),
                            'lifecycleEvents': [
                                {
                                    'lifecycleEventName': 'string',
                                    'diagnostics': {
                                        'errorCode':
                                        'Success'|'ScriptMissing'
                                        |'ScriptNotExecutable'
                                        |'ScriptTimedOut'
                                        |'ScriptFailed'
                                        |'UnknownError',
                                        'scriptName': 'string',
                                        'message': 'string',
                                        'logTail': 'string'
                                    },
                                    'startTime': datetime(2015, 1, 1),
                                    'endTime': datetime(2015, 1, 1),
                                    'status':
                                    'Pending'|'InProgress'|'Succeeded'
                                    |'Failed'|'Skipped'|'Unknown'
                                },
                            ],
                            'lambdaFunctionInfo': {
                                'functionName': 'string',
                                'functionAlias': 'string',
                                'currentVersion': 'string',
                                'targetVersion': 'string',
                                'targetVersionWeight': 123.0
                            }
                        },
                        'ecsTarget': {
                            'deploymentId': 'string',
                            'targetId': 'string',
                            'targetArn': 'string',
                            'lastUpdatedAt': datetime(2015, 1, 1),
                            'lifecycleEvents': [
                                {
                                    'lifecycleEventName': 'string',
                                    'diagnostics': {
                                        'errorCode':
                                        'Success'|'ScriptMissing'
                                        |'ScriptNotExecutable'
                                        |'ScriptTimedOut'
                                        |'ScriptFailed'
                                        |'UnknownError',
                                        'scriptName': 'string',
                                        'message': 'string',
                                        'logTail': 'string'
                                    },
                                    'startTime': datetime(2015, 1, 1),
                                    'endTime': datetime(2015, 1, 1),
                                    'status':
                                    'Pending'|'InProgress'|'Succeeded'
                                    |'Failed'|'Skipped'|'Unknown'
                                },
                            ],
                            'status':
                            'Pending'|'InProgress'|'Succeeded'|'Failed'
                            |'Skipped'|'Unknown'|'Ready',
                            'taskSetsInfo': [
                                {
                                    'identifer': 'string',
                                    'desiredCount': 123,
                                    'pendingCount': 123,
                                    'runningCount': 123,
                                    'status': 'string',
                                    'trafficWeight': 123.0,
                                    'targetGroup': {
                                        'name': 'string'
                                    },
                                    'taskSetLabel': 'Blue'|'Green'
                                },
                            ]
                        }
                    },
                ]
            }
          **Response Structure**

          - *(dict) --*

            - **deploymentTargets** *(list) --*

              A list of target objects for a deployment. Each target object contains details about
              the target, such as its status and lifecycle events. The type of the target objects
              depends on the deployment' compute platform.

              * **EC2/On-premises** : Each target object is an EC2 or on-premises instance.

              * **AWS Lambda** : The target object is a specific version of an AWS Lambda function.

              * **Amazon ECS** : The target object is an Amazon ECS service.

              - *(dict) --*

                Information about the deployment target.

                - **deploymentTargetType** *(string) --*

                  The deployment type that is specific to the deployment's compute platform.

                - **instanceTarget** *(dict) --*

                  Information about the target for a deployment that uses the EC2/On-premises
                  compute platform.

                  - **deploymentId** *(string) --*

                    The unique ID of a deployment.

                  - **targetId** *(string) --*

                    The unique ID of a deployment target that has a type of ``instanceTarget`` .

                  - **targetArn** *(string) --*

                    The ARN of the target.

                  - **status** *(string) --*

                    The status an EC2/On-premises deployment's target instance.

                  - **lastUpdatedAt** *(datetime) --*

                    The date and time when the target instance was updated by a deployment.

                  - **lifecycleEvents** *(list) --*

                    The lifecycle events of the deployment to this target instance.

                    - *(dict) --*

                      Information about a deployment lifecycle event.

                      - **lifecycleEventName** *(string) --*

                        The deployment lifecycle event name, such as ApplicationStop, BeforeInstall,
                        AfterInstall, ApplicationStart, or ValidateService.

                      - **diagnostics** *(dict) --*

                        Diagnostic information about the deployment lifecycle event.

                        - **errorCode** *(string) --*

                          The associated error code:

                          * Success: The specified script ran.

                          * ScriptMissing: The specified script was not found in the specified
                          location.

                          * ScriptNotExecutable: The specified script is not a recognized executable
                          file type.

                          * ScriptTimedOut: The specified script did not finish running in the
                          specified time period.

                          * ScriptFailed: The specified script failed to run as expected.

                          * UnknownError: The specified script did not run for an unknown reason.

                        - **scriptName** *(string) --*

                          The name of the script.

                        - **message** *(string) --*

                          The message associated with the error.

                        - **logTail** *(string) --*

                          The last portion of the diagnostic log.

                          If available, AWS CodeDeploy returns up to the last 4 KB of the diagnostic
                          log.

                      - **startTime** *(datetime) --*

                        A timestamp that indicates when the deployment lifecycle event started.

                      - **endTime** *(datetime) --*

                        A timestamp that indicates when the deployment lifecycle event ended.

                      - **status** *(string) --*

                        The deployment lifecycle event status:

                        * Pending: The deployment lifecycle event is pending.

                        * InProgress: The deployment lifecycle event is in progress.

                        * Succeeded: The deployment lifecycle event ran successfully.

                        * Failed: The deployment lifecycle event has failed.

                        * Skipped: The deployment lifecycle event has been skipped.

                        * Unknown: The deployment lifecycle event is unknown.

                  - **instanceLabel** *(string) --*

                    A label that identifies whether the instance is an original target (``BLUE`` )
                    or a replacement target (``GREEN`` ).

                - **lambdaTarget** *(dict) --*

                  Information about the target for a deployment that uses the AWS Lambda compute
                  platform.

                  - **deploymentId** *(string) --*

                    The unique ID of a deployment.

                  - **targetId** *(string) --*

                    The unique ID of a deployment target that has a type of ``lambdaTarget`` .

                  - **targetArn** *(string) --*

                    The ARN of the target.

                  - **status** *(string) --*

                    The status an AWS Lambda deployment's target Lambda function.

                  - **lastUpdatedAt** *(datetime) --*

                    The date and time when the target Lambda function was updated by a deployment.

                  - **lifecycleEvents** *(list) --*

                    The lifecycle events of the deployment to this target Lambda function.

                    - *(dict) --*

                      Information about a deployment lifecycle event.

                      - **lifecycleEventName** *(string) --*

                        The deployment lifecycle event name, such as ApplicationStop, BeforeInstall,
                        AfterInstall, ApplicationStart, or ValidateService.

                      - **diagnostics** *(dict) --*

                        Diagnostic information about the deployment lifecycle event.

                        - **errorCode** *(string) --*

                          The associated error code:

                          * Success: The specified script ran.

                          * ScriptMissing: The specified script was not found in the specified
                          location.

                          * ScriptNotExecutable: The specified script is not a recognized executable
                          file type.

                          * ScriptTimedOut: The specified script did not finish running in the
                          specified time period.

                          * ScriptFailed: The specified script failed to run as expected.

                          * UnknownError: The specified script did not run for an unknown reason.

                        - **scriptName** *(string) --*

                          The name of the script.

                        - **message** *(string) --*

                          The message associated with the error.

                        - **logTail** *(string) --*

                          The last portion of the diagnostic log.

                          If available, AWS CodeDeploy returns up to the last 4 KB of the diagnostic
                          log.

                      - **startTime** *(datetime) --*

                        A timestamp that indicates when the deployment lifecycle event started.

                      - **endTime** *(datetime) --*

                        A timestamp that indicates when the deployment lifecycle event ended.

                      - **status** *(string) --*

                        The deployment lifecycle event status:

                        * Pending: The deployment lifecycle event is pending.

                        * InProgress: The deployment lifecycle event is in progress.

                        * Succeeded: The deployment lifecycle event ran successfully.

                        * Failed: The deployment lifecycle event has failed.

                        * Skipped: The deployment lifecycle event has been skipped.

                        * Unknown: The deployment lifecycle event is unknown.

                  - **lambdaFunctionInfo** *(dict) --*

                    A ``LambdaFunctionInfo`` object that describes a target Lambda function.

                    - **functionName** *(string) --*

                      The name of a Lambda function.

                    - **functionAlias** *(string) --*

                      The alias of a Lambda function. For more information, see `Introduction to AWS
                      Lambda Aliases
                      <https://docs.aws.amazon.com/lambda/latest/dg/aliases-intro.html>`__ .

                    - **currentVersion** *(string) --*

                      The version of a Lambda function that production traffic points to.

                    - **targetVersion** *(string) --*

                      The version of a Lambda function that production traffic points to after the
                      Lambda function is deployed.

                    - **targetVersionWeight** *(float) --*

                      The percentage of production traffic that the target version of a Lambda
                      function receives.

                - **ecsTarget** *(dict) --*

                  Information about the target for a deployment that uses the Amazon ECS compute
                  platform.

                  - **deploymentId** *(string) --*

                    The unique ID of a deployment.

                  - **targetId** *(string) --*

                    The unique ID of a deployment target that has a type of ``ecsTarget`` .

                  - **targetArn** *(string) --*

                    The ARN of the target.

                  - **lastUpdatedAt** *(datetime) --*

                    The date and time when the target Amazon ECS application was updated by a
                    deployment.

                  - **lifecycleEvents** *(list) --*

                    The lifecycle events of the deployment to this target Amazon ECS application.

                    - *(dict) --*

                      Information about a deployment lifecycle event.

                      - **lifecycleEventName** *(string) --*

                        The deployment lifecycle event name, such as ApplicationStop, BeforeInstall,
                        AfterInstall, ApplicationStart, or ValidateService.

                      - **diagnostics** *(dict) --*

                        Diagnostic information about the deployment lifecycle event.

                        - **errorCode** *(string) --*

                          The associated error code:

                          * Success: The specified script ran.

                          * ScriptMissing: The specified script was not found in the specified
                          location.

                          * ScriptNotExecutable: The specified script is not a recognized executable
                          file type.

                          * ScriptTimedOut: The specified script did not finish running in the
                          specified time period.

                          * ScriptFailed: The specified script failed to run as expected.

                          * UnknownError: The specified script did not run for an unknown reason.

                        - **scriptName** *(string) --*

                          The name of the script.

                        - **message** *(string) --*

                          The message associated with the error.

                        - **logTail** *(string) --*

                          The last portion of the diagnostic log.

                          If available, AWS CodeDeploy returns up to the last 4 KB of the diagnostic
                          log.

                      - **startTime** *(datetime) --*

                        A timestamp that indicates when the deployment lifecycle event started.

                      - **endTime** *(datetime) --*

                        A timestamp that indicates when the deployment lifecycle event ended.

                      - **status** *(string) --*

                        The deployment lifecycle event status:

                        * Pending: The deployment lifecycle event is pending.

                        * InProgress: The deployment lifecycle event is in progress.

                        * Succeeded: The deployment lifecycle event ran successfully.

                        * Failed: The deployment lifecycle event has failed.

                        * Skipped: The deployment lifecycle event has been skipped.

                        * Unknown: The deployment lifecycle event is unknown.

                  - **status** *(string) --*

                    The status an Amazon ECS deployment's target ECS application.

                  - **taskSetsInfo** *(list) --*

                    The ``ECSTaskSet`` objects associated with the ECS target.

                    - *(dict) --*

                      Information about a set of Amazon ECS tasks in an AWS CodeDeploy deployment.
                      An Amazon ECS task set includes details such as the desired number of tasks,
                      how many tasks are running, and whether the task set serves production
                      traffic. An AWS CodeDeploy application that uses the Amazon ECS compute
                      platform deploys a containerized application in an Amazon ECS service as a
                      task set.

                      - **identifer** *(string) --*

                        A unique ID of an ``ECSTaskSet`` .

                      - **desiredCount** *(integer) --*

                        The number of tasks in a task set. During a deployment that uses the Amazon
                        ECS compute type, CodeDeploy instructs Amazon ECS to create a new task set
                        and uses this value to determine how many tasks to create. After the updated
                        task set is created, CodeDeploy shifts traffic to the new task set.

                      - **pendingCount** *(integer) --*

                        The number of tasks in the task set that are in the ``PENDING`` status
                        during an Amazon ECS deployment. A task in the ``PENDING`` state is
                        preparing to enter the ``RUNNING`` state. A task set enters the ``PENDING``
                        status when it launches for the first time, or when it is restarted after
                        being in the ``STOPPED`` state.

                      - **runningCount** *(integer) --*

                        The number of tasks in the task set that are in the ``RUNNING`` status
                        during an Amazon ECS deployment. A task in the ``RUNNING`` state is running
                        and ready for use.

                      - **status** *(string) --*

                        The status of the task set. There are three valid task set statuses:

                        * ``PRIMARY`` : Indicates the task set is serving production traffic.

                        * ``ACTIVE`` : Indicates the task set is not serving production traffic.

                        * ``DRAINING`` : Indicates the tasks in the task set are being stopped and
                        their corresponding targets are being deregistered from their target group.

                      - **trafficWeight** *(float) --*

                        The percentage of traffic served by this task set.

                      - **targetGroup** *(dict) --*

                        The target group associated with the task set. The target group is used by
                        AWS CodeDeploy to manage traffic to a task set.

                        - **name** *(string) --*

                          For blue/green deployments, the name of the target group that instances in
                          the original environment are deregistered from, and instances in the
                          replacement environment are registered with. For in-place deployments, the
                          name of the target group that instances are deregistered from, so they are
                          not serving traffic during a deployment, and then re-registered with after
                          the deployment is complete.

                      - **taskSetLabel** *(string) --*

                        A label that identifies whether the ECS task set is an original target
                        (``BLUE`` ) or a replacement target (``GREEN`` ).
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def batch_get_deployments(
        self, deploymentIds: List[str]
    ) -> ClientBatchGetDeploymentsResponseTypeDef:
        """
        Gets information about one or more deployments. The maximum number of deployments that can
        be returned is 25.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/codedeploy-2014-10-06/BatchGetDeployments>`_

        **Request Syntax**
        ::

          response = client.batch_get_deployments(
              deploymentIds=[
                  'string',
              ]
          )
        :type deploymentIds: list
        :param deploymentIds: **[REQUIRED]**

          A list of deployment IDs, separated by spaces. The maximum number of deployment IDs you
          can specify is 25.

          - *(string) --*

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'deploymentsInfo': [
                    {
                        'applicationName': 'string',
                        'deploymentGroupName': 'string',
                        'deploymentConfigName': 'string',
                        'deploymentId': 'string',
                        'previousRevision': {
                            'revisionType': 'S3'|'GitHub'|'String'|'AppSpecContent',
                            's3Location': {
                                'bucket': 'string',
                                'key': 'string',
                                'bundleType': 'tar'|'tgz'|'zip'|'YAML'|'JSON',
                                'version': 'string',
                                'eTag': 'string'
                            },
                            'gitHubLocation': {
                                'repository': 'string',
                                'commitId': 'string'
                            },
                            'string': {
                                'content': 'string',
                                'sha256': 'string'
                            },
                            'appSpecContent': {
                                'content': 'string',
                                'sha256': 'string'
                            }
                        },
                        'revision': {
                            'revisionType': 'S3'|'GitHub'|'String'|'AppSpecContent',
                            's3Location': {
                                'bucket': 'string',
                                'key': 'string',
                                'bundleType': 'tar'|'tgz'|'zip'|'YAML'|'JSON',
                                'version': 'string',
                                'eTag': 'string'
                            },
                            'gitHubLocation': {
                                'repository': 'string',
                                'commitId': 'string'
                            },
                            'string': {
                                'content': 'string',
                                'sha256': 'string'
                            },
                            'appSpecContent': {
                                'content': 'string',
                                'sha256': 'string'
                            }
                        },
                        'status':
                        'Created'|'Queued'|'InProgress'|'Succeeded'|'Failed'
                        |'Stopped'|'Ready',
                        'errorInformation': {
                            'code':
                            'AGENT_ISSUE'|'ALARM_ACTIVE'|'APPLICATION_MISSING'
                            |'AUTOSCALING_VALIDATION_ERROR'
                            |'AUTO_SCALING_CONFIGURATION'
                            |'AUTO_SCALING_IAM_ROLE_PERMISSIONS'
                            |'CODEDEPLOY_RESOURCE_CANNOT_BE_FOUND'
                            |'CUSTOMER_APPLICATION_UNHEALTHY'
                            |'DEPLOYMENT_GROUP_MISSING'|'ECS_UPDATE_ERROR'
                            |'ELASTIC_LOAD_BALANCING_INVALID'
                            |'ELB_INVALID_INSTANCE'|'HEALTH_CONSTRAINTS'
                            |'HEALTH_CONSTRAINTS_INVALID'
                            |'HOOK_EXECUTION_FAILURE'|'IAM_ROLE_MISSING'
                            |'IAM_ROLE_PERMISSIONS'|'INTERNAL_ERROR'
                            |'INVALID_ECS_SERVICE'
                            |'INVALID_LAMBDA_CONFIGURATION'
                            |'INVALID_LAMBDA_FUNCTION'|'INVALID_REVISION'
                            |'MANUAL_STOP'
                            |'MISSING_BLUE_GREEN_DEPLOYMENT_CONFIGURATION'
                            |'MISSING_ELB_INFORMATION'|'MISSING_GITHUB_TOKEN'
                            |'NO_EC2_SUBSCRIPTION'|'NO_INSTANCES'
                            |'OVER_MAX_INSTANCES'|'RESOURCE_LIMIT_EXCEEDED'
                            |'REVISION_MISSING'|'THROTTLED'|'TIMEOUT',
                            'message': 'string'
                        },
                        'createTime': datetime(2015, 1, 1),
                        'startTime': datetime(2015, 1, 1),
                        'completeTime': datetime(2015, 1, 1),
                        'deploymentOverview': {
                            'Pending': 123,
                            'InProgress': 123,
                            'Succeeded': 123,
                            'Failed': 123,
                            'Skipped': 123,
                            'Ready': 123
                        },
                        'description': 'string',
                        'creator': 'user'|'autoscaling'|'codeDeployRollback',
                        'ignoreApplicationStopFailures': True|False,
                        'autoRollbackConfiguration': {
                            'enabled': True|False,
                            'events': [
                                'DEPLOYMENT_FAILURE'|'DEPLOYMENT_STOP_ON_ALARM'
                                |'DEPLOYMENT_STOP_ON_REQUEST',
                            ]
                        },
                        'updateOutdatedInstancesOnly': True|False,
                        'rollbackInfo': {
                            'rollbackDeploymentId': 'string',
                            'rollbackTriggeringDeploymentId': 'string',
                            'rollbackMessage': 'string'
                        },
                        'deploymentStyle': {
                            'deploymentType': 'IN_PLACE'|'BLUE_GREEN',
                            'deploymentOption': 'WITH_TRAFFIC_CONTROL'|'WITHOUT_TRAFFIC_CONTROL'
                        },
                        'targetInstances': {
                            'tagFilters': [
                                {
                                    'Key': 'string',
                                    'Value': 'string',
                                    'Type': 'KEY_ONLY'|'VALUE_ONLY'|'KEY_AND_VALUE'
                                },
                            ],
                            'autoScalingGroups': [
                                'string',
                            ],
                            'ec2TagSet': {
                                'ec2TagSetList': [
                                    [
                                        {
                                            'Key': 'string',
                                            'Value': 'string',
                                            'Type': 'KEY_ONLY'|'VALUE_ONLY'|'KEY_AND_VALUE'
                                        },
                                    ],
                                ]
                            }
                        },
                        'instanceTerminationWaitTimeStarted': True|False,
                        'blueGreenDeploymentConfiguration': {
                            'terminateBlueInstancesOnDeploymentSuccess': {
                                'action': 'TERMINATE'|'KEEP_ALIVE',
                                'terminationWaitTimeInMinutes': 123
                            },
                            'deploymentReadyOption': {
                                'actionOnTimeout': 'CONTINUE_DEPLOYMENT'|'STOP_DEPLOYMENT',
                                'waitTimeInMinutes': 123
                            },
                            'greenFleetProvisioningOption': {
                                'action': 'DISCOVER_EXISTING'|'COPY_AUTO_SCALING_GROUP'
                            }
                        },
                        'loadBalancerInfo': {
                            'elbInfoList': [
                                {
                                    'name': 'string'
                                },
                            ],
                            'targetGroupInfoList': [
                                {
                                    'name': 'string'
                                },
                            ],
                            'targetGroupPairInfoList': [
                                {
                                    'targetGroups': [
                                        {
                                            'name': 'string'
                                        },
                                    ],
                                    'prodTrafficRoute': {
                                        'listenerArns': [
                                            'string',
                                        ]
                                    },
                                    'testTrafficRoute': {
                                        'listenerArns': [
                                            'string',
                                        ]
                                    }
                                },
                            ]
                        },
                        'additionalDeploymentStatusInfo': 'string',
                        'fileExistsBehavior': 'DISALLOW'|'OVERWRITE'|'RETAIN',
                        'deploymentStatusMessages': [
                            'string',
                        ],
                        'computePlatform': 'Server'|'Lambda'|'ECS'
                    },
                ]
            }
          **Response Structure**

          - *(dict) --*

            Represents the output of a BatchGetDeployments operation.

            - **deploymentsInfo** *(list) --*

              Information about the deployments.

              - *(dict) --*

                Information about a deployment.

                - **applicationName** *(string) --*

                  The application name.

                - **deploymentGroupName** *(string) --*

                  The deployment group name.

                - **deploymentConfigName** *(string) --*

                  The deployment configuration name.

                - **deploymentId** *(string) --*

                  The unique ID of a deployment.

                - **previousRevision** *(dict) --*

                  Information about the application revision that was deployed to the deployment
                  group before the most recent successful deployment.

                  - **revisionType** *(string) --*

                    The type of application revision:

                    * S3: An application revision stored in Amazon S3.

                    * GitHub: An application revision stored in GitHub (EC2/On-premises deployments
                    only).

                    * String: A YAML-formatted or JSON-formatted string (AWS Lambda deployments
                    only).

                  - **s3Location** *(dict) --*

                    Information about the location of a revision stored in Amazon S3.

                    - **bucket** *(string) --*

                      The name of the Amazon S3 bucket where the application revision is stored.

                    - **key** *(string) --*

                      The name of the Amazon S3 object that represents the bundled artifacts for the
                      application revision.

                    - **bundleType** *(string) --*

                      The file type of the application revision. Must be one of the following:

                      * tar: A tar archive file.

                      * tgz: A compressed tar archive file.

                      * zip: A zip archive file.

                    - **version** *(string) --*

                      A specific version of the Amazon S3 object that represents the bundled
                      artifacts for the application revision.

                      If the version is not specified, the system uses the most recent version by
                      default.

                    - **eTag** *(string) --*

                      The ETag of the Amazon S3 object that represents the bundled artifacts for the
                      application revision.

                      If the ETag is not specified as an input parameter, ETag validation of the
                      object is skipped.

                  - **gitHubLocation** *(dict) --*

                    Information about the location of application artifacts stored in GitHub.

                    - **repository** *(string) --*

                      The GitHub account and repository pair that stores a reference to the commit
                      that represents the bundled artifacts for the application revision.

                      Specified as account/repository.

                    - **commitId** *(string) --*

                      The SHA1 commit ID of the GitHub commit that represents the bundled artifacts
                      for the application revision.

                  - **string** *(dict) --*

                    Information about the location of an AWS Lambda deployment revision stored as a
                    RawString.

                    - **content** *(string) --*

                      The YAML-formatted or JSON-formatted revision string. It includes information
                      about which Lambda function to update and optional Lambda functions that
                      validate deployment lifecycle events.

                    - **sha256** *(string) --*

                      The SHA256 hash value of the revision content.

                  - **appSpecContent** *(dict) --*

                    The content of an AppSpec file for an AWS Lambda or Amazon ECS deployment. The
                    content is formatted as JSON or YAML and stored as a RawString.

                    - **content** *(string) --*

                      The YAML-formatted or JSON-formatted revision string.

                      For an AWS Lambda deployment, the content includes a Lambda function name, the
                      alias for its original version, and the alias for its replacement version. The
                      deployment shifts traffic from the original version of the Lambda function to
                      the replacement version.

                      For an Amazon ECS deployment, the content includes the task name, information
                      about the load balancer that serves traffic to the container, and more.

                      For both types of deployments, the content can specify Lambda functions that
                      run at specified hooks, such as ``BeforeInstall`` , during a deployment.

                    - **sha256** *(string) --*

                      The SHA256 hash value of the revision content.

                - **revision** *(dict) --*

                  Information about the location of stored application artifacts and the service
                  from which to retrieve them.

                  - **revisionType** *(string) --*

                    The type of application revision:

                    * S3: An application revision stored in Amazon S3.

                    * GitHub: An application revision stored in GitHub (EC2/On-premises deployments
                    only).

                    * String: A YAML-formatted or JSON-formatted string (AWS Lambda deployments
                    only).

                  - **s3Location** *(dict) --*

                    Information about the location of a revision stored in Amazon S3.

                    - **bucket** *(string) --*

                      The name of the Amazon S3 bucket where the application revision is stored.

                    - **key** *(string) --*

                      The name of the Amazon S3 object that represents the bundled artifacts for the
                      application revision.

                    - **bundleType** *(string) --*

                      The file type of the application revision. Must be one of the following:

                      * tar: A tar archive file.

                      * tgz: A compressed tar archive file.

                      * zip: A zip archive file.

                    - **version** *(string) --*

                      A specific version of the Amazon S3 object that represents the bundled
                      artifacts for the application revision.

                      If the version is not specified, the system uses the most recent version by
                      default.

                    - **eTag** *(string) --*

                      The ETag of the Amazon S3 object that represents the bundled artifacts for the
                      application revision.

                      If the ETag is not specified as an input parameter, ETag validation of the
                      object is skipped.

                  - **gitHubLocation** *(dict) --*

                    Information about the location of application artifacts stored in GitHub.

                    - **repository** *(string) --*

                      The GitHub account and repository pair that stores a reference to the commit
                      that represents the bundled artifacts for the application revision.

                      Specified as account/repository.

                    - **commitId** *(string) --*

                      The SHA1 commit ID of the GitHub commit that represents the bundled artifacts
                      for the application revision.

                  - **string** *(dict) --*

                    Information about the location of an AWS Lambda deployment revision stored as a
                    RawString.

                    - **content** *(string) --*

                      The YAML-formatted or JSON-formatted revision string. It includes information
                      about which Lambda function to update and optional Lambda functions that
                      validate deployment lifecycle events.

                    - **sha256** *(string) --*

                      The SHA256 hash value of the revision content.

                  - **appSpecContent** *(dict) --*

                    The content of an AppSpec file for an AWS Lambda or Amazon ECS deployment. The
                    content is formatted as JSON or YAML and stored as a RawString.

                    - **content** *(string) --*

                      The YAML-formatted or JSON-formatted revision string.

                      For an AWS Lambda deployment, the content includes a Lambda function name, the
                      alias for its original version, and the alias for its replacement version. The
                      deployment shifts traffic from the original version of the Lambda function to
                      the replacement version.

                      For an Amazon ECS deployment, the content includes the task name, information
                      about the load balancer that serves traffic to the container, and more.

                      For both types of deployments, the content can specify Lambda functions that
                      run at specified hooks, such as ``BeforeInstall`` , during a deployment.

                    - **sha256** *(string) --*

                      The SHA256 hash value of the revision content.

                - **status** *(string) --*

                  The current state of the deployment as a whole.

                - **errorInformation** *(dict) --*

                  Information about any error associated with this deployment.

                  - **code** *(string) --*

                    For more information, see `Error Codes for AWS CodeDeploy
                    <https://docs.aws.amazon.com/codedeploy/latest/userguide/error-codes.html>`__ in
                    the `AWS CodeDeploy User Guide
                    <https://docs.aws.amazon.com/codedeploy/latest/userguide>`__ .

                    The error code:

                    * APPLICATION_MISSING: The application was missing. This error code is most
                    likely raised if the application is deleted after the deployment is created, but
                    before it is started.

                    * DEPLOYMENT_GROUP_MISSING: The deployment group was missing. This error code is
                    most likely raised if the deployment group is deleted after the deployment is
                    created, but before it is started.

                    * HEALTH_CONSTRAINTS: The deployment failed on too many instances to be
                    successfully deployed within the instance health constraints specified.

                    * HEALTH_CONSTRAINTS_INVALID: The revision cannot be successfully deployed
                    within the instance health constraints specified.

                    * IAM_ROLE_MISSING: The service role cannot be accessed.

                    * IAM_ROLE_PERMISSIONS: The service role does not have the correct permissions.

                    * INTERNAL_ERROR: There was an internal error.

                    * NO_EC2_SUBSCRIPTION: The calling account is not subscribed to Amazon EC2.

                    * NO_INSTANCES: No instances were specified, or no instances can be found.

                    * OVER_MAX_INSTANCES: The maximum number of instances was exceeded.

                    * THROTTLED: The operation was throttled because the calling account exceeded
                    the throttling limits of one or more AWS services.

                    * TIMEOUT: The deployment has timed out.

                    * REVISION_MISSING: The revision ID was missing. This error code is most likely
                    raised if the revision is deleted after the deployment is created, but before it
                    is started.

                  - **message** *(string) --*

                    An accompanying error message.

                - **createTime** *(datetime) --*

                  A timestamp that indicates when the deployment was created.

                - **startTime** *(datetime) --*

                  A timestamp that indicates when the deployment was deployed to the deployment
                  group.

                  In some cases, the reported value of the start time might be later than the
                  complete time. This is due to differences in the clock settings of backend servers
                  that participate in the deployment process.

                - **completeTime** *(datetime) --*

                  A timestamp that indicates when the deployment was complete.

                - **deploymentOverview** *(dict) --*

                  A summary of the deployment status of the instances in the deployment.

                  - **Pending** *(integer) --*

                    The number of instances in the deployment in a pending state.

                  - **InProgress** *(integer) --*

                    The number of instances in which the deployment is in progress.

                  - **Succeeded** *(integer) --*

                    The number of instances in the deployment to which revisions have been
                    successfully deployed.

                  - **Failed** *(integer) --*

                    The number of instances in the deployment in a failed state.

                  - **Skipped** *(integer) --*

                    The number of instances in the deployment in a skipped state.

                  - **Ready** *(integer) --*

                    The number of instances in a replacement environment ready to receive traffic in
                    a blue/green deployment.

                - **description** *(string) --*

                  A comment about the deployment.

                - **creator** *(string) --*

                  The means by which the deployment was created:

                  * user: A user created the deployment.

                  * autoscaling: Amazon EC2 Auto Scaling created the deployment.

                  * codeDeployRollback: A rollback process created the deployment.

                - **ignoreApplicationStopFailures** *(boolean) --*

                  If true, then if an ``ApplicationStop`` , ``BeforeBlockTraffic`` , or
                  ``AfterBlockTraffic`` deployment lifecycle event to an instance fails, then the
                  deployment continues to the next deployment lifecycle event. For example, if
                  ``ApplicationStop`` fails, the deployment continues with DownloadBundle. If
                  ``BeforeBlockTraffic`` fails, the deployment continues with ``BlockTraffic`` . If
                  ``AfterBlockTraffic`` fails, the deployment continues with ``ApplicationStop`` .

                  If false or not specified, then if a lifecycle event fails during a deployment to
                  an instance, that deployment fails. If deployment to that instance is part of an
                  overall deployment and the number of healthy hosts is not less than the minimum
                  number of healthy hosts, then a deployment to the next instance is attempted.

                  During a deployment, the AWS CodeDeploy agent runs the scripts specified for
                  ``ApplicationStop`` , ``BeforeBlockTraffic`` , and ``AfterBlockTraffic`` in the
                  AppSpec file from the previous successful deployment. (All other scripts are run
                  from the AppSpec file in the current deployment.) If one of these scripts contains
                  an error and does not run successfully, the deployment can fail.

                  If the cause of the failure is a script from the last successful deployment that
                  will never run successfully, create a new deployment and use
                  ``ignoreApplicationStopFailures`` to specify that the ``ApplicationStop`` ,
                  ``BeforeBlockTraffic`` , and ``AfterBlockTraffic`` failures should be ignored.

                - **autoRollbackConfiguration** *(dict) --*

                  Information about the automatic rollback configuration associated with the
                  deployment.

                  - **enabled** *(boolean) --*

                    Indicates whether a defined automatic rollback configuration is currently
                    enabled.

                  - **events** *(list) --*

                    The event type or types that trigger a rollback.

                    - *(string) --*

                - **updateOutdatedInstancesOnly** *(boolean) --*

                  Indicates whether only instances that are not running the latest application
                  revision are to be deployed to.

                - **rollbackInfo** *(dict) --*

                  Information about a deployment rollback.

                  - **rollbackDeploymentId** *(string) --*

                    The ID of the deployment rollback.

                  - **rollbackTriggeringDeploymentId** *(string) --*

                    The deployment ID of the deployment that was underway and triggered a rollback
                    deployment because it failed or was stopped.

                  - **rollbackMessage** *(string) --*

                    Information that describes the status of a deployment rollback (for example,
                    whether the deployment can't be rolled back, is in progress, failed, or
                    succeeded).

                - **deploymentStyle** *(dict) --*

                  Information about the type of deployment, either in-place or blue/green, you want
                  to run and whether to route deployment traffic behind a load balancer.

                  - **deploymentType** *(string) --*

                    Indicates whether to run an in-place deployment or a blue/green deployment.

                  - **deploymentOption** *(string) --*

                    Indicates whether to route deployment traffic behind a load balancer.

                - **targetInstances** *(dict) --*

                  Information about the instances that belong to the replacement environment in a
                  blue/green deployment.

                  - **tagFilters** *(list) --*

                    The tag filter key, type, and value used to identify Amazon EC2 instances in a
                    replacement environment for a blue/green deployment. Cannot be used in the same
                    call as ec2TagSet.

                    - *(dict) --*

                      Information about an EC2 tag filter.

                      - **Key** *(string) --*

                        The tag filter key.

                      - **Value** *(string) --*

                        The tag filter value.

                      - **Type** *(string) --*

                        The tag filter type:

                        * KEY_ONLY: Key only.

                        * VALUE_ONLY: Value only.

                        * KEY_AND_VALUE: Key and value.

                  - **autoScalingGroups** *(list) --*

                    The names of one or more Auto Scaling groups to identify a replacement
                    environment for a blue/green deployment.

                    - *(string) --*

                  - **ec2TagSet** *(dict) --*

                    Information about the groups of EC2 instance tags that an instance must be
                    identified by in order for it to be included in the replacement environment for
                    a blue/green deployment. Cannot be used in the same call as tagFilters.

                    - **ec2TagSetList** *(list) --*

                      A list that contains other lists of EC2 instance tag groups. For an instance
                      to be included in the deployment group, it must be identified by all of the
                      tag groups in the list.

                      - *(list) --*

                        - *(dict) --*

                          Information about an EC2 tag filter.

                          - **Key** *(string) --*

                            The tag filter key.

                          - **Value** *(string) --*

                            The tag filter value.

                          - **Type** *(string) --*

                            The tag filter type:

                            * KEY_ONLY: Key only.

                            * VALUE_ONLY: Value only.

                            * KEY_AND_VALUE: Key and value.

                - **instanceTerminationWaitTimeStarted** *(boolean) --*

                  Indicates whether the wait period set for the termination of instances in the
                  original environment has started. Status is 'false' if the KEEP_ALIVE option is
                  specified. Otherwise, 'true' as soon as the termination wait period starts.

                - **blueGreenDeploymentConfiguration** *(dict) --*

                  Information about blue/green deployment options for this deployment.

                  - **terminateBlueInstancesOnDeploymentSuccess** *(dict) --*

                    Information about whether to terminate instances in the original fleet during a
                    blue/green deployment.

                    - **action** *(string) --*

                      The action to take on instances in the original environment after a successful
                      blue/green deployment.

                      * TERMINATE: Instances are terminated after a specified wait time.

                      * KEEP_ALIVE: Instances are left running after they are deregistered from the
                      load balancer and removed from the deployment group.

                    - **terminationWaitTimeInMinutes** *(integer) --*

                      For an Amazon EC2 deployment, the number of minutes to wait after a successful
                      blue/green deployment before terminating instances from the original
                      environment.

                      For an Amazon ECS deployment, the number of minutes before deleting the
                      original (blue) task set. During an Amazon ECS deployment, CodeDeploy shifts
                      traffic from the original (blue) task set to a replacement (green) task set.

                      The maximum setting is 2880 minutes (2 days).

                  - **deploymentReadyOption** *(dict) --*

                    Information about the action to take when newly provisioned instances are ready
                    to receive traffic in a blue/green deployment.

                    - **actionOnTimeout** *(string) --*

                      Information about when to reroute traffic from an original environment to a
                      replacement environment in a blue/green deployment.

                      * CONTINUE_DEPLOYMENT: Register new instances with the load balancer
                      immediately after the new application revision is installed on the instances
                      in the replacement environment.

                      * STOP_DEPLOYMENT: Do not register new instances with a load balancer unless
                      traffic rerouting is started using  ContinueDeployment . If traffic rerouting
                      is not started before the end of the specified wait period, the deployment
                      status is changed to Stopped.

                    - **waitTimeInMinutes** *(integer) --*

                      The number of minutes to wait before the status of a blue/green deployment is
                      changed to Stopped if rerouting is not started manually. Applies only to the
                      STOP_DEPLOYMENT option for actionOnTimeout

                  - **greenFleetProvisioningOption** *(dict) --*

                    Information about how instances are provisioned for a replacement environment in
                    a blue/green deployment.

                    - **action** *(string) --*

                      The method used to add instances to a replacement environment.

                      * DISCOVER_EXISTING: Use instances that already exist or will be created
                      manually.

                      * COPY_AUTO_SCALING_GROUP: Use settings from a specified Auto Scaling group to
                      define and create instances in a new Auto Scaling group.

                - **loadBalancerInfo** *(dict) --*

                  Information about the load balancer used in the deployment.

                  - **elbInfoList** *(list) --*

                    An array that contains information about the load balancer to use for load
                    balancing in a deployment. In Elastic Load Balancing, load balancers are used
                    with Classic Load Balancers.

                    .. note::

                      Adding more than one load balancer to the array is not supported.

                    - *(dict) --*

                      Information about a load balancer in Elastic Load Balancing to use in a
                      deployment. Instances are registered directly with a load balancer, and
                      traffic is routed to the load balancer.

                      - **name** *(string) --*

                        For blue/green deployments, the name of the load balancer that is used to
                        route traffic from original instances to replacement instances in a
                        blue/green deployment. For in-place deployments, the name of the load
                        balancer that instances are deregistered from so they are not serving
                        traffic during a deployment, and then re-registered with after the
                        deployment is complete.

                  - **targetGroupInfoList** *(list) --*

                    An array that contains information about the target group to use for load
                    balancing in a deployment. In Elastic Load Balancing, target groups are used
                    with Application Load Balancers.

                    .. note::

                      Adding more than one target group to the array is not supported.

                    - *(dict) --*

                      Information about a target group in Elastic Load Balancing to use in a
                      deployment. Instances are registered as targets in a target group, and traffic
                      is routed to the target group.

                      - **name** *(string) --*

                        For blue/green deployments, the name of the target group that instances in
                        the original environment are deregistered from, and instances in the
                        replacement environment are registered with. For in-place deployments, the
                        name of the target group that instances are deregistered from, so they are
                        not serving traffic during a deployment, and then re-registered with after
                        the deployment is complete.

                  - **targetGroupPairInfoList** *(list) --*

                    The target group pair information. This is an array of ``TargeGroupPairInfo``
                    objects with a maximum size of one.

                    - *(dict) --*

                      Information about two target groups and how traffic is routed during an Amazon
                      ECS deployment. An optional test traffic route can be specified.

                      - **targetGroups** *(list) --*

                        One pair of target groups. One is associated with the original task set. The
                        second is associated with the task set that serves traffic after the
                        deployment is complete.

                        - *(dict) --*

                          Information about a target group in Elastic Load Balancing to use in a
                          deployment. Instances are registered as targets in a target group, and
                          traffic is routed to the target group.

                          - **name** *(string) --*

                            For blue/green deployments, the name of the target group that instances
                            in the original environment are deregistered from, and instances in the
                            replacement environment are registered with. For in-place deployments,
                            the name of the target group that instances are deregistered from, so
                            they are not serving traffic during a deployment, and then re-registered
                            with after the deployment is complete.

                      - **prodTrafficRoute** *(dict) --*

                        The path used by a load balancer to route production traffic when an Amazon
                        ECS deployment is complete.

                        - **listenerArns** *(list) --*

                          The ARN of one listener. The listener identifies the route between a
                          target group and a load balancer. This is an array of strings with a
                          maximum size of one.

                          - *(string) --*

                      - **testTrafficRoute** *(dict) --*

                        An optional path used by a load balancer to route test traffic after an
                        Amazon ECS deployment. Validation can occur while test traffic is served
                        during a deployment.

                        - **listenerArns** *(list) --*

                          The ARN of one listener. The listener identifies the route between a
                          target group and a load balancer. This is an array of strings with a
                          maximum size of one.

                          - *(string) --*

                - **additionalDeploymentStatusInfo** *(string) --*

                  Provides information about the results of a deployment, such as whether instances
                  in the original environment in a blue/green deployment were not terminated.

                - **fileExistsBehavior** *(string) --*

                  Information about how AWS CodeDeploy handles files that already exist in a
                  deployment target location but weren't part of the previous successful deployment.

                  * DISALLOW: The deployment fails. This is also the default behavior if no option
                  is specified.

                  * OVERWRITE: The version of the file from the application revision currently being
                  deployed replaces the version already on the instance.

                  * RETAIN: The version of the file already on the instance is kept and used as part
                  of the new deployment.

                - **deploymentStatusMessages** *(list) --*

                  Messages that contain information about the status of a deployment.

                  - *(string) --*

                - **computePlatform** *(string) --*

                  The destination platform type for the deployment (``Lambda`` , ``Server`` , or
                  ``ECS`` ).
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def batch_get_on_premises_instances(
        self, instanceNames: List[str]
    ) -> ClientBatchGetOnPremisesInstancesResponseTypeDef:
        """
        Gets information about one or more on-premises instances. The maximum number of on-premises
        instances that can be returned is 25.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/codedeploy-2014-10-06/BatchGetOnPremisesInstances>`_

        **Request Syntax**
        ::

          response = client.batch_get_on_premises_instances(
              instanceNames=[
                  'string',
              ]
          )
        :type instanceNames: list
        :param instanceNames: **[REQUIRED]**

          The names of the on-premises instances about which to get information. The maximum number
          of instance names you can specify is 25.

          - *(string) --*

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'instanceInfos': [
                    {
                        'instanceName': 'string',
                        'iamSessionArn': 'string',
                        'iamUserArn': 'string',
                        'instanceArn': 'string',
                        'registerTime': datetime(2015, 1, 1),
                        'deregisterTime': datetime(2015, 1, 1),
                        'tags': [
                            {
                                'Key': 'string',
                                'Value': 'string'
                            },
                        ]
                    },
                ]
            }
          **Response Structure**

          - *(dict) --*

            Represents the output of a BatchGetOnPremisesInstances operation.

            - **instanceInfos** *(list) --*

              Information about the on-premises instances.

              - *(dict) --*

                Information about an on-premises instance.

                - **instanceName** *(string) --*

                  The name of the on-premises instance.

                - **iamSessionArn** *(string) --*

                  The ARN of the IAM session associated with the on-premises instance.

                - **iamUserArn** *(string) --*

                  The IAM user ARN associated with the on-premises instance.

                - **instanceArn** *(string) --*

                  The ARN of the on-premises instance.

                - **registerTime** *(datetime) --*

                  The time at which the on-premises instance was registered.

                - **deregisterTime** *(datetime) --*

                  If the on-premises instance was deregistered, the time at which the on-premises
                  instance was deregistered.

                - **tags** *(list) --*

                  The tags currently associated with the on-premises instance.

                  - *(dict) --*

                    Information about a tag.

                    - **Key** *(string) --*

                      The tag's key.

                    - **Value** *(string) --*

                      The tag's value.
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
    def continue_deployment(
        self,
        deploymentId: str = None,
        deploymentWaitType: Literal["READY_WAIT", "TERMINATION_WAIT"] = None,
    ) -> None:
        """
        For a blue/green deployment, starts the process of rerouting traffic from instances in the
        original environment to instances in the replacement environment without waiting for a
        specified wait time to elapse. (Traffic rerouting, which is achieved by registering
        instances in the replacement environment with the load balancer, can start as soon as all
        instances have a status of Ready.)

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/codedeploy-2014-10-06/ContinueDeployment>`_

        **Request Syntax**
        ::

          response = client.continue_deployment(
              deploymentId='string',
              deploymentWaitType='READY_WAIT'|'TERMINATION_WAIT'
          )
        :type deploymentId: string
        :param deploymentId:

          The unique ID of a blue/green deployment for which you want to start rerouting traffic to
          the replacement environment.

        :type deploymentWaitType: string
        :param deploymentWaitType:

          The status of the deployment's waiting period. READY_WAIT indicates the deployment is
          ready to start shifting traffic. TERMINATION_WAIT indicates the traffic is shifted, but
          the original target is not terminated.

        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_application(
        self,
        applicationName: str,
        computePlatform: Literal["Server", "Lambda", "ECS"] = None,
        tags: List[ClientCreateApplicationTagsTypeDef] = None,
    ) -> ClientCreateApplicationResponseTypeDef:
        """
        Creates an application.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/codedeploy-2014-10-06/CreateApplication>`_

        **Request Syntax**
        ::

          response = client.create_application(
              applicationName='string',
              computePlatform='Server'|'Lambda'|'ECS',
              tags=[
                  {
                      'Key': 'string',
                      'Value': 'string'
                  },
              ]
          )
        :type applicationName: string
        :param applicationName: **[REQUIRED]**

          The name of the application. This name must be unique with the applicable IAM user or AWS
          account.

        :type computePlatform: string
        :param computePlatform:

          The destination platform type for the deployment (``Lambda`` , ``Server`` , or ``ECS`` ).

        :type tags: list
        :param tags:

          The metadata that you apply to CodeDeploy applications to help you organize and categorize
          them. Each tag consists of a key and an optional value, both of which you define.

          - *(dict) --*

            Information about a tag.

            - **Key** *(string) --*

              The tag's key.

            - **Value** *(string) --*

              The tag's value.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'applicationId': 'string'
            }
          **Response Structure**

          - *(dict) --*

            Represents the output of a CreateApplication operation.

            - **applicationId** *(string) --*

              A unique application ID.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_deployment(
        self,
        applicationName: str,
        deploymentGroupName: str = None,
        revision: ClientCreateDeploymentRevisionTypeDef = None,
        deploymentConfigName: str = None,
        description: str = None,
        ignoreApplicationStopFailures: bool = None,
        targetInstances: ClientCreateDeploymentTargetInstancesTypeDef = None,
        autoRollbackConfiguration: ClientCreateDeploymentAutoRollbackConfigurationTypeDef = None,
        updateOutdatedInstancesOnly: bool = None,
        fileExistsBehavior: Literal["DISALLOW", "OVERWRITE", "RETAIN"] = None,
    ) -> ClientCreateDeploymentResponseTypeDef:
        """
        Deploys an application revision through the specified deployment group.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/codedeploy-2014-10-06/CreateDeployment>`_

        **Request Syntax**
        ::

          response = client.create_deployment(
              applicationName='string',
              deploymentGroupName='string',
              revision={
                  'revisionType': 'S3'|'GitHub'|'String'|'AppSpecContent',
                  's3Location': {
                      'bucket': 'string',
                      'key': 'string',
                      'bundleType': 'tar'|'tgz'|'zip'|'YAML'|'JSON',
                      'version': 'string',
                      'eTag': 'string'
                  },
                  'gitHubLocation': {
                      'repository': 'string',
                      'commitId': 'string'
                  },
                  'string': {
                      'content': 'string',
                      'sha256': 'string'
                  },
                  'appSpecContent': {
                      'content': 'string',
                      'sha256': 'string'
                  }
              },
              deploymentConfigName='string',
              description='string',
              ignoreApplicationStopFailures=True|False,
              targetInstances={
                  'tagFilters': [
                      {
                          'Key': 'string',
                          'Value': 'string',
                          'Type': 'KEY_ONLY'|'VALUE_ONLY'|'KEY_AND_VALUE'
                      },
                  ],
                  'autoScalingGroups': [
                      'string',
                  ],
                  'ec2TagSet': {
                      'ec2TagSetList': [
                          [
                              {
                                  'Key': 'string',
                                  'Value': 'string',
                                  'Type': 'KEY_ONLY'|'VALUE_ONLY'|'KEY_AND_VALUE'
                              },
                          ],
                      ]
                  }
              },
              autoRollbackConfiguration={
                  'enabled': True|False,
                  'events': [
                      'DEPLOYMENT_FAILURE'|'DEPLOYMENT_STOP_ON_ALARM'|'DEPLOYMENT_STOP_ON_REQUEST',
                  ]
              },
              updateOutdatedInstancesOnly=True|False,
              fileExistsBehavior='DISALLOW'|'OVERWRITE'|'RETAIN'
          )
        :type applicationName: string
        :param applicationName: **[REQUIRED]**

          The name of an AWS CodeDeploy application associated with the IAM user or AWS account.

        :type deploymentGroupName: string
        :param deploymentGroupName:

          The name of the deployment group.

        :type revision: dict
        :param revision:

          The type and location of the revision to deploy.

          - **revisionType** *(string) --*

            The type of application revision:

            * S3: An application revision stored in Amazon S3.

            * GitHub: An application revision stored in GitHub (EC2/On-premises deployments only).

            * String: A YAML-formatted or JSON-formatted string (AWS Lambda deployments only).

          - **s3Location** *(dict) --*

            Information about the location of a revision stored in Amazon S3.

            - **bucket** *(string) --*

              The name of the Amazon S3 bucket where the application revision is stored.

            - **key** *(string) --*

              The name of the Amazon S3 object that represents the bundled artifacts for the
              application revision.

            - **bundleType** *(string) --*

              The file type of the application revision. Must be one of the following:

              * tar: A tar archive file.

              * tgz: A compressed tar archive file.

              * zip: A zip archive file.

            - **version** *(string) --*

              A specific version of the Amazon S3 object that represents the bundled artifacts for
              the application revision.

              If the version is not specified, the system uses the most recent version by default.

            - **eTag** *(string) --*

              The ETag of the Amazon S3 object that represents the bundled artifacts for the
              application revision.

              If the ETag is not specified as an input parameter, ETag validation of the object is
              skipped.

          - **gitHubLocation** *(dict) --*

            Information about the location of application artifacts stored in GitHub.

            - **repository** *(string) --*

              The GitHub account and repository pair that stores a reference to the commit that
              represents the bundled artifacts for the application revision.

              Specified as account/repository.

            - **commitId** *(string) --*

              The SHA1 commit ID of the GitHub commit that represents the bundled artifacts for the
              application revision.

          - **string** *(dict) --*

            Information about the location of an AWS Lambda deployment revision stored as a
            RawString.

            - **content** *(string) --*

              The YAML-formatted or JSON-formatted revision string. It includes information about
              which Lambda function to update and optional Lambda functions that validate deployment
              lifecycle events.

            - **sha256** *(string) --*

              The SHA256 hash value of the revision content.

          - **appSpecContent** *(dict) --*

            The content of an AppSpec file for an AWS Lambda or Amazon ECS deployment. The content
            is formatted as JSON or YAML and stored as a RawString.

            - **content** *(string) --*

              The YAML-formatted or JSON-formatted revision string.

              For an AWS Lambda deployment, the content includes a Lambda function name, the alias
              for its original version, and the alias for its replacement version. The deployment
              shifts traffic from the original version of the Lambda function to the replacement
              version.

              For an Amazon ECS deployment, the content includes the task name, information about
              the load balancer that serves traffic to the container, and more.

              For both types of deployments, the content can specify Lambda functions that run at
              specified hooks, such as ``BeforeInstall`` , during a deployment.

            - **sha256** *(string) --*

              The SHA256 hash value of the revision content.

        :type deploymentConfigName: string
        :param deploymentConfigName:

          The name of a deployment configuration associated with the IAM user or AWS account.

          If not specified, the value configured in the deployment group is used as the default. If
          the deployment group does not have a deployment configuration associated with it,
          CodeDeployDefault.OneAtATime is used by default.

        :type description: string
        :param description:

          A comment about the deployment.

        :type ignoreApplicationStopFailures: boolean
        :param ignoreApplicationStopFailures:

          If true, then if an ApplicationStop, BeforeBlockTraffic, or AfterBlockTraffic deployment
          lifecycle event to an instance fails, then the deployment continues to the next deployment
          lifecycle event. For example, if ApplicationStop fails, the deployment continues with
          DownloadBundle. If BeforeBlockTraffic fails, the deployment continues with BlockTraffic.
          If AfterBlockTraffic fails, the deployment continues with ApplicationStop.

          If false or not specified, then if a lifecycle event fails during a deployment to an
          instance, that deployment fails. If deployment to that instance is part of an overall
          deployment and the number of healthy hosts is not less than the minimum number of healthy
          hosts, then a deployment to the next instance is attempted.

          During a deployment, the AWS CodeDeploy agent runs the scripts specified for
          ApplicationStop, BeforeBlockTraffic, and AfterBlockTraffic in the AppSpec file from the
          previous successful deployment. (All other scripts are run from the AppSpec file in the
          current deployment.) If one of these scripts contains an error and does not run
          successfully, the deployment can fail.

          If the cause of the failure is a script from the last successful deployment that will
          never run successfully, create a new deployment and use ``ignoreApplicationStopFailures``
          to specify that the ApplicationStop, BeforeBlockTraffic, and AfterBlockTraffic failures
          should be ignored.

        :type targetInstances: dict
        :param targetInstances:

          Information about the instances that belong to the replacement environment in a blue/green
          deployment.

          - **tagFilters** *(list) --*

            The tag filter key, type, and value used to identify Amazon EC2 instances in a
            replacement environment for a blue/green deployment. Cannot be used in the same call as
            ec2TagSet.

            - *(dict) --*

              Information about an EC2 tag filter.

              - **Key** *(string) --*

                The tag filter key.

              - **Value** *(string) --*

                The tag filter value.

              - **Type** *(string) --*

                The tag filter type:

                * KEY_ONLY: Key only.

                * VALUE_ONLY: Value only.

                * KEY_AND_VALUE: Key and value.

          - **autoScalingGroups** *(list) --*

            The names of one or more Auto Scaling groups to identify a replacement environment for a
            blue/green deployment.

            - *(string) --*

          - **ec2TagSet** *(dict) --*

            Information about the groups of EC2 instance tags that an instance must be identified by
            in order for it to be included in the replacement environment for a blue/green
            deployment. Cannot be used in the same call as tagFilters.

            - **ec2TagSetList** *(list) --*

              A list that contains other lists of EC2 instance tag groups. For an instance to be
              included in the deployment group, it must be identified by all of the tag groups in
              the list.

              - *(list) --*

                - *(dict) --*

                  Information about an EC2 tag filter.

                  - **Key** *(string) --*

                    The tag filter key.

                  - **Value** *(string) --*

                    The tag filter value.

                  - **Type** *(string) --*

                    The tag filter type:

                    * KEY_ONLY: Key only.

                    * VALUE_ONLY: Value only.

                    * KEY_AND_VALUE: Key and value.

        :type autoRollbackConfiguration: dict
        :param autoRollbackConfiguration:

          Configuration information for an automatic rollback that is added when a deployment is
          created.

          - **enabled** *(boolean) --*

            Indicates whether a defined automatic rollback configuration is currently enabled.

          - **events** *(list) --*

            The event type or types that trigger a rollback.

            - *(string) --*

        :type updateOutdatedInstancesOnly: boolean
        :param updateOutdatedInstancesOnly:

          Indicates whether to deploy to all instances or only to instances that are not running the
          latest application revision.

        :type fileExistsBehavior: string
        :param fileExistsBehavior:

          Information about how AWS CodeDeploy handles files that already exist in a deployment
          target location but weren't part of the previous successful deployment.

          The fileExistsBehavior parameter takes any of the following values:

          * DISALLOW: The deployment fails. This is also the default behavior if no option is
          specified.

          * OVERWRITE: The version of the file from the application revision currently being
          deployed replaces the version already on the instance.

          * RETAIN: The version of the file already on the instance is kept and used as part of the
          new deployment.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'deploymentId': 'string'
            }
          **Response Structure**

          - *(dict) --*

            Represents the output of a CreateDeployment operation.

            - **deploymentId** *(string) --*

              The unique ID of a deployment.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_deployment_config(
        self,
        deploymentConfigName: str,
        minimumHealthyHosts: ClientCreateDeploymentConfigMinimumHealthyHostsTypeDef = None,
        trafficRoutingConfig: ClientCreateDeploymentConfigTrafficRoutingConfigTypeDef = None,
        computePlatform: Literal["Server", "Lambda", "ECS"] = None,
    ) -> ClientCreateDeploymentConfigResponseTypeDef:
        """
        Creates a deployment configuration.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/codedeploy-2014-10-06/CreateDeploymentConfig>`_

        **Request Syntax**
        ::

          response = client.create_deployment_config(
              deploymentConfigName='string',
              minimumHealthyHosts={
                  'value': 123,
                  'type': 'HOST_COUNT'|'FLEET_PERCENT'
              },
              trafficRoutingConfig={
                  'type': 'TimeBasedCanary'|'TimeBasedLinear'|'AllAtOnce',
                  'timeBasedCanary': {
                      'canaryPercentage': 123,
                      'canaryInterval': 123
                  },
                  'timeBasedLinear': {
                      'linearPercentage': 123,
                      'linearInterval': 123
                  }
              },
              computePlatform='Server'|'Lambda'|'ECS'
          )
        :type deploymentConfigName: string
        :param deploymentConfigName: **[REQUIRED]**

          The name of the deployment configuration to create.

        :type minimumHealthyHosts: dict
        :param minimumHealthyHosts:

          The minimum number of healthy instances that should be available at any time during the
          deployment. There are two parameters expected in the input: type and value.

          The type parameter takes either of the following values:

          * HOST_COUNT: The value parameter represents the minimum number of healthy instances as an
          absolute value.

          * FLEET_PERCENT: The value parameter represents the minimum number of healthy instances as
          a percentage of the total number of instances in the deployment. If you specify
          FLEET_PERCENT, at the start of the deployment, AWS CodeDeploy converts the percentage to
          the equivalent number of instance and rounds up fractional instances.

          The value parameter takes an integer.

          For example, to set a minimum of 95% healthy instance, specify a type of FLEET_PERCENT and
          a value of 95.

          - **value** *(integer) --*

            The minimum healthy instance value.

          - **type** *(string) --*

            The minimum healthy instance type:

            * HOST_COUNT: The minimum number of healthy instance as an absolute value.

            * FLEET_PERCENT: The minimum number of healthy instance as a percentage of the total
            number of instance in the deployment.

            In an example of nine instance, if a HOST_COUNT of six is specified, deploy to up to
            three instances at a time. The deployment is successful if six or more instances are
            deployed to successfully. Otherwise, the deployment fails. If a FLEET_PERCENT of 40 is
            specified, deploy to up to five instance at a time. The deployment is successful if four
            or more instance are deployed to successfully. Otherwise, the deployment fails.

            .. note::

              In a call to the ``GetDeploymentConfig`` , CodeDeployDefault.OneAtATime returns a
              minimum healthy instance type of MOST_CONCURRENCY and a value of 1. This means a
              deployment to only one instance at a time. (You cannot set the type to
              MOST_CONCURRENCY, only to HOST_COUNT or FLEET_PERCENT.) In addition, with
              CodeDeployDefault.OneAtATime, AWS CodeDeploy attempts to ensure that all instances but
              one are kept in a healthy state during the deployment. Although this allows one
              instance at a time to be taken offline for a new deployment, it also means that if the
              deployment to the last instance fails, the overall deployment is still successful.

            For more information, see `AWS CodeDeploy Instance Health
            <https://docs.aws.amazon.com/codedeploy/latest/userguide/instances-health.html>`__ in
            the *AWS CodeDeploy User Guide* .

        :type trafficRoutingConfig: dict
        :param trafficRoutingConfig:

          The configuration that specifies how the deployment traffic is routed.

          - **type** *(string) --*

            The type of traffic shifting (``TimeBasedCanary`` or ``TimeBasedLinear`` ) used by a
            deployment configuration .

          - **timeBasedCanary** *(dict) --*

            A configuration that shifts traffic from one version of a Lambda function to another in
            two increments. The original and target Lambda function versions are specified in the
            deployment's AppSpec file.

            - **canaryPercentage** *(integer) --*

              The percentage of traffic to shift in the first increment of a ``TimeBasedCanary``
              deployment.

            - **canaryInterval** *(integer) --*

              The number of minutes between the first and second traffic shifts of a
              ``TimeBasedCanary`` deployment.

          - **timeBasedLinear** *(dict) --*

            A configuration that shifts traffic from one version of a Lambda function to another in
            equal increments, with an equal number of minutes between each increment. The original
            and target Lambda function versions are specified in the deployment's AppSpec file.

            - **linearPercentage** *(integer) --*

              The percentage of traffic that is shifted at the start of each increment of a
              ``TimeBasedLinear`` deployment.

            - **linearInterval** *(integer) --*

              The number of minutes between each incremental traffic shift of a ``TimeBasedLinear``
              deployment.

        :type computePlatform: string
        :param computePlatform:

          The destination platform type for the deployment (``Lambda`` , ``Server`` , or ``ECS`` ).

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'deploymentConfigId': 'string'
            }
          **Response Structure**

          - *(dict) --*

            Represents the output of a CreateDeploymentConfig operation.

            - **deploymentConfigId** *(string) --*

              A unique deployment configuration ID.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_deployment_group(
        self,
        applicationName: str,
        deploymentGroupName: str,
        serviceRoleArn: str,
        deploymentConfigName: str = None,
        ec2TagFilters: List[ClientCreateDeploymentGroupEc2TagFiltersTypeDef] = None,
        onPremisesInstanceTagFilters: List[
            ClientCreateDeploymentGroupOnPremisesInstanceTagFiltersTypeDef
        ] = None,
        autoScalingGroups: List[str] = None,
        triggerConfigurations: List[ClientCreateDeploymentGroupTriggerConfigurationsTypeDef] = None,
        alarmConfiguration: ClientCreateDeploymentGroupAlarmConfigurationTypeDef = None,
        autoRollbackConfiguration: ClientCreateDeploymentGroupAutoRollbackConfigurationTypeDef = None,
        deploymentStyle: ClientCreateDeploymentGroupDeploymentStyleTypeDef = None,
        blueGreenDeploymentConfiguration: ClientCreateDeploymentGroupBlueGreenDeploymentConfigurationTypeDef = None,
        loadBalancerInfo: ClientCreateDeploymentGroupLoadBalancerInfoTypeDef = None,
        ec2TagSet: ClientCreateDeploymentGroupEc2TagSetTypeDef = None,
        ecsServices: List[ClientCreateDeploymentGroupEcsServicesTypeDef] = None,
        onPremisesTagSet: ClientCreateDeploymentGroupOnPremisesTagSetTypeDef = None,
        tags: List[ClientCreateDeploymentGroupTagsTypeDef] = None,
    ) -> ClientCreateDeploymentGroupResponseTypeDef:
        """
        Creates a deployment group to which application revisions are deployed.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/codedeploy-2014-10-06/CreateDeploymentGroup>`_

        **Request Syntax**
        ::

          response = client.create_deployment_group(
              applicationName='string',
              deploymentGroupName='string',
              deploymentConfigName='string',
              ec2TagFilters=[
                  {
                      'Key': 'string',
                      'Value': 'string',
                      'Type': 'KEY_ONLY'|'VALUE_ONLY'|'KEY_AND_VALUE'
                  },
              ],
              onPremisesInstanceTagFilters=[
                  {
                      'Key': 'string',
                      'Value': 'string',
                      'Type': 'KEY_ONLY'|'VALUE_ONLY'|'KEY_AND_VALUE'
                  },
              ],
              autoScalingGroups=[
                  'string',
              ],
              serviceRoleArn='string',
              triggerConfigurations=[
                  {
                      'triggerName': 'string',
                      'triggerTargetArn': 'string',
                      'triggerEvents': [
                          'DeploymentStart'|'DeploymentSuccess'|'DeploymentFailure'|'DeploymentStop'
                          |'DeploymentRollback'|'DeploymentReady'|'InstanceStart'|'InstanceSuccess'
                          |'InstanceFailure'|'InstanceReady',
                      ]
                  },
              ],
              alarmConfiguration={
                  'enabled': True|False,
                  'ignorePollAlarmFailure': True|False,
                  'alarms': [
                      {
                          'name': 'string'
                      },
                  ]
              },
              autoRollbackConfiguration={
                  'enabled': True|False,
                  'events': [
                      'DEPLOYMENT_FAILURE'|'DEPLOYMENT_STOP_ON_ALARM'|'DEPLOYMENT_STOP_ON_REQUEST',
                  ]
              },
              deploymentStyle={
                  'deploymentType': 'IN_PLACE'|'BLUE_GREEN',
                  'deploymentOption': 'WITH_TRAFFIC_CONTROL'|'WITHOUT_TRAFFIC_CONTROL'
              },
              blueGreenDeploymentConfiguration={
                  'terminateBlueInstancesOnDeploymentSuccess': {
                      'action': 'TERMINATE'|'KEEP_ALIVE',
                      'terminationWaitTimeInMinutes': 123
                  },
                  'deploymentReadyOption': {
                      'actionOnTimeout': 'CONTINUE_DEPLOYMENT'|'STOP_DEPLOYMENT',
                      'waitTimeInMinutes': 123
                  },
                  'greenFleetProvisioningOption': {
                      'action': 'DISCOVER_EXISTING'|'COPY_AUTO_SCALING_GROUP'
                  }
              },
              loadBalancerInfo={
                  'elbInfoList': [
                      {
                          'name': 'string'
                      },
                  ],
                  'targetGroupInfoList': [
                      {
                          'name': 'string'
                      },
                  ],
                  'targetGroupPairInfoList': [
                      {
                          'targetGroups': [
                              {
                                  'name': 'string'
                              },
                          ],
                          'prodTrafficRoute': {
                              'listenerArns': [
                                  'string',
                              ]
                          },
                          'testTrafficRoute': {
                              'listenerArns': [
                                  'string',
                              ]
                          }
                      },
                  ]
              },
              ec2TagSet={
                  'ec2TagSetList': [
                      [
                          {
                              'Key': 'string',
                              'Value': 'string',
                              'Type': 'KEY_ONLY'|'VALUE_ONLY'|'KEY_AND_VALUE'
                          },
                      ],
                  ]
              },
              ecsServices=[
                  {
                      'serviceName': 'string',
                      'clusterName': 'string'
                  },
              ],
              onPremisesTagSet={
                  'onPremisesTagSetList': [
                      [
                          {
                              'Key': 'string',
                              'Value': 'string',
                              'Type': 'KEY_ONLY'|'VALUE_ONLY'|'KEY_AND_VALUE'
                          },
                      ],
                  ]
              },
              tags=[
                  {
                      'Key': 'string',
                      'Value': 'string'
                  },
              ]
          )
        :type applicationName: string
        :param applicationName: **[REQUIRED]**

          The name of an AWS CodeDeploy application associated with the IAM user or AWS account.

        :type deploymentGroupName: string
        :param deploymentGroupName: **[REQUIRED]**

          The name of a new deployment group for the specified application.

        :type deploymentConfigName: string
        :param deploymentConfigName:

          If specified, the deployment configuration name can be either one of the predefined
          configurations provided with AWS CodeDeploy or a custom deployment configuration that you
          create by calling the create deployment configuration operation.

          CodeDeployDefault.OneAtATime is the default deployment configuration. It is used if a
          configuration isn't specified for the deployment or deployment group.

          For more information about the predefined deployment configurations in AWS CodeDeploy, see
          `Working with Deployment Groups in AWS CodeDeploy
          <https://docs.aws.amazon.com/codedeploy/latest/userguide/deployment-configurations.html>`__
          in the AWS CodeDeploy User Guide.

        :type ec2TagFilters: list
        :param ec2TagFilters:

          The Amazon EC2 tags on which to filter. The deployment group includes EC2 instances with
          any of the specified tags. Cannot be used in the same call as ec2TagSet.

          - *(dict) --*

            Information about an EC2 tag filter.

            - **Key** *(string) --*

              The tag filter key.

            - **Value** *(string) --*

              The tag filter value.

            - **Type** *(string) --*

              The tag filter type:

              * KEY_ONLY: Key only.

              * VALUE_ONLY: Value only.

              * KEY_AND_VALUE: Key and value.

        :type onPremisesInstanceTagFilters: list
        :param onPremisesInstanceTagFilters:

          The on-premises instance tags on which to filter. The deployment group includes
          on-premises instances with any of the specified tags. Cannot be used in the same call as
          OnPremisesTagSet.

          - *(dict) --*

            Information about an on-premises instance tag filter.

            - **Key** *(string) --*

              The on-premises instance tag filter key.

            - **Value** *(string) --*

              The on-premises instance tag filter value.

            - **Type** *(string) --*

              The on-premises instance tag filter type:

              * KEY_ONLY: Key only.

              * VALUE_ONLY: Value only.

              * KEY_AND_VALUE: Key and value.

        :type autoScalingGroups: list
        :param autoScalingGroups:

          A list of associated Amazon EC2 Auto Scaling groups.

          - *(string) --*

        :type serviceRoleArn: string
        :param serviceRoleArn: **[REQUIRED]**

          A service role ARN that allows AWS CodeDeploy to act on the user's behalf when interacting
          with AWS services.

        :type triggerConfigurations: list
        :param triggerConfigurations:

          Information about triggers to create when the deployment group is created. For examples,
          see `Create a Trigger for an AWS CodeDeploy Event
          <https://docs.aws.amazon.com/codedeploy/latest/userguide/how-to-notify-sns.html>`__ in the
          AWS CodeDeploy User Guide.

          - *(dict) --*

            Information about notification triggers for the deployment group.

            - **triggerName** *(string) --*

              The name of the notification trigger.

            - **triggerTargetArn** *(string) --*

              The ARN of the Amazon Simple Notification Service topic through which notifications
              about deployment or instance events are sent.

            - **triggerEvents** *(list) --*

              The event type or types for which notifications are triggered.

              - *(string) --*

        :type alarmConfiguration: dict
        :param alarmConfiguration:

          Information to add about Amazon CloudWatch alarms when the deployment group is created.

          - **enabled** *(boolean) --*

            Indicates whether the alarm configuration is enabled.

          - **ignorePollAlarmFailure** *(boolean) --*

            Indicates whether a deployment should continue if information about the current state of
            alarms cannot be retrieved from Amazon CloudWatch. The default value is false.

            * true: The deployment proceeds even if alarm status information can't be retrieved from
            Amazon CloudWatch.

            * false: The deployment stops if alarm status information can't be retrieved from Amazon
            CloudWatch.

          - **alarms** *(list) --*

            A list of alarms configured for the deployment group. A maximum of 10 alarms can be
            added to a deployment group.

            - *(dict) --*

              Information about an alarm.

              - **name** *(string) --*

                The name of the alarm. Maximum length is 255 characters. Each alarm name can be used
                only once in a list of alarms.

        :type autoRollbackConfiguration: dict
        :param autoRollbackConfiguration:

          Configuration information for an automatic rollback that is added when a deployment group
          is created.

          - **enabled** *(boolean) --*

            Indicates whether a defined automatic rollback configuration is currently enabled.

          - **events** *(list) --*

            The event type or types that trigger a rollback.

            - *(string) --*

        :type deploymentStyle: dict
        :param deploymentStyle:

          Information about the type of deployment, in-place or blue/green, that you want to run and
          whether to route deployment traffic behind a load balancer.

          - **deploymentType** *(string) --*

            Indicates whether to run an in-place deployment or a blue/green deployment.

          - **deploymentOption** *(string) --*

            Indicates whether to route deployment traffic behind a load balancer.

        :type blueGreenDeploymentConfiguration: dict
        :param blueGreenDeploymentConfiguration:

          Information about blue/green deployment options for a deployment group.

          - **terminateBlueInstancesOnDeploymentSuccess** *(dict) --*

            Information about whether to terminate instances in the original fleet during a
            blue/green deployment.

            - **action** *(string) --*

              The action to take on instances in the original environment after a successful
              blue/green deployment.

              * TERMINATE: Instances are terminated after a specified wait time.

              * KEEP_ALIVE: Instances are left running after they are deregistered from the load
              balancer and removed from the deployment group.

            - **terminationWaitTimeInMinutes** *(integer) --*

              For an Amazon EC2 deployment, the number of minutes to wait after a successful
              blue/green deployment before terminating instances from the original environment.

              For an Amazon ECS deployment, the number of minutes before deleting the original
              (blue) task set. During an Amazon ECS deployment, CodeDeploy shifts traffic from the
              original (blue) task set to a replacement (green) task set.

              The maximum setting is 2880 minutes (2 days).

          - **deploymentReadyOption** *(dict) --*

            Information about the action to take when newly provisioned instances are ready to
            receive traffic in a blue/green deployment.

            - **actionOnTimeout** *(string) --*

              Information about when to reroute traffic from an original environment to a
              replacement environment in a blue/green deployment.

              * CONTINUE_DEPLOYMENT: Register new instances with the load balancer immediately after
              the new application revision is installed on the instances in the replacement
              environment.

              * STOP_DEPLOYMENT: Do not register new instances with a load balancer unless traffic
              rerouting is started using  ContinueDeployment . If traffic rerouting is not started
              before the end of the specified wait period, the deployment status is changed to
              Stopped.

            - **waitTimeInMinutes** *(integer) --*

              The number of minutes to wait before the status of a blue/green deployment is changed
              to Stopped if rerouting is not started manually. Applies only to the STOP_DEPLOYMENT
              option for actionOnTimeout

          - **greenFleetProvisioningOption** *(dict) --*

            Information about how instances are provisioned for a replacement environment in a
            blue/green deployment.

            - **action** *(string) --*

              The method used to add instances to a replacement environment.

              * DISCOVER_EXISTING: Use instances that already exist or will be created manually.

              * COPY_AUTO_SCALING_GROUP: Use settings from a specified Auto Scaling group to define
              and create instances in a new Auto Scaling group.

        :type loadBalancerInfo: dict
        :param loadBalancerInfo:

          Information about the load balancer used in a deployment.

          - **elbInfoList** *(list) --*

            An array that contains information about the load balancer to use for load balancing in
            a deployment. In Elastic Load Balancing, load balancers are used with Classic Load
            Balancers.

            .. note::

              Adding more than one load balancer to the array is not supported.

            - *(dict) --*

              Information about a load balancer in Elastic Load Balancing to use in a deployment.
              Instances are registered directly with a load balancer, and traffic is routed to the
              load balancer.

              - **name** *(string) --*

                For blue/green deployments, the name of the load balancer that is used to route
                traffic from original instances to replacement instances in a blue/green deployment.
                For in-place deployments, the name of the load balancer that instances are
                deregistered from so they are not serving traffic during a deployment, and then
                re-registered with after the deployment is complete.

          - **targetGroupInfoList** *(list) --*

            An array that contains information about the target group to use for load balancing in a
            deployment. In Elastic Load Balancing, target groups are used with Application Load
            Balancers.

            .. note::

              Adding more than one target group to the array is not supported.

            - *(dict) --*

              Information about a target group in Elastic Load Balancing to use in a deployment.
              Instances are registered as targets in a target group, and traffic is routed to the
              target group.

              - **name** *(string) --*

                For blue/green deployments, the name of the target group that instances in the
                original environment are deregistered from, and instances in the replacement
                environment are registered with. For in-place deployments, the name of the target
                group that instances are deregistered from, so they are not serving traffic during a
                deployment, and then re-registered with after the deployment is complete.

          - **targetGroupPairInfoList** *(list) --*

            The target group pair information. This is an array of ``TargeGroupPairInfo`` objects
            with a maximum size of one.

            - *(dict) --*

              Information about two target groups and how traffic is routed during an Amazon ECS
              deployment. An optional test traffic route can be specified.

              - **targetGroups** *(list) --*

                One pair of target groups. One is associated with the original task set. The second
                is associated with the task set that serves traffic after the deployment is
                complete.

                - *(dict) --*

                  Information about a target group in Elastic Load Balancing to use in a deployment.
                  Instances are registered as targets in a target group, and traffic is routed to
                  the target group.

                  - **name** *(string) --*

                    For blue/green deployments, the name of the target group that instances in the
                    original environment are deregistered from, and instances in the replacement
                    environment are registered with. For in-place deployments, the name of the
                    target group that instances are deregistered from, so they are not serving
                    traffic during a deployment, and then re-registered with after the deployment is
                    complete.

              - **prodTrafficRoute** *(dict) --*

                The path used by a load balancer to route production traffic when an Amazon ECS
                deployment is complete.

                - **listenerArns** *(list) --*

                  The ARN of one listener. The listener identifies the route between a target group
                  and a load balancer. This is an array of strings with a maximum size of one.

                  - *(string) --*

              - **testTrafficRoute** *(dict) --*

                An optional path used by a load balancer to route test traffic after an Amazon ECS
                deployment. Validation can occur while test traffic is served during a deployment.

                - **listenerArns** *(list) --*

                  The ARN of one listener. The listener identifies the route between a target group
                  and a load balancer. This is an array of strings with a maximum size of one.

                  - *(string) --*

        :type ec2TagSet: dict
        :param ec2TagSet:

          Information about groups of tags applied to EC2 instances. The deployment group includes
          only EC2 instances identified by all the tag groups. Cannot be used in the same call as
          ec2TagFilters.

          - **ec2TagSetList** *(list) --*

            A list that contains other lists of EC2 instance tag groups. For an instance to be
            included in the deployment group, it must be identified by all of the tag groups in the
            list.

            - *(list) --*

              - *(dict) --*

                Information about an EC2 tag filter.

                - **Key** *(string) --*

                  The tag filter key.

                - **Value** *(string) --*

                  The tag filter value.

                - **Type** *(string) --*

                  The tag filter type:

                  * KEY_ONLY: Key only.

                  * VALUE_ONLY: Value only.

                  * KEY_AND_VALUE: Key and value.

        :type ecsServices: list
        :param ecsServices:

          The target Amazon ECS services in the deployment group. This applies only to deployment
          groups that use the Amazon ECS compute platform. A target Amazon ECS service is specified
          as an Amazon ECS cluster and service name pair using the format
          ``<clustername>:<servicename>`` .

          - *(dict) --*

            Contains the service and cluster names used to identify an Amazon ECS deployment's
            target.

            - **serviceName** *(string) --*

              The name of the target Amazon ECS service.

            - **clusterName** *(string) --*

              The name of the cluster that the Amazon ECS service is associated with.

        :type onPremisesTagSet: dict
        :param onPremisesTagSet:

          Information about groups of tags applied to on-premises instances. The deployment group
          includes only on-premises instances identified by all of the tag groups. Cannot be used in
          the same call as onPremisesInstanceTagFilters.

          - **onPremisesTagSetList** *(list) --*

            A list that contains other lists of on-premises instance tag groups. For an instance to
            be included in the deployment group, it must be identified by all of the tag groups in
            the list.

            - *(list) --*

              - *(dict) --*

                Information about an on-premises instance tag filter.

                - **Key** *(string) --*

                  The on-premises instance tag filter key.

                - **Value** *(string) --*

                  The on-premises instance tag filter value.

                - **Type** *(string) --*

                  The on-premises instance tag filter type:

                  * KEY_ONLY: Key only.

                  * VALUE_ONLY: Value only.

                  * KEY_AND_VALUE: Key and value.

        :type tags: list
        :param tags:

          The metadata that you apply to CodeDeploy deployment groups to help you organize and
          categorize them. Each tag consists of a key and an optional value, both of which you
          define.

          - *(dict) --*

            Information about a tag.

            - **Key** *(string) --*

              The tag's key.

            - **Value** *(string) --*

              The tag's value.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'deploymentGroupId': 'string'
            }
          **Response Structure**

          - *(dict) --*

            Represents the output of a CreateDeploymentGroup operation.

            - **deploymentGroupId** *(string) --*

              A unique deployment group ID.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_application(self, applicationName: str) -> None:
        """
        Deletes an application.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/codedeploy-2014-10-06/DeleteApplication>`_

        **Request Syntax**
        ::

          response = client.delete_application(
              applicationName='string'
          )
        :type applicationName: string
        :param applicationName: **[REQUIRED]**

          The name of an AWS CodeDeploy application associated with the IAM user or AWS account.

        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_deployment_config(self, deploymentConfigName: str) -> None:
        """
        Deletes a deployment configuration.

        .. note::

          A deployment configuration cannot be deleted if it is currently in use. Predefined
          configurations cannot be deleted.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/codedeploy-2014-10-06/DeleteDeploymentConfig>`_

        **Request Syntax**
        ::

          response = client.delete_deployment_config(
              deploymentConfigName='string'
          )
        :type deploymentConfigName: string
        :param deploymentConfigName: **[REQUIRED]**

          The name of a deployment configuration associated with the IAM user or AWS account.

        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_deployment_group(
        self, applicationName: str, deploymentGroupName: str
    ) -> ClientDeleteDeploymentGroupResponseTypeDef:
        """
        Deletes a deployment group.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/codedeploy-2014-10-06/DeleteDeploymentGroup>`_

        **Request Syntax**
        ::

          response = client.delete_deployment_group(
              applicationName='string',
              deploymentGroupName='string'
          )
        :type applicationName: string
        :param applicationName: **[REQUIRED]**

          The name of an AWS CodeDeploy application associated with the IAM user or AWS account.

        :type deploymentGroupName: string
        :param deploymentGroupName: **[REQUIRED]**

          The name of a deployment group for the specified application.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'hooksNotCleanedUp': [
                    {
                        'name': 'string',
                        'hook': 'string'
                    },
                ]
            }
          **Response Structure**

          - *(dict) --*

            Represents the output of a DeleteDeploymentGroup operation.

            - **hooksNotCleanedUp** *(list) --*

              If the output contains no data, and the corresponding deployment group contained at
              least one Auto Scaling group, AWS CodeDeploy successfully removed all corresponding
              Auto Scaling lifecycle event hooks from the Amazon EC2 instances in the Auto Scaling
              group. If the output contains data, AWS CodeDeploy could not remove some Auto Scaling
              lifecycle event hooks from the Amazon EC2 instances in the Auto Scaling group.

              - *(dict) --*

                Information about an Auto Scaling group.

                - **name** *(string) --*

                  The Auto Scaling group name.

                - **hook** *(string) --*

                  An Auto Scaling lifecycle event hook name.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_git_hub_account_token(
        self, tokenName: str = None
    ) -> ClientDeleteGitHubAccountTokenResponseTypeDef:
        """
        Deletes a GitHub account connection.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/codedeploy-2014-10-06/DeleteGitHubAccountToken>`_

        **Request Syntax**
        ::

          response = client.delete_git_hub_account_token(
              tokenName='string'
          )
        :type tokenName: string
        :param tokenName:

          The name of the GitHub account connection to delete.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'tokenName': 'string'
            }
          **Response Structure**

          - *(dict) --*

            Represents the output of a DeleteGitHubAccountToken operation.

            - **tokenName** *(string) --*

              The name of the GitHub account connection that was deleted.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def deregister_on_premises_instance(self, instanceName: str) -> None:
        """
        Deregisters an on-premises instance.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/codedeploy-2014-10-06/DeregisterOnPremisesInstance>`_

        **Request Syntax**
        ::

          response = client.deregister_on_premises_instance(
              instanceName='string'
          )
        :type instanceName: string
        :param instanceName: **[REQUIRED]**

          The name of the on-premises instance to deregister.

        :returns: None
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
    def get_application(self, applicationName: str) -> ClientGetApplicationResponseTypeDef:
        """
        Gets information about an application.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/codedeploy-2014-10-06/GetApplication>`_

        **Request Syntax**
        ::

          response = client.get_application(
              applicationName='string'
          )
        :type applicationName: string
        :param applicationName: **[REQUIRED]**

          The name of an AWS CodeDeploy application associated with the IAM user or AWS account.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'application': {
                    'applicationId': 'string',
                    'applicationName': 'string',
                    'createTime': datetime(2015, 1, 1),
                    'linkedToGitHub': True|False,
                    'gitHubAccountName': 'string',
                    'computePlatform': 'Server'|'Lambda'|'ECS'
                }
            }
          **Response Structure**

          - *(dict) --*

            Represents the output of a GetApplication operation.

            - **application** *(dict) --*

              Information about the application.

              - **applicationId** *(string) --*

                The application ID.

              - **applicationName** *(string) --*

                The application name.

              - **createTime** *(datetime) --*

                The time at which the application was created.

              - **linkedToGitHub** *(boolean) --*

                True if the user has authenticated with GitHub for the specified application.
                Otherwise, false.

              - **gitHubAccountName** *(string) --*

                The name for a connection to a GitHub account.

              - **computePlatform** *(string) --*

                The destination platform type for deployment of the application (``Lambda`` or
                ``Server`` ).
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_application_revision(
        self, applicationName: str, revision: ClientGetApplicationRevisionRevisionTypeDef
    ) -> ClientGetApplicationRevisionResponseTypeDef:
        """
        Gets information about an application revision.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/codedeploy-2014-10-06/GetApplicationRevision>`_

        **Request Syntax**
        ::

          response = client.get_application_revision(
              applicationName='string',
              revision={
                  'revisionType': 'S3'|'GitHub'|'String'|'AppSpecContent',
                  's3Location': {
                      'bucket': 'string',
                      'key': 'string',
                      'bundleType': 'tar'|'tgz'|'zip'|'YAML'|'JSON',
                      'version': 'string',
                      'eTag': 'string'
                  },
                  'gitHubLocation': {
                      'repository': 'string',
                      'commitId': 'string'
                  },
                  'string': {
                      'content': 'string',
                      'sha256': 'string'
                  },
                  'appSpecContent': {
                      'content': 'string',
                      'sha256': 'string'
                  }
              }
          )
        :type applicationName: string
        :param applicationName: **[REQUIRED]**

          The name of the application that corresponds to the revision.

        :type revision: dict
        :param revision: **[REQUIRED]**

          Information about the application revision to get, including type and location.

          - **revisionType** *(string) --*

            The type of application revision:

            * S3: An application revision stored in Amazon S3.

            * GitHub: An application revision stored in GitHub (EC2/On-premises deployments only).

            * String: A YAML-formatted or JSON-formatted string (AWS Lambda deployments only).

          - **s3Location** *(dict) --*

            Information about the location of a revision stored in Amazon S3.

            - **bucket** *(string) --*

              The name of the Amazon S3 bucket where the application revision is stored.

            - **key** *(string) --*

              The name of the Amazon S3 object that represents the bundled artifacts for the
              application revision.

            - **bundleType** *(string) --*

              The file type of the application revision. Must be one of the following:

              * tar: A tar archive file.

              * tgz: A compressed tar archive file.

              * zip: A zip archive file.

            - **version** *(string) --*

              A specific version of the Amazon S3 object that represents the bundled artifacts for
              the application revision.

              If the version is not specified, the system uses the most recent version by default.

            - **eTag** *(string) --*

              The ETag of the Amazon S3 object that represents the bundled artifacts for the
              application revision.

              If the ETag is not specified as an input parameter, ETag validation of the object is
              skipped.

          - **gitHubLocation** *(dict) --*

            Information about the location of application artifacts stored in GitHub.

            - **repository** *(string) --*

              The GitHub account and repository pair that stores a reference to the commit that
              represents the bundled artifacts for the application revision.

              Specified as account/repository.

            - **commitId** *(string) --*

              The SHA1 commit ID of the GitHub commit that represents the bundled artifacts for the
              application revision.

          - **string** *(dict) --*

            Information about the location of an AWS Lambda deployment revision stored as a
            RawString.

            - **content** *(string) --*

              The YAML-formatted or JSON-formatted revision string. It includes information about
              which Lambda function to update and optional Lambda functions that validate deployment
              lifecycle events.

            - **sha256** *(string) --*

              The SHA256 hash value of the revision content.

          - **appSpecContent** *(dict) --*

            The content of an AppSpec file for an AWS Lambda or Amazon ECS deployment. The content
            is formatted as JSON or YAML and stored as a RawString.

            - **content** *(string) --*

              The YAML-formatted or JSON-formatted revision string.

              For an AWS Lambda deployment, the content includes a Lambda function name, the alias
              for its original version, and the alias for its replacement version. The deployment
              shifts traffic from the original version of the Lambda function to the replacement
              version.

              For an Amazon ECS deployment, the content includes the task name, information about
              the load balancer that serves traffic to the container, and more.

              For both types of deployments, the content can specify Lambda functions that run at
              specified hooks, such as ``BeforeInstall`` , during a deployment.

            - **sha256** *(string) --*

              The SHA256 hash value of the revision content.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'applicationName': 'string',
                'revision': {
                    'revisionType': 'S3'|'GitHub'|'String'|'AppSpecContent',
                    's3Location': {
                        'bucket': 'string',
                        'key': 'string',
                        'bundleType': 'tar'|'tgz'|'zip'|'YAML'|'JSON',
                        'version': 'string',
                        'eTag': 'string'
                    },
                    'gitHubLocation': {
                        'repository': 'string',
                        'commitId': 'string'
                    },
                    'string': {
                        'content': 'string',
                        'sha256': 'string'
                    },
                    'appSpecContent': {
                        'content': 'string',
                        'sha256': 'string'
                    }
                },
                'revisionInfo': {
                    'description': 'string',
                    'deploymentGroups': [
                        'string',
                    ],
                    'firstUsedTime': datetime(2015, 1, 1),
                    'lastUsedTime': datetime(2015, 1, 1),
                    'registerTime': datetime(2015, 1, 1)
                }
            }
          **Response Structure**

          - *(dict) --*

            Represents the output of a GetApplicationRevision operation.

            - **applicationName** *(string) --*

              The name of the application that corresponds to the revision.

            - **revision** *(dict) --*

              Additional information about the revision, including type and location.

              - **revisionType** *(string) --*

                The type of application revision:

                * S3: An application revision stored in Amazon S3.

                * GitHub: An application revision stored in GitHub (EC2/On-premises deployments
                only).

                * String: A YAML-formatted or JSON-formatted string (AWS Lambda deployments only).

              - **s3Location** *(dict) --*

                Information about the location of a revision stored in Amazon S3.

                - **bucket** *(string) --*

                  The name of the Amazon S3 bucket where the application revision is stored.

                - **key** *(string) --*

                  The name of the Amazon S3 object that represents the bundled artifacts for the
                  application revision.

                - **bundleType** *(string) --*

                  The file type of the application revision. Must be one of the following:

                  * tar: A tar archive file.

                  * tgz: A compressed tar archive file.

                  * zip: A zip archive file.

                - **version** *(string) --*

                  A specific version of the Amazon S3 object that represents the bundled artifacts
                  for the application revision.

                  If the version is not specified, the system uses the most recent version by
                  default.

                - **eTag** *(string) --*

                  The ETag of the Amazon S3 object that represents the bundled artifacts for the
                  application revision.

                  If the ETag is not specified as an input parameter, ETag validation of the object
                  is skipped.

              - **gitHubLocation** *(dict) --*

                Information about the location of application artifacts stored in GitHub.

                - **repository** *(string) --*

                  The GitHub account and repository pair that stores a reference to the commit that
                  represents the bundled artifacts for the application revision.

                  Specified as account/repository.

                - **commitId** *(string) --*

                  The SHA1 commit ID of the GitHub commit that represents the bundled artifacts for
                  the application revision.

              - **string** *(dict) --*

                Information about the location of an AWS Lambda deployment revision stored as a
                RawString.

                - **content** *(string) --*

                  The YAML-formatted or JSON-formatted revision string. It includes information
                  about which Lambda function to update and optional Lambda functions that validate
                  deployment lifecycle events.

                - **sha256** *(string) --*

                  The SHA256 hash value of the revision content.

              - **appSpecContent** *(dict) --*

                The content of an AppSpec file for an AWS Lambda or Amazon ECS deployment. The
                content is formatted as JSON or YAML and stored as a RawString.

                - **content** *(string) --*

                  The YAML-formatted or JSON-formatted revision string.

                  For an AWS Lambda deployment, the content includes a Lambda function name, the
                  alias for its original version, and the alias for its replacement version. The
                  deployment shifts traffic from the original version of the Lambda function to the
                  replacement version.

                  For an Amazon ECS deployment, the content includes the task name, information
                  about the load balancer that serves traffic to the container, and more.

                  For both types of deployments, the content can specify Lambda functions that run
                  at specified hooks, such as ``BeforeInstall`` , during a deployment.

                - **sha256** *(string) --*

                  The SHA256 hash value of the revision content.

            - **revisionInfo** *(dict) --*

              General information about the revision.

              - **description** *(string) --*

                A comment about the revision.

              - **deploymentGroups** *(list) --*

                The deployment groups for which this is the current target revision.

                - *(string) --*

              - **firstUsedTime** *(datetime) --*

                When the revision was first used by AWS CodeDeploy.

              - **lastUsedTime** *(datetime) --*

                When the revision was last used by AWS CodeDeploy.

              - **registerTime** *(datetime) --*

                When the revision was registered with AWS CodeDeploy.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_deployment(self, deploymentId: str) -> ClientGetDeploymentResponseTypeDef:
        """
        Gets information about a deployment.

        .. note::

          The ``content`` property of the ``appSpecContent`` object in the returned revision is
          always null. Use ``GetApplicationRevision`` and the ``sha256`` property of the returned
          ``appSpecContent`` object to get the content of the deployment’s AppSpec file.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/codedeploy-2014-10-06/GetDeployment>`_

        **Request Syntax**
        ::

          response = client.get_deployment(
              deploymentId='string'
          )
        :type deploymentId: string
        :param deploymentId: **[REQUIRED]**

          The unique ID of a deployment associated with the IAM user or AWS account.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'deploymentInfo': {
                    'applicationName': 'string',
                    'deploymentGroupName': 'string',
                    'deploymentConfigName': 'string',
                    'deploymentId': 'string',
                    'previousRevision': {
                        'revisionType': 'S3'|'GitHub'|'String'|'AppSpecContent',
                        's3Location': {
                            'bucket': 'string',
                            'key': 'string',
                            'bundleType': 'tar'|'tgz'|'zip'|'YAML'|'JSON',
                            'version': 'string',
                            'eTag': 'string'
                        },
                        'gitHubLocation': {
                            'repository': 'string',
                            'commitId': 'string'
                        },
                        'string': {
                            'content': 'string',
                            'sha256': 'string'
                        },
                        'appSpecContent': {
                            'content': 'string',
                            'sha256': 'string'
                        }
                    },
                    'revision': {
                        'revisionType': 'S3'|'GitHub'|'String'|'AppSpecContent',
                        's3Location': {
                            'bucket': 'string',
                            'key': 'string',
                            'bundleType': 'tar'|'tgz'|'zip'|'YAML'|'JSON',
                            'version': 'string',
                            'eTag': 'string'
                        },
                        'gitHubLocation': {
                            'repository': 'string',
                            'commitId': 'string'
                        },
                        'string': {
                            'content': 'string',
                            'sha256': 'string'
                        },
                        'appSpecContent': {
                            'content': 'string',
                            'sha256': 'string'
                        }
                    },
                    'status':
                    'Created'|'Queued'|'InProgress'|'Succeeded'|'Failed'|'Stopped'
                    |'Ready',
                    'errorInformation': {
                        'code':
                        'AGENT_ISSUE'|'ALARM_ACTIVE'|'APPLICATION_MISSING'
                        |'AUTOSCALING_VALIDATION_ERROR'|'AUTO_SCALING_CONFIGURATION'
                        |'AUTO_SCALING_IAM_ROLE_PERMISSIONS'
                        |'CODEDEPLOY_RESOURCE_CANNOT_BE_FOUND'
                        |'CUSTOMER_APPLICATION_UNHEALTHY'|'DEPLOYMENT_GROUP_MISSING'
                        |'ECS_UPDATE_ERROR'|'ELASTIC_LOAD_BALANCING_INVALID'
                        |'ELB_INVALID_INSTANCE'|'HEALTH_CONSTRAINTS'
                        |'HEALTH_CONSTRAINTS_INVALID'|'HOOK_EXECUTION_FAILURE'
                        |'IAM_ROLE_MISSING'|'IAM_ROLE_PERMISSIONS'|'INTERNAL_ERROR'
                        |'INVALID_ECS_SERVICE'|'INVALID_LAMBDA_CONFIGURATION'
                        |'INVALID_LAMBDA_FUNCTION'|'INVALID_REVISION'|'MANUAL_STOP'
                        |'MISSING_BLUE_GREEN_DEPLOYMENT_CONFIGURATION'
                        |'MISSING_ELB_INFORMATION'|'MISSING_GITHUB_TOKEN'
                        |'NO_EC2_SUBSCRIPTION'|'NO_INSTANCES'|'OVER_MAX_INSTANCES'
                        |'RESOURCE_LIMIT_EXCEEDED'|'REVISION_MISSING'|'THROTTLED'
                        |'TIMEOUT',
                        'message': 'string'
                    },
                    'createTime': datetime(2015, 1, 1),
                    'startTime': datetime(2015, 1, 1),
                    'completeTime': datetime(2015, 1, 1),
                    'deploymentOverview': {
                        'Pending': 123,
                        'InProgress': 123,
                        'Succeeded': 123,
                        'Failed': 123,
                        'Skipped': 123,
                        'Ready': 123
                    },
                    'description': 'string',
                    'creator': 'user'|'autoscaling'|'codeDeployRollback',
                    'ignoreApplicationStopFailures': True|False,
                    'autoRollbackConfiguration': {
                        'enabled': True|False,
                        'events': [
                            'DEPLOYMENT_FAILURE'|'DEPLOYMENT_STOP_ON_ALARM'
                            |'DEPLOYMENT_STOP_ON_REQUEST',
                        ]
                    },
                    'updateOutdatedInstancesOnly': True|False,
                    'rollbackInfo': {
                        'rollbackDeploymentId': 'string',
                        'rollbackTriggeringDeploymentId': 'string',
                        'rollbackMessage': 'string'
                    },
                    'deploymentStyle': {
                        'deploymentType': 'IN_PLACE'|'BLUE_GREEN',
                        'deploymentOption': 'WITH_TRAFFIC_CONTROL'|'WITHOUT_TRAFFIC_CONTROL'
                    },
                    'targetInstances': {
                        'tagFilters': [
                            {
                                'Key': 'string',
                                'Value': 'string',
                                'Type': 'KEY_ONLY'|'VALUE_ONLY'|'KEY_AND_VALUE'
                            },
                        ],
                        'autoScalingGroups': [
                            'string',
                        ],
                        'ec2TagSet': {
                            'ec2TagSetList': [
                                [
                                    {
                                        'Key': 'string',
                                        'Value': 'string',
                                        'Type': 'KEY_ONLY'|'VALUE_ONLY'|'KEY_AND_VALUE'
                                    },
                                ],
                            ]
                        }
                    },
                    'instanceTerminationWaitTimeStarted': True|False,
                    'blueGreenDeploymentConfiguration': {
                        'terminateBlueInstancesOnDeploymentSuccess': {
                            'action': 'TERMINATE'|'KEEP_ALIVE',
                            'terminationWaitTimeInMinutes': 123
                        },
                        'deploymentReadyOption': {
                            'actionOnTimeout': 'CONTINUE_DEPLOYMENT'|'STOP_DEPLOYMENT',
                            'waitTimeInMinutes': 123
                        },
                        'greenFleetProvisioningOption': {
                            'action': 'DISCOVER_EXISTING'|'COPY_AUTO_SCALING_GROUP'
                        }
                    },
                    'loadBalancerInfo': {
                        'elbInfoList': [
                            {
                                'name': 'string'
                            },
                        ],
                        'targetGroupInfoList': [
                            {
                                'name': 'string'
                            },
                        ],
                        'targetGroupPairInfoList': [
                            {
                                'targetGroups': [
                                    {
                                        'name': 'string'
                                    },
                                ],
                                'prodTrafficRoute': {
                                    'listenerArns': [
                                        'string',
                                    ]
                                },
                                'testTrafficRoute': {
                                    'listenerArns': [
                                        'string',
                                    ]
                                }
                            },
                        ]
                    },
                    'additionalDeploymentStatusInfo': 'string',
                    'fileExistsBehavior': 'DISALLOW'|'OVERWRITE'|'RETAIN',
                    'deploymentStatusMessages': [
                        'string',
                    ],
                    'computePlatform': 'Server'|'Lambda'|'ECS'
                }
            }
          **Response Structure**

          - *(dict) --*

            Represents the output of a GetDeployment operation.

            - **deploymentInfo** *(dict) --*

              Information about the deployment.

              - **applicationName** *(string) --*

                The application name.

              - **deploymentGroupName** *(string) --*

                The deployment group name.

              - **deploymentConfigName** *(string) --*

                The deployment configuration name.

              - **deploymentId** *(string) --*

                The unique ID of a deployment.

              - **previousRevision** *(dict) --*

                Information about the application revision that was deployed to the deployment group
                before the most recent successful deployment.

                - **revisionType** *(string) --*

                  The type of application revision:

                  * S3: An application revision stored in Amazon S3.

                  * GitHub: An application revision stored in GitHub (EC2/On-premises deployments
                  only).

                  * String: A YAML-formatted or JSON-formatted string (AWS Lambda deployments only).

                - **s3Location** *(dict) --*

                  Information about the location of a revision stored in Amazon S3.

                  - **bucket** *(string) --*

                    The name of the Amazon S3 bucket where the application revision is stored.

                  - **key** *(string) --*

                    The name of the Amazon S3 object that represents the bundled artifacts for the
                    application revision.

                  - **bundleType** *(string) --*

                    The file type of the application revision. Must be one of the following:

                    * tar: A tar archive file.

                    * tgz: A compressed tar archive file.

                    * zip: A zip archive file.

                  - **version** *(string) --*

                    A specific version of the Amazon S3 object that represents the bundled artifacts
                    for the application revision.

                    If the version is not specified, the system uses the most recent version by
                    default.

                  - **eTag** *(string) --*

                    The ETag of the Amazon S3 object that represents the bundled artifacts for the
                    application revision.

                    If the ETag is not specified as an input parameter, ETag validation of the
                    object is skipped.

                - **gitHubLocation** *(dict) --*

                  Information about the location of application artifacts stored in GitHub.

                  - **repository** *(string) --*

                    The GitHub account and repository pair that stores a reference to the commit
                    that represents the bundled artifacts for the application revision.

                    Specified as account/repository.

                  - **commitId** *(string) --*

                    The SHA1 commit ID of the GitHub commit that represents the bundled artifacts
                    for the application revision.

                - **string** *(dict) --*

                  Information about the location of an AWS Lambda deployment revision stored as a
                  RawString.

                  - **content** *(string) --*

                    The YAML-formatted or JSON-formatted revision string. It includes information
                    about which Lambda function to update and optional Lambda functions that
                    validate deployment lifecycle events.

                  - **sha256** *(string) --*

                    The SHA256 hash value of the revision content.

                - **appSpecContent** *(dict) --*

                  The content of an AppSpec file for an AWS Lambda or Amazon ECS deployment. The
                  content is formatted as JSON or YAML and stored as a RawString.

                  - **content** *(string) --*

                    The YAML-formatted or JSON-formatted revision string.

                    For an AWS Lambda deployment, the content includes a Lambda function name, the
                    alias for its original version, and the alias for its replacement version. The
                    deployment shifts traffic from the original version of the Lambda function to
                    the replacement version.

                    For an Amazon ECS deployment, the content includes the task name, information
                    about the load balancer that serves traffic to the container, and more.

                    For both types of deployments, the content can specify Lambda functions that run
                    at specified hooks, such as ``BeforeInstall`` , during a deployment.

                  - **sha256** *(string) --*

                    The SHA256 hash value of the revision content.

              - **revision** *(dict) --*

                Information about the location of stored application artifacts and the service from
                which to retrieve them.

                - **revisionType** *(string) --*

                  The type of application revision:

                  * S3: An application revision stored in Amazon S3.

                  * GitHub: An application revision stored in GitHub (EC2/On-premises deployments
                  only).

                  * String: A YAML-formatted or JSON-formatted string (AWS Lambda deployments only).

                - **s3Location** *(dict) --*

                  Information about the location of a revision stored in Amazon S3.

                  - **bucket** *(string) --*

                    The name of the Amazon S3 bucket where the application revision is stored.

                  - **key** *(string) --*

                    The name of the Amazon S3 object that represents the bundled artifacts for the
                    application revision.

                  - **bundleType** *(string) --*

                    The file type of the application revision. Must be one of the following:

                    * tar: A tar archive file.

                    * tgz: A compressed tar archive file.

                    * zip: A zip archive file.

                  - **version** *(string) --*

                    A specific version of the Amazon S3 object that represents the bundled artifacts
                    for the application revision.

                    If the version is not specified, the system uses the most recent version by
                    default.

                  - **eTag** *(string) --*

                    The ETag of the Amazon S3 object that represents the bundled artifacts for the
                    application revision.

                    If the ETag is not specified as an input parameter, ETag validation of the
                    object is skipped.

                - **gitHubLocation** *(dict) --*

                  Information about the location of application artifacts stored in GitHub.

                  - **repository** *(string) --*

                    The GitHub account and repository pair that stores a reference to the commit
                    that represents the bundled artifacts for the application revision.

                    Specified as account/repository.

                  - **commitId** *(string) --*

                    The SHA1 commit ID of the GitHub commit that represents the bundled artifacts
                    for the application revision.

                - **string** *(dict) --*

                  Information about the location of an AWS Lambda deployment revision stored as a
                  RawString.

                  - **content** *(string) --*

                    The YAML-formatted or JSON-formatted revision string. It includes information
                    about which Lambda function to update and optional Lambda functions that
                    validate deployment lifecycle events.

                  - **sha256** *(string) --*

                    The SHA256 hash value of the revision content.

                - **appSpecContent** *(dict) --*

                  The content of an AppSpec file for an AWS Lambda or Amazon ECS deployment. The
                  content is formatted as JSON or YAML and stored as a RawString.

                  - **content** *(string) --*

                    The YAML-formatted or JSON-formatted revision string.

                    For an AWS Lambda deployment, the content includes a Lambda function name, the
                    alias for its original version, and the alias for its replacement version. The
                    deployment shifts traffic from the original version of the Lambda function to
                    the replacement version.

                    For an Amazon ECS deployment, the content includes the task name, information
                    about the load balancer that serves traffic to the container, and more.

                    For both types of deployments, the content can specify Lambda functions that run
                    at specified hooks, such as ``BeforeInstall`` , during a deployment.

                  - **sha256** *(string) --*

                    The SHA256 hash value of the revision content.

              - **status** *(string) --*

                The current state of the deployment as a whole.

              - **errorInformation** *(dict) --*

                Information about any error associated with this deployment.

                - **code** *(string) --*

                  For more information, see `Error Codes for AWS CodeDeploy
                  <https://docs.aws.amazon.com/codedeploy/latest/userguide/error-codes.html>`__ in
                  the `AWS CodeDeploy User Guide
                  <https://docs.aws.amazon.com/codedeploy/latest/userguide>`__ .

                  The error code:

                  * APPLICATION_MISSING: The application was missing. This error code is most likely
                  raised if the application is deleted after the deployment is created, but before
                  it is started.

                  * DEPLOYMENT_GROUP_MISSING: The deployment group was missing. This error code is
                  most likely raised if the deployment group is deleted after the deployment is
                  created, but before it is started.

                  * HEALTH_CONSTRAINTS: The deployment failed on too many instances to be
                  successfully deployed within the instance health constraints specified.

                  * HEALTH_CONSTRAINTS_INVALID: The revision cannot be successfully deployed within
                  the instance health constraints specified.

                  * IAM_ROLE_MISSING: The service role cannot be accessed.

                  * IAM_ROLE_PERMISSIONS: The service role does not have the correct permissions.

                  * INTERNAL_ERROR: There was an internal error.

                  * NO_EC2_SUBSCRIPTION: The calling account is not subscribed to Amazon EC2.

                  * NO_INSTANCES: No instances were specified, or no instances can be found.

                  * OVER_MAX_INSTANCES: The maximum number of instances was exceeded.

                  * THROTTLED: The operation was throttled because the calling account exceeded the
                  throttling limits of one or more AWS services.

                  * TIMEOUT: The deployment has timed out.

                  * REVISION_MISSING: The revision ID was missing. This error code is most likely
                  raised if the revision is deleted after the deployment is created, but before it
                  is started.

                - **message** *(string) --*

                  An accompanying error message.

              - **createTime** *(datetime) --*

                A timestamp that indicates when the deployment was created.

              - **startTime** *(datetime) --*

                A timestamp that indicates when the deployment was deployed to the deployment group.

                In some cases, the reported value of the start time might be later than the complete
                time. This is due to differences in the clock settings of backend servers that
                participate in the deployment process.

              - **completeTime** *(datetime) --*

                A timestamp that indicates when the deployment was complete.

              - **deploymentOverview** *(dict) --*

                A summary of the deployment status of the instances in the deployment.

                - **Pending** *(integer) --*

                  The number of instances in the deployment in a pending state.

                - **InProgress** *(integer) --*

                  The number of instances in which the deployment is in progress.

                - **Succeeded** *(integer) --*

                  The number of instances in the deployment to which revisions have been
                  successfully deployed.

                - **Failed** *(integer) --*

                  The number of instances in the deployment in a failed state.

                - **Skipped** *(integer) --*

                  The number of instances in the deployment in a skipped state.

                - **Ready** *(integer) --*

                  The number of instances in a replacement environment ready to receive traffic in a
                  blue/green deployment.

              - **description** *(string) --*

                A comment about the deployment.

              - **creator** *(string) --*

                The means by which the deployment was created:

                * user: A user created the deployment.

                * autoscaling: Amazon EC2 Auto Scaling created the deployment.

                * codeDeployRollback: A rollback process created the deployment.

              - **ignoreApplicationStopFailures** *(boolean) --*

                If true, then if an ``ApplicationStop`` , ``BeforeBlockTraffic`` , or
                ``AfterBlockTraffic`` deployment lifecycle event to an instance fails, then the
                deployment continues to the next deployment lifecycle event. For example, if
                ``ApplicationStop`` fails, the deployment continues with DownloadBundle. If
                ``BeforeBlockTraffic`` fails, the deployment continues with ``BlockTraffic`` . If
                ``AfterBlockTraffic`` fails, the deployment continues with ``ApplicationStop`` .

                If false or not specified, then if a lifecycle event fails during a deployment to an
                instance, that deployment fails. If deployment to that instance is part of an
                overall deployment and the number of healthy hosts is not less than the minimum
                number of healthy hosts, then a deployment to the next instance is attempted.

                During a deployment, the AWS CodeDeploy agent runs the scripts specified for
                ``ApplicationStop`` , ``BeforeBlockTraffic`` , and ``AfterBlockTraffic`` in the
                AppSpec file from the previous successful deployment. (All other scripts are run
                from the AppSpec file in the current deployment.) If one of these scripts contains
                an error and does not run successfully, the deployment can fail.

                If the cause of the failure is a script from the last successful deployment that
                will never run successfully, create a new deployment and use
                ``ignoreApplicationStopFailures`` to specify that the ``ApplicationStop`` ,
                ``BeforeBlockTraffic`` , and ``AfterBlockTraffic`` failures should be ignored.

              - **autoRollbackConfiguration** *(dict) --*

                Information about the automatic rollback configuration associated with the
                deployment.

                - **enabled** *(boolean) --*

                  Indicates whether a defined automatic rollback configuration is currently enabled.

                - **events** *(list) --*

                  The event type or types that trigger a rollback.

                  - *(string) --*

              - **updateOutdatedInstancesOnly** *(boolean) --*

                Indicates whether only instances that are not running the latest application
                revision are to be deployed to.

              - **rollbackInfo** *(dict) --*

                Information about a deployment rollback.

                - **rollbackDeploymentId** *(string) --*

                  The ID of the deployment rollback.

                - **rollbackTriggeringDeploymentId** *(string) --*

                  The deployment ID of the deployment that was underway and triggered a rollback
                  deployment because it failed or was stopped.

                - **rollbackMessage** *(string) --*

                  Information that describes the status of a deployment rollback (for example,
                  whether the deployment can't be rolled back, is in progress, failed, or
                  succeeded).

              - **deploymentStyle** *(dict) --*

                Information about the type of deployment, either in-place or blue/green, you want to
                run and whether to route deployment traffic behind a load balancer.

                - **deploymentType** *(string) --*

                  Indicates whether to run an in-place deployment or a blue/green deployment.

                - **deploymentOption** *(string) --*

                  Indicates whether to route deployment traffic behind a load balancer.

              - **targetInstances** *(dict) --*

                Information about the instances that belong to the replacement environment in a
                blue/green deployment.

                - **tagFilters** *(list) --*

                  The tag filter key, type, and value used to identify Amazon EC2 instances in a
                  replacement environment for a blue/green deployment. Cannot be used in the same
                  call as ec2TagSet.

                  - *(dict) --*

                    Information about an EC2 tag filter.

                    - **Key** *(string) --*

                      The tag filter key.

                    - **Value** *(string) --*

                      The tag filter value.

                    - **Type** *(string) --*

                      The tag filter type:

                      * KEY_ONLY: Key only.

                      * VALUE_ONLY: Value only.

                      * KEY_AND_VALUE: Key and value.

                - **autoScalingGroups** *(list) --*

                  The names of one or more Auto Scaling groups to identify a replacement environment
                  for a blue/green deployment.

                  - *(string) --*

                - **ec2TagSet** *(dict) --*

                  Information about the groups of EC2 instance tags that an instance must be
                  identified by in order for it to be included in the replacement environment for a
                  blue/green deployment. Cannot be used in the same call as tagFilters.

                  - **ec2TagSetList** *(list) --*

                    A list that contains other lists of EC2 instance tag groups. For an instance to
                    be included in the deployment group, it must be identified by all of the tag
                    groups in the list.

                    - *(list) --*

                      - *(dict) --*

                        Information about an EC2 tag filter.

                        - **Key** *(string) --*

                          The tag filter key.

                        - **Value** *(string) --*

                          The tag filter value.

                        - **Type** *(string) --*

                          The tag filter type:

                          * KEY_ONLY: Key only.

                          * VALUE_ONLY: Value only.

                          * KEY_AND_VALUE: Key and value.

              - **instanceTerminationWaitTimeStarted** *(boolean) --*

                Indicates whether the wait period set for the termination of instances in the
                original environment has started. Status is 'false' if the KEEP_ALIVE option is
                specified. Otherwise, 'true' as soon as the termination wait period starts.

              - **blueGreenDeploymentConfiguration** *(dict) --*

                Information about blue/green deployment options for this deployment.

                - **terminateBlueInstancesOnDeploymentSuccess** *(dict) --*

                  Information about whether to terminate instances in the original fleet during a
                  blue/green deployment.

                  - **action** *(string) --*

                    The action to take on instances in the original environment after a successful
                    blue/green deployment.

                    * TERMINATE: Instances are terminated after a specified wait time.

                    * KEEP_ALIVE: Instances are left running after they are deregistered from the
                    load balancer and removed from the deployment group.

                  - **terminationWaitTimeInMinutes** *(integer) --*

                    For an Amazon EC2 deployment, the number of minutes to wait after a successful
                    blue/green deployment before terminating instances from the original
                    environment.

                    For an Amazon ECS deployment, the number of minutes before deleting the original
                    (blue) task set. During an Amazon ECS deployment, CodeDeploy shifts traffic from
                    the original (blue) task set to a replacement (green) task set.

                    The maximum setting is 2880 minutes (2 days).

                - **deploymentReadyOption** *(dict) --*

                  Information about the action to take when newly provisioned instances are ready to
                  receive traffic in a blue/green deployment.

                  - **actionOnTimeout** *(string) --*

                    Information about when to reroute traffic from an original environment to a
                    replacement environment in a blue/green deployment.

                    * CONTINUE_DEPLOYMENT: Register new instances with the load balancer immediately
                    after the new application revision is installed on the instances in the
                    replacement environment.

                    * STOP_DEPLOYMENT: Do not register new instances with a load balancer unless
                    traffic rerouting is started using  ContinueDeployment . If traffic rerouting is
                    not started before the end of the specified wait period, the deployment status
                    is changed to Stopped.

                  - **waitTimeInMinutes** *(integer) --*

                    The number of minutes to wait before the status of a blue/green deployment is
                    changed to Stopped if rerouting is not started manually. Applies only to the
                    STOP_DEPLOYMENT option for actionOnTimeout

                - **greenFleetProvisioningOption** *(dict) --*

                  Information about how instances are provisioned for a replacement environment in a
                  blue/green deployment.

                  - **action** *(string) --*

                    The method used to add instances to a replacement environment.

                    * DISCOVER_EXISTING: Use instances that already exist or will be created
                    manually.

                    * COPY_AUTO_SCALING_GROUP: Use settings from a specified Auto Scaling group to
                    define and create instances in a new Auto Scaling group.

              - **loadBalancerInfo** *(dict) --*

                Information about the load balancer used in the deployment.

                - **elbInfoList** *(list) --*

                  An array that contains information about the load balancer to use for load
                  balancing in a deployment. In Elastic Load Balancing, load balancers are used with
                  Classic Load Balancers.

                  .. note::

                    Adding more than one load balancer to the array is not supported.

                  - *(dict) --*

                    Information about a load balancer in Elastic Load Balancing to use in a
                    deployment. Instances are registered directly with a load balancer, and traffic
                    is routed to the load balancer.

                    - **name** *(string) --*

                      For blue/green deployments, the name of the load balancer that is used to
                      route traffic from original instances to replacement instances in a blue/green
                      deployment. For in-place deployments, the name of the load balancer that
                      instances are deregistered from so they are not serving traffic during a
                      deployment, and then re-registered with after the deployment is complete.

                - **targetGroupInfoList** *(list) --*

                  An array that contains information about the target group to use for load
                  balancing in a deployment. In Elastic Load Balancing, target groups are used with
                  Application Load Balancers.

                  .. note::

                    Adding more than one target group to the array is not supported.

                  - *(dict) --*

                    Information about a target group in Elastic Load Balancing to use in a
                    deployment. Instances are registered as targets in a target group, and traffic
                    is routed to the target group.

                    - **name** *(string) --*

                      For blue/green deployments, the name of the target group that instances in the
                      original environment are deregistered from, and instances in the replacement
                      environment are registered with. For in-place deployments, the name of the
                      target group that instances are deregistered from, so they are not serving
                      traffic during a deployment, and then re-registered with after the deployment
                      is complete.

                - **targetGroupPairInfoList** *(list) --*

                  The target group pair information. This is an array of ``TargeGroupPairInfo``
                  objects with a maximum size of one.

                  - *(dict) --*

                    Information about two target groups and how traffic is routed during an Amazon
                    ECS deployment. An optional test traffic route can be specified.

                    - **targetGroups** *(list) --*

                      One pair of target groups. One is associated with the original task set. The
                      second is associated with the task set that serves traffic after the
                      deployment is complete.

                      - *(dict) --*

                        Information about a target group in Elastic Load Balancing to use in a
                        deployment. Instances are registered as targets in a target group, and
                        traffic is routed to the target group.

                        - **name** *(string) --*

                          For blue/green deployments, the name of the target group that instances in
                          the original environment are deregistered from, and instances in the
                          replacement environment are registered with. For in-place deployments, the
                          name of the target group that instances are deregistered from, so they are
                          not serving traffic during a deployment, and then re-registered with after
                          the deployment is complete.

                    - **prodTrafficRoute** *(dict) --*

                      The path used by a load balancer to route production traffic when an Amazon
                      ECS deployment is complete.

                      - **listenerArns** *(list) --*

                        The ARN of one listener. The listener identifies the route between a target
                        group and a load balancer. This is an array of strings with a maximum size
                        of one.

                        - *(string) --*

                    - **testTrafficRoute** *(dict) --*

                      An optional path used by a load balancer to route test traffic after an Amazon
                      ECS deployment. Validation can occur while test traffic is served during a
                      deployment.

                      - **listenerArns** *(list) --*

                        The ARN of one listener. The listener identifies the route between a target
                        group and a load balancer. This is an array of strings with a maximum size
                        of one.

                        - *(string) --*

              - **additionalDeploymentStatusInfo** *(string) --*

                Provides information about the results of a deployment, such as whether instances in
                the original environment in a blue/green deployment were not terminated.

              - **fileExistsBehavior** *(string) --*

                Information about how AWS CodeDeploy handles files that already exist in a
                deployment target location but weren't part of the previous successful deployment.

                * DISALLOW: The deployment fails. This is also the default behavior if no option is
                specified.

                * OVERWRITE: The version of the file from the application revision currently being
                deployed replaces the version already on the instance.

                * RETAIN: The version of the file already on the instance is kept and used as part
                of the new deployment.

              - **deploymentStatusMessages** *(list) --*

                Messages that contain information about the status of a deployment.

                - *(string) --*

              - **computePlatform** *(string) --*

                The destination platform type for the deployment (``Lambda`` , ``Server`` , or
                ``ECS`` ).
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_deployment_config(
        self, deploymentConfigName: str
    ) -> ClientGetDeploymentConfigResponseTypeDef:
        """
        Gets information about a deployment configuration.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/codedeploy-2014-10-06/GetDeploymentConfig>`_

        **Request Syntax**
        ::

          response = client.get_deployment_config(
              deploymentConfigName='string'
          )
        :type deploymentConfigName: string
        :param deploymentConfigName: **[REQUIRED]**

          The name of a deployment configuration associated with the IAM user or AWS account.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'deploymentConfigInfo': {
                    'deploymentConfigId': 'string',
                    'deploymentConfigName': 'string',
                    'minimumHealthyHosts': {
                        'value': 123,
                        'type': 'HOST_COUNT'|'FLEET_PERCENT'
                    },
                    'createTime': datetime(2015, 1, 1),
                    'computePlatform': 'Server'|'Lambda'|'ECS',
                    'trafficRoutingConfig': {
                        'type': 'TimeBasedCanary'|'TimeBasedLinear'|'AllAtOnce',
                        'timeBasedCanary': {
                            'canaryPercentage': 123,
                            'canaryInterval': 123
                        },
                        'timeBasedLinear': {
                            'linearPercentage': 123,
                            'linearInterval': 123
                        }
                    }
                }
            }
          **Response Structure**

          - *(dict) --*

            Represents the output of a GetDeploymentConfig operation.

            - **deploymentConfigInfo** *(dict) --*

              Information about the deployment configuration.

              - **deploymentConfigId** *(string) --*

                The deployment configuration ID.

              - **deploymentConfigName** *(string) --*

                The deployment configuration name.

              - **minimumHealthyHosts** *(dict) --*

                Information about the number or percentage of minimum healthy instance.

                - **value** *(integer) --*

                  The minimum healthy instance value.

                - **type** *(string) --*

                  The minimum healthy instance type:

                  * HOST_COUNT: The minimum number of healthy instance as an absolute value.

                  * FLEET_PERCENT: The minimum number of healthy instance as a percentage of the
                  total number of instance in the deployment.

                  In an example of nine instance, if a HOST_COUNT of six is specified, deploy to up
                  to three instances at a time. The deployment is successful if six or more
                  instances are deployed to successfully. Otherwise, the deployment fails. If a
                  FLEET_PERCENT of 40 is specified, deploy to up to five instance at a time. The
                  deployment is successful if four or more instance are deployed to successfully.
                  Otherwise, the deployment fails.

                  .. note::

                    In a call to the ``GetDeploymentConfig`` , CodeDeployDefault.OneAtATime returns
                    a minimum healthy instance type of MOST_CONCURRENCY and a value of 1. This means
                    a deployment to only one instance at a time. (You cannot set the type to
                    MOST_CONCURRENCY, only to HOST_COUNT or FLEET_PERCENT.) In addition, with
                    CodeDeployDefault.OneAtATime, AWS CodeDeploy attempts to ensure that all
                    instances but one are kept in a healthy state during the deployment. Although
                    this allows one instance at a time to be taken offline for a new deployment, it
                    also means that if the deployment to the last instance fails, the overall
                    deployment is still successful.

                  For more information, see `AWS CodeDeploy Instance Health
                  <https://docs.aws.amazon.com/codedeploy/latest/userguide/instances-health.html>`__
                  in the *AWS CodeDeploy User Guide* .

              - **createTime** *(datetime) --*

                The time at which the deployment configuration was created.

              - **computePlatform** *(string) --*

                The destination platform type for the deployment (``Lambda`` , ``Server`` , or
                ``ECS`` ).

              - **trafficRoutingConfig** *(dict) --*

                The configuration that specifies how the deployment traffic is routed. Only
                deployments with a Lambda compute platform can specify this.

                - **type** *(string) --*

                  The type of traffic shifting (``TimeBasedCanary`` or ``TimeBasedLinear`` ) used by
                  a deployment configuration .

                - **timeBasedCanary** *(dict) --*

                  A configuration that shifts traffic from one version of a Lambda function to
                  another in two increments. The original and target Lambda function versions are
                  specified in the deployment's AppSpec file.

                  - **canaryPercentage** *(integer) --*

                    The percentage of traffic to shift in the first increment of a
                    ``TimeBasedCanary`` deployment.

                  - **canaryInterval** *(integer) --*

                    The number of minutes between the first and second traffic shifts of a
                    ``TimeBasedCanary`` deployment.

                - **timeBasedLinear** *(dict) --*

                  A configuration that shifts traffic from one version of a Lambda function to
                  another in equal increments, with an equal number of minutes between each
                  increment. The original and target Lambda function versions are specified in the
                  deployment's AppSpec file.

                  - **linearPercentage** *(integer) --*

                    The percentage of traffic that is shifted at the start of each increment of a
                    ``TimeBasedLinear`` deployment.

                  - **linearInterval** *(integer) --*

                    The number of minutes between each incremental traffic shift of a
                    ``TimeBasedLinear`` deployment.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_deployment_group(
        self, applicationName: str, deploymentGroupName: str
    ) -> ClientGetDeploymentGroupResponseTypeDef:
        """
        Gets information about a deployment group.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/codedeploy-2014-10-06/GetDeploymentGroup>`_

        **Request Syntax**
        ::

          response = client.get_deployment_group(
              applicationName='string',
              deploymentGroupName='string'
          )
        :type applicationName: string
        :param applicationName: **[REQUIRED]**

          The name of an AWS CodeDeploy application associated with the IAM user or AWS account.

        :type deploymentGroupName: string
        :param deploymentGroupName: **[REQUIRED]**

          The name of a deployment group for the specified application.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'deploymentGroupInfo': {
                    'applicationName': 'string',
                    'deploymentGroupId': 'string',
                    'deploymentGroupName': 'string',
                    'deploymentConfigName': 'string',
                    'ec2TagFilters': [
                        {
                            'Key': 'string',
                            'Value': 'string',
                            'Type': 'KEY_ONLY'|'VALUE_ONLY'|'KEY_AND_VALUE'
                        },
                    ],
                    'onPremisesInstanceTagFilters': [
                        {
                            'Key': 'string',
                            'Value': 'string',
                            'Type': 'KEY_ONLY'|'VALUE_ONLY'|'KEY_AND_VALUE'
                        },
                    ],
                    'autoScalingGroups': [
                        {
                            'name': 'string',
                            'hook': 'string'
                        },
                    ],
                    'serviceRoleArn': 'string',
                    'targetRevision': {
                        'revisionType': 'S3'|'GitHub'|'String'|'AppSpecContent',
                        's3Location': {
                            'bucket': 'string',
                            'key': 'string',
                            'bundleType': 'tar'|'tgz'|'zip'|'YAML'|'JSON',
                            'version': 'string',
                            'eTag': 'string'
                        },
                        'gitHubLocation': {
                            'repository': 'string',
                            'commitId': 'string'
                        },
                        'string': {
                            'content': 'string',
                            'sha256': 'string'
                        },
                        'appSpecContent': {
                            'content': 'string',
                            'sha256': 'string'
                        }
                    },
                    'triggerConfigurations': [
                        {
                            'triggerName': 'string',
                            'triggerTargetArn': 'string',
                            'triggerEvents': [
                                'DeploymentStart'|'DeploymentSuccess'|'DeploymentFailure'
                                |'DeploymentStop'|'DeploymentRollback'|'DeploymentReady'
                                |'InstanceStart'|'InstanceSuccess'|'InstanceFailure'
                                |'InstanceReady',
                            ]
                        },
                    ],
                    'alarmConfiguration': {
                        'enabled': True|False,
                        'ignorePollAlarmFailure': True|False,
                        'alarms': [
                            {
                                'name': 'string'
                            },
                        ]
                    },
                    'autoRollbackConfiguration': {
                        'enabled': True|False,
                        'events': [
                            'DEPLOYMENT_FAILURE'|'DEPLOYMENT_STOP_ON_ALARM'
                            |'DEPLOYMENT_STOP_ON_REQUEST',
                        ]
                    },
                    'deploymentStyle': {
                        'deploymentType': 'IN_PLACE'|'BLUE_GREEN',
                        'deploymentOption': 'WITH_TRAFFIC_CONTROL'|'WITHOUT_TRAFFIC_CONTROL'
                    },
                    'blueGreenDeploymentConfiguration': {
                        'terminateBlueInstancesOnDeploymentSuccess': {
                            'action': 'TERMINATE'|'KEEP_ALIVE',
                            'terminationWaitTimeInMinutes': 123
                        },
                        'deploymentReadyOption': {
                            'actionOnTimeout': 'CONTINUE_DEPLOYMENT'|'STOP_DEPLOYMENT',
                            'waitTimeInMinutes': 123
                        },
                        'greenFleetProvisioningOption': {
                            'action': 'DISCOVER_EXISTING'|'COPY_AUTO_SCALING_GROUP'
                        }
                    },
                    'loadBalancerInfo': {
                        'elbInfoList': [
                            {
                                'name': 'string'
                            },
                        ],
                        'targetGroupInfoList': [
                            {
                                'name': 'string'
                            },
                        ],
                        'targetGroupPairInfoList': [
                            {
                                'targetGroups': [
                                    {
                                        'name': 'string'
                                    },
                                ],
                                'prodTrafficRoute': {
                                    'listenerArns': [
                                        'string',
                                    ]
                                },
                                'testTrafficRoute': {
                                    'listenerArns': [
                                        'string',
                                    ]
                                }
                            },
                        ]
                    },
                    'lastSuccessfulDeployment': {
                        'deploymentId': 'string',
                        'status':
                        'Created'|'Queued'|'InProgress'|'Succeeded'|'Failed'
                        |'Stopped'|'Ready',
                        'endTime': datetime(2015, 1, 1),
                        'createTime': datetime(2015, 1, 1)
                    },
                    'lastAttemptedDeployment': {
                        'deploymentId': 'string',
                        'status':
                        'Created'|'Queued'|'InProgress'|'Succeeded'|'Failed'
                        |'Stopped'|'Ready',
                        'endTime': datetime(2015, 1, 1),
                        'createTime': datetime(2015, 1, 1)
                    },
                    'ec2TagSet': {
                        'ec2TagSetList': [
                            [
                                {
                                    'Key': 'string',
                                    'Value': 'string',
                                    'Type': 'KEY_ONLY'|'VALUE_ONLY'|'KEY_AND_VALUE'
                                },
                            ],
                        ]
                    },
                    'onPremisesTagSet': {
                        'onPremisesTagSetList': [
                            [
                                {
                                    'Key': 'string',
                                    'Value': 'string',
                                    'Type': 'KEY_ONLY'|'VALUE_ONLY'|'KEY_AND_VALUE'
                                },
                            ],
                        ]
                    },
                    'computePlatform': 'Server'|'Lambda'|'ECS',
                    'ecsServices': [
                        {
                            'serviceName': 'string',
                            'clusterName': 'string'
                        },
                    ]
                }
            }
          **Response Structure**

          - *(dict) --*

            Represents the output of a GetDeploymentGroup operation.

            - **deploymentGroupInfo** *(dict) --*

              Information about the deployment group.

              - **applicationName** *(string) --*

                The application name.

              - **deploymentGroupId** *(string) --*

                The deployment group ID.

              - **deploymentGroupName** *(string) --*

                The deployment group name.

              - **deploymentConfigName** *(string) --*

                The deployment configuration name.

              - **ec2TagFilters** *(list) --*

                The Amazon EC2 tags on which to filter. The deployment group includes EC2 instances
                with any of the specified tags.

                - *(dict) --*

                  Information about an EC2 tag filter.

                  - **Key** *(string) --*

                    The tag filter key.

                  - **Value** *(string) --*

                    The tag filter value.

                  - **Type** *(string) --*

                    The tag filter type:

                    * KEY_ONLY: Key only.

                    * VALUE_ONLY: Value only.

                    * KEY_AND_VALUE: Key and value.

              - **onPremisesInstanceTagFilters** *(list) --*

                The on-premises instance tags on which to filter. The deployment group includes
                on-premises instances with any of the specified tags.

                - *(dict) --*

                  Information about an on-premises instance tag filter.

                  - **Key** *(string) --*

                    The on-premises instance tag filter key.

                  - **Value** *(string) --*

                    The on-premises instance tag filter value.

                  - **Type** *(string) --*

                    The on-premises instance tag filter type:

                    * KEY_ONLY: Key only.

                    * VALUE_ONLY: Value only.

                    * KEY_AND_VALUE: Key and value.

              - **autoScalingGroups** *(list) --*

                A list of associated Auto Scaling groups.

                - *(dict) --*

                  Information about an Auto Scaling group.

                  - **name** *(string) --*

                    The Auto Scaling group name.

                  - **hook** *(string) --*

                    An Auto Scaling lifecycle event hook name.

              - **serviceRoleArn** *(string) --*

                A service role Amazon Resource Name (ARN) that grants CodeDeploy permission to make
                calls to AWS services on your behalf. For more information, see `Create a Service
                Role for AWS CodeDeploy
                <https://docs.aws.amazon.com/codedeploy/latest/userguide/getting-started-create-service-role.html>`__
                in the *AWS CodeDeploy User Guide* .

              - **targetRevision** *(dict) --*

                Information about the deployment group's target revision, including type and
                location.

                - **revisionType** *(string) --*

                  The type of application revision:

                  * S3: An application revision stored in Amazon S3.

                  * GitHub: An application revision stored in GitHub (EC2/On-premises deployments
                  only).

                  * String: A YAML-formatted or JSON-formatted string (AWS Lambda deployments only).

                - **s3Location** *(dict) --*

                  Information about the location of a revision stored in Amazon S3.

                  - **bucket** *(string) --*

                    The name of the Amazon S3 bucket where the application revision is stored.

                  - **key** *(string) --*

                    The name of the Amazon S3 object that represents the bundled artifacts for the
                    application revision.

                  - **bundleType** *(string) --*

                    The file type of the application revision. Must be one of the following:

                    * tar: A tar archive file.

                    * tgz: A compressed tar archive file.

                    * zip: A zip archive file.

                  - **version** *(string) --*

                    A specific version of the Amazon S3 object that represents the bundled artifacts
                    for the application revision.

                    If the version is not specified, the system uses the most recent version by
                    default.

                  - **eTag** *(string) --*

                    The ETag of the Amazon S3 object that represents the bundled artifacts for the
                    application revision.

                    If the ETag is not specified as an input parameter, ETag validation of the
                    object is skipped.

                - **gitHubLocation** *(dict) --*

                  Information about the location of application artifacts stored in GitHub.

                  - **repository** *(string) --*

                    The GitHub account and repository pair that stores a reference to the commit
                    that represents the bundled artifacts for the application revision.

                    Specified as account/repository.

                  - **commitId** *(string) --*

                    The SHA1 commit ID of the GitHub commit that represents the bundled artifacts
                    for the application revision.

                - **string** *(dict) --*

                  Information about the location of an AWS Lambda deployment revision stored as a
                  RawString.

                  - **content** *(string) --*

                    The YAML-formatted or JSON-formatted revision string. It includes information
                    about which Lambda function to update and optional Lambda functions that
                    validate deployment lifecycle events.

                  - **sha256** *(string) --*

                    The SHA256 hash value of the revision content.

                - **appSpecContent** *(dict) --*

                  The content of an AppSpec file for an AWS Lambda or Amazon ECS deployment. The
                  content is formatted as JSON or YAML and stored as a RawString.

                  - **content** *(string) --*

                    The YAML-formatted or JSON-formatted revision string.

                    For an AWS Lambda deployment, the content includes a Lambda function name, the
                    alias for its original version, and the alias for its replacement version. The
                    deployment shifts traffic from the original version of the Lambda function to
                    the replacement version.

                    For an Amazon ECS deployment, the content includes the task name, information
                    about the load balancer that serves traffic to the container, and more.

                    For both types of deployments, the content can specify Lambda functions that run
                    at specified hooks, such as ``BeforeInstall`` , during a deployment.

                  - **sha256** *(string) --*

                    The SHA256 hash value of the revision content.

              - **triggerConfigurations** *(list) --*

                Information about triggers associated with the deployment group.

                - *(dict) --*

                  Information about notification triggers for the deployment group.

                  - **triggerName** *(string) --*

                    The name of the notification trigger.

                  - **triggerTargetArn** *(string) --*

                    The ARN of the Amazon Simple Notification Service topic through which
                    notifications about deployment or instance events are sent.

                  - **triggerEvents** *(list) --*

                    The event type or types for which notifications are triggered.

                    - *(string) --*

              - **alarmConfiguration** *(dict) --*

                A list of alarms associated with the deployment group.

                - **enabled** *(boolean) --*

                  Indicates whether the alarm configuration is enabled.

                - **ignorePollAlarmFailure** *(boolean) --*

                  Indicates whether a deployment should continue if information about the current
                  state of alarms cannot be retrieved from Amazon CloudWatch. The default value is
                  false.

                  * true: The deployment proceeds even if alarm status information can't be
                  retrieved from Amazon CloudWatch.

                  * false: The deployment stops if alarm status information can't be retrieved from
                  Amazon CloudWatch.

                - **alarms** *(list) --*

                  A list of alarms configured for the deployment group. A maximum of 10 alarms can
                  be added to a deployment group.

                  - *(dict) --*

                    Information about an alarm.

                    - **name** *(string) --*

                      The name of the alarm. Maximum length is 255 characters. Each alarm name can
                      be used only once in a list of alarms.

              - **autoRollbackConfiguration** *(dict) --*

                Information about the automatic rollback configuration associated with the
                deployment group.

                - **enabled** *(boolean) --*

                  Indicates whether a defined automatic rollback configuration is currently enabled.

                - **events** *(list) --*

                  The event type or types that trigger a rollback.

                  - *(string) --*

              - **deploymentStyle** *(dict) --*

                Information about the type of deployment, either in-place or blue/green, you want to
                run and whether to route deployment traffic behind a load balancer.

                - **deploymentType** *(string) --*

                  Indicates whether to run an in-place deployment or a blue/green deployment.

                - **deploymentOption** *(string) --*

                  Indicates whether to route deployment traffic behind a load balancer.

              - **blueGreenDeploymentConfiguration** *(dict) --*

                Information about blue/green deployment options for a deployment group.

                - **terminateBlueInstancesOnDeploymentSuccess** *(dict) --*

                  Information about whether to terminate instances in the original fleet during a
                  blue/green deployment.

                  - **action** *(string) --*

                    The action to take on instances in the original environment after a successful
                    blue/green deployment.

                    * TERMINATE: Instances are terminated after a specified wait time.

                    * KEEP_ALIVE: Instances are left running after they are deregistered from the
                    load balancer and removed from the deployment group.

                  - **terminationWaitTimeInMinutes** *(integer) --*

                    For an Amazon EC2 deployment, the number of minutes to wait after a successful
                    blue/green deployment before terminating instances from the original
                    environment.

                    For an Amazon ECS deployment, the number of minutes before deleting the original
                    (blue) task set. During an Amazon ECS deployment, CodeDeploy shifts traffic from
                    the original (blue) task set to a replacement (green) task set.

                    The maximum setting is 2880 minutes (2 days).

                - **deploymentReadyOption** *(dict) --*

                  Information about the action to take when newly provisioned instances are ready to
                  receive traffic in a blue/green deployment.

                  - **actionOnTimeout** *(string) --*

                    Information about when to reroute traffic from an original environment to a
                    replacement environment in a blue/green deployment.

                    * CONTINUE_DEPLOYMENT: Register new instances with the load balancer immediately
                    after the new application revision is installed on the instances in the
                    replacement environment.

                    * STOP_DEPLOYMENT: Do not register new instances with a load balancer unless
                    traffic rerouting is started using  ContinueDeployment . If traffic rerouting is
                    not started before the end of the specified wait period, the deployment status
                    is changed to Stopped.

                  - **waitTimeInMinutes** *(integer) --*

                    The number of minutes to wait before the status of a blue/green deployment is
                    changed to Stopped if rerouting is not started manually. Applies only to the
                    STOP_DEPLOYMENT option for actionOnTimeout

                - **greenFleetProvisioningOption** *(dict) --*

                  Information about how instances are provisioned for a replacement environment in a
                  blue/green deployment.

                  - **action** *(string) --*

                    The method used to add instances to a replacement environment.

                    * DISCOVER_EXISTING: Use instances that already exist or will be created
                    manually.

                    * COPY_AUTO_SCALING_GROUP: Use settings from a specified Auto Scaling group to
                    define and create instances in a new Auto Scaling group.

              - **loadBalancerInfo** *(dict) --*

                Information about the load balancer to use in a deployment.

                - **elbInfoList** *(list) --*

                  An array that contains information about the load balancer to use for load
                  balancing in a deployment. In Elastic Load Balancing, load balancers are used with
                  Classic Load Balancers.

                  .. note::

                    Adding more than one load balancer to the array is not supported.

                  - *(dict) --*

                    Information about a load balancer in Elastic Load Balancing to use in a
                    deployment. Instances are registered directly with a load balancer, and traffic
                    is routed to the load balancer.

                    - **name** *(string) --*

                      For blue/green deployments, the name of the load balancer that is used to
                      route traffic from original instances to replacement instances in a blue/green
                      deployment. For in-place deployments, the name of the load balancer that
                      instances are deregistered from so they are not serving traffic during a
                      deployment, and then re-registered with after the deployment is complete.

                - **targetGroupInfoList** *(list) --*

                  An array that contains information about the target group to use for load
                  balancing in a deployment. In Elastic Load Balancing, target groups are used with
                  Application Load Balancers.

                  .. note::

                    Adding more than one target group to the array is not supported.

                  - *(dict) --*

                    Information about a target group in Elastic Load Balancing to use in a
                    deployment. Instances are registered as targets in a target group, and traffic
                    is routed to the target group.

                    - **name** *(string) --*

                      For blue/green deployments, the name of the target group that instances in the
                      original environment are deregistered from, and instances in the replacement
                      environment are registered with. For in-place deployments, the name of the
                      target group that instances are deregistered from, so they are not serving
                      traffic during a deployment, and then re-registered with after the deployment
                      is complete.

                - **targetGroupPairInfoList** *(list) --*

                  The target group pair information. This is an array of ``TargeGroupPairInfo``
                  objects with a maximum size of one.

                  - *(dict) --*

                    Information about two target groups and how traffic is routed during an Amazon
                    ECS deployment. An optional test traffic route can be specified.

                    - **targetGroups** *(list) --*

                      One pair of target groups. One is associated with the original task set. The
                      second is associated with the task set that serves traffic after the
                      deployment is complete.

                      - *(dict) --*

                        Information about a target group in Elastic Load Balancing to use in a
                        deployment. Instances are registered as targets in a target group, and
                        traffic is routed to the target group.

                        - **name** *(string) --*

                          For blue/green deployments, the name of the target group that instances in
                          the original environment are deregistered from, and instances in the
                          replacement environment are registered with. For in-place deployments, the
                          name of the target group that instances are deregistered from, so they are
                          not serving traffic during a deployment, and then re-registered with after
                          the deployment is complete.

                    - **prodTrafficRoute** *(dict) --*

                      The path used by a load balancer to route production traffic when an Amazon
                      ECS deployment is complete.

                      - **listenerArns** *(list) --*

                        The ARN of one listener. The listener identifies the route between a target
                        group and a load balancer. This is an array of strings with a maximum size
                        of one.

                        - *(string) --*

                    - **testTrafficRoute** *(dict) --*

                      An optional path used by a load balancer to route test traffic after an Amazon
                      ECS deployment. Validation can occur while test traffic is served during a
                      deployment.

                      - **listenerArns** *(list) --*

                        The ARN of one listener. The listener identifies the route between a target
                        group and a load balancer. This is an array of strings with a maximum size
                        of one.

                        - *(string) --*

              - **lastSuccessfulDeployment** *(dict) --*

                Information about the most recent successful deployment to the deployment group.

                - **deploymentId** *(string) --*

                  The unique ID of a deployment.

                - **status** *(string) --*

                  The status of the most recent deployment.

                - **endTime** *(datetime) --*

                  A timestamp that indicates when the most recent deployment to the deployment group
                  was complete.

                - **createTime** *(datetime) --*

                  A timestamp that indicates when the most recent deployment to the deployment group
                  started.

              - **lastAttemptedDeployment** *(dict) --*

                Information about the most recent attempted deployment to the deployment group.

                - **deploymentId** *(string) --*

                  The unique ID of a deployment.

                - **status** *(string) --*

                  The status of the most recent deployment.

                - **endTime** *(datetime) --*

                  A timestamp that indicates when the most recent deployment to the deployment group
                  was complete.

                - **createTime** *(datetime) --*

                  A timestamp that indicates when the most recent deployment to the deployment group
                  started.

              - **ec2TagSet** *(dict) --*

                Information about groups of tags applied to an EC2 instance. The deployment group
                includes only EC2 instances identified by all of the tag groups. Cannot be used in
                the same call as ec2TagFilters.

                - **ec2TagSetList** *(list) --*

                  A list that contains other lists of EC2 instance tag groups. For an instance to be
                  included in the deployment group, it must be identified by all of the tag groups
                  in the list.

                  - *(list) --*

                    - *(dict) --*

                      Information about an EC2 tag filter.

                      - **Key** *(string) --*

                        The tag filter key.

                      - **Value** *(string) --*

                        The tag filter value.

                      - **Type** *(string) --*

                        The tag filter type:

                        * KEY_ONLY: Key only.

                        * VALUE_ONLY: Value only.

                        * KEY_AND_VALUE: Key and value.

              - **onPremisesTagSet** *(dict) --*

                Information about groups of tags applied to an on-premises instance. The deployment
                group includes only on-premises instances identified by all the tag groups. Cannot
                be used in the same call as onPremisesInstanceTagFilters.

                - **onPremisesTagSetList** *(list) --*

                  A list that contains other lists of on-premises instance tag groups. For an
                  instance to be included in the deployment group, it must be identified by all of
                  the tag groups in the list.

                  - *(list) --*

                    - *(dict) --*

                      Information about an on-premises instance tag filter.

                      - **Key** *(string) --*

                        The on-premises instance tag filter key.

                      - **Value** *(string) --*

                        The on-premises instance tag filter value.

                      - **Type** *(string) --*

                        The on-premises instance tag filter type:

                        * KEY_ONLY: Key only.

                        * VALUE_ONLY: Value only.

                        * KEY_AND_VALUE: Key and value.

              - **computePlatform** *(string) --*

                The destination platform type for the deployment (``Lambda`` , ``Server`` , or
                ``ECS`` ).

              - **ecsServices** *(list) --*

                The target Amazon ECS services in the deployment group. This applies only to
                deployment groups that use the Amazon ECS compute platform. A target Amazon ECS
                service is specified as an Amazon ECS cluster and service name pair using the format
                ``<clustername>:<servicename>`` .

                - *(dict) --*

                  Contains the service and cluster names used to identify an Amazon ECS deployment's
                  target.

                  - **serviceName** *(string) --*

                    The name of the target Amazon ECS service.

                  - **clusterName** *(string) --*

                    The name of the cluster that the Amazon ECS service is associated with.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_deployment_instance(
        self, deploymentId: str, instanceId: str
    ) -> ClientGetDeploymentInstanceResponseTypeDef:
        """
        Gets information about an instance as part of a deployment.

        .. danger::

            This operation is deprecated and may not function as expected. This operation should not
            be used going forward and is only kept for the purpose of backwards compatiblity.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/codedeploy-2014-10-06/GetDeploymentInstance>`_

        **Request Syntax**
        ::

          response = client.get_deployment_instance(
              deploymentId='string',
              instanceId='string'
          )
        :type deploymentId: string
        :param deploymentId: **[REQUIRED]**

          The unique ID of a deployment.

        :type instanceId: string
        :param instanceId: **[REQUIRED]**

          The unique ID of an instance in the deployment group.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'instanceSummary': {
                    'deploymentId': 'string',
                    'instanceId': 'string',
                    'status':
                    'Pending'|'InProgress'|'Succeeded'|'Failed'|'Skipped'|'Unknown'
                    |'Ready',
                    'lastUpdatedAt': datetime(2015, 1, 1),
                    'lifecycleEvents': [
                        {
                            'lifecycleEventName': 'string',
                            'diagnostics': {
                                'errorCode':
                                'Success'|'ScriptMissing'
                                |'ScriptNotExecutable'|'ScriptTimedOut'
                                |'ScriptFailed'|'UnknownError',
                                'scriptName': 'string',
                                'message': 'string',
                                'logTail': 'string'
                            },
                            'startTime': datetime(2015, 1, 1),
                            'endTime': datetime(2015, 1, 1),
                            'status':
                            'Pending'|'InProgress'|'Succeeded'|'Failed'
                            |'Skipped'|'Unknown'
                        },
                    ],
                    'instanceType': 'Blue'|'Green'
                }
            }
          **Response Structure**

          - *(dict) --*

            Represents the output of a GetDeploymentInstance operation.

            - **instanceSummary** *(dict) --*

              Information about the instance.

              - **deploymentId** *(string) --*

                The unique ID of a deployment.

              - **instanceId** *(string) --*

                The instance ID.

              - **status** *(string) --*

                The deployment status for this instance:

                * Pending: The deployment is pending for this instance.

                * In Progress: The deployment is in progress for this instance.

                * Succeeded: The deployment has succeeded for this instance.

                * Failed: The deployment has failed for this instance.

                * Skipped: The deployment has been skipped for this instance.

                * Unknown: The deployment status is unknown for this instance.

              - **lastUpdatedAt** *(datetime) --*

                A timestamp that indicaties when the instance information was last updated.

              - **lifecycleEvents** *(list) --*

                A list of lifecycle events for this instance.

                - *(dict) --*

                  Information about a deployment lifecycle event.

                  - **lifecycleEventName** *(string) --*

                    The deployment lifecycle event name, such as ApplicationStop, BeforeInstall,
                    AfterInstall, ApplicationStart, or ValidateService.

                  - **diagnostics** *(dict) --*

                    Diagnostic information about the deployment lifecycle event.

                    - **errorCode** *(string) --*

                      The associated error code:

                      * Success: The specified script ran.

                      * ScriptMissing: The specified script was not found in the specified location.

                      * ScriptNotExecutable: The specified script is not a recognized executable
                      file type.

                      * ScriptTimedOut: The specified script did not finish running in the specified
                      time period.

                      * ScriptFailed: The specified script failed to run as expected.

                      * UnknownError: The specified script did not run for an unknown reason.

                    - **scriptName** *(string) --*

                      The name of the script.

                    - **message** *(string) --*

                      The message associated with the error.

                    - **logTail** *(string) --*

                      The last portion of the diagnostic log.

                      If available, AWS CodeDeploy returns up to the last 4 KB of the diagnostic
                      log.

                  - **startTime** *(datetime) --*

                    A timestamp that indicates when the deployment lifecycle event started.

                  - **endTime** *(datetime) --*

                    A timestamp that indicates when the deployment lifecycle event ended.

                  - **status** *(string) --*

                    The deployment lifecycle event status:

                    * Pending: The deployment lifecycle event is pending.

                    * InProgress: The deployment lifecycle event is in progress.

                    * Succeeded: The deployment lifecycle event ran successfully.

                    * Failed: The deployment lifecycle event has failed.

                    * Skipped: The deployment lifecycle event has been skipped.

                    * Unknown: The deployment lifecycle event is unknown.

              - **instanceType** *(string) --*

                Information about which environment an instance belongs to in a blue/green
                deployment.

                * BLUE: The instance is part of the original environment.

                * GREEN: The instance is part of the replacement environment.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_deployment_target(
        self, deploymentId: str = None, targetId: str = None
    ) -> ClientGetDeploymentTargetResponseTypeDef:
        """
        Returns information about a deployment target.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/codedeploy-2014-10-06/GetDeploymentTarget>`_

        **Request Syntax**
        ::

          response = client.get_deployment_target(
              deploymentId='string',
              targetId='string'
          )
        :type deploymentId: string
        :param deploymentId:

          The unique ID of a deployment.

        :type targetId: string
        :param targetId:

          The unique ID of a deployment target.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'deploymentTarget': {
                    'deploymentTargetType': 'InstanceTarget'|'LambdaTarget'|'ECSTarget',
                    'instanceTarget': {
                        'deploymentId': 'string',
                        'targetId': 'string',
                        'targetArn': 'string',
                        'status':
                        'Pending'|'InProgress'|'Succeeded'|'Failed'|'Skipped'
                        |'Unknown'|'Ready',
                        'lastUpdatedAt': datetime(2015, 1, 1),
                        'lifecycleEvents': [
                            {
                                'lifecycleEventName': 'string',
                                'diagnostics': {
                                    'errorCode':
                                    'Success'|'ScriptMissing'
                                    |'ScriptNotExecutable'
                                    |'ScriptTimedOut'|'ScriptFailed'
                                    |'UnknownError',
                                    'scriptName': 'string',
                                    'message': 'string',
                                    'logTail': 'string'
                                },
                                'startTime': datetime(2015, 1, 1),
                                'endTime': datetime(2015, 1, 1),
                                'status':
                                'Pending'|'InProgress'|'Succeeded'|'Failed'
                                |'Skipped'|'Unknown'
                            },
                        ],
                        'instanceLabel': 'Blue'|'Green'
                    },
                    'lambdaTarget': {
                        'deploymentId': 'string',
                        'targetId': 'string',
                        'targetArn': 'string',
                        'status':
                        'Pending'|'InProgress'|'Succeeded'|'Failed'|'Skipped'
                        |'Unknown'|'Ready',
                        'lastUpdatedAt': datetime(2015, 1, 1),
                        'lifecycleEvents': [
                            {
                                'lifecycleEventName': 'string',
                                'diagnostics': {
                                    'errorCode':
                                    'Success'|'ScriptMissing'
                                    |'ScriptNotExecutable'
                                    |'ScriptTimedOut'|'ScriptFailed'
                                    |'UnknownError',
                                    'scriptName': 'string',
                                    'message': 'string',
                                    'logTail': 'string'
                                },
                                'startTime': datetime(2015, 1, 1),
                                'endTime': datetime(2015, 1, 1),
                                'status':
                                'Pending'|'InProgress'|'Succeeded'|'Failed'
                                |'Skipped'|'Unknown'
                            },
                        ],
                        'lambdaFunctionInfo': {
                            'functionName': 'string',
                            'functionAlias': 'string',
                            'currentVersion': 'string',
                            'targetVersion': 'string',
                            'targetVersionWeight': 123.0
                        }
                    },
                    'ecsTarget': {
                        'deploymentId': 'string',
                        'targetId': 'string',
                        'targetArn': 'string',
                        'lastUpdatedAt': datetime(2015, 1, 1),
                        'lifecycleEvents': [
                            {
                                'lifecycleEventName': 'string',
                                'diagnostics': {
                                    'errorCode':
                                    'Success'|'ScriptMissing'
                                    |'ScriptNotExecutable'
                                    |'ScriptTimedOut'|'ScriptFailed'
                                    |'UnknownError',
                                    'scriptName': 'string',
                                    'message': 'string',
                                    'logTail': 'string'
                                },
                                'startTime': datetime(2015, 1, 1),
                                'endTime': datetime(2015, 1, 1),
                                'status':
                                'Pending'|'InProgress'|'Succeeded'|'Failed'
                                |'Skipped'|'Unknown'
                            },
                        ],
                        'status':
                        'Pending'|'InProgress'|'Succeeded'|'Failed'|'Skipped'
                        |'Unknown'|'Ready',
                        'taskSetsInfo': [
                            {
                                'identifer': 'string',
                                'desiredCount': 123,
                                'pendingCount': 123,
                                'runningCount': 123,
                                'status': 'string',
                                'trafficWeight': 123.0,
                                'targetGroup': {
                                    'name': 'string'
                                },
                                'taskSetLabel': 'Blue'|'Green'
                            },
                        ]
                    }
                }
            }
          **Response Structure**

          - *(dict) --*

            - **deploymentTarget** *(dict) --*

              A deployment target that contains information about a deployment such as its status,
              lifecyle events, and when it was last updated. It also contains metadata about the
              deployment target. The deployment target metadata depends on the deployment target's
              type (``instanceTarget`` , ``lambdaTarget`` , or ``ecsTarget`` ).

              - **deploymentTargetType** *(string) --*

                The deployment type that is specific to the deployment's compute platform.

              - **instanceTarget** *(dict) --*

                Information about the target for a deployment that uses the EC2/On-premises compute
                platform.

                - **deploymentId** *(string) --*

                  The unique ID of a deployment.

                - **targetId** *(string) --*

                  The unique ID of a deployment target that has a type of ``instanceTarget`` .

                - **targetArn** *(string) --*

                  The ARN of the target.

                - **status** *(string) --*

                  The status an EC2/On-premises deployment's target instance.

                - **lastUpdatedAt** *(datetime) --*

                  The date and time when the target instance was updated by a deployment.

                - **lifecycleEvents** *(list) --*

                  The lifecycle events of the deployment to this target instance.

                  - *(dict) --*

                    Information about a deployment lifecycle event.

                    - **lifecycleEventName** *(string) --*

                      The deployment lifecycle event name, such as ApplicationStop, BeforeInstall,
                      AfterInstall, ApplicationStart, or ValidateService.

                    - **diagnostics** *(dict) --*

                      Diagnostic information about the deployment lifecycle event.

                      - **errorCode** *(string) --*

                        The associated error code:

                        * Success: The specified script ran.

                        * ScriptMissing: The specified script was not found in the specified
                        location.

                        * ScriptNotExecutable: The specified script is not a recognized executable
                        file type.

                        * ScriptTimedOut: The specified script did not finish running in the
                        specified time period.

                        * ScriptFailed: The specified script failed to run as expected.

                        * UnknownError: The specified script did not run for an unknown reason.

                      - **scriptName** *(string) --*

                        The name of the script.

                      - **message** *(string) --*

                        The message associated with the error.

                      - **logTail** *(string) --*

                        The last portion of the diagnostic log.

                        If available, AWS CodeDeploy returns up to the last 4 KB of the diagnostic
                        log.

                    - **startTime** *(datetime) --*

                      A timestamp that indicates when the deployment lifecycle event started.

                    - **endTime** *(datetime) --*

                      A timestamp that indicates when the deployment lifecycle event ended.

                    - **status** *(string) --*

                      The deployment lifecycle event status:

                      * Pending: The deployment lifecycle event is pending.

                      * InProgress: The deployment lifecycle event is in progress.

                      * Succeeded: The deployment lifecycle event ran successfully.

                      * Failed: The deployment lifecycle event has failed.

                      * Skipped: The deployment lifecycle event has been skipped.

                      * Unknown: The deployment lifecycle event is unknown.

                - **instanceLabel** *(string) --*

                  A label that identifies whether the instance is an original target (``BLUE`` ) or
                  a replacement target (``GREEN`` ).

              - **lambdaTarget** *(dict) --*

                Information about the target for a deployment that uses the AWS Lambda compute
                platform.

                - **deploymentId** *(string) --*

                  The unique ID of a deployment.

                - **targetId** *(string) --*

                  The unique ID of a deployment target that has a type of ``lambdaTarget`` .

                - **targetArn** *(string) --*

                  The ARN of the target.

                - **status** *(string) --*

                  The status an AWS Lambda deployment's target Lambda function.

                - **lastUpdatedAt** *(datetime) --*

                  The date and time when the target Lambda function was updated by a deployment.

                - **lifecycleEvents** *(list) --*

                  The lifecycle events of the deployment to this target Lambda function.

                  - *(dict) --*

                    Information about a deployment lifecycle event.

                    - **lifecycleEventName** *(string) --*

                      The deployment lifecycle event name, such as ApplicationStop, BeforeInstall,
                      AfterInstall, ApplicationStart, or ValidateService.

                    - **diagnostics** *(dict) --*

                      Diagnostic information about the deployment lifecycle event.

                      - **errorCode** *(string) --*

                        The associated error code:

                        * Success: The specified script ran.

                        * ScriptMissing: The specified script was not found in the specified
                        location.

                        * ScriptNotExecutable: The specified script is not a recognized executable
                        file type.

                        * ScriptTimedOut: The specified script did not finish running in the
                        specified time period.

                        * ScriptFailed: The specified script failed to run as expected.

                        * UnknownError: The specified script did not run for an unknown reason.

                      - **scriptName** *(string) --*

                        The name of the script.

                      - **message** *(string) --*

                        The message associated with the error.

                      - **logTail** *(string) --*

                        The last portion of the diagnostic log.

                        If available, AWS CodeDeploy returns up to the last 4 KB of the diagnostic
                        log.

                    - **startTime** *(datetime) --*

                      A timestamp that indicates when the deployment lifecycle event started.

                    - **endTime** *(datetime) --*

                      A timestamp that indicates when the deployment lifecycle event ended.

                    - **status** *(string) --*

                      The deployment lifecycle event status:

                      * Pending: The deployment lifecycle event is pending.

                      * InProgress: The deployment lifecycle event is in progress.

                      * Succeeded: The deployment lifecycle event ran successfully.

                      * Failed: The deployment lifecycle event has failed.

                      * Skipped: The deployment lifecycle event has been skipped.

                      * Unknown: The deployment lifecycle event is unknown.

                - **lambdaFunctionInfo** *(dict) --*

                  A ``LambdaFunctionInfo`` object that describes a target Lambda function.

                  - **functionName** *(string) --*

                    The name of a Lambda function.

                  - **functionAlias** *(string) --*

                    The alias of a Lambda function. For more information, see `Introduction to AWS
                    Lambda Aliases
                    <https://docs.aws.amazon.com/lambda/latest/dg/aliases-intro.html>`__ .

                  - **currentVersion** *(string) --*

                    The version of a Lambda function that production traffic points to.

                  - **targetVersion** *(string) --*

                    The version of a Lambda function that production traffic points to after the
                    Lambda function is deployed.

                  - **targetVersionWeight** *(float) --*

                    The percentage of production traffic that the target version of a Lambda
                    function receives.

              - **ecsTarget** *(dict) --*

                Information about the target for a deployment that uses the Amazon ECS compute
                platform.

                - **deploymentId** *(string) --*

                  The unique ID of a deployment.

                - **targetId** *(string) --*

                  The unique ID of a deployment target that has a type of ``ecsTarget`` .

                - **targetArn** *(string) --*

                  The ARN of the target.

                - **lastUpdatedAt** *(datetime) --*

                  The date and time when the target Amazon ECS application was updated by a
                  deployment.

                - **lifecycleEvents** *(list) --*

                  The lifecycle events of the deployment to this target Amazon ECS application.

                  - *(dict) --*

                    Information about a deployment lifecycle event.

                    - **lifecycleEventName** *(string) --*

                      The deployment lifecycle event name, such as ApplicationStop, BeforeInstall,
                      AfterInstall, ApplicationStart, or ValidateService.

                    - **diagnostics** *(dict) --*

                      Diagnostic information about the deployment lifecycle event.

                      - **errorCode** *(string) --*

                        The associated error code:

                        * Success: The specified script ran.

                        * ScriptMissing: The specified script was not found in the specified
                        location.

                        * ScriptNotExecutable: The specified script is not a recognized executable
                        file type.

                        * ScriptTimedOut: The specified script did not finish running in the
                        specified time period.

                        * ScriptFailed: The specified script failed to run as expected.

                        * UnknownError: The specified script did not run for an unknown reason.

                      - **scriptName** *(string) --*

                        The name of the script.

                      - **message** *(string) --*

                        The message associated with the error.

                      - **logTail** *(string) --*

                        The last portion of the diagnostic log.

                        If available, AWS CodeDeploy returns up to the last 4 KB of the diagnostic
                        log.

                    - **startTime** *(datetime) --*

                      A timestamp that indicates when the deployment lifecycle event started.

                    - **endTime** *(datetime) --*

                      A timestamp that indicates when the deployment lifecycle event ended.

                    - **status** *(string) --*

                      The deployment lifecycle event status:

                      * Pending: The deployment lifecycle event is pending.

                      * InProgress: The deployment lifecycle event is in progress.

                      * Succeeded: The deployment lifecycle event ran successfully.

                      * Failed: The deployment lifecycle event has failed.

                      * Skipped: The deployment lifecycle event has been skipped.

                      * Unknown: The deployment lifecycle event is unknown.

                - **status** *(string) --*

                  The status an Amazon ECS deployment's target ECS application.

                - **taskSetsInfo** *(list) --*

                  The ``ECSTaskSet`` objects associated with the ECS target.

                  - *(dict) --*

                    Information about a set of Amazon ECS tasks in an AWS CodeDeploy deployment. An
                    Amazon ECS task set includes details such as the desired number of tasks, how
                    many tasks are running, and whether the task set serves production traffic. An
                    AWS CodeDeploy application that uses the Amazon ECS compute platform deploys a
                    containerized application in an Amazon ECS service as a task set.

                    - **identifer** *(string) --*

                      A unique ID of an ``ECSTaskSet`` .

                    - **desiredCount** *(integer) --*

                      The number of tasks in a task set. During a deployment that uses the Amazon
                      ECS compute type, CodeDeploy instructs Amazon ECS to create a new task set and
                      uses this value to determine how many tasks to create. After the updated task
                      set is created, CodeDeploy shifts traffic to the new task set.

                    - **pendingCount** *(integer) --*

                      The number of tasks in the task set that are in the ``PENDING`` status during
                      an Amazon ECS deployment. A task in the ``PENDING`` state is preparing to
                      enter the ``RUNNING`` state. A task set enters the ``PENDING`` status when it
                      launches for the first time, or when it is restarted after being in the
                      ``STOPPED`` state.

                    - **runningCount** *(integer) --*

                      The number of tasks in the task set that are in the ``RUNNING`` status during
                      an Amazon ECS deployment. A task in the ``RUNNING`` state is running and ready
                      for use.

                    - **status** *(string) --*

                      The status of the task set. There are three valid task set statuses:

                      * ``PRIMARY`` : Indicates the task set is serving production traffic.

                      * ``ACTIVE`` : Indicates the task set is not serving production traffic.

                      * ``DRAINING`` : Indicates the tasks in the task set are being stopped and
                      their corresponding targets are being deregistered from their target group.

                    - **trafficWeight** *(float) --*

                      The percentage of traffic served by this task set.

                    - **targetGroup** *(dict) --*

                      The target group associated with the task set. The target group is used by AWS
                      CodeDeploy to manage traffic to a task set.

                      - **name** *(string) --*

                        For blue/green deployments, the name of the target group that instances in
                        the original environment are deregistered from, and instances in the
                        replacement environment are registered with. For in-place deployments, the
                        name of the target group that instances are deregistered from, so they are
                        not serving traffic during a deployment, and then re-registered with after
                        the deployment is complete.

                    - **taskSetLabel** *(string) --*

                      A label that identifies whether the ECS task set is an original target
                      (``BLUE`` ) or a replacement target (``GREEN`` ).
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_on_premises_instance(
        self, instanceName: str
    ) -> ClientGetOnPremisesInstanceResponseTypeDef:
        """
        Gets information about an on-premises instance.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/codedeploy-2014-10-06/GetOnPremisesInstance>`_

        **Request Syntax**
        ::

          response = client.get_on_premises_instance(
              instanceName='string'
          )
        :type instanceName: string
        :param instanceName: **[REQUIRED]**

          The name of the on-premises instance about which to get information.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'instanceInfo': {
                    'instanceName': 'string',
                    'iamSessionArn': 'string',
                    'iamUserArn': 'string',
                    'instanceArn': 'string',
                    'registerTime': datetime(2015, 1, 1),
                    'deregisterTime': datetime(2015, 1, 1),
                    'tags': [
                        {
                            'Key': 'string',
                            'Value': 'string'
                        },
                    ]
                }
            }
          **Response Structure**

          - *(dict) --*

            Represents the output of a GetOnPremisesInstance operation.

            - **instanceInfo** *(dict) --*

              Information about the on-premises instance.

              - **instanceName** *(string) --*

                The name of the on-premises instance.

              - **iamSessionArn** *(string) --*

                The ARN of the IAM session associated with the on-premises instance.

              - **iamUserArn** *(string) --*

                The IAM user ARN associated with the on-premises instance.

              - **instanceArn** *(string) --*

                The ARN of the on-premises instance.

              - **registerTime** *(datetime) --*

                The time at which the on-premises instance was registered.

              - **deregisterTime** *(datetime) --*

                If the on-premises instance was deregistered, the time at which the on-premises
                instance was deregistered.

              - **tags** *(list) --*

                The tags currently associated with the on-premises instance.

                - *(dict) --*

                  Information about a tag.

                  - **Key** *(string) --*

                    The tag's key.

                  - **Value** *(string) --*

                    The tag's value.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_application_revisions(
        self,
        applicationName: str,
        sortBy: Literal["registerTime", "firstUsedTime", "lastUsedTime"] = None,
        sortOrder: Literal["ascending", "descending"] = None,
        s3Bucket: str = None,
        s3KeyPrefix: str = None,
        deployed: Literal["include", "exclude", "ignore"] = None,
        nextToken: str = None,
    ) -> ClientListApplicationRevisionsResponseTypeDef:
        """
        Lists information about revisions for an application.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/codedeploy-2014-10-06/ListApplicationRevisions>`_

        **Request Syntax**
        ::

          response = client.list_application_revisions(
              applicationName='string',
              sortBy='registerTime'|'firstUsedTime'|'lastUsedTime',
              sortOrder='ascending'|'descending',
              s3Bucket='string',
              s3KeyPrefix='string',
              deployed='include'|'exclude'|'ignore',
              nextToken='string'
          )
        :type applicationName: string
        :param applicationName: **[REQUIRED]**

          The name of an AWS CodeDeploy application associated with the IAM user or AWS account.

        :type sortBy: string
        :param sortBy:

          The column name to use to sort the list results:

          * registerTime: Sort by the time the revisions were registered with AWS CodeDeploy.

          * firstUsedTime: Sort by the time the revisions were first used in a deployment.

          * lastUsedTime: Sort by the time the revisions were last used in a deployment.

          If not specified or set to null, the results are returned in an arbitrary order.

        :type sortOrder: string
        :param sortOrder:

          The order in which to sort the list results:

          * ascending: ascending order.

          * descending: descending order.

          If not specified, the results are sorted in ascending order.

          If set to null, the results are sorted in an arbitrary order.

        :type s3Bucket: string
        :param s3Bucket:

          An Amazon S3 bucket name to limit the search for revisions.

          If set to null, all of the user's buckets are searched.

        :type s3KeyPrefix: string
        :param s3KeyPrefix:

          A key prefix for the set of Amazon S3 objects to limit the search for revisions.

        :type deployed: string
        :param deployed:

          Whether to list revisions based on whether the revision is the target revision of an
          deployment group:

          * include: List revisions that are target revisions of a deployment group.

          * exclude: Do not list revisions that are target revisions of a deployment group.

          * ignore: List all revisions.

        :type nextToken: string
        :param nextToken:

          An identifier returned from the previous ``ListApplicationRevisions`` call. It can be used
          to return the next set of applications in the list.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'revisions': [
                    {
                        'revisionType': 'S3'|'GitHub'|'String'|'AppSpecContent',
                        's3Location': {
                            'bucket': 'string',
                            'key': 'string',
                            'bundleType': 'tar'|'tgz'|'zip'|'YAML'|'JSON',
                            'version': 'string',
                            'eTag': 'string'
                        },
                        'gitHubLocation': {
                            'repository': 'string',
                            'commitId': 'string'
                        },
                        'string': {
                            'content': 'string',
                            'sha256': 'string'
                        },
                        'appSpecContent': {
                            'content': 'string',
                            'sha256': 'string'
                        }
                    },
                ],
                'nextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            Represents the output of a ListApplicationRevisions operation.

            - **revisions** *(list) --*

              A list of locations that contain the matching revisions.

              - *(dict) --*

                Information about the location of an application revision.

                - **revisionType** *(string) --*

                  The type of application revision:

                  * S3: An application revision stored in Amazon S3.

                  * GitHub: An application revision stored in GitHub (EC2/On-premises deployments
                  only).

                  * String: A YAML-formatted or JSON-formatted string (AWS Lambda deployments only).

                - **s3Location** *(dict) --*

                  Information about the location of a revision stored in Amazon S3.

                  - **bucket** *(string) --*

                    The name of the Amazon S3 bucket where the application revision is stored.

                  - **key** *(string) --*

                    The name of the Amazon S3 object that represents the bundled artifacts for the
                    application revision.

                  - **bundleType** *(string) --*

                    The file type of the application revision. Must be one of the following:

                    * tar: A tar archive file.

                    * tgz: A compressed tar archive file.

                    * zip: A zip archive file.

                  - **version** *(string) --*

                    A specific version of the Amazon S3 object that represents the bundled artifacts
                    for the application revision.

                    If the version is not specified, the system uses the most recent version by
                    default.

                  - **eTag** *(string) --*

                    The ETag of the Amazon S3 object that represents the bundled artifacts for the
                    application revision.

                    If the ETag is not specified as an input parameter, ETag validation of the
                    object is skipped.

                - **gitHubLocation** *(dict) --*

                  Information about the location of application artifacts stored in GitHub.

                  - **repository** *(string) --*

                    The GitHub account and repository pair that stores a reference to the commit
                    that represents the bundled artifacts for the application revision.

                    Specified as account/repository.

                  - **commitId** *(string) --*

                    The SHA1 commit ID of the GitHub commit that represents the bundled artifacts
                    for the application revision.

                - **string** *(dict) --*

                  Information about the location of an AWS Lambda deployment revision stored as a
                  RawString.

                  - **content** *(string) --*

                    The YAML-formatted or JSON-formatted revision string. It includes information
                    about which Lambda function to update and optional Lambda functions that
                    validate deployment lifecycle events.

                  - **sha256** *(string) --*

                    The SHA256 hash value of the revision content.

                - **appSpecContent** *(dict) --*

                  The content of an AppSpec file for an AWS Lambda or Amazon ECS deployment. The
                  content is formatted as JSON or YAML and stored as a RawString.

                  - **content** *(string) --*

                    The YAML-formatted or JSON-formatted revision string.

                    For an AWS Lambda deployment, the content includes a Lambda function name, the
                    alias for its original version, and the alias for its replacement version. The
                    deployment shifts traffic from the original version of the Lambda function to
                    the replacement version.

                    For an Amazon ECS deployment, the content includes the task name, information
                    about the load balancer that serves traffic to the container, and more.

                    For both types of deployments, the content can specify Lambda functions that run
                    at specified hooks, such as ``BeforeInstall`` , during a deployment.

                  - **sha256** *(string) --*

                    The SHA256 hash value of the revision content.

            - **nextToken** *(string) --*

              If a large amount of information is returned, an identifier is also returned. It can
              be used in a subsequent list application revisions call to return the next set of
              application revisions in the list.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_applications(self, nextToken: str = None) -> ClientListApplicationsResponseTypeDef:
        """
        Lists the applications registered with the IAM user or AWS account.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/codedeploy-2014-10-06/ListApplications>`_

        **Request Syntax**
        ::

          response = client.list_applications(
              nextToken='string'
          )
        :type nextToken: string
        :param nextToken:

          An identifier returned from the previous list applications call. It can be used to return
          the next set of applications in the list.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'applications': [
                    'string',
                ],
                'nextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            Represents the output of a ListApplications operation.

            - **applications** *(list) --*

              A list of application names.

              - *(string) --*

            - **nextToken** *(string) --*

              If a large amount of information is returned, an identifier is also returned. It can
              be used in a subsequent list applications call to return the next set of applications
              in the list.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_deployment_configs(
        self, nextToken: str = None
    ) -> ClientListDeploymentConfigsResponseTypeDef:
        """
        Lists the deployment configurations with the IAM user or AWS account.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/codedeploy-2014-10-06/ListDeploymentConfigs>`_

        **Request Syntax**
        ::

          response = client.list_deployment_configs(
              nextToken='string'
          )
        :type nextToken: string
        :param nextToken:

          An identifier returned from the previous ``ListDeploymentConfigs`` call. It can be used to
          return the next set of deployment configurations in the list.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'deploymentConfigsList': [
                    'string',
                ],
                'nextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            Represents the output of a ListDeploymentConfigs operation.

            - **deploymentConfigsList** *(list) --*

              A list of deployment configurations, including built-in configurations such as
              CodeDeployDefault.OneAtATime.

              - *(string) --*

            - **nextToken** *(string) --*

              If a large amount of information is returned, an identifier is also returned. It can
              be used in a subsequent list deployment configurations call to return the next set of
              deployment configurations in the list.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_deployment_groups(
        self, applicationName: str, nextToken: str = None
    ) -> ClientListDeploymentGroupsResponseTypeDef:
        """
        Lists the deployment groups for an application registered with the IAM user or AWS account.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/codedeploy-2014-10-06/ListDeploymentGroups>`_

        **Request Syntax**
        ::

          response = client.list_deployment_groups(
              applicationName='string',
              nextToken='string'
          )
        :type applicationName: string
        :param applicationName: **[REQUIRED]**

          The name of an AWS CodeDeploy application associated with the IAM user or AWS account.

        :type nextToken: string
        :param nextToken:

          An identifier returned from the previous list deployment groups call. It can be used to
          return the next set of deployment groups in the list.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'applicationName': 'string',
                'deploymentGroups': [
                    'string',
                ],
                'nextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            Represents the output of a ListDeploymentGroups operation.

            - **applicationName** *(string) --*

              The application name.

            - **deploymentGroups** *(list) --*

              A list of deployment group names.

              - *(string) --*

            - **nextToken** *(string) --*

              If a large amount of information is returned, an identifier is also returned. It can
              be used in a subsequent list deployment groups call to return the next set of
              deployment groups in the list.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_deployment_instances(
        self,
        deploymentId: str,
        nextToken: str = None,
        instanceStatusFilter: List[
            Literal["Pending", "InProgress", "Succeeded", "Failed", "Skipped", "Unknown", "Ready"]
        ] = None,
        instanceTypeFilter: List[Literal["Blue", "Green"]] = None,
    ) -> ClientListDeploymentInstancesResponseTypeDef:
        """
        .. note::

          The newer BatchGetDeploymentTargets should be used instead because it works with all
          compute types. ``ListDeploymentInstances`` throws an exception if it is used with a
          compute platform other than EC2/On-premises or AWS Lambda.

        Lists the instance for a deployment associated with the IAM user or AWS account.

        .. danger::

            This operation is deprecated and may not function as expected. This operation should not
            be used going forward and is only kept for the purpose of backwards compatiblity.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/codedeploy-2014-10-06/ListDeploymentInstances>`_

        **Request Syntax**
        ::

          response = client.list_deployment_instances(
              deploymentId='string',
              nextToken='string',
              instanceStatusFilter=[
                  'Pending'|'InProgress'|'Succeeded'|'Failed'|'Skipped'|'Unknown'|'Ready',
              ],
              instanceTypeFilter=[
                  'Blue'|'Green',
              ]
          )
        :type deploymentId: string
        :param deploymentId: **[REQUIRED]**

          The unique ID of a deployment.

        :type nextToken: string
        :param nextToken:

          An identifier returned from the previous list deployment instances call. It can be used to
          return the next set of deployment instances in the list.

        :type instanceStatusFilter: list
        :param instanceStatusFilter:

          A subset of instances to list by status:

          * Pending: Include those instances with pending deployments.

          * InProgress: Include those instances where deployments are still in progress.

          * Succeeded: Include those instances with successful deployments.

          * Failed: Include those instances with failed deployments.

          * Skipped: Include those instances with skipped deployments.

          * Unknown: Include those instances with deployments in an unknown state.

          - *(string) --*

        :type instanceTypeFilter: list
        :param instanceTypeFilter:

          The set of instances in a blue/green deployment, either those in the original environment
          ("BLUE") or those in the replacement environment ("GREEN"), for which you want to view
          instance information.

          - *(string) --*

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'instancesList': [
                    'string',
                ],
                'nextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            Represents the output of a ListDeploymentInstances operation.

            - **instancesList** *(list) --*

              A list of instance IDs.

              - *(string) --*

            - **nextToken** *(string) --*

              If a large amount of information is returned, an identifier is also returned. It can
              be used in a subsequent list deployment instances call to return the next set of
              deployment instances in the list.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_deployment_targets(
        self,
        deploymentId: str = None,
        nextToken: str = None,
        targetFilters: Dict[str, List[str]] = None,
    ) -> ClientListDeploymentTargetsResponseTypeDef:
        """
        Returns an array of target IDs that are associated a deployment.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/codedeploy-2014-10-06/ListDeploymentTargets>`_

        **Request Syntax**
        ::

          response = client.list_deployment_targets(
              deploymentId='string',
              nextToken='string',
              targetFilters={
                  'string': [
                      'string',
                  ]
              }
          )
        :type deploymentId: string
        :param deploymentId:

          The unique ID of a deployment.

        :type nextToken: string
        :param nextToken:

          A token identifier returned from the previous ``ListDeploymentTargets`` call. It can be
          used to return the next set of deployment targets in the list.

        :type targetFilters: dict
        :param targetFilters:

          A key used to filter the returned targets. The two valid values are:

          * ``TargetStatus`` - A ``TargetStatus`` filter string can be ``Failed`` , ``InProgress`` ,
          ``Pending`` , ``Ready`` , ``Skipped`` , ``Succeeded`` , or ``Unknown`` .

          * ``ServerInstanceLabel`` - A ``ServerInstanceLabel`` filter string can be ``Blue`` or
          ``Green`` .

          - *(string) --*

            - *(list) --*

              - *(string) --*

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'targetIds': [
                    'string',
                ],
                'nextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **targetIds** *(list) --*

              The unique IDs of deployment targets.

              - *(string) --*

            - **nextToken** *(string) --*

              If a large amount of information is returned, a token identifier is also returned. It
              can be used in a subsequent ``ListDeploymentTargets`` call to return the next set of
              deployment targets in the list.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_deployments(
        self,
        applicationName: str = None,
        deploymentGroupName: str = None,
        includeOnlyStatuses: List[
            Literal["Created", "Queued", "InProgress", "Succeeded", "Failed", "Stopped", "Ready"]
        ] = None,
        createTimeRange: ClientListDeploymentsCreateTimeRangeTypeDef = None,
        nextToken: str = None,
    ) -> ClientListDeploymentsResponseTypeDef:
        """
        Lists the deployments in a deployment group for an application registered with the IAM user
        or AWS account.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/codedeploy-2014-10-06/ListDeployments>`_

        **Request Syntax**
        ::

          response = client.list_deployments(
              applicationName='string',
              deploymentGroupName='string',
              includeOnlyStatuses=[
                  'Created'|'Queued'|'InProgress'|'Succeeded'|'Failed'|'Stopped'|'Ready',
              ],
              createTimeRange={
                  'start': datetime(2015, 1, 1),
                  'end': datetime(2015, 1, 1)
              },
              nextToken='string'
          )
        :type applicationName: string
        :param applicationName:

          The name of an AWS CodeDeploy application associated with the IAM user or AWS account.

          .. note::

            If ``applicationName`` is specified, then ``deploymentGroupName`` must be specified. If
            it is not specified, then ``deploymentGroupName`` must not be specified.

        :type deploymentGroupName: string
        :param deploymentGroupName:

          The name of a deployment group for the specified application.

          .. note::

            If ``deploymentGroupName`` is specified, then ``applicationName`` must be specified. If
            it is not specified, then ``applicationName`` must not be specified.

        :type includeOnlyStatuses: list
        :param includeOnlyStatuses:

          A subset of deployments to list by status:

          * Created: Include created deployments in the resulting list.

          * Queued: Include queued deployments in the resulting list.

          * In Progress: Include in-progress deployments in the resulting list.

          * Succeeded: Include successful deployments in the resulting list.

          * Failed: Include failed deployments in the resulting list.

          * Stopped: Include stopped deployments in the resulting list.

          - *(string) --*

        :type createTimeRange: dict
        :param createTimeRange:

          A time range (start and end) for returning a subset of the list of deployments.

          - **start** *(datetime) --*

            The start time of the time range.

            .. note::

              Specify null to leave the start time open-ended.

          - **end** *(datetime) --*

            The end time of the time range.

            .. note::

              Specify null to leave the end time open-ended.

        :type nextToken: string
        :param nextToken:

          An identifier returned from the previous list deployments call. It can be used to return
          the next set of deployments in the list.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'deployments': [
                    'string',
                ],
                'nextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            Represents the output of a ListDeployments operation.

            - **deployments** *(list) --*

              A list of deployment IDs.

              - *(string) --*

            - **nextToken** *(string) --*

              If a large amount of information is returned, an identifier is also returned. It can
              be used in a subsequent list deployments call to return the next set of deployments in
              the list.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_git_hub_account_token_names(
        self, nextToken: str = None
    ) -> ClientListGitHubAccountTokenNamesResponseTypeDef:
        """
        Lists the names of stored connections to GitHub accounts.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/codedeploy-2014-10-06/ListGitHubAccountTokenNames>`_

        **Request Syntax**
        ::

          response = client.list_git_hub_account_token_names(
              nextToken='string'
          )
        :type nextToken: string
        :param nextToken:

          An identifier returned from the previous ListGitHubAccountTokenNames call. It can be used
          to return the next set of names in the list.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'tokenNameList': [
                    'string',
                ],
                'nextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            Represents the output of a ListGitHubAccountTokenNames operation.

            - **tokenNameList** *(list) --*

              A list of names of connections to GitHub accounts.

              - *(string) --*

            - **nextToken** *(string) --*

              If a large amount of information is returned, an identifier is also returned. It can
              be used in a subsequent ListGitHubAccountTokenNames call to return the next set of
              names in the list.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_on_premises_instances(
        self,
        registrationStatus: Literal["Registered", "Deregistered"] = None,
        tagFilters: List[ClientListOnPremisesInstancesTagFiltersTypeDef] = None,
        nextToken: str = None,
    ) -> ClientListOnPremisesInstancesResponseTypeDef:
        """
        Gets a list of names for one or more on-premises instances.

        Unless otherwise specified, both registered and deregistered on-premises instance names are
        listed. To list only registered or deregistered on-premises instance names, use the
        registration status parameter.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/codedeploy-2014-10-06/ListOnPremisesInstances>`_

        **Request Syntax**
        ::

          response = client.list_on_premises_instances(
              registrationStatus='Registered'|'Deregistered',
              tagFilters=[
                  {
                      'Key': 'string',
                      'Value': 'string',
                      'Type': 'KEY_ONLY'|'VALUE_ONLY'|'KEY_AND_VALUE'
                  },
              ],
              nextToken='string'
          )
        :type registrationStatus: string
        :param registrationStatus:

          The registration status of the on-premises instances:

          * Deregistered: Include deregistered on-premises instances in the resulting list.

          * Registered: Include registered on-premises instances in the resulting list.

        :type tagFilters: list
        :param tagFilters:

          The on-premises instance tags that are used to restrict the on-premises instance names
          returned.

          - *(dict) --*

            Information about an on-premises instance tag filter.

            - **Key** *(string) --*

              The on-premises instance tag filter key.

            - **Value** *(string) --*

              The on-premises instance tag filter value.

            - **Type** *(string) --*

              The on-premises instance tag filter type:

              * KEY_ONLY: Key only.

              * VALUE_ONLY: Value only.

              * KEY_AND_VALUE: Key and value.

        :type nextToken: string
        :param nextToken:

          An identifier returned from the previous list on-premises instances call. It can be used
          to return the next set of on-premises instances in the list.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'instanceNames': [
                    'string',
                ],
                'nextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            Represents the output of the list on-premises instances operation.

            - **instanceNames** *(list) --*

              The list of matching on-premises instance names.

              - *(string) --*

            - **nextToken** *(string) --*

              If a large amount of information is returned, an identifier is also returned. It can
              be used in a subsequent list on-premises instances call to return the next set of
              on-premises instances in the list.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_tags_for_resource(
        self, ResourceArn: str, NextToken: str = None
    ) -> ClientListTagsForResourceResponseTypeDef:
        """
        Returns a list of tags for the resource identified by a specified ARN. Tags are used to
        organize and categorize your CodeDeploy resources.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/codedeploy-2014-10-06/ListTagsForResource>`_

        **Request Syntax**
        ::

          response = client.list_tags_for_resource(
              ResourceArn='string',
              NextToken='string'
          )
        :type ResourceArn: string
        :param ResourceArn: **[REQUIRED]**

          The ARN of a CodeDeploy resource. ``ListTagsForResource`` returns all the tags associated
          with the resource that is identified by the ``ResourceArn`` .

        :type NextToken: string
        :param NextToken:

          An identifier returned from the previous ``ListTagsForResource`` call. It can be used to
          return the next set of applications in the list.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Tags': [
                    {
                        'Key': 'string',
                        'Value': 'string'
                    },
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **Tags** *(list) --*

              A list of tags returned by ``ListTagsForResource`` . The tags are associated with the
              resource identified by the input ``ResourceArn`` parameter.

              - *(dict) --*

                Information about a tag.

                - **Key** *(string) --*

                  The tag's key.

                - **Value** *(string) --*

                  The tag's value.

            - **NextToken** *(string) --*

              If a large amount of information is returned, an identifier is also returned. It can
              be used in a subsequent list application revisions call to return the next set of
              application revisions in the list.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def put_lifecycle_event_hook_execution_status(
        self,
        deploymentId: str = None,
        lifecycleEventHookExecutionId: str = None,
        status: Literal[
            "Pending", "InProgress", "Succeeded", "Failed", "Skipped", "Unknown"
        ] = None,
    ) -> ClientPutLifecycleEventHookExecutionStatusResponseTypeDef:
        """
        Sets the result of a Lambda validation function. The function validates one or both
        lifecycle events (``BeforeAllowTraffic`` and ``AfterAllowTraffic`` ) and returns
        ``Succeeded`` or ``Failed`` .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/codedeploy-2014-10-06/PutLifecycleEventHookExecutionStatus>`_

        **Request Syntax**
        ::

          response = client.put_lifecycle_event_hook_execution_status(
              deploymentId='string',
              lifecycleEventHookExecutionId='string',
              status='Pending'|'InProgress'|'Succeeded'|'Failed'|'Skipped'|'Unknown'
          )
        :type deploymentId: string
        :param deploymentId:

          The unique ID of a deployment. Pass this ID to a Lambda function that validates a
          deployment lifecycle event.

        :type lifecycleEventHookExecutionId: string
        :param lifecycleEventHookExecutionId:

          The execution ID of a deployment's lifecycle hook. A deployment lifecycle hook is
          specified in the ``hooks`` section of the AppSpec file.

        :type status: string
        :param status:

          The result of a Lambda function that validates a deployment lifecycle event (``Succeeded``
          or ``Failed`` ).

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'lifecycleEventHookExecutionId': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **lifecycleEventHookExecutionId** *(string) --*

              The execution ID of the lifecycle event hook. A hook is specified in the ``hooks``
              section of the deployment's AppSpec file.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def register_application_revision(
        self,
        applicationName: str,
        revision: ClientRegisterApplicationRevisionRevisionTypeDef,
        description: str = None,
    ) -> None:
        """
        Registers with AWS CodeDeploy a revision for the specified application.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/codedeploy-2014-10-06/RegisterApplicationRevision>`_

        **Request Syntax**
        ::

          response = client.register_application_revision(
              applicationName='string',
              description='string',
              revision={
                  'revisionType': 'S3'|'GitHub'|'String'|'AppSpecContent',
                  's3Location': {
                      'bucket': 'string',
                      'key': 'string',
                      'bundleType': 'tar'|'tgz'|'zip'|'YAML'|'JSON',
                      'version': 'string',
                      'eTag': 'string'
                  },
                  'gitHubLocation': {
                      'repository': 'string',
                      'commitId': 'string'
                  },
                  'string': {
                      'content': 'string',
                      'sha256': 'string'
                  },
                  'appSpecContent': {
                      'content': 'string',
                      'sha256': 'string'
                  }
              }
          )
        :type applicationName: string
        :param applicationName: **[REQUIRED]**

          The name of an AWS CodeDeploy application associated with the IAM user or AWS account.

        :type description: string
        :param description:

          A comment about the revision.

        :type revision: dict
        :param revision: **[REQUIRED]**

          Information about the application revision to register, including type and location.

          - **revisionType** *(string) --*

            The type of application revision:

            * S3: An application revision stored in Amazon S3.

            * GitHub: An application revision stored in GitHub (EC2/On-premises deployments only).

            * String: A YAML-formatted or JSON-formatted string (AWS Lambda deployments only).

          - **s3Location** *(dict) --*

            Information about the location of a revision stored in Amazon S3.

            - **bucket** *(string) --*

              The name of the Amazon S3 bucket where the application revision is stored.

            - **key** *(string) --*

              The name of the Amazon S3 object that represents the bundled artifacts for the
              application revision.

            - **bundleType** *(string) --*

              The file type of the application revision. Must be one of the following:

              * tar: A tar archive file.

              * tgz: A compressed tar archive file.

              * zip: A zip archive file.

            - **version** *(string) --*

              A specific version of the Amazon S3 object that represents the bundled artifacts for
              the application revision.

              If the version is not specified, the system uses the most recent version by default.

            - **eTag** *(string) --*

              The ETag of the Amazon S3 object that represents the bundled artifacts for the
              application revision.

              If the ETag is not specified as an input parameter, ETag validation of the object is
              skipped.

          - **gitHubLocation** *(dict) --*

            Information about the location of application artifacts stored in GitHub.

            - **repository** *(string) --*

              The GitHub account and repository pair that stores a reference to the commit that
              represents the bundled artifacts for the application revision.

              Specified as account/repository.

            - **commitId** *(string) --*

              The SHA1 commit ID of the GitHub commit that represents the bundled artifacts for the
              application revision.

          - **string** *(dict) --*

            Information about the location of an AWS Lambda deployment revision stored as a
            RawString.

            - **content** *(string) --*

              The YAML-formatted or JSON-formatted revision string. It includes information about
              which Lambda function to update and optional Lambda functions that validate deployment
              lifecycle events.

            - **sha256** *(string) --*

              The SHA256 hash value of the revision content.

          - **appSpecContent** *(dict) --*

            The content of an AppSpec file for an AWS Lambda or Amazon ECS deployment. The content
            is formatted as JSON or YAML and stored as a RawString.

            - **content** *(string) --*

              The YAML-formatted or JSON-formatted revision string.

              For an AWS Lambda deployment, the content includes a Lambda function name, the alias
              for its original version, and the alias for its replacement version. The deployment
              shifts traffic from the original version of the Lambda function to the replacement
              version.

              For an Amazon ECS deployment, the content includes the task name, information about
              the load balancer that serves traffic to the container, and more.

              For both types of deployments, the content can specify Lambda functions that run at
              specified hooks, such as ``BeforeInstall`` , during a deployment.

            - **sha256** *(string) --*

              The SHA256 hash value of the revision content.

        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def register_on_premises_instance(
        self, instanceName: str, iamSessionArn: str = None, iamUserArn: str = None
    ) -> None:
        """
        Registers an on-premises instance.

        .. note::

          Only one IAM ARN (an IAM session ARN or IAM user ARN) is supported in the request. You
          cannot use both.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/codedeploy-2014-10-06/RegisterOnPremisesInstance>`_

        **Request Syntax**
        ::

          response = client.register_on_premises_instance(
              instanceName='string',
              iamSessionArn='string',
              iamUserArn='string'
          )
        :type instanceName: string
        :param instanceName: **[REQUIRED]**

          The name of the on-premises instance to register.

        :type iamSessionArn: string
        :param iamSessionArn:

          The ARN of the IAM session to associate with the on-premises instance.

        :type iamUserArn: string
        :param iamUserArn:

          The ARN of the IAM user to associate with the on-premises instance.

        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def remove_tags_from_on_premises_instances(
        self,
        tags: List[ClientRemoveTagsFromOnPremisesInstancesTagsTypeDef],
        instanceNames: List[str],
    ) -> None:
        """
        Removes one or more tags from one or more on-premises instances.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/codedeploy-2014-10-06/RemoveTagsFromOnPremisesInstances>`_

        **Request Syntax**
        ::

          response = client.remove_tags_from_on_premises_instances(
              tags=[
                  {
                      'Key': 'string',
                      'Value': 'string'
                  },
              ],
              instanceNames=[
                  'string',
              ]
          )
        :type tags: list
        :param tags: **[REQUIRED]**

          The tag key-value pairs to remove from the on-premises instances.

          - *(dict) --*

            Information about a tag.

            - **Key** *(string) --*

              The tag's key.

            - **Value** *(string) --*

              The tag's value.

        :type instanceNames: list
        :param instanceNames: **[REQUIRED]**

          The names of the on-premises instances from which to remove tags.

          - *(string) --*

        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def skip_wait_time_for_instance_termination(self, deploymentId: str = None) -> None:
        """
        In a blue/green deployment, overrides any specified wait time and starts terminating
        instances immediately after the traffic routing is complete.

        .. danger::

            This operation is deprecated and may not function as expected. This operation should not
            be used going forward and is only kept for the purpose of backwards compatiblity.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/codedeploy-2014-10-06/SkipWaitTimeForInstanceTermination>`_

        **Request Syntax**
        ::

          response = client.skip_wait_time_for_instance_termination(
              deploymentId='string'
          )
        :type deploymentId: string
        :param deploymentId:

          The unique ID of a blue/green deployment for which you want to skip the instance
          termination wait time.

        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def stop_deployment(
        self, deploymentId: str, autoRollbackEnabled: bool = None
    ) -> ClientStopDeploymentResponseTypeDef:
        """
        Attempts to stop an ongoing deployment.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/codedeploy-2014-10-06/StopDeployment>`_

        **Request Syntax**
        ::

          response = client.stop_deployment(
              deploymentId='string',
              autoRollbackEnabled=True|False
          )
        :type deploymentId: string
        :param deploymentId: **[REQUIRED]**

          The unique ID of a deployment.

        :type autoRollbackEnabled: boolean
        :param autoRollbackEnabled:

          Indicates, when a deployment is stopped, whether instances that have been updated should
          be rolled back to the previous version of the application revision.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'status': 'Pending'|'Succeeded',
                'statusMessage': 'string'
            }
          **Response Structure**

          - *(dict) --*

            Represents the output of a StopDeployment operation.

            - **status** *(string) --*

              The status of the stop deployment operation:

              * Pending: The stop operation is pending.

              * Succeeded: The stop operation was successful.

            - **statusMessage** *(string) --*

              An accompanying status message.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def tag_resource(
        self, ResourceArn: str, Tags: List[ClientTagResourceTagsTypeDef]
    ) -> Dict[str, Any]:
        """
        Associates the list of tags in the input ``Tags`` parameter with the resource identified by
        the ``ResourceArn`` input parameter.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/codedeploy-2014-10-06/TagResource>`_

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

          The ARN of a resource, such as a CodeDeploy application or deployment group.

        :type Tags: list
        :param Tags: **[REQUIRED]**

          A list of tags that ``TagResource`` associates with a resource. The resource is identified
          by the ``ResourceArn`` input parameter.

          - *(dict) --*

            Information about a tag.

            - **Key** *(string) --*

              The tag's key.

            - **Value** *(string) --*

              The tag's value.

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
        Disassociates a resource from a list of tags. The resource is identified by the
        ``ResourceArn`` input parameter. The tags are identfied by the list of keys in the
        ``TagKeys`` input parameter.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/codedeploy-2014-10-06/UntagResource>`_

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

          The ARN that specifies from which resource to disassociate the tags with the keys in the
          ``TagKeys`` input paramter.

        :type TagKeys: list
        :param TagKeys: **[REQUIRED]**

          A list of keys of ``Tag`` objects. The ``Tag`` objects identified by the keys are
          disassociated from the resource specified by the ``ResourceArn`` input parameter.

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
    def update_application(
        self, applicationName: str = None, newApplicationName: str = None
    ) -> None:
        """
        Changes the name of an application.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/codedeploy-2014-10-06/UpdateApplication>`_

        **Request Syntax**
        ::

          response = client.update_application(
              applicationName='string',
              newApplicationName='string'
          )
        :type applicationName: string
        :param applicationName:

          The current name of the application you want to change.

        :type newApplicationName: string
        :param newApplicationName:

          The new name to give the application.

        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_deployment_group(
        self,
        applicationName: str,
        currentDeploymentGroupName: str,
        newDeploymentGroupName: str = None,
        deploymentConfigName: str = None,
        ec2TagFilters: List[ClientUpdateDeploymentGroupEc2TagFiltersTypeDef] = None,
        onPremisesInstanceTagFilters: List[
            ClientUpdateDeploymentGroupOnPremisesInstanceTagFiltersTypeDef
        ] = None,
        autoScalingGroups: List[str] = None,
        serviceRoleArn: str = None,
        triggerConfigurations: List[ClientUpdateDeploymentGroupTriggerConfigurationsTypeDef] = None,
        alarmConfiguration: ClientUpdateDeploymentGroupAlarmConfigurationTypeDef = None,
        autoRollbackConfiguration: ClientUpdateDeploymentGroupAutoRollbackConfigurationTypeDef = None,
        deploymentStyle: ClientUpdateDeploymentGroupDeploymentStyleTypeDef = None,
        blueGreenDeploymentConfiguration: ClientUpdateDeploymentGroupBlueGreenDeploymentConfigurationTypeDef = None,
        loadBalancerInfo: ClientUpdateDeploymentGroupLoadBalancerInfoTypeDef = None,
        ec2TagSet: ClientUpdateDeploymentGroupEc2TagSetTypeDef = None,
        ecsServices: List[ClientUpdateDeploymentGroupEcsServicesTypeDef] = None,
        onPremisesTagSet: ClientUpdateDeploymentGroupOnPremisesTagSetTypeDef = None,
    ) -> ClientUpdateDeploymentGroupResponseTypeDef:
        """
        Changes information about a deployment group.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/codedeploy-2014-10-06/UpdateDeploymentGroup>`_

        **Request Syntax**
        ::

          response = client.update_deployment_group(
              applicationName='string',
              currentDeploymentGroupName='string',
              newDeploymentGroupName='string',
              deploymentConfigName='string',
              ec2TagFilters=[
                  {
                      'Key': 'string',
                      'Value': 'string',
                      'Type': 'KEY_ONLY'|'VALUE_ONLY'|'KEY_AND_VALUE'
                  },
              ],
              onPremisesInstanceTagFilters=[
                  {
                      'Key': 'string',
                      'Value': 'string',
                      'Type': 'KEY_ONLY'|'VALUE_ONLY'|'KEY_AND_VALUE'
                  },
              ],
              autoScalingGroups=[
                  'string',
              ],
              serviceRoleArn='string',
              triggerConfigurations=[
                  {
                      'triggerName': 'string',
                      'triggerTargetArn': 'string',
                      'triggerEvents': [
                          'DeploymentStart'|'DeploymentSuccess'|'DeploymentFailure'|'DeploymentStop'
                          |'DeploymentRollback'|'DeploymentReady'|'InstanceStart'|'InstanceSuccess'
                          |'InstanceFailure'|'InstanceReady',
                      ]
                  },
              ],
              alarmConfiguration={
                  'enabled': True|False,
                  'ignorePollAlarmFailure': True|False,
                  'alarms': [
                      {
                          'name': 'string'
                      },
                  ]
              },
              autoRollbackConfiguration={
                  'enabled': True|False,
                  'events': [
                      'DEPLOYMENT_FAILURE'|'DEPLOYMENT_STOP_ON_ALARM'|'DEPLOYMENT_STOP_ON_REQUEST',
                  ]
              },
              deploymentStyle={
                  'deploymentType': 'IN_PLACE'|'BLUE_GREEN',
                  'deploymentOption': 'WITH_TRAFFIC_CONTROL'|'WITHOUT_TRAFFIC_CONTROL'
              },
              blueGreenDeploymentConfiguration={
                  'terminateBlueInstancesOnDeploymentSuccess': {
                      'action': 'TERMINATE'|'KEEP_ALIVE',
                      'terminationWaitTimeInMinutes': 123
                  },
                  'deploymentReadyOption': {
                      'actionOnTimeout': 'CONTINUE_DEPLOYMENT'|'STOP_DEPLOYMENT',
                      'waitTimeInMinutes': 123
                  },
                  'greenFleetProvisioningOption': {
                      'action': 'DISCOVER_EXISTING'|'COPY_AUTO_SCALING_GROUP'
                  }
              },
              loadBalancerInfo={
                  'elbInfoList': [
                      {
                          'name': 'string'
                      },
                  ],
                  'targetGroupInfoList': [
                      {
                          'name': 'string'
                      },
                  ],
                  'targetGroupPairInfoList': [
                      {
                          'targetGroups': [
                              {
                                  'name': 'string'
                              },
                          ],
                          'prodTrafficRoute': {
                              'listenerArns': [
                                  'string',
                              ]
                          },
                          'testTrafficRoute': {
                              'listenerArns': [
                                  'string',
                              ]
                          }
                      },
                  ]
              },
              ec2TagSet={
                  'ec2TagSetList': [
                      [
                          {
                              'Key': 'string',
                              'Value': 'string',
                              'Type': 'KEY_ONLY'|'VALUE_ONLY'|'KEY_AND_VALUE'
                          },
                      ],
                  ]
              },
              ecsServices=[
                  {
                      'serviceName': 'string',
                      'clusterName': 'string'
                  },
              ],
              onPremisesTagSet={
                  'onPremisesTagSetList': [
                      [
                          {
                              'Key': 'string',
                              'Value': 'string',
                              'Type': 'KEY_ONLY'|'VALUE_ONLY'|'KEY_AND_VALUE'
                          },
                      ],
                  ]
              }
          )
        :type applicationName: string
        :param applicationName: **[REQUIRED]**

          The application name that corresponds to the deployment group to update.

        :type currentDeploymentGroupName: string
        :param currentDeploymentGroupName: **[REQUIRED]**

          The current name of the deployment group.

        :type newDeploymentGroupName: string
        :param newDeploymentGroupName:

          The new name of the deployment group, if you want to change it.

        :type deploymentConfigName: string
        :param deploymentConfigName:

          The replacement deployment configuration name to use, if you want to change it.

        :type ec2TagFilters: list
        :param ec2TagFilters:

          The replacement set of Amazon EC2 tags on which to filter, if you want to change them. To
          keep the existing tags, enter their names. To remove tags, do not enter any tag names.

          - *(dict) --*

            Information about an EC2 tag filter.

            - **Key** *(string) --*

              The tag filter key.

            - **Value** *(string) --*

              The tag filter value.

            - **Type** *(string) --*

              The tag filter type:

              * KEY_ONLY: Key only.

              * VALUE_ONLY: Value only.

              * KEY_AND_VALUE: Key and value.

        :type onPremisesInstanceTagFilters: list
        :param onPremisesInstanceTagFilters:

          The replacement set of on-premises instance tags on which to filter, if you want to change
          them. To keep the existing tags, enter their names. To remove tags, do not enter any tag
          names.

          - *(dict) --*

            Information about an on-premises instance tag filter.

            - **Key** *(string) --*

              The on-premises instance tag filter key.

            - **Value** *(string) --*

              The on-premises instance tag filter value.

            - **Type** *(string) --*

              The on-premises instance tag filter type:

              * KEY_ONLY: Key only.

              * VALUE_ONLY: Value only.

              * KEY_AND_VALUE: Key and value.

        :type autoScalingGroups: list
        :param autoScalingGroups:

          The replacement list of Auto Scaling groups to be included in the deployment group, if you
          want to change them. To keep the Auto Scaling groups, enter their names. To remove Auto
          Scaling groups, do not enter any Auto Scaling group names.

          - *(string) --*

        :type serviceRoleArn: string
        :param serviceRoleArn:

          A replacement ARN for the service role, if you want to change it.

        :type triggerConfigurations: list
        :param triggerConfigurations:

          Information about triggers to change when the deployment group is updated. For examples,
          see `Modify Triggers in an AWS CodeDeploy Deployment Group
          <https://docs.aws.amazon.com/codedeploy/latest/userguide/how-to-notify-edit.html>`__ in
          the AWS CodeDeploy User Guide.

          - *(dict) --*

            Information about notification triggers for the deployment group.

            - **triggerName** *(string) --*

              The name of the notification trigger.

            - **triggerTargetArn** *(string) --*

              The ARN of the Amazon Simple Notification Service topic through which notifications
              about deployment or instance events are sent.

            - **triggerEvents** *(list) --*

              The event type or types for which notifications are triggered.

              - *(string) --*

        :type alarmConfiguration: dict
        :param alarmConfiguration:

          Information to add or change about Amazon CloudWatch alarms when the deployment group is
          updated.

          - **enabled** *(boolean) --*

            Indicates whether the alarm configuration is enabled.

          - **ignorePollAlarmFailure** *(boolean) --*

            Indicates whether a deployment should continue if information about the current state of
            alarms cannot be retrieved from Amazon CloudWatch. The default value is false.

            * true: The deployment proceeds even if alarm status information can't be retrieved from
            Amazon CloudWatch.

            * false: The deployment stops if alarm status information can't be retrieved from Amazon
            CloudWatch.

          - **alarms** *(list) --*

            A list of alarms configured for the deployment group. A maximum of 10 alarms can be
            added to a deployment group.

            - *(dict) --*

              Information about an alarm.

              - **name** *(string) --*

                The name of the alarm. Maximum length is 255 characters. Each alarm name can be used
                only once in a list of alarms.

        :type autoRollbackConfiguration: dict
        :param autoRollbackConfiguration:

          Information for an automatic rollback configuration that is added or changed when a
          deployment group is updated.

          - **enabled** *(boolean) --*

            Indicates whether a defined automatic rollback configuration is currently enabled.

          - **events** *(list) --*

            The event type or types that trigger a rollback.

            - *(string) --*

        :type deploymentStyle: dict
        :param deploymentStyle:

          Information about the type of deployment, either in-place or blue/green, you want to run
          and whether to route deployment traffic behind a load balancer.

          - **deploymentType** *(string) --*

            Indicates whether to run an in-place deployment or a blue/green deployment.

          - **deploymentOption** *(string) --*

            Indicates whether to route deployment traffic behind a load balancer.

        :type blueGreenDeploymentConfiguration: dict
        :param blueGreenDeploymentConfiguration:

          Information about blue/green deployment options for a deployment group.

          - **terminateBlueInstancesOnDeploymentSuccess** *(dict) --*

            Information about whether to terminate instances in the original fleet during a
            blue/green deployment.

            - **action** *(string) --*

              The action to take on instances in the original environment after a successful
              blue/green deployment.

              * TERMINATE: Instances are terminated after a specified wait time.

              * KEEP_ALIVE: Instances are left running after they are deregistered from the load
              balancer and removed from the deployment group.

            - **terminationWaitTimeInMinutes** *(integer) --*

              For an Amazon EC2 deployment, the number of minutes to wait after a successful
              blue/green deployment before terminating instances from the original environment.

              For an Amazon ECS deployment, the number of minutes before deleting the original
              (blue) task set. During an Amazon ECS deployment, CodeDeploy shifts traffic from the
              original (blue) task set to a replacement (green) task set.

              The maximum setting is 2880 minutes (2 days).

          - **deploymentReadyOption** *(dict) --*

            Information about the action to take when newly provisioned instances are ready to
            receive traffic in a blue/green deployment.

            - **actionOnTimeout** *(string) --*

              Information about when to reroute traffic from an original environment to a
              replacement environment in a blue/green deployment.

              * CONTINUE_DEPLOYMENT: Register new instances with the load balancer immediately after
              the new application revision is installed on the instances in the replacement
              environment.

              * STOP_DEPLOYMENT: Do not register new instances with a load balancer unless traffic
              rerouting is started using  ContinueDeployment . If traffic rerouting is not started
              before the end of the specified wait period, the deployment status is changed to
              Stopped.

            - **waitTimeInMinutes** *(integer) --*

              The number of minutes to wait before the status of a blue/green deployment is changed
              to Stopped if rerouting is not started manually. Applies only to the STOP_DEPLOYMENT
              option for actionOnTimeout

          - **greenFleetProvisioningOption** *(dict) --*

            Information about how instances are provisioned for a replacement environment in a
            blue/green deployment.

            - **action** *(string) --*

              The method used to add instances to a replacement environment.

              * DISCOVER_EXISTING: Use instances that already exist or will be created manually.

              * COPY_AUTO_SCALING_GROUP: Use settings from a specified Auto Scaling group to define
              and create instances in a new Auto Scaling group.

        :type loadBalancerInfo: dict
        :param loadBalancerInfo:

          Information about the load balancer used in a deployment.

          - **elbInfoList** *(list) --*

            An array that contains information about the load balancer to use for load balancing in
            a deployment. In Elastic Load Balancing, load balancers are used with Classic Load
            Balancers.

            .. note::

              Adding more than one load balancer to the array is not supported.

            - *(dict) --*

              Information about a load balancer in Elastic Load Balancing to use in a deployment.
              Instances are registered directly with a load balancer, and traffic is routed to the
              load balancer.

              - **name** *(string) --*

                For blue/green deployments, the name of the load balancer that is used to route
                traffic from original instances to replacement instances in a blue/green deployment.
                For in-place deployments, the name of the load balancer that instances are
                deregistered from so they are not serving traffic during a deployment, and then
                re-registered with after the deployment is complete.

          - **targetGroupInfoList** *(list) --*

            An array that contains information about the target group to use for load balancing in a
            deployment. In Elastic Load Balancing, target groups are used with Application Load
            Balancers.

            .. note::

              Adding more than one target group to the array is not supported.

            - *(dict) --*

              Information about a target group in Elastic Load Balancing to use in a deployment.
              Instances are registered as targets in a target group, and traffic is routed to the
              target group.

              - **name** *(string) --*

                For blue/green deployments, the name of the target group that instances in the
                original environment are deregistered from, and instances in the replacement
                environment are registered with. For in-place deployments, the name of the target
                group that instances are deregistered from, so they are not serving traffic during a
                deployment, and then re-registered with after the deployment is complete.

          - **targetGroupPairInfoList** *(list) --*

            The target group pair information. This is an array of ``TargeGroupPairInfo`` objects
            with a maximum size of one.

            - *(dict) --*

              Information about two target groups and how traffic is routed during an Amazon ECS
              deployment. An optional test traffic route can be specified.

              - **targetGroups** *(list) --*

                One pair of target groups. One is associated with the original task set. The second
                is associated with the task set that serves traffic after the deployment is
                complete.

                - *(dict) --*

                  Information about a target group in Elastic Load Balancing to use in a deployment.
                  Instances are registered as targets in a target group, and traffic is routed to
                  the target group.

                  - **name** *(string) --*

                    For blue/green deployments, the name of the target group that instances in the
                    original environment are deregistered from, and instances in the replacement
                    environment are registered with. For in-place deployments, the name of the
                    target group that instances are deregistered from, so they are not serving
                    traffic during a deployment, and then re-registered with after the deployment is
                    complete.

              - **prodTrafficRoute** *(dict) --*

                The path used by a load balancer to route production traffic when an Amazon ECS
                deployment is complete.

                - **listenerArns** *(list) --*

                  The ARN of one listener. The listener identifies the route between a target group
                  and a load balancer. This is an array of strings with a maximum size of one.

                  - *(string) --*

              - **testTrafficRoute** *(dict) --*

                An optional path used by a load balancer to route test traffic after an Amazon ECS
                deployment. Validation can occur while test traffic is served during a deployment.

                - **listenerArns** *(list) --*

                  The ARN of one listener. The listener identifies the route between a target group
                  and a load balancer. This is an array of strings with a maximum size of one.

                  - *(string) --*

        :type ec2TagSet: dict
        :param ec2TagSet:

          Information about groups of tags applied to on-premises instances. The deployment group
          includes only EC2 instances identified by all the tag groups.

          - **ec2TagSetList** *(list) --*

            A list that contains other lists of EC2 instance tag groups. For an instance to be
            included in the deployment group, it must be identified by all of the tag groups in the
            list.

            - *(list) --*

              - *(dict) --*

                Information about an EC2 tag filter.

                - **Key** *(string) --*

                  The tag filter key.

                - **Value** *(string) --*

                  The tag filter value.

                - **Type** *(string) --*

                  The tag filter type:

                  * KEY_ONLY: Key only.

                  * VALUE_ONLY: Value only.

                  * KEY_AND_VALUE: Key and value.

        :type ecsServices: list
        :param ecsServices:

          The target Amazon ECS services in the deployment group. This applies only to deployment
          groups that use the Amazon ECS compute platform. A target Amazon ECS service is specified
          as an Amazon ECS cluster and service name pair using the format
          ``<clustername>:<servicename>`` .

          - *(dict) --*

            Contains the service and cluster names used to identify an Amazon ECS deployment's
            target.

            - **serviceName** *(string) --*

              The name of the target Amazon ECS service.

            - **clusterName** *(string) --*

              The name of the cluster that the Amazon ECS service is associated with.

        :type onPremisesTagSet: dict
        :param onPremisesTagSet:

          Information about an on-premises instance tag set. The deployment group includes only
          on-premises instances identified by all the tag groups.

          - **onPremisesTagSetList** *(list) --*

            A list that contains other lists of on-premises instance tag groups. For an instance to
            be included in the deployment group, it must be identified by all of the tag groups in
            the list.

            - *(list) --*

              - *(dict) --*

                Information about an on-premises instance tag filter.

                - **Key** *(string) --*

                  The on-premises instance tag filter key.

                - **Value** *(string) --*

                  The on-premises instance tag filter value.

                - **Type** *(string) --*

                  The on-premises instance tag filter type:

                  * KEY_ONLY: Key only.

                  * VALUE_ONLY: Value only.

                  * KEY_AND_VALUE: Key and value.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'hooksNotCleanedUp': [
                    {
                        'name': 'string',
                        'hook': 'string'
                    },
                ]
            }
          **Response Structure**

          - *(dict) --*

            Represents the output of an UpdateDeploymentGroup operation.

            - **hooksNotCleanedUp** *(list) --*

              If the output contains no data, and the corresponding deployment group contained at
              least one Auto Scaling group, AWS CodeDeploy successfully removed all corresponding
              Auto Scaling lifecycle event hooks from the AWS account. If the output contains data,
              AWS CodeDeploy could not remove some Auto Scaling lifecycle event hooks from the AWS
              account.

              - *(dict) --*

                Information about an Auto Scaling group.

                - **name** *(string) --*

                  The Auto Scaling group name.

                - **hook** *(string) --*

                  An Auto Scaling lifecycle event hook name.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_application_revisions"]
    ) -> paginator_scope.ListApplicationRevisionsPaginator:
        """
        Get Paginator for `list_application_revisions` operation.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_applications"]
    ) -> paginator_scope.ListApplicationsPaginator:
        """
        Get Paginator for `list_applications` operation.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_deployment_configs"]
    ) -> paginator_scope.ListDeploymentConfigsPaginator:
        """
        Get Paginator for `list_deployment_configs` operation.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_deployment_groups"]
    ) -> paginator_scope.ListDeploymentGroupsPaginator:
        """
        Get Paginator for `list_deployment_groups` operation.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_deployment_instances"]
    ) -> paginator_scope.ListDeploymentInstancesPaginator:
        """
        Get Paginator for `list_deployment_instances` operation.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_deployment_targets"]
    ) -> paginator_scope.ListDeploymentTargetsPaginator:
        """
        Get Paginator for `list_deployment_targets` operation.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_deployments"]
    ) -> paginator_scope.ListDeploymentsPaginator:
        """
        Get Paginator for `list_deployments` operation.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_git_hub_account_token_names"]
    ) -> paginator_scope.ListGitHubAccountTokenNamesPaginator:
        """
        Get Paginator for `list_git_hub_account_token_names` operation.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_on_premises_instances"]
    ) -> paginator_scope.ListOnPremisesInstancesPaginator:
        """
        Get Paginator for `list_on_premises_instances` operation.
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

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_waiter(
        self, waiter_name: Literal["deployment_successful"]
    ) -> waiter_scope.DeploymentSuccessfulWaiter:
        """
        Get Waiter `deployment_successful`.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_waiter(self, waiter_name: str) -> Boto3Waiter:
        """
        Returns an object that can wait for some condition.

        :type waiter_name: str
        :param waiter_name: The name of the waiter to get. See the waiters
            section of the service docs for a list of available waiters.

        :returns: The specified waiter object.
        :rtype: botocore.waiter.Waiter
        """


class Exceptions:
    AlarmsLimitExceededException: Boto3ClientError
    ApplicationAlreadyExistsException: Boto3ClientError
    ApplicationDoesNotExistException: Boto3ClientError
    ApplicationLimitExceededException: Boto3ClientError
    ApplicationNameRequiredException: Boto3ClientError
    ArnNotSupportedException: Boto3ClientError
    BatchLimitExceededException: Boto3ClientError
    BucketNameFilterRequiredException: Boto3ClientError
    ClientError: Boto3ClientError
    DeploymentAlreadyCompletedException: Boto3ClientError
    DeploymentAlreadyStartedException: Boto3ClientError
    DeploymentConfigAlreadyExistsException: Boto3ClientError
    DeploymentConfigDoesNotExistException: Boto3ClientError
    DeploymentConfigInUseException: Boto3ClientError
    DeploymentConfigLimitExceededException: Boto3ClientError
    DeploymentConfigNameRequiredException: Boto3ClientError
    DeploymentDoesNotExistException: Boto3ClientError
    DeploymentGroupAlreadyExistsException: Boto3ClientError
    DeploymentGroupDoesNotExistException: Boto3ClientError
    DeploymentGroupLimitExceededException: Boto3ClientError
    DeploymentGroupNameRequiredException: Boto3ClientError
    DeploymentIdRequiredException: Boto3ClientError
    DeploymentIsNotInReadyStateException: Boto3ClientError
    DeploymentLimitExceededException: Boto3ClientError
    DeploymentNotStartedException: Boto3ClientError
    DeploymentTargetDoesNotExistException: Boto3ClientError
    DeploymentTargetIdRequiredException: Boto3ClientError
    DeploymentTargetListSizeExceededException: Boto3ClientError
    DescriptionTooLongException: Boto3ClientError
    ECSServiceMappingLimitExceededException: Boto3ClientError
    GitHubAccountTokenDoesNotExistException: Boto3ClientError
    GitHubAccountTokenNameRequiredException: Boto3ClientError
    IamArnRequiredException: Boto3ClientError
    IamSessionArnAlreadyRegisteredException: Boto3ClientError
    IamUserArnAlreadyRegisteredException: Boto3ClientError
    IamUserArnRequiredException: Boto3ClientError
    InstanceDoesNotExistException: Boto3ClientError
    InstanceIdRequiredException: Boto3ClientError
    InstanceLimitExceededException: Boto3ClientError
    InstanceNameAlreadyRegisteredException: Boto3ClientError
    InstanceNameRequiredException: Boto3ClientError
    InstanceNotRegisteredException: Boto3ClientError
    InvalidAlarmConfigException: Boto3ClientError
    InvalidApplicationNameException: Boto3ClientError
    InvalidArnException: Boto3ClientError
    InvalidAutoRollbackConfigException: Boto3ClientError
    InvalidAutoScalingGroupException: Boto3ClientError
    InvalidBlueGreenDeploymentConfigurationException: Boto3ClientError
    InvalidBucketNameFilterException: Boto3ClientError
    InvalidComputePlatformException: Boto3ClientError
    InvalidDeployedStateFilterException: Boto3ClientError
    InvalidDeploymentConfigIdException: Boto3ClientError
    InvalidDeploymentConfigNameException: Boto3ClientError
    InvalidDeploymentGroupNameException: Boto3ClientError
    InvalidDeploymentIdException: Boto3ClientError
    InvalidDeploymentInstanceTypeException: Boto3ClientError
    InvalidDeploymentStatusException: Boto3ClientError
    InvalidDeploymentStyleException: Boto3ClientError
    InvalidDeploymentTargetIdException: Boto3ClientError
    InvalidDeploymentWaitTypeException: Boto3ClientError
    InvalidEC2TagCombinationException: Boto3ClientError
    InvalidEC2TagException: Boto3ClientError
    InvalidECSServiceException: Boto3ClientError
    InvalidFileExistsBehaviorException: Boto3ClientError
    InvalidGitHubAccountTokenException: Boto3ClientError
    InvalidGitHubAccountTokenNameException: Boto3ClientError
    InvalidIamSessionArnException: Boto3ClientError
    InvalidIamUserArnException: Boto3ClientError
    InvalidIgnoreApplicationStopFailuresValueException: Boto3ClientError
    InvalidInputException: Boto3ClientError
    InvalidInstanceIdException: Boto3ClientError
    InvalidInstanceNameException: Boto3ClientError
    InvalidInstanceStatusException: Boto3ClientError
    InvalidInstanceTypeException: Boto3ClientError
    InvalidKeyPrefixFilterException: Boto3ClientError
    InvalidLifecycleEventHookExecutionIdException: Boto3ClientError
    InvalidLifecycleEventHookExecutionStatusException: Boto3ClientError
    InvalidLoadBalancerInfoException: Boto3ClientError
    InvalidMinimumHealthyHostValueException: Boto3ClientError
    InvalidNextTokenException: Boto3ClientError
    InvalidOnPremisesTagCombinationException: Boto3ClientError
    InvalidOperationException: Boto3ClientError
    InvalidRegistrationStatusException: Boto3ClientError
    InvalidRevisionException: Boto3ClientError
    InvalidRoleException: Boto3ClientError
    InvalidSortByException: Boto3ClientError
    InvalidSortOrderException: Boto3ClientError
    InvalidTagException: Boto3ClientError
    InvalidTagFilterException: Boto3ClientError
    InvalidTagsToAddException: Boto3ClientError
    InvalidTargetException: Boto3ClientError
    InvalidTargetFilterNameException: Boto3ClientError
    InvalidTargetGroupPairException: Boto3ClientError
    InvalidTargetInstancesException: Boto3ClientError
    InvalidTimeRangeException: Boto3ClientError
    InvalidTrafficRoutingConfigurationException: Boto3ClientError
    InvalidTriggerConfigException: Boto3ClientError
    InvalidUpdateOutdatedInstancesOnlyValueException: Boto3ClientError
    LifecycleEventAlreadyCompletedException: Boto3ClientError
    LifecycleHookLimitExceededException: Boto3ClientError
    MultipleIamArnsProvidedException: Boto3ClientError
    OperationNotSupportedException: Boto3ClientError
    ResourceArnRequiredException: Boto3ClientError
    ResourceValidationException: Boto3ClientError
    RevisionDoesNotExistException: Boto3ClientError
    RevisionRequiredException: Boto3ClientError
    RoleRequiredException: Boto3ClientError
    TagLimitExceededException: Boto3ClientError
    TagRequiredException: Boto3ClientError
    TagSetListLimitExceededException: Boto3ClientError
    ThrottlingException: Boto3ClientError
    TriggerTargetsLimitExceededException: Boto3ClientError
    UnsupportedActionForDeploymentTypeException: Boto3ClientError
