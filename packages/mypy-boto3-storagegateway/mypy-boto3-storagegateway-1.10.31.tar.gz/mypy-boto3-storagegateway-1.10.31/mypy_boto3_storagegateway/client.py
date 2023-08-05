"Main interface for storagegateway service Client"
from __future__ import annotations

from typing import Any, Dict, List
from botocore.client import BaseClient
from botocore.exceptions import ClientError as Boto3ClientError
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3.type_defs import Literal, overload

# pylint: disable=import-self
import mypy_boto3_storagegateway.client as client_scope

# pylint: disable=import-self
import mypy_boto3_storagegateway.paginator as paginator_scope
from mypy_boto3_storagegateway.type_defs import (
    ClientActivateGatewayResponseTypeDef,
    ClientActivateGatewayTagsTypeDef,
    ClientAddCacheResponseTypeDef,
    ClientAddTagsToResourceResponseTypeDef,
    ClientAddTagsToResourceTagsTypeDef,
    ClientAddUploadBufferResponseTypeDef,
    ClientAddWorkingStorageResponseTypeDef,
    ClientAssignTapePoolResponseTypeDef,
    ClientAttachVolumeResponseTypeDef,
    ClientCancelArchivalResponseTypeDef,
    ClientCancelRetrievalResponseTypeDef,
    ClientCreateCachedIscsiVolumeResponseTypeDef,
    ClientCreateCachedIscsiVolumeTagsTypeDef,
    ClientCreateNfsFileShareNFSFileShareDefaultsTypeDef,
    ClientCreateNfsFileShareResponseTypeDef,
    ClientCreateNfsFileShareTagsTypeDef,
    ClientCreateSmbFileShareResponseTypeDef,
    ClientCreateSmbFileShareTagsTypeDef,
    ClientCreateSnapshotFromVolumeRecoveryPointResponseTypeDef,
    ClientCreateSnapshotFromVolumeRecoveryPointTagsTypeDef,
    ClientCreateSnapshotResponseTypeDef,
    ClientCreateSnapshotTagsTypeDef,
    ClientCreateStoredIscsiVolumeResponseTypeDef,
    ClientCreateStoredIscsiVolumeTagsTypeDef,
    ClientCreateTapeWithBarcodeResponseTypeDef,
    ClientCreateTapeWithBarcodeTagsTypeDef,
    ClientCreateTapesResponseTypeDef,
    ClientCreateTapesTagsTypeDef,
    ClientDeleteBandwidthRateLimitResponseTypeDef,
    ClientDeleteChapCredentialsResponseTypeDef,
    ClientDeleteFileShareResponseTypeDef,
    ClientDeleteGatewayResponseTypeDef,
    ClientDeleteSnapshotScheduleResponseTypeDef,
    ClientDeleteTapeArchiveResponseTypeDef,
    ClientDeleteTapeResponseTypeDef,
    ClientDeleteVolumeResponseTypeDef,
    ClientDescribeAvailabilityMonitorTestResponseTypeDef,
    ClientDescribeBandwidthRateLimitResponseTypeDef,
    ClientDescribeCacheResponseTypeDef,
    ClientDescribeCachedIscsiVolumesResponseTypeDef,
    ClientDescribeChapCredentialsResponseTypeDef,
    ClientDescribeGatewayInformationResponseTypeDef,
    ClientDescribeMaintenanceStartTimeResponseTypeDef,
    ClientDescribeNfsFileSharesResponseTypeDef,
    ClientDescribeSmbFileSharesResponseTypeDef,
    ClientDescribeSmbSettingsResponseTypeDef,
    ClientDescribeSnapshotScheduleResponseTypeDef,
    ClientDescribeStoredIscsiVolumesResponseTypeDef,
    ClientDescribeTapeArchivesResponseTypeDef,
    ClientDescribeTapeRecoveryPointsResponseTypeDef,
    ClientDescribeTapesResponseTypeDef,
    ClientDescribeUploadBufferResponseTypeDef,
    ClientDescribeVtlDevicesResponseTypeDef,
    ClientDescribeWorkingStorageResponseTypeDef,
    ClientDetachVolumeResponseTypeDef,
    ClientDisableGatewayResponseTypeDef,
    ClientJoinDomainResponseTypeDef,
    ClientListFileSharesResponseTypeDef,
    ClientListGatewaysResponseTypeDef,
    ClientListLocalDisksResponseTypeDef,
    ClientListTagsForResourceResponseTypeDef,
    ClientListTapesResponseTypeDef,
    ClientListVolumeInitiatorsResponseTypeDef,
    ClientListVolumeRecoveryPointsResponseTypeDef,
    ClientListVolumesResponseTypeDef,
    ClientNotifyWhenUploadedResponseTypeDef,
    ClientRefreshCacheResponseTypeDef,
    ClientRemoveTagsFromResourceResponseTypeDef,
    ClientResetCacheResponseTypeDef,
    ClientRetrieveTapeArchiveResponseTypeDef,
    ClientRetrieveTapeRecoveryPointResponseTypeDef,
    ClientSetLocalConsolePasswordResponseTypeDef,
    ClientSetSmbGuestPasswordResponseTypeDef,
    ClientShutdownGatewayResponseTypeDef,
    ClientStartAvailabilityMonitorTestResponseTypeDef,
    ClientStartGatewayResponseTypeDef,
    ClientUpdateBandwidthRateLimitResponseTypeDef,
    ClientUpdateChapCredentialsResponseTypeDef,
    ClientUpdateGatewayInformationResponseTypeDef,
    ClientUpdateGatewaySoftwareNowResponseTypeDef,
    ClientUpdateMaintenanceStartTimeResponseTypeDef,
    ClientUpdateNfsFileShareNFSFileShareDefaultsTypeDef,
    ClientUpdateNfsFileShareResponseTypeDef,
    ClientUpdateSmbFileShareResponseTypeDef,
    ClientUpdateSmbSecurityStrategyResponseTypeDef,
    ClientUpdateSnapshotScheduleResponseTypeDef,
    ClientUpdateSnapshotScheduleTagsTypeDef,
    ClientUpdateVtlDeviceTypeResponseTypeDef,
)


__all__ = ("Client",)


class Client(BaseClient):
    exceptions: client_scope.Exceptions

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def activate_gateway(
        self,
        ActivationKey: str,
        GatewayName: str,
        GatewayTimezone: str,
        GatewayRegion: str,
        GatewayType: str = None,
        TapeDriveType: str = None,
        MediumChangerType: str = None,
        Tags: List[ClientActivateGatewayTagsTypeDef] = None,
    ) -> ClientActivateGatewayResponseTypeDef:
        """
        Activates the gateway you previously deployed on your host. In the activation process, you
        specify information such as the AWS Region that you want to use for storing snapshots or
        tapes, the time zone for scheduled snapshots the gateway snapshot schedule window, an
        activation key, and a name for your gateway. The activation process also associates your
        gateway with your account; for more information, see  UpdateGatewayInformation .

        .. note::

          You must turn on the gateway VM before you can activate your gateway.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/storagegateway-2013-06-30/ActivateGateway>`_

        **Request Syntax**
        ::

          response = client.activate_gateway(
              ActivationKey='string',
              GatewayName='string',
              GatewayTimezone='string',
              GatewayRegion='string',
              GatewayType='string',
              TapeDriveType='string',
              MediumChangerType='string',
              Tags=[
                  {
                      'Key': 'string',
                      'Value': 'string'
                  },
              ]
          )
        :type ActivationKey: string
        :param ActivationKey: **[REQUIRED]**

          Your gateway activation key. You can obtain the activation key by sending an HTTP GET
          request with redirects enabled to the gateway IP address (port 80). The redirect URL
          returned in the response provides you the activation key for your gateway in the query
          string parameter ``activationKey`` . It may also include other activation-related
          parameters, however, these are merely defaults -- the arguments you pass to the
          ``ActivateGateway`` API call determine the actual configuration of your gateway.

          For more information, see
          https://docs.aws.amazon.com/storagegateway/latest/userguide/get-activation-key.html in the
          Storage Gateway User Guide.

        :type GatewayName: string
        :param GatewayName: **[REQUIRED]**

          The name you configured for your gateway.

        :type GatewayTimezone: string
        :param GatewayTimezone: **[REQUIRED]**

          A value that indicates the time zone you want to set for the gateway. The time zone is of
          the format "GMT-hr:mm" or "GMT+hr:mm". For example, GMT-4:00 indicates the time is 4 hours
          behind GMT. GMT+2:00 indicates the time is 2 hours ahead of GMT. The time zone is used,
          for example, for scheduling snapshots and your gateway's maintenance schedule.

        :type GatewayRegion: string
        :param GatewayRegion: **[REQUIRED]**

          A value that indicates the AWS Region where you want to store your data. The gateway AWS
          Region specified must be the same AWS Region as the AWS Region in your ``Host`` header in
          the request. For more information about available AWS Regions and endpoints for AWS
          Storage Gateway, see `Regions and Endpoints
          <https://docs.aws.amazon.com/general/latest/gr/rande.html#sg_region>`__ in the *Amazon Web
          Services Glossary* .

          Valid Values: See `AWS Storage Gateway Regions and Endpoints
          <https://docs.aws.amazon.com/general/latest/gr/rande.html#sg_region>`__ in the AWS General
          Reference.

        :type GatewayType: string
        :param GatewayType:

          A value that defines the type of gateway to activate. The type specified is critical to
          all later functions of the gateway and cannot be changed after activation. The default
          value is ``CACHED`` .

          Valid Values: "STORED", "CACHED", "VTL", "FILE_S3"

        :type TapeDriveType: string
        :param TapeDriveType:

          The value that indicates the type of tape drive to use for tape gateway. This field is
          optional.

          Valid Values: "IBM-ULT3580-TD5"

        :type MediumChangerType: string
        :param MediumChangerType:

          The value that indicates the type of medium changer to use for tape gateway. This field is
          optional.

          Valid Values: "STK-L700", "AWS-Gateway-VTL"

        :type Tags: list
        :param Tags:

          A list of up to 50 tags that you can assign to the gateway. Each tag is a key-value pair.

          .. note::

            Valid characters for key and value are letters, spaces, and numbers that can be
            represented in UTF-8 format, and the following special characters: + - =
                 . _ : / @. The
            maximum length of a tag's key is 128 characters, and the maximum length for a tag's
            value is 256 characters.

          - *(dict) --*

            A key-value pair that helps you manage, filter, and search for your resource. Allowed
            characters: letters, white space, and numbers, representable in UTF-8, and the following
            characters: + - = . _ : /

            - **Key** *(string) --* **[REQUIRED]**

              Tag key (String). The key can't start with aws:.

            - **Value** *(string) --* **[REQUIRED]**

              Value of the tag key.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'GatewayARN': 'string'
            }
          **Response Structure**

          - *(dict) --*

            AWS Storage Gateway returns the Amazon Resource Name (ARN) of the activated gateway. It
            is a string made of information such as your account, gateway name, and AWS Region. This
            ARN is used to reference the gateway in other API operations as well as resource-based
            authorization.

            .. note::

              For gateways activated prior to September 02, 2015, the gateway ARN contains the
              gateway name rather than the gateway ID. Changing the name of the gateway has no
              effect on the gateway ARN.

            - **GatewayARN** *(string) --*

              The Amazon Resource Name (ARN) of the gateway. Use the  ListGateways operation to
              return a list of gateways for your account and AWS Region.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def add_cache(self, GatewayARN: str, DiskIds: List[str]) -> ClientAddCacheResponseTypeDef:
        """
        Configures one or more gateway local disks as cache for a gateway. This operation is only
        supported in the cached volume, tape and file gateway type (see `Storage Gateway Concepts
        <https://docs.aws.amazon.com/storagegateway/latest/userguide/StorageGatewayConcepts.html>`__
        ).

        In the request, you specify the gateway Amazon Resource Name (ARN) to which you want to add
        cache, and one or more disk IDs that you want to configure as cache.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/storagegateway-2013-06-30/AddCache>`_

        **Request Syntax**
        ::

          response = client.add_cache(
              GatewayARN='string',
              DiskIds=[
                  'string',
              ]
          )
        :type GatewayARN: string
        :param GatewayARN: **[REQUIRED]**

          The Amazon Resource Name (ARN) of the gateway. Use the  ListGateways operation to return a
          list of gateways for your account and AWS Region.

        :type DiskIds: list
        :param DiskIds: **[REQUIRED]**

          An array of strings that identify disks that are to be configured as working storage. Each
          string have a minimum length of 1 and maximum length of 300. You can get the disk IDs from
          the  ListLocalDisks API.

          - *(string) --*

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'GatewayARN': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **GatewayARN** *(string) --*

              The Amazon Resource Name (ARN) of the gateway. Use the  ListGateways operation to
              return a list of gateways for your account and AWS Region.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def add_tags_to_resource(
        self, ResourceARN: str, Tags: List[ClientAddTagsToResourceTagsTypeDef]
    ) -> ClientAddTagsToResourceResponseTypeDef:
        """
        Adds one or more tags to the specified resource. You use tags to add metadata to resources,
        which you can use to categorize these resources. For example, you can categorize resources
        by purpose, owner, environment, or team. Each tag consists of a key and a value, which you
        define. You can add tags to the following AWS Storage Gateway resources:

        * Storage gateways of all types

        * Storage volumes

        * Virtual tapes

        * NFS and SMB file shares

        You can create a maximum of 50 tags for each resource. Virtual tapes and storage volumes
        that are recovered to a new gateway maintain their tags.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/storagegateway-2013-06-30/AddTagsToResource>`_

        **Request Syntax**
        ::

          response = client.add_tags_to_resource(
              ResourceARN='string',
              Tags=[
                  {
                      'Key': 'string',
                      'Value': 'string'
                  },
              ]
          )
        :type ResourceARN: string
        :param ResourceARN: **[REQUIRED]**

          The Amazon Resource Name (ARN) of the resource you want to add tags to.

        :type Tags: list
        :param Tags: **[REQUIRED]**

          The key-value pair that represents the tag you want to add to the resource. The value can
          be an empty string.

          .. note::

            Valid characters for key and value are letters, spaces, and numbers representable in
            UTF-8 format, and the following special characters: + - =
                 . _ : / @. The maximum length
            of a tag's key is 128 characters, and the maximum length for a tag's value is 256.

          - *(dict) --*

            A key-value pair that helps you manage, filter, and search for your resource. Allowed
            characters: letters, white space, and numbers, representable in UTF-8, and the following
            characters: + - = . _ : /

            - **Key** *(string) --* **[REQUIRED]**

              Tag key (String). The key can't start with aws:.

            - **Value** *(string) --* **[REQUIRED]**

              Value of the tag key.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'ResourceARN': 'string'
            }
          **Response Structure**

          - *(dict) --*

            AddTagsToResourceOutput

            - **ResourceARN** *(string) --*

              The Amazon Resource Name (ARN) of the resource you want to add tags to.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def add_upload_buffer(
        self, GatewayARN: str, DiskIds: List[str]
    ) -> ClientAddUploadBufferResponseTypeDef:
        """
        Configures one or more gateway local disks as upload buffer for a specified gateway. This
        operation is supported for the stored volume, cached volume and tape gateway types.

        In the request, you specify the gateway Amazon Resource Name (ARN) to which you want to add
        upload buffer, and one or more disk IDs that you want to configure as upload buffer.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/storagegateway-2013-06-30/AddUploadBuffer>`_

        **Request Syntax**
        ::

          response = client.add_upload_buffer(
              GatewayARN='string',
              DiskIds=[
                  'string',
              ]
          )
        :type GatewayARN: string
        :param GatewayARN: **[REQUIRED]**

          The Amazon Resource Name (ARN) of the gateway. Use the  ListGateways operation to return a
          list of gateways for your account and AWS Region.

        :type DiskIds: list
        :param DiskIds: **[REQUIRED]**

          An array of strings that identify disks that are to be configured as working storage. Each
          string have a minimum length of 1 and maximum length of 300. You can get the disk IDs from
          the  ListLocalDisks API.

          - *(string) --*

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'GatewayARN': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **GatewayARN** *(string) --*

              The Amazon Resource Name (ARN) of the gateway. Use the  ListGateways operation to
              return a list of gateways for your account and AWS Region.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def add_working_storage(
        self, GatewayARN: str, DiskIds: List[str]
    ) -> ClientAddWorkingStorageResponseTypeDef:
        """
        Configures one or more gateway local disks as working storage for a gateway. This operation
        is only supported in the stored volume gateway type. This operation is deprecated in cached
        volume API version 20120630. Use  AddUploadBuffer instead.

        .. note::

          Working storage is also referred to as upload buffer. You can also use the
          AddUploadBuffer operation to add upload buffer to a stored volume gateway.

        In the request, you specify the gateway Amazon Resource Name (ARN) to which you want to add
        working storage, and one or more disk IDs that you want to configure as working storage.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/storagegateway-2013-06-30/AddWorkingStorage>`_

        **Request Syntax**
        ::

          response = client.add_working_storage(
              GatewayARN='string',
              DiskIds=[
                  'string',
              ]
          )
        :type GatewayARN: string
        :param GatewayARN: **[REQUIRED]**

          The Amazon Resource Name (ARN) of the gateway. Use the  ListGateways operation to return a
          list of gateways for your account and AWS Region.

        :type DiskIds: list
        :param DiskIds: **[REQUIRED]**

          An array of strings that identify disks that are to be configured as working storage. Each
          string have a minimum length of 1 and maximum length of 300. You can get the disk IDs from
          the  ListLocalDisks API.

          - *(string) --*

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'GatewayARN': 'string'
            }
          **Response Structure**

          - *(dict) --*

            A JSON object containing the of the gateway for which working storage was configured.

            - **GatewayARN** *(string) --*

              The Amazon Resource Name (ARN) of the gateway. Use the  ListGateways operation to
              return a list of gateways for your account and AWS Region.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def assign_tape_pool(self, TapeARN: str, PoolId: str) -> ClientAssignTapePoolResponseTypeDef:
        """
        Assigns a tape to a tape pool for archiving. The tape assigned to a pool is archived in the
        S3 storage class that is associated with the pool. When you use your backup application to
        eject the tape, the tape is archived directly into the S3 storage class (Glacier or Deep
        Archive) that corresponds to the pool.

        Valid values: "GLACIER", "DEEP_ARCHIVE"

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/storagegateway-2013-06-30/AssignTapePool>`_

        **Request Syntax**
        ::

          response = client.assign_tape_pool(
              TapeARN='string',
              PoolId='string'
          )
        :type TapeARN: string
        :param TapeARN: **[REQUIRED]**

          The unique Amazon Resource Name (ARN) of the virtual tape that you want to add to the tape
          pool.

        :type PoolId: string
        :param PoolId: **[REQUIRED]**

          The ID of the pool that you want to add your tape to for archiving. The tape in this pool
          is archived in the S3 storage class that is associated with the pool. When you use your
          backup application to eject the tape, the tape is archived directly into the storage class
          (Glacier or Deep Archive) that corresponds to the pool.

          Valid values: "GLACIER", "DEEP_ARCHIVE"

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'TapeARN': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **TapeARN** *(string) --*

              The unique Amazon Resource Names (ARN) of the virtual tape that was added to the tape
              pool.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def attach_volume(
        self,
        GatewayARN: str,
        VolumeARN: str,
        NetworkInterfaceId: str,
        TargetName: str = None,
        DiskId: str = None,
    ) -> ClientAttachVolumeResponseTypeDef:
        """
        Connects a volume to an iSCSI connection and then attaches the volume to the specified
        gateway. Detaching and attaching a volume enables you to recover your data from one gateway
        to a different gateway without creating a snapshot. It also makes it easier to move your
        volumes from an on-premises gateway to a gateway hosted on an Amazon EC2 instance.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/storagegateway-2013-06-30/AttachVolume>`_

        **Request Syntax**
        ::

          response = client.attach_volume(
              GatewayARN='string',
              TargetName='string',
              VolumeARN='string',
              NetworkInterfaceId='string',
              DiskId='string'
          )
        :type GatewayARN: string
        :param GatewayARN: **[REQUIRED]**

          The Amazon Resource Name (ARN) of the gateway that you want to attach the volume to.

        :type TargetName: string
        :param TargetName:

          The name of the iSCSI target used by an initiator to connect to a volume and used as a
          suffix for the target ARN. For example, specifying ``TargetName`` as *myvolume* results in
          the target ARN of
          ``arn:aws:storagegateway:us-east-2:111122223333:gateway/sgw-12A3456B/target/iqn.1997-05.com.amazon:myvolume``
          . The target name must be unique across all volumes on a gateway.

          If you don't specify a value, Storage Gateway uses the value that was previously used for
          this volume as the new target name.

        :type VolumeARN: string
        :param VolumeARN: **[REQUIRED]**

          The Amazon Resource Name (ARN) of the volume to attach to the specified gateway.

        :type NetworkInterfaceId: string
        :param NetworkInterfaceId: **[REQUIRED]**

          The network interface of the gateway on which to expose the iSCSI target. Only IPv4
          addresses are accepted. Use  DescribeGatewayInformation to get a list of the network
          interfaces available on a gateway.

          Valid Values: A valid IP address.

        :type DiskId: string
        :param DiskId:

          The unique device ID or other distinguishing data that identifies the local disk used to
          create the volume. This value is only required when you are attaching a stored volume.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'VolumeARN': 'string',
                'TargetARN': 'string'
            }
          **Response Structure**

          - *(dict) --*

            AttachVolumeOutput

            - **VolumeARN** *(string) --*

              The Amazon Resource Name (ARN) of the volume that was attached to the gateway.

            - **TargetARN** *(string) --*

              The Amazon Resource Name (ARN) of the volume target, which includes the iSCSI name for
              the initiator that was used to connect to the target.
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
    def cancel_archival(self, GatewayARN: str, TapeARN: str) -> ClientCancelArchivalResponseTypeDef:
        """
        Cancels archiving of a virtual tape to the virtual tape shelf (VTS) after the archiving
        process is initiated. This operation is only supported in the tape gateway type.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/storagegateway-2013-06-30/CancelArchival>`_

        **Request Syntax**
        ::

          response = client.cancel_archival(
              GatewayARN='string',
              TapeARN='string'
          )
        :type GatewayARN: string
        :param GatewayARN: **[REQUIRED]**

          The Amazon Resource Name (ARN) of the gateway. Use the  ListGateways operation to return a
          list of gateways for your account and AWS Region.

        :type TapeARN: string
        :param TapeARN: **[REQUIRED]**

          The Amazon Resource Name (ARN) of the virtual tape you want to cancel archiving for.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'TapeARN': 'string'
            }
          **Response Structure**

          - *(dict) --*

            CancelArchivalOutput

            - **TapeARN** *(string) --*

              The Amazon Resource Name (ARN) of the virtual tape for which archiving was canceled.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def cancel_retrieval(
        self, GatewayARN: str, TapeARN: str
    ) -> ClientCancelRetrievalResponseTypeDef:
        """
        Cancels retrieval of a virtual tape from the virtual tape shelf (VTS) to a gateway after the
        retrieval process is initiated. The virtual tape is returned to the VTS. This operation is
        only supported in the tape gateway type.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/storagegateway-2013-06-30/CancelRetrieval>`_

        **Request Syntax**
        ::

          response = client.cancel_retrieval(
              GatewayARN='string',
              TapeARN='string'
          )
        :type GatewayARN: string
        :param GatewayARN: **[REQUIRED]**

          The Amazon Resource Name (ARN) of the gateway. Use the  ListGateways operation to return a
          list of gateways for your account and AWS Region.

        :type TapeARN: string
        :param TapeARN: **[REQUIRED]**

          The Amazon Resource Name (ARN) of the virtual tape you want to cancel retrieval for.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'TapeARN': 'string'
            }
          **Response Structure**

          - *(dict) --*

            CancelRetrievalOutput

            - **TapeARN** *(string) --*

              The Amazon Resource Name (ARN) of the virtual tape for which retrieval was canceled.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_cached_iscsi_volume(
        self,
        GatewayARN: str,
        VolumeSizeInBytes: int,
        TargetName: str,
        NetworkInterfaceId: str,
        ClientToken: str,
        SnapshotId: str = None,
        SourceVolumeARN: str = None,
        KMSEncrypted: bool = None,
        KMSKey: str = None,
        Tags: List[ClientCreateCachedIscsiVolumeTagsTypeDef] = None,
    ) -> ClientCreateCachedIscsiVolumeResponseTypeDef:
        """
        Creates a cached volume on a specified cached volume gateway. This operation is only
        supported in the cached volume gateway type.

        .. note::

          Cache storage must be allocated to the gateway before you can create a cached volume. Use
          the  AddCache operation to add cache storage to a gateway.

        In the request, you must specify the gateway, size of the volume in bytes, the iSCSI target
        name, an IP address on which to expose the target, and a unique client token. In response,
        the gateway creates the volume and returns information about it. This information includes
        the volume Amazon Resource Name (ARN), its size, and the iSCSI target ARN that initiators
        can use to connect to the volume target.

        Optionally, you can provide the ARN for an existing volume as the ``SourceVolumeARN`` for
        this cached volume, which creates an exact copy of the existing volume’s latest recovery
        point. The ``VolumeSizeInBytes`` value must be equal to or larger than the size of the
        copied volume, in bytes.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/storagegateway-2013-06-30/CreateCachediSCSIVolume>`_

        **Request Syntax**
        ::

          response = client.create_cached_iscsi_volume(
              GatewayARN='string',
              VolumeSizeInBytes=123,
              SnapshotId='string',
              TargetName='string',
              SourceVolumeARN='string',
              NetworkInterfaceId='string',
              ClientToken='string',
              KMSEncrypted=True|False,
              KMSKey='string',
              Tags=[
                  {
                      'Key': 'string',
                      'Value': 'string'
                  },
              ]
          )
        :type GatewayARN: string
        :param GatewayARN: **[REQUIRED]**

          The Amazon Resource Name (ARN) of the gateway. Use the  ListGateways operation to return a
          list of gateways for your account and AWS Region.

        :type VolumeSizeInBytes: integer
        :param VolumeSizeInBytes: **[REQUIRED]**

          The size of the volume in bytes.

        :type SnapshotId: string
        :param SnapshotId:

          The snapshot ID (e.g. "snap-1122aabb") of the snapshot to restore as the new cached
          volume. Specify this field if you want to create the iSCSI storage volume from a snapshot
          otherwise do not include this field. To list snapshots for your account use
          `DescribeSnapshots
          <https://docs.aws.amazon.com/AWSEC2/latest/APIReference/ApiReference-query-DescribeSnapshots.html>`__
          in the *Amazon Elastic Compute Cloud API Reference* .

        :type TargetName: string
        :param TargetName: **[REQUIRED]**

          The name of the iSCSI target used by an initiator to connect to a volume and used as a
          suffix for the target ARN. For example, specifying ``TargetName`` as *myvolume* results in
          the target ARN of
          ``arn:aws:storagegateway:us-east-2:111122223333:gateway/sgw-12A3456B/target/iqn.1997-05.com.amazon:myvolume``
          . The target name must be unique across all volumes on a gateway.

          If you don't specify a value, Storage Gateway uses the value that was previously used for
          this volume as the new target name.

        :type SourceVolumeARN: string
        :param SourceVolumeARN:

          The ARN for an existing volume. Specifying this ARN makes the new volume into an exact
          copy of the specified existing volume's latest recovery point. The ``VolumeSizeInBytes``
          value for this new volume must be equal to or larger than the size of the existing volume,
          in bytes.

        :type NetworkInterfaceId: string
        :param NetworkInterfaceId: **[REQUIRED]**

          The network interface of the gateway on which to expose the iSCSI target. Only IPv4
          addresses are accepted. Use  DescribeGatewayInformation to get a list of the network
          interfaces available on a gateway.

          Valid Values: A valid IP address.

        :type ClientToken: string
        :param ClientToken: **[REQUIRED]**

          A unique identifier that you use to retry a request. If you retry a request, use the same
          ``ClientToken`` you specified in the initial request.

        :type KMSEncrypted: boolean
        :param KMSEncrypted:

          True to use Amazon S3 server side encryption with your own AWS KMS key, or false to use a
          key managed by Amazon S3. Optional.

        :type KMSKey: string
        :param KMSKey:

          The Amazon Resource Name (ARN) of the AWS KMS key used for Amazon S3 server side
          encryption. This value can only be set when KMSEncrypted is true. Optional.

        :type Tags: list
        :param Tags:

          A list of up to 50 tags that you can assign to a cached volume. Each tag is a key-value
          pair.

          .. note::

            Valid characters for key and value are letters, spaces, and numbers that you can
            represent in UTF-8 format, and the following special characters: + - =
                 . _ : / @. The
            maximum length of a tag's key is 128 characters, and the maximum length for a tag's
            value is 256 characters.

          - *(dict) --*

            A key-value pair that helps you manage, filter, and search for your resource. Allowed
            characters: letters, white space, and numbers, representable in UTF-8, and the following
            characters: + - = . _ : /

            - **Key** *(string) --* **[REQUIRED]**

              Tag key (String). The key can't start with aws:.

            - **Value** *(string) --* **[REQUIRED]**

              Value of the tag key.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'VolumeARN': 'string',
                'TargetARN': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **VolumeARN** *(string) --*

              The Amazon Resource Name (ARN) of the configured volume.

            - **TargetARN** *(string) --*

              The Amazon Resource Name (ARN) of the volume target, which includes the iSCSI name
              that initiators can use to connect to the target.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_nfs_file_share(
        self,
        ClientToken: str,
        GatewayARN: str,
        Role: str,
        LocationARN: str,
        NFSFileShareDefaults: ClientCreateNfsFileShareNFSFileShareDefaultsTypeDef = None,
        KMSEncrypted: bool = None,
        KMSKey: str = None,
        DefaultStorageClass: str = None,
        ObjectACL: Literal[
            "private",
            "public-read",
            "public-read-write",
            "authenticated-read",
            "bucket-owner-read",
            "bucket-owner-full-control",
            "aws-exec-read",
        ] = None,
        ClientList: List[str] = None,
        Squash: str = None,
        ReadOnly: bool = None,
        GuessMIMETypeEnabled: bool = None,
        RequesterPays: bool = None,
        Tags: List[ClientCreateNfsFileShareTagsTypeDef] = None,
    ) -> ClientCreateNfsFileShareResponseTypeDef:
        """
        Creates a Network File System (NFS) file share on an existing file gateway. In Storage
        Gateway, a file share is a file system mount point backed by Amazon S3 cloud storage.
        Storage Gateway exposes file shares using a NFS interface. This operation is only supported
        for file gateways.

        .. warning::

          File gateway requires AWS Security Token Service (AWS STS) to be activated to enable you
          create a file share. Make sure AWS STS is activated in the AWS Region you are creating
          your file gateway in. If AWS STS is not activated in the AWS Region, activate it. For
          information about how to activate AWS STS, see Activating and Deactivating AWS STS in an
          AWS Region in the AWS Identity and Access Management User Guide.

          File gateway does not support creating hard or symbolic links on a file share.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/storagegateway-2013-06-30/CreateNFSFileShare>`_

        **Request Syntax**
        ::

          response = client.create_nfs_file_share(
              ClientToken='string',
              NFSFileShareDefaults={
                  'FileMode': 'string',
                  'DirectoryMode': 'string',
                  'GroupId': 123,
                  'OwnerId': 123
              },
              GatewayARN='string',
              KMSEncrypted=True|False,
              KMSKey='string',
              Role='string',
              LocationARN='string',
              DefaultStorageClass='string',
              ObjectACL=
                  'private'|'public-read'|'public-read-write'|'authenticated-read'
                  |'bucket-owner-read'|'bucket-owner-full-control'|'aws-exec-read',
              ClientList=[
                  'string',
              ],
              Squash='string',
              ReadOnly=True|False,
              GuessMIMETypeEnabled=True|False,
              RequesterPays=True|False,
              Tags=[
                  {
                      'Key': 'string',
                      'Value': 'string'
                  },
              ]
          )
        :type ClientToken: string
        :param ClientToken: **[REQUIRED]**

          A unique string value that you supply that is used by file gateway to ensure idempotent
          file share creation.

        :type NFSFileShareDefaults: dict
        :param NFSFileShareDefaults:

          File share default values. Optional.

          - **FileMode** *(string) --*

            The Unix file mode in the form "nnnn". For example, "0666" represents the default file
            mode inside the file share. The default value is 0666.

          - **DirectoryMode** *(string) --*

            The Unix directory mode in the form "nnnn". For example, "0666" represents the default
            access mode for all directories inside the file share. The default value is 0777.

          - **GroupId** *(integer) --*

            The default group ID for the file share (unless the files have another group ID
            specified). The default value is nfsnobody.

          - **OwnerId** *(integer) --*

            The default owner ID for files in the file share (unless the files have another owner ID
            specified). The default value is nfsnobody.

        :type GatewayARN: string
        :param GatewayARN: **[REQUIRED]**

          The Amazon Resource Name (ARN) of the file gateway on which you want to create a file
          share.

        :type KMSEncrypted: boolean
        :param KMSEncrypted:

          True to use Amazon S3 server side encryption with your own AWS KMS key, or false to use a
          key managed by Amazon S3. Optional.

        :type KMSKey: string
        :param KMSKey:

          The Amazon Resource Name (ARN) AWS KMS key used for Amazon S3 server side encryption. This
          value can only be set when KMSEncrypted is true. Optional.

        :type Role: string
        :param Role: **[REQUIRED]**

          The ARN of the AWS Identity and Access Management (IAM) role that a file gateway assumes
          when it accesses the underlying storage.

        :type LocationARN: string
        :param LocationARN: **[REQUIRED]**

          The ARN of the backed storage used for storing file data.

        :type DefaultStorageClass: string
        :param DefaultStorageClass:

          The default storage class for objects put into an Amazon S3 bucket by the file gateway.
          Possible values are ``S3_STANDARD`` , ``S3_STANDARD_IA`` , or ``S3_ONEZONE_IA`` . If this
          field is not populated, the default value ``S3_STANDARD`` is used. Optional.

        :type ObjectACL: string
        :param ObjectACL:

          A value that sets the access control list permission for objects in the S3 bucket that a
          file gateway puts objects into. The default value is "private".

        :type ClientList: list
        :param ClientList:

          The list of clients that are allowed to access the file gateway. The list must contain
          either valid IP addresses or valid CIDR blocks.

          - *(string) --*

        :type Squash: string
        :param Squash:

          A value that maps a user to anonymous user. Valid options are the following:

          * ``RootSquash`` - Only root is mapped to anonymous user.

          * ``NoSquash`` - No one is mapped to anonymous user

          * ``AllSquash`` - Everyone is mapped to anonymous user.

        :type ReadOnly: boolean
        :param ReadOnly:

          A value that sets the write status of a file share. This value is true if the write status
          is read-only, and otherwise false.

        :type GuessMIMETypeEnabled: boolean
        :param GuessMIMETypeEnabled:

          A value that enables guessing of the MIME type for uploaded objects based on file
          extensions. Set this value to true to enable MIME type guessing, and otherwise to false.
          The default value is true.

        :type RequesterPays: boolean
        :param RequesterPays:

          A value that sets who pays the cost of the request and the cost associated with data
          download from the S3 bucket. If this value is set to true, the requester pays the costs.
          Otherwise the S3 bucket owner pays. However, the S3 bucket owner always pays the cost of
          storing data.

          .. note::

             ``RequesterPays`` is a configuration for the S3 bucket that backs the file share, so
             make sure that the configuration on the file share is the same as the S3 bucket
             configuration.

        :type Tags: list
        :param Tags:

          A list of up to 50 tags that can be assigned to the NFS file share. Each tag is a
          key-value pair.

          .. note::

            Valid characters for key and value are letters, spaces, and numbers representable in
            UTF-8 format, and the following special characters: + - =
                 . _ : / @. The maximum length
            of a tag's key is 128 characters, and the maximum length for a tag's value is 256.

          - *(dict) --*

            A key-value pair that helps you manage, filter, and search for your resource. Allowed
            characters: letters, white space, and numbers, representable in UTF-8, and the following
            characters: + - = . _ : /

            - **Key** *(string) --* **[REQUIRED]**

              Tag key (String). The key can't start with aws:.

            - **Value** *(string) --* **[REQUIRED]**

              Value of the tag key.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'FileShareARN': 'string'
            }
          **Response Structure**

          - *(dict) --*

            CreateNFSFileShareOutput

            - **FileShareARN** *(string) --*

              The Amazon Resource Name (ARN) of the newly created file share.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_smb_file_share(
        self,
        ClientToken: str,
        GatewayARN: str,
        Role: str,
        LocationARN: str,
        KMSEncrypted: bool = None,
        KMSKey: str = None,
        DefaultStorageClass: str = None,
        ObjectACL: Literal[
            "private",
            "public-read",
            "public-read-write",
            "authenticated-read",
            "bucket-owner-read",
            "bucket-owner-full-control",
            "aws-exec-read",
        ] = None,
        ReadOnly: bool = None,
        GuessMIMETypeEnabled: bool = None,
        RequesterPays: bool = None,
        SMBACLEnabled: bool = None,
        AdminUserList: List[str] = None,
        ValidUserList: List[str] = None,
        InvalidUserList: List[str] = None,
        Authentication: str = None,
        Tags: List[ClientCreateSmbFileShareTagsTypeDef] = None,
    ) -> ClientCreateSmbFileShareResponseTypeDef:
        """
        Creates a Server Message Block (SMB) file share on an existing file gateway. In Storage
        Gateway, a file share is a file system mount point backed by Amazon S3 cloud storage.
        Storage Gateway expose file shares using a SMB interface. This operation is only supported
        for file gateways.

        .. warning::

          File gateways require AWS Security Token Service (AWS STS) to be activated to enable you
          to create a file share. Make sure that AWS STS is activated in the AWS Region you are
          creating your file gateway in. If AWS STS is not activated in this AWS Region, activate
          it. For information about how to activate AWS STS, see `Activating and Deactivating AWS
          STS in an AWS Region
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_enable-regions.html>`__
          in the *AWS Identity and Access Management User Guide.*

          File gateways don't support creating hard or symbolic links on a file share.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/storagegateway-2013-06-30/CreateSMBFileShare>`_

        **Request Syntax**
        ::

          response = client.create_smb_file_share(
              ClientToken='string',
              GatewayARN='string',
              KMSEncrypted=True|False,
              KMSKey='string',
              Role='string',
              LocationARN='string',
              DefaultStorageClass='string',
              ObjectACL=
                  'private'|'public-read'|'public-read-write'|'authenticated-read'
                  |'bucket-owner-read'|'bucket-owner-full-control'|'aws-exec-read',
              ReadOnly=True|False,
              GuessMIMETypeEnabled=True|False,
              RequesterPays=True|False,
              SMBACLEnabled=True|False,
              AdminUserList=[
                  'string',
              ],
              ValidUserList=[
                  'string',
              ],
              InvalidUserList=[
                  'string',
              ],
              Authentication='string',
              Tags=[
                  {
                      'Key': 'string',
                      'Value': 'string'
                  },
              ]
          )
        :type ClientToken: string
        :param ClientToken: **[REQUIRED]**

          A unique string value that you supply that is used by file gateway to ensure idempotent
          file share creation.

        :type GatewayARN: string
        :param GatewayARN: **[REQUIRED]**

          The Amazon Resource Name (ARN) of the file gateway on which you want to create a file
          share.

        :type KMSEncrypted: boolean
        :param KMSEncrypted:

          True to use Amazon S3 server side encryption with your own AWS KMS key, or false to use a
          key managed by Amazon S3. Optional.

        :type KMSKey: string
        :param KMSKey:

          The Amazon Resource Name (ARN) of the AWS KMS key used for Amazon S3 server side
          encryption. This value can only be set when KMSEncrypted is true. Optional.

        :type Role: string
        :param Role: **[REQUIRED]**

          The ARN of the AWS Identity and Access Management (IAM) role that a file gateway assumes
          when it accesses the underlying storage.

        :type LocationARN: string
        :param LocationARN: **[REQUIRED]**

          The ARN of the backed storage used for storing file data.

        :type DefaultStorageClass: string
        :param DefaultStorageClass:

          The default storage class for objects put into an Amazon S3 bucket by the file gateway.
          Possible values are ``S3_STANDARD`` , ``S3_STANDARD_IA`` , or ``S3_ONEZONE_IA`` . If this
          field is not populated, the default value ``S3_STANDARD`` is used. Optional.

        :type ObjectACL: string
        :param ObjectACL:

          A value that sets the access control list permission for objects in the S3 bucket that a
          file gateway puts objects into. The default value is "private".

        :type ReadOnly: boolean
        :param ReadOnly:

          A value that sets the write status of a file share. This value is true if the write status
          is read-only, and otherwise false.

        :type GuessMIMETypeEnabled: boolean
        :param GuessMIMETypeEnabled:

          A value that enables guessing of the MIME type for uploaded objects based on file
          extensions. Set this value to true to enable MIME type guessing, and otherwise to false.
          The default value is true.

        :type RequesterPays: boolean
        :param RequesterPays:

          A value that sets who pays the cost of the request and the cost associated with data
          download from the S3 bucket. If this value is set to true, the requester pays the costs.
          Otherwise the S3 bucket owner pays. However, the S3 bucket owner always pays the cost of
          storing data.

          .. note::

             ``RequesterPays`` is a configuration for the S3 bucket that backs the file share, so
             make sure that the configuration on the file share is the same as the S3 bucket
             configuration.

        :type SMBACLEnabled: boolean
        :param SMBACLEnabled:

          Set this value to "true to enable ACL (access control list) on the SMB file share. Set it
          to "false" to map file and directory permissions to the POSIX permissions.

          For more information, see
          https://docs.aws.amazon.com/storagegateway/latest/userguide/smb-acl.html in the Storage
          Gateway User Guide.

        :type AdminUserList: list
        :param AdminUserList:

          A list of users in the Active Directory that will be granted administrator privileges on
          the file share. These users can do all file operations as the super-user.

          .. warning::

            Use this option very carefully, because any user in this list can do anything they like
            on the file share, regardless of file permissions.

          - *(string) --*

        :type ValidUserList: list
        :param ValidUserList:

          A list of users or groups in the Active Directory that are allowed to access the file
          share. A group must be prefixed with the @ character. For example ``@group1`` . Can only
          be set if Authentication is set to ``ActiveDirectory`` .

          - *(string) --*

        :type InvalidUserList: list
        :param InvalidUserList:

          A list of users or groups in the Active Directory that are not allowed to access the file
          share. A group must be prefixed with the @ character. For example ``@group1`` . Can only
          be set if Authentication is set to ``ActiveDirectory`` .

          - *(string) --*

        :type Authentication: string
        :param Authentication:

          The authentication method that users use to access the file share.

          Valid values are ``ActiveDirectory`` or ``GuestAccess`` . The default is
          ``ActiveDirectory`` .

        :type Tags: list
        :param Tags:

          A list of up to 50 tags that can be assigned to the NFS file share. Each tag is a
          key-value pair.

          .. note::

            Valid characters for key and value are letters, spaces, and numbers representable in
            UTF-8 format, and the following special characters: + - =
                 . _ : / @. The maximum length
            of a tag's key is 128 characters, and the maximum length for a tag's value is 256.

          - *(dict) --*

            A key-value pair that helps you manage, filter, and search for your resource. Allowed
            characters: letters, white space, and numbers, representable in UTF-8, and the following
            characters: + - = . _ : /

            - **Key** *(string) --* **[REQUIRED]**

              Tag key (String). The key can't start with aws:.

            - **Value** *(string) --* **[REQUIRED]**

              Value of the tag key.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'FileShareARN': 'string'
            }
          **Response Structure**

          - *(dict) --*

            CreateSMBFileShareOutput

            - **FileShareARN** *(string) --*

              The Amazon Resource Name (ARN) of the newly created file share.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_snapshot(
        self,
        VolumeARN: str,
        SnapshotDescription: str,
        Tags: List[ClientCreateSnapshotTagsTypeDef] = None,
    ) -> ClientCreateSnapshotResponseTypeDef:
        """
        Initiates a snapshot of a volume.

        AWS Storage Gateway provides the ability to back up point-in-time snapshots of your data to
        Amazon Simple Storage (S3) for durable off-site recovery, as well as import the data to an
        Amazon Elastic Block Store (EBS) volume in Amazon Elastic Compute Cloud (EC2). You can take
        snapshots of your gateway volume on a scheduled or ad hoc basis. This API enables you to
        take ad-hoc snapshot. For more information, see `Editing a Snapshot Schedule
        <https://docs.aws.amazon.com/storagegateway/latest/userguide/managing-volumes.html#SchedulingSnapshot>`__
        .

        In the CreateSnapshot request you identify the volume by providing its Amazon Resource Name
        (ARN). You must also provide description for the snapshot. When AWS Storage Gateway takes
        the snapshot of specified volume, the snapshot and description appears in the AWS Storage
        Gateway Console. In response, AWS Storage Gateway returns you a snapshot ID. You can use
        this snapshot ID to check the snapshot progress or later use it when you want to create a
        volume from a snapshot. This operation is only supported in stored and cached volume gateway
        type.

        .. note::

          To list or delete a snapshot, you must use the Amazon EC2 API. For more information, see
          DescribeSnapshots or DeleteSnapshot in the `EC2 API reference
          <https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_Operations.html>`__ .

        .. warning::

          Volume and snapshot IDs are changing to a longer length ID format. For more information,
          see the important note on the `Welcome
          <https://docs.aws.amazon.com/storagegateway/latest/APIReference/Welcome.html>`__ page.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/storagegateway-2013-06-30/CreateSnapshot>`_

        **Request Syntax**
        ::

          response = client.create_snapshot(
              VolumeARN='string',
              SnapshotDescription='string',
              Tags=[
                  {
                      'Key': 'string',
                      'Value': 'string'
                  },
              ]
          )
        :type VolumeARN: string
        :param VolumeARN: **[REQUIRED]**

          The Amazon Resource Name (ARN) of the volume. Use the  ListVolumes operation to return a
          list of gateway volumes.

        :type SnapshotDescription: string
        :param SnapshotDescription: **[REQUIRED]**

          Textual description of the snapshot that appears in the Amazon EC2 console, Elastic Block
          Store snapshots panel in the **Description** field, and in the AWS Storage Gateway
          snapshot **Details** pane, **Description** field

        :type Tags: list
        :param Tags:

          A list of up to 50 tags that can be assigned to a snapshot. Each tag is a key-value pair.

          .. note::

            Valid characters for key and value are letters, spaces, and numbers representable in
            UTF-8 format, and the following special characters: + - =
                 . _ : / @. The maximum length
            of a tag's key is 128 characters, and the maximum length for a tag's value is 256.

          - *(dict) --*

            A key-value pair that helps you manage, filter, and search for your resource. Allowed
            characters: letters, white space, and numbers, representable in UTF-8, and the following
            characters: + - = . _ : /

            - **Key** *(string) --* **[REQUIRED]**

              Tag key (String). The key can't start with aws:.

            - **Value** *(string) --* **[REQUIRED]**

              Value of the tag key.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'VolumeARN': 'string',
                'SnapshotId': 'string'
            }
          **Response Structure**

          - *(dict) --*

            A JSON object containing the following fields:

            - **VolumeARN** *(string) --*

              The Amazon Resource Name (ARN) of the volume of which the snapshot was taken.

            - **SnapshotId** *(string) --*

              The snapshot ID that is used to refer to the snapshot in future operations such as
              describing snapshots (Amazon Elastic Compute Cloud API ``DescribeSnapshots`` ) or
              creating a volume from a snapshot ( CreateStorediSCSIVolume ).
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_snapshot_from_volume_recovery_point(
        self,
        VolumeARN: str,
        SnapshotDescription: str,
        Tags: List[ClientCreateSnapshotFromVolumeRecoveryPointTagsTypeDef] = None,
    ) -> ClientCreateSnapshotFromVolumeRecoveryPointResponseTypeDef:
        """
        Initiates a snapshot of a gateway from a volume recovery point. This operation is only
        supported in the cached volume gateway type.

        A volume recovery point is a point in time at which all data of the volume is consistent and
        from which you can create a snapshot. To get a list of volume recovery point for cached
        volume gateway, use  ListVolumeRecoveryPoints .

        In the ``CreateSnapshotFromVolumeRecoveryPoint`` request, you identify the volume by
        providing its Amazon Resource Name (ARN). You must also provide a description for the
        snapshot. When the gateway takes a snapshot of the specified volume, the snapshot and its
        description appear in the AWS Storage Gateway console. In response, the gateway returns you
        a snapshot ID. You can use this snapshot ID to check the snapshot progress or later use it
        when you want to create a volume from a snapshot.

        .. note::

          To list or delete a snapshot, you must use the Amazon EC2 API. For more information, in
          *Amazon Elastic Compute Cloud API Reference* .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/storagegateway-2013-06-30/CreateSnapshotFromVolumeRecoveryPoint>`_

        **Request Syntax**
        ::

          response = client.create_snapshot_from_volume_recovery_point(
              VolumeARN='string',
              SnapshotDescription='string',
              Tags=[
                  {
                      'Key': 'string',
                      'Value': 'string'
                  },
              ]
          )
        :type VolumeARN: string
        :param VolumeARN: **[REQUIRED]**

          The Amazon Resource Name (ARN) of the iSCSI volume target. Use the
          DescribeStorediSCSIVolumes operation to return to retrieve the TargetARN for specified
          VolumeARN.

        :type SnapshotDescription: string
        :param SnapshotDescription: **[REQUIRED]**

          Textual description of the snapshot that appears in the Amazon EC2 console, Elastic Block
          Store snapshots panel in the **Description** field, and in the AWS Storage Gateway
          snapshot **Details** pane, **Description** field

        :type Tags: list
        :param Tags:

          A list of up to 50 tags that can be assigned to a snapshot. Each tag is a key-value pair.

          .. note::

            Valid characters for key and value are letters, spaces, and numbers representable in
            UTF-8 format, and the following special characters: + - =
                 . _ : / @. The maximum length
            of a tag's key is 128 characters, and the maximum length for a tag's value is 256.

          - *(dict) --*

            A key-value pair that helps you manage, filter, and search for your resource. Allowed
            characters: letters, white space, and numbers, representable in UTF-8, and the following
            characters: + - = . _ : /

            - **Key** *(string) --* **[REQUIRED]**

              Tag key (String). The key can't start with aws:.

            - **Value** *(string) --* **[REQUIRED]**

              Value of the tag key.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'SnapshotId': 'string',
                'VolumeARN': 'string',
                'VolumeRecoveryPointTime': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **SnapshotId** *(string) --*

              The ID of the snapshot.

            - **VolumeARN** *(string) --*

              The Amazon Resource Name (ARN) of the iSCSI volume target. Use the
              DescribeStorediSCSIVolumes operation to return to retrieve the TargetARN for specified
              VolumeARN.

            - **VolumeRecoveryPointTime** *(string) --*

              The time the volume was created from the recovery point.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_stored_iscsi_volume(
        self,
        GatewayARN: str,
        DiskId: str,
        PreserveExistingData: bool,
        TargetName: str,
        NetworkInterfaceId: str,
        SnapshotId: str = None,
        KMSEncrypted: bool = None,
        KMSKey: str = None,
        Tags: List[ClientCreateStoredIscsiVolumeTagsTypeDef] = None,
    ) -> ClientCreateStoredIscsiVolumeResponseTypeDef:
        """
        Creates a volume on a specified gateway. This operation is only supported in the stored
        volume gateway type.

        The size of the volume to create is inferred from the disk size. You can choose to preserve
        existing data on the disk, create volume from an existing snapshot, or create an empty
        volume. If you choose to create an empty gateway volume, then any existing data on the disk
        is erased.

        In the request you must specify the gateway and the disk information on which you are
        creating the volume. In response, the gateway creates the volume and returns volume
        information such as the volume Amazon Resource Name (ARN), its size, and the iSCSI target
        ARN that initiators can use to connect to the volume target.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/storagegateway-2013-06-30/CreateStorediSCSIVolume>`_

        **Request Syntax**
        ::

          response = client.create_stored_iscsi_volume(
              GatewayARN='string',
              DiskId='string',
              SnapshotId='string',
              PreserveExistingData=True|False,
              TargetName='string',
              NetworkInterfaceId='string',
              KMSEncrypted=True|False,
              KMSKey='string',
              Tags=[
                  {
                      'Key': 'string',
                      'Value': 'string'
                  },
              ]
          )
        :type GatewayARN: string
        :param GatewayARN: **[REQUIRED]**

          The Amazon Resource Name (ARN) of the gateway. Use the  ListGateways operation to return a
          list of gateways for your account and AWS Region.

        :type DiskId: string
        :param DiskId: **[REQUIRED]**

          The unique identifier for the gateway local disk that is configured as a stored volume.
          Use `ListLocalDisks
          <https://docs.aws.amazon.com/storagegateway/latest/userguide/API_ListLocalDisks.html>`__
          to list disk IDs for a gateway.

        :type SnapshotId: string
        :param SnapshotId:

          The snapshot ID (e.g. "snap-1122aabb") of the snapshot to restore as the new stored
          volume. Specify this field if you want to create the iSCSI storage volume from a snapshot
          otherwise do not include this field. To list snapshots for your account use
          `DescribeSnapshots
          <https://docs.aws.amazon.com/AWSEC2/latest/APIReference/ApiReference-query-DescribeSnapshots.html>`__
          in the *Amazon Elastic Compute Cloud API Reference* .

        :type PreserveExistingData: boolean
        :param PreserveExistingData: **[REQUIRED]**

          Specify this field as true if you want to preserve the data on the local disk. Otherwise,
          specifying this field as false creates an empty volume.

          Valid Values: true, false

        :type TargetName: string
        :param TargetName: **[REQUIRED]**

          The name of the iSCSI target used by an initiator to connect to a volume and used as a
          suffix for the target ARN. For example, specifying ``TargetName`` as *myvolume* results in
          the target ARN of
          ``arn:aws:storagegateway:us-east-2:111122223333:gateway/sgw-12A3456B/target/iqn.1997-05.com.amazon:myvolume``
          . The target name must be unique across all volumes on a gateway.

          If you don't specify a value, Storage Gateway uses the value that was previously used for
          this volume as the new target name.

        :type NetworkInterfaceId: string
        :param NetworkInterfaceId: **[REQUIRED]**

          The network interface of the gateway on which to expose the iSCSI target. Only IPv4
          addresses are accepted. Use  DescribeGatewayInformation to get a list of the network
          interfaces available on a gateway.

          Valid Values: A valid IP address.

        :type KMSEncrypted: boolean
        :param KMSEncrypted:

          True to use Amazon S3 server side encryption with your own AWS KMS key, or false to use a
          key managed by Amazon S3. Optional.

        :type KMSKey: string
        :param KMSKey:

          The Amazon Resource Name (ARN) of the KMS key used for Amazon S3 server side encryption.
          This value can only be set when KMSEncrypted is true. Optional.

        :type Tags: list
        :param Tags:

          A list of up to 50 tags that can be assigned to a stored volume. Each tag is a key-value
          pair.

          .. note::

            Valid characters for key and value are letters, spaces, and numbers representable in
            UTF-8 format, and the following special characters: + - =
                 . _ : / @. The maximum length
            of a tag's key is 128 characters, and the maximum length for a tag's value is 256.

          - *(dict) --*

            A key-value pair that helps you manage, filter, and search for your resource. Allowed
            characters: letters, white space, and numbers, representable in UTF-8, and the following
            characters: + - = . _ : /

            - **Key** *(string) --* **[REQUIRED]**

              Tag key (String). The key can't start with aws:.

            - **Value** *(string) --* **[REQUIRED]**

              Value of the tag key.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'VolumeARN': 'string',
                'VolumeSizeInBytes': 123,
                'TargetARN': 'string'
            }
          **Response Structure**

          - *(dict) --*

            A JSON object containing the following fields:

            - **VolumeARN** *(string) --*

              The Amazon Resource Name (ARN) of the configured volume.

            - **VolumeSizeInBytes** *(integer) --*

              The size of the volume in bytes.

            - **TargetARN** *(string) --*

              The Amazon Resource Name (ARN) of the volume target, which includes the iSCSI name
              that initiators can use to connect to the target.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_tape_with_barcode(
        self,
        GatewayARN: str,
        TapeSizeInBytes: int,
        TapeBarcode: str,
        KMSEncrypted: bool = None,
        KMSKey: str = None,
        PoolId: str = None,
        Tags: List[ClientCreateTapeWithBarcodeTagsTypeDef] = None,
    ) -> ClientCreateTapeWithBarcodeResponseTypeDef:
        """
        Creates a virtual tape by using your own barcode. You write data to the virtual tape and
        then archive the tape. A barcode is unique and can not be reused if it has already been used
        on a tape . This applies to barcodes used on deleted tapes. This operation is only supported
        in the tape gateway type.

        .. note::

          Cache storage must be allocated to the gateway before you can create a virtual tape. Use
          the  AddCache operation to add cache storage to a gateway.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/storagegateway-2013-06-30/CreateTapeWithBarcode>`_

        **Request Syntax**
        ::

          response = client.create_tape_with_barcode(
              GatewayARN='string',
              TapeSizeInBytes=123,
              TapeBarcode='string',
              KMSEncrypted=True|False,
              KMSKey='string',
              PoolId='string',
              Tags=[
                  {
                      'Key': 'string',
                      'Value': 'string'
                  },
              ]
          )
        :type GatewayARN: string
        :param GatewayARN: **[REQUIRED]**

          The unique Amazon Resource Name (ARN) that represents the gateway to associate the virtual
          tape with. Use the  ListGateways operation to return a list of gateways for your account
          and AWS Region.

        :type TapeSizeInBytes: integer
        :param TapeSizeInBytes: **[REQUIRED]**

          The size, in bytes, of the virtual tape that you want to create.

          .. note::

            The size must be aligned by gigabyte (1024*1024*1024 byte).

        :type TapeBarcode: string
        :param TapeBarcode: **[REQUIRED]**

          The barcode that you want to assign to the tape.

          .. note::

            Barcodes cannot be reused. This includes barcodes used for tapes that have been deleted.

        :type KMSEncrypted: boolean
        :param KMSEncrypted:

          True to use Amazon S3 server side encryption with your own AWS KMS key, or false to use a
          key managed by Amazon S3. Optional.

        :type KMSKey: string
        :param KMSKey:

          The Amazon Resource Name (ARN) of the AWS KMS Key used for Amazon S3 server side
          encryption. This value can only be set when KMSEncrypted is true. Optional.

        :type PoolId: string
        :param PoolId:

          The ID of the pool that you want to add your tape to for archiving. The tape in this pool
          is archived in the S3 storage class that is associated with the pool. When you use your
          backup application to eject the tape, the tape is archived directly into the storage class
          (Glacier or Deep Archive) that corresponds to the pool.

          Valid values: "GLACIER", "DEEP_ARCHIVE"

        :type Tags: list
        :param Tags:

          A list of up to 50 tags that can be assigned to a virtual tape that has a barcode. Each
          tag is a key-value pair.

          .. note::

            Valid characters for key and value are letters, spaces, and numbers representable in
            UTF-8 format, and the following special characters: + - =
                 . _ : / @. The maximum length
            of a tag's key is 128 characters, and the maximum length for a tag's value is 256.

          - *(dict) --*

            A key-value pair that helps you manage, filter, and search for your resource. Allowed
            characters: letters, white space, and numbers, representable in UTF-8, and the following
            characters: + - = . _ : /

            - **Key** *(string) --* **[REQUIRED]**

              Tag key (String). The key can't start with aws:.

            - **Value** *(string) --* **[REQUIRED]**

              Value of the tag key.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'TapeARN': 'string'
            }
          **Response Structure**

          - *(dict) --*

            CreateTapeOutput

            - **TapeARN** *(string) --*

              A unique Amazon Resource Name (ARN) that represents the virtual tape that was created.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_tapes(
        self,
        GatewayARN: str,
        TapeSizeInBytes: int,
        ClientToken: str,
        NumTapesToCreate: int,
        TapeBarcodePrefix: str,
        KMSEncrypted: bool = None,
        KMSKey: str = None,
        PoolId: str = None,
        Tags: List[ClientCreateTapesTagsTypeDef] = None,
    ) -> ClientCreateTapesResponseTypeDef:
        """
        Creates one or more virtual tapes. You write data to the virtual tapes and then archive the
        tapes. This operation is only supported in the tape gateway type.

        .. note::

          Cache storage must be allocated to the gateway before you can create virtual tapes. Use
          the  AddCache operation to add cache storage to a gateway.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/storagegateway-2013-06-30/CreateTapes>`_

        **Request Syntax**
        ::

          response = client.create_tapes(
              GatewayARN='string',
              TapeSizeInBytes=123,
              ClientToken='string',
              NumTapesToCreate=123,
              TapeBarcodePrefix='string',
              KMSEncrypted=True|False,
              KMSKey='string',
              PoolId='string',
              Tags=[
                  {
                      'Key': 'string',
                      'Value': 'string'
                  },
              ]
          )
        :type GatewayARN: string
        :param GatewayARN: **[REQUIRED]**

          The unique Amazon Resource Name (ARN) that represents the gateway to associate the virtual
          tapes with. Use the  ListGateways operation to return a list of gateways for your account
          and AWS Region.

        :type TapeSizeInBytes: integer
        :param TapeSizeInBytes: **[REQUIRED]**

          The size, in bytes, of the virtual tapes that you want to create.

          .. note::

            The size must be aligned by gigabyte (1024*1024*1024 byte).

        :type ClientToken: string
        :param ClientToken: **[REQUIRED]**

          A unique identifier that you use to retry a request. If you retry a request, use the same
          ``ClientToken`` you specified in the initial request.

          .. note::

            Using the same ``ClientToken`` prevents creating the tape multiple times.

        :type NumTapesToCreate: integer
        :param NumTapesToCreate: **[REQUIRED]**

          The number of virtual tapes that you want to create.

        :type TapeBarcodePrefix: string
        :param TapeBarcodePrefix: **[REQUIRED]**

          A prefix that you append to the barcode of the virtual tape you are creating. This prefix
          makes the barcode unique.

          .. note::

            The prefix must be 1 to 4 characters in length and must be one of the uppercase letters
            from A to Z.

        :type KMSEncrypted: boolean
        :param KMSEncrypted:

          True to use Amazon S3 server side encryption with your own AWS KMS key, or false to use a
          key managed by Amazon S3. Optional.

        :type KMSKey: string
        :param KMSKey:

          The Amazon Resource Name (ARN) of the AWS KMS key used for Amazon S3 server side
          encryption. This value can only be set when KMSEncrypted is true. Optional.

        :type PoolId: string
        :param PoolId:

          The ID of the pool that you want to add your tape to for archiving. The tape in this pool
          is archived in the S3 storage class that is associated with the pool. When you use your
          backup application to eject the tape, the tape is archived directly into the storage class
          (Glacier or Deep Archive) that corresponds to the pool.

          Valid values: "GLACIER", "DEEP_ARCHIVE"

        :type Tags: list
        :param Tags:

          A list of up to 50 tags that can be assigned to a virtual tape. Each tag is a key-value
          pair.

          .. note::

            Valid characters for key and value are letters, spaces, and numbers representable in
            UTF-8 format, and the following special characters: + - =
                 . _ : / @. The maximum length
            of a tag's key is 128 characters, and the maximum length for a tag's value is 256.

          - *(dict) --*

            A key-value pair that helps you manage, filter, and search for your resource. Allowed
            characters: letters, white space, and numbers, representable in UTF-8, and the following
            characters: + - = . _ : /

            - **Key** *(string) --* **[REQUIRED]**

              Tag key (String). The key can't start with aws:.

            - **Value** *(string) --* **[REQUIRED]**

              Value of the tag key.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'TapeARNs': [
                    'string',
                ]
            }
          **Response Structure**

          - *(dict) --*

            CreateTapeOutput

            - **TapeARNs** *(list) --*

              A list of unique Amazon Resource Names (ARNs) that represents the virtual tapes that
              were created.

              - *(string) --*
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_bandwidth_rate_limit(
        self, GatewayARN: str, BandwidthType: str
    ) -> ClientDeleteBandwidthRateLimitResponseTypeDef:
        """
        Deletes the bandwidth rate limits of a gateway. You can delete either the upload and
        download bandwidth rate limit, or you can delete both. If you delete only one of the limits,
        the other limit remains unchanged. To specify which gateway to work with, use the Amazon
        Resource Name (ARN) of the gateway in your request. This operation is supported for the
        stored volume, cached volume and tape gateway types.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/storagegateway-2013-06-30/DeleteBandwidthRateLimit>`_

        **Request Syntax**
        ::

          response = client.delete_bandwidth_rate_limit(
              GatewayARN='string',
              BandwidthType='string'
          )
        :type GatewayARN: string
        :param GatewayARN: **[REQUIRED]**

          The Amazon Resource Name (ARN) of the gateway. Use the  ListGateways operation to return a
          list of gateways for your account and AWS Region.

        :type BandwidthType: string
        :param BandwidthType: **[REQUIRED]**

          One of the BandwidthType values that indicates the gateway bandwidth rate limit to delete.

          Valid Values: ``Upload`` , ``Download`` , ``All`` .

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'GatewayARN': 'string'
            }
          **Response Structure**

          - *(dict) --*

            A JSON object containing the of the gateway whose bandwidth rate information was
            deleted.

            - **GatewayARN** *(string) --*

              The Amazon Resource Name (ARN) of the gateway. Use the  ListGateways operation to
              return a list of gateways for your account and AWS Region.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_chap_credentials(
        self, TargetARN: str, InitiatorName: str
    ) -> ClientDeleteChapCredentialsResponseTypeDef:
        """
        Deletes Challenge-Handshake Authentication Protocol (CHAP) credentials for a specified iSCSI
        target and initiator pair. This operation is supported in volume and tape gateway types.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/storagegateway-2013-06-30/DeleteChapCredentials>`_

        **Request Syntax**
        ::

          response = client.delete_chap_credentials(
              TargetARN='string',
              InitiatorName='string'
          )
        :type TargetARN: string
        :param TargetARN: **[REQUIRED]**

          The Amazon Resource Name (ARN) of the iSCSI volume target. Use the
          DescribeStorediSCSIVolumes operation to return to retrieve the TargetARN for specified
          VolumeARN.

        :type InitiatorName: string
        :param InitiatorName: **[REQUIRED]**

          The iSCSI initiator that connects to the target.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'TargetARN': 'string',
                'InitiatorName': 'string'
            }
          **Response Structure**

          - *(dict) --*

            A JSON object containing the following fields:

            - **TargetARN** *(string) --*

              The Amazon Resource Name (ARN) of the target.

            - **InitiatorName** *(string) --*

              The iSCSI initiator that connects to the target.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_file_share(
        self, FileShareARN: str, ForceDelete: bool = None
    ) -> ClientDeleteFileShareResponseTypeDef:
        """
        Deletes a file share from a file gateway. This operation is only supported for file
        gateways.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/storagegateway-2013-06-30/DeleteFileShare>`_

        **Request Syntax**
        ::

          response = client.delete_file_share(
              FileShareARN='string',
              ForceDelete=True|False
          )
        :type FileShareARN: string
        :param FileShareARN: **[REQUIRED]**

          The Amazon Resource Name (ARN) of the file share to be deleted.

        :type ForceDelete: boolean
        :param ForceDelete:

          If this value is set to true, the operation deletes a file share immediately and aborts
          all data uploads to AWS. Otherwise, the file share is not deleted until all data is
          uploaded to AWS. This process aborts the data upload process, and the file share enters
          the FORCE_DELETING status.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'FileShareARN': 'string'
            }
          **Response Structure**

          - *(dict) --*

            DeleteFileShareOutput

            - **FileShareARN** *(string) --*

              The Amazon Resource Name (ARN) of the deleted file share.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_gateway(self, GatewayARN: str) -> ClientDeleteGatewayResponseTypeDef:
        """
        Deletes a gateway. To specify which gateway to delete, use the Amazon Resource Name (ARN) of
        the gateway in your request. The operation deletes the gateway; however, it does not delete
        the gateway virtual machine (VM) from your host computer.

        After you delete a gateway, you cannot reactivate it. Completed snapshots of the gateway
        volumes are not deleted upon deleting the gateway, however, pending snapshots will not
        complete. After you delete a gateway, your next step is to remove it from your environment.

        .. warning::

          You no longer pay software charges after the gateway is deleted; however, your existing
          Amazon EBS snapshots persist and you will continue to be billed for these snapshots. You
          can choose to remove all remaining Amazon EBS snapshots by canceling your Amazon EC2
          subscription. If you prefer not to cancel your Amazon EC2 subscription, you can delete
          your snapshots using the Amazon EC2 console. For more information, see the `AWS Storage
          Gateway Detail Page <http://aws.amazon.com/storagegateway>`__ .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/storagegateway-2013-06-30/DeleteGateway>`_

        **Request Syntax**
        ::

          response = client.delete_gateway(
              GatewayARN='string'
          )
        :type GatewayARN: string
        :param GatewayARN: **[REQUIRED]**

          The Amazon Resource Name (ARN) of the gateway. Use the  ListGateways operation to return a
          list of gateways for your account and AWS Region.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'GatewayARN': 'string'
            }
          **Response Structure**

          - *(dict) --*

            A JSON object containing the ID of the deleted gateway.

            - **GatewayARN** *(string) --*

              The Amazon Resource Name (ARN) of the gateway. Use the  ListGateways operation to
              return a list of gateways for your account and AWS Region.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_snapshot_schedule(
        self, VolumeARN: str
    ) -> ClientDeleteSnapshotScheduleResponseTypeDef:
        """
        Deletes a snapshot of a volume.

        You can take snapshots of your gateway volumes on a scheduled or ad hoc basis. This API
        action enables you to delete a snapshot schedule for a volume. For more information, see
        `Working with Snapshots
        <https://docs.aws.amazon.com/storagegateway/latest/userguide/WorkingWithSnapshots.html>`__ .
        In the ``DeleteSnapshotSchedule`` request, you identify the volume by providing its Amazon
        Resource Name (ARN). This operation is only supported in stored and cached volume gateway
        types.

        .. note::

          To list or delete a snapshot, you must use the Amazon EC2 API. in *Amazon Elastic Compute
          Cloud API Reference* .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/storagegateway-2013-06-30/DeleteSnapshotSchedule>`_

        **Request Syntax**
        ::

          response = client.delete_snapshot_schedule(
              VolumeARN='string'
          )
        :type VolumeARN: string
        :param VolumeARN: **[REQUIRED]**

          The volume which snapshot schedule to delete.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'VolumeARN': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **VolumeARN** *(string) --*

              The volume which snapshot schedule was deleted.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_tape(self, GatewayARN: str, TapeARN: str) -> ClientDeleteTapeResponseTypeDef:
        """
        Deletes the specified virtual tape. This operation is only supported in the tape gateway
        type.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/storagegateway-2013-06-30/DeleteTape>`_

        **Request Syntax**
        ::

          response = client.delete_tape(
              GatewayARN='string',
              TapeARN='string'
          )
        :type GatewayARN: string
        :param GatewayARN: **[REQUIRED]**

          The unique Amazon Resource Name (ARN) of the gateway that the virtual tape to delete is
          associated with. Use the  ListGateways operation to return a list of gateways for your
          account and AWS Region.

        :type TapeARN: string
        :param TapeARN: **[REQUIRED]**

          The Amazon Resource Name (ARN) of the virtual tape to delete.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'TapeARN': 'string'
            }
          **Response Structure**

          - *(dict) --*

            DeleteTapeOutput

            - **TapeARN** *(string) --*

              The Amazon Resource Name (ARN) of the deleted virtual tape.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_tape_archive(self, TapeARN: str) -> ClientDeleteTapeArchiveResponseTypeDef:
        """
        Deletes the specified virtual tape from the virtual tape shelf (VTS). This operation is only
        supported in the tape gateway type.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/storagegateway-2013-06-30/DeleteTapeArchive>`_

        **Request Syntax**
        ::

          response = client.delete_tape_archive(
              TapeARN='string'
          )
        :type TapeARN: string
        :param TapeARN: **[REQUIRED]**

          The Amazon Resource Name (ARN) of the virtual tape to delete from the virtual tape shelf
          (VTS).

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'TapeARN': 'string'
            }
          **Response Structure**

          - *(dict) --*

            DeleteTapeArchiveOutput

            - **TapeARN** *(string) --*

              The Amazon Resource Name (ARN) of the virtual tape that was deleted from the virtual
              tape shelf (VTS).
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_volume(self, VolumeARN: str) -> ClientDeleteVolumeResponseTypeDef:
        """
        Deletes the specified storage volume that you previously created using the
        CreateCachediSCSIVolume or  CreateStorediSCSIVolume API. This operation is only supported in
        the cached volume and stored volume types. For stored volume gateways, the local disk that
        was configured as the storage volume is not deleted. You can reuse the local disk to create
        another storage volume.

        Before you delete a volume, make sure there are no iSCSI connections to the volume you are
        deleting. You should also make sure there is no snapshot in progress. You can use the Amazon
        Elastic Compute Cloud (Amazon EC2) API to query snapshots on the volume you are deleting and
        check the snapshot status. For more information, go to `DescribeSnapshots
        <https://docs.aws.amazon.com/AWSEC2/latest/APIReference/ApiReference-query-DescribeSnapshots.html>`__
        in the *Amazon Elastic Compute Cloud API Reference* .

        In the request, you must provide the Amazon Resource Name (ARN) of the storage volume you
        want to delete.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/storagegateway-2013-06-30/DeleteVolume>`_

        **Request Syntax**
        ::

          response = client.delete_volume(
              VolumeARN='string'
          )
        :type VolumeARN: string
        :param VolumeARN: **[REQUIRED]**

          The Amazon Resource Name (ARN) of the volume. Use the  ListVolumes operation to return a
          list of gateway volumes.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'VolumeARN': 'string'
            }
          **Response Structure**

          - *(dict) --*

            A JSON object containing the of the storage volume that was deleted

            - **VolumeARN** *(string) --*

              The Amazon Resource Name (ARN) of the storage volume that was deleted. It is the same
              ARN you provided in the request.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_availability_monitor_test(
        self, GatewayARN: str
    ) -> ClientDescribeAvailabilityMonitorTestResponseTypeDef:
        """
        Returns information about the most recent High Availability monitoring test that was
        performed on the host in a cluster. If a test isn't performed, the status and start time in
        the response would be null.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/storagegateway-2013-06-30/DescribeAvailabilityMonitorTest>`_

        **Request Syntax**
        ::

          response = client.describe_availability_monitor_test(
              GatewayARN='string'
          )
        :type GatewayARN: string
        :param GatewayARN: **[REQUIRED]**

          The Amazon Resource Name (ARN) of the gateway. Use the  ListGateways operation to return a
          list of gateways for your account and AWS Region.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'GatewayARN': 'string',
                'Status': 'COMPLETE'|'FAILED'|'PENDING',
                'StartTime': datetime(2015, 1, 1)
            }
          **Response Structure**

          - *(dict) --*

            - **GatewayARN** *(string) --*

              The Amazon Resource Name (ARN) of the gateway. Use the  ListGateways operation to
              return a list of gateways for your account and AWS Region.

            - **Status** *(string) --*

              The status of the High Availability monitoring test. If a test hasn't been performed,
              the value of this field is null.

            - **StartTime** *(datetime) --*

              The time the High Availability monitoring test was started. If a test hasn't been
              performed, the value of this field is null.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_bandwidth_rate_limit(
        self, GatewayARN: str
    ) -> ClientDescribeBandwidthRateLimitResponseTypeDef:
        """
        Returns the bandwidth rate limits of a gateway. By default, these limits are not set, which
        means no bandwidth rate limiting is in effect. This operation is supported for the stored
        volume, cached volume and tape gateway types.'

        This operation only returns a value for a bandwidth rate limit only if the limit is set. If
        no limits are set for the gateway, then this operation returns only the gateway ARN in the
        response body. To specify which gateway to describe, use the Amazon Resource Name (ARN) of
        the gateway in your request.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/storagegateway-2013-06-30/DescribeBandwidthRateLimit>`_

        **Request Syntax**
        ::

          response = client.describe_bandwidth_rate_limit(
              GatewayARN='string'
          )
        :type GatewayARN: string
        :param GatewayARN: **[REQUIRED]**

          The Amazon Resource Name (ARN) of the gateway. Use the  ListGateways operation to return a
          list of gateways for your account and AWS Region.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'GatewayARN': 'string',
                'AverageUploadRateLimitInBitsPerSec': 123,
                'AverageDownloadRateLimitInBitsPerSec': 123
            }
          **Response Structure**

          - *(dict) --*

            A JSON object containing the following fields:

            - **GatewayARN** *(string) --*

              The Amazon Resource Name (ARN) of the gateway. Use the  ListGateways operation to
              return a list of gateways for your account and AWS Region.

            - **AverageUploadRateLimitInBitsPerSec** *(integer) --*

              The average upload bandwidth rate limit in bits per second. This field does not appear
              in the response if the upload rate limit is not set.

            - **AverageDownloadRateLimitInBitsPerSec** *(integer) --*

              The average download bandwidth rate limit in bits per second. This field does not
              appear in the response if the download rate limit is not set.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_cache(self, GatewayARN: str) -> ClientDescribeCacheResponseTypeDef:
        """
        Returns information about the cache of a gateway. This operation is only supported in the
        cached volume, tape and file gateway types.

        The response includes disk IDs that are configured as cache, and it includes the amount of
        cache allocated and used.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/storagegateway-2013-06-30/DescribeCache>`_

        **Request Syntax**
        ::

          response = client.describe_cache(
              GatewayARN='string'
          )
        :type GatewayARN: string
        :param GatewayARN: **[REQUIRED]**

          The Amazon Resource Name (ARN) of the gateway. Use the  ListGateways operation to return a
          list of gateways for your account and AWS Region.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'GatewayARN': 'string',
                'DiskIds': [
                    'string',
                ],
                'CacheAllocatedInBytes': 123,
                'CacheUsedPercentage': 123.0,
                'CacheDirtyPercentage': 123.0,
                'CacheHitPercentage': 123.0,
                'CacheMissPercentage': 123.0
            }
          **Response Structure**

          - *(dict) --*

            - **GatewayARN** *(string) --*

              The Amazon Resource Name (ARN) of the gateway. Use the  ListGateways operation to
              return a list of gateways for your account and AWS Region.

            - **DiskIds** *(list) --*

              An array of strings that identify disks that are to be configured as working storage.
              Each string have a minimum length of 1 and maximum length of 300. You can get the disk
              IDs from the  ListLocalDisks API.

              - *(string) --*

            - **CacheAllocatedInBytes** *(integer) --*

              The amount of cache in bytes allocated to the a gateway.

            - **CacheUsedPercentage** *(float) --*

              Percent use of the gateway's cache storage. This metric applies only to the
              gateway-cached volume setup. The sample is taken at the end of the reporting period.

            - **CacheDirtyPercentage** *(float) --*

              The file share's contribution to the overall percentage of the gateway's cache that
              has not been persisted to AWS. The sample is taken at the end of the reporting period.

            - **CacheHitPercentage** *(float) --*

              Percent of application read operations from the file shares that are served from
              cache. The sample is taken at the end of the reporting period.

            - **CacheMissPercentage** *(float) --*

              Percent of application read operations from the file shares that are not served from
              cache. The sample is taken at the end of the reporting period.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_cached_iscsi_volumes(
        self, VolumeARNs: List[str]
    ) -> ClientDescribeCachedIscsiVolumesResponseTypeDef:
        """
        Returns a description of the gateway volumes specified in the request. This operation is
        only supported in the cached volume gateway types.

        The list of gateway volumes in the request must be from one gateway. In the response Amazon
        Storage Gateway returns volume information sorted by volume Amazon Resource Name (ARN).

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/storagegateway-2013-06-30/DescribeCachediSCSIVolumes>`_

        **Request Syntax**
        ::

          response = client.describe_cached_iscsi_volumes(
              VolumeARNs=[
                  'string',
              ]
          )
        :type VolumeARNs: list
        :param VolumeARNs: **[REQUIRED]**

          An array of strings where each string represents the Amazon Resource Name (ARN) of a
          cached volume. All of the specified cached volumes must from the same gateway. Use
          ListVolumes to get volume ARNs for a gateway.

          - *(string) --*

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'CachediSCSIVolumes': [
                    {
                        'VolumeARN': 'string',
                        'VolumeId': 'string',
                        'VolumeType': 'string',
                        'VolumeStatus': 'string',
                        'VolumeAttachmentStatus': 'string',
                        'VolumeSizeInBytes': 123,
                        'VolumeProgress': 123.0,
                        'SourceSnapshotId': 'string',
                        'VolumeiSCSIAttributes': {
                            'TargetARN': 'string',
                            'NetworkInterfaceId': 'string',
                            'NetworkInterfacePort': 123,
                            'LunNumber': 123,
                            'ChapEnabled': True|False
                        },
                        'CreatedDate': datetime(2015, 1, 1),
                        'VolumeUsedInBytes': 123,
                        'KMSKey': 'string',
                        'TargetName': 'string'
                    },
                ]
            }
          **Response Structure**

          - *(dict) --*

            A JSON object containing the following fields:

            - **CachediSCSIVolumes** *(list) --*

              An array of objects where each object contains metadata about one cached volume.

              - *(dict) --*

                Describes an iSCSI cached volume.

                - **VolumeARN** *(string) --*

                  The Amazon Resource Name (ARN) of the storage volume.

                - **VolumeId** *(string) --*

                  The unique identifier of the volume, e.g. vol-AE4B946D.

                - **VolumeType** *(string) --*

                  One of the VolumeType enumeration values that describes the type of the volume.

                - **VolumeStatus** *(string) --*

                  One of the VolumeStatus values that indicates the state of the storage volume.

                - **VolumeAttachmentStatus** *(string) --*

                  A value that indicates whether a storage volume is attached to or detached from a
                  gateway. For more information, see `Moving Your Volumes to a Different Gateway
                  <https://docs.aws.amazon.com/storagegateway/latest/userguide/managing-volumes.html#attach-detach-volume>`__
                  .

                - **VolumeSizeInBytes** *(integer) --*

                  The size, in bytes, of the volume capacity.

                - **VolumeProgress** *(float) --*

                  Represents the percentage complete if the volume is restoring or bootstrapping
                  that represents the percent of data transferred. This field does not appear in the
                  response if the cached volume is not restoring or bootstrapping.

                - **SourceSnapshotId** *(string) --*

                  If the cached volume was created from a snapshot, this field contains the snapshot
                  ID used, e.g. snap-78e22663. Otherwise, this field is not included.

                - **VolumeiSCSIAttributes** *(dict) --*

                  An  VolumeiSCSIAttributes object that represents a collection of iSCSI attributes
                  for one stored volume.

                  - **TargetARN** *(string) --*

                    The Amazon Resource Name (ARN) of the volume target.

                  - **NetworkInterfaceId** *(string) --*

                    The network interface identifier.

                  - **NetworkInterfacePort** *(integer) --*

                    The port used to communicate with iSCSI targets.

                  - **LunNumber** *(integer) --*

                    The logical disk number.

                  - **ChapEnabled** *(boolean) --*

                    Indicates whether mutual CHAP is enabled for the iSCSI target.

                - **CreatedDate** *(datetime) --*

                  The date the volume was created. Volumes created prior to March 28, 2017 don’t
                  have this time stamp.

                - **VolumeUsedInBytes** *(integer) --*

                  The size of the data stored on the volume in bytes. This value is calculated based
                  on the number of blocks that are touched, instead of the actual amount of data
                  written. This value can be useful for sequential write patterns but less accurate
                  for random write patterns. ``VolumeUsedInBytes`` is different from the compressed
                  size of the volume, which is the value that is used to calculate your bill.

                  .. note::

                    This value is not available for volumes created prior to May 13, 2015, until you
                    store data on the volume.

                - **KMSKey** *(string) --*

                  The Amazon Resource Name (ARN) of the AWS KMS key used for Amazon S3 server side
                  encryption. This value can only be set when KMSEncrypted is true. Optional.

                - **TargetName** *(string) --*

                  The name of the iSCSI target used by an initiator to connect to a volume and used
                  as a suffix for the target ARN. For example, specifying ``TargetName`` as
                  *myvolume* results in the target ARN of
                  ``arn:aws:storagegateway:us-east-2:111122223333:gateway/sgw-12A3456B/target/iqn.1997-05.com.amazon:myvolume``
                  . The target name must be unique across all volumes on a gateway.

                  If you don't specify a value, Storage Gateway uses the value that was previously
                  used for this volume as the new target name.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_chap_credentials(
        self, TargetARN: str
    ) -> ClientDescribeChapCredentialsResponseTypeDef:
        """
        Returns an array of Challenge-Handshake Authentication Protocol (CHAP) credentials
        information for a specified iSCSI target, one for each target-initiator pair. This operation
        is supported in the volume and tape gateway types.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/storagegateway-2013-06-30/DescribeChapCredentials>`_

        **Request Syntax**
        ::

          response = client.describe_chap_credentials(
              TargetARN='string'
          )
        :type TargetARN: string
        :param TargetARN: **[REQUIRED]**

          The Amazon Resource Name (ARN) of the iSCSI volume target. Use the
          DescribeStorediSCSIVolumes operation to return to retrieve the TargetARN for specified
          VolumeARN.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'ChapCredentials': [
                    {
                        'TargetARN': 'string',
                        'SecretToAuthenticateInitiator': 'string',
                        'InitiatorName': 'string',
                        'SecretToAuthenticateTarget': 'string'
                    },
                ]
            }
          **Response Structure**

          - *(dict) --*

            A JSON object containing a .

            - **ChapCredentials** *(list) --*

              An array of  ChapInfo objects that represent CHAP credentials. Each object in the
              array contains CHAP credential information for one target-initiator pair. If no CHAP
              credentials are set, an empty array is returned. CHAP credential information is
              provided in a JSON object with the following fields:

              * **InitiatorName** : The iSCSI initiator that connects to the target.

              * **SecretToAuthenticateInitiator** : The secret key that the initiator (for example,
              the Windows client) must provide to participate in mutual CHAP with the target.

              * **SecretToAuthenticateTarget** : The secret key that the target must provide to
              participate in mutual CHAP with the initiator (e.g. Windows client).

              * **TargetARN** : The Amazon Resource Name (ARN) of the storage volume.

              - *(dict) --*

                Describes Challenge-Handshake Authentication Protocol (CHAP) information that
                supports authentication between your gateway and iSCSI initiators.

                - **TargetARN** *(string) --*

                  The Amazon Resource Name (ARN) of the volume.

                  Valid Values: 50 to 500 lowercase letters, numbers, periods (.), and hyphens (-).

                - **SecretToAuthenticateInitiator** *(string) --*

                  The secret key that the initiator (for example, the Windows client) must provide
                  to participate in mutual CHAP with the target.

                - **InitiatorName** *(string) --*

                  The iSCSI initiator that connects to the target.

                - **SecretToAuthenticateTarget** *(string) --*

                  The secret key that the target must provide to participate in mutual CHAP with the
                  initiator (e.g. Windows client).
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_gateway_information(
        self, GatewayARN: str
    ) -> ClientDescribeGatewayInformationResponseTypeDef:
        """
        Returns metadata about a gateway such as its name, network interfaces, configured time zone,
        and the state (whether the gateway is running or not). To specify which gateway to describe,
        use the Amazon Resource Name (ARN) of the gateway in your request.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/storagegateway-2013-06-30/DescribeGatewayInformation>`_

        **Request Syntax**
        ::

          response = client.describe_gateway_information(
              GatewayARN='string'
          )
        :type GatewayARN: string
        :param GatewayARN: **[REQUIRED]**

          The Amazon Resource Name (ARN) of the gateway. Use the  ListGateways operation to return a
          list of gateways for your account and AWS Region.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'GatewayARN': 'string',
                'GatewayId': 'string',
                'GatewayName': 'string',
                'GatewayTimezone': 'string',
                'GatewayState': 'string',
                'GatewayNetworkInterfaces': [
                    {
                        'Ipv4Address': 'string',
                        'MacAddress': 'string',
                        'Ipv6Address': 'string'
                    },
                ],
                'GatewayType': 'string',
                'NextUpdateAvailabilityDate': 'string',
                'LastSoftwareUpdate': 'string',
                'Ec2InstanceId': 'string',
                'Ec2InstanceRegion': 'string',
                'Tags': [
                    {
                        'Key': 'string',
                        'Value': 'string'
                    },
                ],
                'VPCEndpoint': 'string',
                'CloudWatchLogGroupARN': 'string',
                'HostEnvironment': 'VMWARE'|'HYPER-V'|'EC2'|'OTHER'
            }
          **Response Structure**

          - *(dict) --*

            A JSON object containing the following fields:

            - **GatewayARN** *(string) --*

              The Amazon Resource Name (ARN) of the gateway. Use the  ListGateways operation to
              return a list of gateways for your account and AWS Region.

            - **GatewayId** *(string) --*

              The unique identifier assigned to your gateway during activation. This ID becomes part
              of the gateway Amazon Resource Name (ARN), which you use as input for other
              operations.

            - **GatewayName** *(string) --*

              The name you configured for your gateway.

            - **GatewayTimezone** *(string) --*

              A value that indicates the time zone configured for the gateway.

            - **GatewayState** *(string) --*

              A value that indicates the operating state of the gateway.

            - **GatewayNetworkInterfaces** *(list) --*

              A  NetworkInterface array that contains descriptions of the gateway network
              interfaces.

              - *(dict) --*

                Describes a gateway's network interface.

                - **Ipv4Address** *(string) --*

                  The Internet Protocol version 4 (IPv4) address of the interface.

                - **MacAddress** *(string) --*

                  The Media Access Control (MAC) address of the interface.

                  .. note::

                    This is currently unsupported and will not be returned in output.

                - **Ipv6Address** *(string) --*

                  The Internet Protocol version 6 (IPv6) address of the interface. *Currently not
                  supported* .

            - **GatewayType** *(string) --*

              The type of the gateway.

            - **NextUpdateAvailabilityDate** *(string) --*

              The date on which an update to the gateway is available. This date is in the time zone
              of the gateway. If the gateway is not available for an update this field is not
              returned in the response.

            - **LastSoftwareUpdate** *(string) --*

              The date on which the last software update was applied to the gateway. If the gateway
              has never been updated, this field does not return a value in the response.

            - **Ec2InstanceId** *(string) --*

              The ID of the Amazon EC2 instance that was used to launch the gateway.

            - **Ec2InstanceRegion** *(string) --*

              The AWS Region where the Amazon EC2 instance is located.

            - **Tags** *(list) --*

              A list of up to 50 tags assigned to the gateway, sorted alphabetically by key name.
              Each tag is a key-value pair. For a gateway with more than 10 tags assigned, you can
              view all tags using the ``ListTagsForResource`` API operation.

              - *(dict) --*

                A key-value pair that helps you manage, filter, and search for your resource.
                Allowed characters: letters, white space, and numbers, representable in UTF-8, and
                the following characters: + - = . _ : /

                - **Key** *(string) --*

                  Tag key (String). The key can't start with aws:.

                - **Value** *(string) --*

                  Value of the tag key.

            - **VPCEndpoint** *(string) --*

              The configuration settings for the virtual private cloud (VPC) endpoint for your
              gateway.

            - **CloudWatchLogGroupARN** *(string) --*

              The Amazon Resource Name (ARN) of the Amazon CloudWatch Log Group that is used to
              monitor events in the gateway.

            - **HostEnvironment** *(string) --*

              The type of hypervisor environment used by the host.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_maintenance_start_time(
        self, GatewayARN: str
    ) -> ClientDescribeMaintenanceStartTimeResponseTypeDef:
        """
        Returns your gateway's weekly maintenance start time including the day and time of the week.
        Note that values are in terms of the gateway's time zone.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/storagegateway-2013-06-30/DescribeMaintenanceStartTime>`_

        **Request Syntax**
        ::

          response = client.describe_maintenance_start_time(
              GatewayARN='string'
          )
        :type GatewayARN: string
        :param GatewayARN: **[REQUIRED]**

          The Amazon Resource Name (ARN) of the gateway. Use the  ListGateways operation to return a
          list of gateways for your account and AWS Region.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'GatewayARN': 'string',
                'HourOfDay': 123,
                'MinuteOfHour': 123,
                'DayOfWeek': 123,
                'DayOfMonth': 123,
                'Timezone': 'string'
            }
          **Response Structure**

          - *(dict) --*

            A JSON object containing the following fields:

            *  DescribeMaintenanceStartTimeOutput$DayOfMonth

            *  DescribeMaintenanceStartTimeOutput$DayOfWeek

            *  DescribeMaintenanceStartTimeOutput$HourOfDay

            *  DescribeMaintenanceStartTimeOutput$MinuteOfHour

            *  DescribeMaintenanceStartTimeOutput$Timezone

            - **GatewayARN** *(string) --*

              The Amazon Resource Name (ARN) of the gateway. Use the  ListGateways operation to
              return a list of gateways for your account and AWS Region.

            - **HourOfDay** *(integer) --*

              The hour component of the maintenance start time represented as *hh* , where *hh* is
              the hour (0 to 23). The hour of the day is in the time zone of the gateway.

            - **MinuteOfHour** *(integer) --*

              The minute component of the maintenance start time represented as *mm* , where *mm* is
              the minute (0 to 59). The minute of the hour is in the time zone of the gateway.

            - **DayOfWeek** *(integer) --*

              An ordinal number between 0 and 6 that represents the day of the week, where 0
              represents Sunday and 6 represents Saturday. The day of week is in the time zone of
              the gateway.

            - **DayOfMonth** *(integer) --*

              The day of the month component of the maintenance start time represented as an ordinal
              number from 1 to 28, where 1 represents the first day of the month and 28 represents
              the last day of the month.

              .. note::

                This value is only available for tape and volume gateways.

            - **Timezone** *(string) --*

              A value that indicates the time zone that is set for the gateway. The start time and
              day of week specified should be in the time zone of the gateway.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_nfs_file_shares(
        self, FileShareARNList: List[str]
    ) -> ClientDescribeNfsFileSharesResponseTypeDef:
        """
        Gets a description for one or more Network File System (NFS) file shares from a file
        gateway. This operation is only supported for file gateways.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/storagegateway-2013-06-30/DescribeNFSFileShares>`_

        **Request Syntax**
        ::

          response = client.describe_nfs_file_shares(
              FileShareARNList=[
                  'string',
              ]
          )
        :type FileShareARNList: list
        :param FileShareARNList: **[REQUIRED]**

          An array containing the Amazon Resource Name (ARN) of each file share to be described.

          - *(string) --*

            The Amazon Resource Name (ARN) of the file share.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'NFSFileShareInfoList': [
                    {
                        'NFSFileShareDefaults': {
                            'FileMode': 'string',
                            'DirectoryMode': 'string',
                            'GroupId': 123,
                            'OwnerId': 123
                        },
                        'FileShareARN': 'string',
                        'FileShareId': 'string',
                        'FileShareStatus': 'string',
                        'GatewayARN': 'string',
                        'KMSEncrypted': True|False,
                        'KMSKey': 'string',
                        'Path': 'string',
                        'Role': 'string',
                        'LocationARN': 'string',
                        'DefaultStorageClass': 'string',
                        'ObjectACL':
                        'private'|'public-read'|'public-read-write'
                        |'authenticated-read'|'bucket-owner-read'
                        |'bucket-owner-full-control'|'aws-exec-read',
                        'ClientList': [
                            'string',
                        ],
                        'Squash': 'string',
                        'ReadOnly': True|False,
                        'GuessMIMETypeEnabled': True|False,
                        'RequesterPays': True|False,
                        'Tags': [
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

            DescribeNFSFileSharesOutput

            - **NFSFileShareInfoList** *(list) --*

              An array containing a description for each requested file share.

              - *(dict) --*

                The Unix file permissions and ownership information assigned, by default, to native
                S3 objects when file gateway discovers them in S3 buckets. This operation is only
                supported in file gateways.

                - **NFSFileShareDefaults** *(dict) --*

                  Describes Network File System (NFS) file share default values. Files and folders
                  stored as Amazon S3 objects in S3 buckets don't, by default, have Unix file
                  permissions assigned to them. Upon discovery in an S3 bucket by Storage Gateway,
                  the S3 objects that represent files and folders are assigned these default Unix
                  permissions. This operation is only supported for file gateways.

                  - **FileMode** *(string) --*

                    The Unix file mode in the form "nnnn". For example, "0666" represents the
                    default file mode inside the file share. The default value is 0666.

                  - **DirectoryMode** *(string) --*

                    The Unix directory mode in the form "nnnn". For example, "0666" represents the
                    default access mode for all directories inside the file share. The default value
                    is 0777.

                  - **GroupId** *(integer) --*

                    The default group ID for the file share (unless the files have another group ID
                    specified). The default value is nfsnobody.

                  - **OwnerId** *(integer) --*

                    The default owner ID for files in the file share (unless the files have another
                    owner ID specified). The default value is nfsnobody.

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

                - **KMSEncrypted** *(boolean) --*

                  True to use Amazon S3 server side encryption with your own AWS KMS key, or false
                  to use a key managed by Amazon S3. Optional.

                - **KMSKey** *(string) --*

                  The Amazon Resource Name (ARN) of the AWS KMS key used for Amazon S3 server side
                  encryption. This value can only be set when KMSEncrypted is true. Optional.

                - **Path** *(string) --*

                  The file share path used by the NFS client to identify the mount point.

                - **Role** *(string) --*

                  The ARN of the IAM role that file gateway assumes when it accesses the underlying
                  storage.

                - **LocationARN** *(string) --*

                  The ARN of the backend storage used for storing file data.

                - **DefaultStorageClass** *(string) --*

                  The default storage class for objects put into an Amazon S3 bucket by the file
                  gateway. Possible values are ``S3_STANDARD`` , ``S3_STANDARD_IA`` , or
                  ``S3_ONEZONE_IA`` . If this field is not populated, the default value
                  ``S3_STANDARD`` is used. Optional.

                - **ObjectACL** *(string) --*

                  A value that sets the access control list permission for objects in the S3 bucket
                  that a file gateway puts objects into. The default value is "private".

                - **ClientList** *(list) --*

                  The list of clients that are allowed to access the file gateway. The list must
                  contain either valid IP addresses or valid CIDR blocks.

                  - *(string) --*

                - **Squash** *(string) --*

                  The user mapped to anonymous user. Valid options are the following:

                  * ``RootSquash`` - Only root is mapped to anonymous user.

                  * ``NoSquash`` - No one is mapped to anonymous user

                  * ``AllSquash`` - Everyone is mapped to anonymous user.

                - **ReadOnly** *(boolean) --*

                  A value that sets the write status of a file share. This value is true if the
                  write status is read-only, and otherwise false.

                - **GuessMIMETypeEnabled** *(boolean) --*

                  A value that enables guessing of the MIME type for uploaded objects based on file
                  extensions. Set this value to true to enable MIME type guessing, and otherwise to
                  false. The default value is true.

                - **RequesterPays** *(boolean) --*

                  A value that sets who pays the cost of the request and the cost associated with
                  data download from the S3 bucket. If this value is set to true, the requester pays
                  the costs. Otherwise the S3 bucket owner pays. However, the S3 bucket owner always
                  pays the cost of storing data.

                  .. note::

                     ``RequesterPays`` is a configuration for the S3 bucket that backs the file
                     share, so make sure that the configuration on the file share is the same as the
                     S3 bucket configuration.

                - **Tags** *(list) --*

                  A list of up to 50 tags assigned to the NFS file share, sorted alphabetically by
                  key name. Each tag is a key-value pair. For a gateway with more than 10 tags
                  assigned, you can view all tags using the ``ListTagsForResource`` API operation.

                  - *(dict) --*

                    A key-value pair that helps you manage, filter, and search for your resource.
                    Allowed characters: letters, white space, and numbers, representable in UTF-8,
                    and the following characters: + - = . _ : /

                    - **Key** *(string) --*

                      Tag key (String). The key can't start with aws:.

                    - **Value** *(string) --*

                      Value of the tag key.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_smb_file_shares(
        self, FileShareARNList: List[str]
    ) -> ClientDescribeSmbFileSharesResponseTypeDef:
        """
        Gets a description for one or more Server Message Block (SMB) file shares from a file
        gateway. This operation is only supported for file gateways.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/storagegateway-2013-06-30/DescribeSMBFileShares>`_

        **Request Syntax**
        ::

          response = client.describe_smb_file_shares(
              FileShareARNList=[
                  'string',
              ]
          )
        :type FileShareARNList: list
        :param FileShareARNList: **[REQUIRED]**

          An array containing the Amazon Resource Name (ARN) of each file share to be described.

          - *(string) --*

            The Amazon Resource Name (ARN) of the file share.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'SMBFileShareInfoList': [
                    {
                        'FileShareARN': 'string',
                        'FileShareId': 'string',
                        'FileShareStatus': 'string',
                        'GatewayARN': 'string',
                        'KMSEncrypted': True|False,
                        'KMSKey': 'string',
                        'Path': 'string',
                        'Role': 'string',
                        'LocationARN': 'string',
                        'DefaultStorageClass': 'string',
                        'ObjectACL':
                        'private'|'public-read'|'public-read-write'
                        |'authenticated-read'|'bucket-owner-read'
                        |'bucket-owner-full-control'|'aws-exec-read',
                        'ReadOnly': True|False,
                        'GuessMIMETypeEnabled': True|False,
                        'RequesterPays': True|False,
                        'SMBACLEnabled': True|False,
                        'AdminUserList': [
                            'string',
                        ],
                        'ValidUserList': [
                            'string',
                        ],
                        'InvalidUserList': [
                            'string',
                        ],
                        'Authentication': 'string',
                        'Tags': [
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

            DescribeSMBFileSharesOutput

            - **SMBFileShareInfoList** *(list) --*

              An array containing a description for each requested file share.

              - *(dict) --*

                The Windows file permissions and ownership information assigned, by default, to
                native S3 objects when file gateway discovers them in S3 buckets. This operation is
                only supported for file gateways.

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

                - **KMSEncrypted** *(boolean) --*

                  True to use Amazon S3 server-side encryption with your own AWS KMS key, or false
                  to use a key managed by Amazon S3. Optional.

                - **KMSKey** *(string) --*

                  The Amazon Resource Name (ARN) of the AWS KMS key used for Amazon S3 server side
                  encryption. This value can only be set when KMSEncrypted is true. Optional.

                - **Path** *(string) --*

                  The file share path used by the SMB client to identify the mount point.

                - **Role** *(string) --*

                  The ARN of the IAM role that file gateway assumes when it accesses the underlying
                  storage.

                - **LocationARN** *(string) --*

                  The ARN of the backend storage used for storing file data.

                - **DefaultStorageClass** *(string) --*

                  The default storage class for objects put into an Amazon S3 bucket by the file
                  gateway. Possible values are ``S3_STANDARD`` , ``S3_STANDARD_IA`` , or
                  ``S3_ONEZONE_IA`` . If this field is not populated, the default value
                  ``S3_STANDARD`` is used. Optional.

                - **ObjectACL** *(string) --*

                  A value that sets the access control list permission for objects in the S3 bucket
                  that a file gateway puts objects into. The default value is "private".

                - **ReadOnly** *(boolean) --*

                  A value that sets the write status of a file share. This value is true if the
                  write status is read-only, and otherwise false.

                - **GuessMIMETypeEnabled** *(boolean) --*

                  A value that enables guessing of the MIME type for uploaded objects based on file
                  extensions. Set this value to true to enable MIME type guessing, and otherwise to
                  false. The default value is true.

                - **RequesterPays** *(boolean) --*

                  A value that sets who pays the cost of the request and the cost associated with
                  data download from the S3 bucket. If this value is set to true, the requester pays
                  the costs. Otherwise the S3 bucket owner pays. However, the S3 bucket owner always
                  pays the cost of storing data.

                  .. note::

                     ``RequesterPays`` is a configuration for the S3 bucket that backs the file
                     share, so make sure that the configuration on the file share is the same as the
                     S3 bucket configuration.

                - **SMBACLEnabled** *(boolean) --*

                  If this value is set to "true", indicates that ACL (access control list) is
                  enabled on the SMB file share. If it is set to "false", it indicates that file and
                  directory permissions are mapped to the POSIX permission.

                  For more information, see
                  https://docs.aws.amazon.com/storagegateway/latest/userguide/smb-acl.html in the
                  Storage Gateway User Guide.

                - **AdminUserList** *(list) --*

                  A list of users or groups in the Active Directory that have administrator rights
                  to the file share. A group must be prefixed with the @ character. For example
                  ``@group1`` . Can only be set if Authentication is set to ``ActiveDirectory`` .

                  - *(string) --*

                - **ValidUserList** *(list) --*

                  A list of users or groups in the Active Directory that are allowed to access the
                  file share. A group must be prefixed with the @ character. For example ``@group1``
                  . Can only be set if Authentication is set to ``ActiveDirectory`` .

                  - *(string) --*

                - **InvalidUserList** *(list) --*

                  A list of users or groups in the Active Directory that are not allowed to access
                  the file share. A group must be prefixed with the @ character. For example
                  ``@group1`` . Can only be set if Authentication is set to ``ActiveDirectory`` .

                  - *(string) --*

                - **Authentication** *(string) --*

                  The authentication method of the file share.

                  Valid values are ``ActiveDirectory`` or ``GuestAccess`` . The default is
                  ``ActiveDirectory`` .

                - **Tags** *(list) --*

                  A list of up to 50 tags assigned to the SMB file share, sorted alphabetically by
                  key name. Each tag is a key-value pair. For a gateway with more than 10 tags
                  assigned, you can view all tags using the ``ListTagsForResource`` API operation.

                  - *(dict) --*

                    A key-value pair that helps you manage, filter, and search for your resource.
                    Allowed characters: letters, white space, and numbers, representable in UTF-8,
                    and the following characters: + - = . _ : /

                    - **Key** *(string) --*

                      Tag key (String). The key can't start with aws:.

                    - **Value** *(string) --*

                      Value of the tag key.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_smb_settings(self, GatewayARN: str) -> ClientDescribeSmbSettingsResponseTypeDef:
        """
        Gets a description of a Server Message Block (SMB) file share settings from a file gateway.
        This operation is only supported for file gateways.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/storagegateway-2013-06-30/DescribeSMBSettings>`_

        **Request Syntax**
        ::

          response = client.describe_smb_settings(
              GatewayARN='string'
          )
        :type GatewayARN: string
        :param GatewayARN: **[REQUIRED]**

          The Amazon Resource Name (ARN) of the gateway. Use the  ListGateways operation to return a
          list of gateways for your account and AWS Region.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'GatewayARN': 'string',
                'DomainName': 'string',
                'ActiveDirectoryStatus':
                'ACCESS_DENIED'|'DETACHED'|'JOINED'|'JOINING'|'NETWORK_ERROR'|'TIMEOUT'
                |'UNKNOWN_ERROR',
                'SMBGuestPasswordSet': True|False,
                'SMBSecurityStrategy': 'ClientSpecified'|'MandatorySigning'|'MandatoryEncryption'
            }
          **Response Structure**

          - *(dict) --*

            - **GatewayARN** *(string) --*

              The Amazon Resource Name (ARN) of the gateway. Use the  ListGateways operation to
              return a list of gateways for your account and AWS Region.

            - **DomainName** *(string) --*

              The name of the domain that the gateway is joined to.

            - **ActiveDirectoryStatus** *(string) --*

              Indicates the status of a gateway that is a member of the Active Directory domain.

              * ACCESS_DENIED: Indicates that the ``JoinDomain`` operation failed due to an
              authentication error.

              * DETACHED: Indicates that gateway is not joined to a domain.

              * JOINED: Indicates that the gateway has successfully joined a domain.

              * JOINING: Indicates that a ``JoinDomain`` operation is in progress.

              * NETWORK_ERROR: Indicates that ``JoinDomain`` operation failed due to a network or
              connectivity error.

              * TIMEOUT: Indicates that the ``JoinDomain`` operation failed because the operation
              didn't complete within the allotted time.

              * UNKNOWN_ERROR: Indicates that the ``JoinDomain`` operation failed due to another
              type of error.

            - **SMBGuestPasswordSet** *(boolean) --*

              This value is true if a password for the guest user “smbguest” is set, and otherwise
              false.

            - **SMBSecurityStrategy** *(string) --*

              The type of security strategy that was specified for file gateway.

              ClientSpecified: if you use this option, requests are established based on what is
              negotiated by the client. This option is recommended when you want to maximize
              compatibility across different clients in your environment.

              MandatorySigning: if you use this option, file gateway only allows connections from
              SMBv2 or SMBv3 clients that have signing enabled. This option works with SMB clients
              on Microsoft Windows Vista, Windows Server 2008 or newer.

              MandatoryEncryption: if you use this option, file gateway only allows connections from
              SMBv3 clients that have encryption enabled. This option is highly recommended for
              environments that handle sensitive data. This option works with SMB clients on
              Microsoft Windows 8, Windows Server 2012 or newer.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_snapshot_schedule(
        self, VolumeARN: str
    ) -> ClientDescribeSnapshotScheduleResponseTypeDef:
        """
        Describes the snapshot schedule for the specified gateway volume. The snapshot schedule
        information includes intervals at which snapshots are automatically initiated on the volume.
        This operation is only supported in the cached volume and stored volume types.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/storagegateway-2013-06-30/DescribeSnapshotSchedule>`_

        **Request Syntax**
        ::

          response = client.describe_snapshot_schedule(
              VolumeARN='string'
          )
        :type VolumeARN: string
        :param VolumeARN: **[REQUIRED]**

          The Amazon Resource Name (ARN) of the volume. Use the  ListVolumes operation to return a
          list of gateway volumes.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'VolumeARN': 'string',
                'StartAt': 123,
                'RecurrenceInHours': 123,
                'Description': 'string',
                'Timezone': 'string',
                'Tags': [
                    {
                        'Key': 'string',
                        'Value': 'string'
                    },
                ]
            }
          **Response Structure**

          - *(dict) --*

            - **VolumeARN** *(string) --*

              The Amazon Resource Name (ARN) of the volume that was specified in the request.

            - **StartAt** *(integer) --*

              The hour of the day at which the snapshot schedule begins represented as *hh* , where
              *hh* is the hour (0 to 23). The hour of the day is in the time zone of the gateway.

            - **RecurrenceInHours** *(integer) --*

              The number of hours between snapshots.

            - **Description** *(string) --*

              The snapshot description.

            - **Timezone** *(string) --*

              A value that indicates the time zone of the gateway.

            - **Tags** *(list) --*

              A list of up to 50 tags assigned to the snapshot schedule, sorted alphabetically by
              key name. Each tag is a key-value pair. For a gateway with more than 10 tags assigned,
              you can view all tags using the ``ListTagsForResource`` API operation.

              - *(dict) --*

                A key-value pair that helps you manage, filter, and search for your resource.
                Allowed characters: letters, white space, and numbers, representable in UTF-8, and
                the following characters: + - = . _ : /

                - **Key** *(string) --*

                  Tag key (String). The key can't start with aws:.

                - **Value** *(string) --*

                  Value of the tag key.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_stored_iscsi_volumes(
        self, VolumeARNs: List[str]
    ) -> ClientDescribeStoredIscsiVolumesResponseTypeDef:
        """
        Returns the description of the gateway volumes specified in the request. The list of gateway
        volumes in the request must be from one gateway. In the response Amazon Storage Gateway
        returns volume information sorted by volume ARNs. This operation is only supported in stored
        volume gateway type.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/storagegateway-2013-06-30/DescribeStorediSCSIVolumes>`_

        **Request Syntax**
        ::

          response = client.describe_stored_iscsi_volumes(
              VolumeARNs=[
                  'string',
              ]
          )
        :type VolumeARNs: list
        :param VolumeARNs: **[REQUIRED]**

          An array of strings where each string represents the Amazon Resource Name (ARN) of a
          stored volume. All of the specified stored volumes must from the same gateway. Use
          ListVolumes to get volume ARNs for a gateway.

          - *(string) --*

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'StorediSCSIVolumes': [
                    {
                        'VolumeARN': 'string',
                        'VolumeId': 'string',
                        'VolumeType': 'string',
                        'VolumeStatus': 'string',
                        'VolumeAttachmentStatus': 'string',
                        'VolumeSizeInBytes': 123,
                        'VolumeProgress': 123.0,
                        'VolumeDiskId': 'string',
                        'SourceSnapshotId': 'string',
                        'PreservedExistingData': True|False,
                        'VolumeiSCSIAttributes': {
                            'TargetARN': 'string',
                            'NetworkInterfaceId': 'string',
                            'NetworkInterfacePort': 123,
                            'LunNumber': 123,
                            'ChapEnabled': True|False
                        },
                        'CreatedDate': datetime(2015, 1, 1),
                        'VolumeUsedInBytes': 123,
                        'KMSKey': 'string',
                        'TargetName': 'string'
                    },
                ]
            }
          **Response Structure**

          - *(dict) --*

            - **StorediSCSIVolumes** *(list) --*

              Describes a single unit of output from  DescribeStorediSCSIVolumes . The following
              fields are returned:

              * **ChapEnabled** : Indicates whether mutual CHAP is enabled for the iSCSI target.

              * **LunNumber** : The logical disk number.

              * **NetworkInterfaceId** : The network interface ID of the stored volume that
              initiator use to map the stored volume as an iSCSI target.

              * **NetworkInterfacePort** : The port used to communicate with iSCSI targets.

              * **PreservedExistingData** : Indicates if when the stored volume was created,
              existing data on the underlying local disk was preserved.

              * **SourceSnapshotId** : If the stored volume was created from a snapshot, this field
              contains the snapshot ID used, e.g. snap-1122aabb. Otherwise, this field is not
              included.

              * **StorediSCSIVolumes** : An array of StorediSCSIVolume objects where each object
              contains metadata about one stored volume.

              * **TargetARN** : The Amazon Resource Name (ARN) of the volume target.

              * **VolumeARN** : The Amazon Resource Name (ARN) of the stored volume.

              * **VolumeDiskId** : The disk ID of the local disk that was specified in the
              CreateStorediSCSIVolume operation.

              * **VolumeId** : The unique identifier of the storage volume, e.g. vol-1122AABB.

              * **VolumeiSCSIAttributes** : An  VolumeiSCSIAttributes object that represents a
              collection of iSCSI attributes for one stored volume.

              * **VolumeProgress** : Represents the percentage complete if the volume is restoring
              or bootstrapping that represents the percent of data transferred. This field does not
              appear in the response if the stored volume is not restoring or bootstrapping.

              * **VolumeSizeInBytes** : The size of the volume in bytes.

              * **VolumeStatus** : One of the ``VolumeStatus`` values that indicates the state of
              the volume.

              * **VolumeType** : One of the enumeration values describing the type of the volume.
              Currently, on STORED volumes are supported.

              - *(dict) --*

                Describes an iSCSI stored volume.

                - **VolumeARN** *(string) --*

                  The Amazon Resource Name (ARN) of the storage volume.

                - **VolumeId** *(string) --*

                  The unique identifier of the volume, e.g. vol-AE4B946D.

                - **VolumeType** *(string) --*

                  One of the VolumeType enumeration values describing the type of the volume.

                - **VolumeStatus** *(string) --*

                  One of the VolumeStatus values that indicates the state of the storage volume.

                - **VolumeAttachmentStatus** *(string) --*

                  A value that indicates whether a storage volume is attached to, detached from, or
                  is in the process of detaching from a gateway. For more information, see `Moving
                  Your Volumes to a Different Gateway
                  <https://docs.aws.amazon.com/storagegateway/latest/userguide/managing-volumes.html#attach-detach-volume>`__
                  .

                - **VolumeSizeInBytes** *(integer) --*

                  The size of the volume in bytes.

                - **VolumeProgress** *(float) --*

                  Represents the percentage complete if the volume is restoring or bootstrapping
                  that represents the percent of data transferred. This field does not appear in the
                  response if the stored volume is not restoring or bootstrapping.

                - **VolumeDiskId** *(string) --*

                  The ID of the local disk that was specified in the  CreateStorediSCSIVolume
                  operation.

                - **SourceSnapshotId** *(string) --*

                  If the stored volume was created from a snapshot, this field contains the snapshot
                  ID used, e.g. snap-78e22663. Otherwise, this field is not included.

                - **PreservedExistingData** *(boolean) --*

                  Indicates if when the stored volume was created, existing data on the underlying
                  local disk was preserved.

                  Valid Values: true, false

                - **VolumeiSCSIAttributes** *(dict) --*

                  An  VolumeiSCSIAttributes object that represents a collection of iSCSI attributes
                  for one stored volume.

                  - **TargetARN** *(string) --*

                    The Amazon Resource Name (ARN) of the volume target.

                  - **NetworkInterfaceId** *(string) --*

                    The network interface identifier.

                  - **NetworkInterfacePort** *(integer) --*

                    The port used to communicate with iSCSI targets.

                  - **LunNumber** *(integer) --*

                    The logical disk number.

                  - **ChapEnabled** *(boolean) --*

                    Indicates whether mutual CHAP is enabled for the iSCSI target.

                - **CreatedDate** *(datetime) --*

                  The date the volume was created. Volumes created prior to March 28, 2017 don’t
                  have this time stamp.

                - **VolumeUsedInBytes** *(integer) --*

                  The size of the data stored on the volume in bytes. This value is calculated based
                  on the number of blocks that are touched, instead of the actual amount of data
                  written. This value can be useful for sequential write patterns but less accurate
                  for random write patterns. ``VolumeUsedInBytes`` is different from the compressed
                  size of the volume, which is the value that is used to calculate your bill.

                  .. note::

                    This value is not available for volumes created prior to May 13, 2015, until you
                    store data on the volume.

                - **KMSKey** *(string) --*

                  The Amazon Resource Name (ARN) of the AWS KMS key used for Amazon S3 server side
                  encryption. This value can only be set when KMSEncrypted is true. Optional.

                - **TargetName** *(string) --*

                  The name of the iSCSI target used by an initiator to connect to a volume and used
                  as a suffix for the target ARN. For example, specifying ``TargetName`` as
                  *myvolume* results in the target ARN of
                  ``arn:aws:storagegateway:us-east-2:111122223333:gateway/sgw-12A3456B/target/iqn.1997-05.com.amazon:myvolume``
                  . The target name must be unique across all volumes on a gateway.

                  If you don't specify a value, Storage Gateway uses the value that was previously
                  used for this volume as the new target name.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_tape_archives(
        self, TapeARNs: List[str] = None, Marker: str = None, Limit: int = None
    ) -> ClientDescribeTapeArchivesResponseTypeDef:
        """
        Returns a description of specified virtual tapes in the virtual tape shelf (VTS). This
        operation is only supported in the tape gateway type.

        If a specific ``TapeARN`` is not specified, AWS Storage Gateway returns a description of all
        virtual tapes found in the VTS associated with your account.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/storagegateway-2013-06-30/DescribeTapeArchives>`_

        **Request Syntax**
        ::

          response = client.describe_tape_archives(
              TapeARNs=[
                  'string',
              ],
              Marker='string',
              Limit=123
          )
        :type TapeARNs: list
        :param TapeARNs:

          Specifies one or more unique Amazon Resource Names (ARNs) that represent the virtual tapes
          you want to describe.

          - *(string) --*

        :type Marker: string
        :param Marker:

          An opaque string that indicates the position at which to begin describing virtual tapes.

        :type Limit: integer
        :param Limit:

          Specifies that the number of virtual tapes descried be limited to the specified number.

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
                'Marker': 'string'
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

            - **Marker** *(string) --*

              An opaque string that indicates the position at which the virtual tapes that were
              fetched for description ended. Use this marker in your next request to fetch the next
              set of virtual tapes in the virtual tape shelf (VTS). If there are no more virtual
              tapes to describe, this field does not appear in the response.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_tape_recovery_points(
        self, GatewayARN: str, Marker: str = None, Limit: int = None
    ) -> ClientDescribeTapeRecoveryPointsResponseTypeDef:
        """
        Returns a list of virtual tape recovery points that are available for the specified tape
        gateway.

        A recovery point is a point-in-time view of a virtual tape at which all the data on the
        virtual tape is consistent. If your gateway crashes, virtual tapes that have recovery points
        can be recovered to a new gateway. This operation is only supported in the tape gateway
        type.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/storagegateway-2013-06-30/DescribeTapeRecoveryPoints>`_

        **Request Syntax**
        ::

          response = client.describe_tape_recovery_points(
              GatewayARN='string',
              Marker='string',
              Limit=123
          )
        :type GatewayARN: string
        :param GatewayARN: **[REQUIRED]**

          The Amazon Resource Name (ARN) of the gateway. Use the  ListGateways operation to return a
          list of gateways for your account and AWS Region.

        :type Marker: string
        :param Marker:

          An opaque string that indicates the position at which to begin describing the virtual tape
          recovery points.

        :type Limit: integer
        :param Limit:

          Specifies that the number of virtual tape recovery points that are described be limited to
          the specified number.

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
                'Marker': 'string'
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

            - **Marker** *(string) --*

              An opaque string that indicates the position at which the virtual tape recovery points
              that were listed for description ended.

              Use this marker in your next request to list the next set of virtual tape recovery
              points in the list. If there are no more recovery points to describe, this field does
              not appear in the response.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_tapes(
        self, GatewayARN: str, TapeARNs: List[str] = None, Marker: str = None, Limit: int = None
    ) -> ClientDescribeTapesResponseTypeDef:
        """
        Returns a description of the specified Amazon Resource Name (ARN) of virtual tapes. If a
        ``TapeARN`` is not specified, returns a description of all virtual tapes associated with the
        specified gateway. This operation is only supported in the tape gateway type.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/storagegateway-2013-06-30/DescribeTapes>`_

        **Request Syntax**
        ::

          response = client.describe_tapes(
              GatewayARN='string',
              TapeARNs=[
                  'string',
              ],
              Marker='string',
              Limit=123
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

        :type Marker: string
        :param Marker:

          A marker value, obtained in a previous call to ``DescribeTapes`` . This marker indicates
          which page of results to retrieve.

          If not specified, the first page of results is retrieved.

        :type Limit: integer
        :param Limit:

          Specifies that the number of virtual tapes described be limited to the specified number.

          .. note::

            Amazon Web Services may impose its own limit, if this field is not set.

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
                'Marker': 'string'
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

            - **Marker** *(string) --*

              An opaque string which can be used as part of a subsequent DescribeTapes call to
              retrieve the next page of results.

              If a response does not contain a marker, then there are no more results to be
              retrieved.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_upload_buffer(self, GatewayARN: str) -> ClientDescribeUploadBufferResponseTypeDef:
        """
        Returns information about the upload buffer of a gateway. This operation is supported for
        the stored volume, cached volume and tape gateway types.

        The response includes disk IDs that are configured as upload buffer space, and it includes
        the amount of upload buffer space allocated and used.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/storagegateway-2013-06-30/DescribeUploadBuffer>`_

        **Request Syntax**
        ::

          response = client.describe_upload_buffer(
              GatewayARN='string'
          )
        :type GatewayARN: string
        :param GatewayARN: **[REQUIRED]**

          The Amazon Resource Name (ARN) of the gateway. Use the  ListGateways operation to return a
          list of gateways for your account and AWS Region.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'GatewayARN': 'string',
                'DiskIds': [
                    'string',
                ],
                'UploadBufferUsedInBytes': 123,
                'UploadBufferAllocatedInBytes': 123
            }
          **Response Structure**

          - *(dict) --*

            - **GatewayARN** *(string) --*

              The Amazon Resource Name (ARN) of the gateway. Use the  ListGateways operation to
              return a list of gateways for your account and AWS Region.

            - **DiskIds** *(list) --*

              An array of the gateway's local disk IDs that are configured as working storage. Each
              local disk ID is specified as a string (minimum length of 1 and maximum length of
              300). If no local disks are configured as working storage, then the DiskIds array is
              empty.

              - *(string) --*

            - **UploadBufferUsedInBytes** *(integer) --*

              The total number of bytes being used in the gateway's upload buffer.

            - **UploadBufferAllocatedInBytes** *(integer) --*

              The total number of bytes allocated in the gateway's as upload buffer.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_vtl_devices(
        self,
        GatewayARN: str,
        VTLDeviceARNs: List[str] = None,
        Marker: str = None,
        Limit: int = None,
    ) -> ClientDescribeVtlDevicesResponseTypeDef:
        """
        Returns a description of virtual tape library (VTL) devices for the specified tape gateway.
        In the response, AWS Storage Gateway returns VTL device information.

        This operation is only supported in the tape gateway type.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/storagegateway-2013-06-30/DescribeVTLDevices>`_

        **Request Syntax**
        ::

          response = client.describe_vtl_devices(
              GatewayARN='string',
              VTLDeviceARNs=[
                  'string',
              ],
              Marker='string',
              Limit=123
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

        :type Marker: string
        :param Marker:

          An opaque string that indicates the position at which to begin describing the VTL devices.

        :type Limit: integer
        :param Limit:

          Specifies that the number of VTL devices described be limited to the specified number.

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
                'Marker': 'string'
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

            - **Marker** *(string) --*

              An opaque string that indicates the position at which the VTL devices that were
              fetched for description ended. Use the marker in your next request to fetch the next
              set of VTL devices in the list. If there are no more VTL devices to describe, this
              field does not appear in the response.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_working_storage(
        self, GatewayARN: str
    ) -> ClientDescribeWorkingStorageResponseTypeDef:
        """
        Returns information about the working storage of a gateway. This operation is only supported
        in the stored volumes gateway type. This operation is deprecated in cached volumes API
        version (20120630). Use DescribeUploadBuffer instead.

        .. note::

          Working storage is also referred to as upload buffer. You can also use the
          DescribeUploadBuffer operation to add upload buffer to a stored volume gateway.

        The response includes disk IDs that are configured as working storage, and it includes the
        amount of working storage allocated and used.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/storagegateway-2013-06-30/DescribeWorkingStorage>`_

        **Request Syntax**
        ::

          response = client.describe_working_storage(
              GatewayARN='string'
          )
        :type GatewayARN: string
        :param GatewayARN: **[REQUIRED]**

          The Amazon Resource Name (ARN) of the gateway. Use the  ListGateways operation to return a
          list of gateways for your account and AWS Region.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'GatewayARN': 'string',
                'DiskIds': [
                    'string',
                ],
                'WorkingStorageUsedInBytes': 123,
                'WorkingStorageAllocatedInBytes': 123
            }
          **Response Structure**

          - *(dict) --*

            A JSON object containing the following fields:

            - **GatewayARN** *(string) --*

              The Amazon Resource Name (ARN) of the gateway. Use the  ListGateways operation to
              return a list of gateways for your account and AWS Region.

            - **DiskIds** *(list) --*

              An array of the gateway's local disk IDs that are configured as working storage. Each
              local disk ID is specified as a string (minimum length of 1 and maximum length of
              300). If no local disks are configured as working storage, then the DiskIds array is
              empty.

              - *(string) --*

            - **WorkingStorageUsedInBytes** *(integer) --*

              The total working storage in bytes in use by the gateway. If no working storage is
              configured for the gateway, this field returns 0.

            - **WorkingStorageAllocatedInBytes** *(integer) --*

              The total working storage in bytes allocated for the gateway. If no working storage is
              configured for the gateway, this field returns 0.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def detach_volume(
        self, VolumeARN: str, ForceDetach: bool = None
    ) -> ClientDetachVolumeResponseTypeDef:
        """
        Disconnects a volume from an iSCSI connection and then detaches the volume from the
        specified gateway. Detaching and attaching a volume enables you to recover your data from
        one gateway to a different gateway without creating a snapshot. It also makes it easier to
        move your volumes from an on-premises gateway to a gateway hosted on an Amazon EC2 instance.
        This operation is only supported in the volume gateway type.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/storagegateway-2013-06-30/DetachVolume>`_

        **Request Syntax**
        ::

          response = client.detach_volume(
              VolumeARN='string',
              ForceDetach=True|False
          )
        :type VolumeARN: string
        :param VolumeARN: **[REQUIRED]**

          The Amazon Resource Name (ARN) of the volume to detach from the gateway.

        :type ForceDetach: boolean
        :param ForceDetach:

          Set to ``true`` to forcibly remove the iSCSI connection of the target volume and detach
          the volume. The default is ``false`` . If this value is set to ``false`` , you must
          manually disconnect the iSCSI connection from the target volume.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'VolumeARN': 'string'
            }
          **Response Structure**

          - *(dict) --*

            AttachVolumeOutput

            - **VolumeARN** *(string) --*

              The Amazon Resource Name (ARN) of the volume that was detached.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def disable_gateway(self, GatewayARN: str) -> ClientDisableGatewayResponseTypeDef:
        """
        Disables a tape gateway when the gateway is no longer functioning. For example, if your
        gateway VM is damaged, you can disable the gateway so you can recover virtual tapes.

        Use this operation for a tape gateway that is not reachable or not functioning. This
        operation is only supported in the tape gateway type.

        .. warning::

          Once a gateway is disabled it cannot be enabled.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/storagegateway-2013-06-30/DisableGateway>`_

        **Request Syntax**
        ::

          response = client.disable_gateway(
              GatewayARN='string'
          )
        :type GatewayARN: string
        :param GatewayARN: **[REQUIRED]**

          The Amazon Resource Name (ARN) of the gateway. Use the  ListGateways operation to return a
          list of gateways for your account and AWS Region.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'GatewayARN': 'string'
            }
          **Response Structure**

          - *(dict) --*

            DisableGatewayOutput

            - **GatewayARN** *(string) --*

              The unique Amazon Resource Name (ARN) of the disabled gateway.
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
    def join_domain(
        self,
        GatewayARN: str,
        DomainName: str,
        UserName: str,
        Password: str,
        OrganizationalUnit: str = None,
        DomainControllers: List[str] = None,
        TimeoutInSeconds: int = None,
    ) -> ClientJoinDomainResponseTypeDef:
        """
        Adds a file gateway to an Active Directory domain. This operation is only supported for file
        gateways that support the SMB file protocol.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/storagegateway-2013-06-30/JoinDomain>`_

        **Request Syntax**
        ::

          response = client.join_domain(
              GatewayARN='string',
              DomainName='string',
              OrganizationalUnit='string',
              DomainControllers=[
                  'string',
              ],
              TimeoutInSeconds=123,
              UserName='string',
              Password='string'
          )
        :type GatewayARN: string
        :param GatewayARN: **[REQUIRED]**

          The Amazon Resource Name (ARN) of the gateway. Use the ``ListGateways`` operation to
          return a list of gateways for your account and AWS Region.

        :type DomainName: string
        :param DomainName: **[REQUIRED]**

          The name of the domain that you want the gateway to join.

        :type OrganizationalUnit: string
        :param OrganizationalUnit:

          The organizational unit (OU) is a container in an Active Directory that can hold users,
          groups, computers, and other OUs and this parameter specifies the OU that the gateway will
          join within the AD domain.

        :type DomainControllers: list
        :param DomainControllers:

          List of IPv4 addresses, NetBIOS names, or host names of your domain server. If you need to
          specify the port number include it after the colon (“:”). For example,
          ``mydc.mydomain.com:389`` .

          - *(string) --*

        :type TimeoutInSeconds: integer
        :param TimeoutInSeconds:

          Specifies the time in seconds, in which the ``JoinDomain`` operation must complete. The
          default is 20 seconds.

        :type UserName: string
        :param UserName: **[REQUIRED]**

          Sets the user name of user who has permission to add the gateway to the Active Directory
          domain. The domain user account should be enabled to join computers to the domain. For
          example, you can use the domain administrator account or an account with delegated
          permissions to join computers to the domain.

        :type Password: string
        :param Password: **[REQUIRED]**

          Sets the password of the user who has permission to add the gateway to the Active
          Directory domain.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'GatewayARN': 'string',
                'ActiveDirectoryStatus':
                'ACCESS_DENIED'|'DETACHED'|'JOINED'|'JOINING'|'NETWORK_ERROR'|'TIMEOUT'
                |'UNKNOWN_ERROR'
            }
          **Response Structure**

          - *(dict) --*

            JoinDomainOutput

            - **GatewayARN** *(string) --*

              The unique Amazon Resource Name (ARN) of the gateway that joined the domain.

            - **ActiveDirectoryStatus** *(string) --*

              Indicates the status of the gateway as a member of the Active Directory domain.

              * ACCESS_DENIED: Indicates that the ``JoinDomain`` operation failed due to an
              authentication error.

              * DETACHED: Indicates that gateway is not joined to a domain.

              * JOINED: Indicates that the gateway has successfully joined a domain.

              * JOINING: Indicates that a ``JoinDomain`` operation is in progress.

              * NETWORK_ERROR: Indicates that ``JoinDomain`` operation failed due to a network or
              connectivity error.

              * TIMEOUT: Indicates that the ``JoinDomain`` operation failed because the operation
              didn't complete within the allotted time.

              * UNKNOWN_ERROR: Indicates that the ``JoinDomain`` operation failed due to another
              type of error.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_file_shares(
        self, GatewayARN: str = None, Limit: int = None, Marker: str = None
    ) -> ClientListFileSharesResponseTypeDef:
        """
        Gets a list of the file shares for a specific file gateway, or the list of file shares that
        belong to the calling user account. This operation is only supported for file gateways.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/storagegateway-2013-06-30/ListFileShares>`_

        **Request Syntax**
        ::

          response = client.list_file_shares(
              GatewayARN='string',
              Limit=123,
              Marker='string'
          )
        :type GatewayARN: string
        :param GatewayARN:

          The Amazon resource Name (ARN) of the gateway whose file shares you want to list. If this
          field is not present, all file shares under your account are listed.

        :type Limit: integer
        :param Limit:

          The maximum number of file shares to return in the response. The value must be an integer
          with a value greater than zero. Optional.

        :type Marker: string
        :param Marker:

          Opaque pagination token returned from a previous ListFileShares operation. If present,
          ``Marker`` specifies where to continue the list from after a previous call to
          ListFileShares. Optional.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Marker': 'string',
                'NextMarker': 'string',
                'FileShareInfoList': [
                    {
                        'FileShareType': 'NFS'|'SMB',
                        'FileShareARN': 'string',
                        'FileShareId': 'string',
                        'FileShareStatus': 'string',
                        'GatewayARN': 'string'
                    },
                ]
            }
          **Response Structure**

          - *(dict) --*

            ListFileShareOutput

            - **Marker** *(string) --*

              If the request includes ``Marker`` , the response returns that value in this field.

            - **NextMarker** *(string) --*

              If a value is present, there are more file shares to return. In a subsequent request,
              use ``NextMarker`` as the value for ``Marker`` to retrieve the next set of file
              shares.

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
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_gateways(
        self, Marker: str = None, Limit: int = None
    ) -> ClientListGatewaysResponseTypeDef:
        """
        Lists gateways owned by an AWS account in an AWS Region specified in the request. The
        returned list is ordered by gateway Amazon Resource Name (ARN).

        By default, the operation returns a maximum of 100 gateways. This operation supports
        pagination that allows you to optionally reduce the number of gateways returned in a
        response.

        If you have more gateways than are returned in a response (that is, the response returns
        only a truncated list of your gateways), the response contains a marker that you can specify
        in your next request to fetch the next page of gateways.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/storagegateway-2013-06-30/ListGateways>`_

        **Request Syntax**
        ::

          response = client.list_gateways(
              Marker='string',
              Limit=123
          )
        :type Marker: string
        :param Marker:

          An opaque string that indicates the position at which to begin the returned list of
          gateways.

        :type Limit: integer
        :param Limit:

          Specifies that the list of gateways returned be limited to the specified number of items.

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
                'Marker': 'string'
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

            - **Marker** *(string) --*

              Use the marker in your next request to fetch the next set of gateways in the list. If
              there are no more gateways to list, this field does not appear in the response.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_local_disks(self, GatewayARN: str) -> ClientListLocalDisksResponseTypeDef:
        """
        Returns a list of the gateway's local disks. To specify which gateway to describe, you use
        the Amazon Resource Name (ARN) of the gateway in the body of the request.

        The request returns a list of all disks, specifying which are configured as working storage,
        cache storage, or stored volume or not configured at all. The response includes a
        ``DiskStatus`` field. This field can have a value of present (the disk is available to use),
        missing (the disk is no longer connected to the gateway), or mismatch (the disk node is
        occupied by a disk that has incorrect metadata or the disk content is corrupted).

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/storagegateway-2013-06-30/ListLocalDisks>`_

        **Request Syntax**
        ::

          response = client.list_local_disks(
              GatewayARN='string'
          )
        :type GatewayARN: string
        :param GatewayARN: **[REQUIRED]**

          The Amazon Resource Name (ARN) of the gateway. Use the  ListGateways operation to return a
          list of gateways for your account and AWS Region.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'GatewayARN': 'string',
                'Disks': [
                    {
                        'DiskId': 'string',
                        'DiskPath': 'string',
                        'DiskNode': 'string',
                        'DiskStatus': 'string',
                        'DiskSizeInBytes': 123,
                        'DiskAllocationType': 'string',
                        'DiskAllocationResource': 'string',
                        'DiskAttributeList': [
                            'string',
                        ]
                    },
                ]
            }
          **Response Structure**

          - *(dict) --*

            - **GatewayARN** *(string) --*

              The Amazon Resource Name (ARN) of the gateway. Use the  ListGateways operation to
              return a list of gateways for your account and AWS Region.

            - **Disks** *(list) --*

              A JSON object containing the following fields:

              *  ListLocalDisksOutput$Disks

              - *(dict) --*

                Represents a gateway's local disk.

                - **DiskId** *(string) --*

                  The unique device ID or other distinguishing data that identifies a local disk.

                - **DiskPath** *(string) --*

                  The path of a local disk in the gateway virtual machine (VM).

                - **DiskNode** *(string) --*

                  The device node of a local disk as assigned by the virtualization environment.

                - **DiskStatus** *(string) --*

                  A value that represents the status of a local disk.

                - **DiskSizeInBytes** *(integer) --*

                  The local disk size in bytes.

                - **DiskAllocationType** *(string) --*

                  One of the ``DiskAllocationType`` enumeration values that identifies how a local
                  disk is used. Valid values: ``UPLOAD_BUFFER`` , ``CACHE_STORAGE``

                - **DiskAllocationResource** *(string) --*

                  The iSCSI qualified name (IQN) that is defined for a disk. This field is not
                  included in the response if the local disk is not defined as an iSCSI target. The
                  format of this field is *targetIqn::LUNNumber::region-volumeId* .

                - **DiskAttributeList** *(list) --*

                  A list of values that represents attributes of a local disk.

                  - *(string) --*
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_tags_for_resource(
        self, ResourceARN: str, Marker: str = None, Limit: int = None
    ) -> ClientListTagsForResourceResponseTypeDef:
        """
        Lists the tags that have been added to the specified resource. This operation is supported
        in storage gateways of all types.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/storagegateway-2013-06-30/ListTagsForResource>`_

        **Request Syntax**
        ::

          response = client.list_tags_for_resource(
              ResourceARN='string',
              Marker='string',
              Limit=123
          )
        :type ResourceARN: string
        :param ResourceARN: **[REQUIRED]**

          The Amazon Resource Name (ARN) of the resource for which you want to list tags.

        :type Marker: string
        :param Marker:

          An opaque string that indicates the position at which to begin returning the list of tags.

        :type Limit: integer
        :param Limit:

          Specifies that the list of tags returned be limited to the specified number of items.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'ResourceARN': 'string',
                'Marker': 'string',
                'Tags': [
                    {
                        'Key': 'string',
                        'Value': 'string'
                    },
                ]
            }
          **Response Structure**

          - *(dict) --*

            ListTagsForResourceOutput

            - **ResourceARN** *(string) --*

              he Amazon Resource Name (ARN) of the resource for which you want to list tags.

            - **Marker** *(string) --*

              An opaque string that indicates the position at which to stop returning the list of
              tags.

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
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_tapes(
        self, TapeARNs: List[str] = None, Marker: str = None, Limit: int = None
    ) -> ClientListTapesResponseTypeDef:
        """
        Lists virtual tapes in your virtual tape library (VTL) and your virtual tape shelf (VTS).
        You specify the tapes to list by specifying one or more tape Amazon Resource Names (ARNs).
        If you don't specify a tape ARN, the operation lists all virtual tapes in both your VTL and
        VTS.

        This operation supports pagination. By default, the operation returns a maximum of up to 100
        tapes. You can optionally specify the ``Limit`` parameter in the body to limit the number of
        tapes in the response. If the number of tapes returned in the response is truncated, the
        response includes a ``Marker`` element that you can use in your subsequent request to
        retrieve the next set of tapes. This operation is only supported in the tape gateway type.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/storagegateway-2013-06-30/ListTapes>`_

        **Request Syntax**
        ::

          response = client.list_tapes(
              TapeARNs=[
                  'string',
              ],
              Marker='string',
              Limit=123
          )
        :type TapeARNs: list
        :param TapeARNs:

          The Amazon Resource Name (ARN) of each of the tapes you want to list. If you don't specify
          a tape ARN, the response lists all tapes in both your VTL and VTS.

          - *(string) --*

        :type Marker: string
        :param Marker:

          A string that indicates the position at which to begin the returned list of tapes.

        :type Limit: integer
        :param Limit:

          An optional number limit for the tapes in the list returned by this call.

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
                'Marker': 'string'
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

            - **Marker** *(string) --*

              A string that indicates the position at which to begin returning the next list of
              tapes. Use the marker in your next request to continue pagination of tapes. If there
              are no more tapes to list, this element does not appear in the response body.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_volume_initiators(self, VolumeARN: str) -> ClientListVolumeInitiatorsResponseTypeDef:
        """
        Lists iSCSI initiators that are connected to a volume. You can use this operation to
        determine whether a volume is being used or not. This operation is only supported in the
        cached volume and stored volume gateway types.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/storagegateway-2013-06-30/ListVolumeInitiators>`_

        **Request Syntax**
        ::

          response = client.list_volume_initiators(
              VolumeARN='string'
          )
        :type VolumeARN: string
        :param VolumeARN: **[REQUIRED]**

          The Amazon Resource Name (ARN) of the volume. Use the  ListVolumes operation to return a
          list of gateway volumes for the gateway.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Initiators': [
                    'string',
                ]
            }
          **Response Structure**

          - *(dict) --*

            ListVolumeInitiatorsOutput

            - **Initiators** *(list) --*

              The host names and port numbers of all iSCSI initiators that are connected to the
              gateway.

              - *(string) --*
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_volume_recovery_points(
        self, GatewayARN: str
    ) -> ClientListVolumeRecoveryPointsResponseTypeDef:
        """
        Lists the recovery points for a specified gateway. This operation is only supported in the
        cached volume gateway type.

        Each cache volume has one recovery point. A volume recovery point is a point in time at
        which all data of the volume is consistent and from which you can create a snapshot or clone
        a new cached volume from a source volume. To create a snapshot from a volume recovery point
        use the  CreateSnapshotFromVolumeRecoveryPoint operation.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/storagegateway-2013-06-30/ListVolumeRecoveryPoints>`_

        **Request Syntax**
        ::

          response = client.list_volume_recovery_points(
              GatewayARN='string'
          )
        :type GatewayARN: string
        :param GatewayARN: **[REQUIRED]**

          The Amazon Resource Name (ARN) of the gateway. Use the  ListGateways operation to return a
          list of gateways for your account and AWS Region.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'GatewayARN': 'string',
                'VolumeRecoveryPointInfos': [
                    {
                        'VolumeARN': 'string',
                        'VolumeSizeInBytes': 123,
                        'VolumeUsageInBytes': 123,
                        'VolumeRecoveryPointTime': 'string'
                    },
                ]
            }
          **Response Structure**

          - *(dict) --*

            - **GatewayARN** *(string) --*

              The Amazon Resource Name (ARN) of the gateway. Use the  ListGateways operation to
              return a list of gateways for your account and AWS Region.

            - **VolumeRecoveryPointInfos** *(list) --*

              An array of  VolumeRecoveryPointInfo objects.

              - *(dict) --*

                Describes a storage volume recovery point object.

                - **VolumeARN** *(string) --*

                  The Amazon Resource Name (ARN) of the volume target.

                - **VolumeSizeInBytes** *(integer) --*

                  The size of the volume in bytes.

                - **VolumeUsageInBytes** *(integer) --*

                  The size of the data stored on the volume in bytes.

                  .. note::

                    This value is not available for volumes created prior to May 13, 2015, until you
                    store data on the volume.

                - **VolumeRecoveryPointTime** *(string) --*

                  The time the recovery point was taken.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_volumes(
        self, GatewayARN: str = None, Marker: str = None, Limit: int = None
    ) -> ClientListVolumesResponseTypeDef:
        """
        Lists the iSCSI stored volumes of a gateway. Results are sorted by volume ARN. The response
        includes only the volume ARNs. If you want additional volume information, use the
        DescribeStorediSCSIVolumes or the  DescribeCachediSCSIVolumes API.

        The operation supports pagination. By default, the operation returns a maximum of up to 100
        volumes. You can optionally specify the ``Limit`` field in the body to limit the number of
        volumes in the response. If the number of volumes returned in the response is truncated, the
        response includes a Marker field. You can use this Marker value in your subsequent request
        to retrieve the next set of volumes. This operation is only supported in the cached volume
        and stored volume gateway types.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/storagegateway-2013-06-30/ListVolumes>`_

        **Request Syntax**
        ::

          response = client.list_volumes(
              GatewayARN='string',
              Marker='string',
              Limit=123
          )
        :type GatewayARN: string
        :param GatewayARN:

          The Amazon Resource Name (ARN) of the gateway. Use the  ListGateways operation to return a
          list of gateways for your account and AWS Region.

        :type Marker: string
        :param Marker:

          A string that indicates the position at which to begin the returned list of volumes.
          Obtain the marker from the response of a previous List iSCSI Volumes request.

        :type Limit: integer
        :param Limit:

          Specifies that the list of volumes returned be limited to the specified number of items.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'GatewayARN': 'string',
                'Marker': 'string',
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
                ]
            }
          **Response Structure**

          - *(dict) --*

            A JSON object containing the following fields:

            *  ListVolumesOutput$Marker

            *  ListVolumesOutput$VolumeInfos

            - **GatewayARN** *(string) --*

              The Amazon Resource Name (ARN) of the gateway. Use the  ListGateways operation to
              return a list of gateways for your account and AWS Region.

            - **Marker** *(string) --*

              Use the marker in your next request to continue pagination of iSCSI volumes. If there
              are no more volumes to list, this field does not appear in the response body.

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
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def notify_when_uploaded(self, FileShareARN: str) -> ClientNotifyWhenUploadedResponseTypeDef:
        """
        Sends you notification through CloudWatch Events when all files written to your file share
        have been uploaded to Amazon S3.

        AWS Storage Gateway can send a notification through Amazon CloudWatch Events when all files
        written to your file share up to that point in time have been uploaded to Amazon S3. These
        files include files written to the file share up to the time that you make a request for
        notification. When the upload is done, Storage Gateway sends you notification through an
        Amazon CloudWatch Event. You can configure CloudWatch Events to send the notification
        through event targets such as Amazon SNS or AWS Lambda function. This operation is only
        supported for file gateways.

        For more information, see Getting File Upload Notification in the Storage Gateway User Guide
        (https://docs.aws.amazon.com/storagegateway/latest/userguide/monitoring-file-gateway.html#get-upload-notification).

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/storagegateway-2013-06-30/NotifyWhenUploaded>`_

        **Request Syntax**
        ::

          response = client.notify_when_uploaded(
              FileShareARN='string'
          )
        :type FileShareARN: string
        :param FileShareARN: **[REQUIRED]**

          The Amazon Resource Name (ARN) of the file share.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'FileShareARN': 'string',
                'NotificationId': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **FileShareARN** *(string) --*

              The Amazon Resource Name (ARN) of the file share.

            - **NotificationId** *(string) --*

              The randomly generated ID of the notification that was sent. This ID is in UUID
              format.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def refresh_cache(
        self, FileShareARN: str, FolderList: List[str] = None, Recursive: bool = None
    ) -> ClientRefreshCacheResponseTypeDef:
        """
        Refreshes the cache for the specified file share. This operation finds objects in the Amazon
        S3 bucket that were added, removed or replaced since the gateway last listed the bucket's
        contents and cached the results. This operation is only supported in the file gateway type.
        You can subscribe to be notified through an Amazon CloudWatch event when your RefreshCache
        operation completes. For more information, see `Getting Notified About File Operations
        <https://docs.aws.amazon.com/storagegateway/latest/userguide/monitoring-file-gateway.html#get-notification>`__
        .

        When this API is called, it only initiates the refresh operation. When the API call
        completes and returns a success code, it doesn't necessarily mean that the file refresh has
        completed. You should use the refresh-complete notification to determine that the operation
        has completed before you check for new files on the gateway file share. You can subscribe to
        be notified through an CloudWatch event when your ``RefreshCache`` operation completes.

        Throttle limit: This API is asynchronous so the gateway will accept no more than two
        refreshes at any time. We recommend using the refresh-complete CloudWatch event notification
        before issuing additional requests. For more information, see `Getting Notified About File
        Operations
        <https://docs.aws.amazon.com/storagegateway/latest/userguide/monitoring-file-gateway.html#get-notification>`__
        .

        If you invoke the RefreshCache API when two requests are already being processed, any new
        request will cause an ``InvalidGatewayRequestException`` error because too many requests
        were sent to the server.

        For more information, see
        "https://docs.aws.amazon.com/storagegateway/latest/userguide/monitoring-file-gateway.html#get-notification".

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/storagegateway-2013-06-30/RefreshCache>`_

        **Request Syntax**
        ::

          response = client.refresh_cache(
              FileShareARN='string',
              FolderList=[
                  'string',
              ],
              Recursive=True|False
          )
        :type FileShareARN: string
        :param FileShareARN: **[REQUIRED]**

          The Amazon Resource Name (ARN) of the file share you want to refresh.

        :type FolderList: list
        :param FolderList:

          A comma-separated list of the paths of folders to refresh in the cache. The default is
          [``"/"`` ]. The default refreshes objects and folders at the root of the Amazon S3 bucket.
          If ``Recursive`` is set to "true", the entire S3 bucket that the file share has access to
          is refreshed.

          - *(string) --*

        :type Recursive: boolean
        :param Recursive:

          A value that specifies whether to recursively refresh folders in the cache. The refresh
          includes folders that were in the cache the last time the gateway listed the folder's
          contents. If this value set to "true", each folder that is listed in ``FolderList`` is
          recursively updated. Otherwise, subfolders listed in ``FolderList`` are not refreshed.
          Only objects that are in folders listed directly under ``FolderList`` are found and used
          for the update. The default is "true".

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'FileShareARN': 'string',
                'NotificationId': 'string'
            }
          **Response Structure**

          - *(dict) --*

            RefreshCacheOutput

            - **FileShareARN** *(string) --*

              The Amazon Resource Name (ARN) of the file share.

            - **NotificationId** *(string) --*

              The randomly generated ID of the notification that was sent. This ID is in UUID
              format.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def remove_tags_from_resource(
        self, ResourceARN: str, TagKeys: List[str]
    ) -> ClientRemoveTagsFromResourceResponseTypeDef:
        """
        Removes one or more tags from the specified resource. This operation is supported in storage
        gateways of all types.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/storagegateway-2013-06-30/RemoveTagsFromResource>`_

        **Request Syntax**
        ::

          response = client.remove_tags_from_resource(
              ResourceARN='string',
              TagKeys=[
                  'string',
              ]
          )
        :type ResourceARN: string
        :param ResourceARN: **[REQUIRED]**

          The Amazon Resource Name (ARN) of the resource you want to remove the tags from.

        :type TagKeys: list
        :param TagKeys: **[REQUIRED]**

          The keys of the tags you want to remove from the specified resource. A tag is composed of
          a key/value pair.

          - *(string) --*

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'ResourceARN': 'string'
            }
          **Response Structure**

          - *(dict) --*

            RemoveTagsFromResourceOutput

            - **ResourceARN** *(string) --*

              The Amazon Resource Name (ARN) of the resource that the tags were removed from.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def reset_cache(self, GatewayARN: str) -> ClientResetCacheResponseTypeDef:
        """
        Resets all cache disks that have encountered a error and makes the disks available for
        reconfiguration as cache storage. If your cache disk encounters a error, the gateway
        prevents read and write operations on virtual tapes in the gateway. For example, an error
        can occur when a disk is corrupted or removed from the gateway. When a cache is reset, the
        gateway loses its cache storage. At this point you can reconfigure the disks as cache disks.
        This operation is only supported in the cached volume and tape types.

        .. warning::

          If the cache disk you are resetting contains data that has not been uploaded to Amazon S3
          yet, that data can be lost. After you reset cache disks, there will be no configured cache
          disks left in the gateway, so you must configure at least one new cache disk for your
          gateway to function properly.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/storagegateway-2013-06-30/ResetCache>`_

        **Request Syntax**
        ::

          response = client.reset_cache(
              GatewayARN='string'
          )
        :type GatewayARN: string
        :param GatewayARN: **[REQUIRED]**

          The Amazon Resource Name (ARN) of the gateway. Use the  ListGateways operation to return a
          list of gateways for your account and AWS Region.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'GatewayARN': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **GatewayARN** *(string) --*

              The Amazon Resource Name (ARN) of the gateway. Use the  ListGateways operation to
              return a list of gateways for your account and AWS Region.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def retrieve_tape_archive(
        self, TapeARN: str, GatewayARN: str
    ) -> ClientRetrieveTapeArchiveResponseTypeDef:
        """
        Retrieves an archived virtual tape from the virtual tape shelf (VTS) to a tape gateway.
        Virtual tapes archived in the VTS are not associated with any gateway. However after a tape
        is retrieved, it is associated with a gateway, even though it is also listed in the VTS,
        that is, archive. This operation is only supported in the tape gateway type.

        Once a tape is successfully retrieved to a gateway, it cannot be retrieved again to another
        gateway. You must archive the tape again before you can retrieve it to another gateway. This
        operation is only supported in the tape gateway type.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/storagegateway-2013-06-30/RetrieveTapeArchive>`_

        **Request Syntax**
        ::

          response = client.retrieve_tape_archive(
              TapeARN='string',
              GatewayARN='string'
          )
        :type TapeARN: string
        :param TapeARN: **[REQUIRED]**

          The Amazon Resource Name (ARN) of the virtual tape you want to retrieve from the virtual
          tape shelf (VTS).

        :type GatewayARN: string
        :param GatewayARN: **[REQUIRED]**

          The Amazon Resource Name (ARN) of the gateway you want to retrieve the virtual tape to.
          Use the  ListGateways operation to return a list of gateways for your account and AWS
          Region.

          You retrieve archived virtual tapes to only one gateway and the gateway must be a tape
          gateway.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'TapeARN': 'string'
            }
          **Response Structure**

          - *(dict) --*

            RetrieveTapeArchiveOutput

            - **TapeARN** *(string) --*

              The Amazon Resource Name (ARN) of the retrieved virtual tape.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def retrieve_tape_recovery_point(
        self, TapeARN: str, GatewayARN: str
    ) -> ClientRetrieveTapeRecoveryPointResponseTypeDef:
        """
        Retrieves the recovery point for the specified virtual tape. This operation is only
        supported in the tape gateway type.

        A recovery point is a point in time view of a virtual tape at which all the data on the tape
        is consistent. If your gateway crashes, virtual tapes that have recovery points can be
        recovered to a new gateway.

        .. note::

          The virtual tape can be retrieved to only one gateway. The retrieved tape is read-only.
          The virtual tape can be retrieved to only a tape gateway. There is no charge for
          retrieving recovery points.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/storagegateway-2013-06-30/RetrieveTapeRecoveryPoint>`_

        **Request Syntax**
        ::

          response = client.retrieve_tape_recovery_point(
              TapeARN='string',
              GatewayARN='string'
          )
        :type TapeARN: string
        :param TapeARN: **[REQUIRED]**

          The Amazon Resource Name (ARN) of the virtual tape for which you want to retrieve the
          recovery point.

        :type GatewayARN: string
        :param GatewayARN: **[REQUIRED]**

          The Amazon Resource Name (ARN) of the gateway. Use the  ListGateways operation to return a
          list of gateways for your account and AWS Region.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'TapeARN': 'string'
            }
          **Response Structure**

          - *(dict) --*

            RetrieveTapeRecoveryPointOutput

            - **TapeARN** *(string) --*

              The Amazon Resource Name (ARN) of the virtual tape for which the recovery point was
              retrieved.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def set_local_console_password(
        self, GatewayARN: str, LocalConsolePassword: str
    ) -> ClientSetLocalConsolePasswordResponseTypeDef:
        """
        Sets the password for your VM local console. When you log in to the local console for the
        first time, you log in to the VM with the default credentials. We recommend that you set a
        new password. You don't need to know the default password to set a new password.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/storagegateway-2013-06-30/SetLocalConsolePassword>`_

        **Request Syntax**
        ::

          response = client.set_local_console_password(
              GatewayARN='string',
              LocalConsolePassword='string'
          )
        :type GatewayARN: string
        :param GatewayARN: **[REQUIRED]**

          The Amazon Resource Name (ARN) of the gateway. Use the  ListGateways operation to return a
          list of gateways for your account and AWS Region.

        :type LocalConsolePassword: string
        :param LocalConsolePassword: **[REQUIRED]**

          The password you want to set for your VM local console.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'GatewayARN': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **GatewayARN** *(string) --*

              The Amazon Resource Name (ARN) of the gateway. Use the  ListGateways operation to
              return a list of gateways for your account and AWS Region.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def set_smb_guest_password(
        self, GatewayARN: str, Password: str
    ) -> ClientSetSmbGuestPasswordResponseTypeDef:
        """
        Sets the password for the guest user ``smbguest`` . The ``smbguest`` user is the user when
        the authentication method for the file share is set to ``GuestAccess`` .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/storagegateway-2013-06-30/SetSMBGuestPassword>`_

        **Request Syntax**
        ::

          response = client.set_smb_guest_password(
              GatewayARN='string',
              Password='string'
          )
        :type GatewayARN: string
        :param GatewayARN: **[REQUIRED]**

          The Amazon Resource Name (ARN) of the file gateway the SMB file share is associated with.

        :type Password: string
        :param Password: **[REQUIRED]**

          The password that you want to set for your SMB Server.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'GatewayARN': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **GatewayARN** *(string) --*

              The Amazon Resource Name (ARN) of the gateway. Use the  ListGateways operation to
              return a list of gateways for your account and AWS Region.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def shutdown_gateway(self, GatewayARN: str) -> ClientShutdownGatewayResponseTypeDef:
        """
        Shuts down a gateway. To specify which gateway to shut down, use the Amazon Resource Name
        (ARN) of the gateway in the body of your request.

        The operation shuts down the gateway service component running in the gateway's virtual
        machine (VM) and not the host VM.

        .. note::

          If you want to shut down the VM, it is recommended that you first shut down the gateway
          component in the VM to avoid unpredictable conditions.

        After the gateway is shutdown, you cannot call any other API except  StartGateway ,
        DescribeGatewayInformation , and  ListGateways . For more information, see  ActivateGateway
        . Your applications cannot read from or write to the gateway's storage volumes, and there
        are no snapshots taken.

        .. note::

          When you make a shutdown request, you will get a ``200 OK`` success response immediately.
          However, it might take some time for the gateway to shut down. You can call the
          DescribeGatewayInformation API to check the status. For more information, see
          ActivateGateway .

        If do not intend to use the gateway again, you must delete the gateway (using  DeleteGateway
        ) to no longer pay software charges associated with the gateway.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/storagegateway-2013-06-30/ShutdownGateway>`_

        **Request Syntax**
        ::

          response = client.shutdown_gateway(
              GatewayARN='string'
          )
        :type GatewayARN: string
        :param GatewayARN: **[REQUIRED]**

          The Amazon Resource Name (ARN) of the gateway. Use the  ListGateways operation to return a
          list of gateways for your account and AWS Region.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'GatewayARN': 'string'
            }
          **Response Structure**

          - *(dict) --*

            A JSON object containing the of the gateway that was shut down.

            - **GatewayARN** *(string) --*

              The Amazon Resource Name (ARN) of the gateway. Use the  ListGateways operation to
              return a list of gateways for your account and AWS Region.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def start_availability_monitor_test(
        self, GatewayARN: str
    ) -> ClientStartAvailabilityMonitorTestResponseTypeDef:
        """
        Start a test that verifies that the specified gateway is configured for High Availability
        monitoring in your host environment. This request only initiates the test and that a
        successful response only indicates that the test was started. It doesn't indicate that the
        test passed. For the status of the test, invoke the ``DescribeAvailabilityMonitorTest`` API.

        .. note::

          Starting this test will cause your gateway to go offline for a brief period.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/storagegateway-2013-06-30/StartAvailabilityMonitorTest>`_

        **Request Syntax**
        ::

          response = client.start_availability_monitor_test(
              GatewayARN='string'
          )
        :type GatewayARN: string
        :param GatewayARN: **[REQUIRED]**

          The Amazon Resource Name (ARN) of the gateway. Use the  ListGateways operation to return a
          list of gateways for your account and AWS Region.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'GatewayARN': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **GatewayARN** *(string) --*

              The Amazon Resource Name (ARN) of the gateway. Use the  ListGateways operation to
              return a list of gateways for your account and AWS Region.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def start_gateway(self, GatewayARN: str) -> ClientStartGatewayResponseTypeDef:
        """
        Starts a gateway that you previously shut down (see  ShutdownGateway ). After the gateway
        starts, you can then make other API calls, your applications can read from or write to the
        gateway's storage volumes and you will be able to take snapshot backups.

        .. note::

          When you make a request, you will get a 200 OK success response immediately. However, it
          might take some time for the gateway to be ready. You should call
          DescribeGatewayInformation and check the status before making any additional API calls.
          For more information, see  ActivateGateway .

        To specify which gateway to start, use the Amazon Resource Name (ARN) of the gateway in your
        request.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/storagegateway-2013-06-30/StartGateway>`_

        **Request Syntax**
        ::

          response = client.start_gateway(
              GatewayARN='string'
          )
        :type GatewayARN: string
        :param GatewayARN: **[REQUIRED]**

          The Amazon Resource Name (ARN) of the gateway. Use the  ListGateways operation to return a
          list of gateways for your account and AWS Region.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'GatewayARN': 'string'
            }
          **Response Structure**

          - *(dict) --*

            A JSON object containing the of the gateway that was restarted.

            - **GatewayARN** *(string) --*

              The Amazon Resource Name (ARN) of the gateway. Use the  ListGateways operation to
              return a list of gateways for your account and AWS Region.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_bandwidth_rate_limit(
        self,
        GatewayARN: str,
        AverageUploadRateLimitInBitsPerSec: int = None,
        AverageDownloadRateLimitInBitsPerSec: int = None,
    ) -> ClientUpdateBandwidthRateLimitResponseTypeDef:
        """
        Updates the bandwidth rate limits of a gateway. You can update both the upload and download
        bandwidth rate limit or specify only one of the two. If you don't set a bandwidth rate
        limit, the existing rate limit remains. This operation is supported for the stored volume,
        cached volume and tape gateway types.'

        By default, a gateway's bandwidth rate limits are not set. If you don't set any limit, the
        gateway does not have any limitations on its bandwidth usage and could potentially use the
        maximum available bandwidth.

        To specify which gateway to update, use the Amazon Resource Name (ARN) of the gateway in
        your request.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/storagegateway-2013-06-30/UpdateBandwidthRateLimit>`_

        **Request Syntax**
        ::

          response = client.update_bandwidth_rate_limit(
              GatewayARN='string',
              AverageUploadRateLimitInBitsPerSec=123,
              AverageDownloadRateLimitInBitsPerSec=123
          )
        :type GatewayARN: string
        :param GatewayARN: **[REQUIRED]**

          The Amazon Resource Name (ARN) of the gateway. Use the  ListGateways operation to return a
          list of gateways for your account and AWS Region.

        :type AverageUploadRateLimitInBitsPerSec: integer
        :param AverageUploadRateLimitInBitsPerSec:

          The average upload bandwidth rate limit in bits per second.

        :type AverageDownloadRateLimitInBitsPerSec: integer
        :param AverageDownloadRateLimitInBitsPerSec:

          The average download bandwidth rate limit in bits per second.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'GatewayARN': 'string'
            }
          **Response Structure**

          - *(dict) --*

            A JSON object containing the of the gateway whose throttle information was updated.

            - **GatewayARN** *(string) --*

              The Amazon Resource Name (ARN) of the gateway. Use the  ListGateways operation to
              return a list of gateways for your account and AWS Region.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_chap_credentials(
        self,
        TargetARN: str,
        SecretToAuthenticateInitiator: str,
        InitiatorName: str,
        SecretToAuthenticateTarget: str = None,
    ) -> ClientUpdateChapCredentialsResponseTypeDef:
        """
        Updates the Challenge-Handshake Authentication Protocol (CHAP) credentials for a specified
        iSCSI target. By default, a gateway does not have CHAP enabled; however, for added security,
        you might use it. This operation is supported in the volume and tape gateway types.

        .. warning::

          When you update CHAP credentials, all existing connections on the target are closed and
          initiators must reconnect with the new credentials.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/storagegateway-2013-06-30/UpdateChapCredentials>`_

        **Request Syntax**
        ::

          response = client.update_chap_credentials(
              TargetARN='string',
              SecretToAuthenticateInitiator='string',
              InitiatorName='string',
              SecretToAuthenticateTarget='string'
          )
        :type TargetARN: string
        :param TargetARN: **[REQUIRED]**

          The Amazon Resource Name (ARN) of the iSCSI volume target. Use the
          DescribeStorediSCSIVolumes operation to return the TargetARN for specified VolumeARN.

        :type SecretToAuthenticateInitiator: string
        :param SecretToAuthenticateInitiator: **[REQUIRED]**

          The secret key that the initiator (for example, the Windows client) must provide to
          participate in mutual CHAP with the target.

          .. note::

            The secret key must be between 12 and 16 bytes when encoded in UTF-8.

        :type InitiatorName: string
        :param InitiatorName: **[REQUIRED]**

          The iSCSI initiator that connects to the target.

        :type SecretToAuthenticateTarget: string
        :param SecretToAuthenticateTarget:

          The secret key that the target must provide to participate in mutual CHAP with the
          initiator (e.g. Windows client).

          Byte constraints: Minimum bytes of 12. Maximum bytes of 16.

          .. note::

            The secret key must be between 12 and 16 bytes when encoded in UTF-8.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'TargetARN': 'string',
                'InitiatorName': 'string'
            }
          **Response Structure**

          - *(dict) --*

            A JSON object containing the following fields:

            - **TargetARN** *(string) --*

              The Amazon Resource Name (ARN) of the target. This is the same target specified in the
              request.

            - **InitiatorName** *(string) --*

              The iSCSI initiator that connects to the target. This is the same initiator name
              specified in the request.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_gateway_information(
        self,
        GatewayARN: str,
        GatewayName: str = None,
        GatewayTimezone: str = None,
        CloudWatchLogGroupARN: str = None,
    ) -> ClientUpdateGatewayInformationResponseTypeDef:
        """
        Updates a gateway's metadata, which includes the gateway's name and time zone. To specify
        which gateway to update, use the Amazon Resource Name (ARN) of the gateway in your request.

        .. note::

          For Gateways activated after September 2, 2015, the gateway's ARN contains the gateway ID
          rather than the gateway name. However, changing the name of the gateway has no effect on
          the gateway's ARN.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/storagegateway-2013-06-30/UpdateGatewayInformation>`_

        **Request Syntax**
        ::

          response = client.update_gateway_information(
              GatewayARN='string',
              GatewayName='string',
              GatewayTimezone='string',
              CloudWatchLogGroupARN='string'
          )
        :type GatewayARN: string
        :param GatewayARN: **[REQUIRED]**

          The Amazon Resource Name (ARN) of the gateway. Use the  ListGateways operation to return a
          list of gateways for your account and AWS Region.

        :type GatewayName: string
        :param GatewayName:

          The name you configured for your gateway.

        :type GatewayTimezone: string
        :param GatewayTimezone:

          A value that indicates the time zone of the gateway.

        :type CloudWatchLogGroupARN: string
        :param CloudWatchLogGroupARN:

          The Amazon Resource Name (ARN) of the Amazon CloudWatch log group that you want to use to
          monitor and log events in the gateway.

          For more information, see `What Is Amazon CloudWatch Logs?
          <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.html>`__ .

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'GatewayARN': 'string',
                'GatewayName': 'string'
            }
          **Response Structure**

          - *(dict) --*

            A JSON object containing the ARN of the gateway that was updated.

            - **GatewayARN** *(string) --*

              The Amazon Resource Name (ARN) of the gateway. Use the  ListGateways operation to
              return a list of gateways for your account and AWS Region.

            - **GatewayName** *(string) --*

              The name you configured for your gateway.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_gateway_software_now(
        self, GatewayARN: str
    ) -> ClientUpdateGatewaySoftwareNowResponseTypeDef:
        """
        Updates the gateway virtual machine (VM) software. The request immediately triggers the
        software update.

        .. note::

          When you make this request, you get a ``200 OK`` success response immediately. However, it
          might take some time for the update to complete. You can call  DescribeGatewayInformation
          to verify the gateway is in the ``STATE_RUNNING`` state.

        .. warning::

          A software update forces a system restart of your gateway. You can minimize the chance of
          any disruption to your applications by increasing your iSCSI Initiators' timeouts. For
          more information about increasing iSCSI Initiator timeouts for Windows and Linux, see
          `Customizing Your Windows iSCSI Settings
          <https://docs.aws.amazon.com/storagegateway/latest/userguide/ConfiguringiSCSIClientInitiatorWindowsClient.html#CustomizeWindowsiSCSISettings>`__
          and `Customizing Your Linux iSCSI Settings
          <https://docs.aws.amazon.com/storagegateway/latest/userguide/ConfiguringiSCSIClientInitiatorRedHatClient.html#CustomizeLinuxiSCSISettings>`__
          , respectively.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/storagegateway-2013-06-30/UpdateGatewaySoftwareNow>`_

        **Request Syntax**
        ::

          response = client.update_gateway_software_now(
              GatewayARN='string'
          )
        :type GatewayARN: string
        :param GatewayARN: **[REQUIRED]**

          The Amazon Resource Name (ARN) of the gateway. Use the  ListGateways operation to return a
          list of gateways for your account and AWS Region.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'GatewayARN': 'string'
            }
          **Response Structure**

          - *(dict) --*

            A JSON object containing the of the gateway that was updated.

            - **GatewayARN** *(string) --*

              The Amazon Resource Name (ARN) of the gateway. Use the  ListGateways operation to
              return a list of gateways for your account and AWS Region.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_maintenance_start_time(
        self,
        GatewayARN: str,
        HourOfDay: int,
        MinuteOfHour: int,
        DayOfWeek: int = None,
        DayOfMonth: int = None,
    ) -> ClientUpdateMaintenanceStartTimeResponseTypeDef:
        """
        Updates a gateway's weekly maintenance start time information, including day and time of the
        week. The maintenance time is the time in your gateway's time zone.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/storagegateway-2013-06-30/UpdateMaintenanceStartTime>`_

        **Request Syntax**
        ::

          response = client.update_maintenance_start_time(
              GatewayARN='string',
              HourOfDay=123,
              MinuteOfHour=123,
              DayOfWeek=123,
              DayOfMonth=123
          )
        :type GatewayARN: string
        :param GatewayARN: **[REQUIRED]**

          The Amazon Resource Name (ARN) of the gateway. Use the  ListGateways operation to return a
          list of gateways for your account and AWS Region.

        :type HourOfDay: integer
        :param HourOfDay: **[REQUIRED]**

          The hour component of the maintenance start time represented as *hh* , where *hh* is the
          hour (00 to 23). The hour of the day is in the time zone of the gateway.

        :type MinuteOfHour: integer
        :param MinuteOfHour: **[REQUIRED]**

          The minute component of the maintenance start time represented as *mm* , where *mm* is the
          minute (00 to 59). The minute of the hour is in the time zone of the gateway.

        :type DayOfWeek: integer
        :param DayOfWeek:

          The day of the week component of the maintenance start time week represented as an ordinal
          number from 0 to 6, where 0 represents Sunday and 6 Saturday.

        :type DayOfMonth: integer
        :param DayOfMonth:

          The day of the month component of the maintenance start time represented as an ordinal
          number from 1 to 28, where 1 represents the first day of the month and 28 represents the
          last day of the month.

          .. note::

            This value is only available for tape and volume gateways.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'GatewayARN': 'string'
            }
          **Response Structure**

          - *(dict) --*

            A JSON object containing the of the gateway whose maintenance start time is updated.

            - **GatewayARN** *(string) --*

              The Amazon Resource Name (ARN) of the gateway. Use the  ListGateways operation to
              return a list of gateways for your account and AWS Region.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_nfs_file_share(
        self,
        FileShareARN: str,
        KMSEncrypted: bool = None,
        KMSKey: str = None,
        NFSFileShareDefaults: ClientUpdateNfsFileShareNFSFileShareDefaultsTypeDef = None,
        DefaultStorageClass: str = None,
        ObjectACL: Literal[
            "private",
            "public-read",
            "public-read-write",
            "authenticated-read",
            "bucket-owner-read",
            "bucket-owner-full-control",
            "aws-exec-read",
        ] = None,
        ClientList: List[str] = None,
        Squash: str = None,
        ReadOnly: bool = None,
        GuessMIMETypeEnabled: bool = None,
        RequesterPays: bool = None,
    ) -> ClientUpdateNfsFileShareResponseTypeDef:
        """
        Updates a Network File System (NFS) file share. This operation is only supported in the file
        gateway type.

        .. note::

          To leave a file share field unchanged, set the corresponding input field to null.

        Updates the following file share setting:

        * Default storage class for your S3 bucket

        * Metadata defaults for your S3 bucket

        * Allowed NFS clients for your file share

        * Squash settings

        * Write status of your file share

        .. note::

          To leave a file share field unchanged, set the corresponding input field to null. This
          operation is only supported in file gateways.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/storagegateway-2013-06-30/UpdateNFSFileShare>`_

        **Request Syntax**
        ::

          response = client.update_nfs_file_share(
              FileShareARN='string',
              KMSEncrypted=True|False,
              KMSKey='string',
              NFSFileShareDefaults={
                  'FileMode': 'string',
                  'DirectoryMode': 'string',
                  'GroupId': 123,
                  'OwnerId': 123
              },
              DefaultStorageClass='string',
              ObjectACL=
                  'private'|'public-read'|'public-read-write'|'authenticated-read'
                  |'bucket-owner-read'|'bucket-owner-full-control'|'aws-exec-read',
              ClientList=[
                  'string',
              ],
              Squash='string',
              ReadOnly=True|False,
              GuessMIMETypeEnabled=True|False,
              RequesterPays=True|False
          )
        :type FileShareARN: string
        :param FileShareARN: **[REQUIRED]**

          The Amazon Resource Name (ARN) of the file share to be updated.

        :type KMSEncrypted: boolean
        :param KMSEncrypted:

          True to use Amazon S3 server side encryption with your own AWS KMS key, or false to use a
          key managed by Amazon S3. Optional.

        :type KMSKey: string
        :param KMSKey:

          The Amazon Resource Name (ARN) of the AWS KMS key used for Amazon S3 server side
          encryption. This value can only be set when KMSEncrypted is true. Optional.

        :type NFSFileShareDefaults: dict
        :param NFSFileShareDefaults:

          The default values for the file share. Optional.

          - **FileMode** *(string) --*

            The Unix file mode in the form "nnnn". For example, "0666" represents the default file
            mode inside the file share. The default value is 0666.

          - **DirectoryMode** *(string) --*

            The Unix directory mode in the form "nnnn". For example, "0666" represents the default
            access mode for all directories inside the file share. The default value is 0777.

          - **GroupId** *(integer) --*

            The default group ID for the file share (unless the files have another group ID
            specified). The default value is nfsnobody.

          - **OwnerId** *(integer) --*

            The default owner ID for files in the file share (unless the files have another owner ID
            specified). The default value is nfsnobody.

        :type DefaultStorageClass: string
        :param DefaultStorageClass:

          The default storage class for objects put into an Amazon S3 bucket by the file gateway.
          Possible values are ``S3_STANDARD`` , ``S3_STANDARD_IA`` , or ``S3_ONEZONE_IA`` . If this
          field is not populated, the default value ``S3_STANDARD`` is used. Optional.

        :type ObjectACL: string
        :param ObjectACL:

          A value that sets the access control list permission for objects in the S3 bucket that a
          file gateway puts objects into. The default value is "private".

        :type ClientList: list
        :param ClientList:

          The list of clients that are allowed to access the file gateway. The list must contain
          either valid IP addresses or valid CIDR blocks.

          - *(string) --*

        :type Squash: string
        :param Squash:

          The user mapped to anonymous user. Valid options are the following:

          * ``RootSquash`` - Only root is mapped to anonymous user.

          * ``NoSquash`` - No one is mapped to anonymous user

          * ``AllSquash`` - Everyone is mapped to anonymous user.

        :type ReadOnly: boolean
        :param ReadOnly:

          A value that sets the write status of a file share. This value is true if the write status
          is read-only, and otherwise false.

        :type GuessMIMETypeEnabled: boolean
        :param GuessMIMETypeEnabled:

          A value that enables guessing of the MIME type for uploaded objects based on file
          extensions. Set this value to true to enable MIME type guessing, and otherwise to false.
          The default value is true.

        :type RequesterPays: boolean
        :param RequesterPays:

          A value that sets who pays the cost of the request and the cost associated with data
          download from the S3 bucket. If this value is set to true, the requester pays the costs.
          Otherwise the S3 bucket owner pays. However, the S3 bucket owner always pays the cost of
          storing data.

          .. note::

             ``RequesterPays`` is a configuration for the S3 bucket that backs the file share, so
             make sure that the configuration on the file share is the same as the S3 bucket
             configuration.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'FileShareARN': 'string'
            }
          **Response Structure**

          - *(dict) --*

            UpdateNFSFileShareOutput

            - **FileShareARN** *(string) --*

              The Amazon Resource Name (ARN) of the updated file share.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_smb_file_share(
        self,
        FileShareARN: str,
        KMSEncrypted: bool = None,
        KMSKey: str = None,
        DefaultStorageClass: str = None,
        ObjectACL: Literal[
            "private",
            "public-read",
            "public-read-write",
            "authenticated-read",
            "bucket-owner-read",
            "bucket-owner-full-control",
            "aws-exec-read",
        ] = None,
        ReadOnly: bool = None,
        GuessMIMETypeEnabled: bool = None,
        RequesterPays: bool = None,
        SMBACLEnabled: bool = None,
        AdminUserList: List[str] = None,
        ValidUserList: List[str] = None,
        InvalidUserList: List[str] = None,
    ) -> ClientUpdateSmbFileShareResponseTypeDef:
        """
        Updates a Server Message Block (SMB) file share.

        .. note::

          To leave a file share field unchanged, set the corresponding input field to null. This
          operation is only supported for file gateways.

        .. warning::

          File gateways require AWS Security Token Service (AWS STS) to be activated to enable you
          to create a file share. Make sure that AWS STS is activated in the AWS Region you are
          creating your file gateway in. If AWS STS is not activated in this AWS Region, activate
          it. For information about how to activate AWS STS, see `Activating and Deactivating AWS
          STS in an AWS Region
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_enable-regions.html>`__
          in the *AWS Identity and Access Management User Guide.*

          File gateways don't support creating hard or symbolic links on a file share.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/storagegateway-2013-06-30/UpdateSMBFileShare>`_

        **Request Syntax**
        ::

          response = client.update_smb_file_share(
              FileShareARN='string',
              KMSEncrypted=True|False,
              KMSKey='string',
              DefaultStorageClass='string',
              ObjectACL=
                  'private'|'public-read'|'public-read-write'|'authenticated-read'
                  |'bucket-owner-read'|'bucket-owner-full-control'|'aws-exec-read',
              ReadOnly=True|False,
              GuessMIMETypeEnabled=True|False,
              RequesterPays=True|False,
              SMBACLEnabled=True|False,
              AdminUserList=[
                  'string',
              ],
              ValidUserList=[
                  'string',
              ],
              InvalidUserList=[
                  'string',
              ]
          )
        :type FileShareARN: string
        :param FileShareARN: **[REQUIRED]**

          The Amazon Resource Name (ARN) of the SMB file share that you want to update.

        :type KMSEncrypted: boolean
        :param KMSEncrypted:

          True to use Amazon S3 server side encryption with your own AWS KMS key, or false to use a
          key managed by Amazon S3. Optional.

        :type KMSKey: string
        :param KMSKey:

          The Amazon Resource Name (ARN) of the AWS KMS key used for Amazon S3 server side
          encryption. This value can only be set when KMSEncrypted is true. Optional.

        :type DefaultStorageClass: string
        :param DefaultStorageClass:

          The default storage class for objects put into an Amazon S3 bucket by the file gateway.
          Possible values are ``S3_STANDARD`` , ``S3_STANDARD_IA`` , or ``S3_ONEZONE_IA`` . If this
          field is not populated, the default value ``S3_STANDARD`` is used. Optional.

        :type ObjectACL: string
        :param ObjectACL:

          A value that sets the access control list permission for objects in the S3 bucket that a
          file gateway puts objects into. The default value is "private".

        :type ReadOnly: boolean
        :param ReadOnly:

          A value that sets the write status of a file share. This value is true if the write status
          is read-only, and otherwise false.

        :type GuessMIMETypeEnabled: boolean
        :param GuessMIMETypeEnabled:

          A value that enables guessing of the MIME type for uploaded objects based on file
          extensions. Set this value to true to enable MIME type guessing, and otherwise to false.
          The default value is true.

        :type RequesterPays: boolean
        :param RequesterPays:

          A value that sets who pays the cost of the request and the cost associated with data
          download from the S3 bucket. If this value is set to true, the requester pays the costs.
          Otherwise the S3 bucket owner pays. However, the S3 bucket owner always pays the cost of
          storing data.

          .. note::

             ``RequesterPays`` is a configuration for the S3 bucket that backs the file share, so
             make sure that the configuration on the file share is the same as the S3 bucket
             configuration.

        :type SMBACLEnabled: boolean
        :param SMBACLEnabled:

          Set this value to "true to enable ACL (access control list) on the SMB file share. Set it
          to "false" to map file and directory permissions to the POSIX permissions.

          For more information, see
          https://docs.aws.amazon.com/storagegateway/latest/userguide/smb-acl.htmlin the Storage
          Gateway User Guide.

        :type AdminUserList: list
        :param AdminUserList:

          A list of users in the Active Directory that have administrator rights to the file share.
          A group must be prefixed with the @ character. For example ``@group1`` . Can only be set
          if Authentication is set to ``ActiveDirectory`` .

          - *(string) --*

        :type ValidUserList: list
        :param ValidUserList:

          A list of users or groups in the Active Directory that are allowed to access the file
          share. A group must be prefixed with the @ character. For example ``@group1`` . Can only
          be set if Authentication is set to ``ActiveDirectory`` .

          - *(string) --*

        :type InvalidUserList: list
        :param InvalidUserList:

          A list of users or groups in the Active Directory that are not allowed to access the file
          share. A group must be prefixed with the @ character. For example ``@group1`` . Can only
          be set if Authentication is set to ``ActiveDirectory`` .

          - *(string) --*

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'FileShareARN': 'string'
            }
          **Response Structure**

          - *(dict) --*

            UpdateSMBFileShareOutput

            - **FileShareARN** *(string) --*

              The Amazon Resource Name (ARN) of the updated SMB file share.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_smb_security_strategy(
        self,
        GatewayARN: str,
        SMBSecurityStrategy: Literal["ClientSpecified", "MandatorySigning", "MandatoryEncryption"],
    ) -> ClientUpdateSmbSecurityStrategyResponseTypeDef:
        """
        Updates the SMB security strategy on a file gateway. This action is only supported in file
        gateways.

        .. note::

          This API is called Security level in the User Guide.

          A higher security level can affect performance of the gateway.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/storagegateway-2013-06-30/UpdateSMBSecurityStrategy>`_

        **Request Syntax**
        ::

          response = client.update_smb_security_strategy(
              GatewayARN='string',
              SMBSecurityStrategy='ClientSpecified'|'MandatorySigning'|'MandatoryEncryption'
          )
        :type GatewayARN: string
        :param GatewayARN: **[REQUIRED]**

          The Amazon Resource Name (ARN) of the gateway. Use the  ListGateways operation to return a
          list of gateways for your account and AWS Region.

        :type SMBSecurityStrategy: string
        :param SMBSecurityStrategy: **[REQUIRED]**

          Specifies the type of security strategy.

          ClientSpecified: if you use this option, requests are established based on what is
          negotiated by the client. This option is recommended when you want to maximize
          compatibility across different clients in your environment.

          MandatorySigning: if you use this option, file gateway only allows connections from SMBv2
          or SMBv3 clients that have signing enabled. This option works with SMB clients on
          Microsoft Windows Vista, Windows Server 2008 or newer.

          MandatoryEncryption: if you use this option, file gateway only allows connections from
          SMBv3 clients that have encryption enabled. This option is highly recommended for
          environments that handle sensitive data. This option works with SMB clients on Microsoft
          Windows 8, Windows Server 2012 or newer.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'GatewayARN': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **GatewayARN** *(string) --*

              The Amazon Resource Name (ARN) of the gateway. Use the  ListGateways operation to
              return a list of gateways for your account and AWS Region.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_snapshot_schedule(
        self,
        VolumeARN: str,
        StartAt: int,
        RecurrenceInHours: int,
        Description: str = None,
        Tags: List[ClientUpdateSnapshotScheduleTagsTypeDef] = None,
    ) -> ClientUpdateSnapshotScheduleResponseTypeDef:
        """
        Updates a snapshot schedule configured for a gateway volume. This operation is only
        supported in the cached volume and stored volume gateway types.

        The default snapshot schedule for volume is once every 24 hours, starting at the creation
        time of the volume. You can use this API to change the snapshot schedule configured for the
        volume.

        In the request you must identify the gateway volume whose snapshot schedule you want to
        update, and the schedule information, including when you want the snapshot to begin on a day
        and the frequency (in hours) of snapshots.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/storagegateway-2013-06-30/UpdateSnapshotSchedule>`_

        **Request Syntax**
        ::

          response = client.update_snapshot_schedule(
              VolumeARN='string',
              StartAt=123,
              RecurrenceInHours=123,
              Description='string',
              Tags=[
                  {
                      'Key': 'string',
                      'Value': 'string'
                  },
              ]
          )
        :type VolumeARN: string
        :param VolumeARN: **[REQUIRED]**

          The Amazon Resource Name (ARN) of the volume. Use the  ListVolumes operation to return a
          list of gateway volumes.

        :type StartAt: integer
        :param StartAt: **[REQUIRED]**

          The hour of the day at which the snapshot schedule begins represented as *hh* , where *hh*
          is the hour (0 to 23). The hour of the day is in the time zone of the gateway.

        :type RecurrenceInHours: integer
        :param RecurrenceInHours: **[REQUIRED]**

          Frequency of snapshots. Specify the number of hours between snapshots.

        :type Description: string
        :param Description:

          Optional description of the snapshot that overwrites the existing description.

        :type Tags: list
        :param Tags:

          A list of up to 50 tags that can be assigned to a snapshot. Each tag is a key-value pair.

          .. note::

            Valid characters for key and value are letters, spaces, and numbers representable in
            UTF-8 format, and the following special characters: + - =
                 . _ : / @. The maximum length
            of a tag's key is 128 characters, and the maximum length for a tag's value is 256.

          - *(dict) --*

            A key-value pair that helps you manage, filter, and search for your resource. Allowed
            characters: letters, white space, and numbers, representable in UTF-8, and the following
            characters: + - = . _ : /

            - **Key** *(string) --* **[REQUIRED]**

              Tag key (String). The key can't start with aws:.

            - **Value** *(string) --* **[REQUIRED]**

              Value of the tag key.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'VolumeARN': 'string'
            }
          **Response Structure**

          - *(dict) --*

            A JSON object containing the of the updated storage volume.

            - **VolumeARN** *(string) --*

              The Amazon Resource Name (ARN) of the volume. Use the  ListVolumes operation to return
              a list of gateway volumes.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_vtl_device_type(
        self, VTLDeviceARN: str, DeviceType: str
    ) -> ClientUpdateVtlDeviceTypeResponseTypeDef:
        """
        Updates the type of medium changer in a tape gateway. When you activate a tape gateway, you
        select a medium changer type for the tape gateway. This operation enables you to select a
        different type of medium changer after a tape gateway is activated. This operation is only
        supported in the tape gateway type.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/storagegateway-2013-06-30/UpdateVTLDeviceType>`_

        **Request Syntax**
        ::

          response = client.update_vtl_device_type(
              VTLDeviceARN='string',
              DeviceType='string'
          )
        :type VTLDeviceARN: string
        :param VTLDeviceARN: **[REQUIRED]**

          The Amazon Resource Name (ARN) of the medium changer you want to select.

        :type DeviceType: string
        :param DeviceType: **[REQUIRED]**

          The type of medium changer you want to select.

          Valid Values: "STK-L700", "AWS-Gateway-VTL"

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'VTLDeviceARN': 'string'
            }
          **Response Structure**

          - *(dict) --*

            UpdateVTLDeviceTypeOutput

            - **VTLDeviceARN** *(string) --*

              The Amazon Resource Name (ARN) of the medium changer you have selected.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_tape_archives"]
    ) -> paginator_scope.DescribeTapeArchivesPaginator:
        """
        Get Paginator for `describe_tape_archives` operation.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_tape_recovery_points"]
    ) -> paginator_scope.DescribeTapeRecoveryPointsPaginator:
        """
        Get Paginator for `describe_tape_recovery_points` operation.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_tapes"]
    ) -> paginator_scope.DescribeTapesPaginator:
        """
        Get Paginator for `describe_tapes` operation.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_vtl_devices"]
    ) -> paginator_scope.DescribeVTLDevicesPaginator:
        """
        Get Paginator for `describe_vtl_devices` operation.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_file_shares"]
    ) -> paginator_scope.ListFileSharesPaginator:
        """
        Get Paginator for `list_file_shares` operation.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_gateways"]
    ) -> paginator_scope.ListGatewaysPaginator:
        """
        Get Paginator for `list_gateways` operation.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_tags_for_resource"]
    ) -> paginator_scope.ListTagsForResourcePaginator:
        """
        Get Paginator for `list_tags_for_resource` operation.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_tapes"]
    ) -> paginator_scope.ListTapesPaginator:
        """
        Get Paginator for `list_tapes` operation.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_volumes"]
    ) -> paginator_scope.ListVolumesPaginator:
        """
        Get Paginator for `list_volumes` operation.
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
    InternalServerError: Boto3ClientError
    InvalidGatewayRequestException: Boto3ClientError
    ServiceUnavailableError: Boto3ClientError
