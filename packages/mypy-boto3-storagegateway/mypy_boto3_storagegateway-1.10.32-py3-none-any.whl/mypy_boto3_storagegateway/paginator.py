"Main interface for storagegateway service Paginators"
from __future__ import annotations

from typing import List
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_storagegateway.type_defs import (
    DescribeTapeArchivesPaginatePaginationConfigTypeDef,
    DescribeTapeArchivesPaginateResponseTypeDef,
    DescribeTapeRecoveryPointsPaginatePaginationConfigTypeDef,
    DescribeTapeRecoveryPointsPaginateResponseTypeDef,
    DescribeTapesPaginatePaginationConfigTypeDef,
    DescribeTapesPaginateResponseTypeDef,
    DescribeVTLDevicesPaginatePaginationConfigTypeDef,
    DescribeVTLDevicesPaginateResponseTypeDef,
    ListFileSharesPaginatePaginationConfigTypeDef,
    ListFileSharesPaginateResponseTypeDef,
    ListGatewaysPaginatePaginationConfigTypeDef,
    ListGatewaysPaginateResponseTypeDef,
    ListTagsForResourcePaginatePaginationConfigTypeDef,
    ListTagsForResourcePaginateResponseTypeDef,
    ListTapesPaginatePaginationConfigTypeDef,
    ListTapesPaginateResponseTypeDef,
    ListVolumesPaginatePaginationConfigTypeDef,
    ListVolumesPaginateResponseTypeDef,
)


__all__ = (
    "DescribeTapeArchivesPaginator",
    "DescribeTapeRecoveryPointsPaginator",
    "DescribeTapesPaginator",
    "DescribeVTLDevicesPaginator",
    "ListFileSharesPaginator",
    "ListGatewaysPaginator",
    "ListTagsForResourcePaginator",
    "ListTapesPaginator",
    "ListVolumesPaginator",
)


class DescribeTapeArchivesPaginator(Boto3Paginator):
    """
    Paginator for `describe_tape_archives`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        TapeARNs: List[str] = None,
        PaginationConfig: DescribeTapeArchivesPaginatePaginationConfigTypeDef = None,
    ) -> DescribeTapeArchivesPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`StorageGateway.Client.describe_tape_archives`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/storagegateway-2013-06-30/DescribeTapeArchives>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              TapeARNs=[
                  'string',
              ],
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type TapeARNs: list
        :param TapeARNs:

          Specifies one or more unique Amazon Resource Names (ARNs) that represent the virtual tapes
          you want to describe.

          - *(string) --*

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
                'TapeArchives': [
                    {
                        'TapeARN': 'string',
                        'TapeBarcode': 'string',
                        'TapeCreatedDate': datetime(2015, 1, 1),
                        'TapeSizeInBytes': 123,
                        'CompletionTime': datetime(2015, 1, 1),
                        'RetrievedTo': 'string',
                        'TapeStatus': 'string',
                        'TapeUsedInBytes': 123,
                        'KMSKey': 'string',
                        'PoolId': 'string'
                    },
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            DescribeTapeArchivesOutput

            - **TapeArchives** *(list) --*

              An array of virtual tape objects in the virtual tape shelf (VTS). The description
              includes of the Amazon Resource Name (ARN) of the virtual tapes. The information
              returned includes the Amazon Resource Names (ARNs) of the tapes, size of the tapes,
              status of the tapes, progress of the description and tape barcode.

              - *(dict) --*

                Represents a virtual tape that is archived in the virtual tape shelf (VTS).

                - **TapeARN** *(string) --*

                  The Amazon Resource Name (ARN) of an archived virtual tape.

                - **TapeBarcode** *(string) --*

                  The barcode that identifies the archived virtual tape.

                - **TapeCreatedDate** *(datetime) --*

                  The date the virtual tape was created.

                - **TapeSizeInBytes** *(integer) --*

                  The size, in bytes, of the archived virtual tape.

                - **CompletionTime** *(datetime) --*

                  The time that the archiving of the virtual tape was completed.

                  The default time stamp format is in the ISO8601 extended YYYY-MM-DD'T'HH:MM:SS'Z'
                  format.

                - **RetrievedTo** *(string) --*

                  The Amazon Resource Name (ARN) of the tape gateway that the virtual tape is being
                  retrieved to.

                  The virtual tape is retrieved from the virtual tape shelf (VTS).

                - **TapeStatus** *(string) --*

                  The current state of the archived virtual tape.

                - **TapeUsedInBytes** *(integer) --*

                  The size, in bytes, of data stored on the virtual tape.

                  .. note::

                    This value is not available for tapes created prior to May 13, 2015.

                - **KMSKey** *(string) --*

                  The Amazon Resource Name (ARN) of the AWS KMS key used for Amazon S3 server side
                  encryption. This value can only be set when KMSEncrypted is true. Optional.

                - **PoolId** *(string) --*

                  The ID of the pool that was used to archive the tape. The tapes in this pool are
                  archived in the S3 storage class that is associated with the pool.

                  Valid values: "GLACIER", "DEEP_ARCHIVE"

            - **NextToken** *(string) --*

              A token to resume pagination.
        """


class DescribeTapeRecoveryPointsPaginator(Boto3Paginator):
    """
    Paginator for `describe_tape_recovery_points`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        GatewayARN: str,
        PaginationConfig: DescribeTapeRecoveryPointsPaginatePaginationConfigTypeDef = None,
    ) -> DescribeTapeRecoveryPointsPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`StorageGateway.Client.describe_tape_recovery_points`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/storagegateway-2013-06-30/DescribeTapeRecoveryPoints>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              GatewayARN='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type GatewayARN: string
        :param GatewayARN: **[REQUIRED]**

          The Amazon Resource Name (ARN) of the gateway. Use the  ListGateways operation to return a
          list of gateways for your account and AWS Region.

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
                'GatewayARN': 'string',
                'TapeRecoveryPointInfos': [
                    {
                        'TapeARN': 'string',
                        'TapeRecoveryPointTime': datetime(2015, 1, 1),
                        'TapeSizeInBytes': 123,
                        'TapeStatus': 'string'
                    },
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            DescribeTapeRecoveryPointsOutput

            - **GatewayARN** *(string) --*

              The Amazon Resource Name (ARN) of the gateway. Use the  ListGateways operation to
              return a list of gateways for your account and AWS Region.

            - **TapeRecoveryPointInfos** *(list) --*

              An array of TapeRecoveryPointInfos that are available for the specified gateway.

              - *(dict) --*

                Describes a recovery point.

                - **TapeARN** *(string) --*

                  The Amazon Resource Name (ARN) of the virtual tape.

                - **TapeRecoveryPointTime** *(datetime) --*

                  The time when the point-in-time view of the virtual tape was replicated for later
                  recovery.

                  The default time stamp format of the tape recovery point time is in the ISO8601
                  extended YYYY-MM-DD'T'HH:MM:SS'Z' format.

                - **TapeSizeInBytes** *(integer) --*

                  The size, in bytes, of the virtual tapes to recover.

                - **TapeStatus** *(string) --*

                  The status of the virtual tapes.

            - **NextToken** *(string) --*

              A token to resume pagination.
        """


class DescribeTapesPaginator(Boto3Paginator):
    """
    Paginator for `describe_tapes`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        GatewayARN: str,
        TapeARNs: List[str] = None,
        PaginationConfig: DescribeTapesPaginatePaginationConfigTypeDef = None,
    ) -> DescribeTapesPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`StorageGateway.Client.describe_tapes`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/storagegateway-2013-06-30/DescribeTapes>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              GatewayARN='string',
              TapeARNs=[
                  'string',
              ],
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type GatewayARN: string
        :param GatewayARN: **[REQUIRED]**

          The Amazon Resource Name (ARN) of the gateway. Use the  ListGateways operation to return a
          list of gateways for your account and AWS Region.

        :type TapeARNs: list
        :param TapeARNs:

          Specifies one or more unique Amazon Resource Names (ARNs) that represent the virtual tapes
          you want to describe. If this parameter is not specified, Tape gateway returns a
          description of all virtual tapes associated with the specified gateway.

          - *(string) --*

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
                'Tapes': [
                    {
                        'TapeARN': 'string',
                        'TapeBarcode': 'string',
                        'TapeCreatedDate': datetime(2015, 1, 1),
                        'TapeSizeInBytes': 123,
                        'TapeStatus': 'string',
                        'VTLDevice': 'string',
                        'Progress': 123.0,
                        'TapeUsedInBytes': 123,
                        'KMSKey': 'string',
                        'PoolId': 'string'
                    },
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            DescribeTapesOutput

            - **Tapes** *(list) --*

              An array of virtual tape descriptions.

              - *(dict) --*

                Describes a virtual tape object.

                - **TapeARN** *(string) --*

                  The Amazon Resource Name (ARN) of the virtual tape.

                - **TapeBarcode** *(string) --*

                  The barcode that identifies a specific virtual tape.

                - **TapeCreatedDate** *(datetime) --*

                  The date the virtual tape was created.

                - **TapeSizeInBytes** *(integer) --*

                  The size, in bytes, of the virtual tape capacity.

                - **TapeStatus** *(string) --*

                  The current state of the virtual tape.

                - **VTLDevice** *(string) --*

                  The virtual tape library (VTL) device that the virtual tape is associated with.

                - **Progress** *(float) --*

                  For archiving virtual tapes, indicates how much data remains to be uploaded before
                  archiving is complete.

                  Range: 0 (not started) to 100 (complete).

                - **TapeUsedInBytes** *(integer) --*

                  The size, in bytes, of data stored on the virtual tape.

                  .. note::

                    This value is not available for tapes created prior to May 13, 2015.

                - **KMSKey** *(string) --*

                  The Amazon Resource Name (ARN) of the AWS KMS key used for Amazon S3 server side
                  encryption. This value can only be set when KMSEncrypted is true. Optional.

                - **PoolId** *(string) --*

                  The ID of the pool that contains tapes that will be archived. The tapes in this
                  pool are archived in the S3 storage class that is associated with the pool. When
                  you use your backup application to eject the tape, the tape is archived directly
                  into the storage class (Glacier or Deep Archive) that corresponds to the pool.

                  Valid values: "GLACIER", "DEEP_ARCHIVE"

            - **NextToken** *(string) --*

              A token to resume pagination.
        """


class DescribeVTLDevicesPaginator(Boto3Paginator):
    """
    Paginator for `describe_vtl_devices`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        GatewayARN: str,
        VTLDeviceARNs: List[str] = None,
        PaginationConfig: DescribeVTLDevicesPaginatePaginationConfigTypeDef = None,
    ) -> DescribeVTLDevicesPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`StorageGateway.Client.describe_vtl_devices`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/storagegateway-2013-06-30/DescribeVTLDevices>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              GatewayARN='string',
              VTLDeviceARNs=[
                  'string',
              ],
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type GatewayARN: string
        :param GatewayARN: **[REQUIRED]**

          The Amazon Resource Name (ARN) of the gateway. Use the  ListGateways operation to return a
          list of gateways for your account and AWS Region.

        :type VTLDeviceARNs: list
        :param VTLDeviceARNs:

          An array of strings, where each string represents the Amazon Resource Name (ARN) of a VTL
          device.

          .. note::

            All of the specified VTL devices must be from the same gateway. If no VTL devices are
            specified, the result will contain all devices on the specified gateway.

          - *(string) --*

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
                'GatewayARN': 'string',
                'VTLDevices': [
                    {
                        'VTLDeviceARN': 'string',
                        'VTLDeviceType': 'string',
                        'VTLDeviceVendor': 'string',
                        'VTLDeviceProductIdentifier': 'string',
                        'DeviceiSCSIAttributes': {
                            'TargetARN': 'string',
                            'NetworkInterfaceId': 'string',
                            'NetworkInterfacePort': 123,
                            'ChapEnabled': True|False
                        }
                    },
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            DescribeVTLDevicesOutput

            - **GatewayARN** *(string) --*

              The Amazon Resource Name (ARN) of the gateway. Use the  ListGateways operation to
              return a list of gateways for your account and AWS Region.

            - **VTLDevices** *(list) --*

              An array of VTL device objects composed of the Amazon Resource Name(ARN) of the VTL
              devices.

              - *(dict) --*

                Represents a device object associated with a tape gateway.

                - **VTLDeviceARN** *(string) --*

                  Specifies the unique Amazon Resource Name (ARN) of the device (tape drive or media
                  changer).

                - **VTLDeviceType** *(string) --*

                  Specifies the type of device that the VTL device emulates.

                - **VTLDeviceVendor** *(string) --*

                  Specifies the vendor of the device that the VTL device object emulates.

                - **VTLDeviceProductIdentifier** *(string) --*

                  Specifies the model number of device that the VTL device emulates.

                - **DeviceiSCSIAttributes** *(dict) --*

                  A list of iSCSI information about a VTL device.

                  - **TargetARN** *(string) --*

                    Specifies the unique Amazon Resource Name (ARN) that encodes the iSCSI qualified
                    name(iqn) of a tape drive or media changer target.

                  - **NetworkInterfaceId** *(string) --*

                    The network interface identifier of the VTL device.

                  - **NetworkInterfacePort** *(integer) --*

                    The port used to communicate with iSCSI VTL device targets.

                  - **ChapEnabled** *(boolean) --*

                    Indicates whether mutual CHAP is enabled for the iSCSI target.

            - **NextToken** *(string) --*

              A token to resume pagination.
        """


class ListFileSharesPaginator(Boto3Paginator):
    """
    Paginator for `list_file_shares`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        GatewayARN: str = None,
        PaginationConfig: ListFileSharesPaginatePaginationConfigTypeDef = None,
    ) -> ListFileSharesPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`StorageGateway.Client.list_file_shares`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/storagegateway-2013-06-30/ListFileShares>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              GatewayARN='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type GatewayARN: string
        :param GatewayARN:

          The Amazon resource Name (ARN) of the gateway whose file shares you want to list. If this
          field is not present, all file shares under your account are listed.

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
                'Marker': 'string',
                'FileShareInfoList': [
                    {
                        'FileShareType': 'NFS'|'SMB',
                        'FileShareARN': 'string',
                        'FileShareId': 'string',
                        'FileShareStatus': 'string',
                        'GatewayARN': 'string'
                    },
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            ListFileShareOutput

            - **Marker** *(string) --*

              If the request includes ``Marker`` , the response returns that value in this field.

            - **FileShareInfoList** *(list) --*

              An array of information about the file gateway's file shares.

              - *(dict) --*

                Describes a file share.

                - **FileShareType** *(string) --*

                  The type of the file share.

                - **FileShareARN** *(string) --*

                  The Amazon Resource Name (ARN) of the file share.

                - **FileShareId** *(string) --*

                  The ID of the file share.

                - **FileShareStatus** *(string) --*

                  The status of the file share. Possible values are ``CREATING`` , ``UPDATING`` ,
                  ``AVAILABLE`` and ``DELETING`` .

                - **GatewayARN** *(string) --*

                  The Amazon Resource Name (ARN) of the gateway. Use the  ListGateways operation to
                  return a list of gateways for your account and AWS Region.

            - **NextToken** *(string) --*

              A token to resume pagination.
        """


class ListGatewaysPaginator(Boto3Paginator):
    """
    Paginator for `list_gateways`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: ListGatewaysPaginatePaginationConfigTypeDef = None
    ) -> ListGatewaysPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`StorageGateway.Client.list_gateways`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/storagegateway-2013-06-30/ListGateways>`_

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
                'Gateways': [
                    {
                        'GatewayId': 'string',
                        'GatewayARN': 'string',
                        'GatewayType': 'string',
                        'GatewayOperationalState': 'string',
                        'GatewayName': 'string',
                        'Ec2InstanceId': 'string',
                        'Ec2InstanceRegion': 'string'
                    },
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **Gateways** *(list) --*

              An array of  GatewayInfo objects.

              - *(dict) --*

                Describes a gateway object.

                - **GatewayId** *(string) --*

                  The unique identifier assigned to your gateway during activation. This ID becomes
                  part of the gateway Amazon Resource Name (ARN), which you use as input for other
                  operations.

                - **GatewayARN** *(string) --*

                  The Amazon Resource Name (ARN) of the gateway. Use the  ListGateways operation to
                  return a list of gateways for your account and AWS Region.

                - **GatewayType** *(string) --*

                  The type of the gateway.

                - **GatewayOperationalState** *(string) --*

                  The state of the gateway.

                  Valid Values: DISABLED or ACTIVE

                - **GatewayName** *(string) --*

                  The name of the gateway.

                - **Ec2InstanceId** *(string) --*

                  The ID of the Amazon EC2 instance that was used to launch the gateway.

                - **Ec2InstanceRegion** *(string) --*

                  The AWS Region where the Amazon EC2 instance is located.

            - **NextToken** *(string) --*

              A token to resume pagination.
        """


class ListTagsForResourcePaginator(Boto3Paginator):
    """
    Paginator for `list_tags_for_resource`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ResourceARN: str,
        PaginationConfig: ListTagsForResourcePaginatePaginationConfigTypeDef = None,
    ) -> ListTagsForResourcePaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`StorageGateway.Client.list_tags_for_resource`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/storagegateway-2013-06-30/ListTagsForResource>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              ResourceARN='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type ResourceARN: string
        :param ResourceARN: **[REQUIRED]**

          The Amazon Resource Name (ARN) of the resource for which you want to list tags.

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
                'ResourceARN': 'string',
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

            ListTagsForResourceOutput

            - **ResourceARN** *(string) --*

              he Amazon Resource Name (ARN) of the resource for which you want to list tags.

            - **Tags** *(list) --*

              An array that contains the tags for the specified resource.

              - *(dict) --*

                A key-value pair that helps you manage, filter, and search for your resource.
                Allowed characters: letters, white space, and numbers, representable in UTF-8, and
                the following characters: + - = . _ : /

                - **Key** *(string) --*

                  Tag key (String). The key can't start with aws:.

                - **Value** *(string) --*

                  Value of the tag key.

            - **NextToken** *(string) --*

              A token to resume pagination.
        """


class ListTapesPaginator(Boto3Paginator):
    """
    Paginator for `list_tapes`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        TapeARNs: List[str] = None,
        PaginationConfig: ListTapesPaginatePaginationConfigTypeDef = None,
    ) -> ListTapesPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`StorageGateway.Client.list_tapes`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/storagegateway-2013-06-30/ListTapes>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              TapeARNs=[
                  'string',
              ],
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type TapeARNs: list
        :param TapeARNs:

          The Amazon Resource Name (ARN) of each of the tapes you want to list. If you don't specify
          a tape ARN, the response lists all tapes in both your VTL and VTS.

          - *(string) --*

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
                'TapeInfos': [
                    {
                        'TapeARN': 'string',
                        'TapeBarcode': 'string',
                        'TapeSizeInBytes': 123,
                        'TapeStatus': 'string',
                        'GatewayARN': 'string',
                        'PoolId': 'string'
                    },
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            A JSON object containing the following fields:

            *  ListTapesOutput$Marker

            *  ListTapesOutput$VolumeInfos

            - **TapeInfos** *(list) --*

              An array of  TapeInfo objects, where each object describes an a single tape. If there
              not tapes in the tape library or VTS, then the ``TapeInfos`` is an empty array.

              - *(dict) --*

                Describes a virtual tape.

                - **TapeARN** *(string) --*

                  The Amazon Resource Name (ARN) of a virtual tape.

                - **TapeBarcode** *(string) --*

                  The barcode that identifies a specific virtual tape.

                - **TapeSizeInBytes** *(integer) --*

                  The size, in bytes, of a virtual tape.

                - **TapeStatus** *(string) --*

                  The status of the tape.

                - **GatewayARN** *(string) --*

                  The Amazon Resource Name (ARN) of the gateway. Use the  ListGateways operation to
                  return a list of gateways for your account and AWS Region.

                - **PoolId** *(string) --*

                  The ID of the pool that you want to add your tape to for archiving. The tape in
                  this pool is archived in the S3 storage class that is associated with the pool.
                  When you use your backup application to eject the tape, the tape is archived
                  directly into the storage class (Glacier or Deep Archive) that corresponds to the
                  pool.

                  Valid values: "GLACIER", "DEEP_ARCHIVE"

            - **NextToken** *(string) --*

              A token to resume pagination.
        """


class ListVolumesPaginator(Boto3Paginator):
    """
    Paginator for `list_volumes`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        GatewayARN: str = None,
        PaginationConfig: ListVolumesPaginatePaginationConfigTypeDef = None,
    ) -> ListVolumesPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`StorageGateway.Client.list_volumes`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/storagegateway-2013-06-30/ListVolumes>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              GatewayARN='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type GatewayARN: string
        :param GatewayARN:

          The Amazon Resource Name (ARN) of the gateway. Use the  ListGateways operation to return a
          list of gateways for your account and AWS Region.

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
                'GatewayARN': 'string',
                'VolumeInfos': [
                    {
                        'VolumeARN': 'string',
                        'VolumeId': 'string',
                        'GatewayARN': 'string',
                        'GatewayId': 'string',
                        'VolumeType': 'string',
                        'VolumeSizeInBytes': 123,
                        'VolumeAttachmentStatus': 'string'
                    },
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            A JSON object containing the following fields:

            *  ListVolumesOutput$Marker

            *  ListVolumesOutput$VolumeInfos

            - **GatewayARN** *(string) --*

              The Amazon Resource Name (ARN) of the gateway. Use the  ListGateways operation to
              return a list of gateways for your account and AWS Region.

            - **VolumeInfos** *(list) --*

              An array of  VolumeInfo objects, where each object describes an iSCSI volume. If no
              volumes are defined for the gateway, then ``VolumeInfos`` is an empty array "[]".

              - *(dict) --*

                Describes a storage volume object.

                - **VolumeARN** *(string) --*

                  The Amazon Resource Name (ARN) for the storage volume. For example, the following
                  is a valid ARN:

                   ``arn:aws:storagegateway:us-east-2:111122223333:gateway/sgw-12A3456B/volume/vol-1122AABB``

                  Valid Values: 50 to 500 lowercase letters, numbers, periods (.), and hyphens (-).

                - **VolumeId** *(string) --*

                  The unique identifier assigned to the volume. This ID becomes part of the volume
                  Amazon Resource Name (ARN), which you use as input for other operations.

                  Valid Values: 50 to 500 lowercase letters, numbers, periods (.), and hyphens (-).

                - **GatewayARN** *(string) --*

                  The Amazon Resource Name (ARN) of the gateway. Use the  ListGateways operation to
                  return a list of gateways for your account and AWS Region.

                - **GatewayId** *(string) --*

                  The unique identifier assigned to your gateway during activation. This ID becomes
                  part of the gateway Amazon Resource Name (ARN), which you use as input for other
                  operations.

                  Valid Values: 50 to 500 lowercase letters, numbers, periods (.), and hyphens (-).

                - **VolumeType** *(string) --*

                  One of the VolumeType enumeration values describing the type of the volume.

                - **VolumeSizeInBytes** *(integer) --*

                  The size of the volume in bytes.

                  Valid Values: 50 to 500 lowercase letters, numbers, periods (.), and hyphens (-).

                - **VolumeAttachmentStatus** *(string) --*

                  One of the VolumeStatus values that indicates the state of the storage volume.

            - **NextToken** *(string) --*

              A token to resume pagination.
        """
