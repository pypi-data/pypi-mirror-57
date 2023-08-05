"Main interface for mediatailor service Client"
from __future__ import annotations

from typing import Any, Dict, List
from botocore.client import BaseClient
from botocore.exceptions import ClientError as Boto3ClientError
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3.type_defs import Literal, overload

# pylint: disable=import-self
import mypy_boto3_mediatailor.client as client_scope

# pylint: disable=import-self
import mypy_boto3_mediatailor.paginator as paginator_scope
from mypy_boto3_mediatailor.type_defs import (
    ClientGetPlaybackConfigurationResponseTypeDef,
    ClientListPlaybackConfigurationsResponseTypeDef,
    ClientListTagsForResourceResponseTypeDef,
    ClientPutPlaybackConfigurationCdnConfigurationTypeDef,
    ClientPutPlaybackConfigurationDashConfigurationTypeDef,
    ClientPutPlaybackConfigurationLivePreRollConfigurationTypeDef,
    ClientPutPlaybackConfigurationResponseTypeDef,
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
    def delete_playback_configuration(self, Name: str) -> Dict[str, Any]:
        """
        Deletes the playback configuration for the specified name.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/mediatailor-2018-04-23/DeletePlaybackConfiguration>`_

        **Request Syntax**
        ::

          response = client.delete_playback_configuration(
              Name='string'
          )
        :type Name: string
        :param Name: **[REQUIRED]**

          The identifier for the playback configuration.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {}
          **Response Structure**

          - *(dict) --*

            The request was successful and there is no content in the response.
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
    def get_playback_configuration(
        self, Name: str
    ) -> ClientGetPlaybackConfigurationResponseTypeDef:
        """
        Returns the playback configuration for the specified name.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/mediatailor-2018-04-23/GetPlaybackConfiguration>`_

        **Request Syntax**
        ::

          response = client.get_playback_configuration(
              Name='string'
          )
        :type Name: string
        :param Name: **[REQUIRED]**

          The identifier for the playback configuration.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'AdDecisionServerUrl': 'string',
                'CdnConfiguration': {
                    'AdSegmentUrlPrefix': 'string',
                    'ContentSegmentUrlPrefix': 'string'
                },
                'DashConfiguration': {
                    'ManifestEndpointPrefix': 'string',
                    'MpdLocation': 'string',
                    'OriginManifestType': 'SINGLE_PERIOD'|'MULTI_PERIOD'
                },
                'HlsConfiguration': {
                    'ManifestEndpointPrefix': 'string'
                },
                'LivePreRollConfiguration': {
                    'AdDecisionServerUrl': 'string',
                    'MaxDurationSeconds': 123
                },
                'Name': 'string',
                'PlaybackConfigurationArn': 'string',
                'PlaybackEndpointPrefix': 'string',
                'SessionInitializationEndpointPrefix': 'string',
                'SlateAdUrl': 'string',
                'Tags': {
                    'string': 'string'
                },
                'TranscodeProfileName': 'string',
                'VideoContentSourceUrl': 'string'
            }
          **Response Structure**

          - *(dict) --*

            Success.

            - **AdDecisionServerUrl** *(string) --*

              The URL for the ad decision server (ADS). This includes the specification of static
              parameters and placeholders for dynamic parameters. AWS Elemental MediaTailor
              substitutes player-specific and session-specific parameters as needed when calling the
              ADS. Alternately, for testing, you can provide a static VAST URL. The maximum length
              is 25,000 characters.

            - **CdnConfiguration** *(dict) --*

              The configuration for using a content delivery network (CDN), like Amazon CloudFront,
              for content and ad segment management.

              - **AdSegmentUrlPrefix** *(string) --*

                A non-default content delivery network (CDN) to serve ad segments. By default, AWS
                Elemental MediaTailor uses Amazon CloudFront with default cache settings as its CDN
                for ad segments. To set up an alternate CDN, create a rule in your CDN for the
                following origin: ads.mediatailor.<region>.amazonaws.com. Then specify the rule's
                name in this AdSegmentUrlPrefix. When AWS Elemental MediaTailor serves a manifest,
                it reports your CDN as the source for ad segments.

              - **ContentSegmentUrlPrefix** *(string) --*

                A content delivery network (CDN) to cache content segments, so that content requests
                don’t always have to go to the origin server. First, create a rule in your CDN for
                the content segment origin server. Then specify the rule's name in this
                ContentSegmentUrlPrefix. When AWS Elemental MediaTailor serves a manifest, it
                reports your CDN as the source for content segments.

            - **DashConfiguration** *(dict) --*

              The configuration for DASH content.

              - **ManifestEndpointPrefix** *(string) --*

                The URL generated by MediaTailor to initiate a playback session. The session uses
                server-side reporting. This setting is ignored in PUT operations.

              - **MpdLocation** *(string) --*

                The setting that controls whether MediaTailor includes the Location tag in DASH
                manifests. MediaTailor populates the Location tag with the URL for manifest update
                requests, to be used by players that don't support sticky redirects. Disable this if
                you have CDN routing rules set up for accessing MediaTailor manifests, and you are
                either using client-side reporting or your players support sticky HTTP redirects.
                Valid values are DISABLED and EMT_DEFAULT. The EMT_DEFAULT setting enables the
                inclusion of the tag and is the default value.

              - **OriginManifestType** *(string) --*

                The setting that controls whether MediaTailor handles manifests from the origin
                server as multi-period manifests or single-period manifests. If your origin server
                produces single-period manifests, set this to SINGLE_PERIOD. The default setting is
                MULTI_PERIOD. For multi-period manifests, omit this setting or set it to
                MULTI_PERIOD.

            - **HlsConfiguration** *(dict) --*

              The configuration for HLS content.

              - **ManifestEndpointPrefix** *(string) --*

                The URL that is used to initiate a playback session for devices that support Apple
                HLS. The session uses server-side reporting.

            - **LivePreRollConfiguration** *(dict) --*

              The configuration for pre-roll ad insertion.

              - **AdDecisionServerUrl** *(string) --*

                The URL for the ad decision server (ADS) for pre-roll ads. This includes the
                specification of static parameters and placeholders for dynamic parameters. AWS
                Elemental MediaTailor substitutes player-specific and session-specific parameters as
                needed when calling the ADS. Alternately, for testing, you can provide a static VAST
                URL. The maximum length is 25,000 characters.

              - **MaxDurationSeconds** *(integer) --* The maximum allowed duration for the pre-roll
              ad avail. AWS Elemental MediaTailor won't play pre-roll ads to exceed this duration,
              regardless of the total duration of ads that the ADS returns.

            - **Name** *(string) --*

              The identifier for the playback configuration.

            - **PlaybackConfigurationArn** *(string) --*

              The Amazon Resource Name (ARN) for the playback configuration.

            - **PlaybackEndpointPrefix** *(string) --*

              The URL that the player accesses to get a manifest from AWS Elemental MediaTailor.
              This session will use server-side reporting.

            - **SessionInitializationEndpointPrefix** *(string) --*

              The URL that the player uses to initialize a session that uses client-side reporting.

            - **SlateAdUrl** *(string) --*

              The URL for a high-quality video asset to transcode and use to fill in time that's not
              used by ads. AWS Elemental MediaTailor shows the slate to fill in gaps in media
              content. Configuring the slate is optional for non-VPAID playback configurations. For
              VPAID, the slate is required because MediaTailor provides it in the slots designated
              for dynamic ad content. The slate must be a high-quality asset that contains both
              audio and video.

            - **Tags** *(dict) --*

              The tags assigned to the playback configuration.

              - *(string) --*

                - *(string) --*

            - **TranscodeProfileName** *(string) --*

              The name that is used to associate this playback configuration with a custom transcode
              profile. This overrides the dynamic transcoding defaults of MediaTailor. Use this only
              if you have already set up custom profiles with the help of AWS Support.

            - **VideoContentSourceUrl** *(string) --*

              The URL prefix for the master playlist for the stream, minus the asset ID. The maximum
              length is 512 characters.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_playback_configurations(
        self, MaxResults: int = None, NextToken: str = None
    ) -> ClientListPlaybackConfigurationsResponseTypeDef:
        """
        Returns a list of the playback configurations defined in AWS Elemental MediaTailor. You can
        specify a maximum number of configurations to return at a time. The default maximum is 50.
        Results are returned in pagefuls. If MediaTailor has more configurations than the specified
        maximum, it provides parameters in the response that you can use to retrieve the next
        pageful.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/mediatailor-2018-04-23/ListPlaybackConfigurations>`_

        **Request Syntax**
        ::

          response = client.list_playback_configurations(
              MaxResults=123,
              NextToken='string'
          )
        :type MaxResults: integer
        :param MaxResults:

          Maximum number of records to return.

        :type NextToken: string
        :param NextToken:

          Pagination token returned by the GET list request when results exceed the maximum allowed.
          Use the token to fetch the next page of results.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Items': [
                    {
                        'AdDecisionServerUrl': 'string',
                        'CdnConfiguration': {
                            'AdSegmentUrlPrefix': 'string',
                            'ContentSegmentUrlPrefix': 'string'
                        },
                        'DashConfiguration': {
                            'ManifestEndpointPrefix': 'string',
                            'MpdLocation': 'string',
                            'OriginManifestType': 'SINGLE_PERIOD'|'MULTI_PERIOD'
                        },
                        'HlsConfiguration': {
                            'ManifestEndpointPrefix': 'string'
                        },
                        'Name': 'string',
                        'PlaybackConfigurationArn': 'string',
                        'PlaybackEndpointPrefix': 'string',
                        'SessionInitializationEndpointPrefix': 'string',
                        'SlateAdUrl': 'string',
                        'Tags': {
                            'string': 'string'
                        },
                        'TranscodeProfileName': 'string',
                        'VideoContentSourceUrl': 'string'
                    },
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            Success.

            - **Items** *(list) --*

              Array of playback configurations. This might be all the available configurations or a
              subset, depending on the settings that you provide and the total number of
              configurations stored.

              - *(dict) --*

                The AWSMediaTailor configuration.

                - **AdDecisionServerUrl** *(string) --*

                  The URL for the ad decision server (ADS). This includes the specification of
                  static parameters and placeholders for dynamic parameters. AWS Elemental
                  MediaTailor substitutes player-specific and session-specific parameters as needed
                  when calling the ADS. Alternately, for testing, you can provide a static VAST URL.
                  The maximum length is 25,000 characters.

                - **CdnConfiguration** *(dict) --*

                  The configuration for using a content delivery network (CDN), like Amazon
                  CloudFront, for content and ad segment management.

                  - **AdSegmentUrlPrefix** *(string) --*

                    A non-default content delivery network (CDN) to serve ad segments. By default,
                    AWS Elemental MediaTailor uses Amazon CloudFront with default cache settings as
                    its CDN for ad segments. To set up an alternate CDN, create a rule in your CDN
                    for the following origin: ads.mediatailor.<region>.amazonaws.com. Then specify
                    the rule's name in this AdSegmentUrlPrefix. When AWS Elemental MediaTailor
                    serves a manifest, it reports your CDN as the source for ad segments.

                  - **ContentSegmentUrlPrefix** *(string) --*

                    A content delivery network (CDN) to cache content segments, so that content
                    requests don’t always have to go to the origin server. First, create a rule in
                    your CDN for the content segment origin server. Then specify the rule's name in
                    this ContentSegmentUrlPrefix. When AWS Elemental MediaTailor serves a manifest,
                    it reports your CDN as the source for content segments.

                - **DashConfiguration** *(dict) --*

                  The configuration for DASH content.

                  - **ManifestEndpointPrefix** *(string) --*

                    The URL generated by MediaTailor to initiate a playback session. The session
                    uses server-side reporting. This setting is ignored in PUT operations.

                  - **MpdLocation** *(string) --*

                    The setting that controls whether MediaTailor includes the Location tag in DASH
                    manifests. MediaTailor populates the Location tag with the URL for manifest
                    update requests, to be used by players that don't support sticky redirects.
                    Disable this if you have CDN routing rules set up for accessing MediaTailor
                    manifests, and you are either using client-side reporting or your players
                    support sticky HTTP redirects. Valid values are DISABLED and EMT_DEFAULT. The
                    EMT_DEFAULT setting enables the inclusion of the tag and is the default value.

                  - **OriginManifestType** *(string) --*

                    The setting that controls whether MediaTailor handles manifests from the origin
                    server as multi-period manifests or single-period manifests. If your origin
                    server produces single-period manifests, set this to SINGLE_PERIOD. The default
                    setting is MULTI_PERIOD. For multi-period manifests, omit this setting or set it
                    to MULTI_PERIOD.

                - **HlsConfiguration** *(dict) --*

                  The configuration for HLS content.

                  - **ManifestEndpointPrefix** *(string) --*

                    The URL that is used to initiate a playback session for devices that support
                    Apple HLS. The session uses server-side reporting.

                - **Name** *(string) --*

                  The identifier for the playback configuration.

                - **PlaybackConfigurationArn** *(string) --*

                  The Amazon Resource Name (ARN) for the playback configuration.

                - **PlaybackEndpointPrefix** *(string) --*

                  The URL that the player accesses to get a manifest from AWS Elemental MediaTailor.
                  This session will use server-side reporting.

                - **SessionInitializationEndpointPrefix** *(string) --*

                  The URL that the player uses to initialize a session that uses client-side
                  reporting.

                - **SlateAdUrl** *(string) --*

                  The URL for a high-quality video asset to transcode and use to fill in time that's
                  not used by ads. AWS Elemental MediaTailor shows the slate to fill in gaps in
                  media content. Configuring the slate is optional for non-VPAID playback
                  configurations. For VPAID, the slate is required because MediaTailor provides it
                  in the slots designated for dynamic ad content. The slate must be a high-quality
                  asset that contains both audio and video.

                - **Tags** *(dict) --*

                  The tags assigned to the playback configuration.

                  - *(string) --*

                    - *(string) --*

                - **TranscodeProfileName** *(string) --*

                  The name that is used to associate this playback configuration with a custom
                  transcode profile. This overrides the dynamic transcoding defaults of MediaTailor.
                  Use this only if you have already set up custom profiles with the help of AWS
                  Support.

                - **VideoContentSourceUrl** *(string) --*

                  The URL prefix for the master playlist for the stream, minus the asset ID. The
                  maximum length is 512 characters.

            - **NextToken** *(string) --*

              Pagination token returned by the GET list request when results exceed the maximum
              allowed. Use the token to fetch the next page of results.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_tags_for_resource(self, ResourceArn: str) -> ClientListTagsForResourceResponseTypeDef:
        """
        Returns a list of the tags assigned to the specified playback configuration resource.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/mediatailor-2018-04-23/ListTagsForResource>`_

        **Request Syntax**
        ::

          response = client.list_tags_for_resource(
              ResourceArn='string'
          )
        :type ResourceArn: string
        :param ResourceArn: **[REQUIRED]**

          The Amazon Resource Name (ARN) for the playback configuration. You can get this from the
          response to any playback configuration request.

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

          - *(dict) --*

            Success.

            - **Tags** *(dict) --*

              A comma-separated list of tag key:value pairs. For example: { "Key1": "Value1",
              "Key2": "Value2" }

              - *(string) --*

                - *(string) --*
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def put_playback_configuration(
        self,
        AdDecisionServerUrl: str = None,
        CdnConfiguration: ClientPutPlaybackConfigurationCdnConfigurationTypeDef = None,
        DashConfiguration: ClientPutPlaybackConfigurationDashConfigurationTypeDef = None,
        LivePreRollConfiguration: ClientPutPlaybackConfigurationLivePreRollConfigurationTypeDef = None,
        Name: str = None,
        SlateAdUrl: str = None,
        Tags: Dict[str, str] = None,
        TranscodeProfileName: str = None,
        VideoContentSourceUrl: str = None,
    ) -> ClientPutPlaybackConfigurationResponseTypeDef:
        """
        Adds a new playback configuration to AWS Elemental MediaTailor.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/mediatailor-2018-04-23/PutPlaybackConfiguration>`_

        **Request Syntax**
        ::

          response = client.put_playback_configuration(
              AdDecisionServerUrl='string',
              CdnConfiguration={
                  'AdSegmentUrlPrefix': 'string',
                  'ContentSegmentUrlPrefix': 'string'
              },
              DashConfiguration={
                  'MpdLocation': 'string',
                  'OriginManifestType': 'SINGLE_PERIOD'|'MULTI_PERIOD'
              },
              LivePreRollConfiguration={
                  'AdDecisionServerUrl': 'string',
                  'MaxDurationSeconds': 123
              },
              Name='string',
              SlateAdUrl='string',
              Tags={
                  'string': 'string'
              },
              TranscodeProfileName='string',
              VideoContentSourceUrl='string'
          )
        :type AdDecisionServerUrl: string
        :param AdDecisionServerUrl:

          The URL for the ad decision server (ADS). This includes the specification of static
          parameters and placeholders for dynamic parameters. AWS Elemental MediaTailor substitutes
          player-specific and session-specific parameters as needed when calling the ADS.
          Alternately, for testing you can provide a static VAST URL. The maximum length is 25,000
          characters.

        :type CdnConfiguration: dict
        :param CdnConfiguration:

          The configuration for using a content delivery network (CDN), like Amazon CloudFront, for
          content and ad segment management.

          - **AdSegmentUrlPrefix** *(string) --*

            A non-default content delivery network (CDN) to serve ad segments. By default, AWS
            Elemental MediaTailor uses Amazon CloudFront with default cache settings as its CDN for
            ad segments. To set up an alternate CDN, create a rule in your CDN for the following
            origin: ads.mediatailor.<region>.amazonaws.com. Then specify the rule's name in this
            AdSegmentUrlPrefix. When AWS Elemental MediaTailor serves a manifest, it reports your
            CDN as the source for ad segments.

          - **ContentSegmentUrlPrefix** *(string) --*

            A content delivery network (CDN) to cache content segments, so that content requests
            don’t always have to go to the origin server. First, create a rule in your CDN for the
            content segment origin server. Then specify the rule's name in this
            ContentSegmentUrlPrefix. When AWS Elemental MediaTailor serves a manifest, it reports
            your CDN as the source for content segments.

        :type DashConfiguration: dict
        :param DashConfiguration:

          The configuration for DASH content.

          - **MpdLocation** *(string) --*

            The setting that controls whether MediaTailor includes the Location tag in DASH
            manifests. MediaTailor populates the Location tag with the URL for manifest update
            requests, to be used by players that don't support sticky redirects. Disable this if you
            have CDN routing rules set up for accessing MediaTailor manifests, and you are either
            using client-side reporting or your players support sticky HTTP redirects. Valid values
            are DISABLED and EMT_DEFAULT. The EMT_DEFAULT setting enables the inclusion of the tag
            and is the default value.

          - **OriginManifestType** *(string) --*

            The setting that controls whether MediaTailor handles manifests from the origin server
            as multi-period manifests or single-period manifests. If your origin server produces
            single-period manifests, set this to SINGLE_PERIOD. The default setting is MULTI_PERIOD.
            For multi-period manifests, omit this setting or set it to MULTI_PERIOD.

        :type LivePreRollConfiguration: dict
        :param LivePreRollConfiguration:

          The configuration for pre-roll ad insertion.

          - **AdDecisionServerUrl** *(string) --*

            The URL for the ad decision server (ADS) for pre-roll ads. This includes the
            specification of static parameters and placeholders for dynamic parameters. AWS
            Elemental MediaTailor substitutes player-specific and session-specific parameters as
            needed when calling the ADS. Alternately, for testing, you can provide a static VAST
            URL. The maximum length is 25,000 characters.

          - **MaxDurationSeconds** *(integer) --* The maximum allowed duration for the pre-roll ad
          avail. AWS Elemental MediaTailor won't play pre-roll ads to exceed this duration,
          regardless of the total duration of ads that the ADS returns.

        :type Name: string
        :param Name:

          The identifier for the playback configuration.

        :type SlateAdUrl: string
        :param SlateAdUrl:

          The URL for a high-quality video asset to transcode and use to fill in time that's not
          used by ads. AWS Elemental MediaTailor shows the slate to fill in gaps in media content.
          Configuring the slate is optional for non-VPAID configurations. For VPAID, the slate is
          required because MediaTailor provides it in the slots that are designated for dynamic ad
          content. The slate must be a high-quality asset that contains both audio and video.

        :type Tags: dict
        :param Tags:

          The tags to assign to the playback configuration.

          - *(string) --*

            - *(string) --*

        :type TranscodeProfileName: string
        :param TranscodeProfileName:

          The name that is used to associate this playback configuration with a custom transcode
          profile. This overrides the dynamic transcoding defaults of MediaTailor. Use this only if
          you have already set up custom profiles with the help of AWS Support.

        :type VideoContentSourceUrl: string
        :param VideoContentSourceUrl:

          The URL prefix for the master playlist for the stream, minus the asset ID. The maximum
          length is 512 characters.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'AdDecisionServerUrl': 'string',
                'CdnConfiguration': {
                    'AdSegmentUrlPrefix': 'string',
                    'ContentSegmentUrlPrefix': 'string'
                },
                'DashConfiguration': {
                    'ManifestEndpointPrefix': 'string',
                    'MpdLocation': 'string',
                    'OriginManifestType': 'SINGLE_PERIOD'|'MULTI_PERIOD'
                },
                'HlsConfiguration': {
                    'ManifestEndpointPrefix': 'string'
                },
                'LivePreRollConfiguration': {
                    'AdDecisionServerUrl': 'string',
                    'MaxDurationSeconds': 123
                },
                'Name': 'string',
                'PlaybackConfigurationArn': 'string',
                'PlaybackEndpointPrefix': 'string',
                'SessionInitializationEndpointPrefix': 'string',
                'SlateAdUrl': 'string',
                'Tags': {
                    'string': 'string'
                },
                'TranscodeProfileName': 'string',
                'VideoContentSourceUrl': 'string'
            }
          **Response Structure**

          - *(dict) --*

            Success.

            - **AdDecisionServerUrl** *(string) --*

              The URL for the ad decision server (ADS). This includes the specification of static
              parameters and placeholders for dynamic parameters. AWS Elemental MediaTailor
              substitutes player-specific and session-specific parameters as needed when calling the
              ADS. Alternately, for testing, you can provide a static VAST URL. The maximum length
              is 25,000 characters.

            - **CdnConfiguration** *(dict) --*

              The configuration for using a content delivery network (CDN), like Amazon CloudFront,
              for content and ad segment management.

              - **AdSegmentUrlPrefix** *(string) --*

                A non-default content delivery network (CDN) to serve ad segments. By default, AWS
                Elemental MediaTailor uses Amazon CloudFront with default cache settings as its CDN
                for ad segments. To set up an alternate CDN, create a rule in your CDN for the
                following origin: ads.mediatailor.<region>.amazonaws.com. Then specify the rule's
                name in this AdSegmentUrlPrefix. When AWS Elemental MediaTailor serves a manifest,
                it reports your CDN as the source for ad segments.

              - **ContentSegmentUrlPrefix** *(string) --*

                A content delivery network (CDN) to cache content segments, so that content requests
                don’t always have to go to the origin server. First, create a rule in your CDN for
                the content segment origin server. Then specify the rule's name in this
                ContentSegmentUrlPrefix. When AWS Elemental MediaTailor serves a manifest, it
                reports your CDN as the source for content segments.

            - **DashConfiguration** *(dict) --*

              The configuration for DASH content.

              - **ManifestEndpointPrefix** *(string) --*

                The URL generated by MediaTailor to initiate a playback session. The session uses
                server-side reporting. This setting is ignored in PUT operations.

              - **MpdLocation** *(string) --*

                The setting that controls whether MediaTailor includes the Location tag in DASH
                manifests. MediaTailor populates the Location tag with the URL for manifest update
                requests, to be used by players that don't support sticky redirects. Disable this if
                you have CDN routing rules set up for accessing MediaTailor manifests, and you are
                either using client-side reporting or your players support sticky HTTP redirects.
                Valid values are DISABLED and EMT_DEFAULT. The EMT_DEFAULT setting enables the
                inclusion of the tag and is the default value.

              - **OriginManifestType** *(string) --*

                The setting that controls whether MediaTailor handles manifests from the origin
                server as multi-period manifests or single-period manifests. If your origin server
                produces single-period manifests, set this to SINGLE_PERIOD. The default setting is
                MULTI_PERIOD. For multi-period manifests, omit this setting or set it to
                MULTI_PERIOD.

            - **HlsConfiguration** *(dict) --*

              The configuration for HLS content.

              - **ManifestEndpointPrefix** *(string) --*

                The URL that is used to initiate a playback session for devices that support Apple
                HLS. The session uses server-side reporting.

            - **LivePreRollConfiguration** *(dict) --*

              The configuration for pre-roll ad insertion.

              - **AdDecisionServerUrl** *(string) --*

                The URL for the ad decision server (ADS) for pre-roll ads. This includes the
                specification of static parameters and placeholders for dynamic parameters. AWS
                Elemental MediaTailor substitutes player-specific and session-specific parameters as
                needed when calling the ADS. Alternately, for testing, you can provide a static VAST
                URL. The maximum length is 25,000 characters.

              - **MaxDurationSeconds** *(integer) --* The maximum allowed duration for the pre-roll
              ad avail. AWS Elemental MediaTailor won't play pre-roll ads to exceed this duration,
              regardless of the total duration of ads that the ADS returns.

            - **Name** *(string) --*

              The identifier for the playback configuration.

            - **PlaybackConfigurationArn** *(string) --*

              The Amazon Resource Name (ARN) for the playback configuration.

            - **PlaybackEndpointPrefix** *(string) --*

              The URL that the player accesses to get a manifest from AWS Elemental MediaTailor.
              This session will use server-side reporting.

            - **SessionInitializationEndpointPrefix** *(string) --*

              The URL that the player uses to initialize a session that uses client-side reporting.

            - **SlateAdUrl** *(string) --*

              The URL for a high-quality video asset to transcode and use to fill in time that's not
              used by ads. AWS Elemental MediaTailor shows the slate to fill in gaps in media
              content. Configuring the slate is optional for non-VPAID playback configurations. For
              VPAID, the slate is required because MediaTailor provides it in the slots designated
              for dynamic ad content. The slate must be a high-quality asset that contains both
              audio and video.

            - **Tags** *(dict) --*

              The tags assigned to the playback configuration.

              - *(string) --*

                - *(string) --*

            - **TranscodeProfileName** *(string) --*

              The name that is used to associate this playback configuration with a custom transcode
              profile. This overrides the dynamic transcoding defaults of MediaTailor. Use this only
              if you have already set up custom profiles with the help of AWS Support.

            - **VideoContentSourceUrl** *(string) --*

              The URL prefix for the master playlist for the stream, minus the asset ID. The maximum
              length is 512 characters.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def tag_resource(self, ResourceArn: str, Tags: Dict[str, str]) -> None:
        """
        Adds tags to the specified playback configuration resource. You can specify one or more tags
        to add.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/mediatailor-2018-04-23/TagResource>`_

        **Request Syntax**
        ::

          response = client.tag_resource(
              ResourceArn='string',
              Tags={
                  'string': 'string'
              }
          )
        :type ResourceArn: string
        :param ResourceArn: **[REQUIRED]**

          The Amazon Resource Name (ARN) for the playback configuration. You can get this from the
          response to any playback configuration request.

        :type Tags: dict
        :param Tags: **[REQUIRED]**

          A comma-separated list of tag key:value pairs. For example: { "Key1": "Value1", "Key2":
          "Value2" }

          - *(string) --*

            - *(string) --*

        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def untag_resource(self, ResourceArn: str, TagKeys: List[str]) -> None:
        """
        Removes tags from the specified playback configuration resource. You can specify one or more
        tags to remove.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/mediatailor-2018-04-23/UntagResource>`_

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

          The Amazon Resource Name (ARN) for the playback configuration. You can get this from the
          response to any playback configuration request.

        :type TagKeys: list
        :param TagKeys: **[REQUIRED]**

          A comma-separated list of the tag keys to remove from the playback configuration.

          - *(string) --*

        :returns: None
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_playback_configurations"]
    ) -> paginator_scope.ListPlaybackConfigurationsPaginator:
        """
        Get Paginator for `list_playback_configurations` operation.
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
    BadRequestException: Boto3ClientError
    ClientError: Boto3ClientError
