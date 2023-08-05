"Main interface for mediaconnect service Client"
from __future__ import annotations

from typing import Any, Dict, List
from botocore.client import BaseClient
from botocore.exceptions import ClientError as Boto3ClientError
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3.type_defs import Literal, overload

# pylint: disable=import-self
import mypy_boto3_mediaconnect.client as client_scope

# pylint: disable=import-self
import mypy_boto3_mediaconnect.paginator as paginator_scope
from mypy_boto3_mediaconnect.type_defs import (
    ClientAddFlowOutputsOutputsTypeDef,
    ClientAddFlowOutputsResponseTypeDef,
    ClientCreateFlowEntitlementsTypeDef,
    ClientCreateFlowOutputsTypeDef,
    ClientCreateFlowResponseTypeDef,
    ClientCreateFlowSourceTypeDef,
    ClientDeleteFlowResponseTypeDef,
    ClientDescribeFlowResponseTypeDef,
    ClientGrantFlowEntitlementsEntitlementsTypeDef,
    ClientGrantFlowEntitlementsResponseTypeDef,
    ClientListEntitlementsResponseTypeDef,
    ClientListFlowsResponseTypeDef,
    ClientListTagsForResourceResponseTypeDef,
    ClientRemoveFlowOutputResponseTypeDef,
    ClientRevokeFlowEntitlementResponseTypeDef,
    ClientStartFlowResponseTypeDef,
    ClientStopFlowResponseTypeDef,
    ClientUpdateFlowEntitlementEncryptionTypeDef,
    ClientUpdateFlowEntitlementResponseTypeDef,
    ClientUpdateFlowOutputEncryptionTypeDef,
    ClientUpdateFlowOutputResponseTypeDef,
    ClientUpdateFlowSourceDecryptionTypeDef,
    ClientUpdateFlowSourceResponseTypeDef,
)


__all__ = ("Client",)


class Client(BaseClient):
    exceptions: client_scope.Exceptions

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def add_flow_outputs(
        self, FlowArn: str, Outputs: List[ClientAddFlowOutputsOutputsTypeDef]
    ) -> ClientAddFlowOutputsResponseTypeDef:
        """
        Adds outputs to an existing flow. You can create up to 20 outputs per flow.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/mediaconnect-2018-11-14/AddFlowOutputs>`_

        **Request Syntax**
        ::

          response = client.add_flow_outputs(
              FlowArn='string',
              Outputs=[
                  {
                      'CidrAllowList': [
                          'string',
                      ],
                      'Description': 'string',
                      'Destination': 'string',
                      'Encryption': {
                          'Algorithm': 'aes128'|'aes192'|'aes256',
                          'ConstantInitializationVector': 'string',
                          'DeviceId': 'string',
                          'KeyType': 'speke'|'static-key',
                          'Region': 'string',
                          'ResourceId': 'string',
                          'RoleArn': 'string',
                          'SecretArn': 'string',
                          'Url': 'string'
                      },
                      'MaxLatency': 123,
                      'Name': 'string',
                      'Port': 123,
                      'Protocol': 'zixi-push'|'rtp-fec'|'rtp'|'zixi-pull'|'rist',
                      'RemoteId': 'string',
                      'SmoothingLatency': 123,
                      'StreamId': 'string'
                  },
              ]
          )
        :type FlowArn: string
        :param FlowArn: **[REQUIRED]** The flow that you want to add outputs to.

        :type Outputs: list
        :param Outputs: **[REQUIRED]** A list of outputs that you want to add.

          - *(dict) --* The output that you want to add to this flow.

            - **CidrAllowList** *(list) --* The range of IP addresses that should be allowed to
            initiate output requests to this flow. These IP addresses should be in the form of a
            Classless Inter-Domain Routing (CIDR) block; for example, 10.0.0.0/16.

              - *(string) --*

            - **Description** *(string) --* A description of the output. This description appears
            only on the AWS Elemental MediaConnect console and will not be seen by the end user.

            - **Destination** *(string) --* The IP address from which video will be sent to output
            destinations.

            - **Encryption** *(dict) --* The type of key used for the encryption. If no keyType is
            provided, the service will use the default setting (static-key).

              - **Algorithm** *(string) --* **[REQUIRED]** The type of algorithm that is used for
              the encryption (such as aes128, aes192, or aes256).

              - **ConstantInitializationVector** *(string) --* A 128-bit, 16-byte hex value
              represented by a 32-character string, to be used with the key for encrypting content.
              This parameter is not valid for static key encryption.

              - **DeviceId** *(string) --* The value of one of the devices that you configured with
              your digital rights management (DRM) platform key provider. This parameter is required
              for SPEKE encryption and is not valid for static key encryption.

              - **KeyType** *(string) --* The type of key that is used for the encryption. If no
              keyType is provided, the service will use the default setting (static-key).

              - **Region** *(string) --* The AWS Region that the API Gateway proxy endpoint was
              created in. This parameter is required for SPEKE encryption and is not valid for
              static key encryption.

              - **ResourceId** *(string) --* An identifier for the content. The service sends this
              value to the key server to identify the current endpoint. The resource ID is also
              known as the content ID. This parameter is required for SPEKE encryption and is not
              valid for static key encryption.

              - **RoleArn** *(string) --* **[REQUIRED]** The ARN of the role that you created during
              setup (when you set up AWS Elemental MediaConnect as a trusted entity).

              - **SecretArn** *(string) --* The ARN of the secret that you created in AWS Secrets
              Manager to store the encryption key. This parameter is required for static key
              encryption and is not valid for SPEKE encryption.

              - **Url** *(string) --* The URL from the API Gateway proxy that you set up to talk to
              your key server. This parameter is required for SPEKE encryption and is not valid for
              static key encryption.

            - **MaxLatency** *(integer) --* The maximum latency in milliseconds for Zixi-based
            streams.

            - **Name** *(string) --* The name of the output. This value must be unique within the
            current flow.

            - **Port** *(integer) --* The port to use when content is distributed to this output.

            - **Protocol** *(string) --* **[REQUIRED]** The protocol to use for the output.

            - **RemoteId** *(string) --* The remote ID for the Zixi-pull output stream.

            - **SmoothingLatency** *(integer) --* The smoothing latency in milliseconds for RIST,
            RTP, and RTP-FEC streams.

            - **StreamId** *(string) --* The stream ID that you want to use for this transport. This
            parameter applies only to Zixi-based streams.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'FlowArn': 'string',
                'Outputs': [
                    {
                        'DataTransferSubscriberFeePercent': 123,
                        'Description': 'string',
                        'Destination': 'string',
                        'Encryption': {
                            'Algorithm': 'aes128'|'aes192'|'aes256',
                            'ConstantInitializationVector': 'string',
                            'DeviceId': 'string',
                            'KeyType': 'speke'|'static-key',
                            'Region': 'string',
                            'ResourceId': 'string',
                            'RoleArn': 'string',
                            'SecretArn': 'string',
                            'Url': 'string'
                        },
                        'EntitlementArn': 'string',
                        'MediaLiveInputArn': 'string',
                        'Name': 'string',
                        'OutputArn': 'string',
                        'Port': 123,
                        'Transport': {
                            'CidrAllowList': [
                                'string',
                            ],
                            'MaxBitrate': 123,
                            'MaxLatency': 123,
                            'Protocol': 'zixi-push'|'rtp-fec'|'rtp'|'zixi-pull'|'rist',
                            'RemoteId': 'string',
                            'SmoothingLatency': 123,
                            'StreamId': 'string'
                        }
                    },
                ]
            }
          **Response Structure**

          - *(dict) --* AWS Elemental MediaConnect added the outputs successfully.

            - **FlowArn** *(string) --* The ARN of the flow that these outputs were added to.

            - **Outputs** *(list) --* The details of the newly added outputs.

              - *(dict) --* The settings for an output.

                - **DataTransferSubscriberFeePercent** *(integer) --* Percentage from 0-100 of the
                data transfer cost to be billed to the subscriber.

                - **Description** *(string) --* A description of the output.

                - **Destination** *(string) --* The address where you want to send the output.

                - **Encryption** *(dict) --* The type of key used for the encryption. If no keyType
                is provided, the service will use the default setting (static-key).

                  - **Algorithm** *(string) --* The type of algorithm that is used for the
                  encryption (such as aes128, aes192, or aes256).

                  - **ConstantInitializationVector** *(string) --* A 128-bit, 16-byte hex value
                  represented by a 32-character string, to be used with the key for encrypting
                  content. This parameter is not valid for static key encryption.

                  - **DeviceId** *(string) --* The value of one of the devices that you configured
                  with your digital rights management (DRM) platform key provider. This parameter is
                  required for SPEKE encryption and is not valid for static key encryption.

                  - **KeyType** *(string) --* The type of key that is used for the encryption. If no
                  keyType is provided, the service will use the default setting (static-key).

                  - **Region** *(string) --* The AWS Region that the API Gateway proxy endpoint was
                  created in. This parameter is required for SPEKE encryption and is not valid for
                  static key encryption.

                  - **ResourceId** *(string) --* An identifier for the content. The service sends
                  this value to the key server to identify the current endpoint. The resource ID is
                  also known as the content ID. This parameter is required for SPEKE encryption and
                  is not valid for static key encryption.

                  - **RoleArn** *(string) --* The ARN of the role that you created during setup
                  (when you set up AWS Elemental MediaConnect as a trusted entity).

                  - **SecretArn** *(string) --* The ARN of the secret that you created in AWS
                  Secrets Manager to store the encryption key. This parameter is required for static
                  key encryption and is not valid for SPEKE encryption.

                  - **Url** *(string) --* The URL from the API Gateway proxy that you set up to talk
                  to your key server. This parameter is required for SPEKE encryption and is not
                  valid for static key encryption.

                - **EntitlementArn** *(string) --* The ARN of the entitlement on the originator''s
                flow. This value is relevant only on entitled flows.

                - **MediaLiveInputArn** *(string) --* The input ARN of the AWS Elemental MediaLive
                channel. This parameter is relevant only for outputs that were added by creating a
                MediaLive input.

                - **Name** *(string) --* The name of the output. This value must be unique within
                the current flow.

                - **OutputArn** *(string) --* The ARN of the output.

                - **Port** *(integer) --* The port to use when content is distributed to this
                output.

                - **Transport** *(dict) --* Attributes related to the transport stream that are used
                in the output.

                  - **CidrAllowList** *(list) --* The range of IP addresses that should be allowed
                  to initiate output requests to this flow. These IP addresses should be in the form
                  of a Classless Inter-Domain Routing (CIDR) block; for example, 10.0.0.0/16.

                    - *(string) --*

                  - **MaxBitrate** *(integer) --* The smoothing max bitrate for RIST, RTP, and
                  RTP-FEC streams.

                  - **MaxLatency** *(integer) --* The maximum latency in milliseconds. This
                  parameter applies only to RIST-based and Zixi-based streams.

                  - **Protocol** *(string) --* The protocol that is used by the source or output.

                  - **RemoteId** *(string) --* The remote ID for the Zixi-pull stream.

                  - **SmoothingLatency** *(integer) --* The smoothing latency in milliseconds for
                  RIST, RTP, and RTP-FEC streams.

                  - **StreamId** *(string) --* The stream ID that you want to use for this
                  transport. This parameter applies only to Zixi-based streams.
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
    def create_flow(
        self,
        Name: str,
        Source: ClientCreateFlowSourceTypeDef,
        AvailabilityZone: str = None,
        Entitlements: List[ClientCreateFlowEntitlementsTypeDef] = None,
        Outputs: List[ClientCreateFlowOutputsTypeDef] = None,
    ) -> ClientCreateFlowResponseTypeDef:
        """
        Creates a new flow. The request must include one source. The request optionally can include
        outputs (up to 20) and entitlements (up to 50).

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/mediaconnect-2018-11-14/CreateFlow>`_

        **Request Syntax**
        ::

          response = client.create_flow(
              AvailabilityZone='string',
              Entitlements=[
                  {
                      'DataTransferSubscriberFeePercent': 123,
                      'Description': 'string',
                      'Encryption': {
                          'Algorithm': 'aes128'|'aes192'|'aes256',
                          'ConstantInitializationVector': 'string',
                          'DeviceId': 'string',
                          'KeyType': 'speke'|'static-key',
                          'Region': 'string',
                          'ResourceId': 'string',
                          'RoleArn': 'string',
                          'SecretArn': 'string',
                          'Url': 'string'
                      },
                      'Name': 'string',
                      'Subscribers': [
                          'string',
                      ]
                  },
              ],
              Name='string',
              Outputs=[
                  {
                      'CidrAllowList': [
                          'string',
                      ],
                      'Description': 'string',
                      'Destination': 'string',
                      'Encryption': {
                          'Algorithm': 'aes128'|'aes192'|'aes256',
                          'ConstantInitializationVector': 'string',
                          'DeviceId': 'string',
                          'KeyType': 'speke'|'static-key',
                          'Region': 'string',
                          'ResourceId': 'string',
                          'RoleArn': 'string',
                          'SecretArn': 'string',
                          'Url': 'string'
                      },
                      'MaxLatency': 123,
                      'Name': 'string',
                      'Port': 123,
                      'Protocol': 'zixi-push'|'rtp-fec'|'rtp'|'zixi-pull'|'rist',
                      'RemoteId': 'string',
                      'SmoothingLatency': 123,
                      'StreamId': 'string'
                  },
              ],
              Source={
                  'Decryption': {
                      'Algorithm': 'aes128'|'aes192'|'aes256',
                      'ConstantInitializationVector': 'string',
                      'DeviceId': 'string',
                      'KeyType': 'speke'|'static-key',
                      'Region': 'string',
                      'ResourceId': 'string',
                      'RoleArn': 'string',
                      'SecretArn': 'string',
                      'Url': 'string'
                  },
                  'Description': 'string',
                  'EntitlementArn': 'string',
                  'IngestPort': 123,
                  'MaxBitrate': 123,
                  'MaxLatency': 123,
                  'Name': 'string',
                  'Protocol': 'zixi-push'|'rtp-fec'|'rtp'|'zixi-pull'|'rist',
                  'StreamId': 'string',
                  'WhitelistCidr': 'string'
              }
          )
        :type AvailabilityZone: string
        :param AvailabilityZone: The Availability Zone that you want to create the flow in. These
        options are limited to the Availability Zones within the current AWS Region.

        :type Entitlements: list
        :param Entitlements: The entitlements that you want to grant on a flow.

          - *(dict) --* The entitlements that you want to grant on a flow.

            - **DataTransferSubscriberFeePercent** *(integer) --* Percentage from 0-100 of the data
            transfer cost to be billed to the subscriber.

            - **Description** *(string) --* A description of the entitlement. This description
            appears only on the AWS Elemental MediaConnect console and will not be seen by the
            subscriber or end user.

            - **Encryption** *(dict) --* The type of encryption that will be used on the output that
            is associated with this entitlement.

              - **Algorithm** *(string) --* **[REQUIRED]** The type of algorithm that is used for
              the encryption (such as aes128, aes192, or aes256).

              - **ConstantInitializationVector** *(string) --* A 128-bit, 16-byte hex value
              represented by a 32-character string, to be used with the key for encrypting content.
              This parameter is not valid for static key encryption.

              - **DeviceId** *(string) --* The value of one of the devices that you configured with
              your digital rights management (DRM) platform key provider. This parameter is required
              for SPEKE encryption and is not valid for static key encryption.

              - **KeyType** *(string) --* The type of key that is used for the encryption. If no
              keyType is provided, the service will use the default setting (static-key).

              - **Region** *(string) --* The AWS Region that the API Gateway proxy endpoint was
              created in. This parameter is required for SPEKE encryption and is not valid for
              static key encryption.

              - **ResourceId** *(string) --* An identifier for the content. The service sends this
              value to the key server to identify the current endpoint. The resource ID is also
              known as the content ID. This parameter is required for SPEKE encryption and is not
              valid for static key encryption.

              - **RoleArn** *(string) --* **[REQUIRED]** The ARN of the role that you created during
              setup (when you set up AWS Elemental MediaConnect as a trusted entity).

              - **SecretArn** *(string) --* The ARN of the secret that you created in AWS Secrets
              Manager to store the encryption key. This parameter is required for static key
              encryption and is not valid for SPEKE encryption.

              - **Url** *(string) --* The URL from the API Gateway proxy that you set up to talk to
              your key server. This parameter is required for SPEKE encryption and is not valid for
              static key encryption.

            - **Name** *(string) --* The name of the entitlement. This value must be unique within
            the current flow.

            - **Subscribers** *(list) --* **[REQUIRED]** The AWS account IDs that you want to share
            your content with. The receiving accounts (subscribers) will be allowed to create their
            own flows using your content as the source.

              - *(string) --*

        :type Name: string
        :param Name: **[REQUIRED]** The name of the flow.

        :type Outputs: list
        :param Outputs: The outputs that you want to add to this flow.

          - *(dict) --* The output that you want to add to this flow.

            - **CidrAllowList** *(list) --* The range of IP addresses that should be allowed to
            initiate output requests to this flow. These IP addresses should be in the form of a
            Classless Inter-Domain Routing (CIDR) block; for example, 10.0.0.0/16.

              - *(string) --*

            - **Description** *(string) --* A description of the output. This description appears
            only on the AWS Elemental MediaConnect console and will not be seen by the end user.

            - **Destination** *(string) --* The IP address from which video will be sent to output
            destinations.

            - **Encryption** *(dict) --* The type of key used for the encryption. If no keyType is
            provided, the service will use the default setting (static-key).

              - **Algorithm** *(string) --* **[REQUIRED]** The type of algorithm that is used for
              the encryption (such as aes128, aes192, or aes256).

              - **ConstantInitializationVector** *(string) --* A 128-bit, 16-byte hex value
              represented by a 32-character string, to be used with the key for encrypting content.
              This parameter is not valid for static key encryption.

              - **DeviceId** *(string) --* The value of one of the devices that you configured with
              your digital rights management (DRM) platform key provider. This parameter is required
              for SPEKE encryption and is not valid for static key encryption.

              - **KeyType** *(string) --* The type of key that is used for the encryption. If no
              keyType is provided, the service will use the default setting (static-key).

              - **Region** *(string) --* The AWS Region that the API Gateway proxy endpoint was
              created in. This parameter is required for SPEKE encryption and is not valid for
              static key encryption.

              - **ResourceId** *(string) --* An identifier for the content. The service sends this
              value to the key server to identify the current endpoint. The resource ID is also
              known as the content ID. This parameter is required for SPEKE encryption and is not
              valid for static key encryption.

              - **RoleArn** *(string) --* **[REQUIRED]** The ARN of the role that you created during
              setup (when you set up AWS Elemental MediaConnect as a trusted entity).

              - **SecretArn** *(string) --* The ARN of the secret that you created in AWS Secrets
              Manager to store the encryption key. This parameter is required for static key
              encryption and is not valid for SPEKE encryption.

              - **Url** *(string) --* The URL from the API Gateway proxy that you set up to talk to
              your key server. This parameter is required for SPEKE encryption and is not valid for
              static key encryption.

            - **MaxLatency** *(integer) --* The maximum latency in milliseconds for Zixi-based
            streams.

            - **Name** *(string) --* The name of the output. This value must be unique within the
            current flow.

            - **Port** *(integer) --* The port to use when content is distributed to this output.

            - **Protocol** *(string) --* **[REQUIRED]** The protocol to use for the output.

            - **RemoteId** *(string) --* The remote ID for the Zixi-pull output stream.

            - **SmoothingLatency** *(integer) --* The smoothing latency in milliseconds for RIST,
            RTP, and RTP-FEC streams.

            - **StreamId** *(string) --* The stream ID that you want to use for this transport. This
            parameter applies only to Zixi-based streams.

        :type Source: dict
        :param Source: **[REQUIRED]** The settings for the source of the flow.

          - **Decryption** *(dict) --* The type of encryption that is used on the content ingested
          from this source.

            - **Algorithm** *(string) --* **[REQUIRED]** The type of algorithm that is used for the
            encryption (such as aes128, aes192, or aes256).

            - **ConstantInitializationVector** *(string) --* A 128-bit, 16-byte hex value
            represented by a 32-character string, to be used with the key for encrypting content.
            This parameter is not valid for static key encryption.

            - **DeviceId** *(string) --* The value of one of the devices that you configured with
            your digital rights management (DRM) platform key provider. This parameter is required
            for SPEKE encryption and is not valid for static key encryption.

            - **KeyType** *(string) --* The type of key that is used for the encryption. If no
            keyType is provided, the service will use the default setting (static-key).

            - **Region** *(string) --* The AWS Region that the API Gateway proxy endpoint was
            created in. This parameter is required for SPEKE encryption and is not valid for static
            key encryption.

            - **ResourceId** *(string) --* An identifier for the content. The service sends this
            value to the key server to identify the current endpoint. The resource ID is also known
            as the content ID. This parameter is required for SPEKE encryption and is not valid for
            static key encryption.

            - **RoleArn** *(string) --* **[REQUIRED]** The ARN of the role that you created during
            setup (when you set up AWS Elemental MediaConnect as a trusted entity).

            - **SecretArn** *(string) --* The ARN of the secret that you created in AWS Secrets
            Manager to store the encryption key. This parameter is required for static key
            encryption and is not valid for SPEKE encryption.

            - **Url** *(string) --* The URL from the API Gateway proxy that you set up to talk to
            your key server. This parameter is required for SPEKE encryption and is not valid for
            static key encryption.

          - **Description** *(string) --* A description for the source. This value is not used or
          seen outside of the current AWS Elemental MediaConnect account.

          - **EntitlementArn** *(string) --* The ARN of the entitlement that allows you to subscribe
          to this flow. The entitlement is set by the flow originator, and the ARN is generated as
          part of the originator's flow.

          - **IngestPort** *(integer) --* The port that the flow will be listening on for incoming
          content.

          - **MaxBitrate** *(integer) --* The smoothing max bitrate for RIST, RTP, and RTP-FEC
          streams.

          - **MaxLatency** *(integer) --* The maximum latency in milliseconds. This parameter
          applies only to RIST-based and Zixi-based streams.

          - **Name** *(string) --* The name of the source.

          - **Protocol** *(string) --* The protocol that is used by the source.

          - **StreamId** *(string) --* The stream ID that you want to use for this transport. This
          parameter applies only to Zixi-based streams.

          - **WhitelistCidr** *(string) --* The range of IP addresses that should be allowed to
          contribute content to your source. These IP addresses should be in the form of a Classless
          Inter-Domain Routing (CIDR) block; for example, 10.0.0.0/16.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Flow': {
                    'AvailabilityZone': 'string',
                    'Description': 'string',
                    'EgressIp': 'string',
                    'Entitlements': [
                        {
                            'DataTransferSubscriberFeePercent': 123,
                            'Description': 'string',
                            'Encryption': {
                                'Algorithm': 'aes128'|'aes192'|'aes256',
                                'ConstantInitializationVector': 'string',
                                'DeviceId': 'string',
                                'KeyType': 'speke'|'static-key',
                                'Region': 'string',
                                'ResourceId': 'string',
                                'RoleArn': 'string',
                                'SecretArn': 'string',
                                'Url': 'string'
                            },
                            'EntitlementArn': 'string',
                            'Name': 'string',
                            'Subscribers': [
                                'string',
                            ]
                        },
                    ],
                    'FlowArn': 'string',
                    'Name': 'string',
                    'Outputs': [
                        {
                            'DataTransferSubscriberFeePercent': 123,
                            'Description': 'string',
                            'Destination': 'string',
                            'Encryption': {
                                'Algorithm': 'aes128'|'aes192'|'aes256',
                                'ConstantInitializationVector': 'string',
                                'DeviceId': 'string',
                                'KeyType': 'speke'|'static-key',
                                'Region': 'string',
                                'ResourceId': 'string',
                                'RoleArn': 'string',
                                'SecretArn': 'string',
                                'Url': 'string'
                            },
                            'EntitlementArn': 'string',
                            'MediaLiveInputArn': 'string',
                            'Name': 'string',
                            'OutputArn': 'string',
                            'Port': 123,
                            'Transport': {
                                'CidrAllowList': [
                                    'string',
                                ],
                                'MaxBitrate': 123,
                                'MaxLatency': 123,
                                'Protocol': 'zixi-push'|'rtp-fec'|'rtp'|'zixi-pull'|'rist',
                                'RemoteId': 'string',
                                'SmoothingLatency': 123,
                                'StreamId': 'string'
                            }
                        },
                    ],
                    'Source': {
                        'DataTransferSubscriberFeePercent': 123,
                        'Decryption': {
                            'Algorithm': 'aes128'|'aes192'|'aes256',
                            'ConstantInitializationVector': 'string',
                            'DeviceId': 'string',
                            'KeyType': 'speke'|'static-key',
                            'Region': 'string',
                            'ResourceId': 'string',
                            'RoleArn': 'string',
                            'SecretArn': 'string',
                            'Url': 'string'
                        },
                        'Description': 'string',
                        'EntitlementArn': 'string',
                        'IngestIp': 'string',
                        'IngestPort': 123,
                        'Name': 'string',
                        'SourceArn': 'string',
                        'Transport': {
                            'CidrAllowList': [
                                'string',
                            ],
                            'MaxBitrate': 123,
                            'MaxLatency': 123,
                            'Protocol': 'zixi-push'|'rtp-fec'|'rtp'|'zixi-pull'|'rist',
                            'RemoteId': 'string',
                            'SmoothingLatency': 123,
                            'StreamId': 'string'
                        },
                        'WhitelistCidr': 'string'
                    },
                    'Status': 'STANDBY'|'ACTIVE'|'UPDATING'|'DELETING'|'STARTING'|'STOPPING'|'ERROR'
                }
            }
          **Response Structure**

          - *(dict) --* AWS Elemental MediaConnect created the new flow successfully.

            - **Flow** *(dict) --* The settings for a flow, including its source, outputs, and
            entitlements.

              - **AvailabilityZone** *(string) --* The Availability Zone that you want to create the
              flow in. These options are limited to the Availability Zones within the current AWS.

              - **Description** *(string) --* A description of the flow. This value is not used or
              seen outside of the current AWS Elemental MediaConnect account.

              - **EgressIp** *(string) --* The IP address from which video will be sent to output
              destinations.

              - **Entitlements** *(list) --* The entitlements in this flow.

                - *(dict) --* The settings for a flow entitlement.

                  - **DataTransferSubscriberFeePercent** *(integer) --* Percentage from 0-100 of the
                  data transfer cost to be billed to the subscriber.

                  - **Description** *(string) --* A description of the entitlement.

                  - **Encryption** *(dict) --* The type of encryption that will be used on the
                  output that is associated with this entitlement.

                    - **Algorithm** *(string) --* The type of algorithm that is used for the
                    encryption (such as aes128, aes192, or aes256).

                    - **ConstantInitializationVector** *(string) --* A 128-bit, 16-byte hex value
                    represented by a 32-character string, to be used with the key for encrypting
                    content. This parameter is not valid for static key encryption.

                    - **DeviceId** *(string) --* The value of one of the devices that you configured
                    with your digital rights management (DRM) platform key provider. This parameter
                    is required for SPEKE encryption and is not valid for static key encryption.

                    - **KeyType** *(string) --* The type of key that is used for the encryption. If
                    no keyType is provided, the service will use the default setting (static-key).

                    - **Region** *(string) --* The AWS Region that the API Gateway proxy endpoint
                    was created in. This parameter is required for SPEKE encryption and is not valid
                    for static key encryption.

                    - **ResourceId** *(string) --* An identifier for the content. The service sends
                    this value to the key server to identify the current endpoint. The resource ID
                    is also known as the content ID. This parameter is required for SPEKE encryption
                    and is not valid for static key encryption.

                    - **RoleArn** *(string) --* The ARN of the role that you created during setup
                    (when you set up AWS Elemental MediaConnect as a trusted entity).

                    - **SecretArn** *(string) --* The ARN of the secret that you created in AWS
                    Secrets Manager to store the encryption key. This parameter is required for
                    static key encryption and is not valid for SPEKE encryption.

                    - **Url** *(string) --* The URL from the API Gateway proxy that you set up to
                    talk to your key server. This parameter is required for SPEKE encryption and is
                    not valid for static key encryption.

                  - **EntitlementArn** *(string) --* The ARN of the entitlement.

                  - **Name** *(string) --* The name of the entitlement.

                  - **Subscribers** *(list) --* The AWS account IDs that you want to share your
                  content with. The receiving accounts (subscribers) will be allowed to create their
                  own flow using your content as the source.

                    - *(string) --*

              - **FlowArn** *(string) --* The Amazon Resource Name (ARN), a unique identifier for
              any AWS resource, of the flow.

              - **Name** *(string) --* The name of the flow.

              - **Outputs** *(list) --* The outputs in this flow.

                - *(dict) --* The settings for an output.

                  - **DataTransferSubscriberFeePercent** *(integer) --* Percentage from 0-100 of the
                  data transfer cost to be billed to the subscriber.

                  - **Description** *(string) --* A description of the output.

                  - **Destination** *(string) --* The address where you want to send the output.

                  - **Encryption** *(dict) --* The type of key used for the encryption. If no
                  keyType is provided, the service will use the default setting (static-key).

                    - **Algorithm** *(string) --* The type of algorithm that is used for the
                    encryption (such as aes128, aes192, or aes256).

                    - **ConstantInitializationVector** *(string) --* A 128-bit, 16-byte hex value
                    represented by a 32-character string, to be used with the key for encrypting
                    content. This parameter is not valid for static key encryption.

                    - **DeviceId** *(string) --* The value of one of the devices that you configured
                    with your digital rights management (DRM) platform key provider. This parameter
                    is required for SPEKE encryption and is not valid for static key encryption.

                    - **KeyType** *(string) --* The type of key that is used for the encryption. If
                    no keyType is provided, the service will use the default setting (static-key).

                    - **Region** *(string) --* The AWS Region that the API Gateway proxy endpoint
                    was created in. This parameter is required for SPEKE encryption and is not valid
                    for static key encryption.

                    - **ResourceId** *(string) --* An identifier for the content. The service sends
                    this value to the key server to identify the current endpoint. The resource ID
                    is also known as the content ID. This parameter is required for SPEKE encryption
                    and is not valid for static key encryption.

                    - **RoleArn** *(string) --* The ARN of the role that you created during setup
                    (when you set up AWS Elemental MediaConnect as a trusted entity).

                    - **SecretArn** *(string) --* The ARN of the secret that you created in AWS
                    Secrets Manager to store the encryption key. This parameter is required for
                    static key encryption and is not valid for SPEKE encryption.

                    - **Url** *(string) --* The URL from the API Gateway proxy that you set up to
                    talk to your key server. This parameter is required for SPEKE encryption and is
                    not valid for static key encryption.

                  - **EntitlementArn** *(string) --* The ARN of the entitlement on the originator''s
                  flow. This value is relevant only on entitled flows.

                  - **MediaLiveInputArn** *(string) --* The input ARN of the AWS Elemental MediaLive
                  channel. This parameter is relevant only for outputs that were added by creating a
                  MediaLive input.

                  - **Name** *(string) --* The name of the output. This value must be unique within
                  the current flow.

                  - **OutputArn** *(string) --* The ARN of the output.

                  - **Port** *(integer) --* The port to use when content is distributed to this
                  output.

                  - **Transport** *(dict) --* Attributes related to the transport stream that are
                  used in the output.

                    - **CidrAllowList** *(list) --* The range of IP addresses that should be allowed
                    to initiate output requests to this flow. These IP addresses should be in the
                    form of a Classless Inter-Domain Routing (CIDR) block; for example, 10.0.0.0/16.

                      - *(string) --*

                    - **MaxBitrate** *(integer) --* The smoothing max bitrate for RIST, RTP, and
                    RTP-FEC streams.

                    - **MaxLatency** *(integer) --* The maximum latency in milliseconds. This
                    parameter applies only to RIST-based and Zixi-based streams.

                    - **Protocol** *(string) --* The protocol that is used by the source or output.

                    - **RemoteId** *(string) --* The remote ID for the Zixi-pull stream.

                    - **SmoothingLatency** *(integer) --* The smoothing latency in milliseconds for
                    RIST, RTP, and RTP-FEC streams.

                    - **StreamId** *(string) --* The stream ID that you want to use for this
                    transport. This parameter applies only to Zixi-based streams.

              - **Source** *(dict) --* The settings for the source of the flow.

                - **DataTransferSubscriberFeePercent** *(integer) --* Percentage from 0-100 of the
                data transfer cost to be billed to the subscriber.

                - **Decryption** *(dict) --* The type of encryption that is used on the content
                ingested from this source.

                  - **Algorithm** *(string) --* The type of algorithm that is used for the
                  encryption (such as aes128, aes192, or aes256).

                  - **ConstantInitializationVector** *(string) --* A 128-bit, 16-byte hex value
                  represented by a 32-character string, to be used with the key for encrypting
                  content. This parameter is not valid for static key encryption.

                  - **DeviceId** *(string) --* The value of one of the devices that you configured
                  with your digital rights management (DRM) platform key provider. This parameter is
                  required for SPEKE encryption and is not valid for static key encryption.

                  - **KeyType** *(string) --* The type of key that is used for the encryption. If no
                  keyType is provided, the service will use the default setting (static-key).

                  - **Region** *(string) --* The AWS Region that the API Gateway proxy endpoint was
                  created in. This parameter is required for SPEKE encryption and is not valid for
                  static key encryption.

                  - **ResourceId** *(string) --* An identifier for the content. The service sends
                  this value to the key server to identify the current endpoint. The resource ID is
                  also known as the content ID. This parameter is required for SPEKE encryption and
                  is not valid for static key encryption.

                  - **RoleArn** *(string) --* The ARN of the role that you created during setup
                  (when you set up AWS Elemental MediaConnect as a trusted entity).

                  - **SecretArn** *(string) --* The ARN of the secret that you created in AWS
                  Secrets Manager to store the encryption key. This parameter is required for static
                  key encryption and is not valid for SPEKE encryption.

                  - **Url** *(string) --* The URL from the API Gateway proxy that you set up to talk
                  to your key server. This parameter is required for SPEKE encryption and is not
                  valid for static key encryption.

                - **Description** *(string) --* A description for the source. This value is not used
                or seen outside of the current AWS Elemental MediaConnect account.

                - **EntitlementArn** *(string) --* The ARN of the entitlement that allows you to
                subscribe to content that comes from another AWS account. The entitlement is set by
                the content originator and the ARN is generated as part of the originator's flow.

                - **IngestIp** *(string) --* The IP address that the flow will be listening on for
                incoming content.

                - **IngestPort** *(integer) --* The port that the flow will be listening on for
                incoming content.

                - **Name** *(string) --* The name of the source.

                - **SourceArn** *(string) --* The ARN of the source.

                - **Transport** *(dict) --* Attributes related to the transport stream that are used
                in the source.

                  - **CidrAllowList** *(list) --* The range of IP addresses that should be allowed
                  to initiate output requests to this flow. These IP addresses should be in the form
                  of a Classless Inter-Domain Routing (CIDR) block; for example, 10.0.0.0/16.

                    - *(string) --*

                  - **MaxBitrate** *(integer) --* The smoothing max bitrate for RIST, RTP, and
                  RTP-FEC streams.

                  - **MaxLatency** *(integer) --* The maximum latency in milliseconds. This
                  parameter applies only to RIST-based and Zixi-based streams.

                  - **Protocol** *(string) --* The protocol that is used by the source or output.

                  - **RemoteId** *(string) --* The remote ID for the Zixi-pull stream.

                  - **SmoothingLatency** *(integer) --* The smoothing latency in milliseconds for
                  RIST, RTP, and RTP-FEC streams.

                  - **StreamId** *(string) --* The stream ID that you want to use for this
                  transport. This parameter applies only to Zixi-based streams.

                - **WhitelistCidr** *(string) --* The range of IP addresses that should be allowed
                to contribute content to your source. These IP addresses should be in the form of a
                Classless Inter-Domain Routing (CIDR) block; for example, 10.0.0.0/16.

              - **Status** *(string) --* The current status of the flow.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_flow(self, FlowArn: str) -> ClientDeleteFlowResponseTypeDef:
        """
        Deletes a flow. Before you can delete a flow, you must stop the flow.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/mediaconnect-2018-11-14/DeleteFlow>`_

        **Request Syntax**
        ::

          response = client.delete_flow(
              FlowArn='string'
          )
        :type FlowArn: string
        :param FlowArn: **[REQUIRED]** The ARN of the flow that you want to delete.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'FlowArn': 'string',
                'Status': 'STANDBY'|'ACTIVE'|'UPDATING'|'DELETING'|'STARTING'|'STOPPING'|'ERROR'
            }
          **Response Structure**

          - *(dict) --* AWS Elemental MediaConnect is deleting the flow.

            - **FlowArn** *(string) --* The ARN of the flow that was deleted.

            - **Status** *(string) --* The status of the flow when the DeleteFlow process begins.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_flow(self, FlowArn: str) -> ClientDescribeFlowResponseTypeDef:
        """
        Displays the details of a flow. The response includes the flow ARN, name, and Availability
        Zone, as well as details about the source, outputs, and entitlements.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/mediaconnect-2018-11-14/DescribeFlow>`_

        **Request Syntax**
        ::

          response = client.describe_flow(
              FlowArn='string'
          )
        :type FlowArn: string
        :param FlowArn: **[REQUIRED]** The ARN of the flow that you want to describe.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Flow': {
                    'AvailabilityZone': 'string',
                    'Description': 'string',
                    'EgressIp': 'string',
                    'Entitlements': [
                        {
                            'DataTransferSubscriberFeePercent': 123,
                            'Description': 'string',
                            'Encryption': {
                                'Algorithm': 'aes128'|'aes192'|'aes256',
                                'ConstantInitializationVector': 'string',
                                'DeviceId': 'string',
                                'KeyType': 'speke'|'static-key',
                                'Region': 'string',
                                'ResourceId': 'string',
                                'RoleArn': 'string',
                                'SecretArn': 'string',
                                'Url': 'string'
                            },
                            'EntitlementArn': 'string',
                            'Name': 'string',
                            'Subscribers': [
                                'string',
                            ]
                        },
                    ],
                    'FlowArn': 'string',
                    'Name': 'string',
                    'Outputs': [
                        {
                            'DataTransferSubscriberFeePercent': 123,
                            'Description': 'string',
                            'Destination': 'string',
                            'Encryption': {
                                'Algorithm': 'aes128'|'aes192'|'aes256',
                                'ConstantInitializationVector': 'string',
                                'DeviceId': 'string',
                                'KeyType': 'speke'|'static-key',
                                'Region': 'string',
                                'ResourceId': 'string',
                                'RoleArn': 'string',
                                'SecretArn': 'string',
                                'Url': 'string'
                            },
                            'EntitlementArn': 'string',
                            'MediaLiveInputArn': 'string',
                            'Name': 'string',
                            'OutputArn': 'string',
                            'Port': 123,
                            'Transport': {
                                'CidrAllowList': [
                                    'string',
                                ],
                                'MaxBitrate': 123,
                                'MaxLatency': 123,
                                'Protocol': 'zixi-push'|'rtp-fec'|'rtp'|'zixi-pull'|'rist',
                                'RemoteId': 'string',
                                'SmoothingLatency': 123,
                                'StreamId': 'string'
                            }
                        },
                    ],
                    'Source': {
                        'DataTransferSubscriberFeePercent': 123,
                        'Decryption': {
                            'Algorithm': 'aes128'|'aes192'|'aes256',
                            'ConstantInitializationVector': 'string',
                            'DeviceId': 'string',
                            'KeyType': 'speke'|'static-key',
                            'Region': 'string',
                            'ResourceId': 'string',
                            'RoleArn': 'string',
                            'SecretArn': 'string',
                            'Url': 'string'
                        },
                        'Description': 'string',
                        'EntitlementArn': 'string',
                        'IngestIp': 'string',
                        'IngestPort': 123,
                        'Name': 'string',
                        'SourceArn': 'string',
                        'Transport': {
                            'CidrAllowList': [
                                'string',
                            ],
                            'MaxBitrate': 123,
                            'MaxLatency': 123,
                            'Protocol': 'zixi-push'|'rtp-fec'|'rtp'|'zixi-pull'|'rist',
                            'RemoteId': 'string',
                            'SmoothingLatency': 123,
                            'StreamId': 'string'
                        },
                        'WhitelistCidr': 'string'
                    },
                    'Status': 'STANDBY'|'ACTIVE'|'UPDATING'|'DELETING'|'STARTING'|'STOPPING'|'ERROR'
                },
                'Messages': {
                    'Errors': [
                        'string',
                    ]
                }
            }
          **Response Structure**

          - *(dict) --* AWS Elemental MediaConnect returned the flow details successfully.

            - **Flow** *(dict) --* The settings for a flow, including its source, outputs, and
            entitlements.

              - **AvailabilityZone** *(string) --* The Availability Zone that you want to create the
              flow in. These options are limited to the Availability Zones within the current AWS.

              - **Description** *(string) --* A description of the flow. This value is not used or
              seen outside of the current AWS Elemental MediaConnect account.

              - **EgressIp** *(string) --* The IP address from which video will be sent to output
              destinations.

              - **Entitlements** *(list) --* The entitlements in this flow.

                - *(dict) --* The settings for a flow entitlement.

                  - **DataTransferSubscriberFeePercent** *(integer) --* Percentage from 0-100 of the
                  data transfer cost to be billed to the subscriber.

                  - **Description** *(string) --* A description of the entitlement.

                  - **Encryption** *(dict) --* The type of encryption that will be used on the
                  output that is associated with this entitlement.

                    - **Algorithm** *(string) --* The type of algorithm that is used for the
                    encryption (such as aes128, aes192, or aes256).

                    - **ConstantInitializationVector** *(string) --* A 128-bit, 16-byte hex value
                    represented by a 32-character string, to be used with the key for encrypting
                    content. This parameter is not valid for static key encryption.

                    - **DeviceId** *(string) --* The value of one of the devices that you configured
                    with your digital rights management (DRM) platform key provider. This parameter
                    is required for SPEKE encryption and is not valid for static key encryption.

                    - **KeyType** *(string) --* The type of key that is used for the encryption. If
                    no keyType is provided, the service will use the default setting (static-key).

                    - **Region** *(string) --* The AWS Region that the API Gateway proxy endpoint
                    was created in. This parameter is required for SPEKE encryption and is not valid
                    for static key encryption.

                    - **ResourceId** *(string) --* An identifier for the content. The service sends
                    this value to the key server to identify the current endpoint. The resource ID
                    is also known as the content ID. This parameter is required for SPEKE encryption
                    and is not valid for static key encryption.

                    - **RoleArn** *(string) --* The ARN of the role that you created during setup
                    (when you set up AWS Elemental MediaConnect as a trusted entity).

                    - **SecretArn** *(string) --* The ARN of the secret that you created in AWS
                    Secrets Manager to store the encryption key. This parameter is required for
                    static key encryption and is not valid for SPEKE encryption.

                    - **Url** *(string) --* The URL from the API Gateway proxy that you set up to
                    talk to your key server. This parameter is required for SPEKE encryption and is
                    not valid for static key encryption.

                  - **EntitlementArn** *(string) --* The ARN of the entitlement.

                  - **Name** *(string) --* The name of the entitlement.

                  - **Subscribers** *(list) --* The AWS account IDs that you want to share your
                  content with. The receiving accounts (subscribers) will be allowed to create their
                  own flow using your content as the source.

                    - *(string) --*

              - **FlowArn** *(string) --* The Amazon Resource Name (ARN), a unique identifier for
              any AWS resource, of the flow.

              - **Name** *(string) --* The name of the flow.

              - **Outputs** *(list) --* The outputs in this flow.

                - *(dict) --* The settings for an output.

                  - **DataTransferSubscriberFeePercent** *(integer) --* Percentage from 0-100 of the
                  data transfer cost to be billed to the subscriber.

                  - **Description** *(string) --* A description of the output.

                  - **Destination** *(string) --* The address where you want to send the output.

                  - **Encryption** *(dict) --* The type of key used for the encryption. If no
                  keyType is provided, the service will use the default setting (static-key).

                    - **Algorithm** *(string) --* The type of algorithm that is used for the
                    encryption (such as aes128, aes192, or aes256).

                    - **ConstantInitializationVector** *(string) --* A 128-bit, 16-byte hex value
                    represented by a 32-character string, to be used with the key for encrypting
                    content. This parameter is not valid for static key encryption.

                    - **DeviceId** *(string) --* The value of one of the devices that you configured
                    with your digital rights management (DRM) platform key provider. This parameter
                    is required for SPEKE encryption and is not valid for static key encryption.

                    - **KeyType** *(string) --* The type of key that is used for the encryption. If
                    no keyType is provided, the service will use the default setting (static-key).

                    - **Region** *(string) --* The AWS Region that the API Gateway proxy endpoint
                    was created in. This parameter is required for SPEKE encryption and is not valid
                    for static key encryption.

                    - **ResourceId** *(string) --* An identifier for the content. The service sends
                    this value to the key server to identify the current endpoint. The resource ID
                    is also known as the content ID. This parameter is required for SPEKE encryption
                    and is not valid for static key encryption.

                    - **RoleArn** *(string) --* The ARN of the role that you created during setup
                    (when you set up AWS Elemental MediaConnect as a trusted entity).

                    - **SecretArn** *(string) --* The ARN of the secret that you created in AWS
                    Secrets Manager to store the encryption key. This parameter is required for
                    static key encryption and is not valid for SPEKE encryption.

                    - **Url** *(string) --* The URL from the API Gateway proxy that you set up to
                    talk to your key server. This parameter is required for SPEKE encryption and is
                    not valid for static key encryption.

                  - **EntitlementArn** *(string) --* The ARN of the entitlement on the originator''s
                  flow. This value is relevant only on entitled flows.

                  - **MediaLiveInputArn** *(string) --* The input ARN of the AWS Elemental MediaLive
                  channel. This parameter is relevant only for outputs that were added by creating a
                  MediaLive input.

                  - **Name** *(string) --* The name of the output. This value must be unique within
                  the current flow.

                  - **OutputArn** *(string) --* The ARN of the output.

                  - **Port** *(integer) --* The port to use when content is distributed to this
                  output.

                  - **Transport** *(dict) --* Attributes related to the transport stream that are
                  used in the output.

                    - **CidrAllowList** *(list) --* The range of IP addresses that should be allowed
                    to initiate output requests to this flow. These IP addresses should be in the
                    form of a Classless Inter-Domain Routing (CIDR) block; for example, 10.0.0.0/16.

                      - *(string) --*

                    - **MaxBitrate** *(integer) --* The smoothing max bitrate for RIST, RTP, and
                    RTP-FEC streams.

                    - **MaxLatency** *(integer) --* The maximum latency in milliseconds. This
                    parameter applies only to RIST-based and Zixi-based streams.

                    - **Protocol** *(string) --* The protocol that is used by the source or output.

                    - **RemoteId** *(string) --* The remote ID for the Zixi-pull stream.

                    - **SmoothingLatency** *(integer) --* The smoothing latency in milliseconds for
                    RIST, RTP, and RTP-FEC streams.

                    - **StreamId** *(string) --* The stream ID that you want to use for this
                    transport. This parameter applies only to Zixi-based streams.

              - **Source** *(dict) --* The settings for the source of the flow.

                - **DataTransferSubscriberFeePercent** *(integer) --* Percentage from 0-100 of the
                data transfer cost to be billed to the subscriber.

                - **Decryption** *(dict) --* The type of encryption that is used on the content
                ingested from this source.

                  - **Algorithm** *(string) --* The type of algorithm that is used for the
                  encryption (such as aes128, aes192, or aes256).

                  - **ConstantInitializationVector** *(string) --* A 128-bit, 16-byte hex value
                  represented by a 32-character string, to be used with the key for encrypting
                  content. This parameter is not valid for static key encryption.

                  - **DeviceId** *(string) --* The value of one of the devices that you configured
                  with your digital rights management (DRM) platform key provider. This parameter is
                  required for SPEKE encryption and is not valid for static key encryption.

                  - **KeyType** *(string) --* The type of key that is used for the encryption. If no
                  keyType is provided, the service will use the default setting (static-key).

                  - **Region** *(string) --* The AWS Region that the API Gateway proxy endpoint was
                  created in. This parameter is required for SPEKE encryption and is not valid for
                  static key encryption.

                  - **ResourceId** *(string) --* An identifier for the content. The service sends
                  this value to the key server to identify the current endpoint. The resource ID is
                  also known as the content ID. This parameter is required for SPEKE encryption and
                  is not valid for static key encryption.

                  - **RoleArn** *(string) --* The ARN of the role that you created during setup
                  (when you set up AWS Elemental MediaConnect as a trusted entity).

                  - **SecretArn** *(string) --* The ARN of the secret that you created in AWS
                  Secrets Manager to store the encryption key. This parameter is required for static
                  key encryption and is not valid for SPEKE encryption.

                  - **Url** *(string) --* The URL from the API Gateway proxy that you set up to talk
                  to your key server. This parameter is required for SPEKE encryption and is not
                  valid for static key encryption.

                - **Description** *(string) --* A description for the source. This value is not used
                or seen outside of the current AWS Elemental MediaConnect account.

                - **EntitlementArn** *(string) --* The ARN of the entitlement that allows you to
                subscribe to content that comes from another AWS account. The entitlement is set by
                the content originator and the ARN is generated as part of the originator's flow.

                - **IngestIp** *(string) --* The IP address that the flow will be listening on for
                incoming content.

                - **IngestPort** *(integer) --* The port that the flow will be listening on for
                incoming content.

                - **Name** *(string) --* The name of the source.

                - **SourceArn** *(string) --* The ARN of the source.

                - **Transport** *(dict) --* Attributes related to the transport stream that are used
                in the source.

                  - **CidrAllowList** *(list) --* The range of IP addresses that should be allowed
                  to initiate output requests to this flow. These IP addresses should be in the form
                  of a Classless Inter-Domain Routing (CIDR) block; for example, 10.0.0.0/16.

                    - *(string) --*

                  - **MaxBitrate** *(integer) --* The smoothing max bitrate for RIST, RTP, and
                  RTP-FEC streams.

                  - **MaxLatency** *(integer) --* The maximum latency in milliseconds. This
                  parameter applies only to RIST-based and Zixi-based streams.

                  - **Protocol** *(string) --* The protocol that is used by the source or output.

                  - **RemoteId** *(string) --* The remote ID for the Zixi-pull stream.

                  - **SmoothingLatency** *(integer) --* The smoothing latency in milliseconds for
                  RIST, RTP, and RTP-FEC streams.

                  - **StreamId** *(string) --* The stream ID that you want to use for this
                  transport. This parameter applies only to Zixi-based streams.

                - **WhitelistCidr** *(string) --* The range of IP addresses that should be allowed
                to contribute content to your source. These IP addresses should be in the form of a
                Classless Inter-Domain Routing (CIDR) block; for example, 10.0.0.0/16.

              - **Status** *(string) --* The current status of the flow.

            - **Messages** *(dict) --* Messages that provide the state of the flow.

              - **Errors** *(list) --* A list of errors that might have been generated from
              processes on this flow.

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
    def grant_flow_entitlements(
        self, Entitlements: List[ClientGrantFlowEntitlementsEntitlementsTypeDef], FlowArn: str
    ) -> ClientGrantFlowEntitlementsResponseTypeDef:
        """
        Grants entitlements to an existing flow.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/mediaconnect-2018-11-14/GrantFlowEntitlements>`_

        **Request Syntax**
        ::

          response = client.grant_flow_entitlements(
              Entitlements=[
                  {
                      'DataTransferSubscriberFeePercent': 123,
                      'Description': 'string',
                      'Encryption': {
                          'Algorithm': 'aes128'|'aes192'|'aes256',
                          'ConstantInitializationVector': 'string',
                          'DeviceId': 'string',
                          'KeyType': 'speke'|'static-key',
                          'Region': 'string',
                          'ResourceId': 'string',
                          'RoleArn': 'string',
                          'SecretArn': 'string',
                          'Url': 'string'
                      },
                      'Name': 'string',
                      'Subscribers': [
                          'string',
                      ]
                  },
              ],
              FlowArn='string'
          )
        :type Entitlements: list
        :param Entitlements: **[REQUIRED]** The list of entitlements that you want to grant.

          - *(dict) --* The entitlements that you want to grant on a flow.

            - **DataTransferSubscriberFeePercent** *(integer) --* Percentage from 0-100 of the data
            transfer cost to be billed to the subscriber.

            - **Description** *(string) --* A description of the entitlement. This description
            appears only on the AWS Elemental MediaConnect console and will not be seen by the
            subscriber or end user.

            - **Encryption** *(dict) --* The type of encryption that will be used on the output that
            is associated with this entitlement.

              - **Algorithm** *(string) --* **[REQUIRED]** The type of algorithm that is used for
              the encryption (such as aes128, aes192, or aes256).

              - **ConstantInitializationVector** *(string) --* A 128-bit, 16-byte hex value
              represented by a 32-character string, to be used with the key for encrypting content.
              This parameter is not valid for static key encryption.

              - **DeviceId** *(string) --* The value of one of the devices that you configured with
              your digital rights management (DRM) platform key provider. This parameter is required
              for SPEKE encryption and is not valid for static key encryption.

              - **KeyType** *(string) --* The type of key that is used for the encryption. If no
              keyType is provided, the service will use the default setting (static-key).

              - **Region** *(string) --* The AWS Region that the API Gateway proxy endpoint was
              created in. This parameter is required for SPEKE encryption and is not valid for
              static key encryption.

              - **ResourceId** *(string) --* An identifier for the content. The service sends this
              value to the key server to identify the current endpoint. The resource ID is also
              known as the content ID. This parameter is required for SPEKE encryption and is not
              valid for static key encryption.

              - **RoleArn** *(string) --* **[REQUIRED]** The ARN of the role that you created during
              setup (when you set up AWS Elemental MediaConnect as a trusted entity).

              - **SecretArn** *(string) --* The ARN of the secret that you created in AWS Secrets
              Manager to store the encryption key. This parameter is required for static key
              encryption and is not valid for SPEKE encryption.

              - **Url** *(string) --* The URL from the API Gateway proxy that you set up to talk to
              your key server. This parameter is required for SPEKE encryption and is not valid for
              static key encryption.

            - **Name** *(string) --* The name of the entitlement. This value must be unique within
            the current flow.

            - **Subscribers** *(list) --* **[REQUIRED]** The AWS account IDs that you want to share
            your content with. The receiving accounts (subscribers) will be allowed to create their
            own flows using your content as the source.

              - *(string) --*

        :type FlowArn: string
        :param FlowArn: **[REQUIRED]** The flow that you want to grant entitlements on.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Entitlements': [
                    {
                        'DataTransferSubscriberFeePercent': 123,
                        'Description': 'string',
                        'Encryption': {
                            'Algorithm': 'aes128'|'aes192'|'aes256',
                            'ConstantInitializationVector': 'string',
                            'DeviceId': 'string',
                            'KeyType': 'speke'|'static-key',
                            'Region': 'string',
                            'ResourceId': 'string',
                            'RoleArn': 'string',
                            'SecretArn': 'string',
                            'Url': 'string'
                        },
                        'EntitlementArn': 'string',
                        'Name': 'string',
                        'Subscribers': [
                            'string',
                        ]
                    },
                ],
                'FlowArn': 'string'
            }
          **Response Structure**

          - *(dict) --* AWS Elemental MediaConnect granted the entitlements successfully.

            - **Entitlements** *(list) --* The entitlements that were just granted.

              - *(dict) --* The settings for a flow entitlement.

                - **DataTransferSubscriberFeePercent** *(integer) --* Percentage from 0-100 of the
                data transfer cost to be billed to the subscriber.

                - **Description** *(string) --* A description of the entitlement.

                - **Encryption** *(dict) --* The type of encryption that will be used on the output
                that is associated with this entitlement.

                  - **Algorithm** *(string) --* The type of algorithm that is used for the
                  encryption (such as aes128, aes192, or aes256).

                  - **ConstantInitializationVector** *(string) --* A 128-bit, 16-byte hex value
                  represented by a 32-character string, to be used with the key for encrypting
                  content. This parameter is not valid for static key encryption.

                  - **DeviceId** *(string) --* The value of one of the devices that you configured
                  with your digital rights management (DRM) platform key provider. This parameter is
                  required for SPEKE encryption and is not valid for static key encryption.

                  - **KeyType** *(string) --* The type of key that is used for the encryption. If no
                  keyType is provided, the service will use the default setting (static-key).

                  - **Region** *(string) --* The AWS Region that the API Gateway proxy endpoint was
                  created in. This parameter is required for SPEKE encryption and is not valid for
                  static key encryption.

                  - **ResourceId** *(string) --* An identifier for the content. The service sends
                  this value to the key server to identify the current endpoint. The resource ID is
                  also known as the content ID. This parameter is required for SPEKE encryption and
                  is not valid for static key encryption.

                  - **RoleArn** *(string) --* The ARN of the role that you created during setup
                  (when you set up AWS Elemental MediaConnect as a trusted entity).

                  - **SecretArn** *(string) --* The ARN of the secret that you created in AWS
                  Secrets Manager to store the encryption key. This parameter is required for static
                  key encryption and is not valid for SPEKE encryption.

                  - **Url** *(string) --* The URL from the API Gateway proxy that you set up to talk
                  to your key server. This parameter is required for SPEKE encryption and is not
                  valid for static key encryption.

                - **EntitlementArn** *(string) --* The ARN of the entitlement.

                - **Name** *(string) --* The name of the entitlement.

                - **Subscribers** *(list) --* The AWS account IDs that you want to share your
                content with. The receiving accounts (subscribers) will be allowed to create their
                own flow using your content as the source.

                  - *(string) --*

            - **FlowArn** *(string) --* The ARN of the flow that these entitlements were granted to.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_entitlements(
        self, MaxResults: int = None, NextToken: str = None
    ) -> ClientListEntitlementsResponseTypeDef:
        """
        Displays a list of all entitlements that have been granted to this account. This request
        returns 20 results per page.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/mediaconnect-2018-11-14/ListEntitlements>`_

        **Request Syntax**
        ::

          response = client.list_entitlements(
              MaxResults=123,
              NextToken='string'
          )
        :type MaxResults: integer
        :param MaxResults: The maximum number of results to return per API request. For example, you
        submit a ListEntitlements request with MaxResults set at 5. Although 20 items match your
        request, the service returns no more than the first 5 items. (The service also returns a
        NextToken value that you can use to fetch the next batch of results.) The service might
        return fewer results than the MaxResults value. If MaxResults is not included in the
        request, the service defaults to pagination with a maximum of 20 results per page.

        :type NextToken: string
        :param NextToken: The token that identifies which batch of results that you want to see. For
        example, you submit a ListEntitlements request with MaxResults set at 5. The service returns
        the first batch of results (up to 5) and a NextToken value. To see the next batch of
        results, you can submit the ListEntitlements request a second time and specify the NextToken
        value.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Entitlements': [
                    {
                        'DataTransferSubscriberFeePercent': 123,
                        'EntitlementArn': 'string',
                        'EntitlementName': 'string'
                    },
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --* AWS Elemental MediaConnect returned the list of entitlements successfully.

            - **Entitlements** *(list) --* A list of entitlements that have been granted to you from
            other AWS accounts.

              - *(dict) --* An entitlement that has been granted to you from other AWS accounts.

                - **DataTransferSubscriberFeePercent** *(integer) --* Percentage from 0-100 of the
                data transfer cost to be billed to the subscriber.

                - **EntitlementArn** *(string) --* The ARN of the entitlement.

                - **EntitlementName** *(string) --* The name of the entitlement.

            - **NextToken** *(string) --* The token that identifies which batch of results that you
            want to see. For example, you submit a ListEntitlements request with MaxResults set at
            5. The service returns the first batch of results (up to 5) and a NextToken value. To
            see the next batch of results, you can submit the ListEntitlements request a second time
            and specify the NextToken value.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_flows(
        self, MaxResults: int = None, NextToken: str = None
    ) -> ClientListFlowsResponseTypeDef:
        """
        Displays a list of flows that are associated with this account. This request returns a
        paginated result.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/mediaconnect-2018-11-14/ListFlows>`_

        **Request Syntax**
        ::

          response = client.list_flows(
              MaxResults=123,
              NextToken='string'
          )
        :type MaxResults: integer
        :param MaxResults: The maximum number of results to return per API request. For example, you
        submit a ListFlows request with MaxResults set at 5. Although 20 items match your request,
        the service returns no more than the first 5 items. (The service also returns a NextToken
        value that you can use to fetch the next batch of results.) The service might return fewer
        results than the MaxResults value. If MaxResults is not included in the request, the service
        defaults to pagination with a maximum of 10 results per page.

        :type NextToken: string
        :param NextToken: The token that identifies which batch of results that you want to see. For
        example, you submit a ListFlows request with MaxResults set at 5. The service returns the
        first batch of results (up to 5) and a NextToken value. To see the next batch of results,
        you can submit the ListFlows request a second time and specify the NextToken value.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Flows': [
                    {
                        'AvailabilityZone': 'string',
                        'Description': 'string',
                        'FlowArn': 'string',
                        'Name': 'string',
                        'SourceType': 'OWNED'|'ENTITLED',
                        'Status':
                        'STANDBY'|'ACTIVE'|'UPDATING'|'DELETING'|'STARTING'
                        |'STOPPING'|'ERROR'
                    },
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --* AWS Elemental MediaConnect returned the list of flows successfully.

            - **Flows** *(list) --* A list of flow summaries.

              - *(dict) --* Provides a summary of a flow, including its ARN, Availability Zone, and
              source type.

                - **AvailabilityZone** *(string) --* The Availability Zone that the flow was created
                in.

                - **Description** *(string) --* A description of the flow.

                - **FlowArn** *(string) --* The ARN of the flow.

                - **Name** *(string) --* The name of the flow.

                - **SourceType** *(string) --* The type of source. This value is either owned
                (originated somewhere other than an AWS Elemental MediaConnect flow owned by another
                AWS account) or entitled (originated at an AWS Elemental MediaConnect flow owned by
                another AWS account).

                - **Status** *(string) --* The current status of the flow.

            - **NextToken** *(string) --* The token that identifies which batch of results that you
            want to see. For example, you submit a ListFlows request with MaxResults set at 5. The
            service returns the first batch of results (up to 5) and a NextToken value. To see the
            next batch of results, you can submit the ListFlows request a second time and specify
            the NextToken value.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_tags_for_resource(self, ResourceArn: str) -> ClientListTagsForResourceResponseTypeDef:
        """
        List all tags on an AWS Elemental MediaConnect resource

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/mediaconnect-2018-11-14/ListTagsForResource>`_

        **Request Syntax**
        ::

          response = client.list_tags_for_resource(
              ResourceArn='string'
          )
        :type ResourceArn: string
        :param ResourceArn: **[REQUIRED]** The Amazon Resource Name (ARN) that identifies the AWS
        Elemental MediaConnect resource for which to list the tags.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Tags': {
                    'string': 'string'
                }
            }
          **Response Structure**

          - *(dict) --* The tags for the resource

            - **Tags** *(dict) --* A map from tag keys to values. Tag keys can have a maximum
            character length of 128 characters, and tag values can have a maximum length of 256
            characters.

              - *(string) --*

                - *(string) --*
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def remove_flow_output(
        self, FlowArn: str, OutputArn: str
    ) -> ClientRemoveFlowOutputResponseTypeDef:
        """
        Removes an output from an existing flow. This request can be made only on an output that
        does not have an entitlement associated with it. If the output has an entitlement, you must
        revoke the entitlement instead. When an entitlement is revoked from a flow, the service
        automatically removes the associated output.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/mediaconnect-2018-11-14/RemoveFlowOutput>`_

        **Request Syntax**
        ::

          response = client.remove_flow_output(
              FlowArn='string',
              OutputArn='string'
          )
        :type FlowArn: string
        :param FlowArn: **[REQUIRED]** The flow that you want to remove an output from.

        :type OutputArn: string
        :param OutputArn: **[REQUIRED]** The ARN of the output that you want to remove.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'FlowArn': 'string',
                'OutputArn': 'string'
            }
          **Response Structure**

          - *(dict) --* output successfully removed from flow configuration.

            - **FlowArn** *(string) --* The ARN of the flow that is associated with the output you
            removed.

            - **OutputArn** *(string) --* The ARN of the output that was removed.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def revoke_flow_entitlement(
        self, EntitlementArn: str, FlowArn: str
    ) -> ClientRevokeFlowEntitlementResponseTypeDef:
        """
        Revokes an entitlement from a flow. Once an entitlement is revoked, the content becomes
        unavailable to the subscriber and the associated output is removed.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/mediaconnect-2018-11-14/RevokeFlowEntitlement>`_

        **Request Syntax**
        ::

          response = client.revoke_flow_entitlement(
              EntitlementArn='string',
              FlowArn='string'
          )
        :type EntitlementArn: string
        :param EntitlementArn: **[REQUIRED]** The ARN of the entitlement that you want to revoke.

        :type FlowArn: string
        :param FlowArn: **[REQUIRED]** The flow that you want to revoke an entitlement from.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'EntitlementArn': 'string',
                'FlowArn': 'string'
            }
          **Response Structure**

          - *(dict) --* AWS Elemental MediaConnect revoked the entitlement successfully.

            - **EntitlementArn** *(string) --* The ARN of the entitlement that was revoked.

            - **FlowArn** *(string) --* The ARN of the flow that the entitlement was revoked from.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def start_flow(self, FlowArn: str) -> ClientStartFlowResponseTypeDef:
        """
        Starts a flow.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/mediaconnect-2018-11-14/StartFlow>`_

        **Request Syntax**
        ::

          response = client.start_flow(
              FlowArn='string'
          )
        :type FlowArn: string
        :param FlowArn: **[REQUIRED]** The ARN of the flow that you want to start.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'FlowArn': 'string',
                'Status': 'STANDBY'|'ACTIVE'|'UPDATING'|'DELETING'|'STARTING'|'STOPPING'|'ERROR'
            }
          **Response Structure**

          - *(dict) --* AWS Elemental MediaConnect is starting the flow.

            - **FlowArn** *(string) --* The ARN of the flow that you started.

            - **Status** *(string) --* The status of the flow when the StartFlow process begins.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def stop_flow(self, FlowArn: str) -> ClientStopFlowResponseTypeDef:
        """
        Stops a flow.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/mediaconnect-2018-11-14/StopFlow>`_

        **Request Syntax**
        ::

          response = client.stop_flow(
              FlowArn='string'
          )
        :type FlowArn: string
        :param FlowArn: **[REQUIRED]** The ARN of the flow that you want to stop.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'FlowArn': 'string',
                'Status': 'STANDBY'|'ACTIVE'|'UPDATING'|'DELETING'|'STARTING'|'STOPPING'|'ERROR'
            }
          **Response Structure**

          - *(dict) --* AWS Elemental MediaConnect is stopping the flow.

            - **FlowArn** *(string) --* The ARN of the flow that you stopped.

            - **Status** *(string) --* The status of the flow when the StopFlow process begins.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def tag_resource(self, ResourceArn: str, Tags: Dict[str, str]) -> None:
        """
        Associates the specified tags to a resource with the specified resourceArn. If existing tags
        on a resource are not specified in the request parameters, they are not changed. When a
        resource is deleted, the tags associated with that resource are deleted as well.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/mediaconnect-2018-11-14/TagResource>`_

        **Request Syntax**
        ::

          response = client.tag_resource(
              ResourceArn='string',
              Tags={
                  'string': 'string'
              }
          )
        :type ResourceArn: string
        :param ResourceArn: **[REQUIRED]** The Amazon Resource Name (ARN) that identifies the AWS
        Elemental MediaConnect resource to which to add tags.

        :type Tags: dict
        :param Tags: **[REQUIRED]** A map from tag keys to values. Tag keys can have a maximum
        character length of 128 characters, and tag values can have a maximum length of 256
        characters.

          - *(string) --*

            - *(string) --*

        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def untag_resource(self, ResourceArn: str, TagKeys: List[str]) -> None:
        """
        Deletes specified tags from a resource.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/mediaconnect-2018-11-14/UntagResource>`_

        **Request Syntax**
        ::

          response = client.untag_resource(
              ResourceArn='string',
              TagKeys=[
                  'string',
              ]
          )
        :type ResourceArn: string
        :param ResourceArn: **[REQUIRED]** The Amazon Resource Name (ARN) that identifies the AWS
        Elemental MediaConnect resource from which to delete tags.

        :type TagKeys: list
        :param TagKeys: **[REQUIRED]** The keys of the tags to be removed.

          - *(string) --*

        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_flow_entitlement(
        self,
        EntitlementArn: str,
        FlowArn: str,
        Description: str = None,
        Encryption: ClientUpdateFlowEntitlementEncryptionTypeDef = None,
        Subscribers: List[str] = None,
    ) -> ClientUpdateFlowEntitlementResponseTypeDef:
        """
        You can change an entitlement's description, subscribers, and encryption. If you change the
        subscribers, the service will remove the outputs that are are used by the subscribers that
        are removed.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/mediaconnect-2018-11-14/UpdateFlowEntitlement>`_

        **Request Syntax**
        ::

          response = client.update_flow_entitlement(
              Description='string',
              Encryption={
                  'Algorithm': 'aes128'|'aes192'|'aes256',
                  'ConstantInitializationVector': 'string',
                  'DeviceId': 'string',
                  'KeyType': 'speke'|'static-key',
                  'Region': 'string',
                  'ResourceId': 'string',
                  'RoleArn': 'string',
                  'SecretArn': 'string',
                  'Url': 'string'
              },
              EntitlementArn='string',
              FlowArn='string',
              Subscribers=[
                  'string',
              ]
          )
        :type Description: string
        :param Description: A description of the entitlement. This description appears only on the
        AWS Elemental MediaConnect console and will not be seen by the subscriber or end user.

        :type Encryption: dict
        :param Encryption: The type of encryption that will be used on the output associated with
        this entitlement.

          - **Algorithm** *(string) --* The type of algorithm that is used for the encryption (such
          as aes128, aes192, or aes256).

          - **ConstantInitializationVector** *(string) --* A 128-bit, 16-byte hex value represented
          by a 32-character string, to be used with the key for encrypting content. This parameter
          is not valid for static key encryption.

          - **DeviceId** *(string) --* The value of one of the devices that you configured with your
          digital rights management (DRM) platform key provider. This parameter is required for
          SPEKE encryption and is not valid for static key encryption.

          - **KeyType** *(string) --* The type of key that is used for the encryption. If no keyType
          is provided, the service will use the default setting (static-key).

          - **Region** *(string) --* The AWS Region that the API Gateway proxy endpoint was created
          in. This parameter is required for SPEKE encryption and is not valid for static key
          encryption.

          - **ResourceId** *(string) --* An identifier for the content. The service sends this value
          to the key server to identify the current endpoint. The resource ID is also known as the
          content ID. This parameter is required for SPEKE encryption and is not valid for static
          key encryption.

          - **RoleArn** *(string) --* The ARN of the role that you created during setup (when you
          set up AWS Elemental MediaConnect as a trusted entity).

          - **SecretArn** *(string) --* The ARN of the secret that you created in AWS Secrets
          Manager to store the encryption key. This parameter is required for static key encryption
          and is not valid for SPEKE encryption.

          - **Url** *(string) --* The URL from the API Gateway proxy that you set up to talk to your
          key server. This parameter is required for SPEKE encryption and is not valid for static
          key encryption.

        :type EntitlementArn: string
        :param EntitlementArn: **[REQUIRED]** The ARN of the entitlement that you want to update.

        :type FlowArn: string
        :param FlowArn: **[REQUIRED]** The flow that is associated with the entitlement that you
        want to update.

        :type Subscribers: list
        :param Subscribers: The AWS account IDs that you want to share your content with. The
        receiving accounts (subscribers) will be allowed to create their own flow using your content
        as the source.

          - *(string) --*

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Entitlement': {
                    'DataTransferSubscriberFeePercent': 123,
                    'Description': 'string',
                    'Encryption': {
                        'Algorithm': 'aes128'|'aes192'|'aes256',
                        'ConstantInitializationVector': 'string',
                        'DeviceId': 'string',
                        'KeyType': 'speke'|'static-key',
                        'Region': 'string',
                        'ResourceId': 'string',
                        'RoleArn': 'string',
                        'SecretArn': 'string',
                        'Url': 'string'
                    },
                    'EntitlementArn': 'string',
                    'Name': 'string',
                    'Subscribers': [
                        'string',
                    ]
                },
                'FlowArn': 'string'
            }
          **Response Structure**

          - *(dict) --* AWS Elemental MediaConnect updated the entitlement successfully.

            - **Entitlement** *(dict) --* The settings for a flow entitlement.

              - **DataTransferSubscriberFeePercent** *(integer) --* Percentage from 0-100 of the
              data transfer cost to be billed to the subscriber.

              - **Description** *(string) --* A description of the entitlement.

              - **Encryption** *(dict) --* The type of encryption that will be used on the output
              that is associated with this entitlement.

                - **Algorithm** *(string) --* The type of algorithm that is used for the encryption
                (such as aes128, aes192, or aes256).

                - **ConstantInitializationVector** *(string) --* A 128-bit, 16-byte hex value
                represented by a 32-character string, to be used with the key for encrypting
                content. This parameter is not valid for static key encryption.

                - **DeviceId** *(string) --* The value of one of the devices that you configured
                with your digital rights management (DRM) platform key provider. This parameter is
                required for SPEKE encryption and is not valid for static key encryption.

                - **KeyType** *(string) --* The type of key that is used for the encryption. If no
                keyType is provided, the service will use the default setting (static-key).

                - **Region** *(string) --* The AWS Region that the API Gateway proxy endpoint was
                created in. This parameter is required for SPEKE encryption and is not valid for
                static key encryption.

                - **ResourceId** *(string) --* An identifier for the content. The service sends this
                value to the key server to identify the current endpoint. The resource ID is also
                known as the content ID. This parameter is required for SPEKE encryption and is not
                valid for static key encryption.

                - **RoleArn** *(string) --* The ARN of the role that you created during setup (when
                you set up AWS Elemental MediaConnect as a trusted entity).

                - **SecretArn** *(string) --* The ARN of the secret that you created in AWS Secrets
                Manager to store the encryption key. This parameter is required for static key
                encryption and is not valid for SPEKE encryption.

                - **Url** *(string) --* The URL from the API Gateway proxy that you set up to talk
                to your key server. This parameter is required for SPEKE encryption and is not valid
                for static key encryption.

              - **EntitlementArn** *(string) --* The ARN of the entitlement.

              - **Name** *(string) --* The name of the entitlement.

              - **Subscribers** *(list) --* The AWS account IDs that you want to share your content
              with. The receiving accounts (subscribers) will be allowed to create their own flow
              using your content as the source.

                - *(string) --*

            - **FlowArn** *(string) --* The ARN of the flow that this entitlement was granted on.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_flow_output(
        self,
        FlowArn: str,
        OutputArn: str,
        CidrAllowList: List[str] = None,
        Description: str = None,
        Destination: str = None,
        Encryption: ClientUpdateFlowOutputEncryptionTypeDef = None,
        MaxLatency: int = None,
        Port: int = None,
        Protocol: Literal["zixi-push", "rtp-fec", "rtp", "zixi-pull", "rist"] = None,
        RemoteId: str = None,
        SmoothingLatency: int = None,
        StreamId: str = None,
    ) -> ClientUpdateFlowOutputResponseTypeDef:
        """
        Updates an existing flow output.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/mediaconnect-2018-11-14/UpdateFlowOutput>`_

        **Request Syntax**
        ::

          response = client.update_flow_output(
              CidrAllowList=[
                  'string',
              ],
              Description='string',
              Destination='string',
              Encryption={
                  'Algorithm': 'aes128'|'aes192'|'aes256',
                  'ConstantInitializationVector': 'string',
                  'DeviceId': 'string',
                  'KeyType': 'speke'|'static-key',
                  'Region': 'string',
                  'ResourceId': 'string',
                  'RoleArn': 'string',
                  'SecretArn': 'string',
                  'Url': 'string'
              },
              FlowArn='string',
              MaxLatency=123,
              OutputArn='string',
              Port=123,
              Protocol='zixi-push'|'rtp-fec'|'rtp'|'zixi-pull'|'rist',
              RemoteId='string',
              SmoothingLatency=123,
              StreamId='string'
          )
        :type CidrAllowList: list
        :param CidrAllowList: The range of IP addresses that should be allowed to initiate output
        requests to this flow. These IP addresses should be in the form of a Classless Inter-Domain
        Routing (CIDR) block; for example, 10.0.0.0/16.

          - *(string) --*

        :type Description: string
        :param Description: A description of the output. This description appears only on the AWS
        Elemental MediaConnect console and will not be seen by the end user.

        :type Destination: string
        :param Destination: The IP address where you want to send the output.

        :type Encryption: dict
        :param Encryption: The type of key used for the encryption. If no keyType is provided, the
        service will use the default setting (static-key).

          - **Algorithm** *(string) --* The type of algorithm that is used for the encryption (such
          as aes128, aes192, or aes256).

          - **ConstantInitializationVector** *(string) --* A 128-bit, 16-byte hex value represented
          by a 32-character string, to be used with the key for encrypting content. This parameter
          is not valid for static key encryption.

          - **DeviceId** *(string) --* The value of one of the devices that you configured with your
          digital rights management (DRM) platform key provider. This parameter is required for
          SPEKE encryption and is not valid for static key encryption.

          - **KeyType** *(string) --* The type of key that is used for the encryption. If no keyType
          is provided, the service will use the default setting (static-key).

          - **Region** *(string) --* The AWS Region that the API Gateway proxy endpoint was created
          in. This parameter is required for SPEKE encryption and is not valid for static key
          encryption.

          - **ResourceId** *(string) --* An identifier for the content. The service sends this value
          to the key server to identify the current endpoint. The resource ID is also known as the
          content ID. This parameter is required for SPEKE encryption and is not valid for static
          key encryption.

          - **RoleArn** *(string) --* The ARN of the role that you created during setup (when you
          set up AWS Elemental MediaConnect as a trusted entity).

          - **SecretArn** *(string) --* The ARN of the secret that you created in AWS Secrets
          Manager to store the encryption key. This parameter is required for static key encryption
          and is not valid for SPEKE encryption.

          - **Url** *(string) --* The URL from the API Gateway proxy that you set up to talk to your
          key server. This parameter is required for SPEKE encryption and is not valid for static
          key encryption.

        :type FlowArn: string
        :param FlowArn: **[REQUIRED]** The flow that is associated with the output that you want to
        update.

        :type MaxLatency: integer
        :param MaxLatency: The maximum latency in milliseconds for Zixi-based streams.

        :type OutputArn: string
        :param OutputArn: **[REQUIRED]** The ARN of the output that you want to update.

        :type Port: integer
        :param Port: The port to use when content is distributed to this output.

        :type Protocol: string
        :param Protocol: The protocol to use for the output.

        :type RemoteId: string
        :param RemoteId: The remote ID for the Zixi-pull stream.

        :type SmoothingLatency: integer
        :param SmoothingLatency: The smoothing latency in milliseconds for RIST, RTP, and RTP-FEC
        streams.

        :type StreamId: string
        :param StreamId: The stream ID that you want to use for this transport. This parameter
        applies only to Zixi-based streams.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'FlowArn': 'string',
                'Output': {
                    'DataTransferSubscriberFeePercent': 123,
                    'Description': 'string',
                    'Destination': 'string',
                    'Encryption': {
                        'Algorithm': 'aes128'|'aes192'|'aes256',
                        'ConstantInitializationVector': 'string',
                        'DeviceId': 'string',
                        'KeyType': 'speke'|'static-key',
                        'Region': 'string',
                        'ResourceId': 'string',
                        'RoleArn': 'string',
                        'SecretArn': 'string',
                        'Url': 'string'
                    },
                    'EntitlementArn': 'string',
                    'MediaLiveInputArn': 'string',
                    'Name': 'string',
                    'OutputArn': 'string',
                    'Port': 123,
                    'Transport': {
                        'CidrAllowList': [
                            'string',
                        ],
                        'MaxBitrate': 123,
                        'MaxLatency': 123,
                        'Protocol': 'zixi-push'|'rtp-fec'|'rtp'|'zixi-pull'|'rist',
                        'RemoteId': 'string',
                        'SmoothingLatency': 123,
                        'StreamId': 'string'
                    }
                }
            }
          **Response Structure**

          - *(dict) --* AWS Elemental MediaConnect updated the output successfully.

            - **FlowArn** *(string) --* The ARN of the flow that is associated with the updated
            output.

            - **Output** *(dict) --* The settings for an output.

              - **DataTransferSubscriberFeePercent** *(integer) --* Percentage from 0-100 of the
              data transfer cost to be billed to the subscriber.

              - **Description** *(string) --* A description of the output.

              - **Destination** *(string) --* The address where you want to send the output.

              - **Encryption** *(dict) --* The type of key used for the encryption. If no keyType is
              provided, the service will use the default setting (static-key).

                - **Algorithm** *(string) --* The type of algorithm that is used for the encryption
                (such as aes128, aes192, or aes256).

                - **ConstantInitializationVector** *(string) --* A 128-bit, 16-byte hex value
                represented by a 32-character string, to be used with the key for encrypting
                content. This parameter is not valid for static key encryption.

                - **DeviceId** *(string) --* The value of one of the devices that you configured
                with your digital rights management (DRM) platform key provider. This parameter is
                required for SPEKE encryption and is not valid for static key encryption.

                - **KeyType** *(string) --* The type of key that is used for the encryption. If no
                keyType is provided, the service will use the default setting (static-key).

                - **Region** *(string) --* The AWS Region that the API Gateway proxy endpoint was
                created in. This parameter is required for SPEKE encryption and is not valid for
                static key encryption.

                - **ResourceId** *(string) --* An identifier for the content. The service sends this
                value to the key server to identify the current endpoint. The resource ID is also
                known as the content ID. This parameter is required for SPEKE encryption and is not
                valid for static key encryption.

                - **RoleArn** *(string) --* The ARN of the role that you created during setup (when
                you set up AWS Elemental MediaConnect as a trusted entity).

                - **SecretArn** *(string) --* The ARN of the secret that you created in AWS Secrets
                Manager to store the encryption key. This parameter is required for static key
                encryption and is not valid for SPEKE encryption.

                - **Url** *(string) --* The URL from the API Gateway proxy that you set up to talk
                to your key server. This parameter is required for SPEKE encryption and is not valid
                for static key encryption.

              - **EntitlementArn** *(string) --* The ARN of the entitlement on the originator''s
              flow. This value is relevant only on entitled flows.

              - **MediaLiveInputArn** *(string) --* The input ARN of the AWS Elemental MediaLive
              channel. This parameter is relevant only for outputs that were added by creating a
              MediaLive input.

              - **Name** *(string) --* The name of the output. This value must be unique within the
              current flow.

              - **OutputArn** *(string) --* The ARN of the output.

              - **Port** *(integer) --* The port to use when content is distributed to this output.

              - **Transport** *(dict) --* Attributes related to the transport stream that are used
              in the output.

                - **CidrAllowList** *(list) --* The range of IP addresses that should be allowed to
                initiate output requests to this flow. These IP addresses should be in the form of a
                Classless Inter-Domain Routing (CIDR) block; for example, 10.0.0.0/16.

                  - *(string) --*

                - **MaxBitrate** *(integer) --* The smoothing max bitrate for RIST, RTP, and RTP-FEC
                streams.

                - **MaxLatency** *(integer) --* The maximum latency in milliseconds. This parameter
                applies only to RIST-based and Zixi-based streams.

                - **Protocol** *(string) --* The protocol that is used by the source or output.

                - **RemoteId** *(string) --* The remote ID for the Zixi-pull stream.

                - **SmoothingLatency** *(integer) --* The smoothing latency in milliseconds for
                RIST, RTP, and RTP-FEC streams.

                - **StreamId** *(string) --* The stream ID that you want to use for this transport.
                This parameter applies only to Zixi-based streams.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_flow_source(
        self,
        FlowArn: str,
        SourceArn: str,
        Decryption: ClientUpdateFlowSourceDecryptionTypeDef = None,
        Description: str = None,
        EntitlementArn: str = None,
        IngestPort: int = None,
        MaxBitrate: int = None,
        MaxLatency: int = None,
        Protocol: Literal["zixi-push", "rtp-fec", "rtp", "zixi-pull", "rist"] = None,
        StreamId: str = None,
        WhitelistCidr: str = None,
    ) -> ClientUpdateFlowSourceResponseTypeDef:
        """
        Updates the source of a flow.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/mediaconnect-2018-11-14/UpdateFlowSource>`_

        **Request Syntax**
        ::

          response = client.update_flow_source(
              Decryption={
                  'Algorithm': 'aes128'|'aes192'|'aes256',
                  'ConstantInitializationVector': 'string',
                  'DeviceId': 'string',
                  'KeyType': 'speke'|'static-key',
                  'Region': 'string',
                  'ResourceId': 'string',
                  'RoleArn': 'string',
                  'SecretArn': 'string',
                  'Url': 'string'
              },
              Description='string',
              EntitlementArn='string',
              FlowArn='string',
              IngestPort=123,
              MaxBitrate=123,
              MaxLatency=123,
              Protocol='zixi-push'|'rtp-fec'|'rtp'|'zixi-pull'|'rist',
              SourceArn='string',
              StreamId='string',
              WhitelistCidr='string'
          )
        :type Decryption: dict
        :param Decryption: The type of encryption used on the content ingested from this source.

          - **Algorithm** *(string) --* The type of algorithm that is used for the encryption (such
          as aes128, aes192, or aes256).

          - **ConstantInitializationVector** *(string) --* A 128-bit, 16-byte hex value represented
          by a 32-character string, to be used with the key for encrypting content. This parameter
          is not valid for static key encryption.

          - **DeviceId** *(string) --* The value of one of the devices that you configured with your
          digital rights management (DRM) platform key provider. This parameter is required for
          SPEKE encryption and is not valid for static key encryption.

          - **KeyType** *(string) --* The type of key that is used for the encryption. If no keyType
          is provided, the service will use the default setting (static-key).

          - **Region** *(string) --* The AWS Region that the API Gateway proxy endpoint was created
          in. This parameter is required for SPEKE encryption and is not valid for static key
          encryption.

          - **ResourceId** *(string) --* An identifier for the content. The service sends this value
          to the key server to identify the current endpoint. The resource ID is also known as the
          content ID. This parameter is required for SPEKE encryption and is not valid for static
          key encryption.

          - **RoleArn** *(string) --* The ARN of the role that you created during setup (when you
          set up AWS Elemental MediaConnect as a trusted entity).

          - **SecretArn** *(string) --* The ARN of the secret that you created in AWS Secrets
          Manager to store the encryption key. This parameter is required for static key encryption
          and is not valid for SPEKE encryption.

          - **Url** *(string) --* The URL from the API Gateway proxy that you set up to talk to your
          key server. This parameter is required for SPEKE encryption and is not valid for static
          key encryption.

        :type Description: string
        :param Description: A description for the source. This value is not used or seen outside of
        the current AWS Elemental MediaConnect account.

        :type EntitlementArn: string
        :param EntitlementArn: The ARN of the entitlement that allows you to subscribe to this flow.
        The entitlement is set by the flow originator, and the ARN is generated as part of the
        originator's flow.

        :type FlowArn: string
        :param FlowArn: **[REQUIRED]** The flow that is associated with the source that you want to
        update.

        :type IngestPort: integer
        :param IngestPort: The port that the flow will be listening on for incoming content.

        :type MaxBitrate: integer
        :param MaxBitrate: The smoothing max bitrate for RIST, RTP, and RTP-FEC streams.

        :type MaxLatency: integer
        :param MaxLatency: The maximum latency in milliseconds. This parameter applies only to
        RIST-based and Zixi-based streams.

        :type Protocol: string
        :param Protocol: The protocol that is used by the source.

        :type SourceArn: string
        :param SourceArn: **[REQUIRED]** The ARN of the source that you want to update.

        :type StreamId: string
        :param StreamId: The stream ID that you want to use for this transport. This parameter
        applies only to Zixi-based streams.

        :type WhitelistCidr: string
        :param WhitelistCidr: The range of IP addresses that should be allowed to contribute content
        to your source. These IP addresses should be in the form of a Classless Inter-Domain Routing
        (CIDR) block; for example, 10.0.0.0/16.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'FlowArn': 'string',
                'Source': {
                    'DataTransferSubscriberFeePercent': 123,
                    'Decryption': {
                        'Algorithm': 'aes128'|'aes192'|'aes256',
                        'ConstantInitializationVector': 'string',
                        'DeviceId': 'string',
                        'KeyType': 'speke'|'static-key',
                        'Region': 'string',
                        'ResourceId': 'string',
                        'RoleArn': 'string',
                        'SecretArn': 'string',
                        'Url': 'string'
                    },
                    'Description': 'string',
                    'EntitlementArn': 'string',
                    'IngestIp': 'string',
                    'IngestPort': 123,
                    'Name': 'string',
                    'SourceArn': 'string',
                    'Transport': {
                        'CidrAllowList': [
                            'string',
                        ],
                        'MaxBitrate': 123,
                        'MaxLatency': 123,
                        'Protocol': 'zixi-push'|'rtp-fec'|'rtp'|'zixi-pull'|'rist',
                        'RemoteId': 'string',
                        'SmoothingLatency': 123,
                        'StreamId': 'string'
                    },
                    'WhitelistCidr': 'string'
                }
            }
          **Response Structure**

          - *(dict) --* AWS Elemental MediaConnect updated the flow successfully.

            - **FlowArn** *(string) --* The ARN of the flow that you want to update.

            - **Source** *(dict) --* The settings for the source of the flow.

              - **DataTransferSubscriberFeePercent** *(integer) --* Percentage from 0-100 of the
              data transfer cost to be billed to the subscriber.

              - **Decryption** *(dict) --* The type of encryption that is used on the content
              ingested from this source.

                - **Algorithm** *(string) --* The type of algorithm that is used for the encryption
                (such as aes128, aes192, or aes256).

                - **ConstantInitializationVector** *(string) --* A 128-bit, 16-byte hex value
                represented by a 32-character string, to be used with the key for encrypting
                content. This parameter is not valid for static key encryption.

                - **DeviceId** *(string) --* The value of one of the devices that you configured
                with your digital rights management (DRM) platform key provider. This parameter is
                required for SPEKE encryption and is not valid for static key encryption.

                - **KeyType** *(string) --* The type of key that is used for the encryption. If no
                keyType is provided, the service will use the default setting (static-key).

                - **Region** *(string) --* The AWS Region that the API Gateway proxy endpoint was
                created in. This parameter is required for SPEKE encryption and is not valid for
                static key encryption.

                - **ResourceId** *(string) --* An identifier for the content. The service sends this
                value to the key server to identify the current endpoint. The resource ID is also
                known as the content ID. This parameter is required for SPEKE encryption and is not
                valid for static key encryption.

                - **RoleArn** *(string) --* The ARN of the role that you created during setup (when
                you set up AWS Elemental MediaConnect as a trusted entity).

                - **SecretArn** *(string) --* The ARN of the secret that you created in AWS Secrets
                Manager to store the encryption key. This parameter is required for static key
                encryption and is not valid for SPEKE encryption.

                - **Url** *(string) --* The URL from the API Gateway proxy that you set up to talk
                to your key server. This parameter is required for SPEKE encryption and is not valid
                for static key encryption.

              - **Description** *(string) --* A description for the source. This value is not used
              or seen outside of the current AWS Elemental MediaConnect account.

              - **EntitlementArn** *(string) --* The ARN of the entitlement that allows you to
              subscribe to content that comes from another AWS account. The entitlement is set by
              the content originator and the ARN is generated as part of the originator's flow.

              - **IngestIp** *(string) --* The IP address that the flow will be listening on for
              incoming content.

              - **IngestPort** *(integer) --* The port that the flow will be listening on for
              incoming content.

              - **Name** *(string) --* The name of the source.

              - **SourceArn** *(string) --* The ARN of the source.

              - **Transport** *(dict) --* Attributes related to the transport stream that are used
              in the source.

                - **CidrAllowList** *(list) --* The range of IP addresses that should be allowed to
                initiate output requests to this flow. These IP addresses should be in the form of a
                Classless Inter-Domain Routing (CIDR) block; for example, 10.0.0.0/16.

                  - *(string) --*

                - **MaxBitrate** *(integer) --* The smoothing max bitrate for RIST, RTP, and RTP-FEC
                streams.

                - **MaxLatency** *(integer) --* The maximum latency in milliseconds. This parameter
                applies only to RIST-based and Zixi-based streams.

                - **Protocol** *(string) --* The protocol that is used by the source or output.

                - **RemoteId** *(string) --* The remote ID for the Zixi-pull stream.

                - **SmoothingLatency** *(integer) --* The smoothing latency in milliseconds for
                RIST, RTP, and RTP-FEC streams.

                - **StreamId** *(string) --* The stream ID that you want to use for this transport.
                This parameter applies only to Zixi-based streams.

              - **WhitelistCidr** *(string) --* The range of IP addresses that should be allowed to
              contribute content to your source. These IP addresses should be in the form of a
              Classless Inter-Domain Routing (CIDR) block; for example, 10.0.0.0/16.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_entitlements"]
    ) -> paginator_scope.ListEntitlementsPaginator:
        """
        Get Paginator for `list_entitlements` operation.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_flows"]
    ) -> paginator_scope.ListFlowsPaginator:
        """
        Get Paginator for `list_flows` operation.
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
    AddFlowOutputs420Exception: Boto3ClientError
    BadRequestException: Boto3ClientError
    ClientError: Boto3ClientError
    CreateFlow420Exception: Boto3ClientError
    ForbiddenException: Boto3ClientError
    GrantFlowEntitlements420Exception: Boto3ClientError
    InternalServerErrorException: Boto3ClientError
    NotFoundException: Boto3ClientError
    ServiceUnavailableException: Boto3ClientError
    TooManyRequestsException: Boto3ClientError
