"Main interface for mediastore service Client"
from __future__ import annotations

from typing import Any, Dict, List
from botocore.client import BaseClient
from botocore.exceptions import ClientError as Boto3ClientError
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3.type_defs import Literal, overload

# pylint: disable=import-self
import mypy_boto3_mediastore.client as client_scope

# pylint: disable=import-self
import mypy_boto3_mediastore.paginator as paginator_scope
from mypy_boto3_mediastore.type_defs import (
    ClientCreateContainerResponseTypeDef,
    ClientCreateContainerTagsTypeDef,
    ClientDescribeContainerResponseTypeDef,
    ClientGetContainerPolicyResponseTypeDef,
    ClientGetCorsPolicyResponseTypeDef,
    ClientGetLifecyclePolicyResponseTypeDef,
    ClientListContainersResponseTypeDef,
    ClientListTagsForResourceResponseTypeDef,
    ClientPutCorsPolicyCorsPolicyTypeDef,
    ClientTagResourceTagsTypeDef,
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
    def create_container(
        self, ContainerName: str, Tags: List[ClientCreateContainerTagsTypeDef] = None
    ) -> ClientCreateContainerResponseTypeDef:
        """
        Creates a storage container to hold objects. A container is similar to a bucket in the
        Amazon S3 service.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/mediastore-2017-09-01/CreateContainer>`_

        **Request Syntax**
        ::

          response = client.create_container(
              ContainerName='string',
              Tags=[
                  {
                      'Key': 'string',
                      'Value': 'string'
                  },
              ]
          )
        :type ContainerName: string
        :param ContainerName: **[REQUIRED]**

          The name for the container. The name must be from 1 to 255 characters. Container names
          must be unique to your AWS account within a specific region. As an example, you could
          create a container named ``movies`` in every region, as long as you don’t have an existing
          container with that name.

        :type Tags: list
        :param Tags:

          An array of key:value pairs that you define. These values can be anything that you want.
          Typically, the tag key represents a category (such as "environment") and the tag value
          represents a specific value within that category (such as "test," "development," or
          "production"). You can add up to 50 tags to each container. For more information about
          tagging, including naming and usage conventions, see `Tagging Resources in MediaStore
          <https://docs.aws.amazon.com/mediastore/latest/ug/tagging.html>`__ .

          - *(dict) --*

            A collection of tags associated with a container. Each tag consists of a key:value pair,
            which can be anything you define. Typically, the tag key represents a category (such as
            "environment") and the tag value represents a specific value within that category (such
            as "test," "development," or "production"). You can add up to 50 tags to each container.
            For more information about tagging, including naming and usage conventions, see `Tagging
            Resources in MediaStore
            <https://docs.aws.amazon.com/mediastore/latest/ug/tagging.html>`__ .

            - **Key** *(string) --* **[REQUIRED]**

              Part of the key:value pair that defines a tag. You can use a tag key to describe a
              category of information, such as "customer." Tag keys are case-sensitive.

            - **Value** *(string) --*

              Part of the key:value pair that defines a tag. You can use a tag value to describe a
              specific value within a category, such as "companyA" or "companyB." Tag values are
              case-sensitive.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Container': {
                    'Endpoint': 'string',
                    'CreationTime': datetime(2015, 1, 1),
                    'ARN': 'string',
                    'Name': 'string',
                    'Status': 'ACTIVE'|'CREATING'|'DELETING',
                    'AccessLoggingEnabled': True|False
                }
            }
          **Response Structure**

          - *(dict) --*

            - **Container** *(dict) --*

              ContainerARN: The Amazon Resource Name (ARN) of the newly created container. The ARN
              has the following format: arn:aws:<region>:<account that owns this
              container>:container/<name of container>. For example:
              arn:aws:mediastore:us-west-2:111122223333:container/movies

              ContainerName: The container name as specified in the request.

              CreationTime: Unix time stamp.

              Status: The status of container creation or deletion. The status is one of the
              following: ``CREATING`` , ``ACTIVE`` , or ``DELETING`` . While the service is creating
              the container, the status is ``CREATING`` . When an endpoint is available, the status
              changes to ``ACTIVE`` .

              The return value does not include the container's endpoint. To make downstream
              requests, you must obtain this value by using  DescribeContainer or  ListContainers .

              - **Endpoint** *(string) --*

                The DNS endpoint of the container. Use the endpoint to identify the specific
                container when sending requests to the data plane. The service assigns this value
                when the container is created. Once the value has been assigned, it does not change.

              - **CreationTime** *(datetime) --*

                Unix timestamp.

              - **ARN** *(string) --*

                The Amazon Resource Name (ARN) of the container. The ARN has the following format:

                arn:aws:<region>:<account that owns this container>:container/<name of container>

                For example: arn:aws:mediastore:us-west-2:111122223333:container/movies

              - **Name** *(string) --*

                The name of the container.

              - **Status** *(string) --*

                The status of container creation or deletion. The status is one of the following:
                ``CREATING`` , ``ACTIVE`` , or ``DELETING`` . While the service is creating the
                container, the status is ``CREATING`` . When the endpoint is available, the status
                changes to ``ACTIVE`` .

              - **AccessLoggingEnabled** *(boolean) --*

                The state of access logging on the container. This value is ``false`` by default,
                indicating that AWS Elemental MediaStore does not send access logs to Amazon
                CloudWatch Logs. When you enable access logging on the container, MediaStore changes
                this value to ``true`` , indicating that the service delivers access logs for
                objects stored in that container to CloudWatch Logs.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_container(self, ContainerName: str) -> Dict[str, Any]:
        """
        Deletes the specified container. Before you make a ``DeleteContainer`` request, delete any
        objects in the container or in any folders in the container. You can delete only empty
        containers.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/mediastore-2017-09-01/DeleteContainer>`_

        **Request Syntax**
        ::

          response = client.delete_container(
              ContainerName='string'
          )
        :type ContainerName: string
        :param ContainerName: **[REQUIRED]**

          The name of the container to delete.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {}
          **Response Structure**

          - *(dict) --*
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_container_policy(self, ContainerName: str) -> Dict[str, Any]:
        """
        Deletes the access policy that is associated with the specified container.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/mediastore-2017-09-01/DeleteContainerPolicy>`_

        **Request Syntax**
        ::

          response = client.delete_container_policy(
              ContainerName='string'
          )
        :type ContainerName: string
        :param ContainerName: **[REQUIRED]**

          The name of the container that holds the policy.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {}
          **Response Structure**

          - *(dict) --*
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_cors_policy(self, ContainerName: str) -> Dict[str, Any]:
        """
        Deletes the cross-origin resource sharing (CORS) configuration information that is set for
        the container.

        To use this operation, you must have permission to perform the
        ``MediaStore:DeleteCorsPolicy`` action. The container owner has this permission by default
        and can grant this permission to others.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/mediastore-2017-09-01/DeleteCorsPolicy>`_

        **Request Syntax**
        ::

          response = client.delete_cors_policy(
              ContainerName='string'
          )
        :type ContainerName: string
        :param ContainerName: **[REQUIRED]**

          The name of the container to remove the policy from.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {}
          **Response Structure**

          - *(dict) --*
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_lifecycle_policy(self, ContainerName: str) -> Dict[str, Any]:
        """
        Removes an object lifecycle policy from a container. It takes up to 20 minutes for the
        change to take effect.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/mediastore-2017-09-01/DeleteLifecyclePolicy>`_

        **Request Syntax**
        ::

          response = client.delete_lifecycle_policy(
              ContainerName='string'
          )
        :type ContainerName: string
        :param ContainerName: **[REQUIRED]**

          The name of the container that holds the object lifecycle policy.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {}
          **Response Structure**

          - *(dict) --*
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_container(
        self, ContainerName: str = None
    ) -> ClientDescribeContainerResponseTypeDef:
        """
        Retrieves the properties of the requested container. This request is commonly used to
        retrieve the endpoint of a container. An endpoint is a value assigned by the service when a
        new container is created. A container's endpoint does not change after it has been assigned.
        The ``DescribeContainer`` request returns a single ``Container`` object based on
        ``ContainerName`` . To return all ``Container`` objects that are associated with a specified
        AWS account, use  ListContainers .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/mediastore-2017-09-01/DescribeContainer>`_

        **Request Syntax**
        ::

          response = client.describe_container(
              ContainerName='string'
          )
        :type ContainerName: string
        :param ContainerName:

          The name of the container to query.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Container': {
                    'Endpoint': 'string',
                    'CreationTime': datetime(2015, 1, 1),
                    'ARN': 'string',
                    'Name': 'string',
                    'Status': 'ACTIVE'|'CREATING'|'DELETING',
                    'AccessLoggingEnabled': True|False
                }
            }
          **Response Structure**

          - *(dict) --*

            - **Container** *(dict) --*

              The name of the queried container.

              - **Endpoint** *(string) --*

                The DNS endpoint of the container. Use the endpoint to identify the specific
                container when sending requests to the data plane. The service assigns this value
                when the container is created. Once the value has been assigned, it does not change.

              - **CreationTime** *(datetime) --*

                Unix timestamp.

              - **ARN** *(string) --*

                The Amazon Resource Name (ARN) of the container. The ARN has the following format:

                arn:aws:<region>:<account that owns this container>:container/<name of container>

                For example: arn:aws:mediastore:us-west-2:111122223333:container/movies

              - **Name** *(string) --*

                The name of the container.

              - **Status** *(string) --*

                The status of container creation or deletion. The status is one of the following:
                ``CREATING`` , ``ACTIVE`` , or ``DELETING`` . While the service is creating the
                container, the status is ``CREATING`` . When the endpoint is available, the status
                changes to ``ACTIVE`` .

              - **AccessLoggingEnabled** *(boolean) --*

                The state of access logging on the container. This value is ``false`` by default,
                indicating that AWS Elemental MediaStore does not send access logs to Amazon
                CloudWatch Logs. When you enable access logging on the container, MediaStore changes
                this value to ``true`` , indicating that the service delivers access logs for
                objects stored in that container to CloudWatch Logs.
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
    def get_container_policy(self, ContainerName: str) -> ClientGetContainerPolicyResponseTypeDef:
        """
        Retrieves the access policy for the specified container. For information about the data that
        is included in an access policy, see the `AWS Identity and Access Management User Guide
        <https://aws.amazon.com/documentation/iam/>`__ .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/mediastore-2017-09-01/GetContainerPolicy>`_

        **Request Syntax**
        ::

          response = client.get_container_policy(
              ContainerName='string'
          )
        :type ContainerName: string
        :param ContainerName: **[REQUIRED]**

          The name of the container.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Policy': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **Policy** *(string) --*

              The contents of the access policy.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_cors_policy(self, ContainerName: str) -> ClientGetCorsPolicyResponseTypeDef:
        """
        Returns the cross-origin resource sharing (CORS) configuration information that is set for
        the container.

        To use this operation, you must have permission to perform the ``MediaStore:GetCorsPolicy``
        action. By default, the container owner has this permission and can grant it to others.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/mediastore-2017-09-01/GetCorsPolicy>`_

        **Request Syntax**
        ::

          response = client.get_cors_policy(
              ContainerName='string'
          )
        :type ContainerName: string
        :param ContainerName: **[REQUIRED]**

          The name of the container that the policy is assigned to.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'CorsPolicy': [
                    {
                        'AllowedOrigins': [
                            'string',
                        ],
                        'AllowedMethods': [
                            'PUT'|'GET'|'DELETE'|'HEAD',
                        ],
                        'AllowedHeaders': [
                            'string',
                        ],
                        'MaxAgeSeconds': 123,
                        'ExposeHeaders': [
                            'string',
                        ]
                    },
                ]
            }
          **Response Structure**

          - *(dict) --*

            - **CorsPolicy** *(list) --*

              The CORS policy assigned to the container.

              - *(dict) --*

                A rule for a CORS policy. You can add up to 100 rules to a CORS policy. If more than
                one rule applies, the service uses the first applicable rule listed.

                - **AllowedOrigins** *(list) --*

                  One or more response headers that you want users to be able to access from their
                  applications (for example, from a JavaScript ``XMLHttpRequest`` object).

                  Each CORS rule must have at least one ``AllowedOrigins`` element. The string value
                  can include only one wildcard character (*), for example, http://*.example.com.
                  Additionally, you can specify only one wildcard character to allow cross-origin
                  access for all origins.

                  - *(string) --*

                - **AllowedMethods** *(list) --*

                  Identifies an HTTP method that the origin that is specified in the rule is allowed
                  to execute.

                  Each CORS rule must contain at least one ``AllowedMethods`` and one
                  ``AllowedOrigins`` element.

                  - *(string) --*

                - **AllowedHeaders** *(list) --*

                  Specifies which headers are allowed in a preflight ``OPTIONS`` request through the
                  ``Access-Control-Request-Headers`` header. Each header name that is specified in
                  ``Access-Control-Request-Headers`` must have a corresponding entry in the rule.
                  Only the headers that were requested are sent back.

                  This element can contain only one wildcard character (*).

                  - *(string) --*

                - **MaxAgeSeconds** *(integer) --*

                  The time in seconds that your browser caches the preflight response for the
                  specified resource.

                  A CORS rule can have only one ``MaxAgeSeconds`` element.

                - **ExposeHeaders** *(list) --*

                  One or more headers in the response that you want users to be able to access from
                  their applications (for example, from a JavaScript ``XMLHttpRequest`` object).

                  This element is optional for each rule.

                  - *(string) --*
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_lifecycle_policy(self, ContainerName: str) -> ClientGetLifecyclePolicyResponseTypeDef:
        """
        Retrieves the object lifecycle policy that is assigned to a container.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/mediastore-2017-09-01/GetLifecyclePolicy>`_

        **Request Syntax**
        ::

          response = client.get_lifecycle_policy(
              ContainerName='string'
          )
        :type ContainerName: string
        :param ContainerName: **[REQUIRED]**

          The name of the container that the object lifecycle policy is assigned to.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'LifecyclePolicy': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **LifecyclePolicy** *(string) --*

              The object lifecycle policy that is assigned to the container.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_containers(
        self, NextToken: str = None, MaxResults: int = None
    ) -> ClientListContainersResponseTypeDef:
        """
        Lists the properties of all containers in AWS Elemental MediaStore.

        You can query to receive all the containers in one response. Or you can include the
        ``MaxResults`` parameter to receive a limited number of containers in each response. In this
        case, the response includes a token. To get the next set of containers, send the command
        again, this time with the ``NextToken`` parameter (with the returned token as its value).
        The next set of responses appears, with a token if there are still more containers to
        receive.

        See also  DescribeContainer , which gets the properties of one container.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/mediastore-2017-09-01/ListContainers>`_

        **Request Syntax**
        ::

          response = client.list_containers(
              NextToken='string',
              MaxResults=123
          )
        :type NextToken: string
        :param NextToken:

          Only if you used ``MaxResults`` in the first command, enter the token (which was included
          in the previous response) to obtain the next set of containers. This token is included in
          a response only if there actually are more containers to list.

        :type MaxResults: integer
        :param MaxResults:

          Enter the maximum number of containers in the response. Use from 1 to 255 characters.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Containers': [
                    {
                        'Endpoint': 'string',
                        'CreationTime': datetime(2015, 1, 1),
                        'ARN': 'string',
                        'Name': 'string',
                        'Status': 'ACTIVE'|'CREATING'|'DELETING',
                        'AccessLoggingEnabled': True|False
                    },
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **Containers** *(list) --*

              The names of the containers.

              - *(dict) --*

                This section describes operations that you can perform on an AWS Elemental
                MediaStore container.

                - **Endpoint** *(string) --*

                  The DNS endpoint of the container. Use the endpoint to identify the specific
                  container when sending requests to the data plane. The service assigns this value
                  when the container is created. Once the value has been assigned, it does not
                  change.

                - **CreationTime** *(datetime) --*

                  Unix timestamp.

                - **ARN** *(string) --*

                  The Amazon Resource Name (ARN) of the container. The ARN has the following format:

                  arn:aws:<region>:<account that owns this container>:container/<name of container>

                  For example: arn:aws:mediastore:us-west-2:111122223333:container/movies

                - **Name** *(string) --*

                  The name of the container.

                - **Status** *(string) --*

                  The status of container creation or deletion. The status is one of the following:
                  ``CREATING`` , ``ACTIVE`` , or ``DELETING`` . While the service is creating the
                  container, the status is ``CREATING`` . When the endpoint is available, the status
                  changes to ``ACTIVE`` .

                - **AccessLoggingEnabled** *(boolean) --*

                  The state of access logging on the container. This value is ``false`` by default,
                  indicating that AWS Elemental MediaStore does not send access logs to Amazon
                  CloudWatch Logs. When you enable access logging on the container, MediaStore
                  changes this value to ``true`` , indicating that the service delivers access logs
                  for objects stored in that container to CloudWatch Logs.

            - **NextToken** *(string) --*

               ``NextToken`` is the token to use in the next call to ``ListContainers`` . This token
               is returned only if you included the ``MaxResults`` tag in the original command, and
               only if there are still containers to return.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_tags_for_resource(self, Resource: str) -> ClientListTagsForResourceResponseTypeDef:
        """
        Returns a list of the tags assigned to the specified container.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/mediastore-2017-09-01/ListTagsForResource>`_

        **Request Syntax**
        ::

          response = client.list_tags_for_resource(
              Resource='string'
          )
        :type Resource: string
        :param Resource: **[REQUIRED]**

          The Amazon Resource Name (ARN) for the container.

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
                ]
            }
          **Response Structure**

          - *(dict) --*

            - **Tags** *(list) --*

              An array of key:value pairs that are assigned to the container.

              - *(dict) --*

                A collection of tags associated with a container. Each tag consists of a key:value
                pair, which can be anything you define. Typically, the tag key represents a category
                (such as "environment") and the tag value represents a specific value within that
                category (such as "test," "development," or "production"). You can add up to 50 tags
                to each container. For more information about tagging, including naming and usage
                conventions, see `Tagging Resources in MediaStore
                <https://docs.aws.amazon.com/mediastore/latest/ug/tagging.html>`__ .

                - **Key** *(string) --*

                  Part of the key:value pair that defines a tag. You can use a tag key to describe a
                  category of information, such as "customer." Tag keys are case-sensitive.

                - **Value** *(string) --*

                  Part of the key:value pair that defines a tag. You can use a tag value to describe
                  a specific value within a category, such as "companyA" or "companyB." Tag values
                  are case-sensitive.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def put_container_policy(self, ContainerName: str, Policy: str) -> Dict[str, Any]:
        """
        Creates an access policy for the specified container to restrict the users and clients that
        can access it. For information about the data that is included in an access policy, see the
        `AWS Identity and Access Management User Guide
        <https://aws.amazon.com/documentation/iam/>`__ .

        For this release of the REST API, you can create only one policy for a container. If you
        enter ``PutContainerPolicy`` twice, the second command modifies the existing policy.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/mediastore-2017-09-01/PutContainerPolicy>`_

        **Request Syntax**
        ::

          response = client.put_container_policy(
              ContainerName='string',
              Policy='string'
          )
        :type ContainerName: string
        :param ContainerName: **[REQUIRED]**

          The name of the container.

        :type Policy: string
        :param Policy: **[REQUIRED]**

          The contents of the policy, which includes the following:

          * One ``Version`` tag

          * One ``Statement`` tag that contains the standard tags for the policy.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {}
          **Response Structure**

          - *(dict) --*
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def put_cors_policy(
        self, ContainerName: str, CorsPolicy: List[ClientPutCorsPolicyCorsPolicyTypeDef]
    ) -> Dict[str, Any]:
        """
        Sets the cross-origin resource sharing (CORS) configuration on a container so that the
        container can service cross-origin requests. For example, you might want to enable a request
        whose origin is http://www.example.com to access your AWS Elemental MediaStore container at
        my.example.container.com by using the browser's XMLHttpRequest capability.

        To enable CORS on a container, you attach a CORS policy to the container. In the CORS
        policy, you configure rules that identify origins and the HTTP methods that can be executed
        on your container. The policy can contain up to 398,000 characters. You can add up to 100
        rules to a CORS policy. If more than one rule applies, the service uses the first applicable
        rule listed.

        To learn more about CORS, see `Cross-Origin Resource Sharing (CORS) in AWS Elemental
        MediaStore <https://docs.aws.amazon.com/mediastore/latest/ug/cors-policy.html>`__ .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/mediastore-2017-09-01/PutCorsPolicy>`_

        **Request Syntax**
        ::

          response = client.put_cors_policy(
              ContainerName='string',
              CorsPolicy=[
                  {
                      'AllowedOrigins': [
                          'string',
                      ],
                      'AllowedMethods': [
                          'PUT'|'GET'|'DELETE'|'HEAD',
                      ],
                      'AllowedHeaders': [
                          'string',
                      ],
                      'MaxAgeSeconds': 123,
                      'ExposeHeaders': [
                          'string',
                      ]
                  },
              ]
          )
        :type ContainerName: string
        :param ContainerName: **[REQUIRED]**

          The name of the container that you want to assign the CORS policy to.

        :type CorsPolicy: list
        :param CorsPolicy: **[REQUIRED]**

          The CORS policy to apply to the container.

          - *(dict) --*

            A rule for a CORS policy. You can add up to 100 rules to a CORS policy. If more than one
            rule applies, the service uses the first applicable rule listed.

            - **AllowedOrigins** *(list) --* **[REQUIRED]**

              One or more response headers that you want users to be able to access from their
              applications (for example, from a JavaScript ``XMLHttpRequest`` object).

              Each CORS rule must have at least one ``AllowedOrigins`` element. The string value can
              include only one wildcard character (*), for example, http://*.example.com.
              Additionally, you can specify only one wildcard character to allow cross-origin access
              for all origins.

              - *(string) --*

            - **AllowedMethods** *(list) --*

              Identifies an HTTP method that the origin that is specified in the rule is allowed to
              execute.

              Each CORS rule must contain at least one ``AllowedMethods`` and one ``AllowedOrigins``
              element.

              - *(string) --*

            - **AllowedHeaders** *(list) --* **[REQUIRED]**

              Specifies which headers are allowed in a preflight ``OPTIONS`` request through the
              ``Access-Control-Request-Headers`` header. Each header name that is specified in
              ``Access-Control-Request-Headers`` must have a corresponding entry in the rule. Only
              the headers that were requested are sent back.

              This element can contain only one wildcard character (*).

              - *(string) --*

            - **MaxAgeSeconds** *(integer) --*

              The time in seconds that your browser caches the preflight response for the specified
              resource.

              A CORS rule can have only one ``MaxAgeSeconds`` element.

            - **ExposeHeaders** *(list) --*

              One or more headers in the response that you want users to be able to access from
              their applications (for example, from a JavaScript ``XMLHttpRequest`` object).

              This element is optional for each rule.

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
    def put_lifecycle_policy(self, ContainerName: str, LifecyclePolicy: str) -> Dict[str, Any]:
        """
        Writes an object lifecycle policy to a container. If the container already has an object
        lifecycle policy, the service replaces the existing policy with the new policy. It takes up
        to 20 minutes for the change to take effect.

        For information about how to construct an object lifecycle policy, see `Components of an
        Object Lifecycle Policy
        <https://docs.aws.amazon.com/mediastore/latest/ug/policies-object-lifecycle-components.html>`__
        .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/mediastore-2017-09-01/PutLifecyclePolicy>`_

        **Request Syntax**
        ::

          response = client.put_lifecycle_policy(
              ContainerName='string',
              LifecyclePolicy='string'
          )
        :type ContainerName: string
        :param ContainerName: **[REQUIRED]**

          The name of the container that you want to assign the object lifecycle policy to.

        :type LifecyclePolicy: string
        :param LifecyclePolicy: **[REQUIRED]**

          The object lifecycle policy to apply to the container.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {}
          **Response Structure**

          - *(dict) --*
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def start_access_logging(self, ContainerName: str) -> Dict[str, Any]:
        """
        Starts access logging on the specified container. When you enable access logging on a
        container, MediaStore delivers access logs for objects stored in that container to Amazon
        CloudWatch Logs.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/mediastore-2017-09-01/StartAccessLogging>`_

        **Request Syntax**
        ::

          response = client.start_access_logging(
              ContainerName='string'
          )
        :type ContainerName: string
        :param ContainerName: **[REQUIRED]**

          The name of the container that you want to start access logging on.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {}
          **Response Structure**

          - *(dict) --*
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def stop_access_logging(self, ContainerName: str) -> Dict[str, Any]:
        """
        Stops access logging on the specified container. When you stop access logging on a
        container, MediaStore stops sending access logs to Amazon CloudWatch Logs. These access logs
        are not saved and are not retrievable.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/mediastore-2017-09-01/StopAccessLogging>`_

        **Request Syntax**
        ::

          response = client.stop_access_logging(
              ContainerName='string'
          )
        :type ContainerName: string
        :param ContainerName: **[REQUIRED]**

          The name of the container that you want to stop access logging on.

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
        self, Resource: str, Tags: List[ClientTagResourceTagsTypeDef]
    ) -> Dict[str, Any]:
        """
        Adds tags to the specified AWS Elemental MediaStore container. Tags are key:value pairs that
        you can associate with AWS resources. For example, the tag key might be "customer" and the
        tag value might be "companyA." You can specify one or more tags to add to each container.
        You can add up to 50 tags to each container. For more information about tagging, including
        naming and usage conventions, see `Tagging Resources in MediaStore
        <https://docs.aws.amazon.com/mediastore/latest/ug/tagging.html>`__ .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/mediastore-2017-09-01/TagResource>`_

        **Request Syntax**
        ::

          response = client.tag_resource(
              Resource='string',
              Tags=[
                  {
                      'Key': 'string',
                      'Value': 'string'
                  },
              ]
          )
        :type Resource: string
        :param Resource: **[REQUIRED]**

          The Amazon Resource Name (ARN) for the container.

        :type Tags: list
        :param Tags: **[REQUIRED]**

          An array of key:value pairs that you want to add to the container. You need to specify
          only the tags that you want to add or update. For example, suppose a container already has
          two tags (customer:CompanyA and priority:High). You want to change the priority tag and
          also add a third tag (type:Contract). For TagResource, you specify the following tags:
          priority:Medium, type:Contract. The result is that your container has three tags:
          customer:CompanyA, priority:Medium, and type:Contract.

          - *(dict) --*

            A collection of tags associated with a container. Each tag consists of a key:value pair,
            which can be anything you define. Typically, the tag key represents a category (such as
            "environment") and the tag value represents a specific value within that category (such
            as "test," "development," or "production"). You can add up to 50 tags to each container.
            For more information about tagging, including naming and usage conventions, see `Tagging
            Resources in MediaStore
            <https://docs.aws.amazon.com/mediastore/latest/ug/tagging.html>`__ .

            - **Key** *(string) --* **[REQUIRED]**

              Part of the key:value pair that defines a tag. You can use a tag key to describe a
              category of information, such as "customer." Tag keys are case-sensitive.

            - **Value** *(string) --*

              Part of the key:value pair that defines a tag. You can use a tag value to describe a
              specific value within a category, such as "companyA" or "companyB." Tag values are
              case-sensitive.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {}
          **Response Structure**

          - *(dict) --*
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def untag_resource(self, Resource: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        Removes tags from the specified container. You can specify one or more tags to remove.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/mediastore-2017-09-01/UntagResource>`_

        **Request Syntax**
        ::

          response = client.untag_resource(
              Resource='string',
              TagKeys=[
                  'string',
              ]
          )
        :type Resource: string
        :param Resource: **[REQUIRED]**

          The Amazon Resource Name (ARN) for the container.

        :type TagKeys: list
        :param TagKeys: **[REQUIRED]**

          A comma-separated list of keys for tags that you want to remove from the container. For
          example, if your container has two tags (customer:CompanyA and priority:High) and you want
          to remove one of the tags (priority:High), you specify the key for the tag that you want
          to remove (priority).

          - *(string) --*

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
        self, operation_name: Literal["list_containers"]
    ) -> paginator_scope.ListContainersPaginator:
        """
        Get Paginator for `list_containers` operation.
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
    ContainerInUseException: Boto3ClientError
    ContainerNotFoundException: Boto3ClientError
    CorsPolicyNotFoundException: Boto3ClientError
    InternalServerError: Boto3ClientError
    LimitExceededException: Boto3ClientError
    PolicyNotFoundException: Boto3ClientError
