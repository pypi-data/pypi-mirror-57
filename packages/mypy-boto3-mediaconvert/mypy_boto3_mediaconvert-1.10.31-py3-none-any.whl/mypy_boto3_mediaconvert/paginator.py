"Main interface for mediaconvert service Paginators"
from __future__ import annotations

from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3.type_defs import Literal
from mypy_boto3_mediaconvert.type_defs import (
    DescribeEndpointsPaginatePaginationConfigTypeDef,
    DescribeEndpointsPaginateResponseTypeDef,
    ListJobTemplatesPaginatePaginationConfigTypeDef,
    ListJobTemplatesPaginateResponseTypeDef,
    ListJobsPaginatePaginationConfigTypeDef,
    ListJobsPaginateResponseTypeDef,
    ListPresetsPaginatePaginationConfigTypeDef,
    ListPresetsPaginateResponseTypeDef,
    ListQueuesPaginatePaginationConfigTypeDef,
    ListQueuesPaginateResponseTypeDef,
)


__all__ = (
    "DescribeEndpointsPaginator",
    "ListJobTemplatesPaginator",
    "ListJobsPaginator",
    "ListPresetsPaginator",
    "ListQueuesPaginator",
)


class DescribeEndpointsPaginator(Boto3Paginator):
    """
    Paginator for `describe_endpoints`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Mode: Literal["DEFAULT", "GET_ONLY"] = None,
        PaginationConfig: DescribeEndpointsPaginatePaginationConfigTypeDef = None,
    ) -> DescribeEndpointsPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`MediaConvert.Client.describe_endpoints`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/mediaconvert-2017-08-29/DescribeEndpoints>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              Mode='DEFAULT'|'GET_ONLY',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type Mode: string
        :param Mode: Optional field, defaults to DEFAULT. Specify DEFAULT for this operation to
        return your endpoints if any exist, or to create an endpoint for you and return it if one
        doesn't already exist. Specify GET_ONLY to return your endpoints if any exist, or an empty
        list if none exist.

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
                'Endpoints': [
                    {
                        'Url': 'string'
                    },
                ],

            }
          **Response Structure**

          - *(dict) --*

            - **Endpoints** *(list) --* List of endpoints

              - *(dict) --* Describes an account-specific API endpoint.

                - **Url** *(string) --* URL of endpoint
        """


class ListJobTemplatesPaginator(Boto3Paginator):
    """
    Paginator for `list_job_templates`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Category: str = None,
        ListBy: Literal["NAME", "CREATION_DATE", "SYSTEM"] = None,
        Order: Literal["ASCENDING", "DESCENDING"] = None,
        PaginationConfig: ListJobTemplatesPaginatePaginationConfigTypeDef = None,
    ) -> ListJobTemplatesPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`MediaConvert.Client.list_job_templates`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/mediaconvert-2017-08-29/ListJobTemplates>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              Category='string',
              ListBy='NAME'|'CREATION_DATE'|'SYSTEM',
              Order='ASCENDING'|'DESCENDING',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type Category: string
        :param Category: Optionally, specify a job template category to limit responses to only job
        templates from that category.

        :type ListBy: string
        :param ListBy: Optional. When you request a list of job templates, you can choose to list
        them alphabetically by NAME or chronologically by CREATION_DATE. If you don't specify, the
        service will list them by name.

        :type Order: string
        :param Order: When you request lists of resources, you can optionally specify whether they
        are sorted in ASCENDING or DESCENDING order. Default varies by resource.

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
                'JobTemplates': [
                    {
                        'AccelerationSettings': {
                            'Mode': 'DISABLED'|'ENABLED'|'PREFERRED'
                        },
                        'Arn': 'string',
                        'Category': 'string',
                        'CreatedAt': datetime(2015, 1, 1),
                        'Description': 'string',
                        'LastUpdated': datetime(2015, 1, 1),
                        'Name': 'string',
                        'Priority': 123,
                        'Queue': 'string',
                        'Settings': {
                            'AdAvailOffset': 123,
                            'AvailBlanking': {
                                'AvailBlankingImage': 'string'
                            },
                            'Esam': {
                                'ManifestConfirmConditionNotification': {
                                    'MccXml': 'string'
                                },
                                'ResponseSignalPreroll': 123,
                                'SignalProcessingNotification': {
                                    'SccXml': 'string'
                                }
                            },
                            'Inputs': [
                                {
                                    'AudioSelectorGroups': {
                                        'string': {
                                            'AudioSelectorNames': [
                                                'string',
                                            ]
                                        }
                                    },
                                    'AudioSelectors': {
                                        'string': {
                                            'CustomLanguageCode': 'string',
                                            'DefaultSelection': 'DEFAULT'|'NOT_DEFAULT',
                                            'ExternalAudioFileInput': 'string',
                                            'LanguageCode':
                                            'ENG'|'SPA'|'FRA'
                                            |'DEU'|'GER'|'ZHO'
                                            |'ARA'|'HIN'|'JPN'
                                            |'RUS'|'POR'|'ITA'
                                            |'URD'|'VIE'|'KOR'
                                            |'PAN'|'ABK'|'AAR'
                                            |'AFR'|'AKA'|'SQI'
                                            |'AMH'|'ARG'|'HYE'
                                            |'ASM'|'AVA'|'AVE'
                                            |'AYM'|'AZE'|'BAM'
                                            |'BAK'|'EUS'|'BEL'
                                            |'BEN'|'BIH'|'BIS'
                                            |'BOS'|'BRE'|'BUL'
                                            |'MYA'|'CAT'|'KHM'
                                            |'CHA'|'CHE'|'NYA'
                                            |'CHU'|'CHV'|'COR'
                                            |'COS'|'CRE'|'HRV'
                                            |'CES'|'DAN'|'DIV'
                                            |'NLD'|'DZO'|'ENM'
                                            |'EPO'|'EST'|'EWE'
                                            |'FAO'|'FIJ'|'FIN'
                                            |'FRM'|'FUL'|'GLA'
                                            |'GLG'|'LUG'|'KAT'
                                            |'ELL'|'GRN'|'GUJ'
                                            |'HAT'|'HAU'|'HEB'
                                            |'HER'|'HMO'|'HUN'
                                            |'ISL'|'IDO'|'IBO'
                                            |'IND'|'INA'|'ILE'
                                            |'IKU'|'IPK'|'GLE'
                                            |'JAV'|'KAL'|'KAN'
                                            |'KAU'|'KAS'|'KAZ'
                                            |'KIK'|'KIN'|'KIR'
                                            |'KOM'|'KON'|'KUA'
                                            |'KUR'|'LAO'|'LAT'
                                            |'LAV'|'LIM'|'LIN'
                                            |'LIT'|'LUB'|'LTZ'
                                            |'MKD'|'MLG'|'MSA'
                                            |'MAL'|'MLT'|'GLV'
                                            |'MRI'|'MAR'|'MAH'
                                            |'MON'|'NAU'|'NAV'
                                            |'NDE'|'NBL'|'NDO'
                                            |'NEP'|'SME'|'NOR'
                                            |'NOB'|'NNO'|'OCI'
                                            |'OJI'|'ORI'|'ORM'
                                            |'OSS'|'PLI'|'FAS'
                                            |'POL'|'PUS'|'QUE'
                                            |'QAA'|'RON'|'ROH'
                                            |'RUN'|'SMO'|'SAG'
                                            |'SAN'|'SRD'|'SRB'
                                            |'SNA'|'III'|'SND'
                                            |'SIN'|'SLK'|'SLV'
                                            |'SOM'|'SOT'|'SUN'
                                            |'SWA'|'SSW'|'SWE'
                                            |'TGL'|'TAH'|'TGK'
                                            |'TAM'|'TAT'|'TEL'
                                            |'THA'|'BOD'|'TIR'
                                            |'TON'|'TSO'|'TSN'
                                            |'TUR'|'TUK'|'TWI'
                                            |'UIG'|'UKR'|'UZB'
                                            |'VEN'|'VOL'|'WLN'
                                            |'CYM'|'FRY'|'WOL'
                                            |'XHO'|'YID'|'YOR'
                                            |'ZHA'|'ZUL'|'ORJ'
                                            |'QPC'|'TNG',
                                            'Offset': 123,
                                            'Pids': [
                                                123,
                                            ],
                                            'ProgramSelection': 123,
                                            'RemixSettings': {
                                                'ChannelMapping': {
                                                    'OutputChannels': [
                                                        {
                                                            'InputChannels': [
                                                                123,
                                                            ]
                                                        },
                                                    ]
                                                },
                                                'ChannelsIn': 123,
                                                'ChannelsOut': 123
                                            },
                                            'SelectorType': 'PID'|'TRACK'|'LANGUAGE_CODE',
                                            'Tracks': [
                                                123,
                                            ]
                                        }
                                    },
                                    'CaptionSelectors': {
                                        'string': {
                                            'CustomLanguageCode': 'string',
                                            'LanguageCode':
                                            'ENG'|'SPA'|'FRA'
                                            |'DEU'|'GER'|'ZHO'
                                            |'ARA'|'HIN'|'JPN'
                                            |'RUS'|'POR'|'ITA'
                                            |'URD'|'VIE'|'KOR'
                                            |'PAN'|'ABK'|'AAR'
                                            |'AFR'|'AKA'|'SQI'
                                            |'AMH'|'ARG'|'HYE'
                                            |'ASM'|'AVA'|'AVE'
                                            |'AYM'|'AZE'|'BAM'
                                            |'BAK'|'EUS'|'BEL'
                                            |'BEN'|'BIH'|'BIS'
                                            |'BOS'|'BRE'|'BUL'
                                            |'MYA'|'CAT'|'KHM'
                                            |'CHA'|'CHE'|'NYA'
                                            |'CHU'|'CHV'|'COR'
                                            |'COS'|'CRE'|'HRV'
                                            |'CES'|'DAN'|'DIV'
                                            |'NLD'|'DZO'|'ENM'
                                            |'EPO'|'EST'|'EWE'
                                            |'FAO'|'FIJ'|'FIN'
                                            |'FRM'|'FUL'|'GLA'
                                            |'GLG'|'LUG'|'KAT'
                                            |'ELL'|'GRN'|'GUJ'
                                            |'HAT'|'HAU'|'HEB'
                                            |'HER'|'HMO'|'HUN'
                                            |'ISL'|'IDO'|'IBO'
                                            |'IND'|'INA'|'ILE'
                                            |'IKU'|'IPK'|'GLE'
                                            |'JAV'|'KAL'|'KAN'
                                            |'KAU'|'KAS'|'KAZ'
                                            |'KIK'|'KIN'|'KIR'
                                            |'KOM'|'KON'|'KUA'
                                            |'KUR'|'LAO'|'LAT'
                                            |'LAV'|'LIM'|'LIN'
                                            |'LIT'|'LUB'|'LTZ'
                                            |'MKD'|'MLG'|'MSA'
                                            |'MAL'|'MLT'|'GLV'
                                            |'MRI'|'MAR'|'MAH'
                                            |'MON'|'NAU'|'NAV'
                                            |'NDE'|'NBL'|'NDO'
                                            |'NEP'|'SME'|'NOR'
                                            |'NOB'|'NNO'|'OCI'
                                            |'OJI'|'ORI'|'ORM'
                                            |'OSS'|'PLI'|'FAS'
                                            |'POL'|'PUS'|'QUE'
                                            |'QAA'|'RON'|'ROH'
                                            |'RUN'|'SMO'|'SAG'
                                            |'SAN'|'SRD'|'SRB'
                                            |'SNA'|'III'|'SND'
                                            |'SIN'|'SLK'|'SLV'
                                            |'SOM'|'SOT'|'SUN'
                                            |'SWA'|'SSW'|'SWE'
                                            |'TGL'|'TAH'|'TGK'
                                            |'TAM'|'TAT'|'TEL'
                                            |'THA'|'BOD'|'TIR'
                                            |'TON'|'TSO'|'TSN'
                                            |'TUR'|'TUK'|'TWI'
                                            |'UIG'|'UKR'|'UZB'
                                            |'VEN'|'VOL'|'WLN'
                                            |'CYM'|'FRY'|'WOL'
                                            |'XHO'|'YID'|'YOR'
                                            |'ZHA'|'ZUL'|'ORJ'
                                            |'QPC'|'TNG',
                                            'SourceSettings': {
                                                'AncillarySourceSettings': {
                                                    'Convert608To708': 'UPCONVERT'|'DISABLED',
                                                    'SourceAncillaryChannelNumber': 123,
                                                    'TerminateCaptions': 'END_OF_INPUT'|'DISABLED'
                                                },
                                                'DvbSubSourceSettings': {
                                                    'Pid': 123
                                                },
                                                'EmbeddedSourceSettings': {
                                                    'Convert608To708': 'UPCONVERT'|'DISABLED',
                                                    'Source608ChannelNumber': 123,
                                                    'Source608TrackNumber': 123,
                                                    'TerminateCaptions': 'END_OF_INPUT'|'DISABLED'
                                                },
                                                'FileSourceSettings': {
                                                    'Convert608To708': 'UPCONVERT'|'DISABLED',
                                                    'SourceFile': 'string',
                                                    'TimeDelta': 123
                                                },
                                                'SourceType':
                                                'ANCILLARY'
                                                |'DVB_SUB'
                                                |'EMBEDDED'
                                                |'SCTE20'
                                                |'SCC'
                                                |'TTML'
                                                |'STL'|'SRT'
                                                |'SMI'
                                                |'TELETEXT'
                                                |'NULL_SOURCE'
                                                |'IMSC',
                                                'TeletextSourceSettings': {
                                                    'PageNumber': 'string'
                                                },
                                                'TrackSourceSettings': {
                                                    'TrackNumber': 123
                                                }
                                            }
                                        }
                                    },
                                    'Crop': {
                                        'Height': 123,
                                        'Width': 123,
                                        'X': 123,
                                        'Y': 123
                                    },
                                    'DeblockFilter': 'ENABLED'|'DISABLED',
                                    'DenoiseFilter': 'ENABLED'|'DISABLED',
                                    'FilterEnable': 'AUTO'|'DISABLE'|'FORCE',
                                    'FilterStrength': 123,
                                    'ImageInserter': {
                                        'InsertableImages': [
                                            {
                                                'Duration': 123,
                                                'FadeIn': 123,
                                                'FadeOut': 123,
                                                'Height': 123,
                                                'ImageInserterInput': 'string',
                                                'ImageX': 123,
                                                'ImageY': 123,
                                                'Layer': 123,
                                                'Opacity': 123,
                                                'StartTime': 'string',
                                                'Width': 123
                                            },
                                        ]
                                    },
                                    'InputClippings': [
                                        {
                                            'EndTimecode': 'string',
                                            'StartTimecode': 'string'
                                        },
                                    ],
                                    'Position': {
                                        'Height': 123,
                                        'Width': 123,
                                        'X': 123,
                                        'Y': 123
                                    },
                                    'ProgramNumber': 123,
                                    'PsiControl': 'IGNORE_PSI'|'USE_PSI',
                                    'TimecodeSource': 'EMBEDDED'|'ZEROBASED'|'SPECIFIEDSTART',
                                    'TimecodeStart': 'string',
                                    'VideoSelector': {
                                        'AlphaBehavior': 'DISCARD'|'REMAP_TO_LUMA',
                                        'ColorSpace':
                                        'FOLLOW'|'REC_601'|'REC_709'
                                        |'HDR10'|'HLG_2020',
                                        'ColorSpaceUsage': 'FORCE'|'FALLBACK',
                                        'Hdr10Metadata': {
                                            'BluePrimaryX': 123,
                                            'BluePrimaryY': 123,
                                            'GreenPrimaryX': 123,
                                            'GreenPrimaryY': 123,
                                            'MaxContentLightLevel': 123,
                                            'MaxFrameAverageLightLevel': 123,
                                            'MaxLuminance': 123,
                                            'MinLuminance': 123,
                                            'RedPrimaryX': 123,
                                            'RedPrimaryY': 123,
                                            'WhitePointX': 123,
                                            'WhitePointY': 123
                                        },
                                        'Pid': 123,
                                        'ProgramNumber': 123,
                                        'Rotate':
                                        'DEGREE_0'|'DEGREES_90'
                                        |'DEGREES_180'|'DEGREES_270'
                                        |'AUTO'
                                    }
                                },
                            ],
                            'MotionImageInserter': {
                                'Framerate': {
                                    'FramerateDenominator': 123,
                                    'FramerateNumerator': 123
                                },
                                'Input': 'string',
                                'InsertionMode': 'MOV'|'PNG',
                                'Offset': {
                                    'ImageX': 123,
                                    'ImageY': 123
                                },
                                'Playback': 'ONCE'|'REPEAT',
                                'StartTime': 'string'
                            },
                            'NielsenConfiguration': {
                                'BreakoutCode': 123,
                                'DistributorId': 'string'
                            },
                            'OutputGroups': [
                                {
                                    'CustomName': 'string',
                                    'Name': 'string',
                                    'OutputGroupSettings': {
                                        'CmafGroupSettings': {
                                            'AdditionalManifests': [
                                                {
                                                    'ManifestNameModifier': 'string',
                                                    'SelectedOutputs': [
                                                        'string',
                                                    ]
                                                },
                                            ],
                                            'BaseUrl': 'string',
                                            'ClientCache': 'DISABLED'|'ENABLED',
                                            'CodecSpecification': 'RFC_6381'|'RFC_4281',
                                            'Destination': 'string',
                                            'DestinationSettings': {
                                                'S3Settings': {
                                                    'AccessControl': {
                                                        'CannedAcl':
                                                        'PUBLIC_READ'|'AUTHENTICATED_READ'|'BUCKET_OWNER_READ'
                                                        |'BUCKET_OWNER_FULL_CONTROL'
                                                    },
                                                    'Encryption': {
                                                        'EncryptionType':
                                                        'SERVER_SIDE_ENCRYPTION_S3'
                                                        |'SERVER_SIDE_ENCRYPTION_KMS',
                                                        'KmsKeyArn': 'string'
                                                    }
                                                }
                                            },
                                            'Encryption': {
                                                'ConstantInitializationVector': 'string',
                                                'EncryptionMethod': 'SAMPLE_AES'|'AES_CTR',
                                                'InitializationVectorInManifest':
                                                'INCLUDE'
                                                |'EXCLUDE',
                                                'SpekeKeyProvider': {
                                                    'CertificateArn': 'string',
                                                    'DashSignaledSystemIds': [
                                                        'string',
                                                    ],
                                                    'HlsSignaledSystemIds': [
                                                        'string',
                                                    ],
                                                    'ResourceId': 'string',
                                                    'Url': 'string'
                                                },
                                                'StaticKeyProvider': {
                                                    'KeyFormat': 'string',
                                                    'KeyFormatVersions': 'string',
                                                    'StaticKeyValue': 'string',
                                                    'Url': 'string'
                                                },
                                                'Type': 'SPEKE'|'STATIC_KEY'
                                            },
                                            'FragmentLength': 123,
                                            'ManifestCompression': 'GZIP'|'NONE',
                                            'ManifestDurationFormat': 'FLOATING_POINT'|'INTEGER',
                                            'MinBufferTime': 123,
                                            'MinFinalSegmentLength': 123.0,
                                            'MpdProfile': 'MAIN_PROFILE'|'ON_DEMAND_PROFILE',
                                            'SegmentControl': 'SINGLE_FILE'|'SEGMENTED_FILES',
                                            'SegmentLength': 123,
                                            'StreamInfResolution': 'INCLUDE'|'EXCLUDE',
                                            'WriteDashManifest': 'DISABLED'|'ENABLED',
                                            'WriteHlsManifest': 'DISABLED'|'ENABLED'
                                        },
                                        'DashIsoGroupSettings': {
                                            'AdditionalManifests': [
                                                {
                                                    'ManifestNameModifier': 'string',
                                                    'SelectedOutputs': [
                                                        'string',
                                                    ]
                                                },
                                            ],
                                            'BaseUrl': 'string',
                                            'Destination': 'string',
                                            'DestinationSettings': {
                                                'S3Settings': {
                                                    'AccessControl': {
                                                        'CannedAcl':
                                                        'PUBLIC_READ'|'AUTHENTICATED_READ'|'BUCKET_OWNER_READ'
                                                        |'BUCKET_OWNER_FULL_CONTROL'
                                                    },
                                                    'Encryption': {
                                                        'EncryptionType':
                                                        'SERVER_SIDE_ENCRYPTION_S3'
                                                        |'SERVER_SIDE_ENCRYPTION_KMS',
                                                        'KmsKeyArn': 'string'
                                                    }
                                                }
                                            },
                                            'Encryption': {
                                                'PlaybackDeviceCompatibility':
                                                'CENC_V1'
                                                |'UNENCRYPTED_SEI',
                                                'SpekeKeyProvider': {
                                                    'CertificateArn': 'string',
                                                    'ResourceId': 'string',
                                                    'SystemIds': [
                                                        'string',
                                                    ],
                                                    'Url': 'string'
                                                }
                                            },
                                            'FragmentLength': 123,
                                            'HbbtvCompliance': 'HBBTV_1_5'|'NONE',
                                            'MinBufferTime': 123,
                                            'MpdProfile': 'MAIN_PROFILE'|'ON_DEMAND_PROFILE',
                                            'SegmentControl': 'SINGLE_FILE'|'SEGMENTED_FILES',
                                            'SegmentLength': 123,
                                            'WriteSegmentTimelineInRepresentation':
                                            'ENABLED'|'DISABLED'
                                        },
                                        'FileGroupSettings': {
                                            'Destination': 'string',
                                            'DestinationSettings': {
                                                'S3Settings': {
                                                    'AccessControl': {
                                                        'CannedAcl':
                                                        'PUBLIC_READ'|'AUTHENTICATED_READ'|'BUCKET_OWNER_READ'
                                                        |'BUCKET_OWNER_FULL_CONTROL'
                                                    },
                                                    'Encryption': {
                                                        'EncryptionType':
                                                        'SERVER_SIDE_ENCRYPTION_S3'
                                                        |'SERVER_SIDE_ENCRYPTION_KMS',
                                                        'KmsKeyArn': 'string'
                                                    }
                                                }
                                            }
                                        },
                                        'HlsGroupSettings': {
                                            'AdMarkers': [
                                                'ELEMENTAL'|'ELEMENTAL_SCTE35',
                                            ],
                                            'AdditionalManifests': [
                                                {
                                                    'ManifestNameModifier': 'string',
                                                    'SelectedOutputs': [
                                                        'string',
                                                    ]
                                                },
                                            ],
                                            'BaseUrl': 'string',
                                            'CaptionLanguageMappings': [
                                                {
                                                    'CaptionChannel': 123,
                                                    'CustomLanguageCode': 'string',
                                                    'LanguageCode':
                                                    'ENG'|'SPA'|'FRA'|'DEU'|'GER'|'ZHO'|'ARA'|'HIN'|'JPN'|'RUS'|'POR'|'ITA'|'URD'|'VIE'|'KOR'|'PAN'|'ABK'|'AAR'|'AFR'|'AKA'|'SQI'|'AMH'|'ARG'|'HYE'|'ASM'|'AVA'|'AVE'|'AYM'|'AZE'|'BAM'|'BAK'|'EUS'|'BEL'|'BEN'|'BIH'|'BIS'|'BOS'|'BRE'|'BUL'|'MYA'|'CAT'|'KHM'|'CHA'|'CHE'|'NYA'|'CHU'|'CHV'|'COR'|'COS'|'CRE'|'HRV'|'CES'|'DAN'|'DIV'|'NLD'|'DZO'|'ENM'|'EPO'|'EST'|'EWE'|'FAO'|'FIJ'|'FIN'|'FRM'|'FUL'|'GLA'|'GLG'|'LUG'|'KAT'|'ELL'|'GRN'|'GUJ'|'HAT'|'HAU'|'HEB'|'HER'|'HMO'|'HUN'|'ISL'|'IDO'|'IBO'|'IND'|'INA'|'ILE'|'IKU'|'IPK'|'GLE'|'JAV'|'KAL'|'KAN'|'KAU'|'KAS'|'KAZ'|'KIK'|'KIN'|'KIR'|'KOM'|'KON'|'KUA'|'KUR'|'LAO'|'LAT'|'LAV'|'LIM'|'LIN'|'LIT'|'LUB'|'LTZ'|'MKD'|'MLG'|'MSA'|'MAL'|'MLT'|'GLV'|'MRI'|'MAR'|'MAH'|'MON'|'NAU'|'NAV'|'NDE'|'NBL'|'NDO'|'NEP'|'SME'|'NOR'|'NOB'|'NNO'|'OCI'|'OJI'|'ORI'|'ORM'|'OSS'|'PLI'|'FAS'|'POL'|'PUS'|'QUE'|'QAA'|'RON'|'ROH'|'RUN'|'SMO'|'SAG'|'SAN'|'SRD'|'SRB'|'SNA'|'III'|'SND'|'SIN'|'SLK'|'SLV'|'SOM'|'SOT'|'SUN'|'SWA'|'SSW'|'SWE'|'TGL'|'TAH'|'TGK'|'TAM'|'TAT'|'TEL'|'THA'|'BOD'|'TIR'|'TON'|'TSO'|'TSN'|'TUR'|'TUK'|'TWI'|'UIG'|'UKR'|'UZB'|'VEN'|'VOL'|'WLN'|'CYM'|'FRY'|'WOL'|'XHO'|'YID'|'YOR'|'ZHA'|'ZUL'|'ORJ'|'QPC'
                                                    |'TNG',
                                                    'LanguageDescription': 'string'
                                                },
                                            ],
                                            'CaptionLanguageSetting': 'INSERT'|'OMIT'|'NONE',
                                            'ClientCache': 'DISABLED'|'ENABLED',
                                            'CodecSpecification': 'RFC_6381'|'RFC_4281',
                                            'Destination': 'string',
                                            'DestinationSettings': {
                                                'S3Settings': {
                                                    'AccessControl': {
                                                        'CannedAcl':
                                                        'PUBLIC_READ'|'AUTHENTICATED_READ'|'BUCKET_OWNER_READ'
                                                        |'BUCKET_OWNER_FULL_CONTROL'
                                                    },
                                                    'Encryption': {
                                                        'EncryptionType':
                                                        'SERVER_SIDE_ENCRYPTION_S3'
                                                        |'SERVER_SIDE_ENCRYPTION_KMS',
                                                        'KmsKeyArn': 'string'
                                                    }
                                                }
                                            },
                                            'DirectoryStructure':
                                            'SINGLE_DIRECTORY'
                                            |'SUBDIRECTORY_PER_STREAM',
                                            'Encryption': {
                                                'ConstantInitializationVector': 'string',
                                                'EncryptionMethod': 'AES128'|'SAMPLE_AES',
                                                'InitializationVectorInManifest':
                                                'INCLUDE'
                                                |'EXCLUDE',
                                                'OfflineEncrypted': 'ENABLED'|'DISABLED',
                                                'SpekeKeyProvider': {
                                                    'CertificateArn': 'string',
                                                    'ResourceId': 'string',
                                                    'SystemIds': [
                                                        'string',
                                                    ],
                                                    'Url': 'string'
                                                },
                                                'StaticKeyProvider': {
                                                    'KeyFormat': 'string',
                                                    'KeyFormatVersions': 'string',
                                                    'StaticKeyValue': 'string',
                                                    'Url': 'string'
                                                },
                                                'Type': 'SPEKE'|'STATIC_KEY'
                                            },
                                            'ManifestCompression': 'GZIP'|'NONE',
                                            'ManifestDurationFormat': 'FLOATING_POINT'|'INTEGER',
                                            'MinFinalSegmentLength': 123.0,
                                            'MinSegmentLength': 123,
                                            'OutputSelection':
                                            'MANIFESTS_AND_SEGMENTS'
                                            |'SEGMENTS_ONLY',
                                            'ProgramDateTime': 'INCLUDE'|'EXCLUDE',
                                            'ProgramDateTimePeriod': 123,
                                            'SegmentControl': 'SINGLE_FILE'|'SEGMENTED_FILES',
                                            'SegmentLength': 123,
                                            'SegmentsPerSubdirectory': 123,
                                            'StreamInfResolution': 'INCLUDE'|'EXCLUDE',
                                            'TimedMetadataId3Frame': 'NONE'|'PRIV'|'TDRL',
                                            'TimedMetadataId3Period': 123,
                                            'TimestampDeltaMilliseconds': 123
                                        },
                                        'MsSmoothGroupSettings': {
                                            'AdditionalManifests': [
                                                {
                                                    'ManifestNameModifier': 'string',
                                                    'SelectedOutputs': [
                                                        'string',
                                                    ]
                                                },
                                            ],
                                            'AudioDeduplication':
                                            'COMBINE_DUPLICATE_STREAMS'
                                            |'NONE',
                                            'Destination': 'string',
                                            'DestinationSettings': {
                                                'S3Settings': {
                                                    'AccessControl': {
                                                        'CannedAcl':
                                                        'PUBLIC_READ'|'AUTHENTICATED_READ'|'BUCKET_OWNER_READ'
                                                        |'BUCKET_OWNER_FULL_CONTROL'
                                                    },
                                                    'Encryption': {
                                                        'EncryptionType':
                                                        'SERVER_SIDE_ENCRYPTION_S3'
                                                        |'SERVER_SIDE_ENCRYPTION_KMS',
                                                        'KmsKeyArn': 'string'
                                                    }
                                                }
                                            },
                                            'Encryption': {
                                                'SpekeKeyProvider': {
                                                    'CertificateArn': 'string',
                                                    'ResourceId': 'string',
                                                    'SystemIds': [
                                                        'string',
                                                    ],
                                                    'Url': 'string'
                                                }
                                            },
                                            'FragmentLength': 123,
                                            'ManifestEncoding': 'UTF8'|'UTF16'
                                        },
                                        'Type':
                                        'HLS_GROUP_SETTINGS'
                                        |'DASH_ISO_GROUP_SETTINGS'
                                        |'FILE_GROUP_SETTINGS'
                                        |'MS_SMOOTH_GROUP_SETTINGS'
                                        |'CMAF_GROUP_SETTINGS'
                                    },
                                    'Outputs': [
                                        {
                                            'AudioDescriptions': [
                                                {
                                                    'AudioNormalizationSettings': {
                                                        'Algorithm':
                                                        'ITU_BS_1770_1'|'ITU_BS_1770_2'|'ITU_BS_1770_3'
                                                        |'ITU_BS_1770_4',
                                                        'AlgorithmControl':
                                                        'CORRECT_AUDIO'
                                                        |'MEASURE_ONLY',
                                                        'CorrectionGateLevel': 123,
                                                        'LoudnessLogging': 'LOG'|'DONT_LOG',
                                                        'PeakCalculation': 'TRUE_PEAK'|'NONE',
                                                        'TargetLkfs': 123.0
                                                    },
                                                    'AudioSourceName': 'string',
                                                    'AudioType': 123,
                                                    'AudioTypeControl':
                                                    'FOLLOW_INPUT'
                                                    |'USE_CONFIGURED',
                                                    'CodecSettings': {
                                                        'AacSettings': {
                                                            'AudioDescriptionBroadcasterMix':
                                                            'BROADCASTER_MIXED_AD'
                                                            |'NORMAL',
                                                            'Bitrate': 123,
                                                            'CodecProfile': 'LC'|'HEV1'|'HEV2',
                                                            'CodingMode':
                                                            'AD_RECEIVER_MIX'|'CODING_MODE_1_0'|'CODING_MODE_1_1'|'CODING_MODE_2_0'
                                                            |'CODING_MODE_5_1',
                                                            'RateControlMode': 'CBR'|'VBR',
                                                            'RawFormat': 'LATM_LOAS'|'NONE',
                                                            'SampleRate': 123,
                                                            'Specification': 'MPEG2'|'MPEG4',
                                                            'VbrQuality':
                                                            'LOW'|'MEDIUM_LOW'|'MEDIUM_HIGH'
                                                            |'HIGH'
                                                        },
                                                        'Ac3Settings': {
                                                            'Bitrate': 123,
                                                            'BitstreamMode':
                                                            'COMPLETE_MAIN'|'COMMENTARY'|'DIALOGUE'|'EMERGENCY'|'HEARING_IMPAIRED'|'MUSIC_AND_EFFECTS'|'VISUALLY_IMPAIRED'
                                                            |'VOICE_OVER',
                                                            'CodingMode':
                                                            'CODING_MODE_1_0'|'CODING_MODE_1_1'|'CODING_MODE_2_0'
                                                            |'CODING_MODE_3_2_LFE',
                                                            'Dialnorm': 123,
                                                            'DynamicRangeCompressionProfile':
                                                            'FILM_STANDARD'
                                                            |'NONE',
                                                            'LfeFilter': 'ENABLED'|'DISABLED',
                                                            'MetadataControl':
                                                            'FOLLOW_INPUT'
                                                            |'USE_CONFIGURED',
                                                            'SampleRate': 123
                                                        },
                                                        'AiffSettings': {
                                                            'BitDepth': 123,
                                                            'Channels': 123,
                                                            'SampleRate': 123
                                                        },
                                                        'Codec':
                                                        'AAC'|'MP2'|'WAV'|'AIFF'|'AC3'|'EAC3'|'EAC3_ATMOS'
                                                        |'PASSTHROUGH',
                                                        'Eac3AtmosSettings': {
                                                            'Bitrate': 123,
                                                            'BitstreamMode': 'COMPLETE_MAIN',
                                                            'CodingMode': 'CODING_MODE_9_1_6',
                                                            'DialogueIntelligence':
                                                            'ENABLED'
                                                            |'DISABLED',
                                                            'DynamicRangeCompressionLine':
                                                            'NONE'|'FILM_STANDARD'|'FILM_LIGHT'|'MUSIC_STANDARD'|'MUSIC_LIGHT'
                                                            |'SPEECH',
                                                            'DynamicRangeCompressionRf':
                                                            'NONE'|'FILM_STANDARD'|'FILM_LIGHT'|'MUSIC_STANDARD'|'MUSIC_LIGHT'
                                                            |'SPEECH',
                                                            'LoRoCenterMixLevel': 123.0,
                                                            'LoRoSurroundMixLevel': 123.0,
                                                            'LtRtCenterMixLevel': 123.0,
                                                            'LtRtSurroundMixLevel': 123.0,
                                                            'MeteringMode':
                                                            'LEQ_A'|'ITU_BS_1770_1'|'ITU_BS_1770_2'|'ITU_BS_1770_3'
                                                            |'ITU_BS_1770_4',
                                                            'SampleRate': 123,
                                                            'SpeechThreshold': 123,
                                                            'StereoDownmix':
                                                            'NOT_INDICATED'|'STEREO'|'SURROUND'
                                                            |'DPL2',
                                                            'SurroundExMode':
                                                            'NOT_INDICATED'|'ENABLED'
                                                            |'DISABLED'
                                                        },
                                                        'Eac3Settings': {
                                                            'AttenuationControl':
                                                            'ATTENUATE_3_DB'
                                                            |'NONE',
                                                            'Bitrate': 123,
                                                            'BitstreamMode':
                                                            'COMPLETE_MAIN'|'COMMENTARY'|'EMERGENCY'|'HEARING_IMPAIRED'
                                                            |'VISUALLY_IMPAIRED',
                                                            'CodingMode':
                                                            'CODING_MODE_1_0'|'CODING_MODE_2_0'
                                                            |'CODING_MODE_3_2',
                                                            'DcFilter': 'ENABLED'|'DISABLED',
                                                            'Dialnorm': 123,
                                                            'DynamicRangeCompressionLine':
                                                            'NONE'|'FILM_STANDARD'|'FILM_LIGHT'|'MUSIC_STANDARD'|'MUSIC_LIGHT'
                                                            |'SPEECH',
                                                            'DynamicRangeCompressionRf':
                                                            'NONE'|'FILM_STANDARD'|'FILM_LIGHT'|'MUSIC_STANDARD'|'MUSIC_LIGHT'
                                                            |'SPEECH',
                                                            'LfeControl': 'LFE'|'NO_LFE',
                                                            'LfeFilter': 'ENABLED'|'DISABLED',
                                                            'LoRoCenterMixLevel': 123.0,
                                                            'LoRoSurroundMixLevel': 123.0,
                                                            'LtRtCenterMixLevel': 123.0,
                                                            'LtRtSurroundMixLevel': 123.0,
                                                            'MetadataControl':
                                                            'FOLLOW_INPUT'
                                                            |'USE_CONFIGURED',
                                                            'PassthroughControl':
                                                            'WHEN_POSSIBLE'
                                                            |'NO_PASSTHROUGH',
                                                            'PhaseControl':
                                                            'SHIFT_90_DEGREES'
                                                            |'NO_SHIFT',
                                                            'SampleRate': 123,
                                                            'StereoDownmix':
                                                            'NOT_INDICATED'|'LO_RO'|'LT_RT'
                                                            |'DPL2',
                                                            'SurroundExMode':
                                                            'NOT_INDICATED'|'ENABLED'
                                                            |'DISABLED',
                                                            'SurroundMode':
                                                            'NOT_INDICATED'|'ENABLED'
                                                            |'DISABLED'
                                                        },
                                                        'Mp2Settings': {
                                                            'Bitrate': 123,
                                                            'Channels': 123,
                                                            'SampleRate': 123
                                                        },
                                                        'WavSettings': {
                                                            'BitDepth': 123,
                                                            'Channels': 123,
                                                            'Format': 'RIFF'|'RF64',
                                                            'SampleRate': 123
                                                        }
                                                    },
                                                    'CustomLanguageCode': 'string',
                                                    'LanguageCode':
                                                    'ENG'|'SPA'|'FRA'|'DEU'|'GER'|'ZHO'|'ARA'|'HIN'|'JPN'|'RUS'|'POR'|'ITA'|'URD'|'VIE'|'KOR'|'PAN'|'ABK'|'AAR'|'AFR'|'AKA'|'SQI'|'AMH'|'ARG'|'HYE'|'ASM'|'AVA'|'AVE'|'AYM'|'AZE'|'BAM'|'BAK'|'EUS'|'BEL'|'BEN'|'BIH'|'BIS'|'BOS'|'BRE'|'BUL'|'MYA'|'CAT'|'KHM'|'CHA'|'CHE'|'NYA'|'CHU'|'CHV'|'COR'|'COS'|'CRE'|'HRV'|'CES'|'DAN'|'DIV'|'NLD'|'DZO'|'ENM'|'EPO'|'EST'|'EWE'|'FAO'|'FIJ'|'FIN'|'FRM'|'FUL'|'GLA'|'GLG'|'LUG'|'KAT'|'ELL'|'GRN'|'GUJ'|'HAT'|'HAU'|'HEB'|'HER'|'HMO'|'HUN'|'ISL'|'IDO'|'IBO'|'IND'|'INA'|'ILE'|'IKU'|'IPK'|'GLE'|'JAV'|'KAL'|'KAN'|'KAU'|'KAS'|'KAZ'|'KIK'|'KIN'|'KIR'|'KOM'|'KON'|'KUA'|'KUR'|'LAO'|'LAT'|'LAV'|'LIM'|'LIN'|'LIT'|'LUB'|'LTZ'|'MKD'|'MLG'|'MSA'|'MAL'|'MLT'|'GLV'|'MRI'|'MAR'|'MAH'|'MON'|'NAU'|'NAV'|'NDE'|'NBL'|'NDO'|'NEP'|'SME'|'NOR'|'NOB'|'NNO'|'OCI'|'OJI'|'ORI'|'ORM'|'OSS'|'PLI'|'FAS'|'POL'|'PUS'|'QUE'|'QAA'|'RON'|'ROH'|'RUN'|'SMO'|'SAG'|'SAN'|'SRD'|'SRB'|'SNA'|'III'|'SND'|'SIN'|'SLK'|'SLV'|'SOM'|'SOT'|'SUN'|'SWA'|'SSW'|'SWE'|'TGL'|'TAH'|'TGK'|'TAM'|'TAT'|'TEL'|'THA'|'BOD'|'TIR'|'TON'|'TSO'|'TSN'|'TUR'|'TUK'|'TWI'|'UIG'|'UKR'|'UZB'|'VEN'|'VOL'|'WLN'|'CYM'|'FRY'|'WOL'|'XHO'|'YID'|'YOR'|'ZHA'|'ZUL'|'ORJ'|'QPC'
                                                    |'TNG',
                                                    'LanguageCodeControl':
                                                    'FOLLOW_INPUT'
                                                    |'USE_CONFIGURED',
                                                    'RemixSettings': {
                                                        'ChannelMapping': {
                                                            'OutputChannels': [
                                                                {
                                                                    'InputChannels': [
                                                                        123,
                                                                    ]
                                                                },
                                                            ]
                                                        },
                                                        'ChannelsIn': 123,
                                                        'ChannelsOut': 123
                                                    },
                                                    'StreamName': 'string'
                                                },
                                            ],
                                            'CaptionDescriptions': [
                                                {
                                                    'CaptionSelectorName': 'string',
                                                    'CustomLanguageCode': 'string',
                                                    'DestinationSettings': {
                                                        'BurninDestinationSettings': {
                                                            'Alignment': 'CENTERED'|'LEFT',
                                                            'BackgroundColor':
                                                            'NONE'|'BLACK'
                                                            |'WHITE',
                                                            'BackgroundOpacity': 123,
                                                            'FontColor':
                                                            'WHITE'|'BLACK'|'YELLOW'|'RED'|'GREEN'
                                                            |'BLUE',
                                                            'FontOpacity': 123,
                                                            'FontResolution': 123,
                                                            'FontScript': 'AUTOMATIC'|'HANS'|'HANT',
                                                            'FontSize': 123,
                                                            'OutlineColor':
                                                            'BLACK'|'WHITE'|'YELLOW'|'RED'|'GREEN'
                                                            |'BLUE',
                                                            'OutlineSize': 123,
                                                            'ShadowColor': 'NONE'|'BLACK'|'WHITE',
                                                            'ShadowOpacity': 123,
                                                            'ShadowXOffset': 123,
                                                            'ShadowYOffset': 123,
                                                            'TeletextSpacing':
                                                            'FIXED_GRID'
                                                            |'PROPORTIONAL',
                                                            'XPosition': 123,
                                                            'YPosition': 123
                                                        },
                                                        'DestinationType':
                                                        'BURN_IN'|'DVB_SUB'|'EMBEDDED'|'EMBEDDED_PLUS_SCTE20'|'IMSC'|'SCTE20_PLUS_EMBEDDED'|'SCC'|'SRT'|'SMI'|'TELETEXT'|'TTML'
                                                        |'WEBVTT',
                                                        'DvbSubDestinationSettings': {
                                                            'Alignment': 'CENTERED'|'LEFT',
                                                            'BackgroundColor':
                                                            'NONE'|'BLACK'
                                                            |'WHITE',
                                                            'BackgroundOpacity': 123,
                                                            'FontColor':
                                                            'WHITE'|'BLACK'|'YELLOW'|'RED'|'GREEN'
                                                            |'BLUE',
                                                            'FontOpacity': 123,
                                                            'FontResolution': 123,
                                                            'FontScript': 'AUTOMATIC'|'HANS'|'HANT',
                                                            'FontSize': 123,
                                                            'OutlineColor':
                                                            'BLACK'|'WHITE'|'YELLOW'|'RED'|'GREEN'
                                                            |'BLUE',
                                                            'OutlineSize': 123,
                                                            'ShadowColor': 'NONE'|'BLACK'|'WHITE',
                                                            'ShadowOpacity': 123,
                                                            'ShadowXOffset': 123,
                                                            'ShadowYOffset': 123,
                                                            'SubtitlingType':
                                                            'HEARING_IMPAIRED'
                                                            |'STANDARD',
                                                            'TeletextSpacing':
                                                            'FIXED_GRID'
                                                            |'PROPORTIONAL',
                                                            'XPosition': 123,
                                                            'YPosition': 123
                                                        },
                                                        'EmbeddedDestinationSettings': {
                                                            'Destination608ChannelNumber': 123,
                                                            'Destination708ServiceNumber': 123
                                                        },
                                                        'ImscDestinationSettings': {
                                                            'StylePassthrough': 'ENABLED'|'DISABLED'
                                                        },
                                                        'SccDestinationSettings': {
                                                            'Framerate':
                                                            'FRAMERATE_23_97'|'FRAMERATE_24'|'FRAMERATE_25'|'FRAMERATE_29_97_DROPFRAME'
                                                            |'FRAMERATE_29_97_NON_DROPFRAME'
                                                        },
                                                        'TeletextDestinationSettings': {
                                                            'PageNumber': 'string',
                                                            'PageTypes': [
                                                                'PAGE_TYPE_INITIAL'
                                                                |'PAGE_TYPE_SUBTITLE'
                                                                |'PAGE_TYPE_ADDL_INFO'
                                                                |'PAGE_TYPE_PROGRAM_SCHEDULE'
                                                                |'PAGE_TYPE_HEARING_IMPAIRED_SUBTITLE',
                                                            ]
                                                        },
                                                        'TtmlDestinationSettings': {
                                                            'StylePassthrough': 'ENABLED'|'DISABLED'
                                                        }
                                                    },
                                                    'LanguageCode':
                                                    'ENG'|'SPA'|'FRA'|'DEU'|'GER'|'ZHO'|'ARA'|'HIN'|'JPN'|'RUS'|'POR'|'ITA'|'URD'|'VIE'|'KOR'|'PAN'|'ABK'|'AAR'|'AFR'|'AKA'|'SQI'|'AMH'|'ARG'|'HYE'|'ASM'|'AVA'|'AVE'|'AYM'|'AZE'|'BAM'|'BAK'|'EUS'|'BEL'|'BEN'|'BIH'|'BIS'|'BOS'|'BRE'|'BUL'|'MYA'|'CAT'|'KHM'|'CHA'|'CHE'|'NYA'|'CHU'|'CHV'|'COR'|'COS'|'CRE'|'HRV'|'CES'|'DAN'|'DIV'|'NLD'|'DZO'|'ENM'|'EPO'|'EST'|'EWE'|'FAO'|'FIJ'|'FIN'|'FRM'|'FUL'|'GLA'|'GLG'|'LUG'|'KAT'|'ELL'|'GRN'|'GUJ'|'HAT'|'HAU'|'HEB'|'HER'|'HMO'|'HUN'|'ISL'|'IDO'|'IBO'|'IND'|'INA'|'ILE'|'IKU'|'IPK'|'GLE'|'JAV'|'KAL'|'KAN'|'KAU'|'KAS'|'KAZ'|'KIK'|'KIN'|'KIR'|'KOM'|'KON'|'KUA'|'KUR'|'LAO'|'LAT'|'LAV'|'LIM'|'LIN'|'LIT'|'LUB'|'LTZ'|'MKD'|'MLG'|'MSA'|'MAL'|'MLT'|'GLV'|'MRI'|'MAR'|'MAH'|'MON'|'NAU'|'NAV'|'NDE'|'NBL'|'NDO'|'NEP'|'SME'|'NOR'|'NOB'|'NNO'|'OCI'|'OJI'|'ORI'|'ORM'|'OSS'|'PLI'|'FAS'|'POL'|'PUS'|'QUE'|'QAA'|'RON'|'ROH'|'RUN'|'SMO'|'SAG'|'SAN'|'SRD'|'SRB'|'SNA'|'III'|'SND'|'SIN'|'SLK'|'SLV'|'SOM'|'SOT'|'SUN'|'SWA'|'SSW'|'SWE'|'TGL'|'TAH'|'TGK'|'TAM'|'TAT'|'TEL'|'THA'|'BOD'|'TIR'|'TON'|'TSO'|'TSN'|'TUR'|'TUK'|'TWI'|'UIG'|'UKR'|'UZB'|'VEN'|'VOL'|'WLN'|'CYM'|'FRY'|'WOL'|'XHO'|'YID'|'YOR'|'ZHA'|'ZUL'|'ORJ'|'QPC'
                                                    |'TNG',
                                                    'LanguageDescription': 'string'
                                                },
                                            ],
                                            'ContainerSettings': {
                                                'Container':
                                                'F4V'|'ISMV'
                                                |'M2TS'
                                                |'M3U8'
                                                |'CMFC'
                                                |'MOV'|'MP4'
                                                |'MPD'|'MXF'
                                                |'RAW',
                                                'F4vSettings': {
                                                    'MoovPlacement': 'PROGRESSIVE_DOWNLOAD'|'NORMAL'
                                                },
                                                'M2tsSettings': {
                                                    'AudioBufferModel': 'DVB'|'ATSC',
                                                    'AudioFramesPerPes': 123,
                                                    'AudioPids': [
                                                        123,
                                                    ],
                                                    'Bitrate': 123,
                                                    'BufferModel': 'MULTIPLEX'|'NONE',
                                                    'DvbNitSettings': {
                                                        'NetworkId': 123,
                                                        'NetworkName': 'string',
                                                        'NitInterval': 123
                                                    },
                                                    'DvbSdtSettings': {
                                                        'OutputSdt':
                                                        'SDT_FOLLOW'|'SDT_FOLLOW_IF_PRESENT'|'SDT_MANUAL'
                                                        |'SDT_NONE',
                                                        'SdtInterval': 123,
                                                        'ServiceName': 'string',
                                                        'ServiceProviderName': 'string'
                                                    },
                                                    'DvbSubPids': [
                                                        123,
                                                    ],
                                                    'DvbTdtSettings': {
                                                        'TdtInterval': 123
                                                    },
                                                    'DvbTeletextPid': 123,
                                                    'EbpAudioInterval':
                                                    'VIDEO_AND_FIXED_INTERVALS'
                                                    |'VIDEO_INTERVAL',
                                                    'EbpPlacement':
                                                    'VIDEO_AND_AUDIO_PIDS'
                                                    |'VIDEO_PID',
                                                    'EsRateInPes': 'INCLUDE'|'EXCLUDE',
                                                    'ForceTsVideoEbpOrder': 'FORCE'|'DEFAULT',
                                                    'FragmentTime': 123.0,
                                                    'MaxPcrInterval': 123,
                                                    'MinEbpInterval': 123,
                                                    'NielsenId3': 'INSERT'|'NONE',
                                                    'NullPacketBitrate': 123.0,
                                                    'PatInterval': 123,
                                                    'PcrControl':
                                                    'PCR_EVERY_PES_PACKET'
                                                    |'CONFIGURED_PCR_PERIOD',
                                                    'PcrPid': 123,
                                                    'PmtInterval': 123,
                                                    'PmtPid': 123,
                                                    'PrivateMetadataPid': 123,
                                                    'ProgramNumber': 123,
                                                    'RateMode': 'VBR'|'CBR',
                                                    'Scte35Esam': {
                                                        'Scte35EsamPid': 123
                                                    },
                                                    'Scte35Pid': 123,
                                                    'Scte35Source': 'PASSTHROUGH'|'NONE',
                                                    'SegmentationMarkers':
                                                    'NONE'|'RAI_SEGSTART'|'RAI_ADAPT'|'PSI_SEGSTART'|'EBP'
                                                    |'EBP_LEGACY',
                                                    'SegmentationStyle':
                                                    'MAINTAIN_CADENCE'
                                                    |'RESET_CADENCE',
                                                    'SegmentationTime': 123.0,
                                                    'TimedMetadataPid': 123,
                                                    'TransportStreamId': 123,
                                                    'VideoPid': 123
                                                },
                                                'M3u8Settings': {
                                                    'AudioFramesPerPes': 123,
                                                    'AudioPids': [
                                                        123,
                                                    ],
                                                    'NielsenId3': 'INSERT'|'NONE',
                                                    'PatInterval': 123,
                                                    'PcrControl':
                                                    'PCR_EVERY_PES_PACKET'
                                                    |'CONFIGURED_PCR_PERIOD',
                                                    'PcrPid': 123,
                                                    'PmtInterval': 123,
                                                    'PmtPid': 123,
                                                    'PrivateMetadataPid': 123,
                                                    'ProgramNumber': 123,
                                                    'Scte35Pid': 123,
                                                    'Scte35Source': 'PASSTHROUGH'|'NONE',
                                                    'TimedMetadata': 'PASSTHROUGH'|'NONE',
                                                    'TimedMetadataPid': 123,
                                                    'TransportStreamId': 123,
                                                    'VideoPid': 123
                                                },
                                                'MovSettings': {
                                                    'ClapAtom': 'INCLUDE'|'EXCLUDE',
                                                    'CslgAtom': 'INCLUDE'|'EXCLUDE',
                                                    'Mpeg2FourCCControl': 'XDCAM'|'MPEG',
                                                    'PaddingControl': 'OMNEON'|'NONE',
                                                    'Reference': 'SELF_CONTAINED'|'EXTERNAL'
                                                },
                                                'Mp4Settings': {
                                                    'CslgAtom': 'INCLUDE'|'EXCLUDE',
                                                    'FreeSpaceBox': 'INCLUDE'|'EXCLUDE',
                                                    'MoovPlacement':
                                                    'PROGRESSIVE_DOWNLOAD'
                                                    |'NORMAL',
                                                    'Mp4MajorBrand': 'string'
                                                },
                                                'MpdSettings': {
                                                    'CaptionContainerType': 'RAW'|'FRAGMENTED_MP4',
                                                    'Scte35Esam': 'INSERT'|'NONE',
                                                    'Scte35Source': 'PASSTHROUGH'|'NONE'
                                                }
                                            },
                                            'Extension': 'string',
                                            'NameModifier': 'string',
                                            'OutputSettings': {
                                                'HlsSettings': {
                                                    'AudioGroupId': 'string',
                                                    'AudioOnlyContainer': 'AUTOMATIC'|'M2TS',
                                                    'AudioRenditionSets': 'string',
                                                    'AudioTrackType':
                                                    'ALTERNATE_AUDIO_AUTO_SELECT_DEFAULT'|'ALTERNATE_AUDIO_AUTO_SELECT'|'ALTERNATE_AUDIO_NOT_AUTO_SELECT'
                                                    |'AUDIO_ONLY_VARIANT_STREAM',
                                                    'IFrameOnlyManifest': 'INCLUDE'|'EXCLUDE',
                                                    'SegmentModifier': 'string'
                                                }
                                            },
                                            'Preset': 'string',
                                            'VideoDescription': {
                                                'AfdSignaling': 'NONE'|'AUTO'|'FIXED',
                                                'AntiAlias': 'DISABLED'|'ENABLED',
                                                'CodecSettings': {
                                                    'Codec':
                                                    'FRAME_CAPTURE'|'H_264'|'H_265'|'MPEG2'
                                                    |'PRORES',
                                                    'FrameCaptureSettings': {
                                                        'FramerateDenominator': 123,
                                                        'FramerateNumerator': 123,
                                                        'MaxCaptures': 123,
                                                        'Quality': 123
                                                    },
                                                    'H264Settings': {
                                                        'AdaptiveQuantization':
                                                        'OFF'|'LOW'|'MEDIUM'|'HIGH'|'HIGHER'
                                                        |'MAX',
                                                        'Bitrate': 123,
                                                        'CodecLevel':
                                                        'AUTO'|'LEVEL_1'|'LEVEL_1_1'|'LEVEL_1_2'|'LEVEL_1_3'|'LEVEL_2'|'LEVEL_2_1'|'LEVEL_2_2'|'LEVEL_3'|'LEVEL_3_1'|'LEVEL_3_2'|'LEVEL_4'|'LEVEL_4_1'|'LEVEL_4_2'|'LEVEL_5'|'LEVEL_5_1'
                                                        |'LEVEL_5_2',
                                                        'CodecProfile':
                                                        'BASELINE'|'HIGH'|'HIGH_10BIT'|'HIGH_422'|'HIGH_422_10BIT'
                                                        |'MAIN',
                                                        'DynamicSubGop': 'ADAPTIVE'|'STATIC',
                                                        'EntropyEncoding': 'CABAC'|'CAVLC',
                                                        'FieldEncoding': 'PAFF'|'FORCE_FIELD',
                                                        'FlickerAdaptiveQuantization':
                                                        'DISABLED'
                                                        |'ENABLED',
                                                        'FramerateControl':
                                                        'INITIALIZE_FROM_SOURCE'
                                                        |'SPECIFIED',
                                                        'FramerateConversionAlgorithm':
                                                        'DUPLICATE_DROP'
                                                        |'INTERPOLATE',
                                                        'FramerateDenominator': 123,
                                                        'FramerateNumerator': 123,
                                                        'GopBReference': 'DISABLED'|'ENABLED',
                                                        'GopClosedCadence': 123,
                                                        'GopSize': 123.0,
                                                        'GopSizeUnits': 'FRAMES'|'SECONDS',
                                                        'HrdBufferInitialFillPercentage': 123,
                                                        'HrdBufferSize': 123,
                                                        'InterlaceMode':
                                                        'PROGRESSIVE'|'TOP_FIELD'|'BOTTOM_FIELD'|'FOLLOW_TOP_FIELD'
                                                        |'FOLLOW_BOTTOM_FIELD',
                                                        'MaxBitrate': 123,
                                                        'MinIInterval': 123,
                                                        'NumberBFramesBetweenReferenceFrames': 123,
                                                        'NumberReferenceFrames': 123,
                                                        'ParControl':
                                                        'INITIALIZE_FROM_SOURCE'
                                                        |'SPECIFIED',
                                                        'ParDenominator': 123,
                                                        'ParNumerator': 123,
                                                        'QualityTuningLevel':
                                                        'SINGLE_PASS'|'SINGLE_PASS_HQ'
                                                        |'MULTI_PASS_HQ',
                                                        'QvbrSettings': {
                                                            'MaxAverageBitrate': 123,
                                                            'QvbrQualityLevel': 123
                                                        },
                                                        'RateControlMode': 'VBR'|'CBR'|'QVBR',
                                                        'RepeatPps': 'DISABLED'|'ENABLED',
                                                        'SceneChangeDetect':
                                                        'DISABLED'|'ENABLED'
                                                        |'TRANSITION_DETECTION',
                                                        'Slices': 123,
                                                        'SlowPal': 'DISABLED'|'ENABLED',
                                                        'Softness': 123,
                                                        'SpatialAdaptiveQuantization':
                                                        'DISABLED'
                                                        |'ENABLED',
                                                        'Syntax': 'DEFAULT'|'RP2027',
                                                        'Telecine': 'NONE'|'SOFT'|'HARD',
                                                        'TemporalAdaptiveQuantization':
                                                        'DISABLED'
                                                        |'ENABLED',
                                                        'UnregisteredSeiTimecode':
                                                        'DISABLED'
                                                        |'ENABLED'
                                                    },
                                                    'H265Settings': {
                                                        'AdaptiveQuantization':
                                                        'OFF'|'LOW'|'MEDIUM'|'HIGH'|'HIGHER'
                                                        |'MAX',
                                                        'AlternateTransferFunctionSei':
                                                        'DISABLED'
                                                        |'ENABLED',
                                                        'Bitrate': 123,
                                                        'CodecLevel':
                                                        'AUTO'|'LEVEL_1'|'LEVEL_2'|'LEVEL_2_1'|'LEVEL_3'|'LEVEL_3_1'|'LEVEL_4'|'LEVEL_4_1'|'LEVEL_5'|'LEVEL_5_1'|'LEVEL_5_2'|'LEVEL_6'|'LEVEL_6_1'
                                                        |'LEVEL_6_2',
                                                        'CodecProfile':
                                                        'MAIN_MAIN'|'MAIN_HIGH'|'MAIN10_MAIN'|'MAIN10_HIGH'|'MAIN_422_8BIT_MAIN'|'MAIN_422_8BIT_HIGH'|'MAIN_422_10BIT_MAIN'
                                                        |'MAIN_422_10BIT_HIGH',
                                                        'DynamicSubGop': 'ADAPTIVE'|'STATIC',
                                                        'FlickerAdaptiveQuantization':
                                                        'DISABLED'
                                                        |'ENABLED',
                                                        'FramerateControl':
                                                        'INITIALIZE_FROM_SOURCE'
                                                        |'SPECIFIED',
                                                        'FramerateConversionAlgorithm':
                                                        'DUPLICATE_DROP'
                                                        |'INTERPOLATE',
                                                        'FramerateDenominator': 123,
                                                        'FramerateNumerator': 123,
                                                        'GopBReference': 'DISABLED'|'ENABLED',
                                                        'GopClosedCadence': 123,
                                                        'GopSize': 123.0,
                                                        'GopSizeUnits': 'FRAMES'|'SECONDS',
                                                        'HrdBufferInitialFillPercentage': 123,
                                                        'HrdBufferSize': 123,
                                                        'InterlaceMode':
                                                        'PROGRESSIVE'|'TOP_FIELD'|'BOTTOM_FIELD'|'FOLLOW_TOP_FIELD'
                                                        |'FOLLOW_BOTTOM_FIELD',
                                                        'MaxBitrate': 123,
                                                        'MinIInterval': 123,
                                                        'NumberBFramesBetweenReferenceFrames': 123,
                                                        'NumberReferenceFrames': 123,
                                                        'ParControl':
                                                        'INITIALIZE_FROM_SOURCE'
                                                        |'SPECIFIED',
                                                        'ParDenominator': 123,
                                                        'ParNumerator': 123,
                                                        'QualityTuningLevel':
                                                        'SINGLE_PASS'|'SINGLE_PASS_HQ'
                                                        |'MULTI_PASS_HQ',
                                                        'QvbrSettings': {
                                                            'MaxAverageBitrate': 123,
                                                            'QvbrQualityLevel': 123
                                                        },
                                                        'RateControlMode': 'VBR'|'CBR'|'QVBR',
                                                        'SampleAdaptiveOffsetFilterMode':
                                                        'DEFAULT'|'ADAPTIVE'
                                                        |'OFF',
                                                        'SceneChangeDetect':
                                                        'DISABLED'|'ENABLED'
                                                        |'TRANSITION_DETECTION',
                                                        'Slices': 123,
                                                        'SlowPal': 'DISABLED'|'ENABLED',
                                                        'SpatialAdaptiveQuantization':
                                                        'DISABLED'
                                                        |'ENABLED',
                                                        'Telecine': 'NONE'|'SOFT'|'HARD',
                                                        'TemporalAdaptiveQuantization':
                                                        'DISABLED'
                                                        |'ENABLED',
                                                        'TemporalIds': 'DISABLED'|'ENABLED',
                                                        'Tiles': 'DISABLED'|'ENABLED',
                                                        'UnregisteredSeiTimecode':
                                                        'DISABLED'
                                                        |'ENABLED',
                                                        'WriteMp4PackagingType': 'HVC1'|'HEV1'
                                                    },
                                                    'Mpeg2Settings': {
                                                        'AdaptiveQuantization':
                                                        'OFF'|'LOW'|'MEDIUM'
                                                        |'HIGH',
                                                        'Bitrate': 123,
                                                        'CodecLevel':
                                                        'AUTO'|'LOW'|'MAIN'|'HIGH1440'
                                                        |'HIGH',
                                                        'CodecProfile': 'MAIN'|'PROFILE_422',
                                                        'DynamicSubGop': 'ADAPTIVE'|'STATIC',
                                                        'FramerateControl':
                                                        'INITIALIZE_FROM_SOURCE'
                                                        |'SPECIFIED',
                                                        'FramerateConversionAlgorithm':
                                                        'DUPLICATE_DROP'
                                                        |'INTERPOLATE',
                                                        'FramerateDenominator': 123,
                                                        'FramerateNumerator': 123,
                                                        'GopClosedCadence': 123,
                                                        'GopSize': 123.0,
                                                        'GopSizeUnits': 'FRAMES'|'SECONDS',
                                                        'HrdBufferInitialFillPercentage': 123,
                                                        'HrdBufferSize': 123,
                                                        'InterlaceMode':
                                                        'PROGRESSIVE'|'TOP_FIELD'|'BOTTOM_FIELD'|'FOLLOW_TOP_FIELD'
                                                        |'FOLLOW_BOTTOM_FIELD',
                                                        'IntraDcPrecision':
                                                        'AUTO'|'INTRA_DC_PRECISION_8'|'INTRA_DC_PRECISION_9'|'INTRA_DC_PRECISION_10'
                                                        |'INTRA_DC_PRECISION_11',
                                                        'MaxBitrate': 123,
                                                        'MinIInterval': 123,
                                                        'NumberBFramesBetweenReferenceFrames': 123,
                                                        'ParControl':
                                                        'INITIALIZE_FROM_SOURCE'
                                                        |'SPECIFIED',
                                                        'ParDenominator': 123,
                                                        'ParNumerator': 123,
                                                        'QualityTuningLevel':
                                                        'SINGLE_PASS'
                                                        |'MULTI_PASS',
                                                        'RateControlMode': 'VBR'|'CBR',
                                                        'SceneChangeDetect': 'DISABLED'|'ENABLED',
                                                        'SlowPal': 'DISABLED'|'ENABLED',
                                                        'Softness': 123,
                                                        'SpatialAdaptiveQuantization':
                                                        'DISABLED'
                                                        |'ENABLED',
                                                        'Syntax': 'DEFAULT'|'D_10',
                                                        'Telecine': 'NONE'|'SOFT'|'HARD',
                                                        'TemporalAdaptiveQuantization':
                                                        'DISABLED'
                                                        |'ENABLED'
                                                    },
                                                    'ProresSettings': {
                                                        'CodecProfile':
                                                        'APPLE_PRORES_422'|'APPLE_PRORES_422_HQ'|'APPLE_PRORES_422_LT'
                                                        |'APPLE_PRORES_422_PROXY',
                                                        'FramerateControl':
                                                        'INITIALIZE_FROM_SOURCE'
                                                        |'SPECIFIED',
                                                        'FramerateConversionAlgorithm':
                                                        'DUPLICATE_DROP'
                                                        |'INTERPOLATE',
                                                        'FramerateDenominator': 123,
                                                        'FramerateNumerator': 123,
                                                        'InterlaceMode':
                                                        'PROGRESSIVE'|'TOP_FIELD'|'BOTTOM_FIELD'|'FOLLOW_TOP_FIELD'
                                                        |'FOLLOW_BOTTOM_FIELD',
                                                        'ParControl':
                                                        'INITIALIZE_FROM_SOURCE'
                                                        |'SPECIFIED',
                                                        'ParDenominator': 123,
                                                        'ParNumerator': 123,
                                                        'SlowPal': 'DISABLED'|'ENABLED',
                                                        'Telecine': 'NONE'|'HARD'
                                                    }
                                                },
                                                'ColorMetadata': 'IGNORE'|'INSERT',
                                                'Crop': {
                                                    'Height': 123,
                                                    'Width': 123,
                                                    'X': 123,
                                                    'Y': 123
                                                },
                                                'DropFrameTimecode': 'DISABLED'|'ENABLED',
                                                'FixedAfd': 123,
                                                'Height': 123,
                                                'Position': {
                                                    'Height': 123,
                                                    'Width': 123,
                                                    'X': 123,
                                                    'Y': 123
                                                },
                                                'RespondToAfd': 'NONE'|'RESPOND'|'PASSTHROUGH',
                                                'ScalingBehavior': 'DEFAULT'|'STRETCH_TO_OUTPUT',
                                                'Sharpness': 123,
                                                'TimecodeInsertion': 'DISABLED'|'PIC_TIMING_SEI',
                                                'VideoPreprocessors': {
                                                    'ColorCorrector': {
                                                        'Brightness': 123,
                                                        'ColorSpaceConversion':
                                                        'NONE'|'FORCE_601'|'FORCE_709'|'FORCE_HDR10'
                                                        |'FORCE_HLG_2020',
                                                        'Contrast': 123,
                                                        'Hdr10Metadata': {
                                                            'BluePrimaryX': 123,
                                                            'BluePrimaryY': 123,
                                                            'GreenPrimaryX': 123,
                                                            'GreenPrimaryY': 123,
                                                            'MaxContentLightLevel': 123,
                                                            'MaxFrameAverageLightLevel': 123,
                                                            'MaxLuminance': 123,
                                                            'MinLuminance': 123,
                                                            'RedPrimaryX': 123,
                                                            'RedPrimaryY': 123,
                                                            'WhitePointX': 123,
                                                            'WhitePointY': 123
                                                        },
                                                        'Hue': 123,
                                                        'Saturation': 123
                                                    },
                                                    'Deinterlacer': {
                                                        'Algorithm':
                                                        'INTERPOLATE'|'INTERPOLATE_TICKER'|'BLEND'
                                                        |'BLEND_TICKER',
                                                        'Control': 'FORCE_ALL_FRAMES'|'NORMAL',
                                                        'Mode':
                                                        'DEINTERLACE'|'INVERSE_TELECINE'
                                                        |'ADAPTIVE'
                                                    },
                                                    'DolbyVision': {
                                                        'L6Metadata': {
                                                            'MaxCll': 123,
                                                            'MaxFall': 123
                                                        },
                                                        'L6Mode':
                                                        'PASSTHROUGH'|'RECALCULATE'
                                                        |'SPECIFY',
                                                        'Profile': 'PROFILE_5'
                                                    },
                                                    'ImageInserter': {
                                                        'InsertableImages': [
                                                            {
                                                                'Duration': 123,
                                                                'FadeIn': 123,
                                                                'FadeOut': 123,
                                                                'Height': 123,
                                                                'ImageInserterInput': 'string',
                                                                'ImageX': 123,
                                                                'ImageY': 123,
                                                                'Layer': 123,
                                                                'Opacity': 123,
                                                                'StartTime': 'string',
                                                                'Width': 123
                                                            },
                                                        ]
                                                    },
                                                    'NoiseReducer': {
                                                        'Filter':
                                                        'BILATERAL'|'MEAN'|'GAUSSIAN'|'LANCZOS'|'SHARPEN'|'CONSERVE'|'SPATIAL'
                                                        |'TEMPORAL',
                                                        'FilterSettings': {
                                                            'Strength': 123
                                                        },
                                                        'SpatialFilterSettings': {
                                                            'PostFilterSharpenStrength': 123,
                                                            'Speed': 123,
                                                            'Strength': 123
                                                        },
                                                        'TemporalFilterSettings': {
                                                            'AggressiveMode': 123,
                                                            'Speed': 123,
                                                            'Strength': 123
                                                        }
                                                    },
                                                    'TimecodeBurnin': {
                                                        'FontSize': 123,
                                                        'Position':
                                                        'TOP_CENTER'|'TOP_LEFT'|'TOP_RIGHT'|'MIDDLE_LEFT'|'MIDDLE_CENTER'|'MIDDLE_RIGHT'|'BOTTOM_LEFT'|'BOTTOM_CENTER'
                                                        |'BOTTOM_RIGHT',
                                                        'Prefix': 'string'
                                                    }
                                                },
                                                'Width': 123
                                            }
                                        },
                                    ]
                                },
                            ],
                            'TimecodeConfig': {
                                'Anchor': 'string',
                                'Source': 'EMBEDDED'|'ZEROBASED'|'SPECIFIEDSTART',
                                'Start': 'string',
                                'TimestampOffset': 'string'
                            },
                            'TimedMetadataInsertion': {
                                'Id3Insertions': [
                                    {
                                        'Id3': 'string',
                                        'Timecode': 'string'
                                    },
                                ]
                            }
                        },
                        'StatusUpdateInterval':
                        'SECONDS_10'|'SECONDS_12'|'SECONDS_15'|'SECONDS_20'
                        |'SECONDS_30'|'SECONDS_60'|'SECONDS_120'|'SECONDS_180'
                        |'SECONDS_240'|'SECONDS_300'|'SECONDS_360'|'SECONDS_420'
                        |'SECONDS_480'|'SECONDS_540'|'SECONDS_600',
                        'Type': 'SYSTEM'|'CUSTOM'
                    },
                ],

            }
          **Response Structure**

          - *(dict) --*

            - **JobTemplates** *(list) --* List of Job templates.

              - *(dict) --* A job template is a pre-made set of encoding instructions that you can
              use to quickly create a job.

                - **AccelerationSettings** *(dict) --* Accelerated transcoding can significantly
                speed up jobs with long, visually complex content.

                  - **Mode** *(string) --* Specify the conditions when the service will run your job
                  with accelerated transcoding.

                - **Arn** *(string) --* An identifier for this resource that is unique within all of
                AWS.

                - **Category** *(string) --* An optional category you create to organize your job
                templates.

                - **CreatedAt** *(datetime) --* The timestamp in epoch seconds for Job template
                creation.

                - **Description** *(string) --* An optional description you create for each job
                template.

                - **LastUpdated** *(datetime) --* The timestamp in epoch seconds when the Job
                template was last updated.

                - **Name** *(string) --* A name you create for each job template. Each name must be
                unique within your account.

                - **Priority** *(integer) --* Relative priority on the job.

                - **Queue** *(string) --* Optional. The queue that jobs created from this template
                are assigned to. If you don't specify this, jobs will go to the default queue.

                - **Settings** *(dict) --* JobTemplateSettings contains all the transcode settings
                saved in the template that will be applied to jobs created from it.

                  - **AdAvailOffset** *(integer) --* When specified, this offset (in milliseconds)
                  is added to the input Ad Avail PTS time.

                  - **AvailBlanking** *(dict) --* Settings for ad avail blanking. Video can be
                  blanked or overlaid with an image, and audio muted during SCTE-35 triggered ad
                  avails.

                    - **AvailBlankingImage** *(string) --* Blanking image to be used. Leave empty
                    for solid black. Only bmp and png images are supported.

                  - **Esam** *(dict) --* Settings for Event Signaling And Messaging (ESAM).

                    - **ManifestConfirmConditionNotification** *(dict) --* Specifies an ESAM
                    ManifestConfirmConditionNotification XML as per OC-SP-ESAM-API-I03-131025. The
                    transcoder uses the manifest conditioning instructions that you provide in the
                    setting MCC XML (mccXml).

                      - **MccXml** *(string) --* Provide your ESAM
                      ManifestConfirmConditionNotification XML document inside your JSON job
                      settings. Form the XML document as per OC-SP-ESAM-API-I03-131025. The
                      transcoder will use the Manifest Conditioning instructions in the message that
                      you supply.

                    - **ResponseSignalPreroll** *(integer) --* Specifies the stream distance, in
                    milliseconds, between the SCTE 35 messages that the transcoder places and the
                    splice points that they refer to. If the time between the start of the asset and
                    the SCTE-35 message is less than this value, then the transcoder places the
                    SCTE-35 marker at the beginning of the stream.

                    - **SignalProcessingNotification** *(dict) --* Specifies an ESAM
                    SignalProcessingNotification XML as per OC-SP-ESAM-API-I03-131025. The
                    transcoder uses the signal processing instructions that you provide in the
                    setting SCC XML (sccXml).

                      - **SccXml** *(string) --* Provide your ESAM SignalProcessingNotification XML
                      document inside your JSON job settings. Form the XML document as per
                      OC-SP-ESAM-API-I03-131025. The transcoder will use the signal processing
                      instructions in the message that you supply. Provide your ESAM
                      SignalProcessingNotification XML document inside your JSON job settings. For
                      your MPEG2-TS file outputs, if you want the service to place SCTE-35 markers
                      at the insertion points you specify in the XML document, you must also enable
                      SCTE-35 ESAM (scte35Esam). Note that you can either specify an ESAM XML
                      document or enable SCTE-35 passthrough. You can't do both.

                  - **Inputs** *(list) --* Use Inputs (inputs) to define the source file used in the
                  transcode job. There can only be one input in a job template. Using the API, you
                  can include multiple inputs when referencing a job template.

                    - *(dict) --* Specified video input in a template.

                      - **AudioSelectorGroups** *(dict) --* Specifies set of audio selectors within
                      an input to combine. An input may have multiple audio selector groups. See
                      "Audio Selector Group":#inputs-audio_selector_group for more information.

                        - *(string) --*

                          - *(dict) --* Group of Audio Selectors

                            - **AudioSelectorNames** *(list) --* Name of an Audio Selector within
                            the same input to include in the group. Audio selector names are
                            standardized, based on their order within the input (e.g., "Audio
                            Selector 1"). The audio selector name parameter can be repeated to add
                            any number of audio selectors to the group.

                              - *(string) --*

                      - **AudioSelectors** *(dict) --* Use Audio selectors (AudioSelectors) to
                      specify a track or set of tracks from the input that you will use in your
                      outputs. You can use mutiple Audio selectors per input.

                        - *(string) --*

                          - *(dict) --* Selector for Audio

                            - **CustomLanguageCode** *(string) --* Selects a specific language code
                            from within an audio source, using the ISO 639-2 or ISO 639-3
                            three-letter language code

                            - **DefaultSelection** *(string) --* Enable this setting on one audio
                            selector to set it as the default for the job. The service uses this
                            default for outputs where it can't find the specified input audio. If
                            you don't set a default, those outputs have no audio.

                            - **ExternalAudioFileInput** *(string) --* Specifies audio data from an
                            external file source.

                            - **LanguageCode** *(string) --* Selects a specific language code from
                            within an audio source.

                            - **Offset** *(integer) --* Specifies a time delta in milliseconds to
                            offset the audio from the input video.

                            - **Pids** *(list) --* Selects a specific PID from within an audio
                            source (e.g. 257 selects PID 0x101).

                              - *(integer) --*

                            - **ProgramSelection** *(integer) --* Use this setting for input streams
                            that contain Dolby E, to have the service extract specific program data
                            from the track. To select multiple programs, create multiple selectors
                            with the same Track and different Program numbers. In the console, this
                            setting is visible when you set Selector type to Track. Choose the
                            program number from the dropdown list. If you are sending a JSON file,
                            provide the program ID, which is part of the audio metadata. If your
                            input file has incorrect metadata, you can choose All channels instead
                            of a program number to have the service ignore the program IDs and
                            include all the programs in the track.

                            - **RemixSettings** *(dict) --* Use these settings to reorder the audio
                            channels of one input to match those of another input. This allows you
                            to combine the two files into a single output, one after the other.

                              - **ChannelMapping** *(dict) --* Channel mapping (ChannelMapping)
                              contains the group of fields that hold the remixing value for each
                              channel. Units are in dB. Acceptable values are within the range from
                              -60 (mute) through 6. A setting of 0 passes the input channel
                              unchanged to the output channel (no attenuation or amplification).

                                - **OutputChannels** *(list) --* List of output channels

                                  - *(dict) --* OutputChannel mapping settings.

                                    - **InputChannels** *(list) --* List of input channels

                                      - *(integer) --*

                              - **ChannelsIn** *(integer) --* Specify the number of audio channels
                              from your input that you want to use in your output. With remixing,
                              you might combine or split the data in these channels, so the number
                              of channels in your final output might be different.

                              - **ChannelsOut** *(integer) --* Specify the number of channels in
                              this output after remixing. Valid values: 1, 2, 4, 6, 8... 64. (1 and
                              even numbers to 64.)

                            - **SelectorType** *(string) --* Specifies the type of the audio
                            selector.

                            - **Tracks** *(list) --* Identify a track from the input audio to
                            include in this selector by entering the track index number. To include
                            several tracks in a single audio selector, specify multiple tracks as
                            follows. Using the console, enter a comma-separated list. For examle,
                            type "1,2,3" to include tracks 1 through 3. Specifying directly in your
                            JSON job file, provide the track numbers in an array. For example,
                            "tracks": [1,2,3].

                              - *(integer) --*

                      - **CaptionSelectors** *(dict) --* Use Captions selectors (CaptionSelectors)
                      to specify the captions data from the input that you will use in your outputs.
                      You can use mutiple captions selectors per input.

                        - *(string) --*

                          - *(dict) --* Set up captions in your outputs by first selecting them from
                          your input here.

                            - **CustomLanguageCode** *(string) --* The specific language to extract
                            from source, using the ISO 639-2 or ISO 639-3 three-letter language
                            code. If input is SCTE-27, complete this field and/or PID to select the
                            caption language to extract. If input is DVB-Sub and output is Burn-in
                            or SMPTE-TT, complete this field and/or PID to select the caption
                            language to extract. If input is DVB-Sub that is being passed through,
                            omit this field (and PID field); there is no way to extract a specific
                            language with pass-through captions.

                            - **LanguageCode** *(string) --* The specific language to extract from
                            source. If input is SCTE-27, complete this field and/or PID to select
                            the caption language to extract. If input is DVB-Sub and output is
                            Burn-in or SMPTE-TT, complete this field and/or PID to select the
                            caption language to extract. If input is DVB-Sub that is being passed
                            through, omit this field (and PID field); there is no way to extract a
                            specific language with pass-through captions.

                            - **SourceSettings** *(dict) --* If your input captions are SCC, TTML,
                            STL, SMI, SRT, or IMSC in an xml file, specify the URI of the input
                            captions source file. If your input captions are IMSC in an IMF package,
                            use TrackSourceSettings instead of FileSoureSettings.

                              - **AncillarySourceSettings** *(dict) --* Settings for ancillary
                              captions source.

                                - **Convert608To708** *(string) --* Specify whether this set of
                                input captions appears in your outputs in both 608 and 708 format.
                                If you choose Upconvert (UPCONVERT), MediaConvert includes the
                                captions data in two ways: it passes the 608 data through using the
                                608 compatibility bytes fields of the 708 wrapper, and it also
                                translates the 608 data into 708.

                                - **SourceAncillaryChannelNumber** *(integer) --* Specifies the 608
                                channel number in the ancillary data track from which to extract
                                captions. Unused for passthrough.

                                - **TerminateCaptions** *(string) --* By default, the service
                                terminates any unterminated captions at the end of each input. If
                                you want the caption to continue onto your next input, disable this
                                setting.

                              - **DvbSubSourceSettings** *(dict) --* DVB Sub Source Settings

                                - **Pid** *(integer) --* When using DVB-Sub with Burn-In or
                                SMPTE-TT, use this PID for the source content. Unused for DVB-Sub
                                passthrough. All DVB-Sub content is passed through, regardless of
                                selectors.

                              - **EmbeddedSourceSettings** *(dict) --* Settings for embedded
                              captions Source

                                - **Convert608To708** *(string) --* Specify whether this set of
                                input captions appears in your outputs in both 608 and 708 format.
                                If you choose Upconvert (UPCONVERT), MediaConvert includes the
                                captions data in two ways: it passes the 608 data through using the
                                608 compatibility bytes fields of the 708 wrapper, and it also
                                translates the 608 data into 708.

                                - **Source608ChannelNumber** *(integer) --* Specifies the 608/708
                                channel number within the video track from which to extract
                                captions. Unused for passthrough.

                                - **Source608TrackNumber** *(integer) --* Specifies the video track
                                index used for extracting captions. The system only supports one
                                input video track, so this should always be set to '1'.

                                - **TerminateCaptions** *(string) --* By default, the service
                                terminates any unterminated captions at the end of each input. If
                                you want the caption to continue onto your next input, disable this
                                setting.

                              - **FileSourceSettings** *(dict) --* If your input captions are SCC,
                              SMI, SRT, STL, TTML, or IMSC 1.1 in an xml file, specify the URI of
                              the input caption source file. If your caption source is IMSC in an
                              IMF package, use TrackSourceSettings instead of FileSoureSettings.

                                - **Convert608To708** *(string) --* Specify whether this set of
                                input captions appears in your outputs in both 608 and 708 format.
                                If you choose Upconvert (UPCONVERT), MediaConvert includes the
                                captions data in two ways: it passes the 608 data through using the
                                608 compatibility bytes fields of the 708 wrapper, and it also
                                translates the 608 data into 708.

                                - **SourceFile** *(string) --* External caption file used for
                                loading captions. Accepted file extensions are 'scc', 'ttml',
                                'dfxp', 'stl', 'srt', 'xml', and 'smi'.

                                - **TimeDelta** *(integer) --* Specifies a time delta in seconds to
                                offset the captions from the source file.

                              - **SourceType** *(string) --* Use Source (SourceType) to identify the
                              format of your input captions. The service cannot auto-detect caption
                              format.

                              - **TeletextSourceSettings** *(dict) --* Settings specific to Teletext
                              caption sources, including Page number.

                                - **PageNumber** *(string) --* Use Page Number (PageNumber) to
                                specify the three-digit hexadecimal page number that will be used
                                for Teletext captions. Do not use this setting if you are passing
                                through teletext from the input source to output.

                              - **TrackSourceSettings** *(dict) --* Settings specific to caption
                              sources that are specified by track number. Currently, this is only
                              IMSC captions in an IMF package. If your caption source is IMSC 1.1 in
                              a separate xml file, use FileSourceSettings instead of
                              TrackSourceSettings.

                                - **TrackNumber** *(integer) --* Use this setting to select a single
                                captions track from a source. Track numbers correspond to the order
                                in the captions source file. For IMF sources, track numbering is
                                based on the order that the captions appear in the CPL. For example,
                                use 1 to select the captions asset that is listed first in the CPL.
                                To include more than one captions track in your job outputs, create
                                multiple input captions selectors. Specify one track per selector.

                      - **Crop** *(dict) --* Use Cropping selection (crop) to specify the video area
                      that the service will include in the output video frame. If you specify a
                      value here, it will override any value that you specify in the output setting
                      Cropping selection (crop).

                        - **Height** *(integer) --* Height of rectangle in pixels. Specify only even
                        numbers.

                        - **Width** *(integer) --* Width of rectangle in pixels. Specify only even
                        numbers.

                        - **X** *(integer) --* The distance, in pixels, between the rectangle and
                        the left edge of the video frame. Specify only even numbers.

                        - **Y** *(integer) --* The distance, in pixels, between the rectangle and
                        the top edge of the video frame. Specify only even numbers.

                      - **DeblockFilter** *(string) --* Enable Deblock (InputDeblockFilter) to
                      produce smoother motion in the output. Default is disabled. Only manaully
                      controllable for MPEG2 and uncompressed video inputs.

                      - **DenoiseFilter** *(string) --* Enable Denoise (InputDenoiseFilter) to
                      filter noise from the input. Default is disabled. Only applicable to MPEG2,
                      H.264, H.265, and uncompressed video inputs.

                      - **FilterEnable** *(string) --* Use Filter enable (InputFilterEnable) to
                      specify how the transcoding service applies the denoise and deblock filters.
                      You must also enable the filters separately, with Denoise (InputDenoiseFilter)
                      and Deblock (InputDeblockFilter). * Auto - The transcoding service determines
                      whether to apply filtering, depending on input type and quality. * Disable -
                      The input is not filtered. This is true even if you use the API to enable them
                      in (InputDeblockFilter) and (InputDeblockFilter). * Force - The in put is
                      filtered regardless of input type.

                      - **FilterStrength** *(integer) --* Use Filter strength (FilterStrength) to
                      adjust the magnitude the input filter settings (Deblock and Denoise). The
                      range is -5 to 5. Default is 0.

                      - **ImageInserter** *(dict) --* Enable the image inserter feature to include a
                      graphic overlay on your video. Enable or disable this feature for each input
                      individually. This setting is disabled by default.

                        - **InsertableImages** *(list) --* Specify the images that you want to
                        overlay on your video. The images must be PNG or TGA files.

                          - *(dict) --* Settings that specify how your still graphic overlay
                          appears.

                            - **Duration** *(integer) --* Specify the time, in milliseconds, for the
                            image to remain on the output video. This duration includes fade-in time
                            but not fade-out time.

                            - **FadeIn** *(integer) --* Specify the length of time, in milliseconds,
                            between the Start time that you specify for the image insertion and the
                            time that the image appears at full opacity. Full opacity is the level
                            that you specify for the opacity setting. If you don't specify a value
                            for Fade-in, the image will appear abruptly at the overlay start time.

                            - **FadeOut** *(integer) --* Specify the length of time, in
                            milliseconds, between the end of the time that you have specified for
                            the image overlay Duration and when the overlaid image has faded to
                            total transparency. If you don't specify a value for Fade-out, the image
                            will disappear abruptly at the end of the inserted image duration.

                            - **Height** *(integer) --* Specify the height of the inserted image in
                            pixels. If you specify a value that's larger than the video resolution
                            height, the service will crop your overlaid image to fit. To use the
                            native height of the image, keep this setting blank.

                            - **ImageInserterInput** *(string) --* Specify the HTTP, HTTPS, or
                            Amazon S3 location of the image that you want to overlay on the video.
                            Use a PNG or TGA file.

                            - **ImageX** *(integer) --* Specify the distance, in pixels, between the
                            inserted image and the left edge of the video frame. Required for any
                            image overlay that you specify.

                            - **ImageY** *(integer) --* Specify the distance, in pixels, between the
                            overlaid image and the top edge of the video frame. Required for any
                            image overlay that you specify.

                            - **Layer** *(integer) --* Specify how overlapping inserted images
                            appear. Images with higher values for Layer appear on top of images with
                            lower values for Layer.

                            - **Opacity** *(integer) --* Use Opacity (Opacity) to specify how much
                            of the underlying video shows through the inserted image. 0 is
                            transparent and 100 is fully opaque. Default is 50.

                            - **StartTime** *(string) --* Specify the timecode of the frame that you
                            want the overlay to first appear on. This must be in timecode
                            (HH:MM:SS:FF or HH:MM:SS;FF) format. Remember to take into account your
                            timecode source settings.

                            - **Width** *(integer) --* Specify the width of the inserted image in
                            pixels. If you specify a value that's larger than the video resolution
                            width, the service will crop your overlaid image to fit. To use the
                            native width of the image, keep this setting blank.

                      - **InputClippings** *(list) --* (InputClippings) contains sets of start and
                      end times that together specify a portion of the input to be used in the
                      outputs. If you provide only a start time, the clip will be the entire input
                      from that point to the end. If you provide only an end time, it will be the
                      entire input up to that point. When you specify more than one input clip, the
                      transcoding service creates the job outputs by stringing the clips together in
                      the order you specify them.

                        - *(dict) --* To transcode only portions of your input (clips), include one
                        Input clipping (one instance of InputClipping in the JSON job file) for each
                        input clip. All input clips you specify will be included in every output of
                        the job.

                          - **EndTimecode** *(string) --* Set End timecode (EndTimecode) to the end
                          of the portion of the input you are clipping. The frame corresponding to
                          the End timecode value is included in the clip. Start timecode or End
                          timecode may be left blank, but not both. Use the format HH:MM:SS:FF or
                          HH:MM:SS;FF, where HH is the hour, MM is the minute, SS is the second, and
                          FF is the frame number. When choosing this value, take into account your
                          setting for timecode source under input settings (InputTimecodeSource).
                          For example, if you have embedded timecodes that start at 01:00:00:00 and
                          you want your clip to end six minutes into the video, use 01:06:00:00.

                          - **StartTimecode** *(string) --* Set Start timecode (StartTimecode) to
                          the beginning of the portion of the input you are clipping. The frame
                          corresponding to the Start timecode value is included in the clip. Start
                          timecode or End timecode may be left blank, but not both. Use the format
                          HH:MM:SS:FF or HH:MM:SS;FF, where HH is the hour, MM is the minute, SS is
                          the second, and FF is the frame number. When choosing this value, take
                          into account your setting for Input timecode source. For example, if you
                          have embedded timecodes that start at 01:00:00:00 and you want your clip
                          to begin five minutes into the video, use 01:05:00:00.

                      - **Position** *(dict) --* Use Selection placement (position) to define the
                      video area in your output frame. The area outside of the rectangle that you
                      specify here is black. If you specify a value here, it will override any value
                      that you specify in the output setting Selection placement (position). If you
                      specify a value here, this will override any AFD values in your input, even if
                      you set Respond to AFD (RespondToAfd) to Respond (RESPOND). If you specify a
                      value here, this will ignore anything that you specify for the setting Scaling
                      Behavior (scalingBehavior).

                        - **Height** *(integer) --* Height of rectangle in pixels. Specify only even
                        numbers.

                        - **Width** *(integer) --* Width of rectangle in pixels. Specify only even
                        numbers.

                        - **X** *(integer) --* The distance, in pixels, between the rectangle and
                        the left edge of the video frame. Specify only even numbers.

                        - **Y** *(integer) --* The distance, in pixels, between the rectangle and
                        the top edge of the video frame. Specify only even numbers.

                      - **ProgramNumber** *(integer) --* Use Program (programNumber) to select a
                      specific program from within a multi-program transport stream. Note that Quad
                      4K is not currently supported. Default is the first program within the
                      transport stream. If the program you specify doesn't exist, the transcoding
                      service will use this default.

                      - **PsiControl** *(string) --* Set PSI control (InputPsiControl) for transport
                      stream inputs to specify which data the demux process to scans. * Ignore PSI -
                      Scan all PIDs for audio and video. * Use PSI - Scan only PSI data.

                      - **TimecodeSource** *(string) --* Use this Timecode source setting, located
                      under the input settings (InputTimecodeSource), to specify how the service
                      counts input video frames. This input frame count affects only the behavior of
                      features that apply to a single input at a time, such as input clipping and
                      synchronizing some captions formats. Choose Embedded (EMBEDDED) to use the
                      timecodes in your input video. Choose Start at zero (ZEROBASED) to start the
                      first frame at zero. Choose Specified start (SPECIFIEDSTART) to start the
                      first frame at the timecode that you specify in the setting Start timecode
                      (timecodeStart). If you don't specify a value for Timecode source, the service
                      will use Embedded by default. For more information about timecodes, see
                      https://docs.aws.amazon.com/console/mediaconvert/timecode.

                      - **TimecodeStart** *(string) --* Specify the timecode that you want the
                      service to use for this input's initial frame. To use this setting, you must
                      set the Timecode source setting, located under the input settings
                      (InputTimecodeSource), to Specified start (SPECIFIEDSTART). For more
                      information about timecodes, see
                      https://docs.aws.amazon.com/console/mediaconvert/timecode.

                      - **VideoSelector** *(dict) --* Selector for video.

                        - **AlphaBehavior** *(string) --* Ignore this setting unless this input is a
                        QuickTime animation. Specify which part of this input MediaConvert uses for
                        your outputs. Leave this setting set to DISCARD in order to delete the alpha
                        channel and preserve the video. Use REMAP_TO_LUMA for this setting to delete
                        the video and map the alpha channel to the luma channel of your outputs.

                        - **ColorSpace** *(string) --* If your input video has accurate color space
                        metadata, or if you don't know about color space, leave this set to the
                        default value Follow (FOLLOW). The service will automatically detect your
                        input color space. If your input video has metadata indicating the wrong
                        color space, specify the accurate color space here. If your input video is
                        HDR 10 and the SMPTE ST 2086 Mastering Display Color Volume static metadata
                        isn't present in your video stream, or if that metadata is present but not
                        accurate, choose Force HDR 10 (FORCE_HDR10) here and specify correct values
                        in the input HDR 10 metadata (Hdr10Metadata) settings. For more information
                        about MediaConvert HDR jobs, see
                        https://docs.aws.amazon.com/console/mediaconvert/hdr.

                        - **ColorSpaceUsage** *(string) --* There are two sources for color
                        metadata, the input file and the job input settings Color space (ColorSpace)
                        and HDR master display information settings(Hdr10Metadata). The Color space
                        usage setting determines which takes precedence. Choose Force (FORCE) to use
                        color metadata from the input job settings. If you don't specify values for
                        those settings, the service defaults to using metadata from your input.
                        FALLBACK - Choose Fallback (FALLBACK) to use color metadata from the source
                        when it is present. If there's no color metadata in your input file, the
                        service defaults to using values you specify in the input settings.

                        - **Hdr10Metadata** *(dict) --* Use these settings to provide HDR 10
                        metadata that is missing or inaccurate in your input video. Appropriate
                        values vary depending on the input video and must be provided by a color
                        grader. The color grader generates these values during the HDR 10 mastering
                        process. The valid range for each of these settings is 0 to 50,000. Each
                        increment represents 0.00002 in CIE1931 color coordinate. Related settings -
                        When you specify these values, you must also set Color space (ColorSpace) to
                        HDR 10 (HDR10). To specify whether the the values you specify here take
                        precedence over the values in the metadata of your input file, set Color
                        space usage (ColorSpaceUsage). To specify whether color metadata is included
                        in an output, set Color metadata (ColorMetadata). For more information about
                        MediaConvert HDR jobs, see
                        https://docs.aws.amazon.com/console/mediaconvert/hdr.

                          - **BluePrimaryX** *(integer) --* HDR Master Display Information must be
                          provided by a color grader, using color grading tools. Range is 0 to
                          50,000, each increment represents 0.00002 in CIE1931 color coordinate.
                          Note that this setting is not for color correction.

                          - **BluePrimaryY** *(integer) --* HDR Master Display Information must be
                          provided by a color grader, using color grading tools. Range is 0 to
                          50,000, each increment represents 0.00002 in CIE1931 color coordinate.
                          Note that this setting is not for color correction.

                          - **GreenPrimaryX** *(integer) --* HDR Master Display Information must be
                          provided by a color grader, using color grading tools. Range is 0 to
                          50,000, each increment represents 0.00002 in CIE1931 color coordinate.
                          Note that this setting is not for color correction.

                          - **GreenPrimaryY** *(integer) --* HDR Master Display Information must be
                          provided by a color grader, using color grading tools. Range is 0 to
                          50,000, each increment represents 0.00002 in CIE1931 color coordinate.
                          Note that this setting is not for color correction.

                          - **MaxContentLightLevel** *(integer) --* Maximum light level among all
                          samples in the coded video sequence, in units of candelas per square
                          meter. This setting doesn't have a default value; you must specify a value
                          that is suitable for the content.

                          - **MaxFrameAverageLightLevel** *(integer) --* Maximum average light level
                          of any frame in the coded video sequence, in units of candelas per square
                          meter. This setting doesn't have a default value; you must specify a value
                          that is suitable for the content.

                          - **MaxLuminance** *(integer) --* Nominal maximum mastering display
                          luminance in units of of 0.0001 candelas per square meter.

                          - **MinLuminance** *(integer) --* Nominal minimum mastering display
                          luminance in units of of 0.0001 candelas per square meter

                          - **RedPrimaryX** *(integer) --* HDR Master Display Information must be
                          provided by a color grader, using color grading tools. Range is 0 to
                          50,000, each increment represents 0.00002 in CIE1931 color coordinate.
                          Note that this setting is not for color correction.

                          - **RedPrimaryY** *(integer) --* HDR Master Display Information must be
                          provided by a color grader, using color grading tools. Range is 0 to
                          50,000, each increment represents 0.00002 in CIE1931 color coordinate.
                          Note that this setting is not for color correction.

                          - **WhitePointX** *(integer) --* HDR Master Display Information must be
                          provided by a color grader, using color grading tools. Range is 0 to
                          50,000, each increment represents 0.00002 in CIE1931 color coordinate.
                          Note that this setting is not for color correction.

                          - **WhitePointY** *(integer) --* HDR Master Display Information must be
                          provided by a color grader, using color grading tools. Range is 0 to
                          50,000, each increment represents 0.00002 in CIE1931 color coordinate.
                          Note that this setting is not for color correction.

                        - **Pid** *(integer) --* Use PID (Pid) to select specific video data from an
                        input file. Specify this value as an integer; the system automatically
                        converts it to the hexidecimal value. For example, 257 selects PID 0x101. A
                        PID, or packet identifier, is an identifier for a set of data in an MPEG-2
                        transport stream container.

                        - **ProgramNumber** *(integer) --* Selects a specific program from within a
                        multi-program transport stream. Note that Quad 4K is not currently
                        supported.

                        - **Rotate** *(string) --* Use Rotate (InputRotate) to specify how the
                        service rotates your video. You can choose automatic rotation or specify a
                        rotation. You can specify a clockwise rotation of 0, 90, 180, or 270
                        degrees. If your input video container is .mov or .mp4 and your input has
                        rotation metadata, you can choose Automatic to have the service rotate your
                        video according to the rotation specified in the metadata. The rotation must
                        be within one degree of 90, 180, or 270 degrees. If the rotation metadata
                        specifies any other rotation, the service will default to no rotation. By
                        default, the service does no rotation, even if your input video has rotation
                        metadata. The service doesn't pass through rotation metadata.

                  - **MotionImageInserter** *(dict) --* Overlay motion graphics on top of your
                  video. The motion graphics that you specify here appear on all outputs in all
                  output groups.

                    - **Framerate** *(dict) --* If your motion graphic asset is a .mov file, keep
                    this setting unspecified. If your motion graphic asset is a series of .png
                    files, specify the frame rate of the overlay in frames per second, as a
                    fraction. For example, specify 24 fps as 24/1. Make sure that the number of
                    images in your series matches the frame rate and your intended overlay duration.
                    For example, if you want a 30-second overlay at 30 fps, you should have 900 .png
                    images. This overlay frame rate doesn't need to match the frame rate of the
                    underlying video.

                      - **FramerateDenominator** *(integer) --* The bottom of the fraction that
                      expresses your overlay frame rate. For example, if your frame rate is 24 fps,
                      set this value to 1.

                      - **FramerateNumerator** *(integer) --* The top of the fraction that expresses
                      your overlay frame rate. For example, if your frame rate is 24 fps, set this
                      value to 24.

                    - **Input** *(string) --* Specify the .mov file or series of .png files that you
                    want to overlay on your video. For .png files, provide the file name of the
                    first file in the series. Make sure that the names of the .png files end with
                    sequential numbers that specify the order that they are played in. For example,
                    overlay_000.png, overlay_001.png, overlay_002.png, and so on. The sequence must
                    start at zero, and each image file name must have the same number of digits. Pad
                    your initial file names with enough zeros to complete the sequence. For example,
                    if the first image is overlay_0.png, there can be only 10 images in the
                    sequence, with the last image being overlay_9.png. But if the first image is
                    overlay_00.png, there can be 100 images in the sequence.

                    - **InsertionMode** *(string) --* Choose the type of motion graphic asset that
                    you are providing for your overlay. You can choose either a .mov file or a
                    series of .png files.

                    - **Offset** *(dict) --* Use Offset to specify the placement of your motion
                    graphic overlay on the video frame. Specify in pixels, from the upper-left
                    corner of the frame. If you don't specify an offset, the service scales your
                    overlay to the full size of the frame. Otherwise, the service inserts the
                    overlay at its native resolution and scales the size up or down with any video
                    scaling.

                      - **ImageX** *(integer) --* Set the distance, in pixels, between the overlay
                      and the left edge of the video frame.

                      - **ImageY** *(integer) --* Set the distance, in pixels, between the overlay
                      and the top edge of the video frame.

                    - **Playback** *(string) --* Specify whether your motion graphic overlay repeats
                    on a loop or plays only once.

                    - **StartTime** *(string) --* Specify when the motion overlay begins. Use
                    timecode format (HH:MM:SS:FF or HH:MM:SS;FF). Make sure that the timecode you
                    provide here takes into account how you have set up your timecode configuration
                    under both job settings and input settings. The simplest way to do that is to
                    set both to start at 0. If you need to set up your job to follow timecodes
                    embedded in your source that don't start at zero, make sure that you specify a
                    start time that is after the first embedded timecode. For more information, see
                    https://docs.aws.amazon.com/mediaconvert/latest/ug/setting-up-timecode.html Find
                    job-wide and input timecode configuration settings in your JSON job settings
                    specification at settings>timecodeConfig>source and
                    settings>inputs>timecodeSource.

                  - **NielsenConfiguration** *(dict) --* Settings for your Nielsen configuration. If
                  you don't do Nielsen measurement and analytics, ignore these settings. When you
                  enable Nielsen configuration (nielsenConfiguration), MediaConvert enables PCM to
                  ID3 tagging for all outputs in the job. To enable Nielsen configuration
                  programmatically, include an instance of nielsenConfiguration in your JSON job
                  specification. Even if you don't include any children of nielsenConfiguration, you
                  still enable the setting.

                    - **BreakoutCode** *(integer) --* Nielsen has discontinued the use of breakout
                    code functionality. If you must include this property, set the value to zero.

                    - **DistributorId** *(string) --* Use Distributor ID (DistributorID) to specify
                    the distributor ID that is assigned to your organization by Neilsen.

                  - **OutputGroups** *(list) --* (OutputGroups) contains one group of settings for
                  each set of outputs that share a common package type. All unpackaged files
                  (MPEG-4, MPEG-2 TS, Quicktime, MXF, and no container) are grouped in a single
                  output group as well. Required in (OutputGroups) is a group of settings that apply
                  to the whole group. This required object depends on the value you set for (Type)
                  under (OutputGroups)>(OutputGroupSettings). Type, settings object pairs are as
                  follows. * FILE_GROUP_SETTINGS, FileGroupSettings * HLS_GROUP_SETTINGS,
                  HlsGroupSettings * DASH_ISO_GROUP_SETTINGS, DashIsoGroupSettings *
                  MS_SMOOTH_GROUP_SETTINGS, MsSmoothGroupSettings * CMAF_GROUP_SETTINGS,
                  CmafGroupSettings

                    - *(dict) --* Group of outputs

                      - **CustomName** *(string) --* Use Custom Group Name (CustomName) to specify a
                      name for the output group. This value is displayed on the console and can make
                      your job settings JSON more human-readable. It does not affect your outputs.
                      Use up to twelve characters that are either letters, numbers, spaces, or
                      underscores.

                      - **Name** *(string) --* Name of the output group

                      - **OutputGroupSettings** *(dict) --* Output Group settings, including type

                        - **CmafGroupSettings** *(dict) --* Required when you set (Type) under
                        (OutputGroups)>(OutputGroupSettings) to CMAF_GROUP_SETTINGS. Each output in
                        a CMAF Output Group may only contain a single video, audio, or caption
                        output.

                          - **AdditionalManifests** *(list) --* By default, the service creates one
                          top-level .m3u8 HLS manifest and one top -level .mpd DASH manifest for
                          each CMAF output group in your job. These default manifests reference
                          every output in the output group. To create additional top-level manifests
                          that reference a subset of the outputs in the output group, specify a list
                          of them here. For each additional manifest that you specify, the service
                          creates one HLS manifest and one DASH manifest.

                            - *(dict) --* Specify the details for each pair of HLS and DASH
                            additional manifests that you want the service to generate for this CMAF
                            output group. Each pair of manifests can reference a different subset of
                            outputs in the group.

                              - **ManifestNameModifier** *(string) --* Specify a name modifier that
                              the service adds to the name of this manifest to make it different
                              from the file names of the other main manifests in the output group.
                              For example, say that the default main manifest for your HLS group is
                              film-name.m3u8. If you enter "-no-premium" for this setting, then the
                              file name the service generates for this top-level manifest is
                              film-name-no-premium.m3u8. For HLS output groups, specify a
                              manifestNameModifier that is different from the nameModifier of the
                              output. The service uses the output name modifier to create unique
                              names for the individual variant manifests.

                              - **SelectedOutputs** *(list) --* Specify the outputs that you want
                              this additional top-level manifest to reference.

                                - *(string) --*

                          - **BaseUrl** *(string) --* A partial URI prefix that will be put in the
                          manifest file at the top level BaseURL element. Can be used if streams are
                          delivered from a different URL than the manifest file.

                          - **ClientCache** *(string) --* When set to ENABLED, sets
                          #EXT-X-ALLOW-CACHE:no tag, which prevents client from saving media
                          segments for later replay.

                          - **CodecSpecification** *(string) --* Specification to use (RFC-6381 or
                          the default RFC-4281) during m3u8 playlist generation.

                          - **Destination** *(string) --* Use Destination (Destination) to specify
                          the S3 output location and the output filename base. Destination accepts
                          format identifiers. If you do not specify the base filename in the URI,
                          the service will use the filename of the input file. If your job has
                          multiple inputs, the service uses the filename of the first input file.

                          - **DestinationSettings** *(dict) --* Settings associated with the
                          destination. Will vary based on the type of destination

                            - **S3Settings** *(dict) --* Settings associated with S3 destination

                              - **AccessControl** *(dict) --* Optional. Have MediaConvert
                              automatically apply Amazon S3 access control for the outputs in this
                              output group. When you don't use this setting, S3 automatically
                              applies the default access control list PRIVATE.

                                - **CannedAcl** *(string) --* Choose an Amazon S3 canned ACL for
                                MediaConvert to apply to this output.

                              - **Encryption** *(dict) --* Settings for how your job outputs are
                              encrypted as they are uploaded to Amazon S3.

                                - **EncryptionType** *(string) --* Specify how you want your data
                                keys managed. AWS uses data keys to encrypt your content. AWS also
                                encrypts the data keys themselves, using a customer master key
                                (CMK), and then stores the encrypted data keys alongside your
                                encrypted content. Use this setting to specify which AWS service
                                manages the CMK. For simplest set up, choose Amazon S3
                                (SERVER_SIDE_ENCRYPTION_S3). If you want your master key to be
                                managed by AWS Key Management Service (KMS), choose AWS KMS
                                (SERVER_SIDE_ENCRYPTION_KMS). By default, when you choose AWS KMS,
                                KMS uses the AWS managed customer master key (CMK) associated with
                                Amazon S3 to encrypt your data keys. You can optionally choose to
                                specify a different, customer managed CMK. Do so by specifying the
                                Amazon Resource Name (ARN) of the key for the setting KMS ARN
                                (kmsKeyArn).

                                - **KmsKeyArn** *(string) --* Optionally, specify the customer
                                master key (CMK) that you want to use to encrypt the data key that
                                AWS uses to encrypt your output content. Enter the Amazon Resource
                                Name (ARN) of the CMK. To use this setting, you must also set
                                Server-side encryption (S3ServerSideEncryptionType) to AWS KMS
                                (SERVER_SIDE_ENCRYPTION_KMS). If you set Server-side encryption to
                                AWS KMS but don't specify a CMK here, AWS uses the AWS managed CMK
                                associated with Amazon S3.

                          - **Encryption** *(dict) --* DRM settings.

                            - **ConstantInitializationVector** *(string) --* This is a 128-bit,
                            16-byte hex value represented by a 32-character text string. If this
                            parameter is not set then the Initialization Vector will follow the
                            segment number by default.

                            - **EncryptionMethod** *(string) --* Specify the encryption scheme that
                            you want the service to use when encrypting your CMAF segments. Choose
                            AES-CBC subsample (SAMPLE-AES) or AES_CTR (AES-CTR).

                            - **InitializationVectorInManifest** *(string) --* When you use DRM with
                            CMAF outputs, choose whether the service writes the 128-bit encryption
                            initialization vector in the HLS and DASH manifests.

                            - **SpekeKeyProvider** *(dict) --* If your output group type is CMAF,
                            use these settings when doing DRM encryption with a SPEKE-compliant key
                            provider. If your output group type is HLS, DASH, or Microsoft Smooth,
                            use the SpekeKeyProvider settings instead.

                              - **CertificateArn** *(string) --* If you want your key provider to
                              encrypt the content keys that it provides to MediaConvert, set up a
                              certificate with a master key using AWS Certificate Manager. Specify
                              the certificate's Amazon Resource Name (ARN) here.

                              - **DashSignaledSystemIds** *(list) --* Specify the DRM system IDs
                              that you want signaled in the DASH manifest that MediaConvert creates
                              as part of this CMAF package. The DASH manifest can currently signal
                              up to three system IDs. For more information, see
                              https://dashif.org/identifiers/content_protection/.

                                - *(string) --*

                              - **HlsSignaledSystemIds** *(list) --* Specify the DRM system ID that
                              you want signaled in the HLS manifest that MediaConvert creates as
                              part of this CMAF package. The HLS manifest can currently signal only
                              one system ID. For more information, see
                              https://dashif.org/identifiers/content_protection/.

                                - *(string) --*

                              - **ResourceId** *(string) --* Specify the resource ID that your
                              SPEKE-compliant key provider uses to identify this content.

                              - **Url** *(string) --* Specify the URL to the key server that your
                              SPEKE-compliant DRM key provider uses to provide keys for encrypting
                              your content.

                            - **StaticKeyProvider** *(dict) --* Use these settings to set up
                            encryption with a static key provider.

                              - **KeyFormat** *(string) --* Relates to DRM implementation. Sets the
                              value of the KEYFORMAT attribute. Must be 'identity' or a reverse DNS
                              string. May be omitted to indicate an implicit value of 'identity'.

                              - **KeyFormatVersions** *(string) --* Relates to DRM implementation.
                              Either a single positive integer version value or a slash delimited
                              list of version values (1/2/3).

                              - **StaticKeyValue** *(string) --* Relates to DRM implementation. Use
                              a 32-character hexidecimal string to specify Key Value
                              (StaticKeyValue).

                              - **Url** *(string) --* Relates to DRM implementation. The location of
                              the license server used for protecting content.

                            - **Type** *(string) --* Specify whether your DRM encryption key is
                            static or from a key provider that follows the SPEKE standard. For more
                            information about SPEKE, see
                            https://docs.aws.amazon.com/speke/latest/documentation/what-is-speke.html.

                          - **FragmentLength** *(integer) --* Length of fragments to generate (in
                          seconds). Fragment length must be compatible with GOP size and Framerate.
                          Note that fragments will end on the next keyframe after this number of
                          seconds, so actual fragment length may be longer. When Emit Single File is
                          checked, the fragmentation is internal to a single output file and it does
                          not cause the creation of many output files as in other output types.

                          - **ManifestCompression** *(string) --* When set to GZIP, compresses HLS
                          playlist.

                          - **ManifestDurationFormat** *(string) --* Indicates whether the output
                          manifest should use floating point values for segment duration.

                          - **MinBufferTime** *(integer) --* Minimum time of initially buffered
                          media that is needed to ensure smooth playout.

                          - **MinFinalSegmentLength** *(float) --* Keep this setting at the default
                          value of 0, unless you are troubleshooting a problem with how devices play
                          back the end of your video asset. If you know that player devices are
                          hanging on the final segment of your video because the length of your
                          final segment is too short, use this setting to specify a minimum final
                          segment length, in seconds. Choose a value that is greater than or equal
                          to 1 and less than your segment length. When you specify a value for this
                          setting, the encoder will combine any final segment that is shorter than
                          the length that you specify with the previous segment. For example, your
                          segment length is 3 seconds and your final segment is .5 seconds without a
                          minimum final segment length; when you set the minimum final segment
                          length to 1, your final segment is 3.5 seconds.

                          - **MpdProfile** *(string) --* Specify whether your DASH profile is
                          on-demand or main. When you choose Main profile (MAIN_PROFILE), the
                          service signals urn:mpeg:dash:profile:isoff-main:2011 in your .mpd DASH
                          manifest. When you choose On-demand (ON_DEMAND_PROFILE), the service
                          signals urn:mpeg:dash:profile:isoff-on-demand:2011 in your .mpd. When you
                          choose On-demand, you must also set the output group setting Segment
                          control (SegmentControl) to Single file (SINGLE_FILE).

                          - **SegmentControl** *(string) --* When set to SINGLE_FILE, a single
                          output file is generated, which is internally segmented using the Fragment
                          Length and Segment Length. When set to SEGMENTED_FILES, separate segment
                          files will be created.

                          - **SegmentLength** *(integer) --* Use this setting to specify the length,
                          in seconds, of each individual CMAF segment. This value applies to the
                          whole package; that is, to every output in the output group. Note that
                          segments end on the first keyframe after this number of seconds, so the
                          actual segment length might be slightly longer. If you set Segment control
                          (CmafSegmentControl) to single file, the service puts the content of each
                          output in a single file that has metadata that marks these segments. If
                          you set it to segmented files, the service creates multiple files for each
                          output, each with the content of one segment.

                          - **StreamInfResolution** *(string) --* Include or exclude RESOLUTION
                          attribute for video in EXT-X-STREAM-INF tag of variant manifest.

                          - **WriteDashManifest** *(string) --* When set to ENABLED, a DASH MPD
                          manifest will be generated for this output.

                          - **WriteHlsManifest** *(string) --* When set to ENABLED, an Apple HLS
                          manifest will be generated for this output.

                        - **DashIsoGroupSettings** *(dict) --* Required when you set (Type) under
                        (OutputGroups)>(OutputGroupSettings) to DASH_ISO_GROUP_SETTINGS.

                          - **AdditionalManifests** *(list) --* By default, the service creates one
                          .mpd DASH manifest for each DASH ISO output group in your job. This
                          default manifest references every output in the output group. To create
                          additional DASH manifests that reference a subset of the outputs in the
                          output group, specify a list of them here.

                            - *(dict) --* Specify the details for each additional DASH manifest that
                            you want the service to generate for this output group. Each manifest
                            can reference a different subset of outputs in the group.

                              - **ManifestNameModifier** *(string) --* Specify a name modifier that
                              the service adds to the name of this manifest to make it different
                              from the file names of the other main manifests in the output group.
                              For example, say that the default main manifest for your DASH group is
                              film-name.mpd. If you enter "-no-premium" for this setting, then the
                              file name the service generates for this top-level manifest is
                              film-name-no-premium.mpd.

                              - **SelectedOutputs** *(list) --* Specify the outputs that you want
                              this additional top-level manifest to reference.

                                - *(string) --*

                          - **BaseUrl** *(string) --* A partial URI prefix that will be put in the
                          manifest (.mpd) file at the top level BaseURL element. Can be used if
                          streams are delivered from a different URL than the manifest file.

                          - **Destination** *(string) --* Use Destination (Destination) to specify
                          the S3 output location and the output filename base. Destination accepts
                          format identifiers. If you do not specify the base filename in the URI,
                          the service will use the filename of the input file. If your job has
                          multiple inputs, the service uses the filename of the first input file.

                          - **DestinationSettings** *(dict) --* Settings associated with the
                          destination. Will vary based on the type of destination

                            - **S3Settings** *(dict) --* Settings associated with S3 destination

                              - **AccessControl** *(dict) --* Optional. Have MediaConvert
                              automatically apply Amazon S3 access control for the outputs in this
                              output group. When you don't use this setting, S3 automatically
                              applies the default access control list PRIVATE.

                                - **CannedAcl** *(string) --* Choose an Amazon S3 canned ACL for
                                MediaConvert to apply to this output.

                              - **Encryption** *(dict) --* Settings for how your job outputs are
                              encrypted as they are uploaded to Amazon S3.

                                - **EncryptionType** *(string) --* Specify how you want your data
                                keys managed. AWS uses data keys to encrypt your content. AWS also
                                encrypts the data keys themselves, using a customer master key
                                (CMK), and then stores the encrypted data keys alongside your
                                encrypted content. Use this setting to specify which AWS service
                                manages the CMK. For simplest set up, choose Amazon S3
                                (SERVER_SIDE_ENCRYPTION_S3). If you want your master key to be
                                managed by AWS Key Management Service (KMS), choose AWS KMS
                                (SERVER_SIDE_ENCRYPTION_KMS). By default, when you choose AWS KMS,
                                KMS uses the AWS managed customer master key (CMK) associated with
                                Amazon S3 to encrypt your data keys. You can optionally choose to
                                specify a different, customer managed CMK. Do so by specifying the
                                Amazon Resource Name (ARN) of the key for the setting KMS ARN
                                (kmsKeyArn).

                                - **KmsKeyArn** *(string) --* Optionally, specify the customer
                                master key (CMK) that you want to use to encrypt the data key that
                                AWS uses to encrypt your output content. Enter the Amazon Resource
                                Name (ARN) of the CMK. To use this setting, you must also set
                                Server-side encryption (S3ServerSideEncryptionType) to AWS KMS
                                (SERVER_SIDE_ENCRYPTION_KMS). If you set Server-side encryption to
                                AWS KMS but don't specify a CMK here, AWS uses the AWS managed CMK
                                associated with Amazon S3.

                          - **Encryption** *(dict) --* DRM settings.

                            - **PlaybackDeviceCompatibility** *(string) --* This setting can improve
                            the compatibility of your output with video players on obsolete devices.
                            It applies only to DASH H.264 outputs with DRM encryption. Choose
                            Unencrypted SEI (UNENCRYPTED_SEI) only to correct problems with playback
                            on older devices. Otherwise, keep the default setting CENC v1 (CENC_V1).
                            If you choose Unencrypted SEI, for that output, the service will exclude
                            the access unit delimiter and will leave the SEI NAL units unencrypted.

                            - **SpekeKeyProvider** *(dict) --* If your output group type is HLS,
                            DASH, or Microsoft Smooth, use these settings when doing DRM encryption
                            with a SPEKE-compliant key provider. If your output group type is CMAF,
                            use the SpekeKeyProviderCmaf settings instead.

                              - **CertificateArn** *(string) --* If you want your key provider to
                              encrypt the content keys that it provides to MediaConvert, set up a
                              certificate with a master key using AWS Certificate Manager. Specify
                              the certificate's Amazon Resource Name (ARN) here.

                              - **ResourceId** *(string) --* Specify the resource ID that your
                              SPEKE-compliant key provider uses to identify this content.

                              - **SystemIds** *(list) --* Relates to SPEKE implementation. DRM
                              system identifiers. DASH output groups support a max of two system
                              ids. Other group types support one system id. See
                              https://dashif.org/identifiers/content_protection/ for more details.

                                - *(string) --*

                              - **Url** *(string) --* Specify the URL to the key server that your
                              SPEKE-compliant DRM key provider uses to provide keys for encrypting
                              your content.

                          - **FragmentLength** *(integer) --* Length of fragments to generate (in
                          seconds). Fragment length must be compatible with GOP size and Framerate.
                          Note that fragments will end on the next keyframe after this number of
                          seconds, so actual fragment length may be longer. When Emit Single File is
                          checked, the fragmentation is internal to a single output file and it does
                          not cause the creation of many output files as in other output types.

                          - **HbbtvCompliance** *(string) --* Supports HbbTV specification as
                          indicated

                          - **MinBufferTime** *(integer) --* Minimum time of initially buffered
                          media that is needed to ensure smooth playout.

                          - **MpdProfile** *(string) --* Specify whether your DASH profile is
                          on-demand or main. When you choose Main profile (MAIN_PROFILE), the
                          service signals urn:mpeg:dash:profile:isoff-main:2011 in your .mpd DASH
                          manifest. When you choose On-demand (ON_DEMAND_PROFILE), the service
                          signals urn:mpeg:dash:profile:isoff-on-demand:2011 in your .mpd. When you
                          choose On-demand, you must also set the output group setting Segment
                          control (SegmentControl) to Single file (SINGLE_FILE).

                          - **SegmentControl** *(string) --* When set to SINGLE_FILE, a single
                          output file is generated, which is internally segmented using the Fragment
                          Length and Segment Length. When set to SEGMENTED_FILES, separate segment
                          files will be created.

                          - **SegmentLength** *(integer) --* Length of mpd segments to create (in
                          seconds). Note that segments will end on the next keyframe after this
                          number of seconds, so actual segment length may be longer. When Emit
                          Single File is checked, the segmentation is internal to a single output
                          file and it does not cause the creation of many output files as in other
                          output types.

                          - **WriteSegmentTimelineInRepresentation** *(string) --* If you get an
                          HTTP error in the 400 range when you play back your DASH output, enable
                          this setting and run your transcoding job again. When you enable this
                          setting, the service writes precise segment durations in the DASH
                          manifest. The segment duration information appears inside the
                          SegmentTimeline element, inside SegmentTemplate at the Representation
                          level. When you don't enable this setting, the service writes approximate
                          segment durations in your DASH manifest.

                        - **FileGroupSettings** *(dict) --* Required when you set (Type) under
                        (OutputGroups)>(OutputGroupSettings) to FILE_GROUP_SETTINGS.

                          - **Destination** *(string) --* Use Destination (Destination) to specify
                          the S3 output location and the output filename base. Destination accepts
                          format identifiers. If you do not specify the base filename in the URI,
                          the service will use the filename of the input file. If your job has
                          multiple inputs, the service uses the filename of the first input file.

                          - **DestinationSettings** *(dict) --* Settings associated with the
                          destination. Will vary based on the type of destination

                            - **S3Settings** *(dict) --* Settings associated with S3 destination

                              - **AccessControl** *(dict) --* Optional. Have MediaConvert
                              automatically apply Amazon S3 access control for the outputs in this
                              output group. When you don't use this setting, S3 automatically
                              applies the default access control list PRIVATE.

                                - **CannedAcl** *(string) --* Choose an Amazon S3 canned ACL for
                                MediaConvert to apply to this output.

                              - **Encryption** *(dict) --* Settings for how your job outputs are
                              encrypted as they are uploaded to Amazon S3.

                                - **EncryptionType** *(string) --* Specify how you want your data
                                keys managed. AWS uses data keys to encrypt your content. AWS also
                                encrypts the data keys themselves, using a customer master key
                                (CMK), and then stores the encrypted data keys alongside your
                                encrypted content. Use this setting to specify which AWS service
                                manages the CMK. For simplest set up, choose Amazon S3
                                (SERVER_SIDE_ENCRYPTION_S3). If you want your master key to be
                                managed by AWS Key Management Service (KMS), choose AWS KMS
                                (SERVER_SIDE_ENCRYPTION_KMS). By default, when you choose AWS KMS,
                                KMS uses the AWS managed customer master key (CMK) associated with
                                Amazon S3 to encrypt your data keys. You can optionally choose to
                                specify a different, customer managed CMK. Do so by specifying the
                                Amazon Resource Name (ARN) of the key for the setting KMS ARN
                                (kmsKeyArn).

                                - **KmsKeyArn** *(string) --* Optionally, specify the customer
                                master key (CMK) that you want to use to encrypt the data key that
                                AWS uses to encrypt your output content. Enter the Amazon Resource
                                Name (ARN) of the CMK. To use this setting, you must also set
                                Server-side encryption (S3ServerSideEncryptionType) to AWS KMS
                                (SERVER_SIDE_ENCRYPTION_KMS). If you set Server-side encryption to
                                AWS KMS but don't specify a CMK here, AWS uses the AWS managed CMK
                                associated with Amazon S3.

                        - **HlsGroupSettings** *(dict) --* Required when you set (Type) under
                        (OutputGroups)>(OutputGroupSettings) to HLS_GROUP_SETTINGS.

                          - **AdMarkers** *(list) --* Choose one or more ad marker types to decorate
                          your Apple HLS manifest. This setting does not determine whether SCTE-35
                          markers appear in the outputs themselves.

                            - *(string) --*

                          - **AdditionalManifests** *(list) --* By default, the service creates one
                          top-level .m3u8 HLS manifest for each HLS output group in your job. This
                          default manifest references every output in the output group. To create
                          additional top-level manifests that reference a subset of the outputs in
                          the output group, specify a list of them here.

                            - *(dict) --* Specify the details for each additional HLS manifest that
                            you want the service to generate for this output group. Each manifest
                            can reference a different subset of outputs in the group.

                              - **ManifestNameModifier** *(string) --* Specify a name modifier that
                              the service adds to the name of this manifest to make it different
                              from the file names of the other main manifests in the output group.
                              For example, say that the default main manifest for your HLS group is
                              film-name.m3u8. If you enter "-no-premium" for this setting, then the
                              file name the service generates for this top-level manifest is
                              film-name-no-premium.m3u8. For HLS output groups, specify a
                              manifestNameModifier that is different from the nameModifier of the
                              output. The service uses the output name modifier to create unique
                              names for the individual variant manifests.

                              - **SelectedOutputs** *(list) --* Specify the outputs that you want
                              this additional top-level manifest to reference.

                                - *(string) --*

                          - **BaseUrl** *(string) --* A partial URI prefix that will be prepended to
                          each output in the media .m3u8 file. Can be used if base manifest is
                          delivered from a different URL than the main .m3u8 file.

                          - **CaptionLanguageMappings** *(list) --* Language to be used on Caption
                          outputs

                            - *(dict) --* Caption Language Mapping

                              - **CaptionChannel** *(integer) --* Caption channel.

                              - **CustomLanguageCode** *(string) --* Specify the language for this
                              captions channel, using the ISO 639-2 or ISO 639-3 three-letter
                              language code

                              - **LanguageCode** *(string) --* Specify the language, using the ISO
                              639-2 three-letter code listed at
                              https://www.loc.gov/standards/iso639-2/php/code_list.php.

                              - **LanguageDescription** *(string) --* Caption language description.

                          - **CaptionLanguageSetting** *(string) --* Applies only to 608 Embedded
                          output captions. Insert: Include CLOSED-CAPTIONS lines in the manifest.
                          Specify at least one language in the CC1 Language Code field. One
                          CLOSED-CAPTION line is added for each Language Code you specify. Make sure
                          to specify the languages in the order in which they appear in the original
                          source (if the source is embedded format) or the order of the caption
                          selectors (if the source is other than embedded). Otherwise, languages in
                          the manifest will not match up properly with the output captions. None:
                          Include CLOSED-CAPTIONS=
                              NONE line in the manifest. Omit: Omit any
                          CLOSED-CAPTIONS line from the manifest.

                          - **ClientCache** *(string) --* When set to ENABLED, sets
                          #EXT-X-ALLOW-CACHE:no tag, which prevents client from saving media
                          segments for later replay.

                          - **CodecSpecification** *(string) --* Specification to use (RFC-6381 or
                          the default RFC-4281) during m3u8 playlist generation.

                          - **Destination** *(string) --* Use Destination (Destination) to specify
                          the S3 output location and the output filename base. Destination accepts
                          format identifiers. If you do not specify the base filename in the URI,
                          the service will use the filename of the input file. If your job has
                          multiple inputs, the service uses the filename of the first input file.

                          - **DestinationSettings** *(dict) --* Settings associated with the
                          destination. Will vary based on the type of destination

                            - **S3Settings** *(dict) --* Settings associated with S3 destination

                              - **AccessControl** *(dict) --* Optional. Have MediaConvert
                              automatically apply Amazon S3 access control for the outputs in this
                              output group. When you don't use this setting, S3 automatically
                              applies the default access control list PRIVATE.

                                - **CannedAcl** *(string) --* Choose an Amazon S3 canned ACL for
                                MediaConvert to apply to this output.

                              - **Encryption** *(dict) --* Settings for how your job outputs are
                              encrypted as they are uploaded to Amazon S3.

                                - **EncryptionType** *(string) --* Specify how you want your data
                                keys managed. AWS uses data keys to encrypt your content. AWS also
                                encrypts the data keys themselves, using a customer master key
                                (CMK), and then stores the encrypted data keys alongside your
                                encrypted content. Use this setting to specify which AWS service
                                manages the CMK. For simplest set up, choose Amazon S3
                                (SERVER_SIDE_ENCRYPTION_S3). If you want your master key to be
                                managed by AWS Key Management Service (KMS), choose AWS KMS
                                (SERVER_SIDE_ENCRYPTION_KMS). By default, when you choose AWS KMS,
                                KMS uses the AWS managed customer master key (CMK) associated with
                                Amazon S3 to encrypt your data keys. You can optionally choose to
                                specify a different, customer managed CMK. Do so by specifying the
                                Amazon Resource Name (ARN) of the key for the setting KMS ARN
                                (kmsKeyArn).

                                - **KmsKeyArn** *(string) --* Optionally, specify the customer
                                master key (CMK) that you want to use to encrypt the data key that
                                AWS uses to encrypt your output content. Enter the Amazon Resource
                                Name (ARN) of the CMK. To use this setting, you must also set
                                Server-side encryption (S3ServerSideEncryptionType) to AWS KMS
                                (SERVER_SIDE_ENCRYPTION_KMS). If you set Server-side encryption to
                                AWS KMS but don't specify a CMK here, AWS uses the AWS managed CMK
                                associated with Amazon S3.

                          - **DirectoryStructure** *(string) --* Indicates whether segments should
                          be placed in subdirectories.

                          - **Encryption** *(dict) --* DRM settings.

                            - **ConstantInitializationVector** *(string) --* This is a 128-bit,
                            16-byte hex value represented by a 32-character text string. If this
                            parameter is not set then the Initialization Vector will follow the
                            segment number by default.

                            - **EncryptionMethod** *(string) --* Encrypts the segments with the
                            given encryption scheme. Leave blank to disable. Selecting 'Disabled' in
                            the web interface also disables encryption.

                            - **InitializationVectorInManifest** *(string) --* The Initialization
                            Vector is a 128-bit number used in conjunction with the key for
                            encrypting blocks. If set to INCLUDE, Initialization Vector is listed in
                            the manifest. Otherwise Initialization Vector is not in the manifest.

                            - **OfflineEncrypted** *(string) --* Enable this setting to insert the
                            EXT-X-SESSION-KEY element into the master playlist. This allows for
                            offline Apple HLS FairPlay content protection.

                            - **SpekeKeyProvider** *(dict) --* If your output group type is HLS,
                            DASH, or Microsoft Smooth, use these settings when doing DRM encryption
                            with a SPEKE-compliant key provider. If your output group type is CMAF,
                            use the SpekeKeyProviderCmaf settings instead.

                              - **CertificateArn** *(string) --* If you want your key provider to
                              encrypt the content keys that it provides to MediaConvert, set up a
                              certificate with a master key using AWS Certificate Manager. Specify
                              the certificate's Amazon Resource Name (ARN) here.

                              - **ResourceId** *(string) --* Specify the resource ID that your
                              SPEKE-compliant key provider uses to identify this content.

                              - **SystemIds** *(list) --* Relates to SPEKE implementation. DRM
                              system identifiers. DASH output groups support a max of two system
                              ids. Other group types support one system id. See
                              https://dashif.org/identifiers/content_protection/ for more details.

                                - *(string) --*

                              - **Url** *(string) --* Specify the URL to the key server that your
                              SPEKE-compliant DRM key provider uses to provide keys for encrypting
                              your content.

                            - **StaticKeyProvider** *(dict) --* Use these settings to set up
                            encryption with a static key provider.

                              - **KeyFormat** *(string) --* Relates to DRM implementation. Sets the
                              value of the KEYFORMAT attribute. Must be 'identity' or a reverse DNS
                              string. May be omitted to indicate an implicit value of 'identity'.

                              - **KeyFormatVersions** *(string) --* Relates to DRM implementation.
                              Either a single positive integer version value or a slash delimited
                              list of version values (1/2/3).

                              - **StaticKeyValue** *(string) --* Relates to DRM implementation. Use
                              a 32-character hexidecimal string to specify Key Value
                              (StaticKeyValue).

                              - **Url** *(string) --* Relates to DRM implementation. The location of
                              the license server used for protecting content.

                            - **Type** *(string) --* Specify whether your DRM encryption key is
                            static or from a key provider that follows the SPEKE standard. For more
                            information about SPEKE, see
                            https://docs.aws.amazon.com/speke/latest/documentation/what-is-speke.html.

                          - **ManifestCompression** *(string) --* When set to GZIP, compresses HLS
                          playlist.

                          - **ManifestDurationFormat** *(string) --* Indicates whether the output
                          manifest should use floating point values for segment duration.

                          - **MinFinalSegmentLength** *(float) --* Keep this setting at the default
                          value of 0, unless you are troubleshooting a problem with how devices play
                          back the end of your video asset. If you know that player devices are
                          hanging on the final segment of your video because the length of your
                          final segment is too short, use this setting to specify a minimum final
                          segment length, in seconds. Choose a value that is greater than or equal
                          to 1 and less than your segment length. When you specify a value for this
                          setting, the encoder will combine any final segment that is shorter than
                          the length that you specify with the previous segment. For example, your
                          segment length is 3 seconds and your final segment is .5 seconds without a
                          minimum final segment length; when you set the minimum final segment
                          length to 1, your final segment is 3.5 seconds.

                          - **MinSegmentLength** *(integer) --* When set, Minimum Segment Size is
                          enforced by looking ahead and back within the specified range for a nearby
                          avail and extending the segment size if needed.

                          - **OutputSelection** *(string) --* Indicates whether the .m3u8 manifest
                          file should be generated for this HLS output group.

                          - **ProgramDateTime** *(string) --* Includes or excludes
                          EXT-X-PROGRAM-DATE-TIME tag in .m3u8 manifest files. The value is
                          calculated as follows: either the program date and time are initialized
                          using the input timecode source, or the time is initialized using the
                          input timecode source and the date is initialized using the
                          timestamp_offset.

                          - **ProgramDateTimePeriod** *(integer) --* Period of insertion of
                          EXT-X-PROGRAM-DATE-TIME entry, in seconds.

                          - **SegmentControl** *(string) --* When set to SINGLE_FILE, emits program
                          as a single media resource (.ts) file, uses #EXT-X-BYTERANGE tags to index
                          segment for playback.

                          - **SegmentLength** *(integer) --* Length of MPEG-2 Transport Stream
                          segments to create (in seconds). Note that segments will end on the next
                          keyframe after this number of seconds, so actual segment length may be
                          longer.

                          - **SegmentsPerSubdirectory** *(integer) --* Number of segments to write
                          to a subdirectory before starting a new one. directoryStructure must be
                          SINGLE_DIRECTORY for this setting to have an effect.

                          - **StreamInfResolution** *(string) --* Include or exclude RESOLUTION
                          attribute for video in EXT-X-STREAM-INF tag of variant manifest.

                          - **TimedMetadataId3Frame** *(string) --* Indicates ID3 frame that has the
                          timecode.

                          - **TimedMetadataId3Period** *(integer) --* Timed Metadata interval in
                          seconds.

                          - **TimestampDeltaMilliseconds** *(integer) --* Provides an extra
                          millisecond delta offset to fine tune the timestamps.

                        - **MsSmoothGroupSettings** *(dict) --* Required when you set (Type) under
                        (OutputGroups)>(OutputGroupSettings) to MS_SMOOTH_GROUP_SETTINGS.

                          - **AdditionalManifests** *(list) --* By default, the service creates one
                          .ism Microsoft Smooth Streaming manifest for each Microsoft Smooth
                          Streaming output group in your job. This default manifest references every
                          output in the output group. To create additional manifests that reference
                          a subset of the outputs in the output group, specify a list of them here.

                            - *(dict) --* Specify the details for each additional Microsoft Smooth
                            Streaming manifest that you want the service to generate for this output
                            group. Each manifest can reference a different subset of outputs in the
                            group.

                              - **ManifestNameModifier** *(string) --* Specify a name modifier that
                              the service adds to the name of this manifest to make it different
                              from the file names of the other main manifests in the output group.
                              For example, say that the default main manifest for your Microsoft
                              Smooth group is film-name.ismv. If you enter "-no-premium" for this
                              setting, then the file name the service generates for this top-level
                              manifest is film-name-no-premium.ismv.

                              - **SelectedOutputs** *(list) --* Specify the outputs that you want
                              this additional top-level manifest to reference.

                                - *(string) --*

                          - **AudioDeduplication** *(string) --* COMBINE_DUPLICATE_STREAMS combines
                          identical audio encoding settings across a Microsoft Smooth output group
                          into a single audio stream.

                          - **Destination** *(string) --* Use Destination (Destination) to specify
                          the S3 output location and the output filename base. Destination accepts
                          format identifiers. If you do not specify the base filename in the URI,
                          the service will use the filename of the input file. If your job has
                          multiple inputs, the service uses the filename of the first input file.

                          - **DestinationSettings** *(dict) --* Settings associated with the
                          destination. Will vary based on the type of destination

                            - **S3Settings** *(dict) --* Settings associated with S3 destination

                              - **AccessControl** *(dict) --* Optional. Have MediaConvert
                              automatically apply Amazon S3 access control for the outputs in this
                              output group. When you don't use this setting, S3 automatically
                              applies the default access control list PRIVATE.

                                - **CannedAcl** *(string) --* Choose an Amazon S3 canned ACL for
                                MediaConvert to apply to this output.

                              - **Encryption** *(dict) --* Settings for how your job outputs are
                              encrypted as they are uploaded to Amazon S3.

                                - **EncryptionType** *(string) --* Specify how you want your data
                                keys managed. AWS uses data keys to encrypt your content. AWS also
                                encrypts the data keys themselves, using a customer master key
                                (CMK), and then stores the encrypted data keys alongside your
                                encrypted content. Use this setting to specify which AWS service
                                manages the CMK. For simplest set up, choose Amazon S3
                                (SERVER_SIDE_ENCRYPTION_S3). If you want your master key to be
                                managed by AWS Key Management Service (KMS), choose AWS KMS
                                (SERVER_SIDE_ENCRYPTION_KMS). By default, when you choose AWS KMS,
                                KMS uses the AWS managed customer master key (CMK) associated with
                                Amazon S3 to encrypt your data keys. You can optionally choose to
                                specify a different, customer managed CMK. Do so by specifying the
                                Amazon Resource Name (ARN) of the key for the setting KMS ARN
                                (kmsKeyArn).

                                - **KmsKeyArn** *(string) --* Optionally, specify the customer
                                master key (CMK) that you want to use to encrypt the data key that
                                AWS uses to encrypt your output content. Enter the Amazon Resource
                                Name (ARN) of the CMK. To use this setting, you must also set
                                Server-side encryption (S3ServerSideEncryptionType) to AWS KMS
                                (SERVER_SIDE_ENCRYPTION_KMS). If you set Server-side encryption to
                                AWS KMS but don't specify a CMK here, AWS uses the AWS managed CMK
                                associated with Amazon S3.

                          - **Encryption** *(dict) --* If you are using DRM, set DRM System
                          (MsSmoothEncryptionSettings) to specify the value SpekeKeyProvider.

                            - **SpekeKeyProvider** *(dict) --* If your output group type is HLS,
                            DASH, or Microsoft Smooth, use these settings when doing DRM encryption
                            with a SPEKE-compliant key provider. If your output group type is CMAF,
                            use the SpekeKeyProviderCmaf settings instead.

                              - **CertificateArn** *(string) --* If you want your key provider to
                              encrypt the content keys that it provides to MediaConvert, set up a
                              certificate with a master key using AWS Certificate Manager. Specify
                              the certificate's Amazon Resource Name (ARN) here.

                              - **ResourceId** *(string) --* Specify the resource ID that your
                              SPEKE-compliant key provider uses to identify this content.

                              - **SystemIds** *(list) --* Relates to SPEKE implementation. DRM
                              system identifiers. DASH output groups support a max of two system
                              ids. Other group types support one system id. See
                              https://dashif.org/identifiers/content_protection/ for more details.

                                - *(string) --*

                              - **Url** *(string) --* Specify the URL to the key server that your
                              SPEKE-compliant DRM key provider uses to provide keys for encrypting
                              your content.

                          - **FragmentLength** *(integer) --* Use Fragment length (FragmentLength)
                          to specify the mp4 fragment sizes in seconds. Fragment length must be
                          compatible with GOP size and frame rate.

                          - **ManifestEncoding** *(string) --* Use Manifest encoding
                          (MsSmoothManifestEncoding) to specify the encoding format for the server
                          and client manifest. Valid options are utf8 and utf16.

                        - **Type** *(string) --* Type of output group (File group, Apple HLS, DASH
                        ISO, Microsoft Smooth Streaming, CMAF)

                      - **Outputs** *(list) --* This object holds groups of encoding settings, one
                      group of settings per output.

                        - *(dict) --* An output object describes the settings for a single output
                        file or stream in an output group.

                          - **AudioDescriptions** *(list) --* (AudioDescriptions) contains groups of
                          audio encoding settings organized by audio codec. Include one instance of
                          (AudioDescriptions) per output. (AudioDescriptions) can contain multiple
                          groups of encoding settings.

                            - *(dict) --* Description of audio output

                              - **AudioNormalizationSettings** *(dict) --* Advanced audio
                              normalization settings. Ignore these settings unless you need to
                              comply with a loudness standard.

                                - **Algorithm** *(string) --* Choose one of the following audio
                                normalization algorithms: ITU-R BS.1770-1: Ungated loudness. A
                                measurement of ungated average loudness for an entire piece of
                                content, suitable for measurement of short-form content under ATSC
                                recommendation A/85. Supports up to 5.1 audio channels. ITU-R
                                BS.1770-2: Gated loudness. A measurement of gated average loudness
                                compliant with the requirements of EBU-R128. Supports up to 5.1
                                audio channels. ITU-R BS.1770-3: Modified peak. The same loudness
                                measurement algorithm as 1770-2, with an updated true peak
                                measurement. ITU-R BS.1770-4: Higher channel count. Allows for more
                                audio channels than the other algorithms, including configurations
                                such as 7.1.

                                - **AlgorithmControl** *(string) --* When enabled the output audio
                                is corrected using the chosen algorithm. If disabled, the audio will
                                be measured but not adjusted.

                                - **CorrectionGateLevel** *(integer) --* Content measuring above
                                this level will be corrected to the target level. Content measuring
                                below this level will not be corrected. Gating only applies when not
                                using real_time_correction.

                                - **LoudnessLogging** *(string) --* If set to LOG, log each output's
                                audio track loudness to a CSV file.

                                - **PeakCalculation** *(string) --* If set to TRUE_PEAK, calculate
                                and log the TruePeak for each output's audio track loudness.

                                - **TargetLkfs** *(float) --* When you use Audio normalization
                                (AudioNormalizationSettings), optionally use this setting to specify
                                a target loudness. If you don't specify a value here, the encoder
                                chooses a value for you, based on the algorithm that you choose for
                                Algorithm (algorithm). If you choose algorithm 1770-1, the encoder
                                will choose -24 LKFS; otherwise, the encoder will choose -23 LKFS.

                              - **AudioSourceName** *(string) --* Specifies which audio data to use
                              from each input. In the simplest case, specify an "Audio
                              Selector":#inputs-audio_selector by name based on its order within
                              each input. For example if you specify "Audio Selector 3", then the
                              third audio selector will be used from each input. If an input does
                              not have an "Audio Selector 3", then the audio selector marked as
                              "default" in that input will be used. If there is no audio selector
                              marked as "default", silence will be inserted for the duration of that
                              input. Alternatively, an "Audio Selector
                              Group":#inputs-audio_selector_group name may be specified, with
                              similar default/silence behavior. If no audio_source_name is
                              specified, then "Audio Selector 1" will be chosen automatically.

                              - **AudioType** *(integer) --* Applies only if Follow Input Audio Type
                              is unchecked (false). A number between 0 and 255. The following are
                              defined in ISO-IEC 13818-1: 0 = Undefined, 1 =
                                   Clean Effects, 2 =
                              Hearing Impaired, 3 =
                                   Visually Impaired Commentary, 4-255 =
                                        Reserved.

                              - **AudioTypeControl** *(string) --* When set to FOLLOW_INPUT, if the
                              input contains an ISO 639 audio_type, then that value is passed
                              through to the output. If the input contains no ISO 639 audio_type,
                              the value in Audio Type is included in the output. Otherwise the value
                              in Audio Type is included in the output. Note that this field and
                              audioType are both ignored if audioDescriptionBroadcasterMix is set to
                              BROADCASTER_MIXED_AD.

                              - **CodecSettings** *(dict) --* Audio codec settings (CodecSettings)
                              under (AudioDescriptions) contains the group of settings related to
                              audio encoding. The settings in this group vary depending on the value
                              that you choose for Audio codec (Codec). For each codec enum that you
                              choose, define the corresponding settings object. The following lists
                              the codec enum, settings object pairs. * AAC, AacSettings * MP2,
                              Mp2Settings * WAV, WavSettings * AIFF, AiffSettings * AC3, Ac3Settings
                              * EAC3, Eac3Settings * EAC3_ATMOS, Eac3AtmosSettings

                                - **AacSettings** *(dict) --* Required when you set (Codec) under
                                (AudioDescriptions)>(CodecSettings) to the value AAC. The service
                                accepts one of two mutually exclusive groups of AAC settings--VBR
                                and CBR. To select one of these modes, set the value of Bitrate
                                control mode (rateControlMode) to "VBR" or "CBR". In VBR mode, you
                                control the audio quality with the setting VBR quality (vbrQuality).
                                In CBR mode, you use the setting Bitrate (bitrate). Defaults and
                                valid values depend on the rate control mode.

                                  - **AudioDescriptionBroadcasterMix** *(string) --* Choose
                                  BROADCASTER_MIXED_AD when the input contains pre-mixed main audio
                                  + audio description (AD) as a stereo pair. The value for AudioType
                                  will be set to 3, which signals to downstream systems that this
                                  stream contains "broadcaster mixed AD". Note that the input
                                  received by the encoder must contain pre-mixed audio; the encoder
                                  does not perform the mixing. When you choose BROADCASTER_MIXED_AD,
                                  the encoder ignores any values you provide in AudioType and
                                  FollowInputAudioType. Choose NORMAL when the input does not
                                  contain pre-mixed audio + audio description (AD). In this case,
                                  the encoder will use any values you provide for AudioType and
                                  FollowInputAudioType.

                                  - **Bitrate** *(integer) --* Specify the average bitrate in bits
                                  per second. The set of valid values for this setting is: 6000,
                                  8000, 10000, 12000, 14000, 16000, 20000, 24000, 28000, 32000,
                                  40000, 48000, 56000, 64000, 80000, 96000, 112000, 128000, 160000,
                                  192000, 224000, 256000, 288000, 320000, 384000, 448000, 512000,
                                  576000, 640000, 768000, 896000, 1024000. The value you set is also
                                  constrained by the values that you choose for Profile
                                  (codecProfile), Bitrate control mode (codingMode), and Sample rate
                                  (sampleRate). Default values depend on Bitrate control mode and
                                  Profile.

                                  - **CodecProfile** *(string) --* AAC Profile.

                                  - **CodingMode** *(string) --* Mono (Audio Description), Mono,
                                  Stereo, or 5.1 channel layout. Valid values depend on rate control
                                  mode and profile. "1.0 - Audio Description (Receiver Mix)" setting
                                  receives a stereo description plus control track and emits a mono
                                  AAC encode of the description track, with control data emitted in
                                  the PES header as per ETSI TS 101 154 Annex E.

                                  - **RateControlMode** *(string) --* Rate Control Mode.

                                  - **RawFormat** *(string) --* Enables LATM/LOAS AAC output. Note
                                  that if you use LATM/LOAS AAC in an output, you must choose "No
                                  container" for the output container.

                                  - **SampleRate** *(integer) --* Sample rate in Hz. Valid values
                                  depend on rate control mode and profile.

                                  - **Specification** *(string) --* Use MPEG-2 AAC instead of MPEG-4
                                  AAC audio for raw or MPEG-2 Transport Stream containers.

                                  - **VbrQuality** *(string) --* VBR Quality Level - Only used if
                                  rate_control_mode is VBR.

                                - **Ac3Settings** *(dict) --* Required when you set (Codec) under
                                (AudioDescriptions)>(CodecSettings) to the value AC3.

                                  - **Bitrate** *(integer) --* Specify the average bitrate in bits
                                  per second. Valid bitrates depend on the coding mode.

                                  - **BitstreamMode** *(string) --* Specify the bitstream mode for
                                  the AC-3 stream that the encoder emits. For more information about
                                  the AC3 bitstream mode, see ATSC A/52-2012 (Annex E).

                                  - **CodingMode** *(string) --* Dolby Digital coding mode.
                                  Determines number of channels.

                                  - **Dialnorm** *(integer) --* Sets the dialnorm for the output. If
                                  blank and input audio is Dolby Digital, dialnorm will be passed
                                  through.

                                  - **DynamicRangeCompressionProfile** *(string) --* If set to
                                  FILM_STANDARD, adds dynamic range compression signaling to the
                                  output bitstream as defined in the Dolby Digital specification.

                                  - **LfeFilter** *(string) --* Applies a 120Hz lowpass filter to
                                  the LFE channel prior to encoding. Only valid with 3_2_LFE coding
                                  mode.

                                  - **MetadataControl** *(string) --* When set to FOLLOW_INPUT,
                                  encoder metadata will be sourced from the DD, DD+, or DolbyE
                                  decoder that supplied this audio data. If audio was not supplied
                                  from one of these streams, then the static metadata settings will
                                  be used.

                                  - **SampleRate** *(integer) --* This value is always 48000. It
                                  represents the sample rate in Hz.

                                - **AiffSettings** *(dict) --* Required when you set (Codec) under
                                (AudioDescriptions)>(CodecSettings) to the value AIFF.

                                  - **BitDepth** *(integer) --* Specify Bit depth (BitDepth), in
                                  bits per sample, to choose the encoding quality for this audio
                                  track.

                                  - **Channels** *(integer) --* Specify the number of channels in
                                  this output audio track. Valid values are 1 and even numbers up to
                                  64. For example, 1, 2, 4, 6, and so on, up to 64.

                                  - **SampleRate** *(integer) --* Sample rate in hz.

                                - **Codec** *(string) --* Type of Audio codec.

                                - **Eac3AtmosSettings** *(dict) --* Required when you set (Codec)
                                under (AudioDescriptions)>(CodecSettings) to the value EAC3_ATMOS.

                                  - **Bitrate** *(integer) --* Specify the average bitrate in bits
                                  per second. Valid values: 384k, 448k, 640k, 768k

                                  - **BitstreamMode** *(string) --* Specify the bitstream mode for
                                  the E-AC-3 stream that the encoder emits. For more information
                                  about the EAC3 bitstream mode, see ATSC A/52-2012 (Annex E).

                                  - **CodingMode** *(string) --* The coding mode for Dolby Digital
                                  Plus JOC (Atmos) is always 9.1.6 (CODING_MODE_9_1_6).

                                  - **DialogueIntelligence** *(string) --* Enable Dolby Dialogue
                                  Intelligence to adjust loudness based on dialogue analysis.

                                  - **DynamicRangeCompressionLine** *(string) --* Specify the
                                  absolute peak level for a signal with dynamic range compression.

                                  - **DynamicRangeCompressionRf** *(string) --* Specify how the
                                  service limits the audio dynamic range when compressing the audio.

                                  - **LoRoCenterMixLevel** *(float) --* Specify a value for the
                                  following Dolby Atmos setting: Left only/Right only center mix
                                  (Lo/Ro center). MediaConvert uses this value for downmixing. How
                                  the service uses this value depends on the value that you choose
                                  for Stereo downmix (Eac3AtmosStereoDownmix). Valid values: 3.0,
                                  1.5, 0.0, -1.5, -3.0, -4.5, and -6.0.

                                  - **LoRoSurroundMixLevel** *(float) --* Specify a value for the
                                  following Dolby Atmos setting: Left only/Right only (Lo/Ro
                                  surround). MediaConvert uses this value for downmixing. How the
                                  service uses this value depends on the value that you choose for
                                  Stereo downmix (Eac3AtmosStereoDownmix). Valid values: -1.5, -3.0,
                                  -4.5, -6.0, and -60. The value -60 mutes the channel.

                                  - **LtRtCenterMixLevel** *(float) --* Specify a value for the
                                  following Dolby Atmos setting: Left total/Right total center mix
                                  (Lt/Rt center). MediaConvert uses this value for downmixing. How
                                  the service uses this value depends on the value that you choose
                                  for Stereo downmix (Eac3AtmosStereoDownmix). Valid values: 3.0,
                                  1.5, 0.0, -1.5, -3.0, -4.5, and -6.0.

                                  - **LtRtSurroundMixLevel** *(float) --* Specify a value for the
                                  following Dolby Atmos setting: Left total/Right total surround mix
                                  (Lt/Rt surround). MediaConvert uses this value for downmixing. How
                                  the service uses this value depends on the value that you choose
                                  for Stereo downmix (Eac3AtmosStereoDownmix). Valid values: -1.5,
                                  -3.0, -4.5, -6.0, and -60. The value -60 mutes the channel.

                                  - **MeteringMode** *(string) --* Choose how the service meters the
                                  loudness of your audio.

                                  - **SampleRate** *(integer) --* This value is always 48000. It
                                  represents the sample rate in Hz.

                                  - **SpeechThreshold** *(integer) --* Specify the percentage of
                                  audio content that must be speech before the encoder uses the
                                  measured speech loudness as the overall program loudness.

                                  - **StereoDownmix** *(string) --* Choose how the service does
                                  stereo downmixing.

                                  - **SurroundExMode** *(string) --* Specify whether your input
                                  audio has an additional center rear surround channel matrix
                                  encoded into your left and right surround channels.

                                - **Eac3Settings** *(dict) --* Required when you set (Codec) under
                                (AudioDescriptions)>(CodecSettings) to the value EAC3.

                                  - **AttenuationControl** *(string) --* If set to ATTENUATE_3_DB,
                                  applies a 3 dB attenuation to the surround channels. Only used for
                                  3/2 coding mode.

                                  - **Bitrate** *(integer) --* Specify the average bitrate in bits
                                  per second. Valid bitrates depend on the coding mode.

                                  - **BitstreamMode** *(string) --* Specify the bitstream mode for
                                  the E-AC-3 stream that the encoder emits. For more information
                                  about the EAC3 bitstream mode, see ATSC A/52-2012 (Annex E).

                                  - **CodingMode** *(string) --* Dolby Digital Plus coding mode.
                                  Determines number of channels.

                                  - **DcFilter** *(string) --* Activates a DC highpass filter for
                                  all input channels.

                                  - **Dialnorm** *(integer) --* Sets the dialnorm for the output. If
                                  blank and input audio is Dolby Digital Plus, dialnorm will be
                                  passed through.

                                  - **DynamicRangeCompressionLine** *(string) --* Specify the
                                  absolute peak level for a signal with dynamic range compression.

                                  - **DynamicRangeCompressionRf** *(string) --* Specify how the
                                  service limits the audio dynamic range when compressing the audio.

                                  - **LfeControl** *(string) --* When encoding 3/2 audio, controls
                                  whether the LFE channel is enabled

                                  - **LfeFilter** *(string) --* Applies a 120Hz lowpass filter to
                                  the LFE channel prior to encoding. Only valid with 3_2_LFE coding
                                  mode.

                                  - **LoRoCenterMixLevel** *(float) --* Specify a value for the
                                  following Dolby Digital Plus setting: Left only/Right only center
                                  mix (Lo/Ro center). MediaConvert uses this value for downmixing.
                                  How the service uses this value depends on the value that you
                                  choose for Stereo downmix (Eac3StereoDownmix). Valid values: 3.0,
                                  1.5, 0.0, -1.5, -3.0, -4.5, -6.0, and -60. The value -60 mutes the
                                  channel. This setting applies only if you keep the default value
                                  of 3/2 - L, R, C, Ls, Rs (CODING_MODE_3_2) for the setting Coding
                                  mode (Eac3CodingMode). If you choose a different value for Coding
                                  mode, the service ignores Left only/Right only center
                                  (loRoCenterMixLevel).

                                  - **LoRoSurroundMixLevel** *(float) --* Specify a value for the
                                  following Dolby Digital Plus setting: Left only/Right only (Lo/Ro
                                  surround). MediaConvert uses this value for downmixing. How the
                                  service uses this value depends on the value that you choose for
                                  Stereo downmix (Eac3StereoDownmix). Valid values: -1.5, -3.0,
                                  -4.5, -6.0, and -60. The value -60 mutes the channel. This setting
                                  applies only if you keep the default value of 3/2 - L, R, C, Ls,
                                  Rs (CODING_MODE_3_2) for the setting Coding mode (Eac3CodingMode).
                                  If you choose a different value for Coding mode, the service
                                  ignores Left only/Right only surround (loRoSurroundMixLevel).

                                  - **LtRtCenterMixLevel** *(float) --* Specify a value for the
                                  following Dolby Digital Plus setting: Left total/Right total
                                  center mix (Lt/Rt center). MediaConvert uses this value for
                                  downmixing. How the service uses this value depends on the value
                                  that you choose for Stereo downmix (Eac3StereoDownmix). Valid
                                  values: 3.0, 1.5, 0.0, -1.5, -3.0, -4.5, -6.0, and -60. The value
                                  -60 mutes the channel. This setting applies only if you keep the
                                  default value of 3/2 - L, R, C, Ls, Rs (CODING_MODE_3_2) for the
                                  setting Coding mode (Eac3CodingMode). If you choose a different
                                  value for Coding mode, the service ignores Left total/Right total
                                  center (ltRtCenterMixLevel).

                                  - **LtRtSurroundMixLevel** *(float) --* Specify a value for the
                                  following Dolby Digital Plus setting: Left total/Right total
                                  surround mix (Lt/Rt surround). MediaConvert uses this value for
                                  downmixing. How the service uses this value depends on the value
                                  that you choose for Stereo downmix (Eac3StereoDownmix). Valid
                                  values: -1.5, -3.0, -4.5, -6.0, and -60. The value -60 mutes the
                                  channel. This setting applies only if you keep the default value
                                  of 3/2 - L, R, C, Ls, Rs (CODING_MODE_3_2) for the setting Coding
                                  mode (Eac3CodingMode). If you choose a different value for Coding
                                  mode, the service ignores Left total/Right total surround
                                  (ltRtSurroundMixLevel).

                                  - **MetadataControl** *(string) --* When set to FOLLOW_INPUT,
                                  encoder metadata will be sourced from the DD, DD+, or DolbyE
                                  decoder that supplied this audio data. If audio was not supplied
                                  from one of these streams, then the static metadata settings will
                                  be used.

                                  - **PassthroughControl** *(string) --* When set to WHEN_POSSIBLE,
                                  input DD+ audio will be passed through if it is present on the
                                  input. this detection is dynamic over the life of the transcode.
                                  Inputs that alternate between DD+ and non-DD+ content will have a
                                  consistent DD+ output as the system alternates between passthrough
                                  and encoding.

                                  - **PhaseControl** *(string) --* Controls the amount of
                                  phase-shift applied to the surround channels. Only used for 3/2
                                  coding mode.

                                  - **SampleRate** *(integer) --* This value is always 48000. It
                                  represents the sample rate in Hz.

                                  - **StereoDownmix** *(string) --* Choose how the service does
                                  stereo downmixing. This setting only applies if you keep the
                                  default value of 3/2 - L, R, C, Ls, Rs (CODING_MODE_3_2) for the
                                  setting Coding mode (Eac3CodingMode). If you choose a different
                                  value for Coding mode, the service ignores Stereo downmix
                                  (Eac3StereoDownmix).

                                  - **SurroundExMode** *(string) --* When encoding 3/2 audio, sets
                                  whether an extra center back surround channel is matrix encoded
                                  into the left and right surround channels.

                                  - **SurroundMode** *(string) --* When encoding 2/0 audio, sets
                                  whether Dolby Surround is matrix encoded into the two channels.

                                - **Mp2Settings** *(dict) --* Required when you set (Codec) under
                                (AudioDescriptions)>(CodecSettings) to the value MP2.

                                  - **Bitrate** *(integer) --* Specify the average bitrate in bits
                                  per second.

                                  - **Channels** *(integer) --* Set Channels to specify the number
                                  of channels in this output audio track. Choosing Mono in the
                                  console will give you 1 output channel; choosing Stereo will give
                                  you 2. In the API, valid values are 1 and 2.

                                  - **SampleRate** *(integer) --* Sample rate in hz.

                                - **WavSettings** *(dict) --* Required when you set (Codec) under
                                (AudioDescriptions)>(CodecSettings) to the value WAV.

                                  - **BitDepth** *(integer) --* Specify Bit depth (BitDepth), in
                                  bits per sample, to choose the encoding quality for this audio
                                  track.

                                  - **Channels** *(integer) --* Specify the number of channels in
                                  this output audio track. Valid values are 1 and even numbers up to
                                  64. For example, 1, 2, 4, 6, and so on, up to 64.

                                  - **Format** *(string) --* The service defaults to using RIFF for
                                  WAV outputs. If your output audio is likely to exceed 4 GB in file
                                  size, or if you otherwise need the extended support of the RF64
                                  format, set your output WAV file format to RF64.

                                  - **SampleRate** *(integer) --* Sample rate in Hz.

                              - **CustomLanguageCode** *(string) --* Specify the language for this
                              audio output track. The service puts this language code into your
                              output audio track when you set Language code control
                              (AudioLanguageCodeControl) to Use configured (USE_CONFIGURED). The
                              service also uses your specified custom language code when you set
                              Language code control (AudioLanguageCodeControl) to Follow input
                              (FOLLOW_INPUT), but your input file doesn't specify a language code.
                              For all outputs, you can use an ISO 639-2 or ISO 639-3 code. For
                              streaming outputs, you can also use any other code in the full
                              RFC-5646 specification. Streaming outputs are those that are in one of
                              the following output groups: CMAF, DASH ISO, Apple HLS, or Microsoft
                              Smooth Streaming.

                              - **LanguageCode** *(string) --* Indicates the language of the audio
                              output track. The ISO 639 language specified in the 'Language Code'
                              drop down will be used when 'Follow Input Language Code' is not
                              selected or when 'Follow Input Language Code' is selected but there is
                              no ISO 639 language code specified by the input.

                              - **LanguageCodeControl** *(string) --* Specify which source for
                              language code takes precedence for this audio track. When you choose
                              Follow input (FOLLOW_INPUT), the service uses the language code from
                              the input track if it's present. If there's no languge code on the
                              input track, the service uses the code that you specify in the setting
                              Language code (languageCode or customLanguageCode). When you choose
                              Use configured (USE_CONFIGURED), the service uses the language code
                              that you specify.

                              - **RemixSettings** *(dict) --* Advanced audio remixing settings.

                                - **ChannelMapping** *(dict) --* Channel mapping (ChannelMapping)
                                contains the group of fields that hold the remixing value for each
                                channel. Units are in dB. Acceptable values are within the range
                                from -60 (mute) through 6. A setting of 0 passes the input channel
                                unchanged to the output channel (no attenuation or amplification).

                                  - **OutputChannels** *(list) --* List of output channels

                                    - *(dict) --* OutputChannel mapping settings.

                                      - **InputChannels** *(list) --* List of input channels

                                        - *(integer) --*

                                - **ChannelsIn** *(integer) --* Specify the number of audio channels
                                from your input that you want to use in your output. With remixing,
                                you might combine or split the data in these channels, so the number
                                of channels in your final output might be different.

                                - **ChannelsOut** *(integer) --* Specify the number of channels in
                                this output after remixing. Valid values: 1, 2, 4, 6, 8... 64. (1
                                and even numbers to 64.)

                              - **StreamName** *(string) --* Specify a label for this output audio
                              stream. For example, "English", "Director commentary", or "track_2".
                              For streaming outputs, MediaConvert passes this information into
                              destination manifests for display on the end-viewer's player device.
                              For outputs in other output groups, the service ignores this setting.

                          - **CaptionDescriptions** *(list) --* (CaptionDescriptions) contains
                          groups of captions settings. For each output that has captions, include
                          one instance of (CaptionDescriptions). (CaptionDescriptions) can contain
                          multiple groups of captions settings.

                            - *(dict) --* Description of Caption output

                              - **CaptionSelectorName** *(string) --* Specifies which "Caption
                              Selector":#inputs-caption_selector to use from each input when
                              generating captions. The name should be of the format "Caption
                              Selector ", which denotes that the Nth Caption Selector will be used
                              from each input.

                              - **CustomLanguageCode** *(string) --* Specify the language for this
                              captions output track. For most captions output formats, the encoder
                              puts this language information in the output captions metadata. If
                              your output captions format is DVB-Sub or Burn in, the encoder uses
                              this language information when automatically selecting the font script
                              for rendering the captions text. For all outputs, you can use an ISO
                              639-2 or ISO 639-3 code. For streaming outputs, you can also use any
                              other code in the full RFC-5646 specification. Streaming outputs are
                              those that are in one of the following output groups: CMAF, DASH ISO,
                              Apple HLS, or Microsoft Smooth Streaming.

                              - **DestinationSettings** *(dict) --* Specific settings required by
                              destination type. Note that burnin_destination_settings are not
                              available if the source of the caption data is Embedded or Teletext.

                                - **BurninDestinationSettings** *(dict) --* Burn-In Destination
                                Settings.

                                  - **Alignment** *(string) --* If no explicit x_position or
                                  y_position is provided, setting alignment to centered will place
                                  the captions at the bottom center of the output. Similarly,
                                  setting a left alignment will align captions to the bottom left of
                                  the output. If x and y positions are given in conjunction with the
                                  alignment parameter, the font will be justified (either left or
                                  centered) relative to those coordinates. This option is not valid
                                  for source captions that are STL, 608/embedded or teletext. These
                                  source settings are already pre-defined by the caption stream. All
                                  burn-in and DVB-Sub font settings must match.

                                  - **BackgroundColor** *(string) --* Specifies the color of the
                                  rectangle behind the captions. All burn-in and DVB-Sub font
                                  settings must match.

                                  - **BackgroundOpacity** *(integer) --* Specifies the opacity of
                                  the background rectangle. 255 is opaque; 0 is transparent. Leaving
                                  this parameter blank is equivalent to setting it to 0
                                  (transparent). All burn-in and DVB-Sub font settings must match.

                                  - **FontColor** *(string) --* Specifies the color of the burned-in
                                  captions. This option is not valid for source captions that are
                                  STL, 608/embedded or teletext. These source settings are already
                                  pre-defined by the caption stream. All burn-in and DVB-Sub font
                                  settings must match.

                                  - **FontOpacity** *(integer) --* Specifies the opacity of the
                                  burned-in captions. 255 is opaque; 0 is transparent. All burn-in
                                  and DVB-Sub font settings must match.

                                  - **FontResolution** *(integer) --* Font resolution in DPI (dots
                                  per inch); default is 96 dpi. All burn-in and DVB-Sub font
                                  settings must match.

                                  - **FontScript** *(string) --* Provide the font script, using an
                                  ISO 15924 script code, if the LanguageCode is not sufficient for
                                  determining the script type. Where LanguageCode or
                                  CustomLanguageCode is sufficient, use "AUTOMATIC" or leave unset.
                                  This is used to help determine the appropriate font for rendering
                                  burn-in captions.

                                  - **FontSize** *(integer) --* A positive integer indicates the
                                  exact font size in points. Set to 0 for automatic font size
                                  selection. All burn-in and DVB-Sub font settings must match.

                                  - **OutlineColor** *(string) --* Specifies font outline color.
                                  This option is not valid for source captions that are either
                                  608/embedded or teletext. These source settings are already
                                  pre-defined by the caption stream. All burn-in and DVB-Sub font
                                  settings must match.

                                  - **OutlineSize** *(integer) --* Specifies font outline size in
                                  pixels. This option is not valid for source captions that are
                                  either 608/embedded or teletext. These source settings are already
                                  pre-defined by the caption stream. All burn-in and DVB-Sub font
                                  settings must match.

                                  - **ShadowColor** *(string) --* Specifies the color of the shadow
                                  cast by the captions. All burn-in and DVB-Sub font settings must
                                  match.

                                  - **ShadowOpacity** *(integer) --* Specifies the opacity of the
                                  shadow. 255 is opaque; 0 is transparent. Leaving this parameter
                                  blank is equivalent to setting it to 0 (transparent). All burn-in
                                  and DVB-Sub font settings must match.

                                  - **ShadowXOffset** *(integer) --* Specifies the horizontal offset
                                  of the shadow relative to the captions in pixels. A value of -2
                                  would result in a shadow offset 2 pixels to the left. All burn-in
                                  and DVB-Sub font settings must match.

                                  - **ShadowYOffset** *(integer) --* Specifies the vertical offset
                                  of the shadow relative to the captions in pixels. A value of -2
                                  would result in a shadow offset 2 pixels above the text. All
                                  burn-in and DVB-Sub font settings must match.

                                  - **TeletextSpacing** *(string) --* Only applies to jobs with
                                  input captions in Teletext or STL formats. Specify whether the
                                  spacing between letters in your captions is set by the captions
                                  grid or varies depending on letter width. Choose fixed grid to
                                  conform to the spacing specified in the captions file more
                                  accurately. Choose proportional to make the text easier to read if
                                  the captions are closed caption.

                                  - **XPosition** *(integer) --* Specifies the horizontal position
                                  of the caption relative to the left side of the output in pixels.
                                  A value of 10 would result in the captions starting 10 pixels from
                                  the left of the output. If no explicit x_position is provided, the
                                  horizontal caption position will be determined by the alignment
                                  parameter. This option is not valid for source captions that are
                                  STL, 608/embedded or teletext. These source settings are already
                                  pre-defined by the caption stream. All burn-in and DVB-Sub font
                                  settings must match.

                                  - **YPosition** *(integer) --* Specifies the vertical position of
                                  the caption relative to the top of the output in pixels. A value
                                  of 10 would result in the captions starting 10 pixels from the top
                                  of the output. If no explicit y_position is provided, the caption
                                  will be positioned towards the bottom of the output. This option
                                  is not valid for source captions that are STL, 608/embedded or
                                  teletext. These source settings are already pre-defined by the
                                  caption stream. All burn-in and DVB-Sub font settings must match.

                                - **DestinationType** *(string) --* Specify the format for this set
                                of captions on this output. The default format is embedded without
                                SCTE-20. Other options are embedded with SCTE-20, burn-in, DVB-sub,
                                IMSC, SCC, SRT, teletext, TTML, and web-VTT. If you are using
                                SCTE-20, choose SCTE-20 plus embedded (SCTE20_PLUS_EMBEDDED) to
                                create an output that complies with the SCTE-43 spec. To create a
                                non-compliant output where the embedded captions come first, choose
                                Embedded plus SCTE-20 (EMBEDDED_PLUS_SCTE20).

                                - **DvbSubDestinationSettings** *(dict) --* DVB-Sub Destination
                                Settings

                                  - **Alignment** *(string) --* If no explicit x_position or
                                  y_position is provided, setting alignment to centered will place
                                  the captions at the bottom center of the output. Similarly,
                                  setting a left alignment will align captions to the bottom left of
                                  the output. If x and y positions are given in conjunction with the
                                  alignment parameter, the font will be justified (either left or
                                  centered) relative to those coordinates. This option is not valid
                                  for source captions that are STL, 608/embedded or teletext. These
                                  source settings are already pre-defined by the caption stream. All
                                  burn-in and DVB-Sub font settings must match.

                                  - **BackgroundColor** *(string) --* Specifies the color of the
                                  rectangle behind the captions. All burn-in and DVB-Sub font
                                  settings must match.

                                  - **BackgroundOpacity** *(integer) --* Specifies the opacity of
                                  the background rectangle. 255 is opaque; 0 is transparent. Leaving
                                  this parameter blank is equivalent to setting it to 0
                                  (transparent). All burn-in and DVB-Sub font settings must match.

                                  - **FontColor** *(string) --* Specifies the color of the burned-in
                                  captions. This option is not valid for source captions that are
                                  STL, 608/embedded or teletext. These source settings are already
                                  pre-defined by the caption stream. All burn-in and DVB-Sub font
                                  settings must match.

                                  - **FontOpacity** *(integer) --* Specifies the opacity of the
                                  burned-in captions. 255 is opaque; 0 is transparent. All burn-in
                                  and DVB-Sub font settings must match.

                                  - **FontResolution** *(integer) --* Font resolution in DPI (dots
                                  per inch); default is 96 dpi. All burn-in and DVB-Sub font
                                  settings must match.

                                  - **FontScript** *(string) --* Provide the font script, using an
                                  ISO 15924 script code, if the LanguageCode is not sufficient for
                                  determining the script type. Where LanguageCode or
                                  CustomLanguageCode is sufficient, use "AUTOMATIC" or leave unset.
                                  This is used to help determine the appropriate font for rendering
                                  DVB-Sub captions.

                                  - **FontSize** *(integer) --* A positive integer indicates the
                                  exact font size in points. Set to 0 for automatic font size
                                  selection. All burn-in and DVB-Sub font settings must match.

                                  - **OutlineColor** *(string) --* Specifies font outline color.
                                  This option is not valid for source captions that are either
                                  608/embedded or teletext. These source settings are already
                                  pre-defined by the caption stream. All burn-in and DVB-Sub font
                                  settings must match.

                                  - **OutlineSize** *(integer) --* Specifies font outline size in
                                  pixels. This option is not valid for source captions that are
                                  either 608/embedded or teletext. These source settings are already
                                  pre-defined by the caption stream. All burn-in and DVB-Sub font
                                  settings must match.

                                  - **ShadowColor** *(string) --* Specifies the color of the shadow
                                  cast by the captions. All burn-in and DVB-Sub font settings must
                                  match.

                                  - **ShadowOpacity** *(integer) --* Specifies the opacity of the
                                  shadow. 255 is opaque; 0 is transparent. Leaving this parameter
                                  blank is equivalent to setting it to 0 (transparent). All burn-in
                                  and DVB-Sub font settings must match.

                                  - **ShadowXOffset** *(integer) --* Specifies the horizontal offset
                                  of the shadow relative to the captions in pixels. A value of -2
                                  would result in a shadow offset 2 pixels to the left. All burn-in
                                  and DVB-Sub font settings must match.

                                  - **ShadowYOffset** *(integer) --* Specifies the vertical offset
                                  of the shadow relative to the captions in pixels. A value of -2
                                  would result in a shadow offset 2 pixels above the text. All
                                  burn-in and DVB-Sub font settings must match.

                                  - **SubtitlingType** *(string) --* Specify whether your DVB
                                  subtitles are standard or for hearing impaired. Choose hearing
                                  impaired if your subtitles include audio descriptions and
                                  dialogue. Choose standard if your subtitles include only dialogue.

                                  - **TeletextSpacing** *(string) --* Only applies to jobs with
                                  input captions in Teletext or STL formats. Specify whether the
                                  spacing between letters in your captions is set by the captions
                                  grid or varies depending on letter width. Choose fixed grid to
                                  conform to the spacing specified in the captions file more
                                  accurately. Choose proportional to make the text easier to read if
                                  the captions are closed caption.

                                  - **XPosition** *(integer) --* Specifies the horizontal position
                                  of the caption relative to the left side of the output in pixels.
                                  A value of 10 would result in the captions starting 10 pixels from
                                  the left of the output. If no explicit x_position is provided, the
                                  horizontal caption position will be determined by the alignment
                                  parameter. This option is not valid for source captions that are
                                  STL, 608/embedded or teletext. These source settings are already
                                  pre-defined by the caption stream. All burn-in and DVB-Sub font
                                  settings must match.

                                  - **YPosition** *(integer) --* Specifies the vertical position of
                                  the caption relative to the top of the output in pixels. A value
                                  of 10 would result in the captions starting 10 pixels from the top
                                  of the output. If no explicit y_position is provided, the caption
                                  will be positioned towards the bottom of the output. This option
                                  is not valid for source captions that are STL, 608/embedded or
                                  teletext. These source settings are already pre-defined by the
                                  caption stream. All burn-in and DVB-Sub font settings must match.

                                - **EmbeddedDestinationSettings** *(dict) --* Settings specific to
                                embedded/ancillary caption outputs, including 608/708 Channel
                                destination number.

                                  - **Destination608ChannelNumber** *(integer) --* Ignore this
                                  setting unless your input captions are SCC format and your output
                                  captions are embedded in the video stream. Specify a CC number for
                                  each captions channel in this output. If you have two channels,
                                  choose CC numbers that aren't in the same field. For example,
                                  choose 1 and 3. For more information, see
                                  https://docs.aws.amazon.com/console/mediaconvert/dual-scc-to-embedded.

                                  - **Destination708ServiceNumber** *(integer) --* Ignore this
                                  setting unless your input captions are SCC format and you want
                                  both 608 and 708 captions embedded in your output stream.
                                  Optionally, specify the 708 service number for each output
                                  captions channel. Choose a different number for each channel. To
                                  use this setting, also set Force 608 to 708 upconvert
                                  (Convert608To708) to Upconvert (UPCONVERT) in your input captions
                                  selector settings. If you choose to upconvert but don't specify a
                                  708 service number, MediaConvert uses the number that you specify
                                  for CC channel number (destination608ChannelNumber) for the 708
                                  service number. For more information, see
                                  https://docs.aws.amazon.com/console/mediaconvert/dual-scc-to-embedded.

                                - **ImscDestinationSettings** *(dict) --* Settings specific to IMSC
                                caption outputs.

                                  - **StylePassthrough** *(string) --* Keep this setting enabled to
                                  have MediaConvert use the font style and position information from
                                  the captions source in the output. This option is available only
                                  when your input captions are CFF-TT, IMSC, SMPTE-TT, or TTML.
                                  Disable this setting for simplified output captions.

                                - **SccDestinationSettings** *(dict) --* Settings for SCC caption
                                output.

                                  - **Framerate** *(string) --* Set Framerate
                                  (SccDestinationFramerate) to make sure that the captions and the
                                  video are synchronized in the output. Specify a frame rate that
                                  matches the frame rate of the associated video. If the video frame
                                  rate is 29.97, choose 29.97 dropframe (FRAMERATE_29_97_DROPFRAME)
                                  only if the video has video_insertion=
                                      true and
                                  drop_frame_timecode=
                                      true; otherwise, choose 29.97 non-dropframe
                                  (FRAMERATE_29_97_NON_DROPFRAME).

                                - **TeletextDestinationSettings** *(dict) --* Settings for Teletext
                                caption output

                                  - **PageNumber** *(string) --* Set pageNumber to the Teletext page
                                  number for the destination captions for this output. This value
                                  must be a three-digit hexadecimal string; strings ending in -FF
                                  are invalid. If you are passing through the entire set of Teletext
                                  data, do not use this field.

                                  - **PageTypes** *(list) --* Specify the page types for this
                                  Teletext page. If you don't specify a value here, the service sets
                                  the page type to the default value Subtitle (PAGE_TYPE_SUBTITLE).
                                  If you pass through the entire set of Teletext data, don't use
                                  this field. When you pass through a set of Teletext pages, your
                                  output has the same page types as your input.

                                    - *(string) --* A page type as defined in the standard ETSI EN
                                    300 468, Table 94

                                - **TtmlDestinationSettings** *(dict) --* Settings specific to TTML
                                caption outputs, including Pass style information
                                (TtmlStylePassthrough).

                                  - **StylePassthrough** *(string) --* Pass through style and
                                  position information from a TTML-like input source (TTML,
                                  SMPTE-TT, CFF-TT) to the CFF-TT output or TTML output.

                              - **LanguageCode** *(string) --* Specify the language of this captions
                              output track. For most captions output formats, the encoder puts this
                              language information in the output captions metadata. If your output
                              captions format is DVB-Sub or Burn in, the encoder uses this language
                              information to choose the font language for rendering the captions
                              text.

                              - **LanguageDescription** *(string) --* Specify a label for this set
                              of output captions. For example, "English", "Director commentary", or
                              "track_2". For streaming outputs, MediaConvert passes this information
                              into destination manifests for display on the end-viewer's player
                              device. For outputs in other output groups, the service ignores this
                              setting.

                          - **ContainerSettings** *(dict) --* Container specific settings.

                            - **Container** *(string) --* Container for this output. Some containers
                            require a container settings object. If not specified, the default
                            object will be created.

                            - **F4vSettings** *(dict) --* Settings for F4v container

                              - **MoovPlacement** *(string) --* If set to PROGRESSIVE_DOWNLOAD, the
                              MOOV atom is relocated to the beginning of the archive as required for
                              progressive downloading. Otherwise it is placed normally at the end.

                            - **M2tsSettings** *(dict) --* MPEG-2 TS container settings. These apply
                            to outputs in a File output group when the output's container
                            (ContainerType) is MPEG-2 Transport Stream (M2TS). In these assets, data
                            is organized by the program map table (PMT). Each transport stream
                            program contains subsets of data, including audio, video, and metadata.
                            Each of these subsets of data has a numerical label called a packet
                            identifier (PID). Each transport stream program corresponds to one
                            MediaConvert output. The PMT lists the types of data in a program along
                            with their PID. Downstream systems and players use the program map table
                            to look up the PID for each type of data it accesses and then uses the
                            PIDs to locate specific data within the asset.

                              - **AudioBufferModel** *(string) --* Selects between the DVB and ATSC
                              buffer models for Dolby Digital audio.

                              - **AudioFramesPerPes** *(integer) --* The number of audio frames to
                              insert for each PES packet.

                              - **AudioPids** *(list) --* Specify the packet identifiers (PIDs) for
                              any elementary audio streams you include in this output. Specify
                              multiple PIDs as a JSON array. Default is the range 482-492.

                                - *(integer) --*

                              - **Bitrate** *(integer) --* Specify the output bitrate of the
                              transport stream in bits per second. Setting to 0 lets the muxer
                              automatically determine the appropriate bitrate. Other common values
                              are 3750000, 7500000, and 15000000.

                              - **BufferModel** *(string) --* Controls what buffer model to use for
                              accurate interleaving. If set to MULTIPLEX, use multiplex buffer
                              model. If set to NONE, this can lead to lower latency, but low-memory
                              devices may not be able to play back the stream without interruptions.

                              - **DvbNitSettings** *(dict) --* Inserts DVB Network Information Table
                              (NIT) at the specified table repetition interval.

                                - **NetworkId** *(integer) --* The numeric value placed in the
                                Network Information Table (NIT).

                                - **NetworkName** *(string) --* The network name text placed in the
                                network_name_descriptor inside the Network Information Table.
                                Maximum length is 256 characters.

                                - **NitInterval** *(integer) --* The number of milliseconds between
                                instances of this table in the output transport stream.

                              - **DvbSdtSettings** *(dict) --* Inserts DVB Service Description Table
                              (NIT) at the specified table repetition interval.

                                - **OutputSdt** *(string) --* Selects method of inserting SDT
                                information into output stream. "Follow input SDT" copies SDT
                                information from input stream to output stream. "Follow input SDT if
                                present" copies SDT information from input stream to output stream
                                if SDT information is present in the input, otherwise it will fall
                                back on the user-defined values. Enter "SDT Manually" means user
                                will enter the SDT information. "No SDT" means output stream will
                                not contain SDT information.

                                - **SdtInterval** *(integer) --* The number of milliseconds between
                                instances of this table in the output transport stream.

                                - **ServiceName** *(string) --* The service name placed in the
                                service_descriptor in the Service Description Table. Maximum length
                                is 256 characters.

                                - **ServiceProviderName** *(string) --* The service provider name
                                placed in the service_descriptor in the Service Description Table.
                                Maximum length is 256 characters.

                              - **DvbSubPids** *(list) --* Specify the packet identifiers (PIDs) for
                              DVB subtitle data included in this output. Specify multiple PIDs as a
                              JSON array. Default is the range 460-479.

                                - *(integer) --*

                              - **DvbTdtSettings** *(dict) --* Inserts DVB Time and Date Table (TDT)
                              at the specified table repetition interval.

                                - **TdtInterval** *(integer) --* The number of milliseconds between
                                instances of this table in the output transport stream.

                              - **DvbTeletextPid** *(integer) --* Specify the packet identifier
                              (PID) for DVB teletext data you include in this output. Default is
                              499.

                              - **EbpAudioInterval** *(string) --* When set to
                              VIDEO_AND_FIXED_INTERVALS, audio EBP markers will be added to
                              partitions 3 and 4. The interval between these additional markers will
                              be fixed, and will be slightly shorter than the video EBP marker
                              interval. When set to VIDEO_INTERVAL, these additional markers will
                              not be inserted. Only applicable when EBP segmentation markers are is
                              selected (segmentationMarkers is EBP or EBP_LEGACY).

                              - **EbpPlacement** *(string) --* Selects which PIDs to place EBP
                              markers on. They can either be placed only on the video PID, or on
                              both the video PID and all audio PIDs. Only applicable when EBP
                              segmentation markers are is selected (segmentationMarkers is EBP or
                              EBP_LEGACY).

                              - **EsRateInPes** *(string) --* Controls whether to include the ES
                              Rate field in the PES header.

                              - **ForceTsVideoEbpOrder** *(string) --* Keep the default value
                              (DEFAULT) unless you know that your audio EBP markers are incorrectly
                              appearing before your video EBP markers. To correct this problem, set
                              this value to Force (FORCE).

                              - **FragmentTime** *(float) --* The length, in seconds, of each
                              fragment. Only used with EBP markers.

                              - **MaxPcrInterval** *(integer) --* Specify the maximum time, in
                              milliseconds, between Program Clock References (PCRs) inserted into
                              the transport stream.

                              - **MinEbpInterval** *(integer) --* When set, enforces that Encoder
                              Boundary Points do not come within the specified time interval of each
                              other by looking ahead at input video. If another EBP is going to come
                              in within the specified time interval, the current EBP is not emitted,
                              and the segment is "stretched" to the next marker. The lookahead value
                              does not add latency to the system. The Live Event must be configured
                              elsewhere to create sufficient latency to make the lookahead accurate.

                              - **NielsenId3** *(string) --* If INSERT, Nielsen inaudible tones for
                              media tracking will be detected in the input audio and an equivalent
                              ID3 tag will be inserted in the output.

                              - **NullPacketBitrate** *(float) --* Value in bits per second of extra
                              null packets to insert into the transport stream. This can be used if
                              a downstream encryption system requires periodic null packets.

                              - **PatInterval** *(integer) --* The number of milliseconds between
                              instances of this table in the output transport stream.

                              - **PcrControl** *(string) --* When set to PCR_EVERY_PES_PACKET, a
                              Program Clock Reference value is inserted for every Packetized
                              Elementary Stream (PES) header. This is effective only when the PCR
                              PID is the same as the video or audio elementary stream.

                              - **PcrPid** *(integer) --* Specify the packet identifier (PID) for
                              the program clock reference (PCR) in this output. If you do not
                              specify a value, the service will use the value for Video PID
                              (VideoPid).

                              - **PmtInterval** *(integer) --* Specify the number of milliseconds
                              between instances of the program map table (PMT) in the output
                              transport stream.

                              - **PmtPid** *(integer) --* Specify the packet identifier (PID) for
                              the program map table (PMT) itself. Default is 480.

                              - **PrivateMetadataPid** *(integer) --* Specify the packet identifier
                              (PID) of the private metadata stream. Default is 503.

                              - **ProgramNumber** *(integer) --* Use Program number (programNumber)
                              to specify the program number used in the program map table (PMT) for
                              this output. Default is 1. Program numbers and program map tables are
                              parts of MPEG-2 transport stream containers, used for organizing data.

                              - **RateMode** *(string) --* When set to CBR, inserts null packets
                              into transport stream to fill specified bitrate. When set to VBR, the
                              bitrate setting acts as the maximum bitrate, but the output will not
                              be padded up to that bitrate.

                              - **Scte35Esam** *(dict) --* Include this in your job settings to put
                              SCTE-35 markers in your HLS and transport stream outputs at the
                              insertion points that you specify in an ESAM XML document. Provide the
                              document in the setting SCC XML (sccXml).

                                - **Scte35EsamPid** *(integer) --* Packet Identifier (PID) of the
                                SCTE-35 stream in the transport stream generated by ESAM.

                              - **Scte35Pid** *(integer) --* Specify the packet identifier (PID) of
                              the SCTE-35 stream in the transport stream.

                              - **Scte35Source** *(string) --* For SCTE-35 markers from your input--
                              Choose Passthrough (PASSTHROUGH) if you want SCTE-35 markers that
                              appear in your input to also appear in this output. Choose None (NONE)
                              if you don't want SCTE-35 markers in this output. For SCTE-35 markers
                              from an ESAM XML document-- Choose None (NONE). Also provide the ESAM
                              XML as a string in the setting Signal processing notification XML
                              (sccXml). Also enable ESAM SCTE-35 (include the property scte35Esam).

                              - **SegmentationMarkers** *(string) --* Inserts segmentation markers
                              at each segmentation_time period. rai_segstart sets the Random Access
                              Indicator bit in the adaptation field. rai_adapt sets the RAI bit and
                              adds the current timecode in the private data bytes. psi_segstart
                              inserts PAT and PMT tables at the start of segments. ebp adds Encoder
                              Boundary Point information to the adaptation field as per OpenCable
                              specification OC-SP-EBP-I01-130118. ebp_legacy adds Encoder Boundary
                              Point information to the adaptation field using a legacy proprietary
                              format.

                              - **SegmentationStyle** *(string) --* The segmentation style parameter
                              controls how segmentation markers are inserted into the transport
                              stream. With avails, it is possible that segments may be truncated,
                              which can influence where future segmentation markers are inserted.
                              When a segmentation style of "reset_cadence" is selected and a segment
                              is truncated due to an avail, we will reset the segmentation cadence.
                              This means the subsequent segment will have a duration of of
                              $segmentation_time seconds. When a segmentation style of
                              "maintain_cadence" is selected and a segment is truncated due to an
                              avail, we will not reset the segmentation cadence. This means the
                              subsequent segment will likely be truncated as well. However, all
                              segments after that will have a duration of $segmentation_time
                              seconds. Note that EBP lookahead is a slight exception to this rule.

                              - **SegmentationTime** *(float) --* Specify the length, in seconds, of
                              each segment. Required unless markers is set to _none_.

                              - **TimedMetadataPid** *(integer) --* Specify the packet identifier
                              (PID) for timed metadata in this output. Default is 502.

                              - **TransportStreamId** *(integer) --* Specify the ID for the
                              transport stream itself in the program map table for this output.
                              Transport stream IDs and program map tables are parts of MPEG-2
                              transport stream containers, used for organizing data.

                              - **VideoPid** *(integer) --* Specify the packet identifier (PID) of
                              the elementary video stream in the transport stream.

                            - **M3u8Settings** *(dict) --* Settings for TS segments in HLS

                              - **AudioFramesPerPes** *(integer) --* The number of audio frames to
                              insert for each PES packet.

                              - **AudioPids** *(list) --* Packet Identifier (PID) of the elementary
                              audio stream(s) in the transport stream. Multiple values are accepted,
                              and can be entered in ranges and/or by comma separation.

                                - *(integer) --*

                              - **NielsenId3** *(string) --* If INSERT, Nielsen inaudible tones for
                              media tracking will be detected in the input audio and an equivalent
                              ID3 tag will be inserted in the output.

                              - **PatInterval** *(integer) --* The number of milliseconds between
                              instances of this table in the output transport stream.

                              - **PcrControl** *(string) --* When set to PCR_EVERY_PES_PACKET a
                              Program Clock Reference value is inserted for every Packetized
                              Elementary Stream (PES) header. This parameter is effective only when
                              the PCR PID is the same as the video or audio elementary stream.

                              - **PcrPid** *(integer) --* Packet Identifier (PID) of the Program
                              Clock Reference (PCR) in the transport stream. When no value is given,
                              the encoder will assign the same value as the Video PID.

                              - **PmtInterval** *(integer) --* The number of milliseconds between
                              instances of this table in the output transport stream.

                              - **PmtPid** *(integer) --* Packet Identifier (PID) for the Program
                              Map Table (PMT) in the transport stream.

                              - **PrivateMetadataPid** *(integer) --* Packet Identifier (PID) of the
                              private metadata stream in the transport stream.

                              - **ProgramNumber** *(integer) --* The value of the program number
                              field in the Program Map Table.

                              - **Scte35Pid** *(integer) --* Packet Identifier (PID) of the SCTE-35
                              stream in the transport stream.

                              - **Scte35Source** *(string) --* For SCTE-35 markers from your input--
                              Choose Passthrough (PASSTHROUGH) if you want SCTE-35 markers that
                              appear in your input to also appear in this output. Choose None (NONE)
                              if you don't want SCTE-35 markers in this output. For SCTE-35 markers
                              from an ESAM XML document-- Choose None (NONE) if you don't want
                              manifest conditioning. Choose Passthrough (PASSTHROUGH) and choose Ad
                              markers (adMarkers) if you do want manifest conditioning. In both
                              cases, also provide the ESAM XML as a string in the setting Signal
                              processing notification XML (sccXml).

                              - **TimedMetadata** *(string) --* Applies only to HLS outputs. Use
                              this setting to specify whether the service inserts the ID3 timed
                              metadata from the input in this output.

                              - **TimedMetadataPid** *(integer) --* Packet Identifier (PID) of the
                              timed metadata stream in the transport stream.

                              - **TransportStreamId** *(integer) --* The value of the transport
                              stream ID field in the Program Map Table.

                              - **VideoPid** *(integer) --* Packet Identifier (PID) of the
                              elementary video stream in the transport stream.

                            - **MovSettings** *(dict) --* Settings for MOV Container.

                              - **ClapAtom** *(string) --* When enabled, include 'clap' atom if
                              appropriate for the video output settings.

                              - **CslgAtom** *(string) --* When enabled, file composition times will
                              start at zero, composition times in the 'ctts' (composition time to
                              sample) box for B-frames will be negative, and a 'cslg' (composition
                              shift least greatest) box will be included per 14496-1 amendment 1.
                              This improves compatibility with Apple players and tools.

                              - **Mpeg2FourCCControl** *(string) --* When set to XDCAM, writes MPEG2
                              video streams into the QuickTime file using XDCAM fourcc codes. This
                              increases compatibility with Apple editors and players, but may
                              decrease compatibility with other players. Only applicable when the
                              video codec is MPEG2.

                              - **PaddingControl** *(string) --* If set to OMNEON, inserts
                              Omneon-compatible padding

                              - **Reference** *(string) --* Always keep the default value
                              (SELF_CONTAINED) for this setting.

                            - **Mp4Settings** *(dict) --* Settings for MP4 container. You can create
                            audio-only AAC outputs with this container.

                              - **CslgAtom** *(string) --* When enabled, file composition times will
                              start at zero, composition times in the 'ctts' (composition time to
                              sample) box for B-frames will be negative, and a 'cslg' (composition
                              shift least greatest) box will be included per 14496-1 amendment 1.
                              This improves compatibility with Apple players and tools.

                              - **FreeSpaceBox** *(string) --* Inserts a free-space box immediately
                              after the moov box.

                              - **MoovPlacement** *(string) --* If set to PROGRESSIVE_DOWNLOAD, the
                              MOOV atom is relocated to the beginning of the archive as required for
                              progressive downloading. Otherwise it is placed normally at the end.

                              - **Mp4MajorBrand** *(string) --* Overrides the "Major Brand" field in
                              the output file. Usually not necessary to specify.

                            - **MpdSettings** *(dict) --* Settings for MP4 segments in DASH

                              - **CaptionContainerType** *(string) --* Use this setting only in DASH
                              output groups that include sidecar TTML or IMSC captions. You specify
                              sidecar captions in a separate output from your audio and video.
                              Choose Raw (RAW) for captions in a single XML file in a raw container.
                              Choose Fragmented MPEG-4 (FRAGMENTED_MP4) for captions in XML format
                              contained within fragmented MP4 files. This set of fragmented MP4
                              files is separate from your video and audio fragmented MP4 files.

                              - **Scte35Esam** *(string) --* Use this setting only when you specify
                              SCTE-35 markers from ESAM. Choose INSERT to put SCTE-35 markers in
                              this output at the insertion points that you specify in an ESAM XML
                              document. Provide the document in the setting SCC XML (sccXml).

                              - **Scte35Source** *(string) --* Ignore this setting unless you have
                              SCTE-35 markers in your input video file. Choose Passthrough
                              (PASSTHROUGH) if you want SCTE-35 markers that appear in your input to
                              also appear in this output. Choose None (NONE) if you don't want those
                              SCTE-35 markers in this output.

                          - **Extension** *(string) --* Use Extension (Extension) to specify the
                          file extension for outputs in File output groups. If you do not specify a
                          value, the service will use default extensions by container type as
                          follows * MPEG-2 transport stream, m2ts * Quicktime, mov * MXF container,
                          mxf * MPEG-4 container, mp4 * No Container, the service will use codec
                          extensions (e.g. AAC, H265, H265, AC3)

                          - **NameModifier** *(string) --* Use Name modifier (NameModifier) to have
                          the service add a string to the end of each output filename. You specify
                          the base filename as part of your destination URI. When you create
                          multiple outputs in the same output group, Name modifier (NameModifier) is
                          required. Name modifier also accepts format identifiers. For DASH ISO
                          outputs, if you use the format identifiers $Number$ or $Time$ in one
                          output, you must use them in the same way in all outputs of the output
                          group.

                          - **OutputSettings** *(dict) --* Specific settings for this type of
                          output.

                            - **HlsSettings** *(dict) --* Settings for HLS output groups

                              - **AudioGroupId** *(string) --* Specifies the group to which the
                              audio Rendition belongs.

                              - **AudioOnlyContainer** *(string) --* Use this setting only in
                              audio-only outputs. Choose MPEG-2 Transport Stream (M2TS) to create a
                              file in an MPEG2-TS container. Keep the default value Automatic
                              (AUTOMATIC) to create an audio-only file in a raw container.
                              Regardless of the value that you specify here, if this output has
                              video, the service will place the output into an MPEG2-TS container.

                              - **AudioRenditionSets** *(string) --* List all the audio groups that
                              are used with the video output stream. Input all the audio GROUP-IDs
                              that are associated to the video, separate by ','.

                              - **AudioTrackType** *(string) --* Four types of audio-only tracks are
                              supported: Audio-Only Variant Stream The client can play back this
                              audio-only stream instead of video in low-bandwidth scenarios.
                              Represented as an EXT-X-STREAM-INF in the HLS manifest. Alternate
                              Audio, Auto Select, Default Alternate rendition that the client should
                              try to play back by default. Represented as an EXT-X-MEDIA in the HLS
                              manifest with DEFAULT=YES, AUTOSELECT=
                                  YES Alternate Audio, Auto
                              Select, Not Default Alternate rendition that the client may try to
                              play back by default. Represented as an EXT-X-MEDIA in the HLS
                              manifest with DEFAULT=NO, AUTOSELECT=
                                  YES Alternate Audio, not Auto
                              Select Alternate rendition that the client will not try to play back
                              by default. Represented as an EXT-X-MEDIA in the HLS manifest with
                              DEFAULT=NO, AUTOSELECT=NO

                              - **IFrameOnlyManifest** *(string) --* When set to INCLUDE, writes
                              I-Frame Only Manifest in addition to the HLS manifest

                              - **SegmentModifier** *(string) --* String concatenated to end of
                              segment filenames. Accepts "Format
                              Identifiers":#format_identifier_parameters.

                          - **Preset** *(string) --* Use Preset (Preset) to specifiy a preset for
                          your transcoding settings. Provide the system or custom preset name. You
                          can specify either Preset (Preset) or Container settings
                          (ContainerSettings), but not both.

                          - **VideoDescription** *(dict) --* (VideoDescription) contains a group of
                          video encoding settings. The specific video settings depend on the video
                          codec that you choose when you specify a value for Video codec (codec).
                          Include one instance of (VideoDescription) per output.

                            - **AfdSignaling** *(string) --* This setting only applies to H.264,
                            H.265, and MPEG2 outputs. Use Insert AFD signaling (AfdSignaling) to
                            specify whether the service includes AFD values in the output video data
                            and what those values are. * Choose None to remove all AFD values from
                            this output. * Choose Fixed to ignore input AFD values and instead
                            encode the value specified in the job. * Choose Auto to calculate output
                            AFD values based on the input AFD scaler data.

                            - **AntiAlias** *(string) --* The anti-alias filter is automatically
                            applied to all outputs. The service no longer accepts the value DISABLED
                            for AntiAlias. If you specify that in your job, the service will ignore
                            the setting.

                            - **CodecSettings** *(dict) --* Video codec settings, (CodecSettings)
                            under (VideoDescription), contains the group of settings related to
                            video encoding. The settings in this group vary depending on the value
                            that you choose for Video codec (Codec). For each codec enum that you
                            choose, define the corresponding settings object. The following lists
                            the codec enum, settings object pairs. * H_264, H264Settings * H_265,
                            H265Settings * MPEG2, Mpeg2Settings * PRORES, ProresSettings *
                            FRAME_CAPTURE, FrameCaptureSettings

                              - **Codec** *(string) --* Specifies the video codec. This must be
                              equal to one of the enum values defined by the object VideoCodec.

                              - **FrameCaptureSettings** *(dict) --* Required when you set (Codec)
                              under (VideoDescription)>(CodecSettings) to the value FRAME_CAPTURE.

                                - **FramerateDenominator** *(integer) --* Frame capture will encode
                                the first frame of the output stream, then one frame every
                                framerateDenominator/framerateNumerator seconds. For example,
                                settings of framerateNumerator =
                                     1 and framerateDenominator = 3 (a
                                rate of 1/3 frame per second) will capture the first frame, then 1
                                frame every 3s. Files will be named as filename.n.jpg where n is the
                                0-based sequence number of each Capture.

                                - **FramerateNumerator** *(integer) --* Frame capture will encode
                                the first frame of the output stream, then one frame every
                                framerateDenominator/framerateNumerator seconds. For example,
                                settings of framerateNumerator =
                                     1 and framerateDenominator = 3 (a
                                rate of 1/3 frame per second) will capture the first frame, then 1
                                frame every 3s. Files will be named as filename.NNNNNNN.jpg where N
                                is the 0-based frame sequence number zero padded to 7 decimal
                                places.

                                - **MaxCaptures** *(integer) --* Maximum number of captures (encoded
                                jpg output files).

                                - **Quality** *(integer) --* JPEG Quality - a higher value equals
                                higher quality.

                              - **H264Settings** *(dict) --* Required when you set (Codec) under
                              (VideoDescription)>(CodecSettings) to the value H_264.

                                - **AdaptiveQuantization** *(string) --* Adaptive quantization.
                                Allows intra-frame quantizers to vary to improve visual quality.

                                - **Bitrate** *(integer) --* Specify the average bitrate in bits per
                                second. Required for VBR and CBR. For MS Smooth outputs, bitrates
                                must be unique when rounded down to the nearest multiple of 1000.

                                - **CodecLevel** *(string) --* Specify an H.264 level that is
                                consistent with your output video settings. If you aren't sure what
                                level to specify, choose Auto (AUTO).

                                - **CodecProfile** *(string) --* H.264 Profile. High 4:2:2 and
                                10-bit profiles are only available with the AVC-I License.

                                - **DynamicSubGop** *(string) --* Choose Adaptive to improve
                                subjective video quality for high-motion content. This will cause
                                the service to use fewer B-frames (which infer information based on
                                other frames) for high-motion portions of the video and more
                                B-frames for low-motion portions. The maximum number of B-frames is
                                limited by the value you provide for the setting B frames between
                                reference frames (numberBFramesBetweenReferenceFrames).

                                - **EntropyEncoding** *(string) --* Entropy encoding mode. Use CABAC
                                (must be in Main or High profile) or CAVLC.

                                - **FieldEncoding** *(string) --* Choosing FORCE_FIELD disables PAFF
                                encoding for interlaced outputs.

                                - **FlickerAdaptiveQuantization** *(string) --* Adjust quantization
                                within each frame to reduce flicker or 'pop' on I-frames.

                                - **FramerateControl** *(string) --* If you are using the console,
                                use the Framerate setting to specify the frame rate for this output.
                                If you want to keep the same frame rate as the input video, choose
                                Follow source. If you want to do frame rate conversion, choose a
                                frame rate from the dropdown list or choose Custom. The framerates
                                shown in the dropdown list are decimal approximations of fractions.
                                If you choose Custom, specify your frame rate as a fraction. If you
                                are creating your transcoding job specification as a JSON file
                                without the console, use FramerateControl to specify which value the
                                service uses for the frame rate for this output. Choose
                                INITIALIZE_FROM_SOURCE if you want the service to use the frame rate
                                from the input. Choose SPECIFIED if you want the service to use the
                                frame rate you specify in the settings FramerateNumerator and
                                FramerateDenominator.

                                - **FramerateConversionAlgorithm** *(string) --* When set to
                                INTERPOLATE, produces smoother motion during frame rate conversion.

                                - **FramerateDenominator** *(integer) --* When you use the API for
                                transcode jobs that use frame rate conversion, specify the frame
                                rate as a fraction. For example, 24000 / 1001 = 23.976 fps. Use
                                FramerateDenominator to specify the denominator of this fraction. In
                                this example, use 1001 for the value of FramerateDenominator. When
                                you use the console for transcode jobs that use frame rate
                                conversion, provide the value as a decimal number for Framerate. In
                                this example, specify 23.976.

                                - **FramerateNumerator** *(integer) --* Frame rate numerator - frame
                                rate is a fraction, e.g. 24000 / 1001 =
                                     23.976 fps.

                                - **GopBReference** *(string) --* If enable, use reference B frames
                                for GOP structures that have B frames > 1.

                                - **GopClosedCadence** *(integer) --* Frequency of closed GOPs. In
                                streaming applications, it is recommended that this be set to 1 so a
                                decoder joining mid-stream will receive an IDR frame as quickly as
                                possible. Setting this value to 0 will break output segmenting.

                                - **GopSize** *(float) --* GOP Length (keyframe interval) in frames
                                or seconds. Must be greater than zero.

                                - **GopSizeUnits** *(string) --* Indicates if the GOP Size in H264
                                is specified in frames or seconds. If seconds the system will
                                convert the GOP Size into a frame count at run time.

                                - **HrdBufferInitialFillPercentage** *(integer) --* Percentage of
                                the buffer that should initially be filled (HRD buffer model).

                                - **HrdBufferSize** *(integer) --* Size of buffer (HRD buffer model)
                                in bits. For example, enter five megabits as 5000000.

                                - **InterlaceMode** *(string) --* Use Interlace mode (InterlaceMode)
                                to choose the scan line type for the output. * Top Field First
                                (TOP_FIELD) and Bottom Field First (BOTTOM_FIELD) produce interlaced
                                output with the entire output having the same field polarity (top or
                                bottom first). * Follow, Default Top (FOLLOW_TOP_FIELD) and Follow,
                                Default Bottom (FOLLOW_BOTTOM_FIELD) use the same field polarity as
                                the source. Therefore, behavior depends on the input scan type, as
                                follows. - If the source is interlaced, the output will be
                                interlaced with the same polarity as the source (it will follow the
                                source). The output could therefore be a mix of "top field first"
                                and "bottom field first". - If the source is progressive, the output
                                will be interlaced with "top field first" or "bottom field first"
                                polarity, depending on which of the Follow options you chose.

                                - **MaxBitrate** *(integer) --* Maximum bitrate in bits/second. For
                                example, enter five megabits per second as 5000000. Required when
                                Rate control mode is QVBR.

                                - **MinIInterval** *(integer) --* Enforces separation between
                                repeated (cadence) I-frames and I-frames inserted by Scene Change
                                Detection. If a scene change I-frame is within I-interval frames of
                                a cadence I-frame, the GOP is shrunk and/or stretched to the scene
                                change I-frame. GOP stretch requires enabling lookahead as well as
                                setting I-interval. The normal cadence resumes for the next GOP.
                                This setting is only used when Scene Change Detect is enabled. Note:
                                Maximum GOP stretch =
                                     GOP size + Min-I-interval - 1

                                - **NumberBFramesBetweenReferenceFrames** *(integer) --* Number of
                                B-frames between reference frames.

                                - **NumberReferenceFrames** *(integer) --* Number of reference
                                frames to use. The encoder may use more than requested if using
                                B-frames and/or interlaced encoding.

                                - **ParControl** *(string) --* Using the API, enable ParFollowSource
                                if you want the service to use the pixel aspect ratio from the
                                input. Using the console, do this by choosing Follow source for
                                Pixel aspect ratio.

                                - **ParDenominator** *(integer) --* Pixel Aspect Ratio denominator.

                                - **ParNumerator** *(integer) --* Pixel Aspect Ratio numerator.

                                - **QualityTuningLevel** *(string) --* Use Quality tuning level
                                (H264QualityTuningLevel) to specifiy whether to use fast
                                single-pass, high-quality singlepass, or high-quality multipass
                                video encoding.

                                - **QvbrSettings** *(dict) --* Settings for quality-defined variable
                                bitrate encoding with the H.264 codec. Required when you set Rate
                                control mode to QVBR. Not valid when you set Rate control mode to a
                                value other than QVBR, or when you don't define Rate control mode.

                                  - **MaxAverageBitrate** *(integer) --* Use this setting only when
                                  Rate control mode is QVBR and Quality tuning level is Multi-pass
                                  HQ. For Max average bitrate values suited to the complexity of
                                  your input video, the service limits the average bitrate of the
                                  video part of this output to the value that you choose. That is,
                                  the total size of the video element is less than or equal to the
                                  value you set multiplied by the number of seconds of encoded
                                  output.

                                  - **QvbrQualityLevel** *(integer) --* Required when you use QVBR
                                  rate control mode. That is, when you specify qvbrSettings within
                                  h264Settings. Specify the target quality level for this output,
                                  from 1 to 10. Use higher numbers for greater quality. Level 10
                                  results in nearly lossless compression. The quality level for most
                                  broadcast-quality transcodes is between 6 and 9.

                                - **RateControlMode** *(string) --* Use this setting to specify
                                whether this output has a variable bitrate (VBR), constant bitrate
                                (CBR) or quality-defined variable bitrate (QVBR).

                                - **RepeatPps** *(string) --* Places a PPS header on each encoded
                                picture, even if repeated.

                                - **SceneChangeDetect** *(string) --* Enable this setting to insert
                                I-frames at scene changes that the service automatically detects.
                                This improves video quality and is enabled by default. If this
                                output uses QVBR, choose Transition detection (TRANSITION_DETECTION)
                                for further video quality improvement. For more information about
                                QVBR, see
                                https://docs.aws.amazon.com/console/mediaconvert/cbr-vbr-qvbr.

                                - **Slices** *(integer) --* Number of slices per picture. Must be
                                less than or equal to the number of macroblock rows for progressive
                                pictures, and less than or equal to half the number of macroblock
                                rows for interlaced pictures.

                                - **SlowPal** *(string) --* Enables Slow PAL rate conversion.
                                23.976fps and 24fps input is relabeled as 25fps, and audio is sped
                                up correspondingly.

                                - **Softness** *(integer) --* Softness. Selects quantizer matrix,
                                larger values reduce high-frequency content in the encoded image.

                                - **SpatialAdaptiveQuantization** *(string) --* Adjust quantization
                                within each frame based on spatial variation of content complexity.

                                - **Syntax** *(string) --* Produces a bitstream compliant with SMPTE
                                RP-2027.

                                - **Telecine** *(string) --* This field applies only if the Streams
                                > Advanced > Framerate (framerate) field is set to 29.970. This
                                field works with the Streams > Advanced > Preprocessors >
                                Deinterlacer field (deinterlace_mode) and the Streams > Advanced >
                                Interlaced Mode field (interlace_mode) to identify the scan type for
                                the output: Progressive, Interlaced, Hard Telecine or Soft Telecine.
                                - Hard: produces 29.97i output from 23.976 input. - Soft: produces
                                23.976; the player converts this output to 29.97i.

                                - **TemporalAdaptiveQuantization** *(string) --* Adjust quantization
                                within each frame based on temporal variation of content complexity.

                                - **UnregisteredSeiTimecode** *(string) --* Inserts timecode for
                                each frame as 4 bytes of an unregistered SEI message.

                              - **H265Settings** *(dict) --* Settings for H265 codec

                                - **AdaptiveQuantization** *(string) --* Adaptive quantization.
                                Allows intra-frame quantizers to vary to improve visual quality.

                                - **AlternateTransferFunctionSei** *(string) --* Enables Alternate
                                Transfer Function SEI message for outputs using Hybrid Log Gamma
                                (HLG) Electro-Optical Transfer Function (EOTF).

                                - **Bitrate** *(integer) --* Specify the average bitrate in bits per
                                second. Required for VBR and CBR. For MS Smooth outputs, bitrates
                                must be unique when rounded down to the nearest multiple of 1000.

                                - **CodecLevel** *(string) --* H.265 Level.

                                - **CodecProfile** *(string) --* Represents the Profile and Tier,
                                per the HEVC (H.265) specification. Selections are grouped as
                                [Profile] / [Tier], so "Main/High" represents Main Profile with High
                                Tier. 4:2:2 profiles are only available with the HEVC 4:2:2 License.

                                - **DynamicSubGop** *(string) --* Choose Adaptive to improve
                                subjective video quality for high-motion content. This will cause
                                the service to use fewer B-frames (which infer information based on
                                other frames) for high-motion portions of the video and more
                                B-frames for low-motion portions. The maximum number of B-frames is
                                limited by the value you provide for the setting B frames between
                                reference frames (numberBFramesBetweenReferenceFrames).

                                - **FlickerAdaptiveQuantization** *(string) --* Adjust quantization
                                within each frame to reduce flicker or 'pop' on I-frames.

                                - **FramerateControl** *(string) --* If you are using the console,
                                use the Framerate setting to specify the frame rate for this output.
                                If you want to keep the same frame rate as the input video, choose
                                Follow source. If you want to do frame rate conversion, choose a
                                frame rate from the dropdown list or choose Custom. The framerates
                                shown in the dropdown list are decimal approximations of fractions.
                                If you choose Custom, specify your frame rate as a fraction. If you
                                are creating your transcoding job sepecification as a JSON file
                                without the console, use FramerateControl to specify which value the
                                service uses for the frame rate for this output. Choose
                                INITIALIZE_FROM_SOURCE if you want the service to use the frame rate
                                from the input. Choose SPECIFIED if you want the service to use the
                                frame rate you specify in the settings FramerateNumerator and
                                FramerateDenominator.

                                - **FramerateConversionAlgorithm** *(string) --* When set to
                                INTERPOLATE, produces smoother motion during frame rate conversion.

                                - **FramerateDenominator** *(integer) --* Frame rate denominator.

                                - **FramerateNumerator** *(integer) --* Frame rate numerator - frame
                                rate is a fraction, e.g. 24000 / 1001 =
                                     23.976 fps.

                                - **GopBReference** *(string) --* If enable, use reference B frames
                                for GOP structures that have B frames > 1.

                                - **GopClosedCadence** *(integer) --* Frequency of closed GOPs. In
                                streaming applications, it is recommended that this be set to 1 so a
                                decoder joining mid-stream will receive an IDR frame as quickly as
                                possible. Setting this value to 0 will break output segmenting.

                                - **GopSize** *(float) --* GOP Length (keyframe interval) in frames
                                or seconds. Must be greater than zero.

                                - **GopSizeUnits** *(string) --* Indicates if the GOP Size in H265
                                is specified in frames or seconds. If seconds the system will
                                convert the GOP Size into a frame count at run time.

                                - **HrdBufferInitialFillPercentage** *(integer) --* Percentage of
                                the buffer that should initially be filled (HRD buffer model).

                                - **HrdBufferSize** *(integer) --* Size of buffer (HRD buffer model)
                                in bits. For example, enter five megabits as 5000000.

                                - **InterlaceMode** *(string) --* Choose the scan line type for the
                                output. Choose Progressive (PROGRESSIVE) to create a progressive
                                output, regardless of the scan type of your input. Choose Top Field
                                First (TOP_FIELD) or Bottom Field First (BOTTOM_FIELD) to create an
                                output that's interlaced with the same field polarity throughout.
                                Choose Follow, Default Top (FOLLOW_TOP_FIELD) or Follow, Default
                                Bottom (FOLLOW_BOTTOM_FIELD) to create an interlaced output with the
                                same field polarity as the source. If the source is interlaced, the
                                output will be interlaced with the same polarity as the source (it
                                will follow the source). The output could therefore be a mix of "top
                                field first" and "bottom field first". If the source is progressive,
                                your output will be interlaced with "top field first" or "bottom
                                field first" polarity, depending on which of the Follow options you
                                chose. If you don't choose a value, the service will default to
                                Progressive (PROGRESSIVE).

                                - **MaxBitrate** *(integer) --* Maximum bitrate in bits/second. For
                                example, enter five megabits per second as 5000000. Required when
                                Rate control mode is QVBR.

                                - **MinIInterval** *(integer) --* Enforces separation between
                                repeated (cadence) I-frames and I-frames inserted by Scene Change
                                Detection. If a scene change I-frame is within I-interval frames of
                                a cadence I-frame, the GOP is shrunk and/or stretched to the scene
                                change I-frame. GOP stretch requires enabling lookahead as well as
                                setting I-interval. The normal cadence resumes for the next GOP.
                                This setting is only used when Scene Change Detect is enabled. Note:
                                Maximum GOP stretch =
                                     GOP size + Min-I-interval - 1

                                - **NumberBFramesBetweenReferenceFrames** *(integer) --* Number of
                                B-frames between reference frames.

                                - **NumberReferenceFrames** *(integer) --* Number of reference
                                frames to use. The encoder may use more than requested if using
                                B-frames and/or interlaced encoding.

                                - **ParControl** *(string) --* Using the API, enable ParFollowSource
                                if you want the service to use the pixel aspect ratio from the
                                input. Using the console, do this by choosing Follow source for
                                Pixel aspect ratio.

                                - **ParDenominator** *(integer) --* Pixel Aspect Ratio denominator.

                                - **ParNumerator** *(integer) --* Pixel Aspect Ratio numerator.

                                - **QualityTuningLevel** *(string) --* Use Quality tuning level
                                (H265QualityTuningLevel) to specifiy whether to use fast
                                single-pass, high-quality singlepass, or high-quality multipass
                                video encoding.

                                - **QvbrSettings** *(dict) --* Settings for quality-defined variable
                                bitrate encoding with the H.265 codec. Required when you set Rate
                                control mode to QVBR. Not valid when you set Rate control mode to a
                                value other than QVBR, or when you don't define Rate control mode.

                                  - **MaxAverageBitrate** *(integer) --* Use this setting only when
                                  Rate control mode is QVBR and Quality tuning level is Multi-pass
                                  HQ. For Max average bitrate values suited to the complexity of
                                  your input video, the service limits the average bitrate of the
                                  video part of this output to the value that you choose. That is,
                                  the total size of the video element is less than or equal to the
                                  value you set multiplied by the number of seconds of encoded
                                  output.

                                  - **QvbrQualityLevel** *(integer) --* Required when you use QVBR
                                  rate control mode. That is, when you specify qvbrSettings within
                                  h265Settings. Specify the target quality level for this output,
                                  from 1 to 10. Use higher numbers for greater quality. Level 10
                                  results in nearly lossless compression. The quality level for most
                                  broadcast-quality transcodes is between 6 and 9.

                                - **RateControlMode** *(string) --* Use this setting to specify
                                whether this output has a variable bitrate (VBR), constant bitrate
                                (CBR) or quality-defined variable bitrate (QVBR).

                                - **SampleAdaptiveOffsetFilterMode** *(string) --* Specify Sample
                                Adaptive Offset (SAO) filter strength. Adaptive mode dynamically
                                selects best strength based on content

                                - **SceneChangeDetect** *(string) --* Enable this setting to insert
                                I-frames at scene changes that the service automatically detects.
                                This improves video quality and is enabled by default. If this
                                output uses QVBR, choose Transition detection (TRANSITION_DETECTION)
                                for further video quality improvement. For more information about
                                QVBR, see
                                https://docs.aws.amazon.com/console/mediaconvert/cbr-vbr-qvbr.

                                - **Slices** *(integer) --* Number of slices per picture. Must be
                                less than or equal to the number of macroblock rows for progressive
                                pictures, and less than or equal to half the number of macroblock
                                rows for interlaced pictures.

                                - **SlowPal** *(string) --* Enables Slow PAL rate conversion.
                                23.976fps and 24fps input is relabeled as 25fps, and audio is sped
                                up correspondingly.

                                - **SpatialAdaptiveQuantization** *(string) --* Adjust quantization
                                within each frame based on spatial variation of content complexity.

                                - **Telecine** *(string) --* This field applies only if the Streams
                                > Advanced > Framerate (framerate) field is set to 29.970. This
                                field works with the Streams > Advanced > Preprocessors >
                                Deinterlacer field (deinterlace_mode) and the Streams > Advanced >
                                Interlaced Mode field (interlace_mode) to identify the scan type for
                                the output: Progressive, Interlaced, Hard Telecine or Soft Telecine.
                                - Hard: produces 29.97i output from 23.976 input. - Soft: produces
                                23.976; the player converts this output to 29.97i.

                                - **TemporalAdaptiveQuantization** *(string) --* Adjust quantization
                                within each frame based on temporal variation of content complexity.

                                - **TemporalIds** *(string) --* Enables temporal layer identifiers
                                in the encoded bitstream. Up to 3 layers are supported depending on
                                GOP structure: I- and P-frames form one layer, reference B-frames
                                can form a second layer and non-reference b-frames can form a third
                                layer. Decoders can optionally decode only the lower temporal layers
                                to generate a lower frame rate output. For example, given a
                                bitstream with temporal IDs and with b-frames = 1 (i.e. IbPbPb
                                display order), a decoder could decode all the frames for full frame
                                rate output or only the I and P frames (lowest temporal layer) for a
                                half frame rate output.

                                - **Tiles** *(string) --* Enable use of tiles, allowing horizontal
                                as well as vertical subdivision of the encoded pictures.

                                - **UnregisteredSeiTimecode** *(string) --* Inserts timecode for
                                each frame as 4 bytes of an unregistered SEI message.

                                - **WriteMp4PackagingType** *(string) --* If the location of
                                parameter set NAL units doesn't matter in your workflow, ignore this
                                setting. Use this setting only with CMAF or DASH outputs, or with
                                standalone file outputs in an MPEG-4 container (MP4 outputs). Choose
                                HVC1 to mark your output as HVC1. This makes your output compliant
                                with the following specification: ISO IECJTC1 SC29 N13798 Text
                                ISO/IEC FDIS 14496-15 3rd Edition. For these outputs, the service
                                stores parameter set NAL units in the sample headers but not in the
                                samples directly. For MP4 outputs, when you choose HVC1, your output
                                video might not work properly with some downstream systems and video
                                players. The service defaults to marking your output as HEV1. For
                                these outputs, the service writes parameter set NAL units directly
                                into the samples.

                              - **Mpeg2Settings** *(dict) --* Required when you set (Codec) under
                              (VideoDescription)>(CodecSettings) to the value MPEG2.

                                - **AdaptiveQuantization** *(string) --* Adaptive quantization.
                                Allows intra-frame quantizers to vary to improve visual quality.

                                - **Bitrate** *(integer) --* Specify the average bitrate in bits per
                                second. Required for VBR and CBR. For MS Smooth outputs, bitrates
                                must be unique when rounded down to the nearest multiple of 1000.

                                - **CodecLevel** *(string) --* Use Level (Mpeg2CodecLevel) to set
                                the MPEG-2 level for the video output.

                                - **CodecProfile** *(string) --* Use Profile (Mpeg2CodecProfile) to
                                set the MPEG-2 profile for the video output.

                                - **DynamicSubGop** *(string) --* Choose Adaptive to improve
                                subjective video quality for high-motion content. This will cause
                                the service to use fewer B-frames (which infer information based on
                                other frames) for high-motion portions of the video and more
                                B-frames for low-motion portions. The maximum number of B-frames is
                                limited by the value you provide for the setting B frames between
                                reference frames (numberBFramesBetweenReferenceFrames).

                                - **FramerateControl** *(string) --* If you are using the console,
                                use the Framerate setting to specify the frame rate for this output.
                                If you want to keep the same frame rate as the input video, choose
                                Follow source. If you want to do frame rate conversion, choose a
                                frame rate from the dropdown list or choose Custom. The framerates
                                shown in the dropdown list are decimal approximations of fractions.
                                If you choose Custom, specify your frame rate as a fraction. If you
                                are creating your transcoding job sepecification as a JSON file
                                without the console, use FramerateControl to specify which value the
                                service uses for the frame rate for this output. Choose
                                INITIALIZE_FROM_SOURCE if you want the service to use the frame rate
                                from the input. Choose SPECIFIED if you want the service to use the
                                frame rate you specify in the settings FramerateNumerator and
                                FramerateDenominator.

                                - **FramerateConversionAlgorithm** *(string) --* When set to
                                INTERPOLATE, produces smoother motion during frame rate conversion.

                                - **FramerateDenominator** *(integer) --* Frame rate denominator.

                                - **FramerateNumerator** *(integer) --* Frame rate numerator - frame
                                rate is a fraction, e.g. 24000 / 1001 =
                                     23.976 fps.

                                - **GopClosedCadence** *(integer) --* Frequency of closed GOPs. In
                                streaming applications, it is recommended that this be set to 1 so a
                                decoder joining mid-stream will receive an IDR frame as quickly as
                                possible. Setting this value to 0 will break output segmenting.

                                - **GopSize** *(float) --* GOP Length (keyframe interval) in frames
                                or seconds. Must be greater than zero.

                                - **GopSizeUnits** *(string) --* Indicates if the GOP Size in MPEG2
                                is specified in frames or seconds. If seconds the system will
                                convert the GOP Size into a frame count at run time.

                                - **HrdBufferInitialFillPercentage** *(integer) --* Percentage of
                                the buffer that should initially be filled (HRD buffer model).

                                - **HrdBufferSize** *(integer) --* Size of buffer (HRD buffer model)
                                in bits. For example, enter five megabits as 5000000.

                                - **InterlaceMode** *(string) --* Use Interlace mode (InterlaceMode)
                                to choose the scan line type for the output. * Top Field First
                                (TOP_FIELD) and Bottom Field First (BOTTOM_FIELD) produce interlaced
                                output with the entire output having the same field polarity (top or
                                bottom first). * Follow, Default Top (FOLLOW_TOP_FIELD) and Follow,
                                Default Bottom (FOLLOW_BOTTOM_FIELD) use the same field polarity as
                                the source. Therefore, behavior depends on the input scan type. - If
                                the source is interlaced, the output will be interlaced with the
                                same polarity as the source (it will follow the source). The output
                                could therefore be a mix of "top field first" and "bottom field
                                first". - If the source is progressive, the output will be
                                interlaced with "top field first" or "bottom field first" polarity,
                                depending on which of the Follow options you chose.

                                - **IntraDcPrecision** *(string) --* Use Intra DC precision
                                (Mpeg2IntraDcPrecision) to set quantization precision for
                                intra-block DC coefficients. If you choose the value auto, the
                                service will automatically select the precision based on the
                                per-frame compression ratio.

                                - **MaxBitrate** *(integer) --* Maximum bitrate in bits/second. For
                                example, enter five megabits per second as 5000000.

                                - **MinIInterval** *(integer) --* Enforces separation between
                                repeated (cadence) I-frames and I-frames inserted by Scene Change
                                Detection. If a scene change I-frame is within I-interval frames of
                                a cadence I-frame, the GOP is shrunk and/or stretched to the scene
                                change I-frame. GOP stretch requires enabling lookahead as well as
                                setting I-interval. The normal cadence resumes for the next GOP.
                                This setting is only used when Scene Change Detect is enabled. Note:
                                Maximum GOP stretch =
                                     GOP size + Min-I-interval - 1

                                - **NumberBFramesBetweenReferenceFrames** *(integer) --* Number of
                                B-frames between reference frames.

                                - **ParControl** *(string) --* Using the API, enable ParFollowSource
                                if you want the service to use the pixel aspect ratio from the
                                input. Using the console, do this by choosing Follow source for
                                Pixel aspect ratio.

                                - **ParDenominator** *(integer) --* Pixel Aspect Ratio denominator.

                                - **ParNumerator** *(integer) --* Pixel Aspect Ratio numerator.

                                - **QualityTuningLevel** *(string) --* Use Quality tuning level
                                (Mpeg2QualityTuningLevel) to specifiy whether to use single-pass or
                                multipass video encoding.

                                - **RateControlMode** *(string) --* Use Rate control mode
                                (Mpeg2RateControlMode) to specifiy whether the bitrate is variable
                                (vbr) or constant (cbr).

                                - **SceneChangeDetect** *(string) --* Enable this setting to insert
                                I-frames at scene changes that the service automatically detects.
                                This improves video quality and is enabled by default.

                                - **SlowPal** *(string) --* Enables Slow PAL rate conversion.
                                23.976fps and 24fps input is relabeled as 25fps, and audio is sped
                                up correspondingly.

                                - **Softness** *(integer) --* Softness. Selects quantizer matrix,
                                larger values reduce high-frequency content in the encoded image.

                                - **SpatialAdaptiveQuantization** *(string) --* Adjust quantization
                                within each frame based on spatial variation of content complexity.

                                - **Syntax** *(string) --* Produces a Type D-10 compatible bitstream
                                (SMPTE 356M-2001).

                                - **Telecine** *(string) --* Only use Telecine (Mpeg2Telecine) when
                                you set Framerate (Framerate) to 29.970. Set Telecine
                                (Mpeg2Telecine) to Hard (hard) to produce a 29.97i output from a
                                23.976 input. Set it to Soft (soft) to produce 23.976 output and
                                leave converstion to the player.

                                - **TemporalAdaptiveQuantization** *(string) --* Adjust quantization
                                within each frame based on temporal variation of content complexity.

                              - **ProresSettings** *(dict) --* Required when you set (Codec) under
                              (VideoDescription)>(CodecSettings) to the value PRORES.

                                - **CodecProfile** *(string) --* Use Profile (ProResCodecProfile) to
                                specifiy the type of Apple ProRes codec to use for this output.

                                - **FramerateControl** *(string) --* If you are using the console,
                                use the Framerate setting to specify the frame rate for this output.
                                If you want to keep the same frame rate as the input video, choose
                                Follow source. If you want to do frame rate conversion, choose a
                                frame rate from the dropdown list or choose Custom. The framerates
                                shown in the dropdown list are decimal approximations of fractions.
                                If you choose Custom, specify your frame rate as a fraction. If you
                                are creating your transcoding job sepecification as a JSON file
                                without the console, use FramerateControl to specify which value the
                                service uses for the frame rate for this output. Choose
                                INITIALIZE_FROM_SOURCE if you want the service to use the frame rate
                                from the input. Choose SPECIFIED if you want the service to use the
                                frame rate you specify in the settings FramerateNumerator and
                                FramerateDenominator.

                                - **FramerateConversionAlgorithm** *(string) --* When set to
                                INTERPOLATE, produces smoother motion during frame rate conversion.

                                - **FramerateDenominator** *(integer) --* Frame rate denominator.

                                - **FramerateNumerator** *(integer) --* When you use the API for
                                transcode jobs that use frame rate conversion, specify the frame
                                rate as a fraction. For example, 24000 / 1001 = 23.976 fps. Use
                                FramerateNumerator to specify the numerator of this fraction. In
                                this example, use 24000 for the value of FramerateNumerator.

                                - **InterlaceMode** *(string) --* Use Interlace mode (InterlaceMode)
                                to choose the scan line type for the output. * Top Field First
                                (TOP_FIELD) and Bottom Field First (BOTTOM_FIELD) produce interlaced
                                output with the entire output having the same field polarity (top or
                                bottom first). * Follow, Default Top (FOLLOW_TOP_FIELD) and Follow,
                                Default Bottom (FOLLOW_BOTTOM_FIELD) use the same field polarity as
                                the source. Therefore, behavior depends on the input scan type. - If
                                the source is interlaced, the output will be interlaced with the
                                same polarity as the source (it will follow the source). The output
                                could therefore be a mix of "top field first" and "bottom field
                                first". - If the source is progressive, the output will be
                                interlaced with "top field first" or "bottom field first" polarity,
                                depending on which of the Follow options you chose.

                                - **ParControl** *(string) --* Use (ProresParControl) to specify how
                                the service determines the pixel aspect ratio. Set to Follow source
                                (INITIALIZE_FROM_SOURCE) to use the pixel aspect ratio from the
                                input. To specify a different pixel aspect ratio: Using the console,
                                choose it from the dropdown menu. Using the API, set
                                ProresParControl to (SPECIFIED) and provide for (ParNumerator) and
                                (ParDenominator).

                                - **ParDenominator** *(integer) --* Pixel Aspect Ratio denominator.

                                - **ParNumerator** *(integer) --* Pixel Aspect Ratio numerator.

                                - **SlowPal** *(string) --* Enables Slow PAL rate conversion.
                                23.976fps and 24fps input is relabeled as 25fps, and audio is sped
                                up correspondingly.

                                - **Telecine** *(string) --* Only use Telecine (ProresTelecine) when
                                you set Framerate (Framerate) to 29.970. Set Telecine
                                (ProresTelecine) to Hard (hard) to produce a 29.97i output from a
                                23.976 input. Set it to Soft (soft) to produce 23.976 output and
                                leave converstion to the player.

                            - **ColorMetadata** *(string) --* Choose Insert (INSERT) for this
                            setting to include color metadata in this output. Choose Ignore (IGNORE)
                            to exclude color metadata from this output. If you don't specify a
                            value, the service sets this to Insert by default.

                            - **Crop** *(dict) --* Use Cropping selection (crop) to specify the
                            video area that the service will include in the output video frame.

                              - **Height** *(integer) --* Height of rectangle in pixels. Specify
                              only even numbers.

                              - **Width** *(integer) --* Width of rectangle in pixels. Specify only
                              even numbers.

                              - **X** *(integer) --* The distance, in pixels, between the rectangle
                              and the left edge of the video frame. Specify only even numbers.

                              - **Y** *(integer) --* The distance, in pixels, between the rectangle
                              and the top edge of the video frame. Specify only even numbers.

                            - **DropFrameTimecode** *(string) --* Applies only to 29.97 fps outputs.
                            When this feature is enabled, the service will use drop-frame timecode
                            on outputs. If it is not possible to use drop-frame timecode, the system
                            will fall back to non-drop-frame. This setting is enabled by default
                            when Timecode insertion (TimecodeInsertion) is enabled.

                            - **FixedAfd** *(integer) --* Applies only if you set AFD
                            Signaling(AfdSignaling) to Fixed (FIXED). Use Fixed (FixedAfd) to
                            specify a four-bit AFD value which the service will write on all frames
                            of this video output.

                            - **Height** *(integer) --* Use the Height (Height) setting to define
                            the video resolution height for this output. Specify in pixels. If you
                            don't provide a value here, the service will use the input height.

                            - **Position** *(dict) --* Use Selection placement (position) to define
                            the video area in your output frame. The area outside of the rectangle
                            that you specify here is black.

                              - **Height** *(integer) --* Height of rectangle in pixels. Specify
                              only even numbers.

                              - **Width** *(integer) --* Width of rectangle in pixels. Specify only
                              even numbers.

                              - **X** *(integer) --* The distance, in pixels, between the rectangle
                              and the left edge of the video frame. Specify only even numbers.

                              - **Y** *(integer) --* The distance, in pixels, between the rectangle
                              and the top edge of the video frame. Specify only even numbers.

                            - **RespondToAfd** *(string) --* Use Respond to AFD (RespondToAfd) to
                            specify how the service changes the video itself in response to AFD
                            values in the input. * Choose Respond to clip the input video frame
                            according to the AFD value, input display aspect ratio, and output
                            display aspect ratio. * Choose Passthrough to include the input AFD
                            values. Do not choose this when AfdSignaling is set to (NONE). A
                            preferred implementation of this workflow is to set RespondToAfd to
                            (NONE) and set AfdSignaling to (AUTO). * Choose None to remove all input
                            AFD values from this output.

                            - **ScalingBehavior** *(string) --* Specify how the service handles
                            outputs that have a different aspect ratio from the input aspect ratio.
                            Choose Stretch to output (STRETCH_TO_OUTPUT) to have the service stretch
                            your video image to fit. Keep the setting Default (DEFAULT) to have the
                            service letterbox your video instead. This setting overrides any value
                            that you specify for the setting Selection placement (position) in this
                            output.

                            - **Sharpness** *(integer) --* Use Sharpness (Sharpness) setting to
                            specify the strength of anti-aliasing. This setting changes the width of
                            the anti-alias filter kernel used for scaling. Sharpness only applies if
                            your output resolution is different from your input resolution. 0 is the
                            softest setting, 100 the sharpest, and 50 recommended for most content.

                            - **TimecodeInsertion** *(string) --* Applies only to H.264, H.265,
                            MPEG2, and ProRes outputs. Only enable Timecode insertion when the input
                            frame rate is identical to the output frame rate. To include timecodes
                            in this output, set Timecode insertion (VideoTimecodeInsertion) to
                            PIC_TIMING_SEI. To leave them out, set it to DISABLED. Default is
                            DISABLED. When the service inserts timecodes in an output, by default,
                            it uses any embedded timecodes from the input. If none are present, the
                            service will set the timecode for the first output frame to zero. To
                            change this default behavior, adjust the settings under Timecode
                            configuration (TimecodeConfig). In the console, these settings are
                            located under Job > Job settings > Timecode configuration. Note -
                            Timecode source under input settings (InputTimecodeSource) does not
                            affect the timecodes that are inserted in the output. Source under Job
                            settings > Timecode configuration (TimecodeSource) does.

                            - **VideoPreprocessors** *(dict) --* Find additional transcoding
                            features under Preprocessors (VideoPreprocessors). Enable the features
                            at each output individually. These features are disabled by default.

                              - **ColorCorrector** *(dict) --* Enable the Color corrector
                              (ColorCorrector) feature if necessary. Enable or disable this feature
                              for each output individually. This setting is disabled by default.

                                - **Brightness** *(integer) --* Brightness level.

                                - **ColorSpaceConversion** *(string) --* Specify the color space you
                                want for this output. The service supports conversion between HDR
                                formats, between SDR formats, and from SDR to HDR. The service
                                doesn't support conversion from HDR to SDR. SDR to HDR conversion
                                doesn't upgrade the dynamic range. The converted video has an HDR
                                format, but visually appears the same as an unconverted output.

                                - **Contrast** *(integer) --* Contrast level.

                                - **Hdr10Metadata** *(dict) --* Use these settings when you convert
                                to the HDR 10 color space. Specify the SMPTE ST 2086 Mastering
                                Display Color Volume static metadata that you want signaled in the
                                output. These values don't affect the pixel values that are encoded
                                in the video stream. They are intended to help the downstream video
                                player display content in a way that reflects the intentions of the
                                the content creator. When you set Color space conversion
                                (ColorSpaceConversion) to HDR 10 (FORCE_HDR10), these settings are
                                required. You must set values for Max frame average light level
                                (maxFrameAverageLightLevel) and Max content light level
                                (maxContentLightLevel); these settings don't have a default value.
                                The default values for the other HDR 10 metadata settings are
                                defined by the P3D65 color space. For more information about
                                MediaConvert HDR jobs, see
                                https://docs.aws.amazon.com/console/mediaconvert/hdr.

                                  - **BluePrimaryX** *(integer) --* HDR Master Display Information
                                  must be provided by a color grader, using color grading tools.
                                  Range is 0 to 50,000, each increment represents 0.00002 in CIE1931
                                  color coordinate. Note that this setting is not for color
                                  correction.

                                  - **BluePrimaryY** *(integer) --* HDR Master Display Information
                                  must be provided by a color grader, using color grading tools.
                                  Range is 0 to 50,000, each increment represents 0.00002 in CIE1931
                                  color coordinate. Note that this setting is not for color
                                  correction.

                                  - **GreenPrimaryX** *(integer) --* HDR Master Display Information
                                  must be provided by a color grader, using color grading tools.
                                  Range is 0 to 50,000, each increment represents 0.00002 in CIE1931
                                  color coordinate. Note that this setting is not for color
                                  correction.

                                  - **GreenPrimaryY** *(integer) --* HDR Master Display Information
                                  must be provided by a color grader, using color grading tools.
                                  Range is 0 to 50,000, each increment represents 0.00002 in CIE1931
                                  color coordinate. Note that this setting is not for color
                                  correction.

                                  - **MaxContentLightLevel** *(integer) --* Maximum light level
                                  among all samples in the coded video sequence, in units of
                                  candelas per square meter. This setting doesn't have a default
                                  value; you must specify a value that is suitable for the content.

                                  - **MaxFrameAverageLightLevel** *(integer) --* Maximum average
                                  light level of any frame in the coded video sequence, in units of
                                  candelas per square meter. This setting doesn't have a default
                                  value; you must specify a value that is suitable for the content.

                                  - **MaxLuminance** *(integer) --* Nominal maximum mastering
                                  display luminance in units of of 0.0001 candelas per square meter.

                                  - **MinLuminance** *(integer) --* Nominal minimum mastering
                                  display luminance in units of of 0.0001 candelas per square meter

                                  - **RedPrimaryX** *(integer) --* HDR Master Display Information
                                  must be provided by a color grader, using color grading tools.
                                  Range is 0 to 50,000, each increment represents 0.00002 in CIE1931
                                  color coordinate. Note that this setting is not for color
                                  correction.

                                  - **RedPrimaryY** *(integer) --* HDR Master Display Information
                                  must be provided by a color grader, using color grading tools.
                                  Range is 0 to 50,000, each increment represents 0.00002 in CIE1931
                                  color coordinate. Note that this setting is not for color
                                  correction.

                                  - **WhitePointX** *(integer) --* HDR Master Display Information
                                  must be provided by a color grader, using color grading tools.
                                  Range is 0 to 50,000, each increment represents 0.00002 in CIE1931
                                  color coordinate. Note that this setting is not for color
                                  correction.

                                  - **WhitePointY** *(integer) --* HDR Master Display Information
                                  must be provided by a color grader, using color grading tools.
                                  Range is 0 to 50,000, each increment represents 0.00002 in CIE1931
                                  color coordinate. Note that this setting is not for color
                                  correction.

                                - **Hue** *(integer) --* Hue in degrees.

                                - **Saturation** *(integer) --* Saturation level.

                              - **Deinterlacer** *(dict) --* Use Deinterlacer (Deinterlacer) to
                              produce smoother motion and a clearer picture.

                                - **Algorithm** *(string) --* Only applies when you set Deinterlacer
                                (DeinterlaceMode) to Deinterlace (DEINTERLACE) or Adaptive
                                (ADAPTIVE). Motion adaptive interpolate (INTERPOLATE) produces
                                sharper pictures, while blend (BLEND) produces smoother motion. Use
                                (INTERPOLATE_TICKER) OR (BLEND_TICKER) if your source file includes
                                a ticker, such as a scrolling headline at the bottom of the frame.

                                - **Control** *(string) --* - When set to NORMAL (default), the
                                deinterlacer does not convert frames that are tagged in metadata as
                                progressive. It will only convert those that are tagged as some
                                other type. - When set to FORCE_ALL_FRAMES, the deinterlacer
                                converts every frame to progressive - even those that are already
                                tagged as progressive. Turn Force mode on only if there is a good
                                chance that the metadata has tagged frames as progressive when they
                                are not progressive. Do not turn on otherwise; processing frames
                                that are already progressive into progressive will probably result
                                in lower quality video.

                                - **Mode** *(string) --* Use Deinterlacer (DeinterlaceMode) to
                                choose how the service will do deinterlacing. Default is
                                Deinterlace. - Deinterlace converts interlaced to progressive. -
                                Inverse telecine converts Hard Telecine 29.97i to progressive
                                23.976p. - Adaptive auto-detects and converts to progressive.

                              - **DolbyVision** *(dict) --* Enable Dolby Vision feature to produce
                              Dolby Vision compatible video output.

                                - **L6Metadata** *(dict) --* Use these settings when you set
                                DolbyVisionLevel6Mode to SPECIFY to override the MaxCLL and MaxFALL
                                values in your input with new values.

                                  - **MaxCll** *(integer) --* Maximum Content Light Level. Static
                                  HDR metadata that corresponds to the brightest pixel in the entire
                                  stream. Measured in nits.

                                  - **MaxFall** *(integer) --* Maximum Frame-Average Light Level.
                                  Static HDR metadata that corresponds to the highest frame-average
                                  brightness in the entire stream. Measured in nits.

                                - **L6Mode** *(string) --* Use Dolby Vision Mode to choose how the
                                service will handle Dolby Vision MaxCLL and MaxFALL properies.

                                - **Profile** *(string) --* In the current MediaConvert
                                implementation, the Dolby Vision profile is always 5 (PROFILE_5).
                                Therefore, all of your inputs must contain Dolby Vision frame
                                interleaved data.

                              - **ImageInserter** *(dict) --* Enable the Image inserter
                              (ImageInserter) feature to include a graphic overlay on your video.
                              Enable or disable this feature for each output individually. This
                              setting is disabled by default.

                                - **InsertableImages** *(list) --* Specify the images that you want
                                to overlay on your video. The images must be PNG or TGA files.

                                  - *(dict) --* Settings that specify how your still graphic overlay
                                  appears.

                                    - **Duration** *(integer) --* Specify the time, in milliseconds,
                                    for the image to remain on the output video. This duration
                                    includes fade-in time but not fade-out time.

                                    - **FadeIn** *(integer) --* Specify the length of time, in
                                    milliseconds, between the Start time that you specify for the
                                    image insertion and the time that the image appears at full
                                    opacity. Full opacity is the level that you specify for the
                                    opacity setting. If you don't specify a value for Fade-in, the
                                    image will appear abruptly at the overlay start time.

                                    - **FadeOut** *(integer) --* Specify the length of time, in
                                    milliseconds, between the end of the time that you have
                                    specified for the image overlay Duration and when the overlaid
                                    image has faded to total transparency. If you don't specify a
                                    value for Fade-out, the image will disappear abruptly at the end
                                    of the inserted image duration.

                                    - **Height** *(integer) --* Specify the height of the inserted
                                    image in pixels. If you specify a value that's larger than the
                                    video resolution height, the service will crop your overlaid
                                    image to fit. To use the native height of the image, keep this
                                    setting blank.

                                    - **ImageInserterInput** *(string) --* Specify the HTTP, HTTPS,
                                    or Amazon S3 location of the image that you want to overlay on
                                    the video. Use a PNG or TGA file.

                                    - **ImageX** *(integer) --* Specify the distance, in pixels,
                                    between the inserted image and the left edge of the video frame.
                                    Required for any image overlay that you specify.

                                    - **ImageY** *(integer) --* Specify the distance, in pixels,
                                    between the overlaid image and the top edge of the video frame.
                                    Required for any image overlay that you specify.

                                    - **Layer** *(integer) --* Specify how overlapping inserted
                                    images appear. Images with higher values for Layer appear on top
                                    of images with lower values for Layer.

                                    - **Opacity** *(integer) --* Use Opacity (Opacity) to specify
                                    how much of the underlying video shows through the inserted
                                    image. 0 is transparent and 100 is fully opaque. Default is 50.

                                    - **StartTime** *(string) --* Specify the timecode of the frame
                                    that you want the overlay to first appear on. This must be in
                                    timecode (HH:MM:SS:FF or HH:MM:SS;FF) format. Remember to take
                                    into account your timecode source settings.

                                    - **Width** *(integer) --* Specify the width of the inserted
                                    image in pixels. If you specify a value that's larger than the
                                    video resolution width, the service will crop your overlaid
                                    image to fit. To use the native width of the image, keep this
                                    setting blank.

                              - **NoiseReducer** *(dict) --* Enable the Noise reducer (NoiseReducer)
                              feature to remove noise from your video output if necessary. Enable or
                              disable this feature for each output individually. This setting is
                              disabled by default.

                                - **Filter** *(string) --* Use Noise reducer filter
                                (NoiseReducerFilter) to select one of the following spatial image
                                filtering functions. To use this setting, you must also enable Noise
                                reducer (NoiseReducer). * Bilateral preserves edges while reducing
                                noise. * Mean (softest), Gaussian, Lanczos, and Sharpen (sharpest)
                                do convolution filtering. * Conserve does min/max noise reduction. *
                                Spatial does frequency-domain filtering based on JND principles. *
                                Temporal optimizes video quality for complex motion.

                                - **FilterSettings** *(dict) --* Settings for a noise reducer filter

                                  - **Strength** *(integer) --* Relative strength of noise reducing
                                  filter. Higher values produce stronger filtering.

                                - **SpatialFilterSettings** *(dict) --* Noise reducer filter
                                settings for spatial filter.

                                  - **PostFilterSharpenStrength** *(integer) --* Specify strength of
                                  post noise reduction sharpening filter, with 0 disabling the
                                  filter and 3 enabling it at maximum strength.

                                  - **Speed** *(integer) --* The speed of the filter, from -2 (lower
                                  speed) to 3 (higher speed), with 0 being the nominal value.

                                  - **Strength** *(integer) --* Relative strength of noise reducing
                                  filter. Higher values produce stronger filtering.

                                - **TemporalFilterSettings** *(dict) --* Noise reducer filter
                                settings for temporal filter.

                                  - **AggressiveMode** *(integer) --* Use Aggressive mode for
                                  content that has complex motion. Higher values produce stronger
                                  temporal filtering. This filters highly complex scenes more
                                  aggressively and creates better VQ for low bitrate outputs.

                                  - **Speed** *(integer) --* The speed of the filter (higher number
                                  is faster). Low setting reduces bit rate at the cost of transcode
                                  time, high setting improves transcode time at the cost of bit
                                  rate.

                                  - **Strength** *(integer) --* Specify the strength of the noise
                                  reducing filter on this output. Higher values produce stronger
                                  filtering. We recommend the following value ranges, depending on
                                  the result that you want: * 0-2 for complexity reduction with
                                  minimal sharpness loss * 2-8 for complexity reduction with image
                                  preservation * 8-16 for a high level of complexity reduction

                              - **TimecodeBurnin** *(dict) --* Timecode burn-in
                              (TimecodeBurnIn)--Burns the output timecode and specified prefix into
                              the output.

                                - **FontSize** *(integer) --* Use Font Size (FontSize) to set the
                                font size of any burned-in timecode. Valid values are 10, 16, 32,
                                48.

                                - **Position** *(string) --* Use Position (Position) under under
                                Timecode burn-in (TimecodeBurnIn) to specify the location the
                                burned-in timecode on output video.

                                - **Prefix** *(string) --* Use Prefix (Prefix) to place ASCII
                                characters before any burned-in timecode. For example, a prefix of
                                "EZ-" will result in the timecode "EZ-00:00:00:00". Provide either
                                the characters themselves or the ASCII code equivalents. The
                                supported range of characters is 0x20 through 0x7e. This includes
                                letters, numbers, and all special characters represented on a
                                standard English keyboard.

                            - **Width** *(integer) --* Use Width (Width) to define the video
                            resolution width, in pixels, for this output. If you don't provide a
                            value here, the service will use the input width.

                  - **TimecodeConfig** *(dict) --* Contains settings used to acquire and adjust
                  timecode information from inputs.

                    - **Anchor** *(string) --* If you use an editing platform that relies on an
                    anchor timecode, use Anchor Timecode (Anchor) to specify a timecode that will
                    match the input video frame to the output video frame. Use 24-hour format with
                    frame number, (HH:MM:SS:FF) or (HH:MM:SS;FF). This setting ignores frame rate
                    conversion. System behavior for Anchor Timecode varies depending on your setting
                    for Source (TimecodeSource). * If Source (TimecodeSource) is set to Specified
                    Start (SPECIFIEDSTART), the first input frame is the specified value in Start
                    Timecode (Start). Anchor Timecode (Anchor) and Start Timecode (Start) are used
                    calculate output timecode. * If Source (TimecodeSource) is set to Start at 0
                    (ZEROBASED) the first frame is 00:00:00:00. * If Source (TimecodeSource) is set
                    to Embedded (EMBEDDED), the first frame is the timecode value on the first input
                    frame of the input.

                    - **Source** *(string) --* Use Source (TimecodeSource) to set how timecodes are
                    handled within this job. To make sure that your video, audio, captions, and
                    markers are synchronized and that time-based features, such as image inserter,
                    work correctly, choose the Timecode source option that matches your assets. All
                    timecodes are in a 24-hour format with frame number (HH:MM:SS:FF). * Embedded
                    (EMBEDDED) - Use the timecode that is in the input video. If no embedded
                    timecode is in the source, the service will use Start at 0 (ZEROBASED) instead.
                    * Start at 0 (ZEROBASED) - Set the timecode of the initial frame to 00:00:00:00.
                    * Specified Start (SPECIFIEDSTART) - Set the timecode of the initial frame to a
                    value other than zero. You use Start timecode (Start) to provide this value.

                    - **Start** *(string) --* Only use when you set Source (TimecodeSource) to
                    Specified start (SPECIFIEDSTART). Use Start timecode (Start) to specify the
                    timecode for the initial frame. Use 24-hour format with frame number,
                    (HH:MM:SS:FF) or (HH:MM:SS;FF).

                    - **TimestampOffset** *(string) --* Only applies to outputs that support
                    program-date-time stamp. Use Timestamp offset (TimestampOffset) to overwrite the
                    timecode date without affecting the time and frame number. Provide the new date
                    as a string in the format "yyyy-mm-dd". To use Time stamp offset, you must also
                    enable Insert program-date-time (InsertProgramDateTime) in the output settings.
                    For example, if the date part of your timecodes is 2002-1-25 and you want to
                    change it to one year later, set Timestamp offset (TimestampOffset) to
                    2003-1-25.

                  - **TimedMetadataInsertion** *(dict) --* Enable Timed metadata insertion
                  (TimedMetadataInsertion) to include ID3 tags in your job. To include timed
                  metadata, you must enable it here, enable it in each output container, and specify
                  tags and timecodes in ID3 insertion (Id3Insertion) objects.

                    - **Id3Insertions** *(list) --* Id3Insertions contains the array of Id3Insertion
                    instances.

                      - *(dict) --* To insert ID3 tags in your output, specify two values. Use ID3
                      tag (Id3) to specify the base 64 encoded string and use Timecode (TimeCode) to
                      specify the time when the tag should be inserted. To insert multiple ID3 tags
                      in your output, create multiple instances of ID3 insertion (Id3Insertion).

                        - **Id3** *(string) --* Use ID3 tag (Id3) to provide a tag value in
                        base64-encode format.

                        - **Timecode** *(string) --* Provide a Timecode (TimeCode) in HH:MM:SS:FF or
                        HH:MM:SS;FF format.

                - **StatusUpdateInterval** *(string) --* Specify how often MediaConvert sends
                STATUS_UPDATE events to Amazon CloudWatch Events. Set the interval, in seconds,
                between status updates. MediaConvert sends an update at this interval from the time
                the service begins processing your job to the time it completes the transcode or
                encounters an error.

                - **Type** *(string) --* A job template can be of two types: system or custom.
                System or built-in job templates can't be modified or deleted by the user.
        """


class ListJobsPaginator(Boto3Paginator):
    """
    Paginator for `list_jobs`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Order: Literal["ASCENDING", "DESCENDING"] = None,
        Queue: str = None,
        Status: Literal["SUBMITTED", "PROGRESSING", "COMPLETE", "CANCELED", "ERROR"] = None,
        PaginationConfig: ListJobsPaginatePaginationConfigTypeDef = None,
    ) -> ListJobsPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`MediaConvert.Client.list_jobs`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/mediaconvert-2017-08-29/ListJobs>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              Order='ASCENDING'|'DESCENDING',
              Queue='string',
              Status='SUBMITTED'|'PROGRESSING'|'COMPLETE'|'CANCELED'|'ERROR',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type Order: string
        :param Order: When you request lists of resources, you can optionally specify whether they
        are sorted in ASCENDING or DESCENDING order. Default varies by resource.

        :type Queue: string
        :param Queue: Provide a queue name to get back only jobs from that queue.

        :type Status: string
        :param Status: A job's status can be SUBMITTED, PROGRESSING, COMPLETE, CANCELED, or ERROR.

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
                'Jobs': [
                    {
                        'AccelerationSettings': {
                            'Mode': 'DISABLED'|'ENABLED'|'PREFERRED'
                        },
                        'AccelerationStatus':
                        'NOT_APPLICABLE'|'IN_PROGRESS'|'ACCELERATED'
                        |'NOT_ACCELERATED',
                        'Arn': 'string',
                        'BillingTagsSource': 'QUEUE'|'PRESET'|'JOB_TEMPLATE'|'JOB',
                        'CreatedAt': datetime(2015, 1, 1),
                        'CurrentPhase': 'PROBING'|'TRANSCODING'|'UPLOADING',
                        'ErrorCode': 123,
                        'ErrorMessage': 'string',
                        'Id': 'string',
                        'JobPercentComplete': 123,
                        'JobTemplate': 'string',
                        'Messages': {
                            'Info': [
                                'string',
                            ],
                            'Warning': [
                                'string',
                            ]
                        },
                        'OutputGroupDetails': [
                            {
                                'OutputDetails': [
                                    {
                                        'DurationInMs': 123,
                                        'VideoDetails': {
                                            'HeightInPx': 123,
                                            'WidthInPx': 123
                                        }
                                    },
                                ]
                            },
                        ],
                        'Priority': 123,
                        'Queue': 'string',
                        'RetryCount': 123,
                        'Role': 'string',
                        'Settings': {
                            'AdAvailOffset': 123,
                            'AvailBlanking': {
                                'AvailBlankingImage': 'string'
                            },
                            'Esam': {
                                'ManifestConfirmConditionNotification': {
                                    'MccXml': 'string'
                                },
                                'ResponseSignalPreroll': 123,
                                'SignalProcessingNotification': {
                                    'SccXml': 'string'
                                }
                            },
                            'Inputs': [
                                {
                                    'AudioSelectorGroups': {
                                        'string': {
                                            'AudioSelectorNames': [
                                                'string',
                                            ]
                                        }
                                    },
                                    'AudioSelectors': {
                                        'string': {
                                            'CustomLanguageCode': 'string',
                                            'DefaultSelection': 'DEFAULT'|'NOT_DEFAULT',
                                            'ExternalAudioFileInput': 'string',
                                            'LanguageCode':
                                            'ENG'|'SPA'|'FRA'
                                            |'DEU'|'GER'|'ZHO'
                                            |'ARA'|'HIN'|'JPN'
                                            |'RUS'|'POR'|'ITA'
                                            |'URD'|'VIE'|'KOR'
                                            |'PAN'|'ABK'|'AAR'
                                            |'AFR'|'AKA'|'SQI'
                                            |'AMH'|'ARG'|'HYE'
                                            |'ASM'|'AVA'|'AVE'
                                            |'AYM'|'AZE'|'BAM'
                                            |'BAK'|'EUS'|'BEL'
                                            |'BEN'|'BIH'|'BIS'
                                            |'BOS'|'BRE'|'BUL'
                                            |'MYA'|'CAT'|'KHM'
                                            |'CHA'|'CHE'|'NYA'
                                            |'CHU'|'CHV'|'COR'
                                            |'COS'|'CRE'|'HRV'
                                            |'CES'|'DAN'|'DIV'
                                            |'NLD'|'DZO'|'ENM'
                                            |'EPO'|'EST'|'EWE'
                                            |'FAO'|'FIJ'|'FIN'
                                            |'FRM'|'FUL'|'GLA'
                                            |'GLG'|'LUG'|'KAT'
                                            |'ELL'|'GRN'|'GUJ'
                                            |'HAT'|'HAU'|'HEB'
                                            |'HER'|'HMO'|'HUN'
                                            |'ISL'|'IDO'|'IBO'
                                            |'IND'|'INA'|'ILE'
                                            |'IKU'|'IPK'|'GLE'
                                            |'JAV'|'KAL'|'KAN'
                                            |'KAU'|'KAS'|'KAZ'
                                            |'KIK'|'KIN'|'KIR'
                                            |'KOM'|'KON'|'KUA'
                                            |'KUR'|'LAO'|'LAT'
                                            |'LAV'|'LIM'|'LIN'
                                            |'LIT'|'LUB'|'LTZ'
                                            |'MKD'|'MLG'|'MSA'
                                            |'MAL'|'MLT'|'GLV'
                                            |'MRI'|'MAR'|'MAH'
                                            |'MON'|'NAU'|'NAV'
                                            |'NDE'|'NBL'|'NDO'
                                            |'NEP'|'SME'|'NOR'
                                            |'NOB'|'NNO'|'OCI'
                                            |'OJI'|'ORI'|'ORM'
                                            |'OSS'|'PLI'|'FAS'
                                            |'POL'|'PUS'|'QUE'
                                            |'QAA'|'RON'|'ROH'
                                            |'RUN'|'SMO'|'SAG'
                                            |'SAN'|'SRD'|'SRB'
                                            |'SNA'|'III'|'SND'
                                            |'SIN'|'SLK'|'SLV'
                                            |'SOM'|'SOT'|'SUN'
                                            |'SWA'|'SSW'|'SWE'
                                            |'TGL'|'TAH'|'TGK'
                                            |'TAM'|'TAT'|'TEL'
                                            |'THA'|'BOD'|'TIR'
                                            |'TON'|'TSO'|'TSN'
                                            |'TUR'|'TUK'|'TWI'
                                            |'UIG'|'UKR'|'UZB'
                                            |'VEN'|'VOL'|'WLN'
                                            |'CYM'|'FRY'|'WOL'
                                            |'XHO'|'YID'|'YOR'
                                            |'ZHA'|'ZUL'|'ORJ'
                                            |'QPC'|'TNG',
                                            'Offset': 123,
                                            'Pids': [
                                                123,
                                            ],
                                            'ProgramSelection': 123,
                                            'RemixSettings': {
                                                'ChannelMapping': {
                                                    'OutputChannels': [
                                                        {
                                                            'InputChannels': [
                                                                123,
                                                            ]
                                                        },
                                                    ]
                                                },
                                                'ChannelsIn': 123,
                                                'ChannelsOut': 123
                                            },
                                            'SelectorType': 'PID'|'TRACK'|'LANGUAGE_CODE',
                                            'Tracks': [
                                                123,
                                            ]
                                        }
                                    },
                                    'CaptionSelectors': {
                                        'string': {
                                            'CustomLanguageCode': 'string',
                                            'LanguageCode':
                                            'ENG'|'SPA'|'FRA'
                                            |'DEU'|'GER'|'ZHO'
                                            |'ARA'|'HIN'|'JPN'
                                            |'RUS'|'POR'|'ITA'
                                            |'URD'|'VIE'|'KOR'
                                            |'PAN'|'ABK'|'AAR'
                                            |'AFR'|'AKA'|'SQI'
                                            |'AMH'|'ARG'|'HYE'
                                            |'ASM'|'AVA'|'AVE'
                                            |'AYM'|'AZE'|'BAM'
                                            |'BAK'|'EUS'|'BEL'
                                            |'BEN'|'BIH'|'BIS'
                                            |'BOS'|'BRE'|'BUL'
                                            |'MYA'|'CAT'|'KHM'
                                            |'CHA'|'CHE'|'NYA'
                                            |'CHU'|'CHV'|'COR'
                                            |'COS'|'CRE'|'HRV'
                                            |'CES'|'DAN'|'DIV'
                                            |'NLD'|'DZO'|'ENM'
                                            |'EPO'|'EST'|'EWE'
                                            |'FAO'|'FIJ'|'FIN'
                                            |'FRM'|'FUL'|'GLA'
                                            |'GLG'|'LUG'|'KAT'
                                            |'ELL'|'GRN'|'GUJ'
                                            |'HAT'|'HAU'|'HEB'
                                            |'HER'|'HMO'|'HUN'
                                            |'ISL'|'IDO'|'IBO'
                                            |'IND'|'INA'|'ILE'
                                            |'IKU'|'IPK'|'GLE'
                                            |'JAV'|'KAL'|'KAN'
                                            |'KAU'|'KAS'|'KAZ'
                                            |'KIK'|'KIN'|'KIR'
                                            |'KOM'|'KON'|'KUA'
                                            |'KUR'|'LAO'|'LAT'
                                            |'LAV'|'LIM'|'LIN'
                                            |'LIT'|'LUB'|'LTZ'
                                            |'MKD'|'MLG'|'MSA'
                                            |'MAL'|'MLT'|'GLV'
                                            |'MRI'|'MAR'|'MAH'
                                            |'MON'|'NAU'|'NAV'
                                            |'NDE'|'NBL'|'NDO'
                                            |'NEP'|'SME'|'NOR'
                                            |'NOB'|'NNO'|'OCI'
                                            |'OJI'|'ORI'|'ORM'
                                            |'OSS'|'PLI'|'FAS'
                                            |'POL'|'PUS'|'QUE'
                                            |'QAA'|'RON'|'ROH'
                                            |'RUN'|'SMO'|'SAG'
                                            |'SAN'|'SRD'|'SRB'
                                            |'SNA'|'III'|'SND'
                                            |'SIN'|'SLK'|'SLV'
                                            |'SOM'|'SOT'|'SUN'
                                            |'SWA'|'SSW'|'SWE'
                                            |'TGL'|'TAH'|'TGK'
                                            |'TAM'|'TAT'|'TEL'
                                            |'THA'|'BOD'|'TIR'
                                            |'TON'|'TSO'|'TSN'
                                            |'TUR'|'TUK'|'TWI'
                                            |'UIG'|'UKR'|'UZB'
                                            |'VEN'|'VOL'|'WLN'
                                            |'CYM'|'FRY'|'WOL'
                                            |'XHO'|'YID'|'YOR'
                                            |'ZHA'|'ZUL'|'ORJ'
                                            |'QPC'|'TNG',
                                            'SourceSettings': {
                                                'AncillarySourceSettings': {
                                                    'Convert608To708': 'UPCONVERT'|'DISABLED',
                                                    'SourceAncillaryChannelNumber': 123,
                                                    'TerminateCaptions': 'END_OF_INPUT'|'DISABLED'
                                                },
                                                'DvbSubSourceSettings': {
                                                    'Pid': 123
                                                },
                                                'EmbeddedSourceSettings': {
                                                    'Convert608To708': 'UPCONVERT'|'DISABLED',
                                                    'Source608ChannelNumber': 123,
                                                    'Source608TrackNumber': 123,
                                                    'TerminateCaptions': 'END_OF_INPUT'|'DISABLED'
                                                },
                                                'FileSourceSettings': {
                                                    'Convert608To708': 'UPCONVERT'|'DISABLED',
                                                    'SourceFile': 'string',
                                                    'TimeDelta': 123
                                                },
                                                'SourceType':
                                                'ANCILLARY'
                                                |'DVB_SUB'
                                                |'EMBEDDED'
                                                |'SCTE20'
                                                |'SCC'
                                                |'TTML'
                                                |'STL'|'SRT'
                                                |'SMI'
                                                |'TELETEXT'
                                                |'NULL_SOURCE'
                                                |'IMSC',
                                                'TeletextSourceSettings': {
                                                    'PageNumber': 'string'
                                                },
                                                'TrackSourceSettings': {
                                                    'TrackNumber': 123
                                                }
                                            }
                                        }
                                    },
                                    'Crop': {
                                        'Height': 123,
                                        'Width': 123,
                                        'X': 123,
                                        'Y': 123
                                    },
                                    'DeblockFilter': 'ENABLED'|'DISABLED',
                                    'DecryptionSettings': {
                                        'DecryptionMode': 'AES_CTR'|'AES_CBC'|'AES_GCM',
                                        'EncryptedDecryptionKey': 'string',
                                        'InitializationVector': 'string',
                                        'KmsKeyRegion': 'string'
                                    },
                                    'DenoiseFilter': 'ENABLED'|'DISABLED',
                                    'FileInput': 'string',
                                    'FilterEnable': 'AUTO'|'DISABLE'|'FORCE',
                                    'FilterStrength': 123,
                                    'ImageInserter': {
                                        'InsertableImages': [
                                            {
                                                'Duration': 123,
                                                'FadeIn': 123,
                                                'FadeOut': 123,
                                                'Height': 123,
                                                'ImageInserterInput': 'string',
                                                'ImageX': 123,
                                                'ImageY': 123,
                                                'Layer': 123,
                                                'Opacity': 123,
                                                'StartTime': 'string',
                                                'Width': 123
                                            },
                                        ]
                                    },
                                    'InputClippings': [
                                        {
                                            'EndTimecode': 'string',
                                            'StartTimecode': 'string'
                                        },
                                    ],
                                    'Position': {
                                        'Height': 123,
                                        'Width': 123,
                                        'X': 123,
                                        'Y': 123
                                    },
                                    'ProgramNumber': 123,
                                    'PsiControl': 'IGNORE_PSI'|'USE_PSI',
                                    'SupplementalImps': [
                                        'string',
                                    ],
                                    'TimecodeSource': 'EMBEDDED'|'ZEROBASED'|'SPECIFIEDSTART',
                                    'TimecodeStart': 'string',
                                    'VideoSelector': {
                                        'AlphaBehavior': 'DISCARD'|'REMAP_TO_LUMA',
                                        'ColorSpace':
                                        'FOLLOW'|'REC_601'|'REC_709'
                                        |'HDR10'|'HLG_2020',
                                        'ColorSpaceUsage': 'FORCE'|'FALLBACK',
                                        'Hdr10Metadata': {
                                            'BluePrimaryX': 123,
                                            'BluePrimaryY': 123,
                                            'GreenPrimaryX': 123,
                                            'GreenPrimaryY': 123,
                                            'MaxContentLightLevel': 123,
                                            'MaxFrameAverageLightLevel': 123,
                                            'MaxLuminance': 123,
                                            'MinLuminance': 123,
                                            'RedPrimaryX': 123,
                                            'RedPrimaryY': 123,
                                            'WhitePointX': 123,
                                            'WhitePointY': 123
                                        },
                                        'Pid': 123,
                                        'ProgramNumber': 123,
                                        'Rotate':
                                        'DEGREE_0'|'DEGREES_90'
                                        |'DEGREES_180'|'DEGREES_270'
                                        |'AUTO'
                                    }
                                },
                            ],
                            'MotionImageInserter': {
                                'Framerate': {
                                    'FramerateDenominator': 123,
                                    'FramerateNumerator': 123
                                },
                                'Input': 'string',
                                'InsertionMode': 'MOV'|'PNG',
                                'Offset': {
                                    'ImageX': 123,
                                    'ImageY': 123
                                },
                                'Playback': 'ONCE'|'REPEAT',
                                'StartTime': 'string'
                            },
                            'NielsenConfiguration': {
                                'BreakoutCode': 123,
                                'DistributorId': 'string'
                            },
                            'OutputGroups': [
                                {
                                    'CustomName': 'string',
                                    'Name': 'string',
                                    'OutputGroupSettings': {
                                        'CmafGroupSettings': {
                                            'AdditionalManifests': [
                                                {
                                                    'ManifestNameModifier': 'string',
                                                    'SelectedOutputs': [
                                                        'string',
                                                    ]
                                                },
                                            ],
                                            'BaseUrl': 'string',
                                            'ClientCache': 'DISABLED'|'ENABLED',
                                            'CodecSpecification': 'RFC_6381'|'RFC_4281',
                                            'Destination': 'string',
                                            'DestinationSettings': {
                                                'S3Settings': {
                                                    'AccessControl': {
                                                        'CannedAcl':
                                                        'PUBLIC_READ'|'AUTHENTICATED_READ'|'BUCKET_OWNER_READ'
                                                        |'BUCKET_OWNER_FULL_CONTROL'
                                                    },
                                                    'Encryption': {
                                                        'EncryptionType':
                                                        'SERVER_SIDE_ENCRYPTION_S3'
                                                        |'SERVER_SIDE_ENCRYPTION_KMS',
                                                        'KmsKeyArn': 'string'
                                                    }
                                                }
                                            },
                                            'Encryption': {
                                                'ConstantInitializationVector': 'string',
                                                'EncryptionMethod': 'SAMPLE_AES'|'AES_CTR',
                                                'InitializationVectorInManifest':
                                                'INCLUDE'
                                                |'EXCLUDE',
                                                'SpekeKeyProvider': {
                                                    'CertificateArn': 'string',
                                                    'DashSignaledSystemIds': [
                                                        'string',
                                                    ],
                                                    'HlsSignaledSystemIds': [
                                                        'string',
                                                    ],
                                                    'ResourceId': 'string',
                                                    'Url': 'string'
                                                },
                                                'StaticKeyProvider': {
                                                    'KeyFormat': 'string',
                                                    'KeyFormatVersions': 'string',
                                                    'StaticKeyValue': 'string',
                                                    'Url': 'string'
                                                },
                                                'Type': 'SPEKE'|'STATIC_KEY'
                                            },
                                            'FragmentLength': 123,
                                            'ManifestCompression': 'GZIP'|'NONE',
                                            'ManifestDurationFormat': 'FLOATING_POINT'|'INTEGER',
                                            'MinBufferTime': 123,
                                            'MinFinalSegmentLength': 123.0,
                                            'MpdProfile': 'MAIN_PROFILE'|'ON_DEMAND_PROFILE',
                                            'SegmentControl': 'SINGLE_FILE'|'SEGMENTED_FILES',
                                            'SegmentLength': 123,
                                            'StreamInfResolution': 'INCLUDE'|'EXCLUDE',
                                            'WriteDashManifest': 'DISABLED'|'ENABLED',
                                            'WriteHlsManifest': 'DISABLED'|'ENABLED'
                                        },
                                        'DashIsoGroupSettings': {
                                            'AdditionalManifests': [
                                                {
                                                    'ManifestNameModifier': 'string',
                                                    'SelectedOutputs': [
                                                        'string',
                                                    ]
                                                },
                                            ],
                                            'BaseUrl': 'string',
                                            'Destination': 'string',
                                            'DestinationSettings': {
                                                'S3Settings': {
                                                    'AccessControl': {
                                                        'CannedAcl':
                                                        'PUBLIC_READ'|'AUTHENTICATED_READ'|'BUCKET_OWNER_READ'
                                                        |'BUCKET_OWNER_FULL_CONTROL'
                                                    },
                                                    'Encryption': {
                                                        'EncryptionType':
                                                        'SERVER_SIDE_ENCRYPTION_S3'
                                                        |'SERVER_SIDE_ENCRYPTION_KMS',
                                                        'KmsKeyArn': 'string'
                                                    }
                                                }
                                            },
                                            'Encryption': {
                                                'PlaybackDeviceCompatibility':
                                                'CENC_V1'
                                                |'UNENCRYPTED_SEI',
                                                'SpekeKeyProvider': {
                                                    'CertificateArn': 'string',
                                                    'ResourceId': 'string',
                                                    'SystemIds': [
                                                        'string',
                                                    ],
                                                    'Url': 'string'
                                                }
                                            },
                                            'FragmentLength': 123,
                                            'HbbtvCompliance': 'HBBTV_1_5'|'NONE',
                                            'MinBufferTime': 123,
                                            'MpdProfile': 'MAIN_PROFILE'|'ON_DEMAND_PROFILE',
                                            'SegmentControl': 'SINGLE_FILE'|'SEGMENTED_FILES',
                                            'SegmentLength': 123,
                                            'WriteSegmentTimelineInRepresentation':
                                            'ENABLED'|'DISABLED'
                                        },
                                        'FileGroupSettings': {
                                            'Destination': 'string',
                                            'DestinationSettings': {
                                                'S3Settings': {
                                                    'AccessControl': {
                                                        'CannedAcl':
                                                        'PUBLIC_READ'|'AUTHENTICATED_READ'|'BUCKET_OWNER_READ'
                                                        |'BUCKET_OWNER_FULL_CONTROL'
                                                    },
                                                    'Encryption': {
                                                        'EncryptionType':
                                                        'SERVER_SIDE_ENCRYPTION_S3'
                                                        |'SERVER_SIDE_ENCRYPTION_KMS',
                                                        'KmsKeyArn': 'string'
                                                    }
                                                }
                                            }
                                        },
                                        'HlsGroupSettings': {
                                            'AdMarkers': [
                                                'ELEMENTAL'|'ELEMENTAL_SCTE35',
                                            ],
                                            'AdditionalManifests': [
                                                {
                                                    'ManifestNameModifier': 'string',
                                                    'SelectedOutputs': [
                                                        'string',
                                                    ]
                                                },
                                            ],
                                            'BaseUrl': 'string',
                                            'CaptionLanguageMappings': [
                                                {
                                                    'CaptionChannel': 123,
                                                    'CustomLanguageCode': 'string',
                                                    'LanguageCode':
                                                    'ENG'|'SPA'|'FRA'|'DEU'|'GER'|'ZHO'|'ARA'|'HIN'|'JPN'|'RUS'|'POR'|'ITA'|'URD'|'VIE'|'KOR'|'PAN'|'ABK'|'AAR'|'AFR'|'AKA'|'SQI'|'AMH'|'ARG'|'HYE'|'ASM'|'AVA'|'AVE'|'AYM'|'AZE'|'BAM'|'BAK'|'EUS'|'BEL'|'BEN'|'BIH'|'BIS'|'BOS'|'BRE'|'BUL'|'MYA'|'CAT'|'KHM'|'CHA'|'CHE'|'NYA'|'CHU'|'CHV'|'COR'|'COS'|'CRE'|'HRV'|'CES'|'DAN'|'DIV'|'NLD'|'DZO'|'ENM'|'EPO'|'EST'|'EWE'|'FAO'|'FIJ'|'FIN'|'FRM'|'FUL'|'GLA'|'GLG'|'LUG'|'KAT'|'ELL'|'GRN'|'GUJ'|'HAT'|'HAU'|'HEB'|'HER'|'HMO'|'HUN'|'ISL'|'IDO'|'IBO'|'IND'|'INA'|'ILE'|'IKU'|'IPK'|'GLE'|'JAV'|'KAL'|'KAN'|'KAU'|'KAS'|'KAZ'|'KIK'|'KIN'|'KIR'|'KOM'|'KON'|'KUA'|'KUR'|'LAO'|'LAT'|'LAV'|'LIM'|'LIN'|'LIT'|'LUB'|'LTZ'|'MKD'|'MLG'|'MSA'|'MAL'|'MLT'|'GLV'|'MRI'|'MAR'|'MAH'|'MON'|'NAU'|'NAV'|'NDE'|'NBL'|'NDO'|'NEP'|'SME'|'NOR'|'NOB'|'NNO'|'OCI'|'OJI'|'ORI'|'ORM'|'OSS'|'PLI'|'FAS'|'POL'|'PUS'|'QUE'|'QAA'|'RON'|'ROH'|'RUN'|'SMO'|'SAG'|'SAN'|'SRD'|'SRB'|'SNA'|'III'|'SND'|'SIN'|'SLK'|'SLV'|'SOM'|'SOT'|'SUN'|'SWA'|'SSW'|'SWE'|'TGL'|'TAH'|'TGK'|'TAM'|'TAT'|'TEL'|'THA'|'BOD'|'TIR'|'TON'|'TSO'|'TSN'|'TUR'|'TUK'|'TWI'|'UIG'|'UKR'|'UZB'|'VEN'|'VOL'|'WLN'|'CYM'|'FRY'|'WOL'|'XHO'|'YID'|'YOR'|'ZHA'|'ZUL'|'ORJ'|'QPC'
                                                    |'TNG',
                                                    'LanguageDescription': 'string'
                                                },
                                            ],
                                            'CaptionLanguageSetting': 'INSERT'|'OMIT'|'NONE',
                                            'ClientCache': 'DISABLED'|'ENABLED',
                                            'CodecSpecification': 'RFC_6381'|'RFC_4281',
                                            'Destination': 'string',
                                            'DestinationSettings': {
                                                'S3Settings': {
                                                    'AccessControl': {
                                                        'CannedAcl':
                                                        'PUBLIC_READ'|'AUTHENTICATED_READ'|'BUCKET_OWNER_READ'
                                                        |'BUCKET_OWNER_FULL_CONTROL'
                                                    },
                                                    'Encryption': {
                                                        'EncryptionType':
                                                        'SERVER_SIDE_ENCRYPTION_S3'
                                                        |'SERVER_SIDE_ENCRYPTION_KMS',
                                                        'KmsKeyArn': 'string'
                                                    }
                                                }
                                            },
                                            'DirectoryStructure':
                                            'SINGLE_DIRECTORY'
                                            |'SUBDIRECTORY_PER_STREAM',
                                            'Encryption': {
                                                'ConstantInitializationVector': 'string',
                                                'EncryptionMethod': 'AES128'|'SAMPLE_AES',
                                                'InitializationVectorInManifest':
                                                'INCLUDE'
                                                |'EXCLUDE',
                                                'OfflineEncrypted': 'ENABLED'|'DISABLED',
                                                'SpekeKeyProvider': {
                                                    'CertificateArn': 'string',
                                                    'ResourceId': 'string',
                                                    'SystemIds': [
                                                        'string',
                                                    ],
                                                    'Url': 'string'
                                                },
                                                'StaticKeyProvider': {
                                                    'KeyFormat': 'string',
                                                    'KeyFormatVersions': 'string',
                                                    'StaticKeyValue': 'string',
                                                    'Url': 'string'
                                                },
                                                'Type': 'SPEKE'|'STATIC_KEY'
                                            },
                                            'ManifestCompression': 'GZIP'|'NONE',
                                            'ManifestDurationFormat': 'FLOATING_POINT'|'INTEGER',
                                            'MinFinalSegmentLength': 123.0,
                                            'MinSegmentLength': 123,
                                            'OutputSelection':
                                            'MANIFESTS_AND_SEGMENTS'
                                            |'SEGMENTS_ONLY',
                                            'ProgramDateTime': 'INCLUDE'|'EXCLUDE',
                                            'ProgramDateTimePeriod': 123,
                                            'SegmentControl': 'SINGLE_FILE'|'SEGMENTED_FILES',
                                            'SegmentLength': 123,
                                            'SegmentsPerSubdirectory': 123,
                                            'StreamInfResolution': 'INCLUDE'|'EXCLUDE',
                                            'TimedMetadataId3Frame': 'NONE'|'PRIV'|'TDRL',
                                            'TimedMetadataId3Period': 123,
                                            'TimestampDeltaMilliseconds': 123
                                        },
                                        'MsSmoothGroupSettings': {
                                            'AdditionalManifests': [
                                                {
                                                    'ManifestNameModifier': 'string',
                                                    'SelectedOutputs': [
                                                        'string',
                                                    ]
                                                },
                                            ],
                                            'AudioDeduplication':
                                            'COMBINE_DUPLICATE_STREAMS'
                                            |'NONE',
                                            'Destination': 'string',
                                            'DestinationSettings': {
                                                'S3Settings': {
                                                    'AccessControl': {
                                                        'CannedAcl':
                                                        'PUBLIC_READ'|'AUTHENTICATED_READ'|'BUCKET_OWNER_READ'
                                                        |'BUCKET_OWNER_FULL_CONTROL'
                                                    },
                                                    'Encryption': {
                                                        'EncryptionType':
                                                        'SERVER_SIDE_ENCRYPTION_S3'
                                                        |'SERVER_SIDE_ENCRYPTION_KMS',
                                                        'KmsKeyArn': 'string'
                                                    }
                                                }
                                            },
                                            'Encryption': {
                                                'SpekeKeyProvider': {
                                                    'CertificateArn': 'string',
                                                    'ResourceId': 'string',
                                                    'SystemIds': [
                                                        'string',
                                                    ],
                                                    'Url': 'string'
                                                }
                                            },
                                            'FragmentLength': 123,
                                            'ManifestEncoding': 'UTF8'|'UTF16'
                                        },
                                        'Type':
                                        'HLS_GROUP_SETTINGS'
                                        |'DASH_ISO_GROUP_SETTINGS'
                                        |'FILE_GROUP_SETTINGS'
                                        |'MS_SMOOTH_GROUP_SETTINGS'
                                        |'CMAF_GROUP_SETTINGS'
                                    },
                                    'Outputs': [
                                        {
                                            'AudioDescriptions': [
                                                {
                                                    'AudioNormalizationSettings': {
                                                        'Algorithm':
                                                        'ITU_BS_1770_1'|'ITU_BS_1770_2'|'ITU_BS_1770_3'
                                                        |'ITU_BS_1770_4',
                                                        'AlgorithmControl':
                                                        'CORRECT_AUDIO'
                                                        |'MEASURE_ONLY',
                                                        'CorrectionGateLevel': 123,
                                                        'LoudnessLogging': 'LOG'|'DONT_LOG',
                                                        'PeakCalculation': 'TRUE_PEAK'|'NONE',
                                                        'TargetLkfs': 123.0
                                                    },
                                                    'AudioSourceName': 'string',
                                                    'AudioType': 123,
                                                    'AudioTypeControl':
                                                    'FOLLOW_INPUT'
                                                    |'USE_CONFIGURED',
                                                    'CodecSettings': {
                                                        'AacSettings': {
                                                            'AudioDescriptionBroadcasterMix':
                                                            'BROADCASTER_MIXED_AD'
                                                            |'NORMAL',
                                                            'Bitrate': 123,
                                                            'CodecProfile': 'LC'|'HEV1'|'HEV2',
                                                            'CodingMode':
                                                            'AD_RECEIVER_MIX'|'CODING_MODE_1_0'|'CODING_MODE_1_1'|'CODING_MODE_2_0'
                                                            |'CODING_MODE_5_1',
                                                            'RateControlMode': 'CBR'|'VBR',
                                                            'RawFormat': 'LATM_LOAS'|'NONE',
                                                            'SampleRate': 123,
                                                            'Specification': 'MPEG2'|'MPEG4',
                                                            'VbrQuality':
                                                            'LOW'|'MEDIUM_LOW'|'MEDIUM_HIGH'
                                                            |'HIGH'
                                                        },
                                                        'Ac3Settings': {
                                                            'Bitrate': 123,
                                                            'BitstreamMode':
                                                            'COMPLETE_MAIN'|'COMMENTARY'|'DIALOGUE'|'EMERGENCY'|'HEARING_IMPAIRED'|'MUSIC_AND_EFFECTS'|'VISUALLY_IMPAIRED'
                                                            |'VOICE_OVER',
                                                            'CodingMode':
                                                            'CODING_MODE_1_0'|'CODING_MODE_1_1'|'CODING_MODE_2_0'
                                                            |'CODING_MODE_3_2_LFE',
                                                            'Dialnorm': 123,
                                                            'DynamicRangeCompressionProfile':
                                                            'FILM_STANDARD'
                                                            |'NONE',
                                                            'LfeFilter': 'ENABLED'|'DISABLED',
                                                            'MetadataControl':
                                                            'FOLLOW_INPUT'
                                                            |'USE_CONFIGURED',
                                                            'SampleRate': 123
                                                        },
                                                        'AiffSettings': {
                                                            'BitDepth': 123,
                                                            'Channels': 123,
                                                            'SampleRate': 123
                                                        },
                                                        'Codec':
                                                        'AAC'|'MP2'|'WAV'|'AIFF'|'AC3'|'EAC3'|'EAC3_ATMOS'
                                                        |'PASSTHROUGH',
                                                        'Eac3AtmosSettings': {
                                                            'Bitrate': 123,
                                                            'BitstreamMode': 'COMPLETE_MAIN',
                                                            'CodingMode': 'CODING_MODE_9_1_6',
                                                            'DialogueIntelligence':
                                                            'ENABLED'
                                                            |'DISABLED',
                                                            'DynamicRangeCompressionLine':
                                                            'NONE'|'FILM_STANDARD'|'FILM_LIGHT'|'MUSIC_STANDARD'|'MUSIC_LIGHT'
                                                            |'SPEECH',
                                                            'DynamicRangeCompressionRf':
                                                            'NONE'|'FILM_STANDARD'|'FILM_LIGHT'|'MUSIC_STANDARD'|'MUSIC_LIGHT'
                                                            |'SPEECH',
                                                            'LoRoCenterMixLevel': 123.0,
                                                            'LoRoSurroundMixLevel': 123.0,
                                                            'LtRtCenterMixLevel': 123.0,
                                                            'LtRtSurroundMixLevel': 123.0,
                                                            'MeteringMode':
                                                            'LEQ_A'|'ITU_BS_1770_1'|'ITU_BS_1770_2'|'ITU_BS_1770_3'
                                                            |'ITU_BS_1770_4',
                                                            'SampleRate': 123,
                                                            'SpeechThreshold': 123,
                                                            'StereoDownmix':
                                                            'NOT_INDICATED'|'STEREO'|'SURROUND'
                                                            |'DPL2',
                                                            'SurroundExMode':
                                                            'NOT_INDICATED'|'ENABLED'
                                                            |'DISABLED'
                                                        },
                                                        'Eac3Settings': {
                                                            'AttenuationControl':
                                                            'ATTENUATE_3_DB'
                                                            |'NONE',
                                                            'Bitrate': 123,
                                                            'BitstreamMode':
                                                            'COMPLETE_MAIN'|'COMMENTARY'|'EMERGENCY'|'HEARING_IMPAIRED'
                                                            |'VISUALLY_IMPAIRED',
                                                            'CodingMode':
                                                            'CODING_MODE_1_0'|'CODING_MODE_2_0'
                                                            |'CODING_MODE_3_2',
                                                            'DcFilter': 'ENABLED'|'DISABLED',
                                                            'Dialnorm': 123,
                                                            'DynamicRangeCompressionLine':
                                                            'NONE'|'FILM_STANDARD'|'FILM_LIGHT'|'MUSIC_STANDARD'|'MUSIC_LIGHT'
                                                            |'SPEECH',
                                                            'DynamicRangeCompressionRf':
                                                            'NONE'|'FILM_STANDARD'|'FILM_LIGHT'|'MUSIC_STANDARD'|'MUSIC_LIGHT'
                                                            |'SPEECH',
                                                            'LfeControl': 'LFE'|'NO_LFE',
                                                            'LfeFilter': 'ENABLED'|'DISABLED',
                                                            'LoRoCenterMixLevel': 123.0,
                                                            'LoRoSurroundMixLevel': 123.0,
                                                            'LtRtCenterMixLevel': 123.0,
                                                            'LtRtSurroundMixLevel': 123.0,
                                                            'MetadataControl':
                                                            'FOLLOW_INPUT'
                                                            |'USE_CONFIGURED',
                                                            'PassthroughControl':
                                                            'WHEN_POSSIBLE'
                                                            |'NO_PASSTHROUGH',
                                                            'PhaseControl':
                                                            'SHIFT_90_DEGREES'
                                                            |'NO_SHIFT',
                                                            'SampleRate': 123,
                                                            'StereoDownmix':
                                                            'NOT_INDICATED'|'LO_RO'|'LT_RT'
                                                            |'DPL2',
                                                            'SurroundExMode':
                                                            'NOT_INDICATED'|'ENABLED'
                                                            |'DISABLED',
                                                            'SurroundMode':
                                                            'NOT_INDICATED'|'ENABLED'
                                                            |'DISABLED'
                                                        },
                                                        'Mp2Settings': {
                                                            'Bitrate': 123,
                                                            'Channels': 123,
                                                            'SampleRate': 123
                                                        },
                                                        'WavSettings': {
                                                            'BitDepth': 123,
                                                            'Channels': 123,
                                                            'Format': 'RIFF'|'RF64',
                                                            'SampleRate': 123
                                                        }
                                                    },
                                                    'CustomLanguageCode': 'string',
                                                    'LanguageCode':
                                                    'ENG'|'SPA'|'FRA'|'DEU'|'GER'|'ZHO'|'ARA'|'HIN'|'JPN'|'RUS'|'POR'|'ITA'|'URD'|'VIE'|'KOR'|'PAN'|'ABK'|'AAR'|'AFR'|'AKA'|'SQI'|'AMH'|'ARG'|'HYE'|'ASM'|'AVA'|'AVE'|'AYM'|'AZE'|'BAM'|'BAK'|'EUS'|'BEL'|'BEN'|'BIH'|'BIS'|'BOS'|'BRE'|'BUL'|'MYA'|'CAT'|'KHM'|'CHA'|'CHE'|'NYA'|'CHU'|'CHV'|'COR'|'COS'|'CRE'|'HRV'|'CES'|'DAN'|'DIV'|'NLD'|'DZO'|'ENM'|'EPO'|'EST'|'EWE'|'FAO'|'FIJ'|'FIN'|'FRM'|'FUL'|'GLA'|'GLG'|'LUG'|'KAT'|'ELL'|'GRN'|'GUJ'|'HAT'|'HAU'|'HEB'|'HER'|'HMO'|'HUN'|'ISL'|'IDO'|'IBO'|'IND'|'INA'|'ILE'|'IKU'|'IPK'|'GLE'|'JAV'|'KAL'|'KAN'|'KAU'|'KAS'|'KAZ'|'KIK'|'KIN'|'KIR'|'KOM'|'KON'|'KUA'|'KUR'|'LAO'|'LAT'|'LAV'|'LIM'|'LIN'|'LIT'|'LUB'|'LTZ'|'MKD'|'MLG'|'MSA'|'MAL'|'MLT'|'GLV'|'MRI'|'MAR'|'MAH'|'MON'|'NAU'|'NAV'|'NDE'|'NBL'|'NDO'|'NEP'|'SME'|'NOR'|'NOB'|'NNO'|'OCI'|'OJI'|'ORI'|'ORM'|'OSS'|'PLI'|'FAS'|'POL'|'PUS'|'QUE'|'QAA'|'RON'|'ROH'|'RUN'|'SMO'|'SAG'|'SAN'|'SRD'|'SRB'|'SNA'|'III'|'SND'|'SIN'|'SLK'|'SLV'|'SOM'|'SOT'|'SUN'|'SWA'|'SSW'|'SWE'|'TGL'|'TAH'|'TGK'|'TAM'|'TAT'|'TEL'|'THA'|'BOD'|'TIR'|'TON'|'TSO'|'TSN'|'TUR'|'TUK'|'TWI'|'UIG'|'UKR'|'UZB'|'VEN'|'VOL'|'WLN'|'CYM'|'FRY'|'WOL'|'XHO'|'YID'|'YOR'|'ZHA'|'ZUL'|'ORJ'|'QPC'
                                                    |'TNG',
                                                    'LanguageCodeControl':
                                                    'FOLLOW_INPUT'
                                                    |'USE_CONFIGURED',
                                                    'RemixSettings': {
                                                        'ChannelMapping': {
                                                            'OutputChannels': [
                                                                {
                                                                    'InputChannels': [
                                                                        123,
                                                                    ]
                                                                },
                                                            ]
                                                        },
                                                        'ChannelsIn': 123,
                                                        'ChannelsOut': 123
                                                    },
                                                    'StreamName': 'string'
                                                },
                                            ],
                                            'CaptionDescriptions': [
                                                {
                                                    'CaptionSelectorName': 'string',
                                                    'CustomLanguageCode': 'string',
                                                    'DestinationSettings': {
                                                        'BurninDestinationSettings': {
                                                            'Alignment': 'CENTERED'|'LEFT',
                                                            'BackgroundColor':
                                                            'NONE'|'BLACK'
                                                            |'WHITE',
                                                            'BackgroundOpacity': 123,
                                                            'FontColor':
                                                            'WHITE'|'BLACK'|'YELLOW'|'RED'|'GREEN'
                                                            |'BLUE',
                                                            'FontOpacity': 123,
                                                            'FontResolution': 123,
                                                            'FontScript': 'AUTOMATIC'|'HANS'|'HANT',
                                                            'FontSize': 123,
                                                            'OutlineColor':
                                                            'BLACK'|'WHITE'|'YELLOW'|'RED'|'GREEN'
                                                            |'BLUE',
                                                            'OutlineSize': 123,
                                                            'ShadowColor': 'NONE'|'BLACK'|'WHITE',
                                                            'ShadowOpacity': 123,
                                                            'ShadowXOffset': 123,
                                                            'ShadowYOffset': 123,
                                                            'TeletextSpacing':
                                                            'FIXED_GRID'
                                                            |'PROPORTIONAL',
                                                            'XPosition': 123,
                                                            'YPosition': 123
                                                        },
                                                        'DestinationType':
                                                        'BURN_IN'|'DVB_SUB'|'EMBEDDED'|'EMBEDDED_PLUS_SCTE20'|'IMSC'|'SCTE20_PLUS_EMBEDDED'|'SCC'|'SRT'|'SMI'|'TELETEXT'|'TTML'
                                                        |'WEBVTT',
                                                        'DvbSubDestinationSettings': {
                                                            'Alignment': 'CENTERED'|'LEFT',
                                                            'BackgroundColor':
                                                            'NONE'|'BLACK'
                                                            |'WHITE',
                                                            'BackgroundOpacity': 123,
                                                            'FontColor':
                                                            'WHITE'|'BLACK'|'YELLOW'|'RED'|'GREEN'
                                                            |'BLUE',
                                                            'FontOpacity': 123,
                                                            'FontResolution': 123,
                                                            'FontScript': 'AUTOMATIC'|'HANS'|'HANT',
                                                            'FontSize': 123,
                                                            'OutlineColor':
                                                            'BLACK'|'WHITE'|'YELLOW'|'RED'|'GREEN'
                                                            |'BLUE',
                                                            'OutlineSize': 123,
                                                            'ShadowColor': 'NONE'|'BLACK'|'WHITE',
                                                            'ShadowOpacity': 123,
                                                            'ShadowXOffset': 123,
                                                            'ShadowYOffset': 123,
                                                            'SubtitlingType':
                                                            'HEARING_IMPAIRED'
                                                            |'STANDARD',
                                                            'TeletextSpacing':
                                                            'FIXED_GRID'
                                                            |'PROPORTIONAL',
                                                            'XPosition': 123,
                                                            'YPosition': 123
                                                        },
                                                        'EmbeddedDestinationSettings': {
                                                            'Destination608ChannelNumber': 123,
                                                            'Destination708ServiceNumber': 123
                                                        },
                                                        'ImscDestinationSettings': {
                                                            'StylePassthrough': 'ENABLED'|'DISABLED'
                                                        },
                                                        'SccDestinationSettings': {
                                                            'Framerate':
                                                            'FRAMERATE_23_97'|'FRAMERATE_24'|'FRAMERATE_25'|'FRAMERATE_29_97_DROPFRAME'
                                                            |'FRAMERATE_29_97_NON_DROPFRAME'
                                                        },
                                                        'TeletextDestinationSettings': {
                                                            'PageNumber': 'string',
                                                            'PageTypes': [
                                                                'PAGE_TYPE_INITIAL'
                                                                |'PAGE_TYPE_SUBTITLE'
                                                                |'PAGE_TYPE_ADDL_INFO'
                                                                |'PAGE_TYPE_PROGRAM_SCHEDULE'
                                                                |'PAGE_TYPE_HEARING_IMPAIRED_SUBTITLE',
                                                            ]
                                                        },
                                                        'TtmlDestinationSettings': {
                                                            'StylePassthrough': 'ENABLED'|'DISABLED'
                                                        }
                                                    },
                                                    'LanguageCode':
                                                    'ENG'|'SPA'|'FRA'|'DEU'|'GER'|'ZHO'|'ARA'|'HIN'|'JPN'|'RUS'|'POR'|'ITA'|'URD'|'VIE'|'KOR'|'PAN'|'ABK'|'AAR'|'AFR'|'AKA'|'SQI'|'AMH'|'ARG'|'HYE'|'ASM'|'AVA'|'AVE'|'AYM'|'AZE'|'BAM'|'BAK'|'EUS'|'BEL'|'BEN'|'BIH'|'BIS'|'BOS'|'BRE'|'BUL'|'MYA'|'CAT'|'KHM'|'CHA'|'CHE'|'NYA'|'CHU'|'CHV'|'COR'|'COS'|'CRE'|'HRV'|'CES'|'DAN'|'DIV'|'NLD'|'DZO'|'ENM'|'EPO'|'EST'|'EWE'|'FAO'|'FIJ'|'FIN'|'FRM'|'FUL'|'GLA'|'GLG'|'LUG'|'KAT'|'ELL'|'GRN'|'GUJ'|'HAT'|'HAU'|'HEB'|'HER'|'HMO'|'HUN'|'ISL'|'IDO'|'IBO'|'IND'|'INA'|'ILE'|'IKU'|'IPK'|'GLE'|'JAV'|'KAL'|'KAN'|'KAU'|'KAS'|'KAZ'|'KIK'|'KIN'|'KIR'|'KOM'|'KON'|'KUA'|'KUR'|'LAO'|'LAT'|'LAV'|'LIM'|'LIN'|'LIT'|'LUB'|'LTZ'|'MKD'|'MLG'|'MSA'|'MAL'|'MLT'|'GLV'|'MRI'|'MAR'|'MAH'|'MON'|'NAU'|'NAV'|'NDE'|'NBL'|'NDO'|'NEP'|'SME'|'NOR'|'NOB'|'NNO'|'OCI'|'OJI'|'ORI'|'ORM'|'OSS'|'PLI'|'FAS'|'POL'|'PUS'|'QUE'|'QAA'|'RON'|'ROH'|'RUN'|'SMO'|'SAG'|'SAN'|'SRD'|'SRB'|'SNA'|'III'|'SND'|'SIN'|'SLK'|'SLV'|'SOM'|'SOT'|'SUN'|'SWA'|'SSW'|'SWE'|'TGL'|'TAH'|'TGK'|'TAM'|'TAT'|'TEL'|'THA'|'BOD'|'TIR'|'TON'|'TSO'|'TSN'|'TUR'|'TUK'|'TWI'|'UIG'|'UKR'|'UZB'|'VEN'|'VOL'|'WLN'|'CYM'|'FRY'|'WOL'|'XHO'|'YID'|'YOR'|'ZHA'|'ZUL'|'ORJ'|'QPC'
                                                    |'TNG',
                                                    'LanguageDescription': 'string'
                                                },
                                            ],
                                            'ContainerSettings': {
                                                'Container':
                                                'F4V'|'ISMV'
                                                |'M2TS'
                                                |'M3U8'
                                                |'CMFC'
                                                |'MOV'|'MP4'
                                                |'MPD'|'MXF'
                                                |'RAW',
                                                'F4vSettings': {
                                                    'MoovPlacement': 'PROGRESSIVE_DOWNLOAD'|'NORMAL'
                                                },
                                                'M2tsSettings': {
                                                    'AudioBufferModel': 'DVB'|'ATSC',
                                                    'AudioFramesPerPes': 123,
                                                    'AudioPids': [
                                                        123,
                                                    ],
                                                    'Bitrate': 123,
                                                    'BufferModel': 'MULTIPLEX'|'NONE',
                                                    'DvbNitSettings': {
                                                        'NetworkId': 123,
                                                        'NetworkName': 'string',
                                                        'NitInterval': 123
                                                    },
                                                    'DvbSdtSettings': {
                                                        'OutputSdt':
                                                        'SDT_FOLLOW'|'SDT_FOLLOW_IF_PRESENT'|'SDT_MANUAL'
                                                        |'SDT_NONE',
                                                        'SdtInterval': 123,
                                                        'ServiceName': 'string',
                                                        'ServiceProviderName': 'string'
                                                    },
                                                    'DvbSubPids': [
                                                        123,
                                                    ],
                                                    'DvbTdtSettings': {
                                                        'TdtInterval': 123
                                                    },
                                                    'DvbTeletextPid': 123,
                                                    'EbpAudioInterval':
                                                    'VIDEO_AND_FIXED_INTERVALS'
                                                    |'VIDEO_INTERVAL',
                                                    'EbpPlacement':
                                                    'VIDEO_AND_AUDIO_PIDS'
                                                    |'VIDEO_PID',
                                                    'EsRateInPes': 'INCLUDE'|'EXCLUDE',
                                                    'ForceTsVideoEbpOrder': 'FORCE'|'DEFAULT',
                                                    'FragmentTime': 123.0,
                                                    'MaxPcrInterval': 123,
                                                    'MinEbpInterval': 123,
                                                    'NielsenId3': 'INSERT'|'NONE',
                                                    'NullPacketBitrate': 123.0,
                                                    'PatInterval': 123,
                                                    'PcrControl':
                                                    'PCR_EVERY_PES_PACKET'
                                                    |'CONFIGURED_PCR_PERIOD',
                                                    'PcrPid': 123,
                                                    'PmtInterval': 123,
                                                    'PmtPid': 123,
                                                    'PrivateMetadataPid': 123,
                                                    'ProgramNumber': 123,
                                                    'RateMode': 'VBR'|'CBR',
                                                    'Scte35Esam': {
                                                        'Scte35EsamPid': 123
                                                    },
                                                    'Scte35Pid': 123,
                                                    'Scte35Source': 'PASSTHROUGH'|'NONE',
                                                    'SegmentationMarkers':
                                                    'NONE'|'RAI_SEGSTART'|'RAI_ADAPT'|'PSI_SEGSTART'|'EBP'
                                                    |'EBP_LEGACY',
                                                    'SegmentationStyle':
                                                    'MAINTAIN_CADENCE'
                                                    |'RESET_CADENCE',
                                                    'SegmentationTime': 123.0,
                                                    'TimedMetadataPid': 123,
                                                    'TransportStreamId': 123,
                                                    'VideoPid': 123
                                                },
                                                'M3u8Settings': {
                                                    'AudioFramesPerPes': 123,
                                                    'AudioPids': [
                                                        123,
                                                    ],
                                                    'NielsenId3': 'INSERT'|'NONE',
                                                    'PatInterval': 123,
                                                    'PcrControl':
                                                    'PCR_EVERY_PES_PACKET'
                                                    |'CONFIGURED_PCR_PERIOD',
                                                    'PcrPid': 123,
                                                    'PmtInterval': 123,
                                                    'PmtPid': 123,
                                                    'PrivateMetadataPid': 123,
                                                    'ProgramNumber': 123,
                                                    'Scte35Pid': 123,
                                                    'Scte35Source': 'PASSTHROUGH'|'NONE',
                                                    'TimedMetadata': 'PASSTHROUGH'|'NONE',
                                                    'TimedMetadataPid': 123,
                                                    'TransportStreamId': 123,
                                                    'VideoPid': 123
                                                },
                                                'MovSettings': {
                                                    'ClapAtom': 'INCLUDE'|'EXCLUDE',
                                                    'CslgAtom': 'INCLUDE'|'EXCLUDE',
                                                    'Mpeg2FourCCControl': 'XDCAM'|'MPEG',
                                                    'PaddingControl': 'OMNEON'|'NONE',
                                                    'Reference': 'SELF_CONTAINED'|'EXTERNAL'
                                                },
                                                'Mp4Settings': {
                                                    'CslgAtom': 'INCLUDE'|'EXCLUDE',
                                                    'FreeSpaceBox': 'INCLUDE'|'EXCLUDE',
                                                    'MoovPlacement':
                                                    'PROGRESSIVE_DOWNLOAD'
                                                    |'NORMAL',
                                                    'Mp4MajorBrand': 'string'
                                                },
                                                'MpdSettings': {
                                                    'CaptionContainerType': 'RAW'|'FRAGMENTED_MP4',
                                                    'Scte35Esam': 'INSERT'|'NONE',
                                                    'Scte35Source': 'PASSTHROUGH'|'NONE'
                                                }
                                            },
                                            'Extension': 'string',
                                            'NameModifier': 'string',
                                            'OutputSettings': {
                                                'HlsSettings': {
                                                    'AudioGroupId': 'string',
                                                    'AudioOnlyContainer': 'AUTOMATIC'|'M2TS',
                                                    'AudioRenditionSets': 'string',
                                                    'AudioTrackType':
                                                    'ALTERNATE_AUDIO_AUTO_SELECT_DEFAULT'|'ALTERNATE_AUDIO_AUTO_SELECT'|'ALTERNATE_AUDIO_NOT_AUTO_SELECT'
                                                    |'AUDIO_ONLY_VARIANT_STREAM',
                                                    'IFrameOnlyManifest': 'INCLUDE'|'EXCLUDE',
                                                    'SegmentModifier': 'string'
                                                }
                                            },
                                            'Preset': 'string',
                                            'VideoDescription': {
                                                'AfdSignaling': 'NONE'|'AUTO'|'FIXED',
                                                'AntiAlias': 'DISABLED'|'ENABLED',
                                                'CodecSettings': {
                                                    'Codec':
                                                    'FRAME_CAPTURE'|'H_264'|'H_265'|'MPEG2'
                                                    |'PRORES',
                                                    'FrameCaptureSettings': {
                                                        'FramerateDenominator': 123,
                                                        'FramerateNumerator': 123,
                                                        'MaxCaptures': 123,
                                                        'Quality': 123
                                                    },
                                                    'H264Settings': {
                                                        'AdaptiveQuantization':
                                                        'OFF'|'LOW'|'MEDIUM'|'HIGH'|'HIGHER'
                                                        |'MAX',
                                                        'Bitrate': 123,
                                                        'CodecLevel':
                                                        'AUTO'|'LEVEL_1'|'LEVEL_1_1'|'LEVEL_1_2'|'LEVEL_1_3'|'LEVEL_2'|'LEVEL_2_1'|'LEVEL_2_2'|'LEVEL_3'|'LEVEL_3_1'|'LEVEL_3_2'|'LEVEL_4'|'LEVEL_4_1'|'LEVEL_4_2'|'LEVEL_5'|'LEVEL_5_1'
                                                        |'LEVEL_5_2',
                                                        'CodecProfile':
                                                        'BASELINE'|'HIGH'|'HIGH_10BIT'|'HIGH_422'|'HIGH_422_10BIT'
                                                        |'MAIN',
                                                        'DynamicSubGop': 'ADAPTIVE'|'STATIC',
                                                        'EntropyEncoding': 'CABAC'|'CAVLC',
                                                        'FieldEncoding': 'PAFF'|'FORCE_FIELD',
                                                        'FlickerAdaptiveQuantization':
                                                        'DISABLED'
                                                        |'ENABLED',
                                                        'FramerateControl':
                                                        'INITIALIZE_FROM_SOURCE'
                                                        |'SPECIFIED',
                                                        'FramerateConversionAlgorithm':
                                                        'DUPLICATE_DROP'
                                                        |'INTERPOLATE',
                                                        'FramerateDenominator': 123,
                                                        'FramerateNumerator': 123,
                                                        'GopBReference': 'DISABLED'|'ENABLED',
                                                        'GopClosedCadence': 123,
                                                        'GopSize': 123.0,
                                                        'GopSizeUnits': 'FRAMES'|'SECONDS',
                                                        'HrdBufferInitialFillPercentage': 123,
                                                        'HrdBufferSize': 123,
                                                        'InterlaceMode':
                                                        'PROGRESSIVE'|'TOP_FIELD'|'BOTTOM_FIELD'|'FOLLOW_TOP_FIELD'
                                                        |'FOLLOW_BOTTOM_FIELD',
                                                        'MaxBitrate': 123,
                                                        'MinIInterval': 123,
                                                        'NumberBFramesBetweenReferenceFrames': 123,
                                                        'NumberReferenceFrames': 123,
                                                        'ParControl':
                                                        'INITIALIZE_FROM_SOURCE'
                                                        |'SPECIFIED',
                                                        'ParDenominator': 123,
                                                        'ParNumerator': 123,
                                                        'QualityTuningLevel':
                                                        'SINGLE_PASS'|'SINGLE_PASS_HQ'
                                                        |'MULTI_PASS_HQ',
                                                        'QvbrSettings': {
                                                            'MaxAverageBitrate': 123,
                                                            'QvbrQualityLevel': 123
                                                        },
                                                        'RateControlMode': 'VBR'|'CBR'|'QVBR',
                                                        'RepeatPps': 'DISABLED'|'ENABLED',
                                                        'SceneChangeDetect':
                                                        'DISABLED'|'ENABLED'
                                                        |'TRANSITION_DETECTION',
                                                        'Slices': 123,
                                                        'SlowPal': 'DISABLED'|'ENABLED',
                                                        'Softness': 123,
                                                        'SpatialAdaptiveQuantization':
                                                        'DISABLED'
                                                        |'ENABLED',
                                                        'Syntax': 'DEFAULT'|'RP2027',
                                                        'Telecine': 'NONE'|'SOFT'|'HARD',
                                                        'TemporalAdaptiveQuantization':
                                                        'DISABLED'
                                                        |'ENABLED',
                                                        'UnregisteredSeiTimecode':
                                                        'DISABLED'
                                                        |'ENABLED'
                                                    },
                                                    'H265Settings': {
                                                        'AdaptiveQuantization':
                                                        'OFF'|'LOW'|'MEDIUM'|'HIGH'|'HIGHER'
                                                        |'MAX',
                                                        'AlternateTransferFunctionSei':
                                                        'DISABLED'
                                                        |'ENABLED',
                                                        'Bitrate': 123,
                                                        'CodecLevel':
                                                        'AUTO'|'LEVEL_1'|'LEVEL_2'|'LEVEL_2_1'|'LEVEL_3'|'LEVEL_3_1'|'LEVEL_4'|'LEVEL_4_1'|'LEVEL_5'|'LEVEL_5_1'|'LEVEL_5_2'|'LEVEL_6'|'LEVEL_6_1'
                                                        |'LEVEL_6_2',
                                                        'CodecProfile':
                                                        'MAIN_MAIN'|'MAIN_HIGH'|'MAIN10_MAIN'|'MAIN10_HIGH'|'MAIN_422_8BIT_MAIN'|'MAIN_422_8BIT_HIGH'|'MAIN_422_10BIT_MAIN'
                                                        |'MAIN_422_10BIT_HIGH',
                                                        'DynamicSubGop': 'ADAPTIVE'|'STATIC',
                                                        'FlickerAdaptiveQuantization':
                                                        'DISABLED'
                                                        |'ENABLED',
                                                        'FramerateControl':
                                                        'INITIALIZE_FROM_SOURCE'
                                                        |'SPECIFIED',
                                                        'FramerateConversionAlgorithm':
                                                        'DUPLICATE_DROP'
                                                        |'INTERPOLATE',
                                                        'FramerateDenominator': 123,
                                                        'FramerateNumerator': 123,
                                                        'GopBReference': 'DISABLED'|'ENABLED',
                                                        'GopClosedCadence': 123,
                                                        'GopSize': 123.0,
                                                        'GopSizeUnits': 'FRAMES'|'SECONDS',
                                                        'HrdBufferInitialFillPercentage': 123,
                                                        'HrdBufferSize': 123,
                                                        'InterlaceMode':
                                                        'PROGRESSIVE'|'TOP_FIELD'|'BOTTOM_FIELD'|'FOLLOW_TOP_FIELD'
                                                        |'FOLLOW_BOTTOM_FIELD',
                                                        'MaxBitrate': 123,
                                                        'MinIInterval': 123,
                                                        'NumberBFramesBetweenReferenceFrames': 123,
                                                        'NumberReferenceFrames': 123,
                                                        'ParControl':
                                                        'INITIALIZE_FROM_SOURCE'
                                                        |'SPECIFIED',
                                                        'ParDenominator': 123,
                                                        'ParNumerator': 123,
                                                        'QualityTuningLevel':
                                                        'SINGLE_PASS'|'SINGLE_PASS_HQ'
                                                        |'MULTI_PASS_HQ',
                                                        'QvbrSettings': {
                                                            'MaxAverageBitrate': 123,
                                                            'QvbrQualityLevel': 123
                                                        },
                                                        'RateControlMode': 'VBR'|'CBR'|'QVBR',
                                                        'SampleAdaptiveOffsetFilterMode':
                                                        'DEFAULT'|'ADAPTIVE'
                                                        |'OFF',
                                                        'SceneChangeDetect':
                                                        'DISABLED'|'ENABLED'
                                                        |'TRANSITION_DETECTION',
                                                        'Slices': 123,
                                                        'SlowPal': 'DISABLED'|'ENABLED',
                                                        'SpatialAdaptiveQuantization':
                                                        'DISABLED'
                                                        |'ENABLED',
                                                        'Telecine': 'NONE'|'SOFT'|'HARD',
                                                        'TemporalAdaptiveQuantization':
                                                        'DISABLED'
                                                        |'ENABLED',
                                                        'TemporalIds': 'DISABLED'|'ENABLED',
                                                        'Tiles': 'DISABLED'|'ENABLED',
                                                        'UnregisteredSeiTimecode':
                                                        'DISABLED'
                                                        |'ENABLED',
                                                        'WriteMp4PackagingType': 'HVC1'|'HEV1'
                                                    },
                                                    'Mpeg2Settings': {
                                                        'AdaptiveQuantization':
                                                        'OFF'|'LOW'|'MEDIUM'
                                                        |'HIGH',
                                                        'Bitrate': 123,
                                                        'CodecLevel':
                                                        'AUTO'|'LOW'|'MAIN'|'HIGH1440'
                                                        |'HIGH',
                                                        'CodecProfile': 'MAIN'|'PROFILE_422',
                                                        'DynamicSubGop': 'ADAPTIVE'|'STATIC',
                                                        'FramerateControl':
                                                        'INITIALIZE_FROM_SOURCE'
                                                        |'SPECIFIED',
                                                        'FramerateConversionAlgorithm':
                                                        'DUPLICATE_DROP'
                                                        |'INTERPOLATE',
                                                        'FramerateDenominator': 123,
                                                        'FramerateNumerator': 123,
                                                        'GopClosedCadence': 123,
                                                        'GopSize': 123.0,
                                                        'GopSizeUnits': 'FRAMES'|'SECONDS',
                                                        'HrdBufferInitialFillPercentage': 123,
                                                        'HrdBufferSize': 123,
                                                        'InterlaceMode':
                                                        'PROGRESSIVE'|'TOP_FIELD'|'BOTTOM_FIELD'|'FOLLOW_TOP_FIELD'
                                                        |'FOLLOW_BOTTOM_FIELD',
                                                        'IntraDcPrecision':
                                                        'AUTO'|'INTRA_DC_PRECISION_8'|'INTRA_DC_PRECISION_9'|'INTRA_DC_PRECISION_10'
                                                        |'INTRA_DC_PRECISION_11',
                                                        'MaxBitrate': 123,
                                                        'MinIInterval': 123,
                                                        'NumberBFramesBetweenReferenceFrames': 123,
                                                        'ParControl':
                                                        'INITIALIZE_FROM_SOURCE'
                                                        |'SPECIFIED',
                                                        'ParDenominator': 123,
                                                        'ParNumerator': 123,
                                                        'QualityTuningLevel':
                                                        'SINGLE_PASS'
                                                        |'MULTI_PASS',
                                                        'RateControlMode': 'VBR'|'CBR',
                                                        'SceneChangeDetect': 'DISABLED'|'ENABLED',
                                                        'SlowPal': 'DISABLED'|'ENABLED',
                                                        'Softness': 123,
                                                        'SpatialAdaptiveQuantization':
                                                        'DISABLED'
                                                        |'ENABLED',
                                                        'Syntax': 'DEFAULT'|'D_10',
                                                        'Telecine': 'NONE'|'SOFT'|'HARD',
                                                        'TemporalAdaptiveQuantization':
                                                        'DISABLED'
                                                        |'ENABLED'
                                                    },
                                                    'ProresSettings': {
                                                        'CodecProfile':
                                                        'APPLE_PRORES_422'|'APPLE_PRORES_422_HQ'|'APPLE_PRORES_422_LT'
                                                        |'APPLE_PRORES_422_PROXY',
                                                        'FramerateControl':
                                                        'INITIALIZE_FROM_SOURCE'
                                                        |'SPECIFIED',
                                                        'FramerateConversionAlgorithm':
                                                        'DUPLICATE_DROP'
                                                        |'INTERPOLATE',
                                                        'FramerateDenominator': 123,
                                                        'FramerateNumerator': 123,
                                                        'InterlaceMode':
                                                        'PROGRESSIVE'|'TOP_FIELD'|'BOTTOM_FIELD'|'FOLLOW_TOP_FIELD'
                                                        |'FOLLOW_BOTTOM_FIELD',
                                                        'ParControl':
                                                        'INITIALIZE_FROM_SOURCE'
                                                        |'SPECIFIED',
                                                        'ParDenominator': 123,
                                                        'ParNumerator': 123,
                                                        'SlowPal': 'DISABLED'|'ENABLED',
                                                        'Telecine': 'NONE'|'HARD'
                                                    }
                                                },
                                                'ColorMetadata': 'IGNORE'|'INSERT',
                                                'Crop': {
                                                    'Height': 123,
                                                    'Width': 123,
                                                    'X': 123,
                                                    'Y': 123
                                                },
                                                'DropFrameTimecode': 'DISABLED'|'ENABLED',
                                                'FixedAfd': 123,
                                                'Height': 123,
                                                'Position': {
                                                    'Height': 123,
                                                    'Width': 123,
                                                    'X': 123,
                                                    'Y': 123
                                                },
                                                'RespondToAfd': 'NONE'|'RESPOND'|'PASSTHROUGH',
                                                'ScalingBehavior': 'DEFAULT'|'STRETCH_TO_OUTPUT',
                                                'Sharpness': 123,
                                                'TimecodeInsertion': 'DISABLED'|'PIC_TIMING_SEI',
                                                'VideoPreprocessors': {
                                                    'ColorCorrector': {
                                                        'Brightness': 123,
                                                        'ColorSpaceConversion':
                                                        'NONE'|'FORCE_601'|'FORCE_709'|'FORCE_HDR10'
                                                        |'FORCE_HLG_2020',
                                                        'Contrast': 123,
                                                        'Hdr10Metadata': {
                                                            'BluePrimaryX': 123,
                                                            'BluePrimaryY': 123,
                                                            'GreenPrimaryX': 123,
                                                            'GreenPrimaryY': 123,
                                                            'MaxContentLightLevel': 123,
                                                            'MaxFrameAverageLightLevel': 123,
                                                            'MaxLuminance': 123,
                                                            'MinLuminance': 123,
                                                            'RedPrimaryX': 123,
                                                            'RedPrimaryY': 123,
                                                            'WhitePointX': 123,
                                                            'WhitePointY': 123
                                                        },
                                                        'Hue': 123,
                                                        'Saturation': 123
                                                    },
                                                    'Deinterlacer': {
                                                        'Algorithm':
                                                        'INTERPOLATE'|'INTERPOLATE_TICKER'|'BLEND'
                                                        |'BLEND_TICKER',
                                                        'Control': 'FORCE_ALL_FRAMES'|'NORMAL',
                                                        'Mode':
                                                        'DEINTERLACE'|'INVERSE_TELECINE'
                                                        |'ADAPTIVE'
                                                    },
                                                    'DolbyVision': {
                                                        'L6Metadata': {
                                                            'MaxCll': 123,
                                                            'MaxFall': 123
                                                        },
                                                        'L6Mode':
                                                        'PASSTHROUGH'|'RECALCULATE'
                                                        |'SPECIFY',
                                                        'Profile': 'PROFILE_5'
                                                    },
                                                    'ImageInserter': {
                                                        'InsertableImages': [
                                                            {
                                                                'Duration': 123,
                                                                'FadeIn': 123,
                                                                'FadeOut': 123,
                                                                'Height': 123,
                                                                'ImageInserterInput': 'string',
                                                                'ImageX': 123,
                                                                'ImageY': 123,
                                                                'Layer': 123,
                                                                'Opacity': 123,
                                                                'StartTime': 'string',
                                                                'Width': 123
                                                            },
                                                        ]
                                                    },
                                                    'NoiseReducer': {
                                                        'Filter':
                                                        'BILATERAL'|'MEAN'|'GAUSSIAN'|'LANCZOS'|'SHARPEN'|'CONSERVE'|'SPATIAL'
                                                        |'TEMPORAL',
                                                        'FilterSettings': {
                                                            'Strength': 123
                                                        },
                                                        'SpatialFilterSettings': {
                                                            'PostFilterSharpenStrength': 123,
                                                            'Speed': 123,
                                                            'Strength': 123
                                                        },
                                                        'TemporalFilterSettings': {
                                                            'AggressiveMode': 123,
                                                            'Speed': 123,
                                                            'Strength': 123
                                                        }
                                                    },
                                                    'TimecodeBurnin': {
                                                        'FontSize': 123,
                                                        'Position':
                                                        'TOP_CENTER'|'TOP_LEFT'|'TOP_RIGHT'|'MIDDLE_LEFT'|'MIDDLE_CENTER'|'MIDDLE_RIGHT'|'BOTTOM_LEFT'|'BOTTOM_CENTER'
                                                        |'BOTTOM_RIGHT',
                                                        'Prefix': 'string'
                                                    }
                                                },
                                                'Width': 123
                                            }
                                        },
                                    ]
                                },
                            ],
                            'TimecodeConfig': {
                                'Anchor': 'string',
                                'Source': 'EMBEDDED'|'ZEROBASED'|'SPECIFIEDSTART',
                                'Start': 'string',
                                'TimestampOffset': 'string'
                            },
                            'TimedMetadataInsertion': {
                                'Id3Insertions': [
                                    {
                                        'Id3': 'string',
                                        'Timecode': 'string'
                                    },
                                ]
                            }
                        },
                        'SimulateReservedQueue': 'DISABLED'|'ENABLED',
                        'Status': 'SUBMITTED'|'PROGRESSING'|'COMPLETE'|'CANCELED'|'ERROR',
                        'StatusUpdateInterval':
                        'SECONDS_10'|'SECONDS_12'|'SECONDS_15'|'SECONDS_20'
                        |'SECONDS_30'|'SECONDS_60'|'SECONDS_120'|'SECONDS_180'
                        |'SECONDS_240'|'SECONDS_300'|'SECONDS_360'|'SECONDS_420'
                        |'SECONDS_480'|'SECONDS_540'|'SECONDS_600',
                        'Timing': {
                            'FinishTime': datetime(2015, 1, 1),
                            'StartTime': datetime(2015, 1, 1),
                            'SubmitTime': datetime(2015, 1, 1)
                        },
                        'UserMetadata': {
                            'string': 'string'
                        }
                    },
                ],

            }
          **Response Structure**

          - *(dict) --*

            - **Jobs** *(list) --* List of jobs

              - *(dict) --* Each job converts an input file into an output file or files. For more
              information, see the User Guide at
              http://docs.aws.amazon.com/mediaconvert/latest/ug/what-is.html

                - **AccelerationSettings** *(dict) --* Accelerated transcoding can significantly
                speed up jobs with long, visually complex content.

                  - **Mode** *(string) --* Specify the conditions when the service will run your job
                  with accelerated transcoding.

                - **AccelerationStatus** *(string) --* Describes whether the current job is running
                with accelerated transcoding. For jobs that have Acceleration (AccelerationMode) set
                to DISABLED, AccelerationStatus is always NOT_APPLICABLE. For jobs that have
                Acceleration (AccelerationMode) set to ENABLED or PREFERRED, AccelerationStatus is
                one of the other states. AccelerationStatus is IN_PROGRESS initially, while the
                service determines whether the input files and job settings are compatible with
                accelerated transcoding. If they are, AcclerationStatus is ACCELERATED. If your
                input files and job settings aren't compatible with accelerated transcoding, the
                service either fails your job or runs it without accelerated transcoding, depending
                on how you set Acceleration (AccelerationMode). When the service runs your job
                without accelerated transcoding, AccelerationStatus is NOT_ACCELERATED.

                - **Arn** *(string) --* An identifier for this resource that is unique within all of
                AWS.

                - **BillingTagsSource** *(string) --* Optional. Choose a tag type that AWS Billing
                and Cost Management will use to sort your AWS Elemental MediaConvert costs on any
                billing report that you set up. Any transcoding outputs that don't have an
                associated tag will appear in your billing report unsorted. If you don't choose a
                valid value for this field, your job outputs will appear on the billing report
                unsorted.

                - **CreatedAt** *(datetime) --* The time, in Unix epoch format in seconds, when the
                job got created.

                - **CurrentPhase** *(string) --* A job's phase can be PROBING, TRANSCODING OR
                UPLOADING

                - **ErrorCode** *(integer) --* Error code for the job

                - **ErrorMessage** *(string) --* Error message of Job

                - **Id** *(string) --* A portion of the job's ARN, unique within your AWS Elemental
                MediaConvert resources

                - **JobPercentComplete** *(integer) --* An estimate of how far your job has
                progressed. This estimate is shown as a percentage of the total time from when your
                job leaves its queue to when your output files appear in your output Amazon S3
                bucket. AWS Elemental MediaConvert provides jobPercentComplete in CloudWatch
                STATUS_UPDATE events and in the response to GetJob and ListJobs requests. The
                jobPercentComplete estimate is reliable for the following input containers:
                Quicktime, Transport Stream, MP4, and MXF. For some jobs, the service can't provide
                information about job progress. In those cases, jobPercentComplete returns a null
                value.

                - **JobTemplate** *(string) --* The job template that the job is created from, if it
                is created from a job template.

                - **Messages** *(dict) --* Provides messages from the service about jobs that you
                have already successfully submitted.

                  - **Info** *(list) --* List of messages that are informational only and don't
                  indicate a problem with your job.

                    - *(string) --*

                  - **Warning** *(list) --* List of messages that warn about conditions that might
                  cause your job not to run or to fail.

                    - *(string) --*

                - **OutputGroupDetails** *(list) --* List of output group details

                  - *(dict) --* Contains details about the output groups specified in the job
                  settings.

                    - **OutputDetails** *(list) --* Details about the output

                      - *(dict) --* Details regarding output

                        - **DurationInMs** *(integer) --* Duration in milliseconds

                        - **VideoDetails** *(dict) --* Contains details about the output's video
                        stream

                          - **HeightInPx** *(integer) --* Height in pixels for the output

                          - **WidthInPx** *(integer) --* Width in pixels for the output

                - **Priority** *(integer) --* Relative priority on the job.

                - **Queue** *(string) --* Optional. When you create a job, you can specify a queue
                to send it to. If you don't specify, the job will go to the default queue. For more
                about queues, see the User Guide topic at
                http://docs.aws.amazon.com/mediaconvert/latest/ug/what-is.html

                - **RetryCount** *(integer) --* The number of times that the service automatically
                attempted to process your job after encountering an error.

                - **Role** *(string) --* The IAM role you use for creating this job. For details
                about permissions, see the User Guide topic at the User Guide at
                http://docs.aws.amazon.com/mediaconvert/latest/ug/iam-role.html

                - **Settings** *(dict) --* JobSettings contains all the transcode settings for a
                job.

                  - **AdAvailOffset** *(integer) --* When specified, this offset (in milliseconds)
                  is added to the input Ad Avail PTS time.

                  - **AvailBlanking** *(dict) --* Settings for ad avail blanking. Video can be
                  blanked or overlaid with an image, and audio muted during SCTE-35 triggered ad
                  avails.

                    - **AvailBlankingImage** *(string) --* Blanking image to be used. Leave empty
                    for solid black. Only bmp and png images are supported.

                  - **Esam** *(dict) --* Settings for Event Signaling And Messaging (ESAM).

                    - **ManifestConfirmConditionNotification** *(dict) --* Specifies an ESAM
                    ManifestConfirmConditionNotification XML as per OC-SP-ESAM-API-I03-131025. The
                    transcoder uses the manifest conditioning instructions that you provide in the
                    setting MCC XML (mccXml).

                      - **MccXml** *(string) --* Provide your ESAM
                      ManifestConfirmConditionNotification XML document inside your JSON job
                      settings. Form the XML document as per OC-SP-ESAM-API-I03-131025. The
                      transcoder will use the Manifest Conditioning instructions in the message that
                      you supply.

                    - **ResponseSignalPreroll** *(integer) --* Specifies the stream distance, in
                    milliseconds, between the SCTE 35 messages that the transcoder places and the
                    splice points that they refer to. If the time between the start of the asset and
                    the SCTE-35 message is less than this value, then the transcoder places the
                    SCTE-35 marker at the beginning of the stream.

                    - **SignalProcessingNotification** *(dict) --* Specifies an ESAM
                    SignalProcessingNotification XML as per OC-SP-ESAM-API-I03-131025. The
                    transcoder uses the signal processing instructions that you provide in the
                    setting SCC XML (sccXml).

                      - **SccXml** *(string) --* Provide your ESAM SignalProcessingNotification XML
                      document inside your JSON job settings. Form the XML document as per
                      OC-SP-ESAM-API-I03-131025. The transcoder will use the signal processing
                      instructions in the message that you supply. Provide your ESAM
                      SignalProcessingNotification XML document inside your JSON job settings. For
                      your MPEG2-TS file outputs, if you want the service to place SCTE-35 markers
                      at the insertion points you specify in the XML document, you must also enable
                      SCTE-35 ESAM (scte35Esam). Note that you can either specify an ESAM XML
                      document or enable SCTE-35 passthrough. You can't do both.

                  - **Inputs** *(list) --* Use Inputs (inputs) to define source file used in the
                  transcode job. There can be multiple inputs add in a job. These inputs will be
                  concantenated together to create the output.

                    - *(dict) --* Specifies media input

                      - **AudioSelectorGroups** *(dict) --* Specifies set of audio selectors within
                      an input to combine. An input may have multiple audio selector groups. See
                      "Audio Selector Group":#inputs-audio_selector_group for more information.

                        - *(string) --*

                          - *(dict) --* Group of Audio Selectors

                            - **AudioSelectorNames** *(list) --* Name of an Audio Selector within
                            the same input to include in the group. Audio selector names are
                            standardized, based on their order within the input (e.g., "Audio
                            Selector 1"). The audio selector name parameter can be repeated to add
                            any number of audio selectors to the group.

                              - *(string) --*

                      - **AudioSelectors** *(dict) --* Use Audio selectors (AudioSelectors) to
                      specify a track or set of tracks from the input that you will use in your
                      outputs. You can use mutiple Audio selectors per input.

                        - *(string) --*

                          - *(dict) --* Selector for Audio

                            - **CustomLanguageCode** *(string) --* Selects a specific language code
                            from within an audio source, using the ISO 639-2 or ISO 639-3
                            three-letter language code

                            - **DefaultSelection** *(string) --* Enable this setting on one audio
                            selector to set it as the default for the job. The service uses this
                            default for outputs where it can't find the specified input audio. If
                            you don't set a default, those outputs have no audio.

                            - **ExternalAudioFileInput** *(string) --* Specifies audio data from an
                            external file source.

                            - **LanguageCode** *(string) --* Selects a specific language code from
                            within an audio source.

                            - **Offset** *(integer) --* Specifies a time delta in milliseconds to
                            offset the audio from the input video.

                            - **Pids** *(list) --* Selects a specific PID from within an audio
                            source (e.g. 257 selects PID 0x101).

                              - *(integer) --*

                            - **ProgramSelection** *(integer) --* Use this setting for input streams
                            that contain Dolby E, to have the service extract specific program data
                            from the track. To select multiple programs, create multiple selectors
                            with the same Track and different Program numbers. In the console, this
                            setting is visible when you set Selector type to Track. Choose the
                            program number from the dropdown list. If you are sending a JSON file,
                            provide the program ID, which is part of the audio metadata. If your
                            input file has incorrect metadata, you can choose All channels instead
                            of a program number to have the service ignore the program IDs and
                            include all the programs in the track.

                            - **RemixSettings** *(dict) --* Use these settings to reorder the audio
                            channels of one input to match those of another input. This allows you
                            to combine the two files into a single output, one after the other.

                              - **ChannelMapping** *(dict) --* Channel mapping (ChannelMapping)
                              contains the group of fields that hold the remixing value for each
                              channel. Units are in dB. Acceptable values are within the range from
                              -60 (mute) through 6. A setting of 0 passes the input channel
                              unchanged to the output channel (no attenuation or amplification).

                                - **OutputChannels** *(list) --* List of output channels

                                  - *(dict) --* OutputChannel mapping settings.

                                    - **InputChannels** *(list) --* List of input channels

                                      - *(integer) --*

                              - **ChannelsIn** *(integer) --* Specify the number of audio channels
                              from your input that you want to use in your output. With remixing,
                              you might combine or split the data in these channels, so the number
                              of channels in your final output might be different.

                              - **ChannelsOut** *(integer) --* Specify the number of channels in
                              this output after remixing. Valid values: 1, 2, 4, 6, 8... 64. (1 and
                              even numbers to 64.)

                            - **SelectorType** *(string) --* Specifies the type of the audio
                            selector.

                            - **Tracks** *(list) --* Identify a track from the input audio to
                            include in this selector by entering the track index number. To include
                            several tracks in a single audio selector, specify multiple tracks as
                            follows. Using the console, enter a comma-separated list. For examle,
                            type "1,2,3" to include tracks 1 through 3. Specifying directly in your
                            JSON job file, provide the track numbers in an array. For example,
                            "tracks": [1,2,3].

                              - *(integer) --*

                      - **CaptionSelectors** *(dict) --* Use Captions selectors (CaptionSelectors)
                      to specify the captions data from the input that you will use in your outputs.
                      You can use mutiple captions selectors per input.

                        - *(string) --*

                          - *(dict) --* Set up captions in your outputs by first selecting them from
                          your input here.

                            - **CustomLanguageCode** *(string) --* The specific language to extract
                            from source, using the ISO 639-2 or ISO 639-3 three-letter language
                            code. If input is SCTE-27, complete this field and/or PID to select the
                            caption language to extract. If input is DVB-Sub and output is Burn-in
                            or SMPTE-TT, complete this field and/or PID to select the caption
                            language to extract. If input is DVB-Sub that is being passed through,
                            omit this field (and PID field); there is no way to extract a specific
                            language with pass-through captions.

                            - **LanguageCode** *(string) --* The specific language to extract from
                            source. If input is SCTE-27, complete this field and/or PID to select
                            the caption language to extract. If input is DVB-Sub and output is
                            Burn-in or SMPTE-TT, complete this field and/or PID to select the
                            caption language to extract. If input is DVB-Sub that is being passed
                            through, omit this field (and PID field); there is no way to extract a
                            specific language with pass-through captions.

                            - **SourceSettings** *(dict) --* If your input captions are SCC, TTML,
                            STL, SMI, SRT, or IMSC in an xml file, specify the URI of the input
                            captions source file. If your input captions are IMSC in an IMF package,
                            use TrackSourceSettings instead of FileSoureSettings.

                              - **AncillarySourceSettings** *(dict) --* Settings for ancillary
                              captions source.

                                - **Convert608To708** *(string) --* Specify whether this set of
                                input captions appears in your outputs in both 608 and 708 format.
                                If you choose Upconvert (UPCONVERT), MediaConvert includes the
                                captions data in two ways: it passes the 608 data through using the
                                608 compatibility bytes fields of the 708 wrapper, and it also
                                translates the 608 data into 708.

                                - **SourceAncillaryChannelNumber** *(integer) --* Specifies the 608
                                channel number in the ancillary data track from which to extract
                                captions. Unused for passthrough.

                                - **TerminateCaptions** *(string) --* By default, the service
                                terminates any unterminated captions at the end of each input. If
                                you want the caption to continue onto your next input, disable this
                                setting.

                              - **DvbSubSourceSettings** *(dict) --* DVB Sub Source Settings

                                - **Pid** *(integer) --* When using DVB-Sub with Burn-In or
                                SMPTE-TT, use this PID for the source content. Unused for DVB-Sub
                                passthrough. All DVB-Sub content is passed through, regardless of
                                selectors.

                              - **EmbeddedSourceSettings** *(dict) --* Settings for embedded
                              captions Source

                                - **Convert608To708** *(string) --* Specify whether this set of
                                input captions appears in your outputs in both 608 and 708 format.
                                If you choose Upconvert (UPCONVERT), MediaConvert includes the
                                captions data in two ways: it passes the 608 data through using the
                                608 compatibility bytes fields of the 708 wrapper, and it also
                                translates the 608 data into 708.

                                - **Source608ChannelNumber** *(integer) --* Specifies the 608/708
                                channel number within the video track from which to extract
                                captions. Unused for passthrough.

                                - **Source608TrackNumber** *(integer) --* Specifies the video track
                                index used for extracting captions. The system only supports one
                                input video track, so this should always be set to '1'.

                                - **TerminateCaptions** *(string) --* By default, the service
                                terminates any unterminated captions at the end of each input. If
                                you want the caption to continue onto your next input, disable this
                                setting.

                              - **FileSourceSettings** *(dict) --* If your input captions are SCC,
                              SMI, SRT, STL, TTML, or IMSC 1.1 in an xml file, specify the URI of
                              the input caption source file. If your caption source is IMSC in an
                              IMF package, use TrackSourceSettings instead of FileSoureSettings.

                                - **Convert608To708** *(string) --* Specify whether this set of
                                input captions appears in your outputs in both 608 and 708 format.
                                If you choose Upconvert (UPCONVERT), MediaConvert includes the
                                captions data in two ways: it passes the 608 data through using the
                                608 compatibility bytes fields of the 708 wrapper, and it also
                                translates the 608 data into 708.

                                - **SourceFile** *(string) --* External caption file used for
                                loading captions. Accepted file extensions are 'scc', 'ttml',
                                'dfxp', 'stl', 'srt', 'xml', and 'smi'.

                                - **TimeDelta** *(integer) --* Specifies a time delta in seconds to
                                offset the captions from the source file.

                              - **SourceType** *(string) --* Use Source (SourceType) to identify the
                              format of your input captions. The service cannot auto-detect caption
                              format.

                              - **TeletextSourceSettings** *(dict) --* Settings specific to Teletext
                              caption sources, including Page number.

                                - **PageNumber** *(string) --* Use Page Number (PageNumber) to
                                specify the three-digit hexadecimal page number that will be used
                                for Teletext captions. Do not use this setting if you are passing
                                through teletext from the input source to output.

                              - **TrackSourceSettings** *(dict) --* Settings specific to caption
                              sources that are specified by track number. Currently, this is only
                              IMSC captions in an IMF package. If your caption source is IMSC 1.1 in
                              a separate xml file, use FileSourceSettings instead of
                              TrackSourceSettings.

                                - **TrackNumber** *(integer) --* Use this setting to select a single
                                captions track from a source. Track numbers correspond to the order
                                in the captions source file. For IMF sources, track numbering is
                                based on the order that the captions appear in the CPL. For example,
                                use 1 to select the captions asset that is listed first in the CPL.
                                To include more than one captions track in your job outputs, create
                                multiple input captions selectors. Specify one track per selector.

                      - **Crop** *(dict) --* Use Cropping selection (crop) to specify the video area
                      that the service will include in the output video frame. If you specify a
                      value here, it will override any value that you specify in the output setting
                      Cropping selection (crop).

                        - **Height** *(integer) --* Height of rectangle in pixels. Specify only even
                        numbers.

                        - **Width** *(integer) --* Width of rectangle in pixels. Specify only even
                        numbers.

                        - **X** *(integer) --* The distance, in pixels, between the rectangle and
                        the left edge of the video frame. Specify only even numbers.

                        - **Y** *(integer) --* The distance, in pixels, between the rectangle and
                        the top edge of the video frame. Specify only even numbers.

                      - **DeblockFilter** *(string) --* Enable Deblock (InputDeblockFilter) to
                      produce smoother motion in the output. Default is disabled. Only manaully
                      controllable for MPEG2 and uncompressed video inputs.

                      - **DecryptionSettings** *(dict) --* Settings for decrypting any input files
                      that you encrypt before you upload them to Amazon S3. MediaConvert can decrypt
                      files only when you use AWS Key Management Service (KMS) to encrypt the data
                      key that you use to encrypt your content.

                        - **DecryptionMode** *(string) --* Specify the encryption mode that you used
                        to encrypt your input files.

                        - **EncryptedDecryptionKey** *(string) --* Warning! Don't provide your
                        encryption key in plaintext. Your job settings could be intercepted, making
                        your encrypted content vulnerable. Specify the encrypted version of the data
                        key that you used to encrypt your content. The data key must be encrypted by
                        AWS Key Management Service (KMS). The key can be 128, 192, or 256 bits.

                        - **InitializationVector** *(string) --* Specify the initialization vector
                        that you used when you encrypted your content before uploading it to Amazon
                        S3. You can use a 16-byte initialization vector with any encryption mode.
                        Or, you can use a 12-byte initialization vector with GCM or CTR.
                        MediaConvert accepts only initialization vectors that are base64-encoded.

                        - **KmsKeyRegion** *(string) --* Specify the AWS Region for AWS Key
                        Management Service (KMS) that you used to encrypt your data key, if that
                        Region is different from the one you are using for AWS Elemental
                        MediaConvert.

                      - **DenoiseFilter** *(string) --* Enable Denoise (InputDenoiseFilter) to
                      filter noise from the input. Default is disabled. Only applicable to MPEG2,
                      H.264, H.265, and uncompressed video inputs.

                      - **FileInput** *(string) --* Specify the source file for your transcoding
                      job. You can use multiple inputs in a single job. The service concatenates
                      these inputs, in the order that you specify them in the job, to create the
                      outputs. If your input format is IMF, specify your input by providing the path
                      to your CPL. For example, "s3://bucket/vf/cpl.xml". If the CPL is in an
                      incomplete IMP, make sure to use *Supplemental IMPs* (SupplementalImps) to
                      specify any supplemental IMPs that contain assets referenced by the CPL.

                      - **FilterEnable** *(string) --* Use Filter enable (InputFilterEnable) to
                      specify how the transcoding service applies the denoise and deblock filters.
                      You must also enable the filters separately, with Denoise (InputDenoiseFilter)
                      and Deblock (InputDeblockFilter). * Auto - The transcoding service determines
                      whether to apply filtering, depending on input type and quality. * Disable -
                      The input is not filtered. This is true even if you use the API to enable them
                      in (InputDeblockFilter) and (InputDeblockFilter). * Force - The in put is
                      filtered regardless of input type.

                      - **FilterStrength** *(integer) --* Use Filter strength (FilterStrength) to
                      adjust the magnitude the input filter settings (Deblock and Denoise). The
                      range is -5 to 5. Default is 0.

                      - **ImageInserter** *(dict) --* Enable the image inserter feature to include a
                      graphic overlay on your video. Enable or disable this feature for each input
                      individually. This setting is disabled by default.

                        - **InsertableImages** *(list) --* Specify the images that you want to
                        overlay on your video. The images must be PNG or TGA files.

                          - *(dict) --* Settings that specify how your still graphic overlay
                          appears.

                            - **Duration** *(integer) --* Specify the time, in milliseconds, for the
                            image to remain on the output video. This duration includes fade-in time
                            but not fade-out time.

                            - **FadeIn** *(integer) --* Specify the length of time, in milliseconds,
                            between the Start time that you specify for the image insertion and the
                            time that the image appears at full opacity. Full opacity is the level
                            that you specify for the opacity setting. If you don't specify a value
                            for Fade-in, the image will appear abruptly at the overlay start time.

                            - **FadeOut** *(integer) --* Specify the length of time, in
                            milliseconds, between the end of the time that you have specified for
                            the image overlay Duration and when the overlaid image has faded to
                            total transparency. If you don't specify a value for Fade-out, the image
                            will disappear abruptly at the end of the inserted image duration.

                            - **Height** *(integer) --* Specify the height of the inserted image in
                            pixels. If you specify a value that's larger than the video resolution
                            height, the service will crop your overlaid image to fit. To use the
                            native height of the image, keep this setting blank.

                            - **ImageInserterInput** *(string) --* Specify the HTTP, HTTPS, or
                            Amazon S3 location of the image that you want to overlay on the video.
                            Use a PNG or TGA file.

                            - **ImageX** *(integer) --* Specify the distance, in pixels, between the
                            inserted image and the left edge of the video frame. Required for any
                            image overlay that you specify.

                            - **ImageY** *(integer) --* Specify the distance, in pixels, between the
                            overlaid image and the top edge of the video frame. Required for any
                            image overlay that you specify.

                            - **Layer** *(integer) --* Specify how overlapping inserted images
                            appear. Images with higher values for Layer appear on top of images with
                            lower values for Layer.

                            - **Opacity** *(integer) --* Use Opacity (Opacity) to specify how much
                            of the underlying video shows through the inserted image. 0 is
                            transparent and 100 is fully opaque. Default is 50.

                            - **StartTime** *(string) --* Specify the timecode of the frame that you
                            want the overlay to first appear on. This must be in timecode
                            (HH:MM:SS:FF or HH:MM:SS;FF) format. Remember to take into account your
                            timecode source settings.

                            - **Width** *(integer) --* Specify the width of the inserted image in
                            pixels. If you specify a value that's larger than the video resolution
                            width, the service will crop your overlaid image to fit. To use the
                            native width of the image, keep this setting blank.

                      - **InputClippings** *(list) --* (InputClippings) contains sets of start and
                      end times that together specify a portion of the input to be used in the
                      outputs. If you provide only a start time, the clip will be the entire input
                      from that point to the end. If you provide only an end time, it will be the
                      entire input up to that point. When you specify more than one input clip, the
                      transcoding service creates the job outputs by stringing the clips together in
                      the order you specify them.

                        - *(dict) --* To transcode only portions of your input (clips), include one
                        Input clipping (one instance of InputClipping in the JSON job file) for each
                        input clip. All input clips you specify will be included in every output of
                        the job.

                          - **EndTimecode** *(string) --* Set End timecode (EndTimecode) to the end
                          of the portion of the input you are clipping. The frame corresponding to
                          the End timecode value is included in the clip. Start timecode or End
                          timecode may be left blank, but not both. Use the format HH:MM:SS:FF or
                          HH:MM:SS;FF, where HH is the hour, MM is the minute, SS is the second, and
                          FF is the frame number. When choosing this value, take into account your
                          setting for timecode source under input settings (InputTimecodeSource).
                          For example, if you have embedded timecodes that start at 01:00:00:00 and
                          you want your clip to end six minutes into the video, use 01:06:00:00.

                          - **StartTimecode** *(string) --* Set Start timecode (StartTimecode) to
                          the beginning of the portion of the input you are clipping. The frame
                          corresponding to the Start timecode value is included in the clip. Start
                          timecode or End timecode may be left blank, but not both. Use the format
                          HH:MM:SS:FF or HH:MM:SS;FF, where HH is the hour, MM is the minute, SS is
                          the second, and FF is the frame number. When choosing this value, take
                          into account your setting for Input timecode source. For example, if you
                          have embedded timecodes that start at 01:00:00:00 and you want your clip
                          to begin five minutes into the video, use 01:05:00:00.

                      - **Position** *(dict) --* Use Selection placement (position) to define the
                      video area in your output frame. The area outside of the rectangle that you
                      specify here is black. If you specify a value here, it will override any value
                      that you specify in the output setting Selection placement (position). If you
                      specify a value here, this will override any AFD values in your input, even if
                      you set Respond to AFD (RespondToAfd) to Respond (RESPOND). If you specify a
                      value here, this will ignore anything that you specify for the setting Scaling
                      Behavior (scalingBehavior).

                        - **Height** *(integer) --* Height of rectangle in pixels. Specify only even
                        numbers.

                        - **Width** *(integer) --* Width of rectangle in pixels. Specify only even
                        numbers.

                        - **X** *(integer) --* The distance, in pixels, between the rectangle and
                        the left edge of the video frame. Specify only even numbers.

                        - **Y** *(integer) --* The distance, in pixels, between the rectangle and
                        the top edge of the video frame. Specify only even numbers.

                      - **ProgramNumber** *(integer) --* Use Program (programNumber) to select a
                      specific program from within a multi-program transport stream. Note that Quad
                      4K is not currently supported. Default is the first program within the
                      transport stream. If the program you specify doesn't exist, the transcoding
                      service will use this default.

                      - **PsiControl** *(string) --* Set PSI control (InputPsiControl) for transport
                      stream inputs to specify which data the demux process to scans. * Ignore PSI -
                      Scan all PIDs for audio and video. * Use PSI - Scan only PSI data.

                      - **SupplementalImps** *(list) --* Provide a list of any necessary
                      supplemental IMPs. You need supplemental IMPs if the CPL that you're using for
                      your input is in an incomplete IMP. Specify either the supplemental IMP
                      directories with a trailing slash or the ASSETMAP.xml files. For example
                      ["s3://bucket/ov/", "s3://bucket/vf2/ASSETMAP.xml"]. You don't need to specify
                      the IMP that contains your input CPL, because the service automatically
                      detects it.

                        - *(string) --*

                      - **TimecodeSource** *(string) --* Use this Timecode source setting, located
                      under the input settings (InputTimecodeSource), to specify how the service
                      counts input video frames. This input frame count affects only the behavior of
                      features that apply to a single input at a time, such as input clipping and
                      synchronizing some captions formats. Choose Embedded (EMBEDDED) to use the
                      timecodes in your input video. Choose Start at zero (ZEROBASED) to start the
                      first frame at zero. Choose Specified start (SPECIFIEDSTART) to start the
                      first frame at the timecode that you specify in the setting Start timecode
                      (timecodeStart). If you don't specify a value for Timecode source, the service
                      will use Embedded by default. For more information about timecodes, see
                      https://docs.aws.amazon.com/console/mediaconvert/timecode.

                      - **TimecodeStart** *(string) --* Specify the timecode that you want the
                      service to use for this input's initial frame. To use this setting, you must
                      set the Timecode source setting, located under the input settings
                      (InputTimecodeSource), to Specified start (SPECIFIEDSTART). For more
                      information about timecodes, see
                      https://docs.aws.amazon.com/console/mediaconvert/timecode.

                      - **VideoSelector** *(dict) --* Selector for video.

                        - **AlphaBehavior** *(string) --* Ignore this setting unless this input is a
                        QuickTime animation. Specify which part of this input MediaConvert uses for
                        your outputs. Leave this setting set to DISCARD in order to delete the alpha
                        channel and preserve the video. Use REMAP_TO_LUMA for this setting to delete
                        the video and map the alpha channel to the luma channel of your outputs.

                        - **ColorSpace** *(string) --* If your input video has accurate color space
                        metadata, or if you don't know about color space, leave this set to the
                        default value Follow (FOLLOW). The service will automatically detect your
                        input color space. If your input video has metadata indicating the wrong
                        color space, specify the accurate color space here. If your input video is
                        HDR 10 and the SMPTE ST 2086 Mastering Display Color Volume static metadata
                        isn't present in your video stream, or if that metadata is present but not
                        accurate, choose Force HDR 10 (FORCE_HDR10) here and specify correct values
                        in the input HDR 10 metadata (Hdr10Metadata) settings. For more information
                        about MediaConvert HDR jobs, see
                        https://docs.aws.amazon.com/console/mediaconvert/hdr.

                        - **ColorSpaceUsage** *(string) --* There are two sources for color
                        metadata, the input file and the job input settings Color space (ColorSpace)
                        and HDR master display information settings(Hdr10Metadata). The Color space
                        usage setting determines which takes precedence. Choose Force (FORCE) to use
                        color metadata from the input job settings. If you don't specify values for
                        those settings, the service defaults to using metadata from your input.
                        FALLBACK - Choose Fallback (FALLBACK) to use color metadata from the source
                        when it is present. If there's no color metadata in your input file, the
                        service defaults to using values you specify in the input settings.

                        - **Hdr10Metadata** *(dict) --* Use these settings to provide HDR 10
                        metadata that is missing or inaccurate in your input video. Appropriate
                        values vary depending on the input video and must be provided by a color
                        grader. The color grader generates these values during the HDR 10 mastering
                        process. The valid range for each of these settings is 0 to 50,000. Each
                        increment represents 0.00002 in CIE1931 color coordinate. Related settings -
                        When you specify these values, you must also set Color space (ColorSpace) to
                        HDR 10 (HDR10). To specify whether the the values you specify here take
                        precedence over the values in the metadata of your input file, set Color
                        space usage (ColorSpaceUsage). To specify whether color metadata is included
                        in an output, set Color metadata (ColorMetadata). For more information about
                        MediaConvert HDR jobs, see
                        https://docs.aws.amazon.com/console/mediaconvert/hdr.

                          - **BluePrimaryX** *(integer) --* HDR Master Display Information must be
                          provided by a color grader, using color grading tools. Range is 0 to
                          50,000, each increment represents 0.00002 in CIE1931 color coordinate.
                          Note that this setting is not for color correction.

                          - **BluePrimaryY** *(integer) --* HDR Master Display Information must be
                          provided by a color grader, using color grading tools. Range is 0 to
                          50,000, each increment represents 0.00002 in CIE1931 color coordinate.
                          Note that this setting is not for color correction.

                          - **GreenPrimaryX** *(integer) --* HDR Master Display Information must be
                          provided by a color grader, using color grading tools. Range is 0 to
                          50,000, each increment represents 0.00002 in CIE1931 color coordinate.
                          Note that this setting is not for color correction.

                          - **GreenPrimaryY** *(integer) --* HDR Master Display Information must be
                          provided by a color grader, using color grading tools. Range is 0 to
                          50,000, each increment represents 0.00002 in CIE1931 color coordinate.
                          Note that this setting is not for color correction.

                          - **MaxContentLightLevel** *(integer) --* Maximum light level among all
                          samples in the coded video sequence, in units of candelas per square
                          meter. This setting doesn't have a default value; you must specify a value
                          that is suitable for the content.

                          - **MaxFrameAverageLightLevel** *(integer) --* Maximum average light level
                          of any frame in the coded video sequence, in units of candelas per square
                          meter. This setting doesn't have a default value; you must specify a value
                          that is suitable for the content.

                          - **MaxLuminance** *(integer) --* Nominal maximum mastering display
                          luminance in units of of 0.0001 candelas per square meter.

                          - **MinLuminance** *(integer) --* Nominal minimum mastering display
                          luminance in units of of 0.0001 candelas per square meter

                          - **RedPrimaryX** *(integer) --* HDR Master Display Information must be
                          provided by a color grader, using color grading tools. Range is 0 to
                          50,000, each increment represents 0.00002 in CIE1931 color coordinate.
                          Note that this setting is not for color correction.

                          - **RedPrimaryY** *(integer) --* HDR Master Display Information must be
                          provided by a color grader, using color grading tools. Range is 0 to
                          50,000, each increment represents 0.00002 in CIE1931 color coordinate.
                          Note that this setting is not for color correction.

                          - **WhitePointX** *(integer) --* HDR Master Display Information must be
                          provided by a color grader, using color grading tools. Range is 0 to
                          50,000, each increment represents 0.00002 in CIE1931 color coordinate.
                          Note that this setting is not for color correction.

                          - **WhitePointY** *(integer) --* HDR Master Display Information must be
                          provided by a color grader, using color grading tools. Range is 0 to
                          50,000, each increment represents 0.00002 in CIE1931 color coordinate.
                          Note that this setting is not for color correction.

                        - **Pid** *(integer) --* Use PID (Pid) to select specific video data from an
                        input file. Specify this value as an integer; the system automatically
                        converts it to the hexidecimal value. For example, 257 selects PID 0x101. A
                        PID, or packet identifier, is an identifier for a set of data in an MPEG-2
                        transport stream container.

                        - **ProgramNumber** *(integer) --* Selects a specific program from within a
                        multi-program transport stream. Note that Quad 4K is not currently
                        supported.

                        - **Rotate** *(string) --* Use Rotate (InputRotate) to specify how the
                        service rotates your video. You can choose automatic rotation or specify a
                        rotation. You can specify a clockwise rotation of 0, 90, 180, or 270
                        degrees. If your input video container is .mov or .mp4 and your input has
                        rotation metadata, you can choose Automatic to have the service rotate your
                        video according to the rotation specified in the metadata. The rotation must
                        be within one degree of 90, 180, or 270 degrees. If the rotation metadata
                        specifies any other rotation, the service will default to no rotation. By
                        default, the service does no rotation, even if your input video has rotation
                        metadata. The service doesn't pass through rotation metadata.

                  - **MotionImageInserter** *(dict) --* Overlay motion graphics on top of your
                  video. The motion graphics that you specify here appear on all outputs in all
                  output groups.

                    - **Framerate** *(dict) --* If your motion graphic asset is a .mov file, keep
                    this setting unspecified. If your motion graphic asset is a series of .png
                    files, specify the frame rate of the overlay in frames per second, as a
                    fraction. For example, specify 24 fps as 24/1. Make sure that the number of
                    images in your series matches the frame rate and your intended overlay duration.
                    For example, if you want a 30-second overlay at 30 fps, you should have 900 .png
                    images. This overlay frame rate doesn't need to match the frame rate of the
                    underlying video.

                      - **FramerateDenominator** *(integer) --* The bottom of the fraction that
                      expresses your overlay frame rate. For example, if your frame rate is 24 fps,
                      set this value to 1.

                      - **FramerateNumerator** *(integer) --* The top of the fraction that expresses
                      your overlay frame rate. For example, if your frame rate is 24 fps, set this
                      value to 24.

                    - **Input** *(string) --* Specify the .mov file or series of .png files that you
                    want to overlay on your video. For .png files, provide the file name of the
                    first file in the series. Make sure that the names of the .png files end with
                    sequential numbers that specify the order that they are played in. For example,
                    overlay_000.png, overlay_001.png, overlay_002.png, and so on. The sequence must
                    start at zero, and each image file name must have the same number of digits. Pad
                    your initial file names with enough zeros to complete the sequence. For example,
                    if the first image is overlay_0.png, there can be only 10 images in the
                    sequence, with the last image being overlay_9.png. But if the first image is
                    overlay_00.png, there can be 100 images in the sequence.

                    - **InsertionMode** *(string) --* Choose the type of motion graphic asset that
                    you are providing for your overlay. You can choose either a .mov file or a
                    series of .png files.

                    - **Offset** *(dict) --* Use Offset to specify the placement of your motion
                    graphic overlay on the video frame. Specify in pixels, from the upper-left
                    corner of the frame. If you don't specify an offset, the service scales your
                    overlay to the full size of the frame. Otherwise, the service inserts the
                    overlay at its native resolution and scales the size up or down with any video
                    scaling.

                      - **ImageX** *(integer) --* Set the distance, in pixels, between the overlay
                      and the left edge of the video frame.

                      - **ImageY** *(integer) --* Set the distance, in pixels, between the overlay
                      and the top edge of the video frame.

                    - **Playback** *(string) --* Specify whether your motion graphic overlay repeats
                    on a loop or plays only once.

                    - **StartTime** *(string) --* Specify when the motion overlay begins. Use
                    timecode format (HH:MM:SS:FF or HH:MM:SS;FF). Make sure that the timecode you
                    provide here takes into account how you have set up your timecode configuration
                    under both job settings and input settings. The simplest way to do that is to
                    set both to start at 0. If you need to set up your job to follow timecodes
                    embedded in your source that don't start at zero, make sure that you specify a
                    start time that is after the first embedded timecode. For more information, see
                    https://docs.aws.amazon.com/mediaconvert/latest/ug/setting-up-timecode.html Find
                    job-wide and input timecode configuration settings in your JSON job settings
                    specification at settings>timecodeConfig>source and
                    settings>inputs>timecodeSource.

                  - **NielsenConfiguration** *(dict) --* Settings for your Nielsen configuration. If
                  you don't do Nielsen measurement and analytics, ignore these settings. When you
                  enable Nielsen configuration (nielsenConfiguration), MediaConvert enables PCM to
                  ID3 tagging for all outputs in the job. To enable Nielsen configuration
                  programmatically, include an instance of nielsenConfiguration in your JSON job
                  specification. Even if you don't include any children of nielsenConfiguration, you
                  still enable the setting.

                    - **BreakoutCode** *(integer) --* Nielsen has discontinued the use of breakout
                    code functionality. If you must include this property, set the value to zero.

                    - **DistributorId** *(string) --* Use Distributor ID (DistributorID) to specify
                    the distributor ID that is assigned to your organization by Neilsen.

                  - **OutputGroups** *(list) --* (OutputGroups) contains one group of settings for
                  each set of outputs that share a common package type. All unpackaged files
                  (MPEG-4, MPEG-2 TS, Quicktime, MXF, and no container) are grouped in a single
                  output group as well. Required in (OutputGroups) is a group of settings that apply
                  to the whole group. This required object depends on the value you set for (Type)
                  under (OutputGroups)>(OutputGroupSettings). Type, settings object pairs are as
                  follows. * FILE_GROUP_SETTINGS, FileGroupSettings * HLS_GROUP_SETTINGS,
                  HlsGroupSettings * DASH_ISO_GROUP_SETTINGS, DashIsoGroupSettings *
                  MS_SMOOTH_GROUP_SETTINGS, MsSmoothGroupSettings * CMAF_GROUP_SETTINGS,
                  CmafGroupSettings

                    - *(dict) --* Group of outputs

                      - **CustomName** *(string) --* Use Custom Group Name (CustomName) to specify a
                      name for the output group. This value is displayed on the console and can make
                      your job settings JSON more human-readable. It does not affect your outputs.
                      Use up to twelve characters that are either letters, numbers, spaces, or
                      underscores.

                      - **Name** *(string) --* Name of the output group

                      - **OutputGroupSettings** *(dict) --* Output Group settings, including type

                        - **CmafGroupSettings** *(dict) --* Required when you set (Type) under
                        (OutputGroups)>(OutputGroupSettings) to CMAF_GROUP_SETTINGS. Each output in
                        a CMAF Output Group may only contain a single video, audio, or caption
                        output.

                          - **AdditionalManifests** *(list) --* By default, the service creates one
                          top-level .m3u8 HLS manifest and one top -level .mpd DASH manifest for
                          each CMAF output group in your job. These default manifests reference
                          every output in the output group. To create additional top-level manifests
                          that reference a subset of the outputs in the output group, specify a list
                          of them here. For each additional manifest that you specify, the service
                          creates one HLS manifest and one DASH manifest.

                            - *(dict) --* Specify the details for each pair of HLS and DASH
                            additional manifests that you want the service to generate for this CMAF
                            output group. Each pair of manifests can reference a different subset of
                            outputs in the group.

                              - **ManifestNameModifier** *(string) --* Specify a name modifier that
                              the service adds to the name of this manifest to make it different
                              from the file names of the other main manifests in the output group.
                              For example, say that the default main manifest for your HLS group is
                              film-name.m3u8. If you enter "-no-premium" for this setting, then the
                              file name the service generates for this top-level manifest is
                              film-name-no-premium.m3u8. For HLS output groups, specify a
                              manifestNameModifier that is different from the nameModifier of the
                              output. The service uses the output name modifier to create unique
                              names for the individual variant manifests.

                              - **SelectedOutputs** *(list) --* Specify the outputs that you want
                              this additional top-level manifest to reference.

                                - *(string) --*

                          - **BaseUrl** *(string) --* A partial URI prefix that will be put in the
                          manifest file at the top level BaseURL element. Can be used if streams are
                          delivered from a different URL than the manifest file.

                          - **ClientCache** *(string) --* When set to ENABLED, sets
                          #EXT-X-ALLOW-CACHE:no tag, which prevents client from saving media
                          segments for later replay.

                          - **CodecSpecification** *(string) --* Specification to use (RFC-6381 or
                          the default RFC-4281) during m3u8 playlist generation.

                          - **Destination** *(string) --* Use Destination (Destination) to specify
                          the S3 output location and the output filename base. Destination accepts
                          format identifiers. If you do not specify the base filename in the URI,
                          the service will use the filename of the input file. If your job has
                          multiple inputs, the service uses the filename of the first input file.

                          - **DestinationSettings** *(dict) --* Settings associated with the
                          destination. Will vary based on the type of destination

                            - **S3Settings** *(dict) --* Settings associated with S3 destination

                              - **AccessControl** *(dict) --* Optional. Have MediaConvert
                              automatically apply Amazon S3 access control for the outputs in this
                              output group. When you don't use this setting, S3 automatically
                              applies the default access control list PRIVATE.

                                - **CannedAcl** *(string) --* Choose an Amazon S3 canned ACL for
                                MediaConvert to apply to this output.

                              - **Encryption** *(dict) --* Settings for how your job outputs are
                              encrypted as they are uploaded to Amazon S3.

                                - **EncryptionType** *(string) --* Specify how you want your data
                                keys managed. AWS uses data keys to encrypt your content. AWS also
                                encrypts the data keys themselves, using a customer master key
                                (CMK), and then stores the encrypted data keys alongside your
                                encrypted content. Use this setting to specify which AWS service
                                manages the CMK. For simplest set up, choose Amazon S3
                                (SERVER_SIDE_ENCRYPTION_S3). If you want your master key to be
                                managed by AWS Key Management Service (KMS), choose AWS KMS
                                (SERVER_SIDE_ENCRYPTION_KMS). By default, when you choose AWS KMS,
                                KMS uses the AWS managed customer master key (CMK) associated with
                                Amazon S3 to encrypt your data keys. You can optionally choose to
                                specify a different, customer managed CMK. Do so by specifying the
                                Amazon Resource Name (ARN) of the key for the setting KMS ARN
                                (kmsKeyArn).

                                - **KmsKeyArn** *(string) --* Optionally, specify the customer
                                master key (CMK) that you want to use to encrypt the data key that
                                AWS uses to encrypt your output content. Enter the Amazon Resource
                                Name (ARN) of the CMK. To use this setting, you must also set
                                Server-side encryption (S3ServerSideEncryptionType) to AWS KMS
                                (SERVER_SIDE_ENCRYPTION_KMS). If you set Server-side encryption to
                                AWS KMS but don't specify a CMK here, AWS uses the AWS managed CMK
                                associated with Amazon S3.

                          - **Encryption** *(dict) --* DRM settings.

                            - **ConstantInitializationVector** *(string) --* This is a 128-bit,
                            16-byte hex value represented by a 32-character text string. If this
                            parameter is not set then the Initialization Vector will follow the
                            segment number by default.

                            - **EncryptionMethod** *(string) --* Specify the encryption scheme that
                            you want the service to use when encrypting your CMAF segments. Choose
                            AES-CBC subsample (SAMPLE-AES) or AES_CTR (AES-CTR).

                            - **InitializationVectorInManifest** *(string) --* When you use DRM with
                            CMAF outputs, choose whether the service writes the 128-bit encryption
                            initialization vector in the HLS and DASH manifests.

                            - **SpekeKeyProvider** *(dict) --* If your output group type is CMAF,
                            use these settings when doing DRM encryption with a SPEKE-compliant key
                            provider. If your output group type is HLS, DASH, or Microsoft Smooth,
                            use the SpekeKeyProvider settings instead.

                              - **CertificateArn** *(string) --* If you want your key provider to
                              encrypt the content keys that it provides to MediaConvert, set up a
                              certificate with a master key using AWS Certificate Manager. Specify
                              the certificate's Amazon Resource Name (ARN) here.

                              - **DashSignaledSystemIds** *(list) --* Specify the DRM system IDs
                              that you want signaled in the DASH manifest that MediaConvert creates
                              as part of this CMAF package. The DASH manifest can currently signal
                              up to three system IDs. For more information, see
                              https://dashif.org/identifiers/content_protection/.

                                - *(string) --*

                              - **HlsSignaledSystemIds** *(list) --* Specify the DRM system ID that
                              you want signaled in the HLS manifest that MediaConvert creates as
                              part of this CMAF package. The HLS manifest can currently signal only
                              one system ID. For more information, see
                              https://dashif.org/identifiers/content_protection/.

                                - *(string) --*

                              - **ResourceId** *(string) --* Specify the resource ID that your
                              SPEKE-compliant key provider uses to identify this content.

                              - **Url** *(string) --* Specify the URL to the key server that your
                              SPEKE-compliant DRM key provider uses to provide keys for encrypting
                              your content.

                            - **StaticKeyProvider** *(dict) --* Use these settings to set up
                            encryption with a static key provider.

                              - **KeyFormat** *(string) --* Relates to DRM implementation. Sets the
                              value of the KEYFORMAT attribute. Must be 'identity' or a reverse DNS
                              string. May be omitted to indicate an implicit value of 'identity'.

                              - **KeyFormatVersions** *(string) --* Relates to DRM implementation.
                              Either a single positive integer version value or a slash delimited
                              list of version values (1/2/3).

                              - **StaticKeyValue** *(string) --* Relates to DRM implementation. Use
                              a 32-character hexidecimal string to specify Key Value
                              (StaticKeyValue).

                              - **Url** *(string) --* Relates to DRM implementation. The location of
                              the license server used for protecting content.

                            - **Type** *(string) --* Specify whether your DRM encryption key is
                            static or from a key provider that follows the SPEKE standard. For more
                            information about SPEKE, see
                            https://docs.aws.amazon.com/speke/latest/documentation/what-is-speke.html.

                          - **FragmentLength** *(integer) --* Length of fragments to generate (in
                          seconds). Fragment length must be compatible with GOP size and Framerate.
                          Note that fragments will end on the next keyframe after this number of
                          seconds, so actual fragment length may be longer. When Emit Single File is
                          checked, the fragmentation is internal to a single output file and it does
                          not cause the creation of many output files as in other output types.

                          - **ManifestCompression** *(string) --* When set to GZIP, compresses HLS
                          playlist.

                          - **ManifestDurationFormat** *(string) --* Indicates whether the output
                          manifest should use floating point values for segment duration.

                          - **MinBufferTime** *(integer) --* Minimum time of initially buffered
                          media that is needed to ensure smooth playout.

                          - **MinFinalSegmentLength** *(float) --* Keep this setting at the default
                          value of 0, unless you are troubleshooting a problem with how devices play
                          back the end of your video asset. If you know that player devices are
                          hanging on the final segment of your video because the length of your
                          final segment is too short, use this setting to specify a minimum final
                          segment length, in seconds. Choose a value that is greater than or equal
                          to 1 and less than your segment length. When you specify a value for this
                          setting, the encoder will combine any final segment that is shorter than
                          the length that you specify with the previous segment. For example, your
                          segment length is 3 seconds and your final segment is .5 seconds without a
                          minimum final segment length; when you set the minimum final segment
                          length to 1, your final segment is 3.5 seconds.

                          - **MpdProfile** *(string) --* Specify whether your DASH profile is
                          on-demand or main. When you choose Main profile (MAIN_PROFILE), the
                          service signals urn:mpeg:dash:profile:isoff-main:2011 in your .mpd DASH
                          manifest. When you choose On-demand (ON_DEMAND_PROFILE), the service
                          signals urn:mpeg:dash:profile:isoff-on-demand:2011 in your .mpd. When you
                          choose On-demand, you must also set the output group setting Segment
                          control (SegmentControl) to Single file (SINGLE_FILE).

                          - **SegmentControl** *(string) --* When set to SINGLE_FILE, a single
                          output file is generated, which is internally segmented using the Fragment
                          Length and Segment Length. When set to SEGMENTED_FILES, separate segment
                          files will be created.

                          - **SegmentLength** *(integer) --* Use this setting to specify the length,
                          in seconds, of each individual CMAF segment. This value applies to the
                          whole package; that is, to every output in the output group. Note that
                          segments end on the first keyframe after this number of seconds, so the
                          actual segment length might be slightly longer. If you set Segment control
                          (CmafSegmentControl) to single file, the service puts the content of each
                          output in a single file that has metadata that marks these segments. If
                          you set it to segmented files, the service creates multiple files for each
                          output, each with the content of one segment.

                          - **StreamInfResolution** *(string) --* Include or exclude RESOLUTION
                          attribute for video in EXT-X-STREAM-INF tag of variant manifest.

                          - **WriteDashManifest** *(string) --* When set to ENABLED, a DASH MPD
                          manifest will be generated for this output.

                          - **WriteHlsManifest** *(string) --* When set to ENABLED, an Apple HLS
                          manifest will be generated for this output.

                        - **DashIsoGroupSettings** *(dict) --* Required when you set (Type) under
                        (OutputGroups)>(OutputGroupSettings) to DASH_ISO_GROUP_SETTINGS.

                          - **AdditionalManifests** *(list) --* By default, the service creates one
                          .mpd DASH manifest for each DASH ISO output group in your job. This
                          default manifest references every output in the output group. To create
                          additional DASH manifests that reference a subset of the outputs in the
                          output group, specify a list of them here.

                            - *(dict) --* Specify the details for each additional DASH manifest that
                            you want the service to generate for this output group. Each manifest
                            can reference a different subset of outputs in the group.

                              - **ManifestNameModifier** *(string) --* Specify a name modifier that
                              the service adds to the name of this manifest to make it different
                              from the file names of the other main manifests in the output group.
                              For example, say that the default main manifest for your DASH group is
                              film-name.mpd. If you enter "-no-premium" for this setting, then the
                              file name the service generates for this top-level manifest is
                              film-name-no-premium.mpd.

                              - **SelectedOutputs** *(list) --* Specify the outputs that you want
                              this additional top-level manifest to reference.

                                - *(string) --*

                          - **BaseUrl** *(string) --* A partial URI prefix that will be put in the
                          manifest (.mpd) file at the top level BaseURL element. Can be used if
                          streams are delivered from a different URL than the manifest file.

                          - **Destination** *(string) --* Use Destination (Destination) to specify
                          the S3 output location and the output filename base. Destination accepts
                          format identifiers. If you do not specify the base filename in the URI,
                          the service will use the filename of the input file. If your job has
                          multiple inputs, the service uses the filename of the first input file.

                          - **DestinationSettings** *(dict) --* Settings associated with the
                          destination. Will vary based on the type of destination

                            - **S3Settings** *(dict) --* Settings associated with S3 destination

                              - **AccessControl** *(dict) --* Optional. Have MediaConvert
                              automatically apply Amazon S3 access control for the outputs in this
                              output group. When you don't use this setting, S3 automatically
                              applies the default access control list PRIVATE.

                                - **CannedAcl** *(string) --* Choose an Amazon S3 canned ACL for
                                MediaConvert to apply to this output.

                              - **Encryption** *(dict) --* Settings for how your job outputs are
                              encrypted as they are uploaded to Amazon S3.

                                - **EncryptionType** *(string) --* Specify how you want your data
                                keys managed. AWS uses data keys to encrypt your content. AWS also
                                encrypts the data keys themselves, using a customer master key
                                (CMK), and then stores the encrypted data keys alongside your
                                encrypted content. Use this setting to specify which AWS service
                                manages the CMK. For simplest set up, choose Amazon S3
                                (SERVER_SIDE_ENCRYPTION_S3). If you want your master key to be
                                managed by AWS Key Management Service (KMS), choose AWS KMS
                                (SERVER_SIDE_ENCRYPTION_KMS). By default, when you choose AWS KMS,
                                KMS uses the AWS managed customer master key (CMK) associated with
                                Amazon S3 to encrypt your data keys. You can optionally choose to
                                specify a different, customer managed CMK. Do so by specifying the
                                Amazon Resource Name (ARN) of the key for the setting KMS ARN
                                (kmsKeyArn).

                                - **KmsKeyArn** *(string) --* Optionally, specify the customer
                                master key (CMK) that you want to use to encrypt the data key that
                                AWS uses to encrypt your output content. Enter the Amazon Resource
                                Name (ARN) of the CMK. To use this setting, you must also set
                                Server-side encryption (S3ServerSideEncryptionType) to AWS KMS
                                (SERVER_SIDE_ENCRYPTION_KMS). If you set Server-side encryption to
                                AWS KMS but don't specify a CMK here, AWS uses the AWS managed CMK
                                associated with Amazon S3.

                          - **Encryption** *(dict) --* DRM settings.

                            - **PlaybackDeviceCompatibility** *(string) --* This setting can improve
                            the compatibility of your output with video players on obsolete devices.
                            It applies only to DASH H.264 outputs with DRM encryption. Choose
                            Unencrypted SEI (UNENCRYPTED_SEI) only to correct problems with playback
                            on older devices. Otherwise, keep the default setting CENC v1 (CENC_V1).
                            If you choose Unencrypted SEI, for that output, the service will exclude
                            the access unit delimiter and will leave the SEI NAL units unencrypted.

                            - **SpekeKeyProvider** *(dict) --* If your output group type is HLS,
                            DASH, or Microsoft Smooth, use these settings when doing DRM encryption
                            with a SPEKE-compliant key provider. If your output group type is CMAF,
                            use the SpekeKeyProviderCmaf settings instead.

                              - **CertificateArn** *(string) --* If you want your key provider to
                              encrypt the content keys that it provides to MediaConvert, set up a
                              certificate with a master key using AWS Certificate Manager. Specify
                              the certificate's Amazon Resource Name (ARN) here.

                              - **ResourceId** *(string) --* Specify the resource ID that your
                              SPEKE-compliant key provider uses to identify this content.

                              - **SystemIds** *(list) --* Relates to SPEKE implementation. DRM
                              system identifiers. DASH output groups support a max of two system
                              ids. Other group types support one system id. See
                              https://dashif.org/identifiers/content_protection/ for more details.

                                - *(string) --*

                              - **Url** *(string) --* Specify the URL to the key server that your
                              SPEKE-compliant DRM key provider uses to provide keys for encrypting
                              your content.

                          - **FragmentLength** *(integer) --* Length of fragments to generate (in
                          seconds). Fragment length must be compatible with GOP size and Framerate.
                          Note that fragments will end on the next keyframe after this number of
                          seconds, so actual fragment length may be longer. When Emit Single File is
                          checked, the fragmentation is internal to a single output file and it does
                          not cause the creation of many output files as in other output types.

                          - **HbbtvCompliance** *(string) --* Supports HbbTV specification as
                          indicated

                          - **MinBufferTime** *(integer) --* Minimum time of initially buffered
                          media that is needed to ensure smooth playout.

                          - **MpdProfile** *(string) --* Specify whether your DASH profile is
                          on-demand or main. When you choose Main profile (MAIN_PROFILE), the
                          service signals urn:mpeg:dash:profile:isoff-main:2011 in your .mpd DASH
                          manifest. When you choose On-demand (ON_DEMAND_PROFILE), the service
                          signals urn:mpeg:dash:profile:isoff-on-demand:2011 in your .mpd. When you
                          choose On-demand, you must also set the output group setting Segment
                          control (SegmentControl) to Single file (SINGLE_FILE).

                          - **SegmentControl** *(string) --* When set to SINGLE_FILE, a single
                          output file is generated, which is internally segmented using the Fragment
                          Length and Segment Length. When set to SEGMENTED_FILES, separate segment
                          files will be created.

                          - **SegmentLength** *(integer) --* Length of mpd segments to create (in
                          seconds). Note that segments will end on the next keyframe after this
                          number of seconds, so actual segment length may be longer. When Emit
                          Single File is checked, the segmentation is internal to a single output
                          file and it does not cause the creation of many output files as in other
                          output types.

                          - **WriteSegmentTimelineInRepresentation** *(string) --* If you get an
                          HTTP error in the 400 range when you play back your DASH output, enable
                          this setting and run your transcoding job again. When you enable this
                          setting, the service writes precise segment durations in the DASH
                          manifest. The segment duration information appears inside the
                          SegmentTimeline element, inside SegmentTemplate at the Representation
                          level. When you don't enable this setting, the service writes approximate
                          segment durations in your DASH manifest.

                        - **FileGroupSettings** *(dict) --* Required when you set (Type) under
                        (OutputGroups)>(OutputGroupSettings) to FILE_GROUP_SETTINGS.

                          - **Destination** *(string) --* Use Destination (Destination) to specify
                          the S3 output location and the output filename base. Destination accepts
                          format identifiers. If you do not specify the base filename in the URI,
                          the service will use the filename of the input file. If your job has
                          multiple inputs, the service uses the filename of the first input file.

                          - **DestinationSettings** *(dict) --* Settings associated with the
                          destination. Will vary based on the type of destination

                            - **S3Settings** *(dict) --* Settings associated with S3 destination

                              - **AccessControl** *(dict) --* Optional. Have MediaConvert
                              automatically apply Amazon S3 access control for the outputs in this
                              output group. When you don't use this setting, S3 automatically
                              applies the default access control list PRIVATE.

                                - **CannedAcl** *(string) --* Choose an Amazon S3 canned ACL for
                                MediaConvert to apply to this output.

                              - **Encryption** *(dict) --* Settings for how your job outputs are
                              encrypted as they are uploaded to Amazon S3.

                                - **EncryptionType** *(string) --* Specify how you want your data
                                keys managed. AWS uses data keys to encrypt your content. AWS also
                                encrypts the data keys themselves, using a customer master key
                                (CMK), and then stores the encrypted data keys alongside your
                                encrypted content. Use this setting to specify which AWS service
                                manages the CMK. For simplest set up, choose Amazon S3
                                (SERVER_SIDE_ENCRYPTION_S3). If you want your master key to be
                                managed by AWS Key Management Service (KMS), choose AWS KMS
                                (SERVER_SIDE_ENCRYPTION_KMS). By default, when you choose AWS KMS,
                                KMS uses the AWS managed customer master key (CMK) associated with
                                Amazon S3 to encrypt your data keys. You can optionally choose to
                                specify a different, customer managed CMK. Do so by specifying the
                                Amazon Resource Name (ARN) of the key for the setting KMS ARN
                                (kmsKeyArn).

                                - **KmsKeyArn** *(string) --* Optionally, specify the customer
                                master key (CMK) that you want to use to encrypt the data key that
                                AWS uses to encrypt your output content. Enter the Amazon Resource
                                Name (ARN) of the CMK. To use this setting, you must also set
                                Server-side encryption (S3ServerSideEncryptionType) to AWS KMS
                                (SERVER_SIDE_ENCRYPTION_KMS). If you set Server-side encryption to
                                AWS KMS but don't specify a CMK here, AWS uses the AWS managed CMK
                                associated with Amazon S3.

                        - **HlsGroupSettings** *(dict) --* Required when you set (Type) under
                        (OutputGroups)>(OutputGroupSettings) to HLS_GROUP_SETTINGS.

                          - **AdMarkers** *(list) --* Choose one or more ad marker types to decorate
                          your Apple HLS manifest. This setting does not determine whether SCTE-35
                          markers appear in the outputs themselves.

                            - *(string) --*

                          - **AdditionalManifests** *(list) --* By default, the service creates one
                          top-level .m3u8 HLS manifest for each HLS output group in your job. This
                          default manifest references every output in the output group. To create
                          additional top-level manifests that reference a subset of the outputs in
                          the output group, specify a list of them here.

                            - *(dict) --* Specify the details for each additional HLS manifest that
                            you want the service to generate for this output group. Each manifest
                            can reference a different subset of outputs in the group.

                              - **ManifestNameModifier** *(string) --* Specify a name modifier that
                              the service adds to the name of this manifest to make it different
                              from the file names of the other main manifests in the output group.
                              For example, say that the default main manifest for your HLS group is
                              film-name.m3u8. If you enter "-no-premium" for this setting, then the
                              file name the service generates for this top-level manifest is
                              film-name-no-premium.m3u8. For HLS output groups, specify a
                              manifestNameModifier that is different from the nameModifier of the
                              output. The service uses the output name modifier to create unique
                              names for the individual variant manifests.

                              - **SelectedOutputs** *(list) --* Specify the outputs that you want
                              this additional top-level manifest to reference.

                                - *(string) --*

                          - **BaseUrl** *(string) --* A partial URI prefix that will be prepended to
                          each output in the media .m3u8 file. Can be used if base manifest is
                          delivered from a different URL than the main .m3u8 file.

                          - **CaptionLanguageMappings** *(list) --* Language to be used on Caption
                          outputs

                            - *(dict) --* Caption Language Mapping

                              - **CaptionChannel** *(integer) --* Caption channel.

                              - **CustomLanguageCode** *(string) --* Specify the language for this
                              captions channel, using the ISO 639-2 or ISO 639-3 three-letter
                              language code

                              - **LanguageCode** *(string) --* Specify the language, using the ISO
                              639-2 three-letter code listed at
                              https://www.loc.gov/standards/iso639-2/php/code_list.php.

                              - **LanguageDescription** *(string) --* Caption language description.

                          - **CaptionLanguageSetting** *(string) --* Applies only to 608 Embedded
                          output captions. Insert: Include CLOSED-CAPTIONS lines in the manifest.
                          Specify at least one language in the CC1 Language Code field. One
                          CLOSED-CAPTION line is added for each Language Code you specify. Make sure
                          to specify the languages in the order in which they appear in the original
                          source (if the source is embedded format) or the order of the caption
                          selectors (if the source is other than embedded). Otherwise, languages in
                          the manifest will not match up properly with the output captions. None:
                          Include CLOSED-CAPTIONS=
                              NONE line in the manifest. Omit: Omit any
                          CLOSED-CAPTIONS line from the manifest.

                          - **ClientCache** *(string) --* When set to ENABLED, sets
                          #EXT-X-ALLOW-CACHE:no tag, which prevents client from saving media
                          segments for later replay.

                          - **CodecSpecification** *(string) --* Specification to use (RFC-6381 or
                          the default RFC-4281) during m3u8 playlist generation.

                          - **Destination** *(string) --* Use Destination (Destination) to specify
                          the S3 output location and the output filename base. Destination accepts
                          format identifiers. If you do not specify the base filename in the URI,
                          the service will use the filename of the input file. If your job has
                          multiple inputs, the service uses the filename of the first input file.

                          - **DestinationSettings** *(dict) --* Settings associated with the
                          destination. Will vary based on the type of destination

                            - **S3Settings** *(dict) --* Settings associated with S3 destination

                              - **AccessControl** *(dict) --* Optional. Have MediaConvert
                              automatically apply Amazon S3 access control for the outputs in this
                              output group. When you don't use this setting, S3 automatically
                              applies the default access control list PRIVATE.

                                - **CannedAcl** *(string) --* Choose an Amazon S3 canned ACL for
                                MediaConvert to apply to this output.

                              - **Encryption** *(dict) --* Settings for how your job outputs are
                              encrypted as they are uploaded to Amazon S3.

                                - **EncryptionType** *(string) --* Specify how you want your data
                                keys managed. AWS uses data keys to encrypt your content. AWS also
                                encrypts the data keys themselves, using a customer master key
                                (CMK), and then stores the encrypted data keys alongside your
                                encrypted content. Use this setting to specify which AWS service
                                manages the CMK. For simplest set up, choose Amazon S3
                                (SERVER_SIDE_ENCRYPTION_S3). If you want your master key to be
                                managed by AWS Key Management Service (KMS), choose AWS KMS
                                (SERVER_SIDE_ENCRYPTION_KMS). By default, when you choose AWS KMS,
                                KMS uses the AWS managed customer master key (CMK) associated with
                                Amazon S3 to encrypt your data keys. You can optionally choose to
                                specify a different, customer managed CMK. Do so by specifying the
                                Amazon Resource Name (ARN) of the key for the setting KMS ARN
                                (kmsKeyArn).

                                - **KmsKeyArn** *(string) --* Optionally, specify the customer
                                master key (CMK) that you want to use to encrypt the data key that
                                AWS uses to encrypt your output content. Enter the Amazon Resource
                                Name (ARN) of the CMK. To use this setting, you must also set
                                Server-side encryption (S3ServerSideEncryptionType) to AWS KMS
                                (SERVER_SIDE_ENCRYPTION_KMS). If you set Server-side encryption to
                                AWS KMS but don't specify a CMK here, AWS uses the AWS managed CMK
                                associated with Amazon S3.

                          - **DirectoryStructure** *(string) --* Indicates whether segments should
                          be placed in subdirectories.

                          - **Encryption** *(dict) --* DRM settings.

                            - **ConstantInitializationVector** *(string) --* This is a 128-bit,
                            16-byte hex value represented by a 32-character text string. If this
                            parameter is not set then the Initialization Vector will follow the
                            segment number by default.

                            - **EncryptionMethod** *(string) --* Encrypts the segments with the
                            given encryption scheme. Leave blank to disable. Selecting 'Disabled' in
                            the web interface also disables encryption.

                            - **InitializationVectorInManifest** *(string) --* The Initialization
                            Vector is a 128-bit number used in conjunction with the key for
                            encrypting blocks. If set to INCLUDE, Initialization Vector is listed in
                            the manifest. Otherwise Initialization Vector is not in the manifest.

                            - **OfflineEncrypted** *(string) --* Enable this setting to insert the
                            EXT-X-SESSION-KEY element into the master playlist. This allows for
                            offline Apple HLS FairPlay content protection.

                            - **SpekeKeyProvider** *(dict) --* If your output group type is HLS,
                            DASH, or Microsoft Smooth, use these settings when doing DRM encryption
                            with a SPEKE-compliant key provider. If your output group type is CMAF,
                            use the SpekeKeyProviderCmaf settings instead.

                              - **CertificateArn** *(string) --* If you want your key provider to
                              encrypt the content keys that it provides to MediaConvert, set up a
                              certificate with a master key using AWS Certificate Manager. Specify
                              the certificate's Amazon Resource Name (ARN) here.

                              - **ResourceId** *(string) --* Specify the resource ID that your
                              SPEKE-compliant key provider uses to identify this content.

                              - **SystemIds** *(list) --* Relates to SPEKE implementation. DRM
                              system identifiers. DASH output groups support a max of two system
                              ids. Other group types support one system id. See
                              https://dashif.org/identifiers/content_protection/ for more details.

                                - *(string) --*

                              - **Url** *(string) --* Specify the URL to the key server that your
                              SPEKE-compliant DRM key provider uses to provide keys for encrypting
                              your content.

                            - **StaticKeyProvider** *(dict) --* Use these settings to set up
                            encryption with a static key provider.

                              - **KeyFormat** *(string) --* Relates to DRM implementation. Sets the
                              value of the KEYFORMAT attribute. Must be 'identity' or a reverse DNS
                              string. May be omitted to indicate an implicit value of 'identity'.

                              - **KeyFormatVersions** *(string) --* Relates to DRM implementation.
                              Either a single positive integer version value or a slash delimited
                              list of version values (1/2/3).

                              - **StaticKeyValue** *(string) --* Relates to DRM implementation. Use
                              a 32-character hexidecimal string to specify Key Value
                              (StaticKeyValue).

                              - **Url** *(string) --* Relates to DRM implementation. The location of
                              the license server used for protecting content.

                            - **Type** *(string) --* Specify whether your DRM encryption key is
                            static or from a key provider that follows the SPEKE standard. For more
                            information about SPEKE, see
                            https://docs.aws.amazon.com/speke/latest/documentation/what-is-speke.html.

                          - **ManifestCompression** *(string) --* When set to GZIP, compresses HLS
                          playlist.

                          - **ManifestDurationFormat** *(string) --* Indicates whether the output
                          manifest should use floating point values for segment duration.

                          - **MinFinalSegmentLength** *(float) --* Keep this setting at the default
                          value of 0, unless you are troubleshooting a problem with how devices play
                          back the end of your video asset. If you know that player devices are
                          hanging on the final segment of your video because the length of your
                          final segment is too short, use this setting to specify a minimum final
                          segment length, in seconds. Choose a value that is greater than or equal
                          to 1 and less than your segment length. When you specify a value for this
                          setting, the encoder will combine any final segment that is shorter than
                          the length that you specify with the previous segment. For example, your
                          segment length is 3 seconds and your final segment is .5 seconds without a
                          minimum final segment length; when you set the minimum final segment
                          length to 1, your final segment is 3.5 seconds.

                          - **MinSegmentLength** *(integer) --* When set, Minimum Segment Size is
                          enforced by looking ahead and back within the specified range for a nearby
                          avail and extending the segment size if needed.

                          - **OutputSelection** *(string) --* Indicates whether the .m3u8 manifest
                          file should be generated for this HLS output group.

                          - **ProgramDateTime** *(string) --* Includes or excludes
                          EXT-X-PROGRAM-DATE-TIME tag in .m3u8 manifest files. The value is
                          calculated as follows: either the program date and time are initialized
                          using the input timecode source, or the time is initialized using the
                          input timecode source and the date is initialized using the
                          timestamp_offset.

                          - **ProgramDateTimePeriod** *(integer) --* Period of insertion of
                          EXT-X-PROGRAM-DATE-TIME entry, in seconds.

                          - **SegmentControl** *(string) --* When set to SINGLE_FILE, emits program
                          as a single media resource (.ts) file, uses #EXT-X-BYTERANGE tags to index
                          segment for playback.

                          - **SegmentLength** *(integer) --* Length of MPEG-2 Transport Stream
                          segments to create (in seconds). Note that segments will end on the next
                          keyframe after this number of seconds, so actual segment length may be
                          longer.

                          - **SegmentsPerSubdirectory** *(integer) --* Number of segments to write
                          to a subdirectory before starting a new one. directoryStructure must be
                          SINGLE_DIRECTORY for this setting to have an effect.

                          - **StreamInfResolution** *(string) --* Include or exclude RESOLUTION
                          attribute for video in EXT-X-STREAM-INF tag of variant manifest.

                          - **TimedMetadataId3Frame** *(string) --* Indicates ID3 frame that has the
                          timecode.

                          - **TimedMetadataId3Period** *(integer) --* Timed Metadata interval in
                          seconds.

                          - **TimestampDeltaMilliseconds** *(integer) --* Provides an extra
                          millisecond delta offset to fine tune the timestamps.

                        - **MsSmoothGroupSettings** *(dict) --* Required when you set (Type) under
                        (OutputGroups)>(OutputGroupSettings) to MS_SMOOTH_GROUP_SETTINGS.

                          - **AdditionalManifests** *(list) --* By default, the service creates one
                          .ism Microsoft Smooth Streaming manifest for each Microsoft Smooth
                          Streaming output group in your job. This default manifest references every
                          output in the output group. To create additional manifests that reference
                          a subset of the outputs in the output group, specify a list of them here.

                            - *(dict) --* Specify the details for each additional Microsoft Smooth
                            Streaming manifest that you want the service to generate for this output
                            group. Each manifest can reference a different subset of outputs in the
                            group.

                              - **ManifestNameModifier** *(string) --* Specify a name modifier that
                              the service adds to the name of this manifest to make it different
                              from the file names of the other main manifests in the output group.
                              For example, say that the default main manifest for your Microsoft
                              Smooth group is film-name.ismv. If you enter "-no-premium" for this
                              setting, then the file name the service generates for this top-level
                              manifest is film-name-no-premium.ismv.

                              - **SelectedOutputs** *(list) --* Specify the outputs that you want
                              this additional top-level manifest to reference.

                                - *(string) --*

                          - **AudioDeduplication** *(string) --* COMBINE_DUPLICATE_STREAMS combines
                          identical audio encoding settings across a Microsoft Smooth output group
                          into a single audio stream.

                          - **Destination** *(string) --* Use Destination (Destination) to specify
                          the S3 output location and the output filename base. Destination accepts
                          format identifiers. If you do not specify the base filename in the URI,
                          the service will use the filename of the input file. If your job has
                          multiple inputs, the service uses the filename of the first input file.

                          - **DestinationSettings** *(dict) --* Settings associated with the
                          destination. Will vary based on the type of destination

                            - **S3Settings** *(dict) --* Settings associated with S3 destination

                              - **AccessControl** *(dict) --* Optional. Have MediaConvert
                              automatically apply Amazon S3 access control for the outputs in this
                              output group. When you don't use this setting, S3 automatically
                              applies the default access control list PRIVATE.

                                - **CannedAcl** *(string) --* Choose an Amazon S3 canned ACL for
                                MediaConvert to apply to this output.

                              - **Encryption** *(dict) --* Settings for how your job outputs are
                              encrypted as they are uploaded to Amazon S3.

                                - **EncryptionType** *(string) --* Specify how you want your data
                                keys managed. AWS uses data keys to encrypt your content. AWS also
                                encrypts the data keys themselves, using a customer master key
                                (CMK), and then stores the encrypted data keys alongside your
                                encrypted content. Use this setting to specify which AWS service
                                manages the CMK. For simplest set up, choose Amazon S3
                                (SERVER_SIDE_ENCRYPTION_S3). If you want your master key to be
                                managed by AWS Key Management Service (KMS), choose AWS KMS
                                (SERVER_SIDE_ENCRYPTION_KMS). By default, when you choose AWS KMS,
                                KMS uses the AWS managed customer master key (CMK) associated with
                                Amazon S3 to encrypt your data keys. You can optionally choose to
                                specify a different, customer managed CMK. Do so by specifying the
                                Amazon Resource Name (ARN) of the key for the setting KMS ARN
                                (kmsKeyArn).

                                - **KmsKeyArn** *(string) --* Optionally, specify the customer
                                master key (CMK) that you want to use to encrypt the data key that
                                AWS uses to encrypt your output content. Enter the Amazon Resource
                                Name (ARN) of the CMK. To use this setting, you must also set
                                Server-side encryption (S3ServerSideEncryptionType) to AWS KMS
                                (SERVER_SIDE_ENCRYPTION_KMS). If you set Server-side encryption to
                                AWS KMS but don't specify a CMK here, AWS uses the AWS managed CMK
                                associated with Amazon S3.

                          - **Encryption** *(dict) --* If you are using DRM, set DRM System
                          (MsSmoothEncryptionSettings) to specify the value SpekeKeyProvider.

                            - **SpekeKeyProvider** *(dict) --* If your output group type is HLS,
                            DASH, or Microsoft Smooth, use these settings when doing DRM encryption
                            with a SPEKE-compliant key provider. If your output group type is CMAF,
                            use the SpekeKeyProviderCmaf settings instead.

                              - **CertificateArn** *(string) --* If you want your key provider to
                              encrypt the content keys that it provides to MediaConvert, set up a
                              certificate with a master key using AWS Certificate Manager. Specify
                              the certificate's Amazon Resource Name (ARN) here.

                              - **ResourceId** *(string) --* Specify the resource ID that your
                              SPEKE-compliant key provider uses to identify this content.

                              - **SystemIds** *(list) --* Relates to SPEKE implementation. DRM
                              system identifiers. DASH output groups support a max of two system
                              ids. Other group types support one system id. See
                              https://dashif.org/identifiers/content_protection/ for more details.

                                - *(string) --*

                              - **Url** *(string) --* Specify the URL to the key server that your
                              SPEKE-compliant DRM key provider uses to provide keys for encrypting
                              your content.

                          - **FragmentLength** *(integer) --* Use Fragment length (FragmentLength)
                          to specify the mp4 fragment sizes in seconds. Fragment length must be
                          compatible with GOP size and frame rate.

                          - **ManifestEncoding** *(string) --* Use Manifest encoding
                          (MsSmoothManifestEncoding) to specify the encoding format for the server
                          and client manifest. Valid options are utf8 and utf16.

                        - **Type** *(string) --* Type of output group (File group, Apple HLS, DASH
                        ISO, Microsoft Smooth Streaming, CMAF)

                      - **Outputs** *(list) --* This object holds groups of encoding settings, one
                      group of settings per output.

                        - *(dict) --* An output object describes the settings for a single output
                        file or stream in an output group.

                          - **AudioDescriptions** *(list) --* (AudioDescriptions) contains groups of
                          audio encoding settings organized by audio codec. Include one instance of
                          (AudioDescriptions) per output. (AudioDescriptions) can contain multiple
                          groups of encoding settings.

                            - *(dict) --* Description of audio output

                              - **AudioNormalizationSettings** *(dict) --* Advanced audio
                              normalization settings. Ignore these settings unless you need to
                              comply with a loudness standard.

                                - **Algorithm** *(string) --* Choose one of the following audio
                                normalization algorithms: ITU-R BS.1770-1: Ungated loudness. A
                                measurement of ungated average loudness for an entire piece of
                                content, suitable for measurement of short-form content under ATSC
                                recommendation A/85. Supports up to 5.1 audio channels. ITU-R
                                BS.1770-2: Gated loudness. A measurement of gated average loudness
                                compliant with the requirements of EBU-R128. Supports up to 5.1
                                audio channels. ITU-R BS.1770-3: Modified peak. The same loudness
                                measurement algorithm as 1770-2, with an updated true peak
                                measurement. ITU-R BS.1770-4: Higher channel count. Allows for more
                                audio channels than the other algorithms, including configurations
                                such as 7.1.

                                - **AlgorithmControl** *(string) --* When enabled the output audio
                                is corrected using the chosen algorithm. If disabled, the audio will
                                be measured but not adjusted.

                                - **CorrectionGateLevel** *(integer) --* Content measuring above
                                this level will be corrected to the target level. Content measuring
                                below this level will not be corrected. Gating only applies when not
                                using real_time_correction.

                                - **LoudnessLogging** *(string) --* If set to LOG, log each output's
                                audio track loudness to a CSV file.

                                - **PeakCalculation** *(string) --* If set to TRUE_PEAK, calculate
                                and log the TruePeak for each output's audio track loudness.

                                - **TargetLkfs** *(float) --* When you use Audio normalization
                                (AudioNormalizationSettings), optionally use this setting to specify
                                a target loudness. If you don't specify a value here, the encoder
                                chooses a value for you, based on the algorithm that you choose for
                                Algorithm (algorithm). If you choose algorithm 1770-1, the encoder
                                will choose -24 LKFS; otherwise, the encoder will choose -23 LKFS.

                              - **AudioSourceName** *(string) --* Specifies which audio data to use
                              from each input. In the simplest case, specify an "Audio
                              Selector":#inputs-audio_selector by name based on its order within
                              each input. For example if you specify "Audio Selector 3", then the
                              third audio selector will be used from each input. If an input does
                              not have an "Audio Selector 3", then the audio selector marked as
                              "default" in that input will be used. If there is no audio selector
                              marked as "default", silence will be inserted for the duration of that
                              input. Alternatively, an "Audio Selector
                              Group":#inputs-audio_selector_group name may be specified, with
                              similar default/silence behavior. If no audio_source_name is
                              specified, then "Audio Selector 1" will be chosen automatically.

                              - **AudioType** *(integer) --* Applies only if Follow Input Audio Type
                              is unchecked (false). A number between 0 and 255. The following are
                              defined in ISO-IEC 13818-1: 0 = Undefined, 1 =
                                   Clean Effects, 2 =
                              Hearing Impaired, 3 =
                                   Visually Impaired Commentary, 4-255 =
                                        Reserved.

                              - **AudioTypeControl** *(string) --* When set to FOLLOW_INPUT, if the
                              input contains an ISO 639 audio_type, then that value is passed
                              through to the output. If the input contains no ISO 639 audio_type,
                              the value in Audio Type is included in the output. Otherwise the value
                              in Audio Type is included in the output. Note that this field and
                              audioType are both ignored if audioDescriptionBroadcasterMix is set to
                              BROADCASTER_MIXED_AD.

                              - **CodecSettings** *(dict) --* Audio codec settings (CodecSettings)
                              under (AudioDescriptions) contains the group of settings related to
                              audio encoding. The settings in this group vary depending on the value
                              that you choose for Audio codec (Codec). For each codec enum that you
                              choose, define the corresponding settings object. The following lists
                              the codec enum, settings object pairs. * AAC, AacSettings * MP2,
                              Mp2Settings * WAV, WavSettings * AIFF, AiffSettings * AC3, Ac3Settings
                              * EAC3, Eac3Settings * EAC3_ATMOS, Eac3AtmosSettings

                                - **AacSettings** *(dict) --* Required when you set (Codec) under
                                (AudioDescriptions)>(CodecSettings) to the value AAC. The service
                                accepts one of two mutually exclusive groups of AAC settings--VBR
                                and CBR. To select one of these modes, set the value of Bitrate
                                control mode (rateControlMode) to "VBR" or "CBR". In VBR mode, you
                                control the audio quality with the setting VBR quality (vbrQuality).
                                In CBR mode, you use the setting Bitrate (bitrate). Defaults and
                                valid values depend on the rate control mode.

                                  - **AudioDescriptionBroadcasterMix** *(string) --* Choose
                                  BROADCASTER_MIXED_AD when the input contains pre-mixed main audio
                                  + audio description (AD) as a stereo pair. The value for AudioType
                                  will be set to 3, which signals to downstream systems that this
                                  stream contains "broadcaster mixed AD". Note that the input
                                  received by the encoder must contain pre-mixed audio; the encoder
                                  does not perform the mixing. When you choose BROADCASTER_MIXED_AD,
                                  the encoder ignores any values you provide in AudioType and
                                  FollowInputAudioType. Choose NORMAL when the input does not
                                  contain pre-mixed audio + audio description (AD). In this case,
                                  the encoder will use any values you provide for AudioType and
                                  FollowInputAudioType.

                                  - **Bitrate** *(integer) --* Specify the average bitrate in bits
                                  per second. The set of valid values for this setting is: 6000,
                                  8000, 10000, 12000, 14000, 16000, 20000, 24000, 28000, 32000,
                                  40000, 48000, 56000, 64000, 80000, 96000, 112000, 128000, 160000,
                                  192000, 224000, 256000, 288000, 320000, 384000, 448000, 512000,
                                  576000, 640000, 768000, 896000, 1024000. The value you set is also
                                  constrained by the values that you choose for Profile
                                  (codecProfile), Bitrate control mode (codingMode), and Sample rate
                                  (sampleRate). Default values depend on Bitrate control mode and
                                  Profile.

                                  - **CodecProfile** *(string) --* AAC Profile.

                                  - **CodingMode** *(string) --* Mono (Audio Description), Mono,
                                  Stereo, or 5.1 channel layout. Valid values depend on rate control
                                  mode and profile. "1.0 - Audio Description (Receiver Mix)" setting
                                  receives a stereo description plus control track and emits a mono
                                  AAC encode of the description track, with control data emitted in
                                  the PES header as per ETSI TS 101 154 Annex E.

                                  - **RateControlMode** *(string) --* Rate Control Mode.

                                  - **RawFormat** *(string) --* Enables LATM/LOAS AAC output. Note
                                  that if you use LATM/LOAS AAC in an output, you must choose "No
                                  container" for the output container.

                                  - **SampleRate** *(integer) --* Sample rate in Hz. Valid values
                                  depend on rate control mode and profile.

                                  - **Specification** *(string) --* Use MPEG-2 AAC instead of MPEG-4
                                  AAC audio for raw or MPEG-2 Transport Stream containers.

                                  - **VbrQuality** *(string) --* VBR Quality Level - Only used if
                                  rate_control_mode is VBR.

                                - **Ac3Settings** *(dict) --* Required when you set (Codec) under
                                (AudioDescriptions)>(CodecSettings) to the value AC3.

                                  - **Bitrate** *(integer) --* Specify the average bitrate in bits
                                  per second. Valid bitrates depend on the coding mode.

                                  - **BitstreamMode** *(string) --* Specify the bitstream mode for
                                  the AC-3 stream that the encoder emits. For more information about
                                  the AC3 bitstream mode, see ATSC A/52-2012 (Annex E).

                                  - **CodingMode** *(string) --* Dolby Digital coding mode.
                                  Determines number of channels.

                                  - **Dialnorm** *(integer) --* Sets the dialnorm for the output. If
                                  blank and input audio is Dolby Digital, dialnorm will be passed
                                  through.

                                  - **DynamicRangeCompressionProfile** *(string) --* If set to
                                  FILM_STANDARD, adds dynamic range compression signaling to the
                                  output bitstream as defined in the Dolby Digital specification.

                                  - **LfeFilter** *(string) --* Applies a 120Hz lowpass filter to
                                  the LFE channel prior to encoding. Only valid with 3_2_LFE coding
                                  mode.

                                  - **MetadataControl** *(string) --* When set to FOLLOW_INPUT,
                                  encoder metadata will be sourced from the DD, DD+, or DolbyE
                                  decoder that supplied this audio data. If audio was not supplied
                                  from one of these streams, then the static metadata settings will
                                  be used.

                                  - **SampleRate** *(integer) --* This value is always 48000. It
                                  represents the sample rate in Hz.

                                - **AiffSettings** *(dict) --* Required when you set (Codec) under
                                (AudioDescriptions)>(CodecSettings) to the value AIFF.

                                  - **BitDepth** *(integer) --* Specify Bit depth (BitDepth), in
                                  bits per sample, to choose the encoding quality for this audio
                                  track.

                                  - **Channels** *(integer) --* Specify the number of channels in
                                  this output audio track. Valid values are 1 and even numbers up to
                                  64. For example, 1, 2, 4, 6, and so on, up to 64.

                                  - **SampleRate** *(integer) --* Sample rate in hz.

                                - **Codec** *(string) --* Type of Audio codec.

                                - **Eac3AtmosSettings** *(dict) --* Required when you set (Codec)
                                under (AudioDescriptions)>(CodecSettings) to the value EAC3_ATMOS.

                                  - **Bitrate** *(integer) --* Specify the average bitrate in bits
                                  per second. Valid values: 384k, 448k, 640k, 768k

                                  - **BitstreamMode** *(string) --* Specify the bitstream mode for
                                  the E-AC-3 stream that the encoder emits. For more information
                                  about the EAC3 bitstream mode, see ATSC A/52-2012 (Annex E).

                                  - **CodingMode** *(string) --* The coding mode for Dolby Digital
                                  Plus JOC (Atmos) is always 9.1.6 (CODING_MODE_9_1_6).

                                  - **DialogueIntelligence** *(string) --* Enable Dolby Dialogue
                                  Intelligence to adjust loudness based on dialogue analysis.

                                  - **DynamicRangeCompressionLine** *(string) --* Specify the
                                  absolute peak level for a signal with dynamic range compression.

                                  - **DynamicRangeCompressionRf** *(string) --* Specify how the
                                  service limits the audio dynamic range when compressing the audio.

                                  - **LoRoCenterMixLevel** *(float) --* Specify a value for the
                                  following Dolby Atmos setting: Left only/Right only center mix
                                  (Lo/Ro center). MediaConvert uses this value for downmixing. How
                                  the service uses this value depends on the value that you choose
                                  for Stereo downmix (Eac3AtmosStereoDownmix). Valid values: 3.0,
                                  1.5, 0.0, -1.5, -3.0, -4.5, and -6.0.

                                  - **LoRoSurroundMixLevel** *(float) --* Specify a value for the
                                  following Dolby Atmos setting: Left only/Right only (Lo/Ro
                                  surround). MediaConvert uses this value for downmixing. How the
                                  service uses this value depends on the value that you choose for
                                  Stereo downmix (Eac3AtmosStereoDownmix). Valid values: -1.5, -3.0,
                                  -4.5, -6.0, and -60. The value -60 mutes the channel.

                                  - **LtRtCenterMixLevel** *(float) --* Specify a value for the
                                  following Dolby Atmos setting: Left total/Right total center mix
                                  (Lt/Rt center). MediaConvert uses this value for downmixing. How
                                  the service uses this value depends on the value that you choose
                                  for Stereo downmix (Eac3AtmosStereoDownmix). Valid values: 3.0,
                                  1.5, 0.0, -1.5, -3.0, -4.5, and -6.0.

                                  - **LtRtSurroundMixLevel** *(float) --* Specify a value for the
                                  following Dolby Atmos setting: Left total/Right total surround mix
                                  (Lt/Rt surround). MediaConvert uses this value for downmixing. How
                                  the service uses this value depends on the value that you choose
                                  for Stereo downmix (Eac3AtmosStereoDownmix). Valid values: -1.5,
                                  -3.0, -4.5, -6.0, and -60. The value -60 mutes the channel.

                                  - **MeteringMode** *(string) --* Choose how the service meters the
                                  loudness of your audio.

                                  - **SampleRate** *(integer) --* This value is always 48000. It
                                  represents the sample rate in Hz.

                                  - **SpeechThreshold** *(integer) --* Specify the percentage of
                                  audio content that must be speech before the encoder uses the
                                  measured speech loudness as the overall program loudness.

                                  - **StereoDownmix** *(string) --* Choose how the service does
                                  stereo downmixing.

                                  - **SurroundExMode** *(string) --* Specify whether your input
                                  audio has an additional center rear surround channel matrix
                                  encoded into your left and right surround channels.

                                - **Eac3Settings** *(dict) --* Required when you set (Codec) under
                                (AudioDescriptions)>(CodecSettings) to the value EAC3.

                                  - **AttenuationControl** *(string) --* If set to ATTENUATE_3_DB,
                                  applies a 3 dB attenuation to the surround channels. Only used for
                                  3/2 coding mode.

                                  - **Bitrate** *(integer) --* Specify the average bitrate in bits
                                  per second. Valid bitrates depend on the coding mode.

                                  - **BitstreamMode** *(string) --* Specify the bitstream mode for
                                  the E-AC-3 stream that the encoder emits. For more information
                                  about the EAC3 bitstream mode, see ATSC A/52-2012 (Annex E).

                                  - **CodingMode** *(string) --* Dolby Digital Plus coding mode.
                                  Determines number of channels.

                                  - **DcFilter** *(string) --* Activates a DC highpass filter for
                                  all input channels.

                                  - **Dialnorm** *(integer) --* Sets the dialnorm for the output. If
                                  blank and input audio is Dolby Digital Plus, dialnorm will be
                                  passed through.

                                  - **DynamicRangeCompressionLine** *(string) --* Specify the
                                  absolute peak level for a signal with dynamic range compression.

                                  - **DynamicRangeCompressionRf** *(string) --* Specify how the
                                  service limits the audio dynamic range when compressing the audio.

                                  - **LfeControl** *(string) --* When encoding 3/2 audio, controls
                                  whether the LFE channel is enabled

                                  - **LfeFilter** *(string) --* Applies a 120Hz lowpass filter to
                                  the LFE channel prior to encoding. Only valid with 3_2_LFE coding
                                  mode.

                                  - **LoRoCenterMixLevel** *(float) --* Specify a value for the
                                  following Dolby Digital Plus setting: Left only/Right only center
                                  mix (Lo/Ro center). MediaConvert uses this value for downmixing.
                                  How the service uses this value depends on the value that you
                                  choose for Stereo downmix (Eac3StereoDownmix). Valid values: 3.0,
                                  1.5, 0.0, -1.5, -3.0, -4.5, -6.0, and -60. The value -60 mutes the
                                  channel. This setting applies only if you keep the default value
                                  of 3/2 - L, R, C, Ls, Rs (CODING_MODE_3_2) for the setting Coding
                                  mode (Eac3CodingMode). If you choose a different value for Coding
                                  mode, the service ignores Left only/Right only center
                                  (loRoCenterMixLevel).

                                  - **LoRoSurroundMixLevel** *(float) --* Specify a value for the
                                  following Dolby Digital Plus setting: Left only/Right only (Lo/Ro
                                  surround). MediaConvert uses this value for downmixing. How the
                                  service uses this value depends on the value that you choose for
                                  Stereo downmix (Eac3StereoDownmix). Valid values: -1.5, -3.0,
                                  -4.5, -6.0, and -60. The value -60 mutes the channel. This setting
                                  applies only if you keep the default value of 3/2 - L, R, C, Ls,
                                  Rs (CODING_MODE_3_2) for the setting Coding mode (Eac3CodingMode).
                                  If you choose a different value for Coding mode, the service
                                  ignores Left only/Right only surround (loRoSurroundMixLevel).

                                  - **LtRtCenterMixLevel** *(float) --* Specify a value for the
                                  following Dolby Digital Plus setting: Left total/Right total
                                  center mix (Lt/Rt center). MediaConvert uses this value for
                                  downmixing. How the service uses this value depends on the value
                                  that you choose for Stereo downmix (Eac3StereoDownmix). Valid
                                  values: 3.0, 1.5, 0.0, -1.5, -3.0, -4.5, -6.0, and -60. The value
                                  -60 mutes the channel. This setting applies only if you keep the
                                  default value of 3/2 - L, R, C, Ls, Rs (CODING_MODE_3_2) for the
                                  setting Coding mode (Eac3CodingMode). If you choose a different
                                  value for Coding mode, the service ignores Left total/Right total
                                  center (ltRtCenterMixLevel).

                                  - **LtRtSurroundMixLevel** *(float) --* Specify a value for the
                                  following Dolby Digital Plus setting: Left total/Right total
                                  surround mix (Lt/Rt surround). MediaConvert uses this value for
                                  downmixing. How the service uses this value depends on the value
                                  that you choose for Stereo downmix (Eac3StereoDownmix). Valid
                                  values: -1.5, -3.0, -4.5, -6.0, and -60. The value -60 mutes the
                                  channel. This setting applies only if you keep the default value
                                  of 3/2 - L, R, C, Ls, Rs (CODING_MODE_3_2) for the setting Coding
                                  mode (Eac3CodingMode). If you choose a different value for Coding
                                  mode, the service ignores Left total/Right total surround
                                  (ltRtSurroundMixLevel).

                                  - **MetadataControl** *(string) --* When set to FOLLOW_INPUT,
                                  encoder metadata will be sourced from the DD, DD+, or DolbyE
                                  decoder that supplied this audio data. If audio was not supplied
                                  from one of these streams, then the static metadata settings will
                                  be used.

                                  - **PassthroughControl** *(string) --* When set to WHEN_POSSIBLE,
                                  input DD+ audio will be passed through if it is present on the
                                  input. this detection is dynamic over the life of the transcode.
                                  Inputs that alternate between DD+ and non-DD+ content will have a
                                  consistent DD+ output as the system alternates between passthrough
                                  and encoding.

                                  - **PhaseControl** *(string) --* Controls the amount of
                                  phase-shift applied to the surround channels. Only used for 3/2
                                  coding mode.

                                  - **SampleRate** *(integer) --* This value is always 48000. It
                                  represents the sample rate in Hz.

                                  - **StereoDownmix** *(string) --* Choose how the service does
                                  stereo downmixing. This setting only applies if you keep the
                                  default value of 3/2 - L, R, C, Ls, Rs (CODING_MODE_3_2) for the
                                  setting Coding mode (Eac3CodingMode). If you choose a different
                                  value for Coding mode, the service ignores Stereo downmix
                                  (Eac3StereoDownmix).

                                  - **SurroundExMode** *(string) --* When encoding 3/2 audio, sets
                                  whether an extra center back surround channel is matrix encoded
                                  into the left and right surround channels.

                                  - **SurroundMode** *(string) --* When encoding 2/0 audio, sets
                                  whether Dolby Surround is matrix encoded into the two channels.

                                - **Mp2Settings** *(dict) --* Required when you set (Codec) under
                                (AudioDescriptions)>(CodecSettings) to the value MP2.

                                  - **Bitrate** *(integer) --* Specify the average bitrate in bits
                                  per second.

                                  - **Channels** *(integer) --* Set Channels to specify the number
                                  of channels in this output audio track. Choosing Mono in the
                                  console will give you 1 output channel; choosing Stereo will give
                                  you 2. In the API, valid values are 1 and 2.

                                  - **SampleRate** *(integer) --* Sample rate in hz.

                                - **WavSettings** *(dict) --* Required when you set (Codec) under
                                (AudioDescriptions)>(CodecSettings) to the value WAV.

                                  - **BitDepth** *(integer) --* Specify Bit depth (BitDepth), in
                                  bits per sample, to choose the encoding quality for this audio
                                  track.

                                  - **Channels** *(integer) --* Specify the number of channels in
                                  this output audio track. Valid values are 1 and even numbers up to
                                  64. For example, 1, 2, 4, 6, and so on, up to 64.

                                  - **Format** *(string) --* The service defaults to using RIFF for
                                  WAV outputs. If your output audio is likely to exceed 4 GB in file
                                  size, or if you otherwise need the extended support of the RF64
                                  format, set your output WAV file format to RF64.

                                  - **SampleRate** *(integer) --* Sample rate in Hz.

                              - **CustomLanguageCode** *(string) --* Specify the language for this
                              audio output track. The service puts this language code into your
                              output audio track when you set Language code control
                              (AudioLanguageCodeControl) to Use configured (USE_CONFIGURED). The
                              service also uses your specified custom language code when you set
                              Language code control (AudioLanguageCodeControl) to Follow input
                              (FOLLOW_INPUT), but your input file doesn't specify a language code.
                              For all outputs, you can use an ISO 639-2 or ISO 639-3 code. For
                              streaming outputs, you can also use any other code in the full
                              RFC-5646 specification. Streaming outputs are those that are in one of
                              the following output groups: CMAF, DASH ISO, Apple HLS, or Microsoft
                              Smooth Streaming.

                              - **LanguageCode** *(string) --* Indicates the language of the audio
                              output track. The ISO 639 language specified in the 'Language Code'
                              drop down will be used when 'Follow Input Language Code' is not
                              selected or when 'Follow Input Language Code' is selected but there is
                              no ISO 639 language code specified by the input.

                              - **LanguageCodeControl** *(string) --* Specify which source for
                              language code takes precedence for this audio track. When you choose
                              Follow input (FOLLOW_INPUT), the service uses the language code from
                              the input track if it's present. If there's no languge code on the
                              input track, the service uses the code that you specify in the setting
                              Language code (languageCode or customLanguageCode). When you choose
                              Use configured (USE_CONFIGURED), the service uses the language code
                              that you specify.

                              - **RemixSettings** *(dict) --* Advanced audio remixing settings.

                                - **ChannelMapping** *(dict) --* Channel mapping (ChannelMapping)
                                contains the group of fields that hold the remixing value for each
                                channel. Units are in dB. Acceptable values are within the range
                                from -60 (mute) through 6. A setting of 0 passes the input channel
                                unchanged to the output channel (no attenuation or amplification).

                                  - **OutputChannels** *(list) --* List of output channels

                                    - *(dict) --* OutputChannel mapping settings.

                                      - **InputChannels** *(list) --* List of input channels

                                        - *(integer) --*

                                - **ChannelsIn** *(integer) --* Specify the number of audio channels
                                from your input that you want to use in your output. With remixing,
                                you might combine or split the data in these channels, so the number
                                of channels in your final output might be different.

                                - **ChannelsOut** *(integer) --* Specify the number of channels in
                                this output after remixing. Valid values: 1, 2, 4, 6, 8... 64. (1
                                and even numbers to 64.)

                              - **StreamName** *(string) --* Specify a label for this output audio
                              stream. For example, "English", "Director commentary", or "track_2".
                              For streaming outputs, MediaConvert passes this information into
                              destination manifests for display on the end-viewer's player device.
                              For outputs in other output groups, the service ignores this setting.

                          - **CaptionDescriptions** *(list) --* (CaptionDescriptions) contains
                          groups of captions settings. For each output that has captions, include
                          one instance of (CaptionDescriptions). (CaptionDescriptions) can contain
                          multiple groups of captions settings.

                            - *(dict) --* Description of Caption output

                              - **CaptionSelectorName** *(string) --* Specifies which "Caption
                              Selector":#inputs-caption_selector to use from each input when
                              generating captions. The name should be of the format "Caption
                              Selector ", which denotes that the Nth Caption Selector will be used
                              from each input.

                              - **CustomLanguageCode** *(string) --* Specify the language for this
                              captions output track. For most captions output formats, the encoder
                              puts this language information in the output captions metadata. If
                              your output captions format is DVB-Sub or Burn in, the encoder uses
                              this language information when automatically selecting the font script
                              for rendering the captions text. For all outputs, you can use an ISO
                              639-2 or ISO 639-3 code. For streaming outputs, you can also use any
                              other code in the full RFC-5646 specification. Streaming outputs are
                              those that are in one of the following output groups: CMAF, DASH ISO,
                              Apple HLS, or Microsoft Smooth Streaming.

                              - **DestinationSettings** *(dict) --* Specific settings required by
                              destination type. Note that burnin_destination_settings are not
                              available if the source of the caption data is Embedded or Teletext.

                                - **BurninDestinationSettings** *(dict) --* Burn-In Destination
                                Settings.

                                  - **Alignment** *(string) --* If no explicit x_position or
                                  y_position is provided, setting alignment to centered will place
                                  the captions at the bottom center of the output. Similarly,
                                  setting a left alignment will align captions to the bottom left of
                                  the output. If x and y positions are given in conjunction with the
                                  alignment parameter, the font will be justified (either left or
                                  centered) relative to those coordinates. This option is not valid
                                  for source captions that are STL, 608/embedded or teletext. These
                                  source settings are already pre-defined by the caption stream. All
                                  burn-in and DVB-Sub font settings must match.

                                  - **BackgroundColor** *(string) --* Specifies the color of the
                                  rectangle behind the captions. All burn-in and DVB-Sub font
                                  settings must match.

                                  - **BackgroundOpacity** *(integer) --* Specifies the opacity of
                                  the background rectangle. 255 is opaque; 0 is transparent. Leaving
                                  this parameter blank is equivalent to setting it to 0
                                  (transparent). All burn-in and DVB-Sub font settings must match.

                                  - **FontColor** *(string) --* Specifies the color of the burned-in
                                  captions. This option is not valid for source captions that are
                                  STL, 608/embedded or teletext. These source settings are already
                                  pre-defined by the caption stream. All burn-in and DVB-Sub font
                                  settings must match.

                                  - **FontOpacity** *(integer) --* Specifies the opacity of the
                                  burned-in captions. 255 is opaque; 0 is transparent. All burn-in
                                  and DVB-Sub font settings must match.

                                  - **FontResolution** *(integer) --* Font resolution in DPI (dots
                                  per inch); default is 96 dpi. All burn-in and DVB-Sub font
                                  settings must match.

                                  - **FontScript** *(string) --* Provide the font script, using an
                                  ISO 15924 script code, if the LanguageCode is not sufficient for
                                  determining the script type. Where LanguageCode or
                                  CustomLanguageCode is sufficient, use "AUTOMATIC" or leave unset.
                                  This is used to help determine the appropriate font for rendering
                                  burn-in captions.

                                  - **FontSize** *(integer) --* A positive integer indicates the
                                  exact font size in points. Set to 0 for automatic font size
                                  selection. All burn-in and DVB-Sub font settings must match.

                                  - **OutlineColor** *(string) --* Specifies font outline color.
                                  This option is not valid for source captions that are either
                                  608/embedded or teletext. These source settings are already
                                  pre-defined by the caption stream. All burn-in and DVB-Sub font
                                  settings must match.

                                  - **OutlineSize** *(integer) --* Specifies font outline size in
                                  pixels. This option is not valid for source captions that are
                                  either 608/embedded or teletext. These source settings are already
                                  pre-defined by the caption stream. All burn-in and DVB-Sub font
                                  settings must match.

                                  - **ShadowColor** *(string) --* Specifies the color of the shadow
                                  cast by the captions. All burn-in and DVB-Sub font settings must
                                  match.

                                  - **ShadowOpacity** *(integer) --* Specifies the opacity of the
                                  shadow. 255 is opaque; 0 is transparent. Leaving this parameter
                                  blank is equivalent to setting it to 0 (transparent). All burn-in
                                  and DVB-Sub font settings must match.

                                  - **ShadowXOffset** *(integer) --* Specifies the horizontal offset
                                  of the shadow relative to the captions in pixels. A value of -2
                                  would result in a shadow offset 2 pixels to the left. All burn-in
                                  and DVB-Sub font settings must match.

                                  - **ShadowYOffset** *(integer) --* Specifies the vertical offset
                                  of the shadow relative to the captions in pixels. A value of -2
                                  would result in a shadow offset 2 pixels above the text. All
                                  burn-in and DVB-Sub font settings must match.

                                  - **TeletextSpacing** *(string) --* Only applies to jobs with
                                  input captions in Teletext or STL formats. Specify whether the
                                  spacing between letters in your captions is set by the captions
                                  grid or varies depending on letter width. Choose fixed grid to
                                  conform to the spacing specified in the captions file more
                                  accurately. Choose proportional to make the text easier to read if
                                  the captions are closed caption.

                                  - **XPosition** *(integer) --* Specifies the horizontal position
                                  of the caption relative to the left side of the output in pixels.
                                  A value of 10 would result in the captions starting 10 pixels from
                                  the left of the output. If no explicit x_position is provided, the
                                  horizontal caption position will be determined by the alignment
                                  parameter. This option is not valid for source captions that are
                                  STL, 608/embedded or teletext. These source settings are already
                                  pre-defined by the caption stream. All burn-in and DVB-Sub font
                                  settings must match.

                                  - **YPosition** *(integer) --* Specifies the vertical position of
                                  the caption relative to the top of the output in pixels. A value
                                  of 10 would result in the captions starting 10 pixels from the top
                                  of the output. If no explicit y_position is provided, the caption
                                  will be positioned towards the bottom of the output. This option
                                  is not valid for source captions that are STL, 608/embedded or
                                  teletext. These source settings are already pre-defined by the
                                  caption stream. All burn-in and DVB-Sub font settings must match.

                                - **DestinationType** *(string) --* Specify the format for this set
                                of captions on this output. The default format is embedded without
                                SCTE-20. Other options are embedded with SCTE-20, burn-in, DVB-sub,
                                IMSC, SCC, SRT, teletext, TTML, and web-VTT. If you are using
                                SCTE-20, choose SCTE-20 plus embedded (SCTE20_PLUS_EMBEDDED) to
                                create an output that complies with the SCTE-43 spec. To create a
                                non-compliant output where the embedded captions come first, choose
                                Embedded plus SCTE-20 (EMBEDDED_PLUS_SCTE20).

                                - **DvbSubDestinationSettings** *(dict) --* DVB-Sub Destination
                                Settings

                                  - **Alignment** *(string) --* If no explicit x_position or
                                  y_position is provided, setting alignment to centered will place
                                  the captions at the bottom center of the output. Similarly,
                                  setting a left alignment will align captions to the bottom left of
                                  the output. If x and y positions are given in conjunction with the
                                  alignment parameter, the font will be justified (either left or
                                  centered) relative to those coordinates. This option is not valid
                                  for source captions that are STL, 608/embedded or teletext. These
                                  source settings are already pre-defined by the caption stream. All
                                  burn-in and DVB-Sub font settings must match.

                                  - **BackgroundColor** *(string) --* Specifies the color of the
                                  rectangle behind the captions. All burn-in and DVB-Sub font
                                  settings must match.

                                  - **BackgroundOpacity** *(integer) --* Specifies the opacity of
                                  the background rectangle. 255 is opaque; 0 is transparent. Leaving
                                  this parameter blank is equivalent to setting it to 0
                                  (transparent). All burn-in and DVB-Sub font settings must match.

                                  - **FontColor** *(string) --* Specifies the color of the burned-in
                                  captions. This option is not valid for source captions that are
                                  STL, 608/embedded or teletext. These source settings are already
                                  pre-defined by the caption stream. All burn-in and DVB-Sub font
                                  settings must match.

                                  - **FontOpacity** *(integer) --* Specifies the opacity of the
                                  burned-in captions. 255 is opaque; 0 is transparent. All burn-in
                                  and DVB-Sub font settings must match.

                                  - **FontResolution** *(integer) --* Font resolution in DPI (dots
                                  per inch); default is 96 dpi. All burn-in and DVB-Sub font
                                  settings must match.

                                  - **FontScript** *(string) --* Provide the font script, using an
                                  ISO 15924 script code, if the LanguageCode is not sufficient for
                                  determining the script type. Where LanguageCode or
                                  CustomLanguageCode is sufficient, use "AUTOMATIC" or leave unset.
                                  This is used to help determine the appropriate font for rendering
                                  DVB-Sub captions.

                                  - **FontSize** *(integer) --* A positive integer indicates the
                                  exact font size in points. Set to 0 for automatic font size
                                  selection. All burn-in and DVB-Sub font settings must match.

                                  - **OutlineColor** *(string) --* Specifies font outline color.
                                  This option is not valid for source captions that are either
                                  608/embedded or teletext. These source settings are already
                                  pre-defined by the caption stream. All burn-in and DVB-Sub font
                                  settings must match.

                                  - **OutlineSize** *(integer) --* Specifies font outline size in
                                  pixels. This option is not valid for source captions that are
                                  either 608/embedded or teletext. These source settings are already
                                  pre-defined by the caption stream. All burn-in and DVB-Sub font
                                  settings must match.

                                  - **ShadowColor** *(string) --* Specifies the color of the shadow
                                  cast by the captions. All burn-in and DVB-Sub font settings must
                                  match.

                                  - **ShadowOpacity** *(integer) --* Specifies the opacity of the
                                  shadow. 255 is opaque; 0 is transparent. Leaving this parameter
                                  blank is equivalent to setting it to 0 (transparent). All burn-in
                                  and DVB-Sub font settings must match.

                                  - **ShadowXOffset** *(integer) --* Specifies the horizontal offset
                                  of the shadow relative to the captions in pixels. A value of -2
                                  would result in a shadow offset 2 pixels to the left. All burn-in
                                  and DVB-Sub font settings must match.

                                  - **ShadowYOffset** *(integer) --* Specifies the vertical offset
                                  of the shadow relative to the captions in pixels. A value of -2
                                  would result in a shadow offset 2 pixels above the text. All
                                  burn-in and DVB-Sub font settings must match.

                                  - **SubtitlingType** *(string) --* Specify whether your DVB
                                  subtitles are standard or for hearing impaired. Choose hearing
                                  impaired if your subtitles include audio descriptions and
                                  dialogue. Choose standard if your subtitles include only dialogue.

                                  - **TeletextSpacing** *(string) --* Only applies to jobs with
                                  input captions in Teletext or STL formats. Specify whether the
                                  spacing between letters in your captions is set by the captions
                                  grid or varies depending on letter width. Choose fixed grid to
                                  conform to the spacing specified in the captions file more
                                  accurately. Choose proportional to make the text easier to read if
                                  the captions are closed caption.

                                  - **XPosition** *(integer) --* Specifies the horizontal position
                                  of the caption relative to the left side of the output in pixels.
                                  A value of 10 would result in the captions starting 10 pixels from
                                  the left of the output. If no explicit x_position is provided, the
                                  horizontal caption position will be determined by the alignment
                                  parameter. This option is not valid for source captions that are
                                  STL, 608/embedded or teletext. These source settings are already
                                  pre-defined by the caption stream. All burn-in and DVB-Sub font
                                  settings must match.

                                  - **YPosition** *(integer) --* Specifies the vertical position of
                                  the caption relative to the top of the output in pixels. A value
                                  of 10 would result in the captions starting 10 pixels from the top
                                  of the output. If no explicit y_position is provided, the caption
                                  will be positioned towards the bottom of the output. This option
                                  is not valid for source captions that are STL, 608/embedded or
                                  teletext. These source settings are already pre-defined by the
                                  caption stream. All burn-in and DVB-Sub font settings must match.

                                - **EmbeddedDestinationSettings** *(dict) --* Settings specific to
                                embedded/ancillary caption outputs, including 608/708 Channel
                                destination number.

                                  - **Destination608ChannelNumber** *(integer) --* Ignore this
                                  setting unless your input captions are SCC format and your output
                                  captions are embedded in the video stream. Specify a CC number for
                                  each captions channel in this output. If you have two channels,
                                  choose CC numbers that aren't in the same field. For example,
                                  choose 1 and 3. For more information, see
                                  https://docs.aws.amazon.com/console/mediaconvert/dual-scc-to-embedded.

                                  - **Destination708ServiceNumber** *(integer) --* Ignore this
                                  setting unless your input captions are SCC format and you want
                                  both 608 and 708 captions embedded in your output stream.
                                  Optionally, specify the 708 service number for each output
                                  captions channel. Choose a different number for each channel. To
                                  use this setting, also set Force 608 to 708 upconvert
                                  (Convert608To708) to Upconvert (UPCONVERT) in your input captions
                                  selector settings. If you choose to upconvert but don't specify a
                                  708 service number, MediaConvert uses the number that you specify
                                  for CC channel number (destination608ChannelNumber) for the 708
                                  service number. For more information, see
                                  https://docs.aws.amazon.com/console/mediaconvert/dual-scc-to-embedded.

                                - **ImscDestinationSettings** *(dict) --* Settings specific to IMSC
                                caption outputs.

                                  - **StylePassthrough** *(string) --* Keep this setting enabled to
                                  have MediaConvert use the font style and position information from
                                  the captions source in the output. This option is available only
                                  when your input captions are CFF-TT, IMSC, SMPTE-TT, or TTML.
                                  Disable this setting for simplified output captions.

                                - **SccDestinationSettings** *(dict) --* Settings for SCC caption
                                output.

                                  - **Framerate** *(string) --* Set Framerate
                                  (SccDestinationFramerate) to make sure that the captions and the
                                  video are synchronized in the output. Specify a frame rate that
                                  matches the frame rate of the associated video. If the video frame
                                  rate is 29.97, choose 29.97 dropframe (FRAMERATE_29_97_DROPFRAME)
                                  only if the video has video_insertion=
                                      true and
                                  drop_frame_timecode=
                                      true; otherwise, choose 29.97 non-dropframe
                                  (FRAMERATE_29_97_NON_DROPFRAME).

                                - **TeletextDestinationSettings** *(dict) --* Settings for Teletext
                                caption output

                                  - **PageNumber** *(string) --* Set pageNumber to the Teletext page
                                  number for the destination captions for this output. This value
                                  must be a three-digit hexadecimal string; strings ending in -FF
                                  are invalid. If you are passing through the entire set of Teletext
                                  data, do not use this field.

                                  - **PageTypes** *(list) --* Specify the page types for this
                                  Teletext page. If you don't specify a value here, the service sets
                                  the page type to the default value Subtitle (PAGE_TYPE_SUBTITLE).
                                  If you pass through the entire set of Teletext data, don't use
                                  this field. When you pass through a set of Teletext pages, your
                                  output has the same page types as your input.

                                    - *(string) --* A page type as defined in the standard ETSI EN
                                    300 468, Table 94

                                - **TtmlDestinationSettings** *(dict) --* Settings specific to TTML
                                caption outputs, including Pass style information
                                (TtmlStylePassthrough).

                                  - **StylePassthrough** *(string) --* Pass through style and
                                  position information from a TTML-like input source (TTML,
                                  SMPTE-TT, CFF-TT) to the CFF-TT output or TTML output.

                              - **LanguageCode** *(string) --* Specify the language of this captions
                              output track. For most captions output formats, the encoder puts this
                              language information in the output captions metadata. If your output
                              captions format is DVB-Sub or Burn in, the encoder uses this language
                              information to choose the font language for rendering the captions
                              text.

                              - **LanguageDescription** *(string) --* Specify a label for this set
                              of output captions. For example, "English", "Director commentary", or
                              "track_2". For streaming outputs, MediaConvert passes this information
                              into destination manifests for display on the end-viewer's player
                              device. For outputs in other output groups, the service ignores this
                              setting.

                          - **ContainerSettings** *(dict) --* Container specific settings.

                            - **Container** *(string) --* Container for this output. Some containers
                            require a container settings object. If not specified, the default
                            object will be created.

                            - **F4vSettings** *(dict) --* Settings for F4v container

                              - **MoovPlacement** *(string) --* If set to PROGRESSIVE_DOWNLOAD, the
                              MOOV atom is relocated to the beginning of the archive as required for
                              progressive downloading. Otherwise it is placed normally at the end.

                            - **M2tsSettings** *(dict) --* MPEG-2 TS container settings. These apply
                            to outputs in a File output group when the output's container
                            (ContainerType) is MPEG-2 Transport Stream (M2TS). In these assets, data
                            is organized by the program map table (PMT). Each transport stream
                            program contains subsets of data, including audio, video, and metadata.
                            Each of these subsets of data has a numerical label called a packet
                            identifier (PID). Each transport stream program corresponds to one
                            MediaConvert output. The PMT lists the types of data in a program along
                            with their PID. Downstream systems and players use the program map table
                            to look up the PID for each type of data it accesses and then uses the
                            PIDs to locate specific data within the asset.

                              - **AudioBufferModel** *(string) --* Selects between the DVB and ATSC
                              buffer models for Dolby Digital audio.

                              - **AudioFramesPerPes** *(integer) --* The number of audio frames to
                              insert for each PES packet.

                              - **AudioPids** *(list) --* Specify the packet identifiers (PIDs) for
                              any elementary audio streams you include in this output. Specify
                              multiple PIDs as a JSON array. Default is the range 482-492.

                                - *(integer) --*

                              - **Bitrate** *(integer) --* Specify the output bitrate of the
                              transport stream in bits per second. Setting to 0 lets the muxer
                              automatically determine the appropriate bitrate. Other common values
                              are 3750000, 7500000, and 15000000.

                              - **BufferModel** *(string) --* Controls what buffer model to use for
                              accurate interleaving. If set to MULTIPLEX, use multiplex buffer
                              model. If set to NONE, this can lead to lower latency, but low-memory
                              devices may not be able to play back the stream without interruptions.

                              - **DvbNitSettings** *(dict) --* Inserts DVB Network Information Table
                              (NIT) at the specified table repetition interval.

                                - **NetworkId** *(integer) --* The numeric value placed in the
                                Network Information Table (NIT).

                                - **NetworkName** *(string) --* The network name text placed in the
                                network_name_descriptor inside the Network Information Table.
                                Maximum length is 256 characters.

                                - **NitInterval** *(integer) --* The number of milliseconds between
                                instances of this table in the output transport stream.

                              - **DvbSdtSettings** *(dict) --* Inserts DVB Service Description Table
                              (NIT) at the specified table repetition interval.

                                - **OutputSdt** *(string) --* Selects method of inserting SDT
                                information into output stream. "Follow input SDT" copies SDT
                                information from input stream to output stream. "Follow input SDT if
                                present" copies SDT information from input stream to output stream
                                if SDT information is present in the input, otherwise it will fall
                                back on the user-defined values. Enter "SDT Manually" means user
                                will enter the SDT information. "No SDT" means output stream will
                                not contain SDT information.

                                - **SdtInterval** *(integer) --* The number of milliseconds between
                                instances of this table in the output transport stream.

                                - **ServiceName** *(string) --* The service name placed in the
                                service_descriptor in the Service Description Table. Maximum length
                                is 256 characters.

                                - **ServiceProviderName** *(string) --* The service provider name
                                placed in the service_descriptor in the Service Description Table.
                                Maximum length is 256 characters.

                              - **DvbSubPids** *(list) --* Specify the packet identifiers (PIDs) for
                              DVB subtitle data included in this output. Specify multiple PIDs as a
                              JSON array. Default is the range 460-479.

                                - *(integer) --*

                              - **DvbTdtSettings** *(dict) --* Inserts DVB Time and Date Table (TDT)
                              at the specified table repetition interval.

                                - **TdtInterval** *(integer) --* The number of milliseconds between
                                instances of this table in the output transport stream.

                              - **DvbTeletextPid** *(integer) --* Specify the packet identifier
                              (PID) for DVB teletext data you include in this output. Default is
                              499.

                              - **EbpAudioInterval** *(string) --* When set to
                              VIDEO_AND_FIXED_INTERVALS, audio EBP markers will be added to
                              partitions 3 and 4. The interval between these additional markers will
                              be fixed, and will be slightly shorter than the video EBP marker
                              interval. When set to VIDEO_INTERVAL, these additional markers will
                              not be inserted. Only applicable when EBP segmentation markers are is
                              selected (segmentationMarkers is EBP or EBP_LEGACY).

                              - **EbpPlacement** *(string) --* Selects which PIDs to place EBP
                              markers on. They can either be placed only on the video PID, or on
                              both the video PID and all audio PIDs. Only applicable when EBP
                              segmentation markers are is selected (segmentationMarkers is EBP or
                              EBP_LEGACY).

                              - **EsRateInPes** *(string) --* Controls whether to include the ES
                              Rate field in the PES header.

                              - **ForceTsVideoEbpOrder** *(string) --* Keep the default value
                              (DEFAULT) unless you know that your audio EBP markers are incorrectly
                              appearing before your video EBP markers. To correct this problem, set
                              this value to Force (FORCE).

                              - **FragmentTime** *(float) --* The length, in seconds, of each
                              fragment. Only used with EBP markers.

                              - **MaxPcrInterval** *(integer) --* Specify the maximum time, in
                              milliseconds, between Program Clock References (PCRs) inserted into
                              the transport stream.

                              - **MinEbpInterval** *(integer) --* When set, enforces that Encoder
                              Boundary Points do not come within the specified time interval of each
                              other by looking ahead at input video. If another EBP is going to come
                              in within the specified time interval, the current EBP is not emitted,
                              and the segment is "stretched" to the next marker. The lookahead value
                              does not add latency to the system. The Live Event must be configured
                              elsewhere to create sufficient latency to make the lookahead accurate.

                              - **NielsenId3** *(string) --* If INSERT, Nielsen inaudible tones for
                              media tracking will be detected in the input audio and an equivalent
                              ID3 tag will be inserted in the output.

                              - **NullPacketBitrate** *(float) --* Value in bits per second of extra
                              null packets to insert into the transport stream. This can be used if
                              a downstream encryption system requires periodic null packets.

                              - **PatInterval** *(integer) --* The number of milliseconds between
                              instances of this table in the output transport stream.

                              - **PcrControl** *(string) --* When set to PCR_EVERY_PES_PACKET, a
                              Program Clock Reference value is inserted for every Packetized
                              Elementary Stream (PES) header. This is effective only when the PCR
                              PID is the same as the video or audio elementary stream.

                              - **PcrPid** *(integer) --* Specify the packet identifier (PID) for
                              the program clock reference (PCR) in this output. If you do not
                              specify a value, the service will use the value for Video PID
                              (VideoPid).

                              - **PmtInterval** *(integer) --* Specify the number of milliseconds
                              between instances of the program map table (PMT) in the output
                              transport stream.

                              - **PmtPid** *(integer) --* Specify the packet identifier (PID) for
                              the program map table (PMT) itself. Default is 480.

                              - **PrivateMetadataPid** *(integer) --* Specify the packet identifier
                              (PID) of the private metadata stream. Default is 503.

                              - **ProgramNumber** *(integer) --* Use Program number (programNumber)
                              to specify the program number used in the program map table (PMT) for
                              this output. Default is 1. Program numbers and program map tables are
                              parts of MPEG-2 transport stream containers, used for organizing data.

                              - **RateMode** *(string) --* When set to CBR, inserts null packets
                              into transport stream to fill specified bitrate. When set to VBR, the
                              bitrate setting acts as the maximum bitrate, but the output will not
                              be padded up to that bitrate.

                              - **Scte35Esam** *(dict) --* Include this in your job settings to put
                              SCTE-35 markers in your HLS and transport stream outputs at the
                              insertion points that you specify in an ESAM XML document. Provide the
                              document in the setting SCC XML (sccXml).

                                - **Scte35EsamPid** *(integer) --* Packet Identifier (PID) of the
                                SCTE-35 stream in the transport stream generated by ESAM.

                              - **Scte35Pid** *(integer) --* Specify the packet identifier (PID) of
                              the SCTE-35 stream in the transport stream.

                              - **Scte35Source** *(string) --* For SCTE-35 markers from your input--
                              Choose Passthrough (PASSTHROUGH) if you want SCTE-35 markers that
                              appear in your input to also appear in this output. Choose None (NONE)
                              if you don't want SCTE-35 markers in this output. For SCTE-35 markers
                              from an ESAM XML document-- Choose None (NONE). Also provide the ESAM
                              XML as a string in the setting Signal processing notification XML
                              (sccXml). Also enable ESAM SCTE-35 (include the property scte35Esam).

                              - **SegmentationMarkers** *(string) --* Inserts segmentation markers
                              at each segmentation_time period. rai_segstart sets the Random Access
                              Indicator bit in the adaptation field. rai_adapt sets the RAI bit and
                              adds the current timecode in the private data bytes. psi_segstart
                              inserts PAT and PMT tables at the start of segments. ebp adds Encoder
                              Boundary Point information to the adaptation field as per OpenCable
                              specification OC-SP-EBP-I01-130118. ebp_legacy adds Encoder Boundary
                              Point information to the adaptation field using a legacy proprietary
                              format.

                              - **SegmentationStyle** *(string) --* The segmentation style parameter
                              controls how segmentation markers are inserted into the transport
                              stream. With avails, it is possible that segments may be truncated,
                              which can influence where future segmentation markers are inserted.
                              When a segmentation style of "reset_cadence" is selected and a segment
                              is truncated due to an avail, we will reset the segmentation cadence.
                              This means the subsequent segment will have a duration of of
                              $segmentation_time seconds. When a segmentation style of
                              "maintain_cadence" is selected and a segment is truncated due to an
                              avail, we will not reset the segmentation cadence. This means the
                              subsequent segment will likely be truncated as well. However, all
                              segments after that will have a duration of $segmentation_time
                              seconds. Note that EBP lookahead is a slight exception to this rule.

                              - **SegmentationTime** *(float) --* Specify the length, in seconds, of
                              each segment. Required unless markers is set to _none_.

                              - **TimedMetadataPid** *(integer) --* Specify the packet identifier
                              (PID) for timed metadata in this output. Default is 502.

                              - **TransportStreamId** *(integer) --* Specify the ID for the
                              transport stream itself in the program map table for this output.
                              Transport stream IDs and program map tables are parts of MPEG-2
                              transport stream containers, used for organizing data.

                              - **VideoPid** *(integer) --* Specify the packet identifier (PID) of
                              the elementary video stream in the transport stream.

                            - **M3u8Settings** *(dict) --* Settings for TS segments in HLS

                              - **AudioFramesPerPes** *(integer) --* The number of audio frames to
                              insert for each PES packet.

                              - **AudioPids** *(list) --* Packet Identifier (PID) of the elementary
                              audio stream(s) in the transport stream. Multiple values are accepted,
                              and can be entered in ranges and/or by comma separation.

                                - *(integer) --*

                              - **NielsenId3** *(string) --* If INSERT, Nielsen inaudible tones for
                              media tracking will be detected in the input audio and an equivalent
                              ID3 tag will be inserted in the output.

                              - **PatInterval** *(integer) --* The number of milliseconds between
                              instances of this table in the output transport stream.

                              - **PcrControl** *(string) --* When set to PCR_EVERY_PES_PACKET a
                              Program Clock Reference value is inserted for every Packetized
                              Elementary Stream (PES) header. This parameter is effective only when
                              the PCR PID is the same as the video or audio elementary stream.

                              - **PcrPid** *(integer) --* Packet Identifier (PID) of the Program
                              Clock Reference (PCR) in the transport stream. When no value is given,
                              the encoder will assign the same value as the Video PID.

                              - **PmtInterval** *(integer) --* The number of milliseconds between
                              instances of this table in the output transport stream.

                              - **PmtPid** *(integer) --* Packet Identifier (PID) for the Program
                              Map Table (PMT) in the transport stream.

                              - **PrivateMetadataPid** *(integer) --* Packet Identifier (PID) of the
                              private metadata stream in the transport stream.

                              - **ProgramNumber** *(integer) --* The value of the program number
                              field in the Program Map Table.

                              - **Scte35Pid** *(integer) --* Packet Identifier (PID) of the SCTE-35
                              stream in the transport stream.

                              - **Scte35Source** *(string) --* For SCTE-35 markers from your input--
                              Choose Passthrough (PASSTHROUGH) if you want SCTE-35 markers that
                              appear in your input to also appear in this output. Choose None (NONE)
                              if you don't want SCTE-35 markers in this output. For SCTE-35 markers
                              from an ESAM XML document-- Choose None (NONE) if you don't want
                              manifest conditioning. Choose Passthrough (PASSTHROUGH) and choose Ad
                              markers (adMarkers) if you do want manifest conditioning. In both
                              cases, also provide the ESAM XML as a string in the setting Signal
                              processing notification XML (sccXml).

                              - **TimedMetadata** *(string) --* Applies only to HLS outputs. Use
                              this setting to specify whether the service inserts the ID3 timed
                              metadata from the input in this output.

                              - **TimedMetadataPid** *(integer) --* Packet Identifier (PID) of the
                              timed metadata stream in the transport stream.

                              - **TransportStreamId** *(integer) --* The value of the transport
                              stream ID field in the Program Map Table.

                              - **VideoPid** *(integer) --* Packet Identifier (PID) of the
                              elementary video stream in the transport stream.

                            - **MovSettings** *(dict) --* Settings for MOV Container.

                              - **ClapAtom** *(string) --* When enabled, include 'clap' atom if
                              appropriate for the video output settings.

                              - **CslgAtom** *(string) --* When enabled, file composition times will
                              start at zero, composition times in the 'ctts' (composition time to
                              sample) box for B-frames will be negative, and a 'cslg' (composition
                              shift least greatest) box will be included per 14496-1 amendment 1.
                              This improves compatibility with Apple players and tools.

                              - **Mpeg2FourCCControl** *(string) --* When set to XDCAM, writes MPEG2
                              video streams into the QuickTime file using XDCAM fourcc codes. This
                              increases compatibility with Apple editors and players, but may
                              decrease compatibility with other players. Only applicable when the
                              video codec is MPEG2.

                              - **PaddingControl** *(string) --* If set to OMNEON, inserts
                              Omneon-compatible padding

                              - **Reference** *(string) --* Always keep the default value
                              (SELF_CONTAINED) for this setting.

                            - **Mp4Settings** *(dict) --* Settings for MP4 container. You can create
                            audio-only AAC outputs with this container.

                              - **CslgAtom** *(string) --* When enabled, file composition times will
                              start at zero, composition times in the 'ctts' (composition time to
                              sample) box for B-frames will be negative, and a 'cslg' (composition
                              shift least greatest) box will be included per 14496-1 amendment 1.
                              This improves compatibility with Apple players and tools.

                              - **FreeSpaceBox** *(string) --* Inserts a free-space box immediately
                              after the moov box.

                              - **MoovPlacement** *(string) --* If set to PROGRESSIVE_DOWNLOAD, the
                              MOOV atom is relocated to the beginning of the archive as required for
                              progressive downloading. Otherwise it is placed normally at the end.

                              - **Mp4MajorBrand** *(string) --* Overrides the "Major Brand" field in
                              the output file. Usually not necessary to specify.

                            - **MpdSettings** *(dict) --* Settings for MP4 segments in DASH

                              - **CaptionContainerType** *(string) --* Use this setting only in DASH
                              output groups that include sidecar TTML or IMSC captions. You specify
                              sidecar captions in a separate output from your audio and video.
                              Choose Raw (RAW) for captions in a single XML file in a raw container.
                              Choose Fragmented MPEG-4 (FRAGMENTED_MP4) for captions in XML format
                              contained within fragmented MP4 files. This set of fragmented MP4
                              files is separate from your video and audio fragmented MP4 files.

                              - **Scte35Esam** *(string) --* Use this setting only when you specify
                              SCTE-35 markers from ESAM. Choose INSERT to put SCTE-35 markers in
                              this output at the insertion points that you specify in an ESAM XML
                              document. Provide the document in the setting SCC XML (sccXml).

                              - **Scte35Source** *(string) --* Ignore this setting unless you have
                              SCTE-35 markers in your input video file. Choose Passthrough
                              (PASSTHROUGH) if you want SCTE-35 markers that appear in your input to
                              also appear in this output. Choose None (NONE) if you don't want those
                              SCTE-35 markers in this output.

                          - **Extension** *(string) --* Use Extension (Extension) to specify the
                          file extension for outputs in File output groups. If you do not specify a
                          value, the service will use default extensions by container type as
                          follows * MPEG-2 transport stream, m2ts * Quicktime, mov * MXF container,
                          mxf * MPEG-4 container, mp4 * No Container, the service will use codec
                          extensions (e.g. AAC, H265, H265, AC3)

                          - **NameModifier** *(string) --* Use Name modifier (NameModifier) to have
                          the service add a string to the end of each output filename. You specify
                          the base filename as part of your destination URI. When you create
                          multiple outputs in the same output group, Name modifier (NameModifier) is
                          required. Name modifier also accepts format identifiers. For DASH ISO
                          outputs, if you use the format identifiers $Number$ or $Time$ in one
                          output, you must use them in the same way in all outputs of the output
                          group.

                          - **OutputSettings** *(dict) --* Specific settings for this type of
                          output.

                            - **HlsSettings** *(dict) --* Settings for HLS output groups

                              - **AudioGroupId** *(string) --* Specifies the group to which the
                              audio Rendition belongs.

                              - **AudioOnlyContainer** *(string) --* Use this setting only in
                              audio-only outputs. Choose MPEG-2 Transport Stream (M2TS) to create a
                              file in an MPEG2-TS container. Keep the default value Automatic
                              (AUTOMATIC) to create an audio-only file in a raw container.
                              Regardless of the value that you specify here, if this output has
                              video, the service will place the output into an MPEG2-TS container.

                              - **AudioRenditionSets** *(string) --* List all the audio groups that
                              are used with the video output stream. Input all the audio GROUP-IDs
                              that are associated to the video, separate by ','.

                              - **AudioTrackType** *(string) --* Four types of audio-only tracks are
                              supported: Audio-Only Variant Stream The client can play back this
                              audio-only stream instead of video in low-bandwidth scenarios.
                              Represented as an EXT-X-STREAM-INF in the HLS manifest. Alternate
                              Audio, Auto Select, Default Alternate rendition that the client should
                              try to play back by default. Represented as an EXT-X-MEDIA in the HLS
                              manifest with DEFAULT=YES, AUTOSELECT=
                                  YES Alternate Audio, Auto
                              Select, Not Default Alternate rendition that the client may try to
                              play back by default. Represented as an EXT-X-MEDIA in the HLS
                              manifest with DEFAULT=NO, AUTOSELECT=
                                  YES Alternate Audio, not Auto
                              Select Alternate rendition that the client will not try to play back
                              by default. Represented as an EXT-X-MEDIA in the HLS manifest with
                              DEFAULT=NO, AUTOSELECT=NO

                              - **IFrameOnlyManifest** *(string) --* When set to INCLUDE, writes
                              I-Frame Only Manifest in addition to the HLS manifest

                              - **SegmentModifier** *(string) --* String concatenated to end of
                              segment filenames. Accepts "Format
                              Identifiers":#format_identifier_parameters.

                          - **Preset** *(string) --* Use Preset (Preset) to specifiy a preset for
                          your transcoding settings. Provide the system or custom preset name. You
                          can specify either Preset (Preset) or Container settings
                          (ContainerSettings), but not both.

                          - **VideoDescription** *(dict) --* (VideoDescription) contains a group of
                          video encoding settings. The specific video settings depend on the video
                          codec that you choose when you specify a value for Video codec (codec).
                          Include one instance of (VideoDescription) per output.

                            - **AfdSignaling** *(string) --* This setting only applies to H.264,
                            H.265, and MPEG2 outputs. Use Insert AFD signaling (AfdSignaling) to
                            specify whether the service includes AFD values in the output video data
                            and what those values are. * Choose None to remove all AFD values from
                            this output. * Choose Fixed to ignore input AFD values and instead
                            encode the value specified in the job. * Choose Auto to calculate output
                            AFD values based on the input AFD scaler data.

                            - **AntiAlias** *(string) --* The anti-alias filter is automatically
                            applied to all outputs. The service no longer accepts the value DISABLED
                            for AntiAlias. If you specify that in your job, the service will ignore
                            the setting.

                            - **CodecSettings** *(dict) --* Video codec settings, (CodecSettings)
                            under (VideoDescription), contains the group of settings related to
                            video encoding. The settings in this group vary depending on the value
                            that you choose for Video codec (Codec). For each codec enum that you
                            choose, define the corresponding settings object. The following lists
                            the codec enum, settings object pairs. * H_264, H264Settings * H_265,
                            H265Settings * MPEG2, Mpeg2Settings * PRORES, ProresSettings *
                            FRAME_CAPTURE, FrameCaptureSettings

                              - **Codec** *(string) --* Specifies the video codec. This must be
                              equal to one of the enum values defined by the object VideoCodec.

                              - **FrameCaptureSettings** *(dict) --* Required when you set (Codec)
                              under (VideoDescription)>(CodecSettings) to the value FRAME_CAPTURE.

                                - **FramerateDenominator** *(integer) --* Frame capture will encode
                                the first frame of the output stream, then one frame every
                                framerateDenominator/framerateNumerator seconds. For example,
                                settings of framerateNumerator =
                                     1 and framerateDenominator = 3 (a
                                rate of 1/3 frame per second) will capture the first frame, then 1
                                frame every 3s. Files will be named as filename.n.jpg where n is the
                                0-based sequence number of each Capture.

                                - **FramerateNumerator** *(integer) --* Frame capture will encode
                                the first frame of the output stream, then one frame every
                                framerateDenominator/framerateNumerator seconds. For example,
                                settings of framerateNumerator =
                                     1 and framerateDenominator = 3 (a
                                rate of 1/3 frame per second) will capture the first frame, then 1
                                frame every 3s. Files will be named as filename.NNNNNNN.jpg where N
                                is the 0-based frame sequence number zero padded to 7 decimal
                                places.

                                - **MaxCaptures** *(integer) --* Maximum number of captures (encoded
                                jpg output files).

                                - **Quality** *(integer) --* JPEG Quality - a higher value equals
                                higher quality.

                              - **H264Settings** *(dict) --* Required when you set (Codec) under
                              (VideoDescription)>(CodecSettings) to the value H_264.

                                - **AdaptiveQuantization** *(string) --* Adaptive quantization.
                                Allows intra-frame quantizers to vary to improve visual quality.

                                - **Bitrate** *(integer) --* Specify the average bitrate in bits per
                                second. Required for VBR and CBR. For MS Smooth outputs, bitrates
                                must be unique when rounded down to the nearest multiple of 1000.

                                - **CodecLevel** *(string) --* Specify an H.264 level that is
                                consistent with your output video settings. If you aren't sure what
                                level to specify, choose Auto (AUTO).

                                - **CodecProfile** *(string) --* H.264 Profile. High 4:2:2 and
                                10-bit profiles are only available with the AVC-I License.

                                - **DynamicSubGop** *(string) --* Choose Adaptive to improve
                                subjective video quality for high-motion content. This will cause
                                the service to use fewer B-frames (which infer information based on
                                other frames) for high-motion portions of the video and more
                                B-frames for low-motion portions. The maximum number of B-frames is
                                limited by the value you provide for the setting B frames between
                                reference frames (numberBFramesBetweenReferenceFrames).

                                - **EntropyEncoding** *(string) --* Entropy encoding mode. Use CABAC
                                (must be in Main or High profile) or CAVLC.

                                - **FieldEncoding** *(string) --* Choosing FORCE_FIELD disables PAFF
                                encoding for interlaced outputs.

                                - **FlickerAdaptiveQuantization** *(string) --* Adjust quantization
                                within each frame to reduce flicker or 'pop' on I-frames.

                                - **FramerateControl** *(string) --* If you are using the console,
                                use the Framerate setting to specify the frame rate for this output.
                                If you want to keep the same frame rate as the input video, choose
                                Follow source. If you want to do frame rate conversion, choose a
                                frame rate from the dropdown list or choose Custom. The framerates
                                shown in the dropdown list are decimal approximations of fractions.
                                If you choose Custom, specify your frame rate as a fraction. If you
                                are creating your transcoding job specification as a JSON file
                                without the console, use FramerateControl to specify which value the
                                service uses for the frame rate for this output. Choose
                                INITIALIZE_FROM_SOURCE if you want the service to use the frame rate
                                from the input. Choose SPECIFIED if you want the service to use the
                                frame rate you specify in the settings FramerateNumerator and
                                FramerateDenominator.

                                - **FramerateConversionAlgorithm** *(string) --* When set to
                                INTERPOLATE, produces smoother motion during frame rate conversion.

                                - **FramerateDenominator** *(integer) --* When you use the API for
                                transcode jobs that use frame rate conversion, specify the frame
                                rate as a fraction. For example, 24000 / 1001 = 23.976 fps. Use
                                FramerateDenominator to specify the denominator of this fraction. In
                                this example, use 1001 for the value of FramerateDenominator. When
                                you use the console for transcode jobs that use frame rate
                                conversion, provide the value as a decimal number for Framerate. In
                                this example, specify 23.976.

                                - **FramerateNumerator** *(integer) --* Frame rate numerator - frame
                                rate is a fraction, e.g. 24000 / 1001 =
                                     23.976 fps.

                                - **GopBReference** *(string) --* If enable, use reference B frames
                                for GOP structures that have B frames > 1.

                                - **GopClosedCadence** *(integer) --* Frequency of closed GOPs. In
                                streaming applications, it is recommended that this be set to 1 so a
                                decoder joining mid-stream will receive an IDR frame as quickly as
                                possible. Setting this value to 0 will break output segmenting.

                                - **GopSize** *(float) --* GOP Length (keyframe interval) in frames
                                or seconds. Must be greater than zero.

                                - **GopSizeUnits** *(string) --* Indicates if the GOP Size in H264
                                is specified in frames or seconds. If seconds the system will
                                convert the GOP Size into a frame count at run time.

                                - **HrdBufferInitialFillPercentage** *(integer) --* Percentage of
                                the buffer that should initially be filled (HRD buffer model).

                                - **HrdBufferSize** *(integer) --* Size of buffer (HRD buffer model)
                                in bits. For example, enter five megabits as 5000000.

                                - **InterlaceMode** *(string) --* Use Interlace mode (InterlaceMode)
                                to choose the scan line type for the output. * Top Field First
                                (TOP_FIELD) and Bottom Field First (BOTTOM_FIELD) produce interlaced
                                output with the entire output having the same field polarity (top or
                                bottom first). * Follow, Default Top (FOLLOW_TOP_FIELD) and Follow,
                                Default Bottom (FOLLOW_BOTTOM_FIELD) use the same field polarity as
                                the source. Therefore, behavior depends on the input scan type, as
                                follows. - If the source is interlaced, the output will be
                                interlaced with the same polarity as the source (it will follow the
                                source). The output could therefore be a mix of "top field first"
                                and "bottom field first". - If the source is progressive, the output
                                will be interlaced with "top field first" or "bottom field first"
                                polarity, depending on which of the Follow options you chose.

                                - **MaxBitrate** *(integer) --* Maximum bitrate in bits/second. For
                                example, enter five megabits per second as 5000000. Required when
                                Rate control mode is QVBR.

                                - **MinIInterval** *(integer) --* Enforces separation between
                                repeated (cadence) I-frames and I-frames inserted by Scene Change
                                Detection. If a scene change I-frame is within I-interval frames of
                                a cadence I-frame, the GOP is shrunk and/or stretched to the scene
                                change I-frame. GOP stretch requires enabling lookahead as well as
                                setting I-interval. The normal cadence resumes for the next GOP.
                                This setting is only used when Scene Change Detect is enabled. Note:
                                Maximum GOP stretch =
                                     GOP size + Min-I-interval - 1

                                - **NumberBFramesBetweenReferenceFrames** *(integer) --* Number of
                                B-frames between reference frames.

                                - **NumberReferenceFrames** *(integer) --* Number of reference
                                frames to use. The encoder may use more than requested if using
                                B-frames and/or interlaced encoding.

                                - **ParControl** *(string) --* Using the API, enable ParFollowSource
                                if you want the service to use the pixel aspect ratio from the
                                input. Using the console, do this by choosing Follow source for
                                Pixel aspect ratio.

                                - **ParDenominator** *(integer) --* Pixel Aspect Ratio denominator.

                                - **ParNumerator** *(integer) --* Pixel Aspect Ratio numerator.

                                - **QualityTuningLevel** *(string) --* Use Quality tuning level
                                (H264QualityTuningLevel) to specifiy whether to use fast
                                single-pass, high-quality singlepass, or high-quality multipass
                                video encoding.

                                - **QvbrSettings** *(dict) --* Settings for quality-defined variable
                                bitrate encoding with the H.264 codec. Required when you set Rate
                                control mode to QVBR. Not valid when you set Rate control mode to a
                                value other than QVBR, or when you don't define Rate control mode.

                                  - **MaxAverageBitrate** *(integer) --* Use this setting only when
                                  Rate control mode is QVBR and Quality tuning level is Multi-pass
                                  HQ. For Max average bitrate values suited to the complexity of
                                  your input video, the service limits the average bitrate of the
                                  video part of this output to the value that you choose. That is,
                                  the total size of the video element is less than or equal to the
                                  value you set multiplied by the number of seconds of encoded
                                  output.

                                  - **QvbrQualityLevel** *(integer) --* Required when you use QVBR
                                  rate control mode. That is, when you specify qvbrSettings within
                                  h264Settings. Specify the target quality level for this output,
                                  from 1 to 10. Use higher numbers for greater quality. Level 10
                                  results in nearly lossless compression. The quality level for most
                                  broadcast-quality transcodes is between 6 and 9.

                                - **RateControlMode** *(string) --* Use this setting to specify
                                whether this output has a variable bitrate (VBR), constant bitrate
                                (CBR) or quality-defined variable bitrate (QVBR).

                                - **RepeatPps** *(string) --* Places a PPS header on each encoded
                                picture, even if repeated.

                                - **SceneChangeDetect** *(string) --* Enable this setting to insert
                                I-frames at scene changes that the service automatically detects.
                                This improves video quality and is enabled by default. If this
                                output uses QVBR, choose Transition detection (TRANSITION_DETECTION)
                                for further video quality improvement. For more information about
                                QVBR, see
                                https://docs.aws.amazon.com/console/mediaconvert/cbr-vbr-qvbr.

                                - **Slices** *(integer) --* Number of slices per picture. Must be
                                less than or equal to the number of macroblock rows for progressive
                                pictures, and less than or equal to half the number of macroblock
                                rows for interlaced pictures.

                                - **SlowPal** *(string) --* Enables Slow PAL rate conversion.
                                23.976fps and 24fps input is relabeled as 25fps, and audio is sped
                                up correspondingly.

                                - **Softness** *(integer) --* Softness. Selects quantizer matrix,
                                larger values reduce high-frequency content in the encoded image.

                                - **SpatialAdaptiveQuantization** *(string) --* Adjust quantization
                                within each frame based on spatial variation of content complexity.

                                - **Syntax** *(string) --* Produces a bitstream compliant with SMPTE
                                RP-2027.

                                - **Telecine** *(string) --* This field applies only if the Streams
                                > Advanced > Framerate (framerate) field is set to 29.970. This
                                field works with the Streams > Advanced > Preprocessors >
                                Deinterlacer field (deinterlace_mode) and the Streams > Advanced >
                                Interlaced Mode field (interlace_mode) to identify the scan type for
                                the output: Progressive, Interlaced, Hard Telecine or Soft Telecine.
                                - Hard: produces 29.97i output from 23.976 input. - Soft: produces
                                23.976; the player converts this output to 29.97i.

                                - **TemporalAdaptiveQuantization** *(string) --* Adjust quantization
                                within each frame based on temporal variation of content complexity.

                                - **UnregisteredSeiTimecode** *(string) --* Inserts timecode for
                                each frame as 4 bytes of an unregistered SEI message.

                              - **H265Settings** *(dict) --* Settings for H265 codec

                                - **AdaptiveQuantization** *(string) --* Adaptive quantization.
                                Allows intra-frame quantizers to vary to improve visual quality.

                                - **AlternateTransferFunctionSei** *(string) --* Enables Alternate
                                Transfer Function SEI message for outputs using Hybrid Log Gamma
                                (HLG) Electro-Optical Transfer Function (EOTF).

                                - **Bitrate** *(integer) --* Specify the average bitrate in bits per
                                second. Required for VBR and CBR. For MS Smooth outputs, bitrates
                                must be unique when rounded down to the nearest multiple of 1000.

                                - **CodecLevel** *(string) --* H.265 Level.

                                - **CodecProfile** *(string) --* Represents the Profile and Tier,
                                per the HEVC (H.265) specification. Selections are grouped as
                                [Profile] / [Tier], so "Main/High" represents Main Profile with High
                                Tier. 4:2:2 profiles are only available with the HEVC 4:2:2 License.

                                - **DynamicSubGop** *(string) --* Choose Adaptive to improve
                                subjective video quality for high-motion content. This will cause
                                the service to use fewer B-frames (which infer information based on
                                other frames) for high-motion portions of the video and more
                                B-frames for low-motion portions. The maximum number of B-frames is
                                limited by the value you provide for the setting B frames between
                                reference frames (numberBFramesBetweenReferenceFrames).

                                - **FlickerAdaptiveQuantization** *(string) --* Adjust quantization
                                within each frame to reduce flicker or 'pop' on I-frames.

                                - **FramerateControl** *(string) --* If you are using the console,
                                use the Framerate setting to specify the frame rate for this output.
                                If you want to keep the same frame rate as the input video, choose
                                Follow source. If you want to do frame rate conversion, choose a
                                frame rate from the dropdown list or choose Custom. The framerates
                                shown in the dropdown list are decimal approximations of fractions.
                                If you choose Custom, specify your frame rate as a fraction. If you
                                are creating your transcoding job sepecification as a JSON file
                                without the console, use FramerateControl to specify which value the
                                service uses for the frame rate for this output. Choose
                                INITIALIZE_FROM_SOURCE if you want the service to use the frame rate
                                from the input. Choose SPECIFIED if you want the service to use the
                                frame rate you specify in the settings FramerateNumerator and
                                FramerateDenominator.

                                - **FramerateConversionAlgorithm** *(string) --* When set to
                                INTERPOLATE, produces smoother motion during frame rate conversion.

                                - **FramerateDenominator** *(integer) --* Frame rate denominator.

                                - **FramerateNumerator** *(integer) --* Frame rate numerator - frame
                                rate is a fraction, e.g. 24000 / 1001 =
                                     23.976 fps.

                                - **GopBReference** *(string) --* If enable, use reference B frames
                                for GOP structures that have B frames > 1.

                                - **GopClosedCadence** *(integer) --* Frequency of closed GOPs. In
                                streaming applications, it is recommended that this be set to 1 so a
                                decoder joining mid-stream will receive an IDR frame as quickly as
                                possible. Setting this value to 0 will break output segmenting.

                                - **GopSize** *(float) --* GOP Length (keyframe interval) in frames
                                or seconds. Must be greater than zero.

                                - **GopSizeUnits** *(string) --* Indicates if the GOP Size in H265
                                is specified in frames or seconds. If seconds the system will
                                convert the GOP Size into a frame count at run time.

                                - **HrdBufferInitialFillPercentage** *(integer) --* Percentage of
                                the buffer that should initially be filled (HRD buffer model).

                                - **HrdBufferSize** *(integer) --* Size of buffer (HRD buffer model)
                                in bits. For example, enter five megabits as 5000000.

                                - **InterlaceMode** *(string) --* Choose the scan line type for the
                                output. Choose Progressive (PROGRESSIVE) to create a progressive
                                output, regardless of the scan type of your input. Choose Top Field
                                First (TOP_FIELD) or Bottom Field First (BOTTOM_FIELD) to create an
                                output that's interlaced with the same field polarity throughout.
                                Choose Follow, Default Top (FOLLOW_TOP_FIELD) or Follow, Default
                                Bottom (FOLLOW_BOTTOM_FIELD) to create an interlaced output with the
                                same field polarity as the source. If the source is interlaced, the
                                output will be interlaced with the same polarity as the source (it
                                will follow the source). The output could therefore be a mix of "top
                                field first" and "bottom field first". If the source is progressive,
                                your output will be interlaced with "top field first" or "bottom
                                field first" polarity, depending on which of the Follow options you
                                chose. If you don't choose a value, the service will default to
                                Progressive (PROGRESSIVE).

                                - **MaxBitrate** *(integer) --* Maximum bitrate in bits/second. For
                                example, enter five megabits per second as 5000000. Required when
                                Rate control mode is QVBR.

                                - **MinIInterval** *(integer) --* Enforces separation between
                                repeated (cadence) I-frames and I-frames inserted by Scene Change
                                Detection. If a scene change I-frame is within I-interval frames of
                                a cadence I-frame, the GOP is shrunk and/or stretched to the scene
                                change I-frame. GOP stretch requires enabling lookahead as well as
                                setting I-interval. The normal cadence resumes for the next GOP.
                                This setting is only used when Scene Change Detect is enabled. Note:
                                Maximum GOP stretch =
                                     GOP size + Min-I-interval - 1

                                - **NumberBFramesBetweenReferenceFrames** *(integer) --* Number of
                                B-frames between reference frames.

                                - **NumberReferenceFrames** *(integer) --* Number of reference
                                frames to use. The encoder may use more than requested if using
                                B-frames and/or interlaced encoding.

                                - **ParControl** *(string) --* Using the API, enable ParFollowSource
                                if you want the service to use the pixel aspect ratio from the
                                input. Using the console, do this by choosing Follow source for
                                Pixel aspect ratio.

                                - **ParDenominator** *(integer) --* Pixel Aspect Ratio denominator.

                                - **ParNumerator** *(integer) --* Pixel Aspect Ratio numerator.

                                - **QualityTuningLevel** *(string) --* Use Quality tuning level
                                (H265QualityTuningLevel) to specifiy whether to use fast
                                single-pass, high-quality singlepass, or high-quality multipass
                                video encoding.

                                - **QvbrSettings** *(dict) --* Settings for quality-defined variable
                                bitrate encoding with the H.265 codec. Required when you set Rate
                                control mode to QVBR. Not valid when you set Rate control mode to a
                                value other than QVBR, or when you don't define Rate control mode.

                                  - **MaxAverageBitrate** *(integer) --* Use this setting only when
                                  Rate control mode is QVBR and Quality tuning level is Multi-pass
                                  HQ. For Max average bitrate values suited to the complexity of
                                  your input video, the service limits the average bitrate of the
                                  video part of this output to the value that you choose. That is,
                                  the total size of the video element is less than or equal to the
                                  value you set multiplied by the number of seconds of encoded
                                  output.

                                  - **QvbrQualityLevel** *(integer) --* Required when you use QVBR
                                  rate control mode. That is, when you specify qvbrSettings within
                                  h265Settings. Specify the target quality level for this output,
                                  from 1 to 10. Use higher numbers for greater quality. Level 10
                                  results in nearly lossless compression. The quality level for most
                                  broadcast-quality transcodes is between 6 and 9.

                                - **RateControlMode** *(string) --* Use this setting to specify
                                whether this output has a variable bitrate (VBR), constant bitrate
                                (CBR) or quality-defined variable bitrate (QVBR).

                                - **SampleAdaptiveOffsetFilterMode** *(string) --* Specify Sample
                                Adaptive Offset (SAO) filter strength. Adaptive mode dynamically
                                selects best strength based on content

                                - **SceneChangeDetect** *(string) --* Enable this setting to insert
                                I-frames at scene changes that the service automatically detects.
                                This improves video quality and is enabled by default. If this
                                output uses QVBR, choose Transition detection (TRANSITION_DETECTION)
                                for further video quality improvement. For more information about
                                QVBR, see
                                https://docs.aws.amazon.com/console/mediaconvert/cbr-vbr-qvbr.

                                - **Slices** *(integer) --* Number of slices per picture. Must be
                                less than or equal to the number of macroblock rows for progressive
                                pictures, and less than or equal to half the number of macroblock
                                rows for interlaced pictures.

                                - **SlowPal** *(string) --* Enables Slow PAL rate conversion.
                                23.976fps and 24fps input is relabeled as 25fps, and audio is sped
                                up correspondingly.

                                - **SpatialAdaptiveQuantization** *(string) --* Adjust quantization
                                within each frame based on spatial variation of content complexity.

                                - **Telecine** *(string) --* This field applies only if the Streams
                                > Advanced > Framerate (framerate) field is set to 29.970. This
                                field works with the Streams > Advanced > Preprocessors >
                                Deinterlacer field (deinterlace_mode) and the Streams > Advanced >
                                Interlaced Mode field (interlace_mode) to identify the scan type for
                                the output: Progressive, Interlaced, Hard Telecine or Soft Telecine.
                                - Hard: produces 29.97i output from 23.976 input. - Soft: produces
                                23.976; the player converts this output to 29.97i.

                                - **TemporalAdaptiveQuantization** *(string) --* Adjust quantization
                                within each frame based on temporal variation of content complexity.

                                - **TemporalIds** *(string) --* Enables temporal layer identifiers
                                in the encoded bitstream. Up to 3 layers are supported depending on
                                GOP structure: I- and P-frames form one layer, reference B-frames
                                can form a second layer and non-reference b-frames can form a third
                                layer. Decoders can optionally decode only the lower temporal layers
                                to generate a lower frame rate output. For example, given a
                                bitstream with temporal IDs and with b-frames = 1 (i.e. IbPbPb
                                display order), a decoder could decode all the frames for full frame
                                rate output or only the I and P frames (lowest temporal layer) for a
                                half frame rate output.

                                - **Tiles** *(string) --* Enable use of tiles, allowing horizontal
                                as well as vertical subdivision of the encoded pictures.

                                - **UnregisteredSeiTimecode** *(string) --* Inserts timecode for
                                each frame as 4 bytes of an unregistered SEI message.

                                - **WriteMp4PackagingType** *(string) --* If the location of
                                parameter set NAL units doesn't matter in your workflow, ignore this
                                setting. Use this setting only with CMAF or DASH outputs, or with
                                standalone file outputs in an MPEG-4 container (MP4 outputs). Choose
                                HVC1 to mark your output as HVC1. This makes your output compliant
                                with the following specification: ISO IECJTC1 SC29 N13798 Text
                                ISO/IEC FDIS 14496-15 3rd Edition. For these outputs, the service
                                stores parameter set NAL units in the sample headers but not in the
                                samples directly. For MP4 outputs, when you choose HVC1, your output
                                video might not work properly with some downstream systems and video
                                players. The service defaults to marking your output as HEV1. For
                                these outputs, the service writes parameter set NAL units directly
                                into the samples.

                              - **Mpeg2Settings** *(dict) --* Required when you set (Codec) under
                              (VideoDescription)>(CodecSettings) to the value MPEG2.

                                - **AdaptiveQuantization** *(string) --* Adaptive quantization.
                                Allows intra-frame quantizers to vary to improve visual quality.

                                - **Bitrate** *(integer) --* Specify the average bitrate in bits per
                                second. Required for VBR and CBR. For MS Smooth outputs, bitrates
                                must be unique when rounded down to the nearest multiple of 1000.

                                - **CodecLevel** *(string) --* Use Level (Mpeg2CodecLevel) to set
                                the MPEG-2 level for the video output.

                                - **CodecProfile** *(string) --* Use Profile (Mpeg2CodecProfile) to
                                set the MPEG-2 profile for the video output.

                                - **DynamicSubGop** *(string) --* Choose Adaptive to improve
                                subjective video quality for high-motion content. This will cause
                                the service to use fewer B-frames (which infer information based on
                                other frames) for high-motion portions of the video and more
                                B-frames for low-motion portions. The maximum number of B-frames is
                                limited by the value you provide for the setting B frames between
                                reference frames (numberBFramesBetweenReferenceFrames).

                                - **FramerateControl** *(string) --* If you are using the console,
                                use the Framerate setting to specify the frame rate for this output.
                                If you want to keep the same frame rate as the input video, choose
                                Follow source. If you want to do frame rate conversion, choose a
                                frame rate from the dropdown list or choose Custom. The framerates
                                shown in the dropdown list are decimal approximations of fractions.
                                If you choose Custom, specify your frame rate as a fraction. If you
                                are creating your transcoding job sepecification as a JSON file
                                without the console, use FramerateControl to specify which value the
                                service uses for the frame rate for this output. Choose
                                INITIALIZE_FROM_SOURCE if you want the service to use the frame rate
                                from the input. Choose SPECIFIED if you want the service to use the
                                frame rate you specify in the settings FramerateNumerator and
                                FramerateDenominator.

                                - **FramerateConversionAlgorithm** *(string) --* When set to
                                INTERPOLATE, produces smoother motion during frame rate conversion.

                                - **FramerateDenominator** *(integer) --* Frame rate denominator.

                                - **FramerateNumerator** *(integer) --* Frame rate numerator - frame
                                rate is a fraction, e.g. 24000 / 1001 =
                                     23.976 fps.

                                - **GopClosedCadence** *(integer) --* Frequency of closed GOPs. In
                                streaming applications, it is recommended that this be set to 1 so a
                                decoder joining mid-stream will receive an IDR frame as quickly as
                                possible. Setting this value to 0 will break output segmenting.

                                - **GopSize** *(float) --* GOP Length (keyframe interval) in frames
                                or seconds. Must be greater than zero.

                                - **GopSizeUnits** *(string) --* Indicates if the GOP Size in MPEG2
                                is specified in frames or seconds. If seconds the system will
                                convert the GOP Size into a frame count at run time.

                                - **HrdBufferInitialFillPercentage** *(integer) --* Percentage of
                                the buffer that should initially be filled (HRD buffer model).

                                - **HrdBufferSize** *(integer) --* Size of buffer (HRD buffer model)
                                in bits. For example, enter five megabits as 5000000.

                                - **InterlaceMode** *(string) --* Use Interlace mode (InterlaceMode)
                                to choose the scan line type for the output. * Top Field First
                                (TOP_FIELD) and Bottom Field First (BOTTOM_FIELD) produce interlaced
                                output with the entire output having the same field polarity (top or
                                bottom first). * Follow, Default Top (FOLLOW_TOP_FIELD) and Follow,
                                Default Bottom (FOLLOW_BOTTOM_FIELD) use the same field polarity as
                                the source. Therefore, behavior depends on the input scan type. - If
                                the source is interlaced, the output will be interlaced with the
                                same polarity as the source (it will follow the source). The output
                                could therefore be a mix of "top field first" and "bottom field
                                first". - If the source is progressive, the output will be
                                interlaced with "top field first" or "bottom field first" polarity,
                                depending on which of the Follow options you chose.

                                - **IntraDcPrecision** *(string) --* Use Intra DC precision
                                (Mpeg2IntraDcPrecision) to set quantization precision for
                                intra-block DC coefficients. If you choose the value auto, the
                                service will automatically select the precision based on the
                                per-frame compression ratio.

                                - **MaxBitrate** *(integer) --* Maximum bitrate in bits/second. For
                                example, enter five megabits per second as 5000000.

                                - **MinIInterval** *(integer) --* Enforces separation between
                                repeated (cadence) I-frames and I-frames inserted by Scene Change
                                Detection. If a scene change I-frame is within I-interval frames of
                                a cadence I-frame, the GOP is shrunk and/or stretched to the scene
                                change I-frame. GOP stretch requires enabling lookahead as well as
                                setting I-interval. The normal cadence resumes for the next GOP.
                                This setting is only used when Scene Change Detect is enabled. Note:
                                Maximum GOP stretch =
                                     GOP size + Min-I-interval - 1

                                - **NumberBFramesBetweenReferenceFrames** *(integer) --* Number of
                                B-frames between reference frames.

                                - **ParControl** *(string) --* Using the API, enable ParFollowSource
                                if you want the service to use the pixel aspect ratio from the
                                input. Using the console, do this by choosing Follow source for
                                Pixel aspect ratio.

                                - **ParDenominator** *(integer) --* Pixel Aspect Ratio denominator.

                                - **ParNumerator** *(integer) --* Pixel Aspect Ratio numerator.

                                - **QualityTuningLevel** *(string) --* Use Quality tuning level
                                (Mpeg2QualityTuningLevel) to specifiy whether to use single-pass or
                                multipass video encoding.

                                - **RateControlMode** *(string) --* Use Rate control mode
                                (Mpeg2RateControlMode) to specifiy whether the bitrate is variable
                                (vbr) or constant (cbr).

                                - **SceneChangeDetect** *(string) --* Enable this setting to insert
                                I-frames at scene changes that the service automatically detects.
                                This improves video quality and is enabled by default.

                                - **SlowPal** *(string) --* Enables Slow PAL rate conversion.
                                23.976fps and 24fps input is relabeled as 25fps, and audio is sped
                                up correspondingly.

                                - **Softness** *(integer) --* Softness. Selects quantizer matrix,
                                larger values reduce high-frequency content in the encoded image.

                                - **SpatialAdaptiveQuantization** *(string) --* Adjust quantization
                                within each frame based on spatial variation of content complexity.

                                - **Syntax** *(string) --* Produces a Type D-10 compatible bitstream
                                (SMPTE 356M-2001).

                                - **Telecine** *(string) --* Only use Telecine (Mpeg2Telecine) when
                                you set Framerate (Framerate) to 29.970. Set Telecine
                                (Mpeg2Telecine) to Hard (hard) to produce a 29.97i output from a
                                23.976 input. Set it to Soft (soft) to produce 23.976 output and
                                leave converstion to the player.

                                - **TemporalAdaptiveQuantization** *(string) --* Adjust quantization
                                within each frame based on temporal variation of content complexity.

                              - **ProresSettings** *(dict) --* Required when you set (Codec) under
                              (VideoDescription)>(CodecSettings) to the value PRORES.

                                - **CodecProfile** *(string) --* Use Profile (ProResCodecProfile) to
                                specifiy the type of Apple ProRes codec to use for this output.

                                - **FramerateControl** *(string) --* If you are using the console,
                                use the Framerate setting to specify the frame rate for this output.
                                If you want to keep the same frame rate as the input video, choose
                                Follow source. If you want to do frame rate conversion, choose a
                                frame rate from the dropdown list or choose Custom. The framerates
                                shown in the dropdown list are decimal approximations of fractions.
                                If you choose Custom, specify your frame rate as a fraction. If you
                                are creating your transcoding job sepecification as a JSON file
                                without the console, use FramerateControl to specify which value the
                                service uses for the frame rate for this output. Choose
                                INITIALIZE_FROM_SOURCE if you want the service to use the frame rate
                                from the input. Choose SPECIFIED if you want the service to use the
                                frame rate you specify in the settings FramerateNumerator and
                                FramerateDenominator.

                                - **FramerateConversionAlgorithm** *(string) --* When set to
                                INTERPOLATE, produces smoother motion during frame rate conversion.

                                - **FramerateDenominator** *(integer) --* Frame rate denominator.

                                - **FramerateNumerator** *(integer) --* When you use the API for
                                transcode jobs that use frame rate conversion, specify the frame
                                rate as a fraction. For example, 24000 / 1001 = 23.976 fps. Use
                                FramerateNumerator to specify the numerator of this fraction. In
                                this example, use 24000 for the value of FramerateNumerator.

                                - **InterlaceMode** *(string) --* Use Interlace mode (InterlaceMode)
                                to choose the scan line type for the output. * Top Field First
                                (TOP_FIELD) and Bottom Field First (BOTTOM_FIELD) produce interlaced
                                output with the entire output having the same field polarity (top or
                                bottom first). * Follow, Default Top (FOLLOW_TOP_FIELD) and Follow,
                                Default Bottom (FOLLOW_BOTTOM_FIELD) use the same field polarity as
                                the source. Therefore, behavior depends on the input scan type. - If
                                the source is interlaced, the output will be interlaced with the
                                same polarity as the source (it will follow the source). The output
                                could therefore be a mix of "top field first" and "bottom field
                                first". - If the source is progressive, the output will be
                                interlaced with "top field first" or "bottom field first" polarity,
                                depending on which of the Follow options you chose.

                                - **ParControl** *(string) --* Use (ProresParControl) to specify how
                                the service determines the pixel aspect ratio. Set to Follow source
                                (INITIALIZE_FROM_SOURCE) to use the pixel aspect ratio from the
                                input. To specify a different pixel aspect ratio: Using the console,
                                choose it from the dropdown menu. Using the API, set
                                ProresParControl to (SPECIFIED) and provide for (ParNumerator) and
                                (ParDenominator).

                                - **ParDenominator** *(integer) --* Pixel Aspect Ratio denominator.

                                - **ParNumerator** *(integer) --* Pixel Aspect Ratio numerator.

                                - **SlowPal** *(string) --* Enables Slow PAL rate conversion.
                                23.976fps and 24fps input is relabeled as 25fps, and audio is sped
                                up correspondingly.

                                - **Telecine** *(string) --* Only use Telecine (ProresTelecine) when
                                you set Framerate (Framerate) to 29.970. Set Telecine
                                (ProresTelecine) to Hard (hard) to produce a 29.97i output from a
                                23.976 input. Set it to Soft (soft) to produce 23.976 output and
                                leave converstion to the player.

                            - **ColorMetadata** *(string) --* Choose Insert (INSERT) for this
                            setting to include color metadata in this output. Choose Ignore (IGNORE)
                            to exclude color metadata from this output. If you don't specify a
                            value, the service sets this to Insert by default.

                            - **Crop** *(dict) --* Use Cropping selection (crop) to specify the
                            video area that the service will include in the output video frame.

                              - **Height** *(integer) --* Height of rectangle in pixels. Specify
                              only even numbers.

                              - **Width** *(integer) --* Width of rectangle in pixels. Specify only
                              even numbers.

                              - **X** *(integer) --* The distance, in pixels, between the rectangle
                              and the left edge of the video frame. Specify only even numbers.

                              - **Y** *(integer) --* The distance, in pixels, between the rectangle
                              and the top edge of the video frame. Specify only even numbers.

                            - **DropFrameTimecode** *(string) --* Applies only to 29.97 fps outputs.
                            When this feature is enabled, the service will use drop-frame timecode
                            on outputs. If it is not possible to use drop-frame timecode, the system
                            will fall back to non-drop-frame. This setting is enabled by default
                            when Timecode insertion (TimecodeInsertion) is enabled.

                            - **FixedAfd** *(integer) --* Applies only if you set AFD
                            Signaling(AfdSignaling) to Fixed (FIXED). Use Fixed (FixedAfd) to
                            specify a four-bit AFD value which the service will write on all frames
                            of this video output.

                            - **Height** *(integer) --* Use the Height (Height) setting to define
                            the video resolution height for this output. Specify in pixels. If you
                            don't provide a value here, the service will use the input height.

                            - **Position** *(dict) --* Use Selection placement (position) to define
                            the video area in your output frame. The area outside of the rectangle
                            that you specify here is black.

                              - **Height** *(integer) --* Height of rectangle in pixels. Specify
                              only even numbers.

                              - **Width** *(integer) --* Width of rectangle in pixels. Specify only
                              even numbers.

                              - **X** *(integer) --* The distance, in pixels, between the rectangle
                              and the left edge of the video frame. Specify only even numbers.

                              - **Y** *(integer) --* The distance, in pixels, between the rectangle
                              and the top edge of the video frame. Specify only even numbers.

                            - **RespondToAfd** *(string) --* Use Respond to AFD (RespondToAfd) to
                            specify how the service changes the video itself in response to AFD
                            values in the input. * Choose Respond to clip the input video frame
                            according to the AFD value, input display aspect ratio, and output
                            display aspect ratio. * Choose Passthrough to include the input AFD
                            values. Do not choose this when AfdSignaling is set to (NONE). A
                            preferred implementation of this workflow is to set RespondToAfd to
                            (NONE) and set AfdSignaling to (AUTO). * Choose None to remove all input
                            AFD values from this output.

                            - **ScalingBehavior** *(string) --* Specify how the service handles
                            outputs that have a different aspect ratio from the input aspect ratio.
                            Choose Stretch to output (STRETCH_TO_OUTPUT) to have the service stretch
                            your video image to fit. Keep the setting Default (DEFAULT) to have the
                            service letterbox your video instead. This setting overrides any value
                            that you specify for the setting Selection placement (position) in this
                            output.

                            - **Sharpness** *(integer) --* Use Sharpness (Sharpness) setting to
                            specify the strength of anti-aliasing. This setting changes the width of
                            the anti-alias filter kernel used for scaling. Sharpness only applies if
                            your output resolution is different from your input resolution. 0 is the
                            softest setting, 100 the sharpest, and 50 recommended for most content.

                            - **TimecodeInsertion** *(string) --* Applies only to H.264, H.265,
                            MPEG2, and ProRes outputs. Only enable Timecode insertion when the input
                            frame rate is identical to the output frame rate. To include timecodes
                            in this output, set Timecode insertion (VideoTimecodeInsertion) to
                            PIC_TIMING_SEI. To leave them out, set it to DISABLED. Default is
                            DISABLED. When the service inserts timecodes in an output, by default,
                            it uses any embedded timecodes from the input. If none are present, the
                            service will set the timecode for the first output frame to zero. To
                            change this default behavior, adjust the settings under Timecode
                            configuration (TimecodeConfig). In the console, these settings are
                            located under Job > Job settings > Timecode configuration. Note -
                            Timecode source under input settings (InputTimecodeSource) does not
                            affect the timecodes that are inserted in the output. Source under Job
                            settings > Timecode configuration (TimecodeSource) does.

                            - **VideoPreprocessors** *(dict) --* Find additional transcoding
                            features under Preprocessors (VideoPreprocessors). Enable the features
                            at each output individually. These features are disabled by default.

                              - **ColorCorrector** *(dict) --* Enable the Color corrector
                              (ColorCorrector) feature if necessary. Enable or disable this feature
                              for each output individually. This setting is disabled by default.

                                - **Brightness** *(integer) --* Brightness level.

                                - **ColorSpaceConversion** *(string) --* Specify the color space you
                                want for this output. The service supports conversion between HDR
                                formats, between SDR formats, and from SDR to HDR. The service
                                doesn't support conversion from HDR to SDR. SDR to HDR conversion
                                doesn't upgrade the dynamic range. The converted video has an HDR
                                format, but visually appears the same as an unconverted output.

                                - **Contrast** *(integer) --* Contrast level.

                                - **Hdr10Metadata** *(dict) --* Use these settings when you convert
                                to the HDR 10 color space. Specify the SMPTE ST 2086 Mastering
                                Display Color Volume static metadata that you want signaled in the
                                output. These values don't affect the pixel values that are encoded
                                in the video stream. They are intended to help the downstream video
                                player display content in a way that reflects the intentions of the
                                the content creator. When you set Color space conversion
                                (ColorSpaceConversion) to HDR 10 (FORCE_HDR10), these settings are
                                required. You must set values for Max frame average light level
                                (maxFrameAverageLightLevel) and Max content light level
                                (maxContentLightLevel); these settings don't have a default value.
                                The default values for the other HDR 10 metadata settings are
                                defined by the P3D65 color space. For more information about
                                MediaConvert HDR jobs, see
                                https://docs.aws.amazon.com/console/mediaconvert/hdr.

                                  - **BluePrimaryX** *(integer) --* HDR Master Display Information
                                  must be provided by a color grader, using color grading tools.
                                  Range is 0 to 50,000, each increment represents 0.00002 in CIE1931
                                  color coordinate. Note that this setting is not for color
                                  correction.

                                  - **BluePrimaryY** *(integer) --* HDR Master Display Information
                                  must be provided by a color grader, using color grading tools.
                                  Range is 0 to 50,000, each increment represents 0.00002 in CIE1931
                                  color coordinate. Note that this setting is not for color
                                  correction.

                                  - **GreenPrimaryX** *(integer) --* HDR Master Display Information
                                  must be provided by a color grader, using color grading tools.
                                  Range is 0 to 50,000, each increment represents 0.00002 in CIE1931
                                  color coordinate. Note that this setting is not for color
                                  correction.

                                  - **GreenPrimaryY** *(integer) --* HDR Master Display Information
                                  must be provided by a color grader, using color grading tools.
                                  Range is 0 to 50,000, each increment represents 0.00002 in CIE1931
                                  color coordinate. Note that this setting is not for color
                                  correction.

                                  - **MaxContentLightLevel** *(integer) --* Maximum light level
                                  among all samples in the coded video sequence, in units of
                                  candelas per square meter. This setting doesn't have a default
                                  value; you must specify a value that is suitable for the content.

                                  - **MaxFrameAverageLightLevel** *(integer) --* Maximum average
                                  light level of any frame in the coded video sequence, in units of
                                  candelas per square meter. This setting doesn't have a default
                                  value; you must specify a value that is suitable for the content.

                                  - **MaxLuminance** *(integer) --* Nominal maximum mastering
                                  display luminance in units of of 0.0001 candelas per square meter.

                                  - **MinLuminance** *(integer) --* Nominal minimum mastering
                                  display luminance in units of of 0.0001 candelas per square meter

                                  - **RedPrimaryX** *(integer) --* HDR Master Display Information
                                  must be provided by a color grader, using color grading tools.
                                  Range is 0 to 50,000, each increment represents 0.00002 in CIE1931
                                  color coordinate. Note that this setting is not for color
                                  correction.

                                  - **RedPrimaryY** *(integer) --* HDR Master Display Information
                                  must be provided by a color grader, using color grading tools.
                                  Range is 0 to 50,000, each increment represents 0.00002 in CIE1931
                                  color coordinate. Note that this setting is not for color
                                  correction.

                                  - **WhitePointX** *(integer) --* HDR Master Display Information
                                  must be provided by a color grader, using color grading tools.
                                  Range is 0 to 50,000, each increment represents 0.00002 in CIE1931
                                  color coordinate. Note that this setting is not for color
                                  correction.

                                  - **WhitePointY** *(integer) --* HDR Master Display Information
                                  must be provided by a color grader, using color grading tools.
                                  Range is 0 to 50,000, each increment represents 0.00002 in CIE1931
                                  color coordinate. Note that this setting is not for color
                                  correction.

                                - **Hue** *(integer) --* Hue in degrees.

                                - **Saturation** *(integer) --* Saturation level.

                              - **Deinterlacer** *(dict) --* Use Deinterlacer (Deinterlacer) to
                              produce smoother motion and a clearer picture.

                                - **Algorithm** *(string) --* Only applies when you set Deinterlacer
                                (DeinterlaceMode) to Deinterlace (DEINTERLACE) or Adaptive
                                (ADAPTIVE). Motion adaptive interpolate (INTERPOLATE) produces
                                sharper pictures, while blend (BLEND) produces smoother motion. Use
                                (INTERPOLATE_TICKER) OR (BLEND_TICKER) if your source file includes
                                a ticker, such as a scrolling headline at the bottom of the frame.

                                - **Control** *(string) --* - When set to NORMAL (default), the
                                deinterlacer does not convert frames that are tagged in metadata as
                                progressive. It will only convert those that are tagged as some
                                other type. - When set to FORCE_ALL_FRAMES, the deinterlacer
                                converts every frame to progressive - even those that are already
                                tagged as progressive. Turn Force mode on only if there is a good
                                chance that the metadata has tagged frames as progressive when they
                                are not progressive. Do not turn on otherwise; processing frames
                                that are already progressive into progressive will probably result
                                in lower quality video.

                                - **Mode** *(string) --* Use Deinterlacer (DeinterlaceMode) to
                                choose how the service will do deinterlacing. Default is
                                Deinterlace. - Deinterlace converts interlaced to progressive. -
                                Inverse telecine converts Hard Telecine 29.97i to progressive
                                23.976p. - Adaptive auto-detects and converts to progressive.

                              - **DolbyVision** *(dict) --* Enable Dolby Vision feature to produce
                              Dolby Vision compatible video output.

                                - **L6Metadata** *(dict) --* Use these settings when you set
                                DolbyVisionLevel6Mode to SPECIFY to override the MaxCLL and MaxFALL
                                values in your input with new values.

                                  - **MaxCll** *(integer) --* Maximum Content Light Level. Static
                                  HDR metadata that corresponds to the brightest pixel in the entire
                                  stream. Measured in nits.

                                  - **MaxFall** *(integer) --* Maximum Frame-Average Light Level.
                                  Static HDR metadata that corresponds to the highest frame-average
                                  brightness in the entire stream. Measured in nits.

                                - **L6Mode** *(string) --* Use Dolby Vision Mode to choose how the
                                service will handle Dolby Vision MaxCLL and MaxFALL properies.

                                - **Profile** *(string) --* In the current MediaConvert
                                implementation, the Dolby Vision profile is always 5 (PROFILE_5).
                                Therefore, all of your inputs must contain Dolby Vision frame
                                interleaved data.

                              - **ImageInserter** *(dict) --* Enable the Image inserter
                              (ImageInserter) feature to include a graphic overlay on your video.
                              Enable or disable this feature for each output individually. This
                              setting is disabled by default.

                                - **InsertableImages** *(list) --* Specify the images that you want
                                to overlay on your video. The images must be PNG or TGA files.

                                  - *(dict) --* Settings that specify how your still graphic overlay
                                  appears.

                                    - **Duration** *(integer) --* Specify the time, in milliseconds,
                                    for the image to remain on the output video. This duration
                                    includes fade-in time but not fade-out time.

                                    - **FadeIn** *(integer) --* Specify the length of time, in
                                    milliseconds, between the Start time that you specify for the
                                    image insertion and the time that the image appears at full
                                    opacity. Full opacity is the level that you specify for the
                                    opacity setting. If you don't specify a value for Fade-in, the
                                    image will appear abruptly at the overlay start time.

                                    - **FadeOut** *(integer) --* Specify the length of time, in
                                    milliseconds, between the end of the time that you have
                                    specified for the image overlay Duration and when the overlaid
                                    image has faded to total transparency. If you don't specify a
                                    value for Fade-out, the image will disappear abruptly at the end
                                    of the inserted image duration.

                                    - **Height** *(integer) --* Specify the height of the inserted
                                    image in pixels. If you specify a value that's larger than the
                                    video resolution height, the service will crop your overlaid
                                    image to fit. To use the native height of the image, keep this
                                    setting blank.

                                    - **ImageInserterInput** *(string) --* Specify the HTTP, HTTPS,
                                    or Amazon S3 location of the image that you want to overlay on
                                    the video. Use a PNG or TGA file.

                                    - **ImageX** *(integer) --* Specify the distance, in pixels,
                                    between the inserted image and the left edge of the video frame.
                                    Required for any image overlay that you specify.

                                    - **ImageY** *(integer) --* Specify the distance, in pixels,
                                    between the overlaid image and the top edge of the video frame.
                                    Required for any image overlay that you specify.

                                    - **Layer** *(integer) --* Specify how overlapping inserted
                                    images appear. Images with higher values for Layer appear on top
                                    of images with lower values for Layer.

                                    - **Opacity** *(integer) --* Use Opacity (Opacity) to specify
                                    how much of the underlying video shows through the inserted
                                    image. 0 is transparent and 100 is fully opaque. Default is 50.

                                    - **StartTime** *(string) --* Specify the timecode of the frame
                                    that you want the overlay to first appear on. This must be in
                                    timecode (HH:MM:SS:FF or HH:MM:SS;FF) format. Remember to take
                                    into account your timecode source settings.

                                    - **Width** *(integer) --* Specify the width of the inserted
                                    image in pixels. If you specify a value that's larger than the
                                    video resolution width, the service will crop your overlaid
                                    image to fit. To use the native width of the image, keep this
                                    setting blank.

                              - **NoiseReducer** *(dict) --* Enable the Noise reducer (NoiseReducer)
                              feature to remove noise from your video output if necessary. Enable or
                              disable this feature for each output individually. This setting is
                              disabled by default.

                                - **Filter** *(string) --* Use Noise reducer filter
                                (NoiseReducerFilter) to select one of the following spatial image
                                filtering functions. To use this setting, you must also enable Noise
                                reducer (NoiseReducer). * Bilateral preserves edges while reducing
                                noise. * Mean (softest), Gaussian, Lanczos, and Sharpen (sharpest)
                                do convolution filtering. * Conserve does min/max noise reduction. *
                                Spatial does frequency-domain filtering based on JND principles. *
                                Temporal optimizes video quality for complex motion.

                                - **FilterSettings** *(dict) --* Settings for a noise reducer filter

                                  - **Strength** *(integer) --* Relative strength of noise reducing
                                  filter. Higher values produce stronger filtering.

                                - **SpatialFilterSettings** *(dict) --* Noise reducer filter
                                settings for spatial filter.

                                  - **PostFilterSharpenStrength** *(integer) --* Specify strength of
                                  post noise reduction sharpening filter, with 0 disabling the
                                  filter and 3 enabling it at maximum strength.

                                  - **Speed** *(integer) --* The speed of the filter, from -2 (lower
                                  speed) to 3 (higher speed), with 0 being the nominal value.

                                  - **Strength** *(integer) --* Relative strength of noise reducing
                                  filter. Higher values produce stronger filtering.

                                - **TemporalFilterSettings** *(dict) --* Noise reducer filter
                                settings for temporal filter.

                                  - **AggressiveMode** *(integer) --* Use Aggressive mode for
                                  content that has complex motion. Higher values produce stronger
                                  temporal filtering. This filters highly complex scenes more
                                  aggressively and creates better VQ for low bitrate outputs.

                                  - **Speed** *(integer) --* The speed of the filter (higher number
                                  is faster). Low setting reduces bit rate at the cost of transcode
                                  time, high setting improves transcode time at the cost of bit
                                  rate.

                                  - **Strength** *(integer) --* Specify the strength of the noise
                                  reducing filter on this output. Higher values produce stronger
                                  filtering. We recommend the following value ranges, depending on
                                  the result that you want: * 0-2 for complexity reduction with
                                  minimal sharpness loss * 2-8 for complexity reduction with image
                                  preservation * 8-16 for a high level of complexity reduction

                              - **TimecodeBurnin** *(dict) --* Timecode burn-in
                              (TimecodeBurnIn)--Burns the output timecode and specified prefix into
                              the output.

                                - **FontSize** *(integer) --* Use Font Size (FontSize) to set the
                                font size of any burned-in timecode. Valid values are 10, 16, 32,
                                48.

                                - **Position** *(string) --* Use Position (Position) under under
                                Timecode burn-in (TimecodeBurnIn) to specify the location the
                                burned-in timecode on output video.

                                - **Prefix** *(string) --* Use Prefix (Prefix) to place ASCII
                                characters before any burned-in timecode. For example, a prefix of
                                "EZ-" will result in the timecode "EZ-00:00:00:00". Provide either
                                the characters themselves or the ASCII code equivalents. The
                                supported range of characters is 0x20 through 0x7e. This includes
                                letters, numbers, and all special characters represented on a
                                standard English keyboard.

                            - **Width** *(integer) --* Use Width (Width) to define the video
                            resolution width, in pixels, for this output. If you don't provide a
                            value here, the service will use the input width.

                  - **TimecodeConfig** *(dict) --* Contains settings used to acquire and adjust
                  timecode information from inputs.

                    - **Anchor** *(string) --* If you use an editing platform that relies on an
                    anchor timecode, use Anchor Timecode (Anchor) to specify a timecode that will
                    match the input video frame to the output video frame. Use 24-hour format with
                    frame number, (HH:MM:SS:FF) or (HH:MM:SS;FF). This setting ignores frame rate
                    conversion. System behavior for Anchor Timecode varies depending on your setting
                    for Source (TimecodeSource). * If Source (TimecodeSource) is set to Specified
                    Start (SPECIFIEDSTART), the first input frame is the specified value in Start
                    Timecode (Start). Anchor Timecode (Anchor) and Start Timecode (Start) are used
                    calculate output timecode. * If Source (TimecodeSource) is set to Start at 0
                    (ZEROBASED) the first frame is 00:00:00:00. * If Source (TimecodeSource) is set
                    to Embedded (EMBEDDED), the first frame is the timecode value on the first input
                    frame of the input.

                    - **Source** *(string) --* Use Source (TimecodeSource) to set how timecodes are
                    handled within this job. To make sure that your video, audio, captions, and
                    markers are synchronized and that time-based features, such as image inserter,
                    work correctly, choose the Timecode source option that matches your assets. All
                    timecodes are in a 24-hour format with frame number (HH:MM:SS:FF). * Embedded
                    (EMBEDDED) - Use the timecode that is in the input video. If no embedded
                    timecode is in the source, the service will use Start at 0 (ZEROBASED) instead.
                    * Start at 0 (ZEROBASED) - Set the timecode of the initial frame to 00:00:00:00.
                    * Specified Start (SPECIFIEDSTART) - Set the timecode of the initial frame to a
                    value other than zero. You use Start timecode (Start) to provide this value.

                    - **Start** *(string) --* Only use when you set Source (TimecodeSource) to
                    Specified start (SPECIFIEDSTART). Use Start timecode (Start) to specify the
                    timecode for the initial frame. Use 24-hour format with frame number,
                    (HH:MM:SS:FF) or (HH:MM:SS;FF).

                    - **TimestampOffset** *(string) --* Only applies to outputs that support
                    program-date-time stamp. Use Timestamp offset (TimestampOffset) to overwrite the
                    timecode date without affecting the time and frame number. Provide the new date
                    as a string in the format "yyyy-mm-dd". To use Time stamp offset, you must also
                    enable Insert program-date-time (InsertProgramDateTime) in the output settings.
                    For example, if the date part of your timecodes is 2002-1-25 and you want to
                    change it to one year later, set Timestamp offset (TimestampOffset) to
                    2003-1-25.

                  - **TimedMetadataInsertion** *(dict) --* Enable Timed metadata insertion
                  (TimedMetadataInsertion) to include ID3 tags in your job. To include timed
                  metadata, you must enable it here, enable it in each output container, and specify
                  tags and timecodes in ID3 insertion (Id3Insertion) objects.

                    - **Id3Insertions** *(list) --* Id3Insertions contains the array of Id3Insertion
                    instances.

                      - *(dict) --* To insert ID3 tags in your output, specify two values. Use ID3
                      tag (Id3) to specify the base 64 encoded string and use Timecode (TimeCode) to
                      specify the time when the tag should be inserted. To insert multiple ID3 tags
                      in your output, create multiple instances of ID3 insertion (Id3Insertion).

                        - **Id3** *(string) --* Use ID3 tag (Id3) to provide a tag value in
                        base64-encode format.

                        - **Timecode** *(string) --* Provide a Timecode (TimeCode) in HH:MM:SS:FF or
                        HH:MM:SS;FF format.

                - **SimulateReservedQueue** *(string) --* Enable this setting when you run a test
                job to estimate how many reserved transcoding slots (RTS) you need. When this is
                enabled, MediaConvert runs your job from an on-demand queue with similar performance
                to what you will see with one RTS in a reserved queue. This setting is disabled by
                default.

                - **Status** *(string) --* A job's status can be SUBMITTED, PROGRESSING, COMPLETE,
                CANCELED, or ERROR.

                - **StatusUpdateInterval** *(string) --* Specify how often MediaConvert sends
                STATUS_UPDATE events to Amazon CloudWatch Events. Set the interval, in seconds,
                between status updates. MediaConvert sends an update at this interval from the time
                the service begins processing your job to the time it completes the transcode or
                encounters an error.

                - **Timing** *(dict) --* Information about when jobs are submitted, started, and
                finished is specified in Unix epoch format in seconds.

                  - **FinishTime** *(datetime) --* The time, in Unix epoch format, that the
                  transcoding job finished

                  - **StartTime** *(datetime) --* The time, in Unix epoch format, that transcoding
                  for the job began.

                  - **SubmitTime** *(datetime) --* The time, in Unix epoch format, that you
                  submitted the job.

                - **UserMetadata** *(dict) --* User-defined metadata that you want to associate with
                an MediaConvert job. You specify metadata in key/value pairs.

                  - *(string) --*

                    - *(string) --*
        """


class ListPresetsPaginator(Boto3Paginator):
    """
    Paginator for `list_presets`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Category: str = None,
        ListBy: Literal["NAME", "CREATION_DATE", "SYSTEM"] = None,
        Order: Literal["ASCENDING", "DESCENDING"] = None,
        PaginationConfig: ListPresetsPaginatePaginationConfigTypeDef = None,
    ) -> ListPresetsPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`MediaConvert.Client.list_presets`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/mediaconvert-2017-08-29/ListPresets>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              Category='string',
              ListBy='NAME'|'CREATION_DATE'|'SYSTEM',
              Order='ASCENDING'|'DESCENDING',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type Category: string
        :param Category: Optionally, specify a preset category to limit responses to only presets
        from that category.

        :type ListBy: string
        :param ListBy: Optional. When you request a list of presets, you can choose to list them
        alphabetically by NAME or chronologically by CREATION_DATE. If you don't specify, the
        service will list them by name.

        :type Order: string
        :param Order: When you request lists of resources, you can optionally specify whether they
        are sorted in ASCENDING or DESCENDING order. Default varies by resource.

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
                'Presets': [
                    {
                        'Arn': 'string',
                        'Category': 'string',
                        'CreatedAt': datetime(2015, 1, 1),
                        'Description': 'string',
                        'LastUpdated': datetime(2015, 1, 1),
                        'Name': 'string',
                        'Settings': {
                            'AudioDescriptions': [
                                {
                                    'AudioNormalizationSettings': {
                                        'Algorithm':
                                        'ITU_BS_1770_1'
                                        |'ITU_BS_1770_2'
                                        |'ITU_BS_1770_3'
                                        |'ITU_BS_1770_4',
                                        'AlgorithmControl': 'CORRECT_AUDIO'|'MEASURE_ONLY',
                                        'CorrectionGateLevel': 123,
                                        'LoudnessLogging': 'LOG'|'DONT_LOG',
                                        'PeakCalculation': 'TRUE_PEAK'|'NONE',
                                        'TargetLkfs': 123.0
                                    },
                                    'AudioSourceName': 'string',
                                    'AudioType': 123,
                                    'AudioTypeControl': 'FOLLOW_INPUT'|'USE_CONFIGURED',
                                    'CodecSettings': {
                                        'AacSettings': {
                                            'AudioDescriptionBroadcasterMix':
                                            'BROADCASTER_MIXED_AD'
                                            |'NORMAL',
                                            'Bitrate': 123,
                                            'CodecProfile': 'LC'|'HEV1'|'HEV2',
                                            'CodingMode':
                                            'AD_RECEIVER_MIX'
                                            |'CODING_MODE_1_0'
                                            |'CODING_MODE_1_1'
                                            |'CODING_MODE_2_0'
                                            |'CODING_MODE_5_1',
                                            'RateControlMode': 'CBR'|'VBR',
                                            'RawFormat': 'LATM_LOAS'|'NONE',
                                            'SampleRate': 123,
                                            'Specification': 'MPEG2'|'MPEG4',
                                            'VbrQuality': 'LOW'|'MEDIUM_LOW'|'MEDIUM_HIGH'|'HIGH'
                                        },
                                        'Ac3Settings': {
                                            'Bitrate': 123,
                                            'BitstreamMode':
                                            'COMPLETE_MAIN'
                                            |'COMMENTARY'
                                            |'DIALOGUE'
                                            |'EMERGENCY'
                                            |'HEARING_IMPAIRED'
                                            |'MUSIC_AND_EFFECTS'
                                            |'VISUALLY_IMPAIRED'
                                            |'VOICE_OVER',
                                            'CodingMode':
                                            'CODING_MODE_1_0'
                                            |'CODING_MODE_1_1'
                                            |'CODING_MODE_2_0'
                                            |'CODING_MODE_3_2_LFE',
                                            'Dialnorm': 123,
                                            'DynamicRangeCompressionProfile':
                                            'FILM_STANDARD'
                                            |'NONE',
                                            'LfeFilter': 'ENABLED'|'DISABLED',
                                            'MetadataControl': 'FOLLOW_INPUT'|'USE_CONFIGURED',
                                            'SampleRate': 123
                                        },
                                        'AiffSettings': {
                                            'BitDepth': 123,
                                            'Channels': 123,
                                            'SampleRate': 123
                                        },
                                        'Codec':
                                        'AAC'|'MP2'|'WAV'|'AIFF'
                                        |'AC3'|'EAC3'|'EAC3_ATMOS'
                                        |'PASSTHROUGH',
                                        'Eac3AtmosSettings': {
                                            'Bitrate': 123,
                                            'BitstreamMode': 'COMPLETE_MAIN',
                                            'CodingMode': 'CODING_MODE_9_1_6',
                                            'DialogueIntelligence': 'ENABLED'|'DISABLED',
                                            'DynamicRangeCompressionLine':
                                            'NONE'
                                            |'FILM_STANDARD'
                                            |'FILM_LIGHT'
                                            |'MUSIC_STANDARD'
                                            |'MUSIC_LIGHT'
                                            |'SPEECH',
                                            'DynamicRangeCompressionRf':
                                            'NONE'
                                            |'FILM_STANDARD'
                                            |'FILM_LIGHT'
                                            |'MUSIC_STANDARD'
                                            |'MUSIC_LIGHT'
                                            |'SPEECH',
                                            'LoRoCenterMixLevel': 123.0,
                                            'LoRoSurroundMixLevel': 123.0,
                                            'LtRtCenterMixLevel': 123.0,
                                            'LtRtSurroundMixLevel': 123.0,
                                            'MeteringMode':
                                            'LEQ_A'
                                            |'ITU_BS_1770_1'
                                            |'ITU_BS_1770_2'
                                            |'ITU_BS_1770_3'
                                            |'ITU_BS_1770_4',
                                            'SampleRate': 123,
                                            'SpeechThreshold': 123,
                                            'StereoDownmix':
                                            'NOT_INDICATED'
                                            |'STEREO'|'SURROUND'
                                            |'DPL2',
                                            'SurroundExMode': 'NOT_INDICATED'|'ENABLED'|'DISABLED'
                                        },
                                        'Eac3Settings': {
                                            'AttenuationControl': 'ATTENUATE_3_DB'|'NONE',
                                            'Bitrate': 123,
                                            'BitstreamMode':
                                            'COMPLETE_MAIN'
                                            |'COMMENTARY'
                                            |'EMERGENCY'
                                            |'HEARING_IMPAIRED'
                                            |'VISUALLY_IMPAIRED',
                                            'CodingMode':
                                            'CODING_MODE_1_0'
                                            |'CODING_MODE_2_0'
                                            |'CODING_MODE_3_2',
                                            'DcFilter': 'ENABLED'|'DISABLED',
                                            'Dialnorm': 123,
                                            'DynamicRangeCompressionLine':
                                            'NONE'
                                            |'FILM_STANDARD'
                                            |'FILM_LIGHT'
                                            |'MUSIC_STANDARD'
                                            |'MUSIC_LIGHT'
                                            |'SPEECH',
                                            'DynamicRangeCompressionRf':
                                            'NONE'
                                            |'FILM_STANDARD'
                                            |'FILM_LIGHT'
                                            |'MUSIC_STANDARD'
                                            |'MUSIC_LIGHT'
                                            |'SPEECH',
                                            'LfeControl': 'LFE'|'NO_LFE',
                                            'LfeFilter': 'ENABLED'|'DISABLED',
                                            'LoRoCenterMixLevel': 123.0,
                                            'LoRoSurroundMixLevel': 123.0,
                                            'LtRtCenterMixLevel': 123.0,
                                            'LtRtSurroundMixLevel': 123.0,
                                            'MetadataControl': 'FOLLOW_INPUT'|'USE_CONFIGURED',
                                            'PassthroughControl': 'WHEN_POSSIBLE'|'NO_PASSTHROUGH',
                                            'PhaseControl': 'SHIFT_90_DEGREES'|'NO_SHIFT',
                                            'SampleRate': 123,
                                            'StereoDownmix': 'NOT_INDICATED'|'LO_RO'|'LT_RT'|'DPL2',
                                            'SurroundExMode': 'NOT_INDICATED'|'ENABLED'|'DISABLED',
                                            'SurroundMode': 'NOT_INDICATED'|'ENABLED'|'DISABLED'
                                        },
                                        'Mp2Settings': {
                                            'Bitrate': 123,
                                            'Channels': 123,
                                            'SampleRate': 123
                                        },
                                        'WavSettings': {
                                            'BitDepth': 123,
                                            'Channels': 123,
                                            'Format': 'RIFF'|'RF64',
                                            'SampleRate': 123
                                        }
                                    },
                                    'CustomLanguageCode': 'string',
                                    'LanguageCode':
                                    'ENG'|'SPA'|'FRA'|'DEU'|'GER'|'ZHO'
                                    |'ARA'|'HIN'|'JPN'|'RUS'|'POR'|'ITA'
                                    |'URD'|'VIE'|'KOR'|'PAN'|'ABK'|'AAR'
                                    |'AFR'|'AKA'|'SQI'|'AMH'|'ARG'|'HYE'
                                    |'ASM'|'AVA'|'AVE'|'AYM'|'AZE'|'BAM'
                                    |'BAK'|'EUS'|'BEL'|'BEN'|'BIH'|'BIS'
                                    |'BOS'|'BRE'|'BUL'|'MYA'|'CAT'|'KHM'
                                    |'CHA'|'CHE'|'NYA'|'CHU'|'CHV'|'COR'
                                    |'COS'|'CRE'|'HRV'|'CES'|'DAN'|'DIV'
                                    |'NLD'|'DZO'|'ENM'|'EPO'|'EST'|'EWE'
                                    |'FAO'|'FIJ'|'FIN'|'FRM'|'FUL'|'GLA'
                                    |'GLG'|'LUG'|'KAT'|'ELL'|'GRN'|'GUJ'
                                    |'HAT'|'HAU'|'HEB'|'HER'|'HMO'|'HUN'
                                    |'ISL'|'IDO'|'IBO'|'IND'|'INA'|'ILE'
                                    |'IKU'|'IPK'|'GLE'|'JAV'|'KAL'|'KAN'
                                    |'KAU'|'KAS'|'KAZ'|'KIK'|'KIN'|'KIR'
                                    |'KOM'|'KON'|'KUA'|'KUR'|'LAO'|'LAT'
                                    |'LAV'|'LIM'|'LIN'|'LIT'|'LUB'|'LTZ'
                                    |'MKD'|'MLG'|'MSA'|'MAL'|'MLT'|'GLV'
                                    |'MRI'|'MAR'|'MAH'|'MON'|'NAU'|'NAV'
                                    |'NDE'|'NBL'|'NDO'|'NEP'|'SME'|'NOR'
                                    |'NOB'|'NNO'|'OCI'|'OJI'|'ORI'|'ORM'
                                    |'OSS'|'PLI'|'FAS'|'POL'|'PUS'|'QUE'
                                    |'QAA'|'RON'|'ROH'|'RUN'|'SMO'|'SAG'
                                    |'SAN'|'SRD'|'SRB'|'SNA'|'III'|'SND'
                                    |'SIN'|'SLK'|'SLV'|'SOM'|'SOT'|'SUN'
                                    |'SWA'|'SSW'|'SWE'|'TGL'|'TAH'|'TGK'
                                    |'TAM'|'TAT'|'TEL'|'THA'|'BOD'|'TIR'
                                    |'TON'|'TSO'|'TSN'|'TUR'|'TUK'|'TWI'
                                    |'UIG'|'UKR'|'UZB'|'VEN'|'VOL'|'WLN'
                                    |'CYM'|'FRY'|'WOL'|'XHO'|'YID'|'YOR'
                                    |'ZHA'|'ZUL'|'ORJ'|'QPC'|'TNG',
                                    'LanguageCodeControl': 'FOLLOW_INPUT'|'USE_CONFIGURED',
                                    'RemixSettings': {
                                        'ChannelMapping': {
                                            'OutputChannels': [
                                                {
                                                    'InputChannels': [
                                                        123,
                                                    ]
                                                },
                                            ]
                                        },
                                        'ChannelsIn': 123,
                                        'ChannelsOut': 123
                                    },
                                    'StreamName': 'string'
                                },
                            ],
                            'CaptionDescriptions': [
                                {
                                    'CustomLanguageCode': 'string',
                                    'DestinationSettings': {
                                        'BurninDestinationSettings': {
                                            'Alignment': 'CENTERED'|'LEFT',
                                            'BackgroundColor': 'NONE'|'BLACK'|'WHITE',
                                            'BackgroundOpacity': 123,
                                            'FontColor':
                                            'WHITE'|'BLACK'
                                            |'YELLOW'|'RED'
                                            |'GREEN'|'BLUE',
                                            'FontOpacity': 123,
                                            'FontResolution': 123,
                                            'FontScript': 'AUTOMATIC'|'HANS'|'HANT',
                                            'FontSize': 123,
                                            'OutlineColor':
                                            'BLACK'|'WHITE'
                                            |'YELLOW'|'RED'
                                            |'GREEN'|'BLUE',
                                            'OutlineSize': 123,
                                            'ShadowColor': 'NONE'|'BLACK'|'WHITE',
                                            'ShadowOpacity': 123,
                                            'ShadowXOffset': 123,
                                            'ShadowYOffset': 123,
                                            'TeletextSpacing': 'FIXED_GRID'|'PROPORTIONAL',
                                            'XPosition': 123,
                                            'YPosition': 123
                                        },
                                        'DestinationType':
                                        'BURN_IN'|'DVB_SUB'
                                        |'EMBEDDED'
                                        |'EMBEDDED_PLUS_SCTE20'
                                        |'IMSC'
                                        |'SCTE20_PLUS_EMBEDDED'
                                        |'SCC'|'SRT'|'SMI'
                                        |'TELETEXT'|'TTML'|'WEBVTT',
                                        'DvbSubDestinationSettings': {
                                            'Alignment': 'CENTERED'|'LEFT',
                                            'BackgroundColor': 'NONE'|'BLACK'|'WHITE',
                                            'BackgroundOpacity': 123,
                                            'FontColor':
                                            'WHITE'|'BLACK'
                                            |'YELLOW'|'RED'
                                            |'GREEN'|'BLUE',
                                            'FontOpacity': 123,
                                            'FontResolution': 123,
                                            'FontScript': 'AUTOMATIC'|'HANS'|'HANT',
                                            'FontSize': 123,
                                            'OutlineColor':
                                            'BLACK'|'WHITE'
                                            |'YELLOW'|'RED'
                                            |'GREEN'|'BLUE',
                                            'OutlineSize': 123,
                                            'ShadowColor': 'NONE'|'BLACK'|'WHITE',
                                            'ShadowOpacity': 123,
                                            'ShadowXOffset': 123,
                                            'ShadowYOffset': 123,
                                            'SubtitlingType': 'HEARING_IMPAIRED'|'STANDARD',
                                            'TeletextSpacing': 'FIXED_GRID'|'PROPORTIONAL',
                                            'XPosition': 123,
                                            'YPosition': 123
                                        },
                                        'EmbeddedDestinationSettings': {
                                            'Destination608ChannelNumber': 123,
                                            'Destination708ServiceNumber': 123
                                        },
                                        'ImscDestinationSettings': {
                                            'StylePassthrough': 'ENABLED'|'DISABLED'
                                        },
                                        'SccDestinationSettings': {
                                            'Framerate':
                                            'FRAMERATE_23_97'
                                            |'FRAMERATE_24'
                                            |'FRAMERATE_25'
                                            |'FRAMERATE_29_97_DROPFRAME'
                                            |'FRAMERATE_29_97_NON_DROPFRAME'
                                        },
                                        'TeletextDestinationSettings': {
                                            'PageNumber': 'string',
                                            'PageTypes': [
                                                'PAGE_TYPE_INITIAL'|'PAGE_TYPE_SUBTITLE'
                                                |'PAGE_TYPE_ADDL_INFO'|'PAGE_TYPE_PROGRAM_SCHEDULE'
                                                |'PAGE_TYPE_HEARING_IMPAIRED_SUBTITLE',
                                            ]
                                        },
                                        'TtmlDestinationSettings': {
                                            'StylePassthrough': 'ENABLED'|'DISABLED'
                                        }
                                    },
                                    'LanguageCode':
                                    'ENG'|'SPA'|'FRA'|'DEU'|'GER'|'ZHO'
                                    |'ARA'|'HIN'|'JPN'|'RUS'|'POR'|'ITA'
                                    |'URD'|'VIE'|'KOR'|'PAN'|'ABK'|'AAR'
                                    |'AFR'|'AKA'|'SQI'|'AMH'|'ARG'|'HYE'
                                    |'ASM'|'AVA'|'AVE'|'AYM'|'AZE'|'BAM'
                                    |'BAK'|'EUS'|'BEL'|'BEN'|'BIH'|'BIS'
                                    |'BOS'|'BRE'|'BUL'|'MYA'|'CAT'|'KHM'
                                    |'CHA'|'CHE'|'NYA'|'CHU'|'CHV'|'COR'
                                    |'COS'|'CRE'|'HRV'|'CES'|'DAN'|'DIV'
                                    |'NLD'|'DZO'|'ENM'|'EPO'|'EST'|'EWE'
                                    |'FAO'|'FIJ'|'FIN'|'FRM'|'FUL'|'GLA'
                                    |'GLG'|'LUG'|'KAT'|'ELL'|'GRN'|'GUJ'
                                    |'HAT'|'HAU'|'HEB'|'HER'|'HMO'|'HUN'
                                    |'ISL'|'IDO'|'IBO'|'IND'|'INA'|'ILE'
                                    |'IKU'|'IPK'|'GLE'|'JAV'|'KAL'|'KAN'
                                    |'KAU'|'KAS'|'KAZ'|'KIK'|'KIN'|'KIR'
                                    |'KOM'|'KON'|'KUA'|'KUR'|'LAO'|'LAT'
                                    |'LAV'|'LIM'|'LIN'|'LIT'|'LUB'|'LTZ'
                                    |'MKD'|'MLG'|'MSA'|'MAL'|'MLT'|'GLV'
                                    |'MRI'|'MAR'|'MAH'|'MON'|'NAU'|'NAV'
                                    |'NDE'|'NBL'|'NDO'|'NEP'|'SME'|'NOR'
                                    |'NOB'|'NNO'|'OCI'|'OJI'|'ORI'|'ORM'
                                    |'OSS'|'PLI'|'FAS'|'POL'|'PUS'|'QUE'
                                    |'QAA'|'RON'|'ROH'|'RUN'|'SMO'|'SAG'
                                    |'SAN'|'SRD'|'SRB'|'SNA'|'III'|'SND'
                                    |'SIN'|'SLK'|'SLV'|'SOM'|'SOT'|'SUN'
                                    |'SWA'|'SSW'|'SWE'|'TGL'|'TAH'|'TGK'
                                    |'TAM'|'TAT'|'TEL'|'THA'|'BOD'|'TIR'
                                    |'TON'|'TSO'|'TSN'|'TUR'|'TUK'|'TWI'
                                    |'UIG'|'UKR'|'UZB'|'VEN'|'VOL'|'WLN'
                                    |'CYM'|'FRY'|'WOL'|'XHO'|'YID'|'YOR'
                                    |'ZHA'|'ZUL'|'ORJ'|'QPC'|'TNG',
                                    'LanguageDescription': 'string'
                                },
                            ],
                            'ContainerSettings': {
                                'Container':
                                'F4V'|'ISMV'|'M2TS'|'M3U8'|'CMFC'|'MOV'
                                |'MP4'|'MPD'|'MXF'|'RAW',
                                'F4vSettings': {
                                    'MoovPlacement': 'PROGRESSIVE_DOWNLOAD'|'NORMAL'
                                },
                                'M2tsSettings': {
                                    'AudioBufferModel': 'DVB'|'ATSC',
                                    'AudioFramesPerPes': 123,
                                    'AudioPids': [
                                        123,
                                    ],
                                    'Bitrate': 123,
                                    'BufferModel': 'MULTIPLEX'|'NONE',
                                    'DvbNitSettings': {
                                        'NetworkId': 123,
                                        'NetworkName': 'string',
                                        'NitInterval': 123
                                    },
                                    'DvbSdtSettings': {
                                        'OutputSdt':
                                        'SDT_FOLLOW'
                                        |'SDT_FOLLOW_IF_PRESENT'
                                        |'SDT_MANUAL'|'SDT_NONE',
                                        'SdtInterval': 123,
                                        'ServiceName': 'string',
                                        'ServiceProviderName': 'string'
                                    },
                                    'DvbSubPids': [
                                        123,
                                    ],
                                    'DvbTdtSettings': {
                                        'TdtInterval': 123
                                    },
                                    'DvbTeletextPid': 123,
                                    'EbpAudioInterval':
                                    'VIDEO_AND_FIXED_INTERVALS'
                                    |'VIDEO_INTERVAL',
                                    'EbpPlacement': 'VIDEO_AND_AUDIO_PIDS'|'VIDEO_PID',
                                    'EsRateInPes': 'INCLUDE'|'EXCLUDE',
                                    'ForceTsVideoEbpOrder': 'FORCE'|'DEFAULT',
                                    'FragmentTime': 123.0,
                                    'MaxPcrInterval': 123,
                                    'MinEbpInterval': 123,
                                    'NielsenId3': 'INSERT'|'NONE',
                                    'NullPacketBitrate': 123.0,
                                    'PatInterval': 123,
                                    'PcrControl': 'PCR_EVERY_PES_PACKET'|'CONFIGURED_PCR_PERIOD',
                                    'PcrPid': 123,
                                    'PmtInterval': 123,
                                    'PmtPid': 123,
                                    'PrivateMetadataPid': 123,
                                    'ProgramNumber': 123,
                                    'RateMode': 'VBR'|'CBR',
                                    'Scte35Esam': {
                                        'Scte35EsamPid': 123
                                    },
                                    'Scte35Pid': 123,
                                    'Scte35Source': 'PASSTHROUGH'|'NONE',
                                    'SegmentationMarkers':
                                    'NONE'|'RAI_SEGSTART'|'RAI_ADAPT'
                                    |'PSI_SEGSTART'|'EBP'|'EBP_LEGACY',
                                    'SegmentationStyle': 'MAINTAIN_CADENCE'|'RESET_CADENCE',
                                    'SegmentationTime': 123.0,
                                    'TimedMetadataPid': 123,
                                    'TransportStreamId': 123,
                                    'VideoPid': 123
                                },
                                'M3u8Settings': {
                                    'AudioFramesPerPes': 123,
                                    'AudioPids': [
                                        123,
                                    ],
                                    'NielsenId3': 'INSERT'|'NONE',
                                    'PatInterval': 123,
                                    'PcrControl': 'PCR_EVERY_PES_PACKET'|'CONFIGURED_PCR_PERIOD',
                                    'PcrPid': 123,
                                    'PmtInterval': 123,
                                    'PmtPid': 123,
                                    'PrivateMetadataPid': 123,
                                    'ProgramNumber': 123,
                                    'Scte35Pid': 123,
                                    'Scte35Source': 'PASSTHROUGH'|'NONE',
                                    'TimedMetadata': 'PASSTHROUGH'|'NONE',
                                    'TimedMetadataPid': 123,
                                    'TransportStreamId': 123,
                                    'VideoPid': 123
                                },
                                'MovSettings': {
                                    'ClapAtom': 'INCLUDE'|'EXCLUDE',
                                    'CslgAtom': 'INCLUDE'|'EXCLUDE',
                                    'Mpeg2FourCCControl': 'XDCAM'|'MPEG',
                                    'PaddingControl': 'OMNEON'|'NONE',
                                    'Reference': 'SELF_CONTAINED'|'EXTERNAL'
                                },
                                'Mp4Settings': {
                                    'CslgAtom': 'INCLUDE'|'EXCLUDE',
                                    'FreeSpaceBox': 'INCLUDE'|'EXCLUDE',
                                    'MoovPlacement': 'PROGRESSIVE_DOWNLOAD'|'NORMAL',
                                    'Mp4MajorBrand': 'string'
                                },
                                'MpdSettings': {
                                    'CaptionContainerType': 'RAW'|'FRAGMENTED_MP4',
                                    'Scte35Esam': 'INSERT'|'NONE',
                                    'Scte35Source': 'PASSTHROUGH'|'NONE'
                                }
                            },
                            'VideoDescription': {
                                'AfdSignaling': 'NONE'|'AUTO'|'FIXED',
                                'AntiAlias': 'DISABLED'|'ENABLED',
                                'CodecSettings': {
                                    'Codec': 'FRAME_CAPTURE'|'H_264'|'H_265'|'MPEG2'|'PRORES',
                                    'FrameCaptureSettings': {
                                        'FramerateDenominator': 123,
                                        'FramerateNumerator': 123,
                                        'MaxCaptures': 123,
                                        'Quality': 123
                                    },
                                    'H264Settings': {
                                        'AdaptiveQuantization':
                                        'OFF'|'LOW'|'MEDIUM'|'HIGH'
                                        |'HIGHER'|'MAX',
                                        'Bitrate': 123,
                                        'CodecLevel':
                                        'AUTO'|'LEVEL_1'|'LEVEL_1_1'
                                        |'LEVEL_1_2'|'LEVEL_1_3'
                                        |'LEVEL_2'|'LEVEL_2_1'
                                        |'LEVEL_2_2'|'LEVEL_3'
                                        |'LEVEL_3_1'|'LEVEL_3_2'
                                        |'LEVEL_4'|'LEVEL_4_1'
                                        |'LEVEL_4_2'|'LEVEL_5'
                                        |'LEVEL_5_1'|'LEVEL_5_2',
                                        'CodecProfile':
                                        'BASELINE'|'HIGH'
                                        |'HIGH_10BIT'|'HIGH_422'
                                        |'HIGH_422_10BIT'|'MAIN',
                                        'DynamicSubGop': 'ADAPTIVE'|'STATIC',
                                        'EntropyEncoding': 'CABAC'|'CAVLC',
                                        'FieldEncoding': 'PAFF'|'FORCE_FIELD',
                                        'FlickerAdaptiveQuantization': 'DISABLED'|'ENABLED',
                                        'FramerateControl': 'INITIALIZE_FROM_SOURCE'|'SPECIFIED',
                                        'FramerateConversionAlgorithm':
                                        'DUPLICATE_DROP'
                                        |'INTERPOLATE',
                                        'FramerateDenominator': 123,
                                        'FramerateNumerator': 123,
                                        'GopBReference': 'DISABLED'|'ENABLED',
                                        'GopClosedCadence': 123,
                                        'GopSize': 123.0,
                                        'GopSizeUnits': 'FRAMES'|'SECONDS',
                                        'HrdBufferInitialFillPercentage': 123,
                                        'HrdBufferSize': 123,
                                        'InterlaceMode':
                                        'PROGRESSIVE'|'TOP_FIELD'
                                        |'BOTTOM_FIELD'
                                        |'FOLLOW_TOP_FIELD'
                                        |'FOLLOW_BOTTOM_FIELD',
                                        'MaxBitrate': 123,
                                        'MinIInterval': 123,
                                        'NumberBFramesBetweenReferenceFrames': 123,
                                        'NumberReferenceFrames': 123,
                                        'ParControl': 'INITIALIZE_FROM_SOURCE'|'SPECIFIED',
                                        'ParDenominator': 123,
                                        'ParNumerator': 123,
                                        'QualityTuningLevel':
                                        'SINGLE_PASS'
                                        |'SINGLE_PASS_HQ'
                                        |'MULTI_PASS_HQ',
                                        'QvbrSettings': {
                                            'MaxAverageBitrate': 123,
                                            'QvbrQualityLevel': 123
                                        },
                                        'RateControlMode': 'VBR'|'CBR'|'QVBR',
                                        'RepeatPps': 'DISABLED'|'ENABLED',
                                        'SceneChangeDetect':
                                        'DISABLED'|'ENABLED'
                                        |'TRANSITION_DETECTION',
                                        'Slices': 123,
                                        'SlowPal': 'DISABLED'|'ENABLED',
                                        'Softness': 123,
                                        'SpatialAdaptiveQuantization': 'DISABLED'|'ENABLED',
                                        'Syntax': 'DEFAULT'|'RP2027',
                                        'Telecine': 'NONE'|'SOFT'|'HARD',
                                        'TemporalAdaptiveQuantization': 'DISABLED'|'ENABLED',
                                        'UnregisteredSeiTimecode': 'DISABLED'|'ENABLED'
                                    },
                                    'H265Settings': {
                                        'AdaptiveQuantization':
                                        'OFF'|'LOW'|'MEDIUM'|'HIGH'
                                        |'HIGHER'|'MAX',
                                        'AlternateTransferFunctionSei': 'DISABLED'|'ENABLED',
                                        'Bitrate': 123,
                                        'CodecLevel':
                                        'AUTO'|'LEVEL_1'|'LEVEL_2'
                                        |'LEVEL_2_1'|'LEVEL_3'
                                        |'LEVEL_3_1'|'LEVEL_4'
                                        |'LEVEL_4_1'|'LEVEL_5'
                                        |'LEVEL_5_1'|'LEVEL_5_2'
                                        |'LEVEL_6'|'LEVEL_6_1'
                                        |'LEVEL_6_2',
                                        'CodecProfile':
                                        'MAIN_MAIN'|'MAIN_HIGH'
                                        |'MAIN10_MAIN'|'MAIN10_HIGH'
                                        |'MAIN_422_8BIT_MAIN'
                                        |'MAIN_422_8BIT_HIGH'
                                        |'MAIN_422_10BIT_MAIN'
                                        |'MAIN_422_10BIT_HIGH',
                                        'DynamicSubGop': 'ADAPTIVE'|'STATIC',
                                        'FlickerAdaptiveQuantization': 'DISABLED'|'ENABLED',
                                        'FramerateControl': 'INITIALIZE_FROM_SOURCE'|'SPECIFIED',
                                        'FramerateConversionAlgorithm':
                                        'DUPLICATE_DROP'
                                        |'INTERPOLATE',
                                        'FramerateDenominator': 123,
                                        'FramerateNumerator': 123,
                                        'GopBReference': 'DISABLED'|'ENABLED',
                                        'GopClosedCadence': 123,
                                        'GopSize': 123.0,
                                        'GopSizeUnits': 'FRAMES'|'SECONDS',
                                        'HrdBufferInitialFillPercentage': 123,
                                        'HrdBufferSize': 123,
                                        'InterlaceMode':
                                        'PROGRESSIVE'|'TOP_FIELD'
                                        |'BOTTOM_FIELD'
                                        |'FOLLOW_TOP_FIELD'
                                        |'FOLLOW_BOTTOM_FIELD',
                                        'MaxBitrate': 123,
                                        'MinIInterval': 123,
                                        'NumberBFramesBetweenReferenceFrames': 123,
                                        'NumberReferenceFrames': 123,
                                        'ParControl': 'INITIALIZE_FROM_SOURCE'|'SPECIFIED',
                                        'ParDenominator': 123,
                                        'ParNumerator': 123,
                                        'QualityTuningLevel':
                                        'SINGLE_PASS'
                                        |'SINGLE_PASS_HQ'
                                        |'MULTI_PASS_HQ',
                                        'QvbrSettings': {
                                            'MaxAverageBitrate': 123,
                                            'QvbrQualityLevel': 123
                                        },
                                        'RateControlMode': 'VBR'|'CBR'|'QVBR',
                                        'SampleAdaptiveOffsetFilterMode':
                                        'DEFAULT'|'ADAPTIVE'|'OFF',
                                        'SceneChangeDetect':
                                        'DISABLED'|'ENABLED'
                                        |'TRANSITION_DETECTION',
                                        'Slices': 123,
                                        'SlowPal': 'DISABLED'|'ENABLED',
                                        'SpatialAdaptiveQuantization': 'DISABLED'|'ENABLED',
                                        'Telecine': 'NONE'|'SOFT'|'HARD',
                                        'TemporalAdaptiveQuantization': 'DISABLED'|'ENABLED',
                                        'TemporalIds': 'DISABLED'|'ENABLED',
                                        'Tiles': 'DISABLED'|'ENABLED',
                                        'UnregisteredSeiTimecode': 'DISABLED'|'ENABLED',
                                        'WriteMp4PackagingType': 'HVC1'|'HEV1'
                                    },
                                    'Mpeg2Settings': {
                                        'AdaptiveQuantization': 'OFF'|'LOW'|'MEDIUM'|'HIGH',
                                        'Bitrate': 123,
                                        'CodecLevel': 'AUTO'|'LOW'|'MAIN'|'HIGH1440'|'HIGH',
                                        'CodecProfile': 'MAIN'|'PROFILE_422',
                                        'DynamicSubGop': 'ADAPTIVE'|'STATIC',
                                        'FramerateControl': 'INITIALIZE_FROM_SOURCE'|'SPECIFIED',
                                        'FramerateConversionAlgorithm':
                                        'DUPLICATE_DROP'
                                        |'INTERPOLATE',
                                        'FramerateDenominator': 123,
                                        'FramerateNumerator': 123,
                                        'GopClosedCadence': 123,
                                        'GopSize': 123.0,
                                        'GopSizeUnits': 'FRAMES'|'SECONDS',
                                        'HrdBufferInitialFillPercentage': 123,
                                        'HrdBufferSize': 123,
                                        'InterlaceMode':
                                        'PROGRESSIVE'|'TOP_FIELD'
                                        |'BOTTOM_FIELD'
                                        |'FOLLOW_TOP_FIELD'
                                        |'FOLLOW_BOTTOM_FIELD',
                                        'IntraDcPrecision':
                                        'AUTO'
                                        |'INTRA_DC_PRECISION_8'
                                        |'INTRA_DC_PRECISION_9'
                                        |'INTRA_DC_PRECISION_10'
                                        |'INTRA_DC_PRECISION_11',
                                        'MaxBitrate': 123,
                                        'MinIInterval': 123,
                                        'NumberBFramesBetweenReferenceFrames': 123,
                                        'ParControl': 'INITIALIZE_FROM_SOURCE'|'SPECIFIED',
                                        'ParDenominator': 123,
                                        'ParNumerator': 123,
                                        'QualityTuningLevel': 'SINGLE_PASS'|'MULTI_PASS',
                                        'RateControlMode': 'VBR'|'CBR',
                                        'SceneChangeDetect': 'DISABLED'|'ENABLED',
                                        'SlowPal': 'DISABLED'|'ENABLED',
                                        'Softness': 123,
                                        'SpatialAdaptiveQuantization': 'DISABLED'|'ENABLED',
                                        'Syntax': 'DEFAULT'|'D_10',
                                        'Telecine': 'NONE'|'SOFT'|'HARD',
                                        'TemporalAdaptiveQuantization': 'DISABLED'|'ENABLED'
                                    },
                                    'ProresSettings': {
                                        'CodecProfile':
                                        'APPLE_PRORES_422'
                                        |'APPLE_PRORES_422_HQ'
                                        |'APPLE_PRORES_422_LT'
                                        |'APPLE_PRORES_422_PROXY',
                                        'FramerateControl': 'INITIALIZE_FROM_SOURCE'|'SPECIFIED',
                                        'FramerateConversionAlgorithm':
                                        'DUPLICATE_DROP'
                                        |'INTERPOLATE',
                                        'FramerateDenominator': 123,
                                        'FramerateNumerator': 123,
                                        'InterlaceMode':
                                        'PROGRESSIVE'|'TOP_FIELD'
                                        |'BOTTOM_FIELD'
                                        |'FOLLOW_TOP_FIELD'
                                        |'FOLLOW_BOTTOM_FIELD',
                                        'ParControl': 'INITIALIZE_FROM_SOURCE'|'SPECIFIED',
                                        'ParDenominator': 123,
                                        'ParNumerator': 123,
                                        'SlowPal': 'DISABLED'|'ENABLED',
                                        'Telecine': 'NONE'|'HARD'
                                    }
                                },
                                'ColorMetadata': 'IGNORE'|'INSERT',
                                'Crop': {
                                    'Height': 123,
                                    'Width': 123,
                                    'X': 123,
                                    'Y': 123
                                },
                                'DropFrameTimecode': 'DISABLED'|'ENABLED',
                                'FixedAfd': 123,
                                'Height': 123,
                                'Position': {
                                    'Height': 123,
                                    'Width': 123,
                                    'X': 123,
                                    'Y': 123
                                },
                                'RespondToAfd': 'NONE'|'RESPOND'|'PASSTHROUGH',
                                'ScalingBehavior': 'DEFAULT'|'STRETCH_TO_OUTPUT',
                                'Sharpness': 123,
                                'TimecodeInsertion': 'DISABLED'|'PIC_TIMING_SEI',
                                'VideoPreprocessors': {
                                    'ColorCorrector': {
                                        'Brightness': 123,
                                        'ColorSpaceConversion':
                                        'NONE'|'FORCE_601'
                                        |'FORCE_709'|'FORCE_HDR10'
                                        |'FORCE_HLG_2020',
                                        'Contrast': 123,
                                        'Hdr10Metadata': {
                                            'BluePrimaryX': 123,
                                            'BluePrimaryY': 123,
                                            'GreenPrimaryX': 123,
                                            'GreenPrimaryY': 123,
                                            'MaxContentLightLevel': 123,
                                            'MaxFrameAverageLightLevel': 123,
                                            'MaxLuminance': 123,
                                            'MinLuminance': 123,
                                            'RedPrimaryX': 123,
                                            'RedPrimaryY': 123,
                                            'WhitePointX': 123,
                                            'WhitePointY': 123
                                        },
                                        'Hue': 123,
                                        'Saturation': 123
                                    },
                                    'Deinterlacer': {
                                        'Algorithm':
                                        'INTERPOLATE'
                                        |'INTERPOLATE_TICKER'
                                        |'BLEND'|'BLEND_TICKER',
                                        'Control': 'FORCE_ALL_FRAMES'|'NORMAL',
                                        'Mode': 'DEINTERLACE'|'INVERSE_TELECINE'|'ADAPTIVE'
                                    },
                                    'DolbyVision': {
                                        'L6Metadata': {
                                            'MaxCll': 123,
                                            'MaxFall': 123
                                        },
                                        'L6Mode': 'PASSTHROUGH'|'RECALCULATE'|'SPECIFY',
                                        'Profile': 'PROFILE_5'
                                    },
                                    'ImageInserter': {
                                        'InsertableImages': [
                                            {
                                                'Duration': 123,
                                                'FadeIn': 123,
                                                'FadeOut': 123,
                                                'Height': 123,
                                                'ImageInserterInput': 'string',
                                                'ImageX': 123,
                                                'ImageY': 123,
                                                'Layer': 123,
                                                'Opacity': 123,
                                                'StartTime': 'string',
                                                'Width': 123
                                            },
                                        ]
                                    },
                                    'NoiseReducer': {
                                        'Filter':
                                        'BILATERAL'|'MEAN'
                                        |'GAUSSIAN'|'LANCZOS'
                                        |'SHARPEN'|'CONSERVE'
                                        |'SPATIAL'|'TEMPORAL',
                                        'FilterSettings': {
                                            'Strength': 123
                                        },
                                        'SpatialFilterSettings': {
                                            'PostFilterSharpenStrength': 123,
                                            'Speed': 123,
                                            'Strength': 123
                                        },
                                        'TemporalFilterSettings': {
                                            'AggressiveMode': 123,
                                            'Speed': 123,
                                            'Strength': 123
                                        }
                                    },
                                    'TimecodeBurnin': {
                                        'FontSize': 123,
                                        'Position':
                                        'TOP_CENTER'|'TOP_LEFT'
                                        |'TOP_RIGHT'|'MIDDLE_LEFT'
                                        |'MIDDLE_CENTER'
                                        |'MIDDLE_RIGHT'
                                        |'BOTTOM_LEFT'
                                        |'BOTTOM_CENTER'
                                        |'BOTTOM_RIGHT',
                                        'Prefix': 'string'
                                    }
                                },
                                'Width': 123
                            }
                        },
                        'Type': 'SYSTEM'|'CUSTOM'
                    },
                ]
            }
          **Response Structure**

          - *(dict) --*

            - **Presets** *(list) --* List of presets

              - *(dict) --* A preset is a collection of preconfigured media conversion settings that
              you want MediaConvert to apply to the output during the conversion process.

                - **Arn** *(string) --* An identifier for this resource that is unique within all of
                AWS.

                - **Category** *(string) --* An optional category you create to organize your
                presets.

                - **CreatedAt** *(datetime) --* The timestamp in epoch seconds for preset creation.

                - **Description** *(string) --* An optional description you create for each preset.

                - **LastUpdated** *(datetime) --* The timestamp in epoch seconds when the preset was
                last updated.

                - **Name** *(string) --* A name you create for each preset. Each name must be unique
                within your account.

                - **Settings** *(dict) --* Settings for preset

                  - **AudioDescriptions** *(list) --* (AudioDescriptions) contains groups of audio
                  encoding settings organized by audio codec. Include one instance of
                  (AudioDescriptions) per output. (AudioDescriptions) can contain multiple groups of
                  encoding settings.

                    - *(dict) --* Description of audio output

                      - **AudioNormalizationSettings** *(dict) --* Advanced audio normalization
                      settings. Ignore these settings unless you need to comply with a loudness
                      standard.

                        - **Algorithm** *(string) --* Choose one of the following audio
                        normalization algorithms: ITU-R BS.1770-1: Ungated loudness. A measurement
                        of ungated average loudness for an entire piece of content, suitable for
                        measurement of short-form content under ATSC recommendation A/85. Supports
                        up to 5.1 audio channels. ITU-R BS.1770-2: Gated loudness. A measurement of
                        gated average loudness compliant with the requirements of EBU-R128. Supports
                        up to 5.1 audio channels. ITU-R BS.1770-3: Modified peak. The same loudness
                        measurement algorithm as 1770-2, with an updated true peak measurement.
                        ITU-R BS.1770-4: Higher channel count. Allows for more audio channels than
                        the other algorithms, including configurations such as 7.1.

                        - **AlgorithmControl** *(string) --* When enabled the output audio is
                        corrected using the chosen algorithm. If disabled, the audio will be
                        measured but not adjusted.

                        - **CorrectionGateLevel** *(integer) --* Content measuring above this level
                        will be corrected to the target level. Content measuring below this level
                        will not be corrected. Gating only applies when not using
                        real_time_correction.

                        - **LoudnessLogging** *(string) --* If set to LOG, log each output's audio
                        track loudness to a CSV file.

                        - **PeakCalculation** *(string) --* If set to TRUE_PEAK, calculate and log
                        the TruePeak for each output's audio track loudness.

                        - **TargetLkfs** *(float) --* When you use Audio normalization
                        (AudioNormalizationSettings), optionally use this setting to specify a
                        target loudness. If you don't specify a value here, the encoder chooses a
                        value for you, based on the algorithm that you choose for Algorithm
                        (algorithm). If you choose algorithm 1770-1, the encoder will choose -24
                        LKFS; otherwise, the encoder will choose -23 LKFS.

                      - **AudioSourceName** *(string) --* Specifies which audio data to use from
                      each input. In the simplest case, specify an "Audio
                      Selector":#inputs-audio_selector by name based on its order within each input.
                      For example if you specify "Audio Selector 3", then the third audio selector
                      will be used from each input. If an input does not have an "Audio Selector 3",
                      then the audio selector marked as "default" in that input will be used. If
                      there is no audio selector marked as "default", silence will be inserted for
                      the duration of that input. Alternatively, an "Audio Selector
                      Group":#inputs-audio_selector_group name may be specified, with similar
                      default/silence behavior. If no audio_source_name is specified, then "Audio
                      Selector 1" will be chosen automatically.

                      - **AudioType** *(integer) --* Applies only if Follow Input Audio Type is
                      unchecked (false). A number between 0 and 255. The following are defined in
                      ISO-IEC 13818-1: 0 = Undefined, 1 = Clean Effects, 2 =
                           Hearing Impaired, 3 =
                      Visually Impaired Commentary, 4-255 = Reserved.

                      - **AudioTypeControl** *(string) --* When set to FOLLOW_INPUT, if the input
                      contains an ISO 639 audio_type, then that value is passed through to the
                      output. If the input contains no ISO 639 audio_type, the value in Audio Type
                      is included in the output. Otherwise the value in Audio Type is included in
                      the output. Note that this field and audioType are both ignored if
                      audioDescriptionBroadcasterMix is set to BROADCASTER_MIXED_AD.

                      - **CodecSettings** *(dict) --* Audio codec settings (CodecSettings) under
                      (AudioDescriptions) contains the group of settings related to audio encoding.
                      The settings in this group vary depending on the value that you choose for
                      Audio codec (Codec). For each codec enum that you choose, define the
                      corresponding settings object. The following lists the codec enum, settings
                      object pairs. * AAC, AacSettings * MP2, Mp2Settings * WAV, WavSettings * AIFF,
                      AiffSettings * AC3, Ac3Settings * EAC3, Eac3Settings * EAC3_ATMOS,
                      Eac3AtmosSettings

                        - **AacSettings** *(dict) --* Required when you set (Codec) under
                        (AudioDescriptions)>(CodecSettings) to the value AAC. The service accepts
                        one of two mutually exclusive groups of AAC settings--VBR and CBR. To select
                        one of these modes, set the value of Bitrate control mode (rateControlMode)
                        to "VBR" or "CBR". In VBR mode, you control the audio quality with the
                        setting VBR quality (vbrQuality). In CBR mode, you use the setting Bitrate
                        (bitrate). Defaults and valid values depend on the rate control mode.

                          - **AudioDescriptionBroadcasterMix** *(string) --* Choose
                          BROADCASTER_MIXED_AD when the input contains pre-mixed main audio + audio
                          description (AD) as a stereo pair. The value for AudioType will be set to
                          3, which signals to downstream systems that this stream contains
                          "broadcaster mixed AD". Note that the input received by the encoder must
                          contain pre-mixed audio; the encoder does not perform the mixing. When you
                          choose BROADCASTER_MIXED_AD, the encoder ignores any values you provide in
                          AudioType and FollowInputAudioType. Choose NORMAL when the input does not
                          contain pre-mixed audio + audio description (AD). In this case, the
                          encoder will use any values you provide for AudioType and
                          FollowInputAudioType.

                          - **Bitrate** *(integer) --* Specify the average bitrate in bits per
                          second. The set of valid values for this setting is: 6000, 8000, 10000,
                          12000, 14000, 16000, 20000, 24000, 28000, 32000, 40000, 48000, 56000,
                          64000, 80000, 96000, 112000, 128000, 160000, 192000, 224000, 256000,
                          288000, 320000, 384000, 448000, 512000, 576000, 640000, 768000, 896000,
                          1024000. The value you set is also constrained by the values that you
                          choose for Profile (codecProfile), Bitrate control mode (codingMode), and
                          Sample rate (sampleRate). Default values depend on Bitrate control mode
                          and Profile.

                          - **CodecProfile** *(string) --* AAC Profile.

                          - **CodingMode** *(string) --* Mono (Audio Description), Mono, Stereo, or
                          5.1 channel layout. Valid values depend on rate control mode and profile.
                          "1.0 - Audio Description (Receiver Mix)" setting receives a stereo
                          description plus control track and emits a mono AAC encode of the
                          description track, with control data emitted in the PES header as per ETSI
                          TS 101 154 Annex E.

                          - **RateControlMode** *(string) --* Rate Control Mode.

                          - **RawFormat** *(string) --* Enables LATM/LOAS AAC output. Note that if
                          you use LATM/LOAS AAC in an output, you must choose "No container" for the
                          output container.

                          - **SampleRate** *(integer) --* Sample rate in Hz. Valid values depend on
                          rate control mode and profile.

                          - **Specification** *(string) --* Use MPEG-2 AAC instead of MPEG-4 AAC
                          audio for raw or MPEG-2 Transport Stream containers.

                          - **VbrQuality** *(string) --* VBR Quality Level - Only used if
                          rate_control_mode is VBR.

                        - **Ac3Settings** *(dict) --* Required when you set (Codec) under
                        (AudioDescriptions)>(CodecSettings) to the value AC3.

                          - **Bitrate** *(integer) --* Specify the average bitrate in bits per
                          second. Valid bitrates depend on the coding mode.

                          - **BitstreamMode** *(string) --* Specify the bitstream mode for the AC-3
                          stream that the encoder emits. For more information about the AC3
                          bitstream mode, see ATSC A/52-2012 (Annex E).

                          - **CodingMode** *(string) --* Dolby Digital coding mode. Determines
                          number of channels.

                          - **Dialnorm** *(integer) --* Sets the dialnorm for the output. If blank
                          and input audio is Dolby Digital, dialnorm will be passed through.

                          - **DynamicRangeCompressionProfile** *(string) --* If set to
                          FILM_STANDARD, adds dynamic range compression signaling to the output
                          bitstream as defined in the Dolby Digital specification.

                          - **LfeFilter** *(string) --* Applies a 120Hz lowpass filter to the LFE
                          channel prior to encoding. Only valid with 3_2_LFE coding mode.

                          - **MetadataControl** *(string) --* When set to FOLLOW_INPUT, encoder
                          metadata will be sourced from the DD, DD+, or DolbyE decoder that supplied
                          this audio data. If audio was not supplied from one of these streams, then
                          the static metadata settings will be used.

                          - **SampleRate** *(integer) --* This value is always 48000. It represents
                          the sample rate in Hz.

                        - **AiffSettings** *(dict) --* Required when you set (Codec) under
                        (AudioDescriptions)>(CodecSettings) to the value AIFF.

                          - **BitDepth** *(integer) --* Specify Bit depth (BitDepth), in bits per
                          sample, to choose the encoding quality for this audio track.

                          - **Channels** *(integer) --* Specify the number of channels in this
                          output audio track. Valid values are 1 and even numbers up to 64. For
                          example, 1, 2, 4, 6, and so on, up to 64.

                          - **SampleRate** *(integer) --* Sample rate in hz.

                        - **Codec** *(string) --* Type of Audio codec.

                        - **Eac3AtmosSettings** *(dict) --* Required when you set (Codec) under
                        (AudioDescriptions)>(CodecSettings) to the value EAC3_ATMOS.

                          - **Bitrate** *(integer) --* Specify the average bitrate in bits per
                          second. Valid values: 384k, 448k, 640k, 768k

                          - **BitstreamMode** *(string) --* Specify the bitstream mode for the
                          E-AC-3 stream that the encoder emits. For more information about the EAC3
                          bitstream mode, see ATSC A/52-2012 (Annex E).

                          - **CodingMode** *(string) --* The coding mode for Dolby Digital Plus JOC
                          (Atmos) is always 9.1.6 (CODING_MODE_9_1_6).

                          - **DialogueIntelligence** *(string) --* Enable Dolby Dialogue
                          Intelligence to adjust loudness based on dialogue analysis.

                          - **DynamicRangeCompressionLine** *(string) --* Specify the absolute peak
                          level for a signal with dynamic range compression.

                          - **DynamicRangeCompressionRf** *(string) --* Specify how the service
                          limits the audio dynamic range when compressing the audio.

                          - **LoRoCenterMixLevel** *(float) --* Specify a value for the following
                          Dolby Atmos setting: Left only/Right only center mix (Lo/Ro center).
                          MediaConvert uses this value for downmixing. How the service uses this
                          value depends on the value that you choose for Stereo downmix
                          (Eac3AtmosStereoDownmix). Valid values: 3.0, 1.5, 0.0, -1.5, -3.0, -4.5,
                          and -6.0.

                          - **LoRoSurroundMixLevel** *(float) --* Specify a value for the following
                          Dolby Atmos setting: Left only/Right only (Lo/Ro surround). MediaConvert
                          uses this value for downmixing. How the service uses this value depends on
                          the value that you choose for Stereo downmix (Eac3AtmosStereoDownmix).
                          Valid values: -1.5, -3.0, -4.5, -6.0, and -60. The value -60 mutes the
                          channel.

                          - **LtRtCenterMixLevel** *(float) --* Specify a value for the following
                          Dolby Atmos setting: Left total/Right total center mix (Lt/Rt center).
                          MediaConvert uses this value for downmixing. How the service uses this
                          value depends on the value that you choose for Stereo downmix
                          (Eac3AtmosStereoDownmix). Valid values: 3.0, 1.5, 0.0, -1.5, -3.0, -4.5,
                          and -6.0.

                          - **LtRtSurroundMixLevel** *(float) --* Specify a value for the following
                          Dolby Atmos setting: Left total/Right total surround mix (Lt/Rt surround).
                          MediaConvert uses this value for downmixing. How the service uses this
                          value depends on the value that you choose for Stereo downmix
                          (Eac3AtmosStereoDownmix). Valid values: -1.5, -3.0, -4.5, -6.0, and -60.
                          The value -60 mutes the channel.

                          - **MeteringMode** *(string) --* Choose how the service meters the
                          loudness of your audio.

                          - **SampleRate** *(integer) --* This value is always 48000. It represents
                          the sample rate in Hz.

                          - **SpeechThreshold** *(integer) --* Specify the percentage of audio
                          content that must be speech before the encoder uses the measured speech
                          loudness as the overall program loudness.

                          - **StereoDownmix** *(string) --* Choose how the service does stereo
                          downmixing.

                          - **SurroundExMode** *(string) --* Specify whether your input audio has an
                          additional center rear surround channel matrix encoded into your left and
                          right surround channels.

                        - **Eac3Settings** *(dict) --* Required when you set (Codec) under
                        (AudioDescriptions)>(CodecSettings) to the value EAC3.

                          - **AttenuationControl** *(string) --* If set to ATTENUATE_3_DB, applies a
                          3 dB attenuation to the surround channels. Only used for 3/2 coding mode.

                          - **Bitrate** *(integer) --* Specify the average bitrate in bits per
                          second. Valid bitrates depend on the coding mode.

                          - **BitstreamMode** *(string) --* Specify the bitstream mode for the
                          E-AC-3 stream that the encoder emits. For more information about the EAC3
                          bitstream mode, see ATSC A/52-2012 (Annex E).

                          - **CodingMode** *(string) --* Dolby Digital Plus coding mode. Determines
                          number of channels.

                          - **DcFilter** *(string) --* Activates a DC highpass filter for all input
                          channels.

                          - **Dialnorm** *(integer) --* Sets the dialnorm for the output. If blank
                          and input audio is Dolby Digital Plus, dialnorm will be passed through.

                          - **DynamicRangeCompressionLine** *(string) --* Specify the absolute peak
                          level for a signal with dynamic range compression.

                          - **DynamicRangeCompressionRf** *(string) --* Specify how the service
                          limits the audio dynamic range when compressing the audio.

                          - **LfeControl** *(string) --* When encoding 3/2 audio, controls whether
                          the LFE channel is enabled

                          - **LfeFilter** *(string) --* Applies a 120Hz lowpass filter to the LFE
                          channel prior to encoding. Only valid with 3_2_LFE coding mode.

                          - **LoRoCenterMixLevel** *(float) --* Specify a value for the following
                          Dolby Digital Plus setting: Left only/Right only center mix (Lo/Ro
                          center). MediaConvert uses this value for downmixing. How the service uses
                          this value depends on the value that you choose for Stereo downmix
                          (Eac3StereoDownmix). Valid values: 3.0, 1.5, 0.0, -1.5, -3.0, -4.5, -6.0,
                          and -60. The value -60 mutes the channel. This setting applies only if you
                          keep the default value of 3/2 - L, R, C, Ls, Rs (CODING_MODE_3_2) for the
                          setting Coding mode (Eac3CodingMode). If you choose a different value for
                          Coding mode, the service ignores Left only/Right only center
                          (loRoCenterMixLevel).

                          - **LoRoSurroundMixLevel** *(float) --* Specify a value for the following
                          Dolby Digital Plus setting: Left only/Right only (Lo/Ro surround).
                          MediaConvert uses this value for downmixing. How the service uses this
                          value depends on the value that you choose for Stereo downmix
                          (Eac3StereoDownmix). Valid values: -1.5, -3.0, -4.5, -6.0, and -60. The
                          value -60 mutes the channel. This setting applies only if you keep the
                          default value of 3/2 - L, R, C, Ls, Rs (CODING_MODE_3_2) for the setting
                          Coding mode (Eac3CodingMode). If you choose a different value for Coding
                          mode, the service ignores Left only/Right only surround
                          (loRoSurroundMixLevel).

                          - **LtRtCenterMixLevel** *(float) --* Specify a value for the following
                          Dolby Digital Plus setting: Left total/Right total center mix (Lt/Rt
                          center). MediaConvert uses this value for downmixing. How the service uses
                          this value depends on the value that you choose for Stereo downmix
                          (Eac3StereoDownmix). Valid values: 3.0, 1.5, 0.0, -1.5, -3.0, -4.5, -6.0,
                          and -60. The value -60 mutes the channel. This setting applies only if you
                          keep the default value of 3/2 - L, R, C, Ls, Rs (CODING_MODE_3_2) for the
                          setting Coding mode (Eac3CodingMode). If you choose a different value for
                          Coding mode, the service ignores Left total/Right total center
                          (ltRtCenterMixLevel).

                          - **LtRtSurroundMixLevel** *(float) --* Specify a value for the following
                          Dolby Digital Plus setting: Left total/Right total surround mix (Lt/Rt
                          surround). MediaConvert uses this value for downmixing. How the service
                          uses this value depends on the value that you choose for Stereo downmix
                          (Eac3StereoDownmix). Valid values: -1.5, -3.0, -4.5, -6.0, and -60. The
                          value -60 mutes the channel. This setting applies only if you keep the
                          default value of 3/2 - L, R, C, Ls, Rs (CODING_MODE_3_2) for the setting
                          Coding mode (Eac3CodingMode). If you choose a different value for Coding
                          mode, the service ignores Left total/Right total surround
                          (ltRtSurroundMixLevel).

                          - **MetadataControl** *(string) --* When set to FOLLOW_INPUT, encoder
                          metadata will be sourced from the DD, DD+, or DolbyE decoder that supplied
                          this audio data. If audio was not supplied from one of these streams, then
                          the static metadata settings will be used.

                          - **PassthroughControl** *(string) --* When set to WHEN_POSSIBLE, input
                          DD+ audio will be passed through if it is present on the input. this
                          detection is dynamic over the life of the transcode. Inputs that alternate
                          between DD+ and non-DD+ content will have a consistent DD+ output as the
                          system alternates between passthrough and encoding.

                          - **PhaseControl** *(string) --* Controls the amount of phase-shift
                          applied to the surround channels. Only used for 3/2 coding mode.

                          - **SampleRate** *(integer) --* This value is always 48000. It represents
                          the sample rate in Hz.

                          - **StereoDownmix** *(string) --* Choose how the service does stereo
                          downmixing. This setting only applies if you keep the default value of 3/2
                          - L, R, C, Ls, Rs (CODING_MODE_3_2) for the setting Coding mode
                          (Eac3CodingMode). If you choose a different value for Coding mode, the
                          service ignores Stereo downmix (Eac3StereoDownmix).

                          - **SurroundExMode** *(string) --* When encoding 3/2 audio, sets whether
                          an extra center back surround channel is matrix encoded into the left and
                          right surround channels.

                          - **SurroundMode** *(string) --* When encoding 2/0 audio, sets whether
                          Dolby Surround is matrix encoded into the two channels.

                        - **Mp2Settings** *(dict) --* Required when you set (Codec) under
                        (AudioDescriptions)>(CodecSettings) to the value MP2.

                          - **Bitrate** *(integer) --* Specify the average bitrate in bits per
                          second.

                          - **Channels** *(integer) --* Set Channels to specify the number of
                          channels in this output audio track. Choosing Mono in the console will
                          give you 1 output channel; choosing Stereo will give you 2. In the API,
                          valid values are 1 and 2.

                          - **SampleRate** *(integer) --* Sample rate in hz.

                        - **WavSettings** *(dict) --* Required when you set (Codec) under
                        (AudioDescriptions)>(CodecSettings) to the value WAV.

                          - **BitDepth** *(integer) --* Specify Bit depth (BitDepth), in bits per
                          sample, to choose the encoding quality for this audio track.

                          - **Channels** *(integer) --* Specify the number of channels in this
                          output audio track. Valid values are 1 and even numbers up to 64. For
                          example, 1, 2, 4, 6, and so on, up to 64.

                          - **Format** *(string) --* The service defaults to using RIFF for WAV
                          outputs. If your output audio is likely to exceed 4 GB in file size, or if
                          you otherwise need the extended support of the RF64 format, set your
                          output WAV file format to RF64.

                          - **SampleRate** *(integer) --* Sample rate in Hz.

                      - **CustomLanguageCode** *(string) --* Specify the language for this audio
                      output track. The service puts this language code into your output audio track
                      when you set Language code control (AudioLanguageCodeControl) to Use
                      configured (USE_CONFIGURED). The service also uses your specified custom
                      language code when you set Language code control (AudioLanguageCodeControl) to
                      Follow input (FOLLOW_INPUT), but your input file doesn't specify a language
                      code. For all outputs, you can use an ISO 639-2 or ISO 639-3 code. For
                      streaming outputs, you can also use any other code in the full RFC-5646
                      specification. Streaming outputs are those that are in one of the following
                      output groups: CMAF, DASH ISO, Apple HLS, or Microsoft Smooth Streaming.

                      - **LanguageCode** *(string) --* Indicates the language of the audio output
                      track. The ISO 639 language specified in the 'Language Code' drop down will be
                      used when 'Follow Input Language Code' is not selected or when 'Follow Input
                      Language Code' is selected but there is no ISO 639 language code specified by
                      the input.

                      - **LanguageCodeControl** *(string) --* Specify which source for language code
                      takes precedence for this audio track. When you choose Follow input
                      (FOLLOW_INPUT), the service uses the language code from the input track if
                      it's present. If there's no languge code on the input track, the service uses
                      the code that you specify in the setting Language code (languageCode or
                      customLanguageCode). When you choose Use configured (USE_CONFIGURED), the
                      service uses the language code that you specify.

                      - **RemixSettings** *(dict) --* Advanced audio remixing settings.

                        - **ChannelMapping** *(dict) --* Channel mapping (ChannelMapping) contains
                        the group of fields that hold the remixing value for each channel. Units are
                        in dB. Acceptable values are within the range from -60 (mute) through 6. A
                        setting of 0 passes the input channel unchanged to the output channel (no
                        attenuation or amplification).

                          - **OutputChannels** *(list) --* List of output channels

                            - *(dict) --* OutputChannel mapping settings.

                              - **InputChannels** *(list) --* List of input channels

                                - *(integer) --*

                        - **ChannelsIn** *(integer) --* Specify the number of audio channels from
                        your input that you want to use in your output. With remixing, you might
                        combine or split the data in these channels, so the number of channels in
                        your final output might be different.

                        - **ChannelsOut** *(integer) --* Specify the number of channels in this
                        output after remixing. Valid values: 1, 2, 4, 6, 8... 64. (1 and even
                        numbers to 64.)

                      - **StreamName** *(string) --* Specify a label for this output audio stream.
                      For example, "English", "Director commentary", or "track_2". For streaming
                      outputs, MediaConvert passes this information into destination manifests for
                      display on the end-viewer's player device. For outputs in other output groups,
                      the service ignores this setting.

                  - **CaptionDescriptions** *(list) --* Caption settings for this preset. There can
                  be multiple caption settings in a single output.

                    - *(dict) --* Caption Description for preset

                      - **CustomLanguageCode** *(string) --* Specify the language for this captions
                      output track. For most captions output formats, the encoder puts this language
                      information in the output captions metadata. If your output captions format is
                      DVB-Sub or Burn in, the encoder uses this language information when
                      automatically selecting the font script for rendering the captions text. For
                      all outputs, you can use an ISO 639-2 or ISO 639-3 code. For streaming
                      outputs, you can also use any other code in the full RFC-5646 specification.
                      Streaming outputs are those that are in one of the following output groups:
                      CMAF, DASH ISO, Apple HLS, or Microsoft Smooth Streaming.

                      - **DestinationSettings** *(dict) --* Specific settings required by
                      destination type. Note that burnin_destination_settings are not available if
                      the source of the caption data is Embedded or Teletext.

                        - **BurninDestinationSettings** *(dict) --* Burn-In Destination Settings.

                          - **Alignment** *(string) --* If no explicit x_position or y_position is
                          provided, setting alignment to centered will place the captions at the
                          bottom center of the output. Similarly, setting a left alignment will
                          align captions to the bottom left of the output. If x and y positions are
                          given in conjunction with the alignment parameter, the font will be
                          justified (either left or centered) relative to those coordinates. This
                          option is not valid for source captions that are STL, 608/embedded or
                          teletext. These source settings are already pre-defined by the caption
                          stream. All burn-in and DVB-Sub font settings must match.

                          - **BackgroundColor** *(string) --* Specifies the color of the rectangle
                          behind the captions. All burn-in and DVB-Sub font settings must match.

                          - **BackgroundOpacity** *(integer) --* Specifies the opacity of the
                          background rectangle. 255 is opaque; 0 is transparent. Leaving this
                          parameter blank is equivalent to setting it to 0 (transparent). All
                          burn-in and DVB-Sub font settings must match.

                          - **FontColor** *(string) --* Specifies the color of the burned-in
                          captions. This option is not valid for source captions that are STL,
                          608/embedded or teletext. These source settings are already pre-defined by
                          the caption stream. All burn-in and DVB-Sub font settings must match.

                          - **FontOpacity** *(integer) --* Specifies the opacity of the burned-in
                          captions. 255 is opaque; 0 is transparent. All burn-in and DVB-Sub font
                          settings must match.

                          - **FontResolution** *(integer) --* Font resolution in DPI (dots per
                          inch); default is 96 dpi. All burn-in and DVB-Sub font settings must
                          match.

                          - **FontScript** *(string) --* Provide the font script, using an ISO 15924
                          script code, if the LanguageCode is not sufficient for determining the
                          script type. Where LanguageCode or CustomLanguageCode is sufficient, use
                          "AUTOMATIC" or leave unset. This is used to help determine the appropriate
                          font for rendering burn-in captions.

                          - **FontSize** *(integer) --* A positive integer indicates the exact font
                          size in points. Set to 0 for automatic font size selection. All burn-in
                          and DVB-Sub font settings must match.

                          - **OutlineColor** *(string) --* Specifies font outline color. This option
                          is not valid for source captions that are either 608/embedded or teletext.
                          These source settings are already pre-defined by the caption stream. All
                          burn-in and DVB-Sub font settings must match.

                          - **OutlineSize** *(integer) --* Specifies font outline size in pixels.
                          This option is not valid for source captions that are either 608/embedded
                          or teletext. These source settings are already pre-defined by the caption
                          stream. All burn-in and DVB-Sub font settings must match.

                          - **ShadowColor** *(string) --* Specifies the color of the shadow cast by
                          the captions. All burn-in and DVB-Sub font settings must match.

                          - **ShadowOpacity** *(integer) --* Specifies the opacity of the shadow.
                          255 is opaque; 0 is transparent. Leaving this parameter blank is
                          equivalent to setting it to 0 (transparent). All burn-in and DVB-Sub font
                          settings must match.

                          - **ShadowXOffset** *(integer) --* Specifies the horizontal offset of the
                          shadow relative to the captions in pixels. A value of -2 would result in a
                          shadow offset 2 pixels to the left. All burn-in and DVB-Sub font settings
                          must match.

                          - **ShadowYOffset** *(integer) --* Specifies the vertical offset of the
                          shadow relative to the captions in pixels. A value of -2 would result in a
                          shadow offset 2 pixels above the text. All burn-in and DVB-Sub font
                          settings must match.

                          - **TeletextSpacing** *(string) --* Only applies to jobs with input
                          captions in Teletext or STL formats. Specify whether the spacing between
                          letters in your captions is set by the captions grid or varies depending
                          on letter width. Choose fixed grid to conform to the spacing specified in
                          the captions file more accurately. Choose proportional to make the text
                          easier to read if the captions are closed caption.

                          - **XPosition** *(integer) --* Specifies the horizontal position of the
                          caption relative to the left side of the output in pixels. A value of 10
                          would result in the captions starting 10 pixels from the left of the
                          output. If no explicit x_position is provided, the horizontal caption
                          position will be determined by the alignment parameter. This option is not
                          valid for source captions that are STL, 608/embedded or teletext. These
                          source settings are already pre-defined by the caption stream. All burn-in
                          and DVB-Sub font settings must match.

                          - **YPosition** *(integer) --* Specifies the vertical position of the
                          caption relative to the top of the output in pixels. A value of 10 would
                          result in the captions starting 10 pixels from the top of the output. If
                          no explicit y_position is provided, the caption will be positioned towards
                          the bottom of the output. This option is not valid for source captions
                          that are STL, 608/embedded or teletext. These source settings are already
                          pre-defined by the caption stream. All burn-in and DVB-Sub font settings
                          must match.

                        - **DestinationType** *(string) --* Specify the format for this set of
                        captions on this output. The default format is embedded without SCTE-20.
                        Other options are embedded with SCTE-20, burn-in, DVB-sub, IMSC, SCC, SRT,
                        teletext, TTML, and web-VTT. If you are using SCTE-20, choose SCTE-20 plus
                        embedded (SCTE20_PLUS_EMBEDDED) to create an output that complies with the
                        SCTE-43 spec. To create a non-compliant output where the embedded captions
                        come first, choose Embedded plus SCTE-20 (EMBEDDED_PLUS_SCTE20).

                        - **DvbSubDestinationSettings** *(dict) --* DVB-Sub Destination Settings

                          - **Alignment** *(string) --* If no explicit x_position or y_position is
                          provided, setting alignment to centered will place the captions at the
                          bottom center of the output. Similarly, setting a left alignment will
                          align captions to the bottom left of the output. If x and y positions are
                          given in conjunction with the alignment parameter, the font will be
                          justified (either left or centered) relative to those coordinates. This
                          option is not valid for source captions that are STL, 608/embedded or
                          teletext. These source settings are already pre-defined by the caption
                          stream. All burn-in and DVB-Sub font settings must match.

                          - **BackgroundColor** *(string) --* Specifies the color of the rectangle
                          behind the captions. All burn-in and DVB-Sub font settings must match.

                          - **BackgroundOpacity** *(integer) --* Specifies the opacity of the
                          background rectangle. 255 is opaque; 0 is transparent. Leaving this
                          parameter blank is equivalent to setting it to 0 (transparent). All
                          burn-in and DVB-Sub font settings must match.

                          - **FontColor** *(string) --* Specifies the color of the burned-in
                          captions. This option is not valid for source captions that are STL,
                          608/embedded or teletext. These source settings are already pre-defined by
                          the caption stream. All burn-in and DVB-Sub font settings must match.

                          - **FontOpacity** *(integer) --* Specifies the opacity of the burned-in
                          captions. 255 is opaque; 0 is transparent. All burn-in and DVB-Sub font
                          settings must match.

                          - **FontResolution** *(integer) --* Font resolution in DPI (dots per
                          inch); default is 96 dpi. All burn-in and DVB-Sub font settings must
                          match.

                          - **FontScript** *(string) --* Provide the font script, using an ISO 15924
                          script code, if the LanguageCode is not sufficient for determining the
                          script type. Where LanguageCode or CustomLanguageCode is sufficient, use
                          "AUTOMATIC" or leave unset. This is used to help determine the appropriate
                          font for rendering DVB-Sub captions.

                          - **FontSize** *(integer) --* A positive integer indicates the exact font
                          size in points. Set to 0 for automatic font size selection. All burn-in
                          and DVB-Sub font settings must match.

                          - **OutlineColor** *(string) --* Specifies font outline color. This option
                          is not valid for source captions that are either 608/embedded or teletext.
                          These source settings are already pre-defined by the caption stream. All
                          burn-in and DVB-Sub font settings must match.

                          - **OutlineSize** *(integer) --* Specifies font outline size in pixels.
                          This option is not valid for source captions that are either 608/embedded
                          or teletext. These source settings are already pre-defined by the caption
                          stream. All burn-in and DVB-Sub font settings must match.

                          - **ShadowColor** *(string) --* Specifies the color of the shadow cast by
                          the captions. All burn-in and DVB-Sub font settings must match.

                          - **ShadowOpacity** *(integer) --* Specifies the opacity of the shadow.
                          255 is opaque; 0 is transparent. Leaving this parameter blank is
                          equivalent to setting it to 0 (transparent). All burn-in and DVB-Sub font
                          settings must match.

                          - **ShadowXOffset** *(integer) --* Specifies the horizontal offset of the
                          shadow relative to the captions in pixels. A value of -2 would result in a
                          shadow offset 2 pixels to the left. All burn-in and DVB-Sub font settings
                          must match.

                          - **ShadowYOffset** *(integer) --* Specifies the vertical offset of the
                          shadow relative to the captions in pixels. A value of -2 would result in a
                          shadow offset 2 pixels above the text. All burn-in and DVB-Sub font
                          settings must match.

                          - **SubtitlingType** *(string) --* Specify whether your DVB subtitles are
                          standard or for hearing impaired. Choose hearing impaired if your
                          subtitles include audio descriptions and dialogue. Choose standard if your
                          subtitles include only dialogue.

                          - **TeletextSpacing** *(string) --* Only applies to jobs with input
                          captions in Teletext or STL formats. Specify whether the spacing between
                          letters in your captions is set by the captions grid or varies depending
                          on letter width. Choose fixed grid to conform to the spacing specified in
                          the captions file more accurately. Choose proportional to make the text
                          easier to read if the captions are closed caption.

                          - **XPosition** *(integer) --* Specifies the horizontal position of the
                          caption relative to the left side of the output in pixels. A value of 10
                          would result in the captions starting 10 pixels from the left of the
                          output. If no explicit x_position is provided, the horizontal caption
                          position will be determined by the alignment parameter. This option is not
                          valid for source captions that are STL, 608/embedded or teletext. These
                          source settings are already pre-defined by the caption stream. All burn-in
                          and DVB-Sub font settings must match.

                          - **YPosition** *(integer) --* Specifies the vertical position of the
                          caption relative to the top of the output in pixels. A value of 10 would
                          result in the captions starting 10 pixels from the top of the output. If
                          no explicit y_position is provided, the caption will be positioned towards
                          the bottom of the output. This option is not valid for source captions
                          that are STL, 608/embedded or teletext. These source settings are already
                          pre-defined by the caption stream. All burn-in and DVB-Sub font settings
                          must match.

                        - **EmbeddedDestinationSettings** *(dict) --* Settings specific to
                        embedded/ancillary caption outputs, including 608/708 Channel destination
                        number.

                          - **Destination608ChannelNumber** *(integer) --* Ignore this setting
                          unless your input captions are SCC format and your output captions are
                          embedded in the video stream. Specify a CC number for each captions
                          channel in this output. If you have two channels, choose CC numbers that
                          aren't in the same field. For example, choose 1 and 3. For more
                          information, see
                          https://docs.aws.amazon.com/console/mediaconvert/dual-scc-to-embedded.

                          - **Destination708ServiceNumber** *(integer) --* Ignore this setting
                          unless your input captions are SCC format and you want both 608 and 708
                          captions embedded in your output stream. Optionally, specify the 708
                          service number for each output captions channel. Choose a different number
                          for each channel. To use this setting, also set Force 608 to 708 upconvert
                          (Convert608To708) to Upconvert (UPCONVERT) in your input captions selector
                          settings. If you choose to upconvert but don't specify a 708 service
                          number, MediaConvert uses the number that you specify for CC channel
                          number (destination608ChannelNumber) for the 708 service number. For more
                          information, see
                          https://docs.aws.amazon.com/console/mediaconvert/dual-scc-to-embedded.

                        - **ImscDestinationSettings** *(dict) --* Settings specific to IMSC caption
                        outputs.

                          - **StylePassthrough** *(string) --* Keep this setting enabled to have
                          MediaConvert use the font style and position information from the captions
                          source in the output. This option is available only when your input
                          captions are CFF-TT, IMSC, SMPTE-TT, or TTML. Disable this setting for
                          simplified output captions.

                        - **SccDestinationSettings** *(dict) --* Settings for SCC caption output.

                          - **Framerate** *(string) --* Set Framerate (SccDestinationFramerate) to
                          make sure that the captions and the video are synchronized in the output.
                          Specify a frame rate that matches the frame rate of the associated video.
                          If the video frame rate is 29.97, choose 29.97 dropframe
                          (FRAMERATE_29_97_DROPFRAME) only if the video has video_insertion=true and
                          drop_frame_timecode=
                              true; otherwise, choose 29.97 non-dropframe
                          (FRAMERATE_29_97_NON_DROPFRAME).

                        - **TeletextDestinationSettings** *(dict) --* Settings for Teletext caption
                        output

                          - **PageNumber** *(string) --* Set pageNumber to the Teletext page number
                          for the destination captions for this output. This value must be a
                          three-digit hexadecimal string; strings ending in -FF are invalid. If you
                          are passing through the entire set of Teletext data, do not use this
                          field.

                          - **PageTypes** *(list) --* Specify the page types for this Teletext page.
                          If you don't specify a value here, the service sets the page type to the
                          default value Subtitle (PAGE_TYPE_SUBTITLE). If you pass through the
                          entire set of Teletext data, don't use this field. When you pass through a
                          set of Teletext pages, your output has the same page types as your input.

                            - *(string) --* A page type as defined in the standard ETSI EN 300 468,
                            Table 94

                        - **TtmlDestinationSettings** *(dict) --* Settings specific to TTML caption
                        outputs, including Pass style information (TtmlStylePassthrough).

                          - **StylePassthrough** *(string) --* Pass through style and position
                          information from a TTML-like input source (TTML, SMPTE-TT, CFF-TT) to the
                          CFF-TT output or TTML output.

                      - **LanguageCode** *(string) --* Specify the language of this captions output
                      track. For most captions output formats, the encoder puts this language
                      information in the output captions metadata. If your output captions format is
                      DVB-Sub or Burn in, the encoder uses this language information to choose the
                      font language for rendering the captions text.

                      - **LanguageDescription** *(string) --* Specify a label for this set of output
                      captions. For example, "English", "Director commentary", or "track_2". For
                      streaming outputs, MediaConvert passes this information into destination
                      manifests for display on the end-viewer's player device. For outputs in other
                      output groups, the service ignores this setting.

                  - **ContainerSettings** *(dict) --* Container specific settings.

                    - **Container** *(string) --* Container for this output. Some containers require
                    a container settings object. If not specified, the default object will be
                    created.

                    - **F4vSettings** *(dict) --* Settings for F4v container

                      - **MoovPlacement** *(string) --* If set to PROGRESSIVE_DOWNLOAD, the MOOV
                      atom is relocated to the beginning of the archive as required for progressive
                      downloading. Otherwise it is placed normally at the end.

                    - **M2tsSettings** *(dict) --* MPEG-2 TS container settings. These apply to
                    outputs in a File output group when the output's container (ContainerType) is
                    MPEG-2 Transport Stream (M2TS). In these assets, data is organized by the
                    program map table (PMT). Each transport stream program contains subsets of data,
                    including audio, video, and metadata. Each of these subsets of data has a
                    numerical label called a packet identifier (PID). Each transport stream program
                    corresponds to one MediaConvert output. The PMT lists the types of data in a
                    program along with their PID. Downstream systems and players use the program map
                    table to look up the PID for each type of data it accesses and then uses the
                    PIDs to locate specific data within the asset.

                      - **AudioBufferModel** *(string) --* Selects between the DVB and ATSC buffer
                      models for Dolby Digital audio.

                      - **AudioFramesPerPes** *(integer) --* The number of audio frames to insert
                      for each PES packet.

                      - **AudioPids** *(list) --* Specify the packet identifiers (PIDs) for any
                      elementary audio streams you include in this output. Specify multiple PIDs as
                      a JSON array. Default is the range 482-492.

                        - *(integer) --*

                      - **Bitrate** *(integer) --* Specify the output bitrate of the transport
                      stream in bits per second. Setting to 0 lets the muxer automatically determine
                      the appropriate bitrate. Other common values are 3750000, 7500000, and
                      15000000.

                      - **BufferModel** *(string) --* Controls what buffer model to use for accurate
                      interleaving. If set to MULTIPLEX, use multiplex buffer model. If set to NONE,
                      this can lead to lower latency, but low-memory devices may not be able to play
                      back the stream without interruptions.

                      - **DvbNitSettings** *(dict) --* Inserts DVB Network Information Table (NIT)
                      at the specified table repetition interval.

                        - **NetworkId** *(integer) --* The numeric value placed in the Network
                        Information Table (NIT).

                        - **NetworkName** *(string) --* The network name text placed in the
                        network_name_descriptor inside the Network Information Table. Maximum length
                        is 256 characters.

                        - **NitInterval** *(integer) --* The number of milliseconds between
                        instances of this table in the output transport stream.

                      - **DvbSdtSettings** *(dict) --* Inserts DVB Service Description Table (NIT)
                      at the specified table repetition interval.

                        - **OutputSdt** *(string) --* Selects method of inserting SDT information
                        into output stream. "Follow input SDT" copies SDT information from input
                        stream to output stream. "Follow input SDT if present" copies SDT
                        information from input stream to output stream if SDT information is present
                        in the input, otherwise it will fall back on the user-defined values. Enter
                        "SDT Manually" means user will enter the SDT information. "No SDT" means
                        output stream will not contain SDT information.

                        - **SdtInterval** *(integer) --* The number of milliseconds between
                        instances of this table in the output transport stream.

                        - **ServiceName** *(string) --* The service name placed in the
                        service_descriptor in the Service Description Table. Maximum length is 256
                        characters.

                        - **ServiceProviderName** *(string) --* The service provider name placed in
                        the service_descriptor in the Service Description Table. Maximum length is
                        256 characters.

                      - **DvbSubPids** *(list) --* Specify the packet identifiers (PIDs) for DVB
                      subtitle data included in this output. Specify multiple PIDs as a JSON array.
                      Default is the range 460-479.

                        - *(integer) --*

                      - **DvbTdtSettings** *(dict) --* Inserts DVB Time and Date Table (TDT) at the
                      specified table repetition interval.

                        - **TdtInterval** *(integer) --* The number of milliseconds between
                        instances of this table in the output transport stream.

                      - **DvbTeletextPid** *(integer) --* Specify the packet identifier (PID) for
                      DVB teletext data you include in this output. Default is 499.

                      - **EbpAudioInterval** *(string) --* When set to VIDEO_AND_FIXED_INTERVALS,
                      audio EBP markers will be added to partitions 3 and 4. The interval between
                      these additional markers will be fixed, and will be slightly shorter than the
                      video EBP marker interval. When set to VIDEO_INTERVAL, these additional
                      markers will not be inserted. Only applicable when EBP segmentation markers
                      are is selected (segmentationMarkers is EBP or EBP_LEGACY).

                      - **EbpPlacement** *(string) --* Selects which PIDs to place EBP markers on.
                      They can either be placed only on the video PID, or on both the video PID and
                      all audio PIDs. Only applicable when EBP segmentation markers are is selected
                      (segmentationMarkers is EBP or EBP_LEGACY).

                      - **EsRateInPes** *(string) --* Controls whether to include the ES Rate field
                      in the PES header.

                      - **ForceTsVideoEbpOrder** *(string) --* Keep the default value (DEFAULT)
                      unless you know that your audio EBP markers are incorrectly appearing before
                      your video EBP markers. To correct this problem, set this value to Force
                      (FORCE).

                      - **FragmentTime** *(float) --* The length, in seconds, of each fragment. Only
                      used with EBP markers.

                      - **MaxPcrInterval** *(integer) --* Specify the maximum time, in milliseconds,
                      between Program Clock References (PCRs) inserted into the transport stream.

                      - **MinEbpInterval** *(integer) --* When set, enforces that Encoder Boundary
                      Points do not come within the specified time interval of each other by looking
                      ahead at input video. If another EBP is going to come in within the specified
                      time interval, the current EBP is not emitted, and the segment is "stretched"
                      to the next marker. The lookahead value does not add latency to the system.
                      The Live Event must be configured elsewhere to create sufficient latency to
                      make the lookahead accurate.

                      - **NielsenId3** *(string) --* If INSERT, Nielsen inaudible tones for media
                      tracking will be detected in the input audio and an equivalent ID3 tag will be
                      inserted in the output.

                      - **NullPacketBitrate** *(float) --* Value in bits per second of extra null
                      packets to insert into the transport stream. This can be used if a downstream
                      encryption system requires periodic null packets.

                      - **PatInterval** *(integer) --* The number of milliseconds between instances
                      of this table in the output transport stream.

                      - **PcrControl** *(string) --* When set to PCR_EVERY_PES_PACKET, a Program
                      Clock Reference value is inserted for every Packetized Elementary Stream (PES)
                      header. This is effective only when the PCR PID is the same as the video or
                      audio elementary stream.

                      - **PcrPid** *(integer) --* Specify the packet identifier (PID) for the
                      program clock reference (PCR) in this output. If you do not specify a value,
                      the service will use the value for Video PID (VideoPid).

                      - **PmtInterval** *(integer) --* Specify the number of milliseconds between
                      instances of the program map table (PMT) in the output transport stream.

                      - **PmtPid** *(integer) --* Specify the packet identifier (PID) for the
                      program map table (PMT) itself. Default is 480.

                      - **PrivateMetadataPid** *(integer) --* Specify the packet identifier (PID) of
                      the private metadata stream. Default is 503.

                      - **ProgramNumber** *(integer) --* Use Program number (programNumber) to
                      specify the program number used in the program map table (PMT) for this
                      output. Default is 1. Program numbers and program map tables are parts of
                      MPEG-2 transport stream containers, used for organizing data.

                      - **RateMode** *(string) --* When set to CBR, inserts null packets into
                      transport stream to fill specified bitrate. When set to VBR, the bitrate
                      setting acts as the maximum bitrate, but the output will not be padded up to
                      that bitrate.

                      - **Scte35Esam** *(dict) --* Include this in your job settings to put SCTE-35
                      markers in your HLS and transport stream outputs at the insertion points that
                      you specify in an ESAM XML document. Provide the document in the setting SCC
                      XML (sccXml).

                        - **Scte35EsamPid** *(integer) --* Packet Identifier (PID) of the SCTE-35
                        stream in the transport stream generated by ESAM.

                      - **Scte35Pid** *(integer) --* Specify the packet identifier (PID) of the
                      SCTE-35 stream in the transport stream.

                      - **Scte35Source** *(string) --* For SCTE-35 markers from your input-- Choose
                      Passthrough (PASSTHROUGH) if you want SCTE-35 markers that appear in your
                      input to also appear in this output. Choose None (NONE) if you don't want
                      SCTE-35 markers in this output. For SCTE-35 markers from an ESAM XML
                      document-- Choose None (NONE). Also provide the ESAM XML as a string in the
                      setting Signal processing notification XML (sccXml). Also enable ESAM SCTE-35
                      (include the property scte35Esam).

                      - **SegmentationMarkers** *(string) --* Inserts segmentation markers at each
                      segmentation_time period. rai_segstart sets the Random Access Indicator bit in
                      the adaptation field. rai_adapt sets the RAI bit and adds the current timecode
                      in the private data bytes. psi_segstart inserts PAT and PMT tables at the
                      start of segments. ebp adds Encoder Boundary Point information to the
                      adaptation field as per OpenCable specification OC-SP-EBP-I01-130118.
                      ebp_legacy adds Encoder Boundary Point information to the adaptation field
                      using a legacy proprietary format.

                      - **SegmentationStyle** *(string) --* The segmentation style parameter
                      controls how segmentation markers are inserted into the transport stream. With
                      avails, it is possible that segments may be truncated, which can influence
                      where future segmentation markers are inserted. When a segmentation style of
                      "reset_cadence" is selected and a segment is truncated due to an avail, we
                      will reset the segmentation cadence. This means the subsequent segment will
                      have a duration of of $segmentation_time seconds. When a segmentation style of
                      "maintain_cadence" is selected and a segment is truncated due to an avail, we
                      will not reset the segmentation cadence. This means the subsequent segment
                      will likely be truncated as well. However, all segments after that will have a
                      duration of $segmentation_time seconds. Note that EBP lookahead is a slight
                      exception to this rule.

                      - **SegmentationTime** *(float) --* Specify the length, in seconds, of each
                      segment. Required unless markers is set to _none_.

                      - **TimedMetadataPid** *(integer) --* Specify the packet identifier (PID) for
                      timed metadata in this output. Default is 502.

                      - **TransportStreamId** *(integer) --* Specify the ID for the transport stream
                      itself in the program map table for this output. Transport stream IDs and
                      program map tables are parts of MPEG-2 transport stream containers, used for
                      organizing data.

                      - **VideoPid** *(integer) --* Specify the packet identifier (PID) of the
                      elementary video stream in the transport stream.

                    - **M3u8Settings** *(dict) --* Settings for TS segments in HLS

                      - **AudioFramesPerPes** *(integer) --* The number of audio frames to insert
                      for each PES packet.

                      - **AudioPids** *(list) --* Packet Identifier (PID) of the elementary audio
                      stream(s) in the transport stream. Multiple values are accepted, and can be
                      entered in ranges and/or by comma separation.

                        - *(integer) --*

                      - **NielsenId3** *(string) --* If INSERT, Nielsen inaudible tones for media
                      tracking will be detected in the input audio and an equivalent ID3 tag will be
                      inserted in the output.

                      - **PatInterval** *(integer) --* The number of milliseconds between instances
                      of this table in the output transport stream.

                      - **PcrControl** *(string) --* When set to PCR_EVERY_PES_PACKET a Program
                      Clock Reference value is inserted for every Packetized Elementary Stream (PES)
                      header. This parameter is effective only when the PCR PID is the same as the
                      video or audio elementary stream.

                      - **PcrPid** *(integer) --* Packet Identifier (PID) of the Program Clock
                      Reference (PCR) in the transport stream. When no value is given, the encoder
                      will assign the same value as the Video PID.

                      - **PmtInterval** *(integer) --* The number of milliseconds between instances
                      of this table in the output transport stream.

                      - **PmtPid** *(integer) --* Packet Identifier (PID) for the Program Map Table
                      (PMT) in the transport stream.

                      - **PrivateMetadataPid** *(integer) --* Packet Identifier (PID) of the private
                      metadata stream in the transport stream.

                      - **ProgramNumber** *(integer) --* The value of the program number field in
                      the Program Map Table.

                      - **Scte35Pid** *(integer) --* Packet Identifier (PID) of the SCTE-35 stream
                      in the transport stream.

                      - **Scte35Source** *(string) --* For SCTE-35 markers from your input-- Choose
                      Passthrough (PASSTHROUGH) if you want SCTE-35 markers that appear in your
                      input to also appear in this output. Choose None (NONE) if you don't want
                      SCTE-35 markers in this output. For SCTE-35 markers from an ESAM XML
                      document-- Choose None (NONE) if you don't want manifest conditioning. Choose
                      Passthrough (PASSTHROUGH) and choose Ad markers (adMarkers) if you do want
                      manifest conditioning. In both cases, also provide the ESAM XML as a string in
                      the setting Signal processing notification XML (sccXml).

                      - **TimedMetadata** *(string) --* Applies only to HLS outputs. Use this
                      setting to specify whether the service inserts the ID3 timed metadata from the
                      input in this output.

                      - **TimedMetadataPid** *(integer) --* Packet Identifier (PID) of the timed
                      metadata stream in the transport stream.

                      - **TransportStreamId** *(integer) --* The value of the transport stream ID
                      field in the Program Map Table.

                      - **VideoPid** *(integer) --* Packet Identifier (PID) of the elementary video
                      stream in the transport stream.

                    - **MovSettings** *(dict) --* Settings for MOV Container.

                      - **ClapAtom** *(string) --* When enabled, include 'clap' atom if appropriate
                      for the video output settings.

                      - **CslgAtom** *(string) --* When enabled, file composition times will start
                      at zero, composition times in the 'ctts' (composition time to sample) box for
                      B-frames will be negative, and a 'cslg' (composition shift least greatest) box
                      will be included per 14496-1 amendment 1. This improves compatibility with
                      Apple players and tools.

                      - **Mpeg2FourCCControl** *(string) --* When set to XDCAM, writes MPEG2 video
                      streams into the QuickTime file using XDCAM fourcc codes. This increases
                      compatibility with Apple editors and players, but may decrease compatibility
                      with other players. Only applicable when the video codec is MPEG2.

                      - **PaddingControl** *(string) --* If set to OMNEON, inserts Omneon-compatible
                      padding

                      - **Reference** *(string) --* Always keep the default value (SELF_CONTAINED)
                      for this setting.

                    - **Mp4Settings** *(dict) --* Settings for MP4 container. You can create
                    audio-only AAC outputs with this container.

                      - **CslgAtom** *(string) --* When enabled, file composition times will start
                      at zero, composition times in the 'ctts' (composition time to sample) box for
                      B-frames will be negative, and a 'cslg' (composition shift least greatest) box
                      will be included per 14496-1 amendment 1. This improves compatibility with
                      Apple players and tools.

                      - **FreeSpaceBox** *(string) --* Inserts a free-space box immediately after
                      the moov box.

                      - **MoovPlacement** *(string) --* If set to PROGRESSIVE_DOWNLOAD, the MOOV
                      atom is relocated to the beginning of the archive as required for progressive
                      downloading. Otherwise it is placed normally at the end.

                      - **Mp4MajorBrand** *(string) --* Overrides the "Major Brand" field in the
                      output file. Usually not necessary to specify.

                    - **MpdSettings** *(dict) --* Settings for MP4 segments in DASH

                      - **CaptionContainerType** *(string) --* Use this setting only in DASH output
                      groups that include sidecar TTML or IMSC captions. You specify sidecar
                      captions in a separate output from your audio and video. Choose Raw (RAW) for
                      captions in a single XML file in a raw container. Choose Fragmented MPEG-4
                      (FRAGMENTED_MP4) for captions in XML format contained within fragmented MP4
                      files. This set of fragmented MP4 files is separate from your video and audio
                      fragmented MP4 files.

                      - **Scte35Esam** *(string) --* Use this setting only when you specify SCTE-35
                      markers from ESAM. Choose INSERT to put SCTE-35 markers in this output at the
                      insertion points that you specify in an ESAM XML document. Provide the
                      document in the setting SCC XML (sccXml).

                      - **Scte35Source** *(string) --* Ignore this setting unless you have SCTE-35
                      markers in your input video file. Choose Passthrough (PASSTHROUGH) if you want
                      SCTE-35 markers that appear in your input to also appear in this output.
                      Choose None (NONE) if you don't want those SCTE-35 markers in this output.

                  - **VideoDescription** *(dict) --* (VideoDescription) contains a group of video
                  encoding settings. The specific video settings depend on the video codec that you
                  choose when you specify a value for Video codec (codec). Include one instance of
                  (VideoDescription) per output.

                    - **AfdSignaling** *(string) --* This setting only applies to H.264, H.265, and
                    MPEG2 outputs. Use Insert AFD signaling (AfdSignaling) to specify whether the
                    service includes AFD values in the output video data and what those values are.
                    * Choose None to remove all AFD values from this output. * Choose Fixed to
                    ignore input AFD values and instead encode the value specified in the job. *
                    Choose Auto to calculate output AFD values based on the input AFD scaler data.

                    - **AntiAlias** *(string) --* The anti-alias filter is automatically applied to
                    all outputs. The service no longer accepts the value DISABLED for AntiAlias. If
                    you specify that in your job, the service will ignore the setting.

                    - **CodecSettings** *(dict) --* Video codec settings, (CodecSettings) under
                    (VideoDescription), contains the group of settings related to video encoding.
                    The settings in this group vary depending on the value that you choose for Video
                    codec (Codec). For each codec enum that you choose, define the corresponding
                    settings object. The following lists the codec enum, settings object pairs. *
                    H_264, H264Settings * H_265, H265Settings * MPEG2, Mpeg2Settings * PRORES,
                    ProresSettings * FRAME_CAPTURE, FrameCaptureSettings

                      - **Codec** *(string) --* Specifies the video codec. This must be equal to one
                      of the enum values defined by the object VideoCodec.

                      - **FrameCaptureSettings** *(dict) --* Required when you set (Codec) under
                      (VideoDescription)>(CodecSettings) to the value FRAME_CAPTURE.

                        - **FramerateDenominator** *(integer) --* Frame capture will encode the
                        first frame of the output stream, then one frame every
                        framerateDenominator/framerateNumerator seconds. For example, settings of
                        framerateNumerator = 1 and framerateDenominator =
                             3 (a rate of 1/3 frame per
                        second) will capture the first frame, then 1 frame every 3s. Files will be
                        named as filename.n.jpg where n is the 0-based sequence number of each
                        Capture.

                        - **FramerateNumerator** *(integer) --* Frame capture will encode the first
                        frame of the output stream, then one frame every
                        framerateDenominator/framerateNumerator seconds. For example, settings of
                        framerateNumerator = 1 and framerateDenominator =
                             3 (a rate of 1/3 frame per
                        second) will capture the first frame, then 1 frame every 3s. Files will be
                        named as filename.NNNNNNN.jpg where N is the 0-based frame sequence number
                        zero padded to 7 decimal places.

                        - **MaxCaptures** *(integer) --* Maximum number of captures (encoded jpg
                        output files).

                        - **Quality** *(integer) --* JPEG Quality - a higher value equals higher
                        quality.

                      - **H264Settings** *(dict) --* Required when you set (Codec) under
                      (VideoDescription)>(CodecSettings) to the value H_264.

                        - **AdaptiveQuantization** *(string) --* Adaptive quantization. Allows
                        intra-frame quantizers to vary to improve visual quality.

                        - **Bitrate** *(integer) --* Specify the average bitrate in bits per second.
                        Required for VBR and CBR. For MS Smooth outputs, bitrates must be unique
                        when rounded down to the nearest multiple of 1000.

                        - **CodecLevel** *(string) --* Specify an H.264 level that is consistent
                        with your output video settings. If you aren't sure what level to specify,
                        choose Auto (AUTO).

                        - **CodecProfile** *(string) --* H.264 Profile. High 4:2:2 and 10-bit
                        profiles are only available with the AVC-I License.

                        - **DynamicSubGop** *(string) --* Choose Adaptive to improve subjective
                        video quality for high-motion content. This will cause the service to use
                        fewer B-frames (which infer information based on other frames) for
                        high-motion portions of the video and more B-frames for low-motion portions.
                        The maximum number of B-frames is limited by the value you provide for the
                        setting B frames between reference frames
                        (numberBFramesBetweenReferenceFrames).

                        - **EntropyEncoding** *(string) --* Entropy encoding mode. Use CABAC (must
                        be in Main or High profile) or CAVLC.

                        - **FieldEncoding** *(string) --* Choosing FORCE_FIELD disables PAFF
                        encoding for interlaced outputs.

                        - **FlickerAdaptiveQuantization** *(string) --* Adjust quantization within
                        each frame to reduce flicker or 'pop' on I-frames.

                        - **FramerateControl** *(string) --* If you are using the console, use the
                        Framerate setting to specify the frame rate for this output. If you want to
                        keep the same frame rate as the input video, choose Follow source. If you
                        want to do frame rate conversion, choose a frame rate from the dropdown list
                        or choose Custom. The framerates shown in the dropdown list are decimal
                        approximations of fractions. If you choose Custom, specify your frame rate
                        as a fraction. If you are creating your transcoding job specification as a
                        JSON file without the console, use FramerateControl to specify which value
                        the service uses for the frame rate for this output. Choose
                        INITIALIZE_FROM_SOURCE if you want the service to use the frame rate from
                        the input. Choose SPECIFIED if you want the service to use the frame rate
                        you specify in the settings FramerateNumerator and FramerateDenominator.

                        - **FramerateConversionAlgorithm** *(string) --* When set to INTERPOLATE,
                        produces smoother motion during frame rate conversion.

                        - **FramerateDenominator** *(integer) --* When you use the API for transcode
                        jobs that use frame rate conversion, specify the frame rate as a fraction.
                        For example, 24000 / 1001 =
                             23.976 fps. Use FramerateDenominator to specify
                        the denominator of this fraction. In this example, use 1001 for the value of
                        FramerateDenominator. When you use the console for transcode jobs that use
                        frame rate conversion, provide the value as a decimal number for Framerate.
                        In this example, specify 23.976.

                        - **FramerateNumerator** *(integer) --* Frame rate numerator - frame rate is
                        a fraction, e.g. 24000 / 1001 = 23.976 fps.

                        - **GopBReference** *(string) --* If enable, use reference B frames for GOP
                        structures that have B frames > 1.

                        - **GopClosedCadence** *(integer) --* Frequency of closed GOPs. In streaming
                        applications, it is recommended that this be set to 1 so a decoder joining
                        mid-stream will receive an IDR frame as quickly as possible. Setting this
                        value to 0 will break output segmenting.

                        - **GopSize** *(float) --* GOP Length (keyframe interval) in frames or
                        seconds. Must be greater than zero.

                        - **GopSizeUnits** *(string) --* Indicates if the GOP Size in H264 is
                        specified in frames or seconds. If seconds the system will convert the GOP
                        Size into a frame count at run time.

                        - **HrdBufferInitialFillPercentage** *(integer) --* Percentage of the buffer
                        that should initially be filled (HRD buffer model).

                        - **HrdBufferSize** *(integer) --* Size of buffer (HRD buffer model) in
                        bits. For example, enter five megabits as 5000000.

                        - **InterlaceMode** *(string) --* Use Interlace mode (InterlaceMode) to
                        choose the scan line type for the output. * Top Field First (TOP_FIELD) and
                        Bottom Field First (BOTTOM_FIELD) produce interlaced output with the entire
                        output having the same field polarity (top or bottom first). * Follow,
                        Default Top (FOLLOW_TOP_FIELD) and Follow, Default Bottom
                        (FOLLOW_BOTTOM_FIELD) use the same field polarity as the source. Therefore,
                        behavior depends on the input scan type, as follows. - If the source is
                        interlaced, the output will be interlaced with the same polarity as the
                        source (it will follow the source). The output could therefore be a mix of
                        "top field first" and "bottom field first". - If the source is progressive,
                        the output will be interlaced with "top field first" or "bottom field first"
                        polarity, depending on which of the Follow options you chose.

                        - **MaxBitrate** *(integer) --* Maximum bitrate in bits/second. For example,
                        enter five megabits per second as 5000000. Required when Rate control mode
                        is QVBR.

                        - **MinIInterval** *(integer) --* Enforces separation between repeated
                        (cadence) I-frames and I-frames inserted by Scene Change Detection. If a
                        scene change I-frame is within I-interval frames of a cadence I-frame, the
                        GOP is shrunk and/or stretched to the scene change I-frame. GOP stretch
                        requires enabling lookahead as well as setting I-interval. The normal
                        cadence resumes for the next GOP. This setting is only used when Scene
                        Change Detect is enabled. Note: Maximum GOP stretch =
                             GOP size +
                        Min-I-interval - 1

                        - **NumberBFramesBetweenReferenceFrames** *(integer) --* Number of B-frames
                        between reference frames.

                        - **NumberReferenceFrames** *(integer) --* Number of reference frames to
                        use. The encoder may use more than requested if using B-frames and/or
                        interlaced encoding.

                        - **ParControl** *(string) --* Using the API, enable ParFollowSource if you
                        want the service to use the pixel aspect ratio from the input. Using the
                        console, do this by choosing Follow source for Pixel aspect ratio.

                        - **ParDenominator** *(integer) --* Pixel Aspect Ratio denominator.

                        - **ParNumerator** *(integer) --* Pixel Aspect Ratio numerator.

                        - **QualityTuningLevel** *(string) --* Use Quality tuning level
                        (H264QualityTuningLevel) to specifiy whether to use fast single-pass,
                        high-quality singlepass, or high-quality multipass video encoding.

                        - **QvbrSettings** *(dict) --* Settings for quality-defined variable bitrate
                        encoding with the H.264 codec. Required when you set Rate control mode to
                        QVBR. Not valid when you set Rate control mode to a value other than QVBR,
                        or when you don't define Rate control mode.

                          - **MaxAverageBitrate** *(integer) --* Use this setting only when Rate
                          control mode is QVBR and Quality tuning level is Multi-pass HQ. For Max
                          average bitrate values suited to the complexity of your input video, the
                          service limits the average bitrate of the video part of this output to the
                          value that you choose. That is, the total size of the video element is
                          less than or equal to the value you set multiplied by the number of
                          seconds of encoded output.

                          - **QvbrQualityLevel** *(integer) --* Required when you use QVBR rate
                          control mode. That is, when you specify qvbrSettings within h264Settings.
                          Specify the target quality level for this output, from 1 to 10. Use higher
                          numbers for greater quality. Level 10 results in nearly lossless
                          compression. The quality level for most broadcast-quality transcodes is
                          between 6 and 9.

                        - **RateControlMode** *(string) --* Use this setting to specify whether this
                        output has a variable bitrate (VBR), constant bitrate (CBR) or
                        quality-defined variable bitrate (QVBR).

                        - **RepeatPps** *(string) --* Places a PPS header on each encoded picture,
                        even if repeated.

                        - **SceneChangeDetect** *(string) --* Enable this setting to insert I-frames
                        at scene changes that the service automatically detects. This improves video
                        quality and is enabled by default. If this output uses QVBR, choose
                        Transition detection (TRANSITION_DETECTION) for further video quality
                        improvement. For more information about QVBR, see
                        https://docs.aws.amazon.com/console/mediaconvert/cbr-vbr-qvbr.

                        - **Slices** *(integer) --* Number of slices per picture. Must be less than
                        or equal to the number of macroblock rows for progressive pictures, and less
                        than or equal to half the number of macroblock rows for interlaced pictures.

                        - **SlowPal** *(string) --* Enables Slow PAL rate conversion. 23.976fps and
                        24fps input is relabeled as 25fps, and audio is sped up correspondingly.

                        - **Softness** *(integer) --* Softness. Selects quantizer matrix, larger
                        values reduce high-frequency content in the encoded image.

                        - **SpatialAdaptiveQuantization** *(string) --* Adjust quantization within
                        each frame based on spatial variation of content complexity.

                        - **Syntax** *(string) --* Produces a bitstream compliant with SMPTE
                        RP-2027.

                        - **Telecine** *(string) --* This field applies only if the Streams >
                        Advanced > Framerate (framerate) field is set to 29.970. This field works
                        with the Streams > Advanced > Preprocessors > Deinterlacer field
                        (deinterlace_mode) and the Streams > Advanced > Interlaced Mode field
                        (interlace_mode) to identify the scan type for the output: Progressive,
                        Interlaced, Hard Telecine or Soft Telecine. - Hard: produces 29.97i output
                        from 23.976 input. - Soft: produces 23.976; the player converts this output
                        to 29.97i.

                        - **TemporalAdaptiveQuantization** *(string) --* Adjust quantization within
                        each frame based on temporal variation of content complexity.

                        - **UnregisteredSeiTimecode** *(string) --* Inserts timecode for each frame
                        as 4 bytes of an unregistered SEI message.

                      - **H265Settings** *(dict) --* Settings for H265 codec

                        - **AdaptiveQuantization** *(string) --* Adaptive quantization. Allows
                        intra-frame quantizers to vary to improve visual quality.

                        - **AlternateTransferFunctionSei** *(string) --* Enables Alternate Transfer
                        Function SEI message for outputs using Hybrid Log Gamma (HLG)
                        Electro-Optical Transfer Function (EOTF).

                        - **Bitrate** *(integer) --* Specify the average bitrate in bits per second.
                        Required for VBR and CBR. For MS Smooth outputs, bitrates must be unique
                        when rounded down to the nearest multiple of 1000.

                        - **CodecLevel** *(string) --* H.265 Level.

                        - **CodecProfile** *(string) --* Represents the Profile and Tier, per the
                        HEVC (H.265) specification. Selections are grouped as [Profile] / [Tier], so
                        "Main/High" represents Main Profile with High Tier. 4:2:2 profiles are only
                        available with the HEVC 4:2:2 License.

                        - **DynamicSubGop** *(string) --* Choose Adaptive to improve subjective
                        video quality for high-motion content. This will cause the service to use
                        fewer B-frames (which infer information based on other frames) for
                        high-motion portions of the video and more B-frames for low-motion portions.
                        The maximum number of B-frames is limited by the value you provide for the
                        setting B frames between reference frames
                        (numberBFramesBetweenReferenceFrames).

                        - **FlickerAdaptiveQuantization** *(string) --* Adjust quantization within
                        each frame to reduce flicker or 'pop' on I-frames.

                        - **FramerateControl** *(string) --* If you are using the console, use the
                        Framerate setting to specify the frame rate for this output. If you want to
                        keep the same frame rate as the input video, choose Follow source. If you
                        want to do frame rate conversion, choose a frame rate from the dropdown list
                        or choose Custom. The framerates shown in the dropdown list are decimal
                        approximations of fractions. If you choose Custom, specify your frame rate
                        as a fraction. If you are creating your transcoding job sepecification as a
                        JSON file without the console, use FramerateControl to specify which value
                        the service uses for the frame rate for this output. Choose
                        INITIALIZE_FROM_SOURCE if you want the service to use the frame rate from
                        the input. Choose SPECIFIED if you want the service to use the frame rate
                        you specify in the settings FramerateNumerator and FramerateDenominator.

                        - **FramerateConversionAlgorithm** *(string) --* When set to INTERPOLATE,
                        produces smoother motion during frame rate conversion.

                        - **FramerateDenominator** *(integer) --* Frame rate denominator.

                        - **FramerateNumerator** *(integer) --* Frame rate numerator - frame rate is
                        a fraction, e.g. 24000 / 1001 = 23.976 fps.

                        - **GopBReference** *(string) --* If enable, use reference B frames for GOP
                        structures that have B frames > 1.

                        - **GopClosedCadence** *(integer) --* Frequency of closed GOPs. In streaming
                        applications, it is recommended that this be set to 1 so a decoder joining
                        mid-stream will receive an IDR frame as quickly as possible. Setting this
                        value to 0 will break output segmenting.

                        - **GopSize** *(float) --* GOP Length (keyframe interval) in frames or
                        seconds. Must be greater than zero.

                        - **GopSizeUnits** *(string) --* Indicates if the GOP Size in H265 is
                        specified in frames or seconds. If seconds the system will convert the GOP
                        Size into a frame count at run time.

                        - **HrdBufferInitialFillPercentage** *(integer) --* Percentage of the buffer
                        that should initially be filled (HRD buffer model).

                        - **HrdBufferSize** *(integer) --* Size of buffer (HRD buffer model) in
                        bits. For example, enter five megabits as 5000000.

                        - **InterlaceMode** *(string) --* Choose the scan line type for the output.
                        Choose Progressive (PROGRESSIVE) to create a progressive output, regardless
                        of the scan type of your input. Choose Top Field First (TOP_FIELD) or Bottom
                        Field First (BOTTOM_FIELD) to create an output that's interlaced with the
                        same field polarity throughout. Choose Follow, Default Top
                        (FOLLOW_TOP_FIELD) or Follow, Default Bottom (FOLLOW_BOTTOM_FIELD) to create
                        an interlaced output with the same field polarity as the source. If the
                        source is interlaced, the output will be interlaced with the same polarity
                        as the source (it will follow the source). The output could therefore be a
                        mix of "top field first" and "bottom field first". If the source is
                        progressive, your output will be interlaced with "top field first" or
                        "bottom field first" polarity, depending on which of the Follow options you
                        chose. If you don't choose a value, the service will default to Progressive
                        (PROGRESSIVE).

                        - **MaxBitrate** *(integer) --* Maximum bitrate in bits/second. For example,
                        enter five megabits per second as 5000000. Required when Rate control mode
                        is QVBR.

                        - **MinIInterval** *(integer) --* Enforces separation between repeated
                        (cadence) I-frames and I-frames inserted by Scene Change Detection. If a
                        scene change I-frame is within I-interval frames of a cadence I-frame, the
                        GOP is shrunk and/or stretched to the scene change I-frame. GOP stretch
                        requires enabling lookahead as well as setting I-interval. The normal
                        cadence resumes for the next GOP. This setting is only used when Scene
                        Change Detect is enabled. Note: Maximum GOP stretch =
                             GOP size +
                        Min-I-interval - 1

                        - **NumberBFramesBetweenReferenceFrames** *(integer) --* Number of B-frames
                        between reference frames.

                        - **NumberReferenceFrames** *(integer) --* Number of reference frames to
                        use. The encoder may use more than requested if using B-frames and/or
                        interlaced encoding.

                        - **ParControl** *(string) --* Using the API, enable ParFollowSource if you
                        want the service to use the pixel aspect ratio from the input. Using the
                        console, do this by choosing Follow source for Pixel aspect ratio.

                        - **ParDenominator** *(integer) --* Pixel Aspect Ratio denominator.

                        - **ParNumerator** *(integer) --* Pixel Aspect Ratio numerator.

                        - **QualityTuningLevel** *(string) --* Use Quality tuning level
                        (H265QualityTuningLevel) to specifiy whether to use fast single-pass,
                        high-quality singlepass, or high-quality multipass video encoding.

                        - **QvbrSettings** *(dict) --* Settings for quality-defined variable bitrate
                        encoding with the H.265 codec. Required when you set Rate control mode to
                        QVBR. Not valid when you set Rate control mode to a value other than QVBR,
                        or when you don't define Rate control mode.

                          - **MaxAverageBitrate** *(integer) --* Use this setting only when Rate
                          control mode is QVBR and Quality tuning level is Multi-pass HQ. For Max
                          average bitrate values suited to the complexity of your input video, the
                          service limits the average bitrate of the video part of this output to the
                          value that you choose. That is, the total size of the video element is
                          less than or equal to the value you set multiplied by the number of
                          seconds of encoded output.

                          - **QvbrQualityLevel** *(integer) --* Required when you use QVBR rate
                          control mode. That is, when you specify qvbrSettings within h265Settings.
                          Specify the target quality level for this output, from 1 to 10. Use higher
                          numbers for greater quality. Level 10 results in nearly lossless
                          compression. The quality level for most broadcast-quality transcodes is
                          between 6 and 9.

                        - **RateControlMode** *(string) --* Use this setting to specify whether this
                        output has a variable bitrate (VBR), constant bitrate (CBR) or
                        quality-defined variable bitrate (QVBR).

                        - **SampleAdaptiveOffsetFilterMode** *(string) --* Specify Sample Adaptive
                        Offset (SAO) filter strength. Adaptive mode dynamically selects best
                        strength based on content

                        - **SceneChangeDetect** *(string) --* Enable this setting to insert I-frames
                        at scene changes that the service automatically detects. This improves video
                        quality and is enabled by default. If this output uses QVBR, choose
                        Transition detection (TRANSITION_DETECTION) for further video quality
                        improvement. For more information about QVBR, see
                        https://docs.aws.amazon.com/console/mediaconvert/cbr-vbr-qvbr.

                        - **Slices** *(integer) --* Number of slices per picture. Must be less than
                        or equal to the number of macroblock rows for progressive pictures, and less
                        than or equal to half the number of macroblock rows for interlaced pictures.

                        - **SlowPal** *(string) --* Enables Slow PAL rate conversion. 23.976fps and
                        24fps input is relabeled as 25fps, and audio is sped up correspondingly.

                        - **SpatialAdaptiveQuantization** *(string) --* Adjust quantization within
                        each frame based on spatial variation of content complexity.

                        - **Telecine** *(string) --* This field applies only if the Streams >
                        Advanced > Framerate (framerate) field is set to 29.970. This field works
                        with the Streams > Advanced > Preprocessors > Deinterlacer field
                        (deinterlace_mode) and the Streams > Advanced > Interlaced Mode field
                        (interlace_mode) to identify the scan type for the output: Progressive,
                        Interlaced, Hard Telecine or Soft Telecine. - Hard: produces 29.97i output
                        from 23.976 input. - Soft: produces 23.976; the player converts this output
                        to 29.97i.

                        - **TemporalAdaptiveQuantization** *(string) --* Adjust quantization within
                        each frame based on temporal variation of content complexity.

                        - **TemporalIds** *(string) --* Enables temporal layer identifiers in the
                        encoded bitstream. Up to 3 layers are supported depending on GOP structure:
                        I- and P-frames form one layer, reference B-frames can form a second layer
                        and non-reference b-frames can form a third layer. Decoders can optionally
                        decode only the lower temporal layers to generate a lower frame rate output.
                        For example, given a bitstream with temporal IDs and with b-frames = 1 (i.e.
                        IbPbPb display order), a decoder could decode all the frames for full frame
                        rate output or only the I and P frames (lowest temporal layer) for a half
                        frame rate output.

                        - **Tiles** *(string) --* Enable use of tiles, allowing horizontal as well
                        as vertical subdivision of the encoded pictures.

                        - **UnregisteredSeiTimecode** *(string) --* Inserts timecode for each frame
                        as 4 bytes of an unregistered SEI message.

                        - **WriteMp4PackagingType** *(string) --* If the location of parameter set
                        NAL units doesn't matter in your workflow, ignore this setting. Use this
                        setting only with CMAF or DASH outputs, or with standalone file outputs in
                        an MPEG-4 container (MP4 outputs). Choose HVC1 to mark your output as HVC1.
                        This makes your output compliant with the following specification: ISO
                        IECJTC1 SC29 N13798 Text ISO/IEC FDIS 14496-15 3rd Edition. For these
                        outputs, the service stores parameter set NAL units in the sample headers
                        but not in the samples directly. For MP4 outputs, when you choose HVC1, your
                        output video might not work properly with some downstream systems and video
                        players. The service defaults to marking your output as HEV1. For these
                        outputs, the service writes parameter set NAL units directly into the
                        samples.

                      - **Mpeg2Settings** *(dict) --* Required when you set (Codec) under
                      (VideoDescription)>(CodecSettings) to the value MPEG2.

                        - **AdaptiveQuantization** *(string) --* Adaptive quantization. Allows
                        intra-frame quantizers to vary to improve visual quality.

                        - **Bitrate** *(integer) --* Specify the average bitrate in bits per second.
                        Required for VBR and CBR. For MS Smooth outputs, bitrates must be unique
                        when rounded down to the nearest multiple of 1000.

                        - **CodecLevel** *(string) --* Use Level (Mpeg2CodecLevel) to set the MPEG-2
                        level for the video output.

                        - **CodecProfile** *(string) --* Use Profile (Mpeg2CodecProfile) to set the
                        MPEG-2 profile for the video output.

                        - **DynamicSubGop** *(string) --* Choose Adaptive to improve subjective
                        video quality for high-motion content. This will cause the service to use
                        fewer B-frames (which infer information based on other frames) for
                        high-motion portions of the video and more B-frames for low-motion portions.
                        The maximum number of B-frames is limited by the value you provide for the
                        setting B frames between reference frames
                        (numberBFramesBetweenReferenceFrames).

                        - **FramerateControl** *(string) --* If you are using the console, use the
                        Framerate setting to specify the frame rate for this output. If you want to
                        keep the same frame rate as the input video, choose Follow source. If you
                        want to do frame rate conversion, choose a frame rate from the dropdown list
                        or choose Custom. The framerates shown in the dropdown list are decimal
                        approximations of fractions. If you choose Custom, specify your frame rate
                        as a fraction. If you are creating your transcoding job sepecification as a
                        JSON file without the console, use FramerateControl to specify which value
                        the service uses for the frame rate for this output. Choose
                        INITIALIZE_FROM_SOURCE if you want the service to use the frame rate from
                        the input. Choose SPECIFIED if you want the service to use the frame rate
                        you specify in the settings FramerateNumerator and FramerateDenominator.

                        - **FramerateConversionAlgorithm** *(string) --* When set to INTERPOLATE,
                        produces smoother motion during frame rate conversion.

                        - **FramerateDenominator** *(integer) --* Frame rate denominator.

                        - **FramerateNumerator** *(integer) --* Frame rate numerator - frame rate is
                        a fraction, e.g. 24000 / 1001 = 23.976 fps.

                        - **GopClosedCadence** *(integer) --* Frequency of closed GOPs. In streaming
                        applications, it is recommended that this be set to 1 so a decoder joining
                        mid-stream will receive an IDR frame as quickly as possible. Setting this
                        value to 0 will break output segmenting.

                        - **GopSize** *(float) --* GOP Length (keyframe interval) in frames or
                        seconds. Must be greater than zero.

                        - **GopSizeUnits** *(string) --* Indicates if the GOP Size in MPEG2 is
                        specified in frames or seconds. If seconds the system will convert the GOP
                        Size into a frame count at run time.

                        - **HrdBufferInitialFillPercentage** *(integer) --* Percentage of the buffer
                        that should initially be filled (HRD buffer model).

                        - **HrdBufferSize** *(integer) --* Size of buffer (HRD buffer model) in
                        bits. For example, enter five megabits as 5000000.

                        - **InterlaceMode** *(string) --* Use Interlace mode (InterlaceMode) to
                        choose the scan line type for the output. * Top Field First (TOP_FIELD) and
                        Bottom Field First (BOTTOM_FIELD) produce interlaced output with the entire
                        output having the same field polarity (top or bottom first). * Follow,
                        Default Top (FOLLOW_TOP_FIELD) and Follow, Default Bottom
                        (FOLLOW_BOTTOM_FIELD) use the same field polarity as the source. Therefore,
                        behavior depends on the input scan type. - If the source is interlaced, the
                        output will be interlaced with the same polarity as the source (it will
                        follow the source). The output could therefore be a mix of "top field first"
                        and "bottom field first". - If the source is progressive, the output will be
                        interlaced with "top field first" or "bottom field first" polarity,
                        depending on which of the Follow options you chose.

                        - **IntraDcPrecision** *(string) --* Use Intra DC precision
                        (Mpeg2IntraDcPrecision) to set quantization precision for intra-block DC
                        coefficients. If you choose the value auto, the service will automatically
                        select the precision based on the per-frame compression ratio.

                        - **MaxBitrate** *(integer) --* Maximum bitrate in bits/second. For example,
                        enter five megabits per second as 5000000.

                        - **MinIInterval** *(integer) --* Enforces separation between repeated
                        (cadence) I-frames and I-frames inserted by Scene Change Detection. If a
                        scene change I-frame is within I-interval frames of a cadence I-frame, the
                        GOP is shrunk and/or stretched to the scene change I-frame. GOP stretch
                        requires enabling lookahead as well as setting I-interval. The normal
                        cadence resumes for the next GOP. This setting is only used when Scene
                        Change Detect is enabled. Note: Maximum GOP stretch =
                             GOP size +
                        Min-I-interval - 1

                        - **NumberBFramesBetweenReferenceFrames** *(integer) --* Number of B-frames
                        between reference frames.

                        - **ParControl** *(string) --* Using the API, enable ParFollowSource if you
                        want the service to use the pixel aspect ratio from the input. Using the
                        console, do this by choosing Follow source for Pixel aspect ratio.

                        - **ParDenominator** *(integer) --* Pixel Aspect Ratio denominator.

                        - **ParNumerator** *(integer) --* Pixel Aspect Ratio numerator.

                        - **QualityTuningLevel** *(string) --* Use Quality tuning level
                        (Mpeg2QualityTuningLevel) to specifiy whether to use single-pass or
                        multipass video encoding.

                        - **RateControlMode** *(string) --* Use Rate control mode
                        (Mpeg2RateControlMode) to specifiy whether the bitrate is variable (vbr) or
                        constant (cbr).

                        - **SceneChangeDetect** *(string) --* Enable this setting to insert I-frames
                        at scene changes that the service automatically detects. This improves video
                        quality and is enabled by default.

                        - **SlowPal** *(string) --* Enables Slow PAL rate conversion. 23.976fps and
                        24fps input is relabeled as 25fps, and audio is sped up correspondingly.

                        - **Softness** *(integer) --* Softness. Selects quantizer matrix, larger
                        values reduce high-frequency content in the encoded image.

                        - **SpatialAdaptiveQuantization** *(string) --* Adjust quantization within
                        each frame based on spatial variation of content complexity.

                        - **Syntax** *(string) --* Produces a Type D-10 compatible bitstream (SMPTE
                        356M-2001).

                        - **Telecine** *(string) --* Only use Telecine (Mpeg2Telecine) when you set
                        Framerate (Framerate) to 29.970. Set Telecine (Mpeg2Telecine) to Hard (hard)
                        to produce a 29.97i output from a 23.976 input. Set it to Soft (soft) to
                        produce 23.976 output and leave converstion to the player.

                        - **TemporalAdaptiveQuantization** *(string) --* Adjust quantization within
                        each frame based on temporal variation of content complexity.

                      - **ProresSettings** *(dict) --* Required when you set (Codec) under
                      (VideoDescription)>(CodecSettings) to the value PRORES.

                        - **CodecProfile** *(string) --* Use Profile (ProResCodecProfile) to
                        specifiy the type of Apple ProRes codec to use for this output.

                        - **FramerateControl** *(string) --* If you are using the console, use the
                        Framerate setting to specify the frame rate for this output. If you want to
                        keep the same frame rate as the input video, choose Follow source. If you
                        want to do frame rate conversion, choose a frame rate from the dropdown list
                        or choose Custom. The framerates shown in the dropdown list are decimal
                        approximations of fractions. If you choose Custom, specify your frame rate
                        as a fraction. If you are creating your transcoding job sepecification as a
                        JSON file without the console, use FramerateControl to specify which value
                        the service uses for the frame rate for this output. Choose
                        INITIALIZE_FROM_SOURCE if you want the service to use the frame rate from
                        the input. Choose SPECIFIED if you want the service to use the frame rate
                        you specify in the settings FramerateNumerator and FramerateDenominator.

                        - **FramerateConversionAlgorithm** *(string) --* When set to INTERPOLATE,
                        produces smoother motion during frame rate conversion.

                        - **FramerateDenominator** *(integer) --* Frame rate denominator.

                        - **FramerateNumerator** *(integer) --* When you use the API for transcode
                        jobs that use frame rate conversion, specify the frame rate as a fraction.
                        For example, 24000 / 1001 =
                             23.976 fps. Use FramerateNumerator to specify
                        the numerator of this fraction. In this example, use 24000 for the value of
                        FramerateNumerator.

                        - **InterlaceMode** *(string) --* Use Interlace mode (InterlaceMode) to
                        choose the scan line type for the output. * Top Field First (TOP_FIELD) and
                        Bottom Field First (BOTTOM_FIELD) produce interlaced output with the entire
                        output having the same field polarity (top or bottom first). * Follow,
                        Default Top (FOLLOW_TOP_FIELD) and Follow, Default Bottom
                        (FOLLOW_BOTTOM_FIELD) use the same field polarity as the source. Therefore,
                        behavior depends on the input scan type. - If the source is interlaced, the
                        output will be interlaced with the same polarity as the source (it will
                        follow the source). The output could therefore be a mix of "top field first"
                        and "bottom field first". - If the source is progressive, the output will be
                        interlaced with "top field first" or "bottom field first" polarity,
                        depending on which of the Follow options you chose.

                        - **ParControl** *(string) --* Use (ProresParControl) to specify how the
                        service determines the pixel aspect ratio. Set to Follow source
                        (INITIALIZE_FROM_SOURCE) to use the pixel aspect ratio from the input. To
                        specify a different pixel aspect ratio: Using the console, choose it from
                        the dropdown menu. Using the API, set ProresParControl to (SPECIFIED) and
                        provide for (ParNumerator) and (ParDenominator).

                        - **ParDenominator** *(integer) --* Pixel Aspect Ratio denominator.

                        - **ParNumerator** *(integer) --* Pixel Aspect Ratio numerator.

                        - **SlowPal** *(string) --* Enables Slow PAL rate conversion. 23.976fps and
                        24fps input is relabeled as 25fps, and audio is sped up correspondingly.

                        - **Telecine** *(string) --* Only use Telecine (ProresTelecine) when you set
                        Framerate (Framerate) to 29.970. Set Telecine (ProresTelecine) to Hard
                        (hard) to produce a 29.97i output from a 23.976 input. Set it to Soft (soft)
                        to produce 23.976 output and leave converstion to the player.

                    - **ColorMetadata** *(string) --* Choose Insert (INSERT) for this setting to
                    include color metadata in this output. Choose Ignore (IGNORE) to exclude color
                    metadata from this output. If you don't specify a value, the service sets this
                    to Insert by default.

                    - **Crop** *(dict) --* Use Cropping selection (crop) to specify the video area
                    that the service will include in the output video frame.

                      - **Height** *(integer) --* Height of rectangle in pixels. Specify only even
                      numbers.

                      - **Width** *(integer) --* Width of rectangle in pixels. Specify only even
                      numbers.

                      - **X** *(integer) --* The distance, in pixels, between the rectangle and the
                      left edge of the video frame. Specify only even numbers.

                      - **Y** *(integer) --* The distance, in pixels, between the rectangle and the
                      top edge of the video frame. Specify only even numbers.

                    - **DropFrameTimecode** *(string) --* Applies only to 29.97 fps outputs. When
                    this feature is enabled, the service will use drop-frame timecode on outputs. If
                    it is not possible to use drop-frame timecode, the system will fall back to
                    non-drop-frame. This setting is enabled by default when Timecode insertion
                    (TimecodeInsertion) is enabled.

                    - **FixedAfd** *(integer) --* Applies only if you set AFD
                    Signaling(AfdSignaling) to Fixed (FIXED). Use Fixed (FixedAfd) to specify a
                    four-bit AFD value which the service will write on all frames of this video
                    output.

                    - **Height** *(integer) --* Use the Height (Height) setting to define the video
                    resolution height for this output. Specify in pixels. If you don't provide a
                    value here, the service will use the input height.

                    - **Position** *(dict) --* Use Selection placement (position) to define the
                    video area in your output frame. The area outside of the rectangle that you
                    specify here is black.

                      - **Height** *(integer) --* Height of rectangle in pixels. Specify only even
                      numbers.

                      - **Width** *(integer) --* Width of rectangle in pixels. Specify only even
                      numbers.

                      - **X** *(integer) --* The distance, in pixels, between the rectangle and the
                      left edge of the video frame. Specify only even numbers.

                      - **Y** *(integer) --* The distance, in pixels, between the rectangle and the
                      top edge of the video frame. Specify only even numbers.

                    - **RespondToAfd** *(string) --* Use Respond to AFD (RespondToAfd) to specify
                    how the service changes the video itself in response to AFD values in the input.
                    * Choose Respond to clip the input video frame according to the AFD value, input
                    display aspect ratio, and output display aspect ratio. * Choose Passthrough to
                    include the input AFD values. Do not choose this when AfdSignaling is set to
                    (NONE). A preferred implementation of this workflow is to set RespondToAfd to
                    (NONE) and set AfdSignaling to (AUTO). * Choose None to remove all input AFD
                    values from this output.

                    - **ScalingBehavior** *(string) --* Specify how the service handles outputs that
                    have a different aspect ratio from the input aspect ratio. Choose Stretch to
                    output (STRETCH_TO_OUTPUT) to have the service stretch your video image to fit.
                    Keep the setting Default (DEFAULT) to have the service letterbox your video
                    instead. This setting overrides any value that you specify for the setting
                    Selection placement (position) in this output.

                    - **Sharpness** *(integer) --* Use Sharpness (Sharpness) setting to specify the
                    strength of anti-aliasing. This setting changes the width of the anti-alias
                    filter kernel used for scaling. Sharpness only applies if your output resolution
                    is different from your input resolution. 0 is the softest setting, 100 the
                    sharpest, and 50 recommended for most content.

                    - **TimecodeInsertion** *(string) --* Applies only to H.264, H.265, MPEG2, and
                    ProRes outputs. Only enable Timecode insertion when the input frame rate is
                    identical to the output frame rate. To include timecodes in this output, set
                    Timecode insertion (VideoTimecodeInsertion) to PIC_TIMING_SEI. To leave them
                    out, set it to DISABLED. Default is DISABLED. When the service inserts timecodes
                    in an output, by default, it uses any embedded timecodes from the input. If none
                    are present, the service will set the timecode for the first output frame to
                    zero. To change this default behavior, adjust the settings under Timecode
                    configuration (TimecodeConfig). In the console, these settings are located under
                    Job > Job settings > Timecode configuration. Note - Timecode source under input
                    settings (InputTimecodeSource) does not affect the timecodes that are inserted
                    in the output. Source under Job settings > Timecode configuration
                    (TimecodeSource) does.

                    - **VideoPreprocessors** *(dict) --* Find additional transcoding features under
                    Preprocessors (VideoPreprocessors). Enable the features at each output
                    individually. These features are disabled by default.

                      - **ColorCorrector** *(dict) --* Enable the Color corrector (ColorCorrector)
                      feature if necessary. Enable or disable this feature for each output
                      individually. This setting is disabled by default.

                        - **Brightness** *(integer) --* Brightness level.

                        - **ColorSpaceConversion** *(string) --* Specify the color space you want
                        for this output. The service supports conversion between HDR formats,
                        between SDR formats, and from SDR to HDR. The service doesn't support
                        conversion from HDR to SDR. SDR to HDR conversion doesn't upgrade the
                        dynamic range. The converted video has an HDR format, but visually appears
                        the same as an unconverted output.

                        - **Contrast** *(integer) --* Contrast level.

                        - **Hdr10Metadata** *(dict) --* Use these settings when you convert to the
                        HDR 10 color space. Specify the SMPTE ST 2086 Mastering Display Color Volume
                        static metadata that you want signaled in the output. These values don't
                        affect the pixel values that are encoded in the video stream. They are
                        intended to help the downstream video player display content in a way that
                        reflects the intentions of the the content creator. When you set Color space
                        conversion (ColorSpaceConversion) to HDR 10 (FORCE_HDR10), these settings
                        are required. You must set values for Max frame average light level
                        (maxFrameAverageLightLevel) and Max content light level
                        (maxContentLightLevel); these settings don't have a default value. The
                        default values for the other HDR 10 metadata settings are defined by the
                        P3D65 color space. For more information about MediaConvert HDR jobs, see
                        https://docs.aws.amazon.com/console/mediaconvert/hdr.

                          - **BluePrimaryX** *(integer) --* HDR Master Display Information must be
                          provided by a color grader, using color grading tools. Range is 0 to
                          50,000, each increment represents 0.00002 in CIE1931 color coordinate.
                          Note that this setting is not for color correction.

                          - **BluePrimaryY** *(integer) --* HDR Master Display Information must be
                          provided by a color grader, using color grading tools. Range is 0 to
                          50,000, each increment represents 0.00002 in CIE1931 color coordinate.
                          Note that this setting is not for color correction.

                          - **GreenPrimaryX** *(integer) --* HDR Master Display Information must be
                          provided by a color grader, using color grading tools. Range is 0 to
                          50,000, each increment represents 0.00002 in CIE1931 color coordinate.
                          Note that this setting is not for color correction.

                          - **GreenPrimaryY** *(integer) --* HDR Master Display Information must be
                          provided by a color grader, using color grading tools. Range is 0 to
                          50,000, each increment represents 0.00002 in CIE1931 color coordinate.
                          Note that this setting is not for color correction.

                          - **MaxContentLightLevel** *(integer) --* Maximum light level among all
                          samples in the coded video sequence, in units of candelas per square
                          meter. This setting doesn't have a default value; you must specify a value
                          that is suitable for the content.

                          - **MaxFrameAverageLightLevel** *(integer) --* Maximum average light level
                          of any frame in the coded video sequence, in units of candelas per square
                          meter. This setting doesn't have a default value; you must specify a value
                          that is suitable for the content.

                          - **MaxLuminance** *(integer) --* Nominal maximum mastering display
                          luminance in units of of 0.0001 candelas per square meter.

                          - **MinLuminance** *(integer) --* Nominal minimum mastering display
                          luminance in units of of 0.0001 candelas per square meter

                          - **RedPrimaryX** *(integer) --* HDR Master Display Information must be
                          provided by a color grader, using color grading tools. Range is 0 to
                          50,000, each increment represents 0.00002 in CIE1931 color coordinate.
                          Note that this setting is not for color correction.

                          - **RedPrimaryY** *(integer) --* HDR Master Display Information must be
                          provided by a color grader, using color grading tools. Range is 0 to
                          50,000, each increment represents 0.00002 in CIE1931 color coordinate.
                          Note that this setting is not for color correction.

                          - **WhitePointX** *(integer) --* HDR Master Display Information must be
                          provided by a color grader, using color grading tools. Range is 0 to
                          50,000, each increment represents 0.00002 in CIE1931 color coordinate.
                          Note that this setting is not for color correction.

                          - **WhitePointY** *(integer) --* HDR Master Display Information must be
                          provided by a color grader, using color grading tools. Range is 0 to
                          50,000, each increment represents 0.00002 in CIE1931 color coordinate.
                          Note that this setting is not for color correction.

                        - **Hue** *(integer) --* Hue in degrees.

                        - **Saturation** *(integer) --* Saturation level.

                      - **Deinterlacer** *(dict) --* Use Deinterlacer (Deinterlacer) to produce
                      smoother motion and a clearer picture.

                        - **Algorithm** *(string) --* Only applies when you set Deinterlacer
                        (DeinterlaceMode) to Deinterlace (DEINTERLACE) or Adaptive (ADAPTIVE).
                        Motion adaptive interpolate (INTERPOLATE) produces sharper pictures, while
                        blend (BLEND) produces smoother motion. Use (INTERPOLATE_TICKER) OR
                        (BLEND_TICKER) if your source file includes a ticker, such as a scrolling
                        headline at the bottom of the frame.

                        - **Control** *(string) --* - When set to NORMAL (default), the deinterlacer
                        does not convert frames that are tagged in metadata as progressive. It will
                        only convert those that are tagged as some other type. - When set to
                        FORCE_ALL_FRAMES, the deinterlacer converts every frame to progressive -
                        even those that are already tagged as progressive. Turn Force mode on only
                        if there is a good chance that the metadata has tagged frames as progressive
                        when they are not progressive. Do not turn on otherwise; processing frames
                        that are already progressive into progressive will probably result in lower
                        quality video.

                        - **Mode** *(string) --* Use Deinterlacer (DeinterlaceMode) to choose how
                        the service will do deinterlacing. Default is Deinterlace. - Deinterlace
                        converts interlaced to progressive. - Inverse telecine converts Hard
                        Telecine 29.97i to progressive 23.976p. - Adaptive auto-detects and converts
                        to progressive.

                      - **DolbyVision** *(dict) --* Enable Dolby Vision feature to produce Dolby
                      Vision compatible video output.

                        - **L6Metadata** *(dict) --* Use these settings when you set
                        DolbyVisionLevel6Mode to SPECIFY to override the MaxCLL and MaxFALL values
                        in your input with new values.

                          - **MaxCll** *(integer) --* Maximum Content Light Level. Static HDR
                          metadata that corresponds to the brightest pixel in the entire stream.
                          Measured in nits.

                          - **MaxFall** *(integer) --* Maximum Frame-Average Light Level. Static HDR
                          metadata that corresponds to the highest frame-average brightness in the
                          entire stream. Measured in nits.

                        - **L6Mode** *(string) --* Use Dolby Vision Mode to choose how the service
                        will handle Dolby Vision MaxCLL and MaxFALL properies.

                        - **Profile** *(string) --* In the current MediaConvert implementation, the
                        Dolby Vision profile is always 5 (PROFILE_5). Therefore, all of your inputs
                        must contain Dolby Vision frame interleaved data.

                      - **ImageInserter** *(dict) --* Enable the Image inserter (ImageInserter)
                      feature to include a graphic overlay on your video. Enable or disable this
                      feature for each output individually. This setting is disabled by default.

                        - **InsertableImages** *(list) --* Specify the images that you want to
                        overlay on your video. The images must be PNG or TGA files.

                          - *(dict) --* Settings that specify how your still graphic overlay
                          appears.

                            - **Duration** *(integer) --* Specify the time, in milliseconds, for the
                            image to remain on the output video. This duration includes fade-in time
                            but not fade-out time.

                            - **FadeIn** *(integer) --* Specify the length of time, in milliseconds,
                            between the Start time that you specify for the image insertion and the
                            time that the image appears at full opacity. Full opacity is the level
                            that you specify for the opacity setting. If you don't specify a value
                            for Fade-in, the image will appear abruptly at the overlay start time.

                            - **FadeOut** *(integer) --* Specify the length of time, in
                            milliseconds, between the end of the time that you have specified for
                            the image overlay Duration and when the overlaid image has faded to
                            total transparency. If you don't specify a value for Fade-out, the image
                            will disappear abruptly at the end of the inserted image duration.

                            - **Height** *(integer) --* Specify the height of the inserted image in
                            pixels. If you specify a value that's larger than the video resolution
                            height, the service will crop your overlaid image to fit. To use the
                            native height of the image, keep this setting blank.

                            - **ImageInserterInput** *(string) --* Specify the HTTP, HTTPS, or
                            Amazon S3 location of the image that you want to overlay on the video.
                            Use a PNG or TGA file.

                            - **ImageX** *(integer) --* Specify the distance, in pixels, between the
                            inserted image and the left edge of the video frame. Required for any
                            image overlay that you specify.

                            - **ImageY** *(integer) --* Specify the distance, in pixels, between the
                            overlaid image and the top edge of the video frame. Required for any
                            image overlay that you specify.

                            - **Layer** *(integer) --* Specify how overlapping inserted images
                            appear. Images with higher values for Layer appear on top of images with
                            lower values for Layer.

                            - **Opacity** *(integer) --* Use Opacity (Opacity) to specify how much
                            of the underlying video shows through the inserted image. 0 is
                            transparent and 100 is fully opaque. Default is 50.

                            - **StartTime** *(string) --* Specify the timecode of the frame that you
                            want the overlay to first appear on. This must be in timecode
                            (HH:MM:SS:FF or HH:MM:SS;FF) format. Remember to take into account your
                            timecode source settings.

                            - **Width** *(integer) --* Specify the width of the inserted image in
                            pixels. If you specify a value that's larger than the video resolution
                            width, the service will crop your overlaid image to fit. To use the
                            native width of the image, keep this setting blank.

                      - **NoiseReducer** *(dict) --* Enable the Noise reducer (NoiseReducer) feature
                      to remove noise from your video output if necessary. Enable or disable this
                      feature for each output individually. This setting is disabled by default.

                        - **Filter** *(string) --* Use Noise reducer filter (NoiseReducerFilter) to
                        select one of the following spatial image filtering functions. To use this
                        setting, you must also enable Noise reducer (NoiseReducer). * Bilateral
                        preserves edges while reducing noise. * Mean (softest), Gaussian, Lanczos,
                        and Sharpen (sharpest) do convolution filtering. * Conserve does min/max
                        noise reduction. * Spatial does frequency-domain filtering based on JND
                        principles. * Temporal optimizes video quality for complex motion.

                        - **FilterSettings** *(dict) --* Settings for a noise reducer filter

                          - **Strength** *(integer) --* Relative strength of noise reducing filter.
                          Higher values produce stronger filtering.

                        - **SpatialFilterSettings** *(dict) --* Noise reducer filter settings for
                        spatial filter.

                          - **PostFilterSharpenStrength** *(integer) --* Specify strength of post
                          noise reduction sharpening filter, with 0 disabling the filter and 3
                          enabling it at maximum strength.

                          - **Speed** *(integer) --* The speed of the filter, from -2 (lower speed)
                          to 3 (higher speed), with 0 being the nominal value.

                          - **Strength** *(integer) --* Relative strength of noise reducing filter.
                          Higher values produce stronger filtering.

                        - **TemporalFilterSettings** *(dict) --* Noise reducer filter settings for
                        temporal filter.

                          - **AggressiveMode** *(integer) --* Use Aggressive mode for content that
                          has complex motion. Higher values produce stronger temporal filtering.
                          This filters highly complex scenes more aggressively and creates better VQ
                          for low bitrate outputs.

                          - **Speed** *(integer) --* The speed of the filter (higher number is
                          faster). Low setting reduces bit rate at the cost of transcode time, high
                          setting improves transcode time at the cost of bit rate.

                          - **Strength** *(integer) --* Specify the strength of the noise reducing
                          filter on this output. Higher values produce stronger filtering. We
                          recommend the following value ranges, depending on the result that you
                          want: * 0-2 for complexity reduction with minimal sharpness loss * 2-8 for
                          complexity reduction with image preservation * 8-16 for a high level of
                          complexity reduction

                      - **TimecodeBurnin** *(dict) --* Timecode burn-in (TimecodeBurnIn)--Burns the
                      output timecode and specified prefix into the output.

                        - **FontSize** *(integer) --* Use Font Size (FontSize) to set the font size
                        of any burned-in timecode. Valid values are 10, 16, 32, 48.

                        - **Position** *(string) --* Use Position (Position) under under Timecode
                        burn-in (TimecodeBurnIn) to specify the location the burned-in timecode on
                        output video.

                        - **Prefix** *(string) --* Use Prefix (Prefix) to place ASCII characters
                        before any burned-in timecode. For example, a prefix of "EZ-" will result in
                        the timecode "EZ-00:00:00:00". Provide either the characters themselves or
                        the ASCII code equivalents. The supported range of characters is 0x20
                        through 0x7e. This includes letters, numbers, and all special characters
                        represented on a standard English keyboard.

                    - **Width** *(integer) --* Use Width (Width) to define the video resolution
                    width, in pixels, for this output. If you don't provide a value here, the
                    service will use the input width.

                - **Type** *(string) --* A preset can be of two types: system or custom. System or
                built-in preset can't be modified or deleted by the user.
        """


class ListQueuesPaginator(Boto3Paginator):
    """
    Paginator for `list_queues`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ListBy: Literal["NAME", "CREATION_DATE"] = None,
        Order: Literal["ASCENDING", "DESCENDING"] = None,
        PaginationConfig: ListQueuesPaginatePaginationConfigTypeDef = None,
    ) -> ListQueuesPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`MediaConvert.Client.list_queues`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/mediaconvert-2017-08-29/ListQueues>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              ListBy='NAME'|'CREATION_DATE',
              Order='ASCENDING'|'DESCENDING',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type ListBy: string
        :param ListBy: Optional. When you request a list of queues, you can choose to list them
        alphabetically by NAME or chronologically by CREATION_DATE. If you don't specify, the
        service will list them by creation date.

        :type Order: string
        :param Order: When you request lists of resources, you can optionally specify whether they
        are sorted in ASCENDING or DESCENDING order. Default varies by resource.

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
                'Queues': [
                    {
                        'Arn': 'string',
                        'CreatedAt': datetime(2015, 1, 1),
                        'Description': 'string',
                        'LastUpdated': datetime(2015, 1, 1),
                        'Name': 'string',
                        'PricingPlan': 'ON_DEMAND'|'RESERVED',
                        'ProgressingJobsCount': 123,
                        'ReservationPlan': {
                            'Commitment': 'ONE_YEAR',
                            'ExpiresAt': datetime(2015, 1, 1),
                            'PurchasedAt': datetime(2015, 1, 1),
                            'RenewalType': 'AUTO_RENEW'|'EXPIRE',
                            'ReservedSlots': 123,
                            'Status': 'ACTIVE'|'EXPIRED'
                        },
                        'Status': 'ACTIVE'|'PAUSED',
                        'SubmittedJobsCount': 123,
                        'Type': 'SYSTEM'|'CUSTOM'
                    },
                ]
            }
          **Response Structure**

          - *(dict) --*

            - **Queues** *(list) --* List of queues.

              - *(dict) --* You can use queues to manage the resources that are available to your
              AWS account for running multiple transcoding jobs at the same time. If you don't
              specify a queue, the service sends all jobs through the default queue. For more
              information, see
              https://docs.aws.amazon.com/mediaconvert/latest/ug/working-with-queues.html.

                - **Arn** *(string) --* An identifier for this resource that is unique within all of
                AWS.

                - **CreatedAt** *(datetime) --* The timestamp in epoch seconds for when you created
                the queue.

                - **Description** *(string) --* An optional description that you create for each
                queue.

                - **LastUpdated** *(datetime) --* The timestamp in epoch seconds for when you most
                recently updated the queue.

                - **Name** *(string) --* A name that you create for each queue. Each name must be
                unique within your account.

                - **PricingPlan** *(string) --* Specifies whether the pricing plan for the queue is
                on-demand or reserved. For on-demand, you pay per minute, billed in increments of
                .01 minute. For reserved, you pay for the transcoding capacity of the entire queue,
                regardless of how much or how little you use it. Reserved pricing requires a
                12-month commitment.

                - **ProgressingJobsCount** *(integer) --* The estimated number of jobs with a
                PROGRESSING status.

                - **ReservationPlan** *(dict) --* Details about the pricing plan for your reserved
                queue. Required for reserved queues and not applicable to on-demand queues.

                  - **Commitment** *(string) --* The length of the term of your reserved queue
                  pricing plan commitment.

                  - **ExpiresAt** *(datetime) --* The timestamp in epoch seconds for when the
                  current pricing plan term for this reserved queue expires.

                  - **PurchasedAt** *(datetime) --* The timestamp in epoch seconds for when you set
                  up the current pricing plan for this reserved queue.

                  - **RenewalType** *(string) --* Specifies whether the term of your reserved queue
                  pricing plan is automatically extended (AUTO_RENEW) or expires (EXPIRE) at the end
                  of the term.

                  - **ReservedSlots** *(integer) --* Specifies the number of reserved transcode
                  slots (RTS) for this queue. The number of RTS determines how many jobs the queue
                  can process in parallel; each RTS can process one job at a time. When you increase
                  this number, you extend your existing commitment with a new 12-month commitment
                  for a larger number of RTS. The new commitment begins when you purchase the
                  additional capacity. You can't decrease the number of RTS in your reserved queue.

                  - **Status** *(string) --* Specifies whether the pricing plan for your reserved
                  queue is ACTIVE or EXPIRED.

                - **Status** *(string) --* Queues can be ACTIVE or PAUSED. If you pause a queue, the
                service won't begin processing jobs in that queue. Jobs that are running when you
                pause the queue continue to run until they finish or result in an error.

                - **SubmittedJobsCount** *(integer) --* The estimated number of jobs with a
                SUBMITTED status.

                - **Type** *(string) --* Specifies whether this on-demand queue is system or custom.
                System queues are built in. You can't modify or delete system queues. You can create
                and modify custom queues.
        """
