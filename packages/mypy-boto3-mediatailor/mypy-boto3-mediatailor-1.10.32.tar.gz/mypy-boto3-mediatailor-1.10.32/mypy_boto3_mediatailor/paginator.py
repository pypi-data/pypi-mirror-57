"Main interface for mediatailor service Paginators"
from __future__ import annotations

from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_mediatailor.type_defs import (
    ListPlaybackConfigurationsPaginatePaginationConfigTypeDef,
    ListPlaybackConfigurationsPaginateResponseTypeDef,
)


__all__ = ("ListPlaybackConfigurationsPaginator",)


class ListPlaybackConfigurationsPaginator(Boto3Paginator):
    """
    Paginator for `list_playback_configurations`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: ListPlaybackConfigurationsPaginatePaginationConfigTypeDef = None
    ) -> ListPlaybackConfigurationsPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`MediaTailor.Client.list_playback_configurations`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/mediatailor-2018-04-23/ListPlaybackConfigurations>`_

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
        """
