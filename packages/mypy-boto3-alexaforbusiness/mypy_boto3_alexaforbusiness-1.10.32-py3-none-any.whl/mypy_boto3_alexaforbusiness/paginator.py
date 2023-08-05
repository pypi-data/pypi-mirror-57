"Main interface for alexaforbusiness service Paginators"
from __future__ import annotations

from typing import List
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3.type_defs import Literal
from mypy_boto3_alexaforbusiness.type_defs import (
    ListBusinessReportSchedulesPaginatePaginationConfigTypeDef,
    ListBusinessReportSchedulesPaginateResponseTypeDef,
    ListConferenceProvidersPaginatePaginationConfigTypeDef,
    ListConferenceProvidersPaginateResponseTypeDef,
    ListDeviceEventsPaginatePaginationConfigTypeDef,
    ListDeviceEventsPaginateResponseTypeDef,
    ListSkillsPaginatePaginationConfigTypeDef,
    ListSkillsPaginateResponseTypeDef,
    ListSkillsStoreCategoriesPaginatePaginationConfigTypeDef,
    ListSkillsStoreCategoriesPaginateResponseTypeDef,
    ListSkillsStoreSkillsByCategoryPaginatePaginationConfigTypeDef,
    ListSkillsStoreSkillsByCategoryPaginateResponseTypeDef,
    ListSmartHomeAppliancesPaginatePaginationConfigTypeDef,
    ListSmartHomeAppliancesPaginateResponseTypeDef,
    ListTagsPaginatePaginationConfigTypeDef,
    ListTagsPaginateResponseTypeDef,
    SearchDevicesPaginateFiltersTypeDef,
    SearchDevicesPaginatePaginationConfigTypeDef,
    SearchDevicesPaginateResponseTypeDef,
    SearchDevicesPaginateSortCriteriaTypeDef,
    SearchProfilesPaginateFiltersTypeDef,
    SearchProfilesPaginatePaginationConfigTypeDef,
    SearchProfilesPaginateResponseTypeDef,
    SearchProfilesPaginateSortCriteriaTypeDef,
    SearchRoomsPaginateFiltersTypeDef,
    SearchRoomsPaginatePaginationConfigTypeDef,
    SearchRoomsPaginateResponseTypeDef,
    SearchRoomsPaginateSortCriteriaTypeDef,
    SearchSkillGroupsPaginateFiltersTypeDef,
    SearchSkillGroupsPaginatePaginationConfigTypeDef,
    SearchSkillGroupsPaginateResponseTypeDef,
    SearchSkillGroupsPaginateSortCriteriaTypeDef,
    SearchUsersPaginateFiltersTypeDef,
    SearchUsersPaginatePaginationConfigTypeDef,
    SearchUsersPaginateResponseTypeDef,
    SearchUsersPaginateSortCriteriaTypeDef,
)


__all__ = (
    "ListBusinessReportSchedulesPaginator",
    "ListConferenceProvidersPaginator",
    "ListDeviceEventsPaginator",
    "ListSkillsPaginator",
    "ListSkillsStoreCategoriesPaginator",
    "ListSkillsStoreSkillsByCategoryPaginator",
    "ListSmartHomeAppliancesPaginator",
    "ListTagsPaginator",
    "SearchDevicesPaginator",
    "SearchProfilesPaginator",
    "SearchRoomsPaginator",
    "SearchSkillGroupsPaginator",
    "SearchUsersPaginator",
)


class ListBusinessReportSchedulesPaginator(Boto3Paginator):
    """
    Paginator for `list_business_report_schedules`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: ListBusinessReportSchedulesPaginatePaginationConfigTypeDef = None
    ) -> ListBusinessReportSchedulesPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`AlexaForBusiness.Client.list_business_report_schedules`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/alexaforbusiness-2017-11-09/ListBusinessReportSchedules>`_

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
                'BusinessReportSchedules': [
                    {
                        'ScheduleArn': 'string',
                        'ScheduleName': 'string',
                        'S3BucketName': 'string',
                        'S3KeyPrefix': 'string',
                        'Format': 'CSV'|'CSV_ZIP',
                        'ContentRange': {
                            'Interval': 'ONE_DAY'|'ONE_WEEK'|'THIRTY_DAYS'
                        },
                        'Recurrence': {
                            'StartDate': 'string'
                        },
                        'LastBusinessReport': {
                            'Status': 'RUNNING'|'SUCCEEDED'|'FAILED',
                            'FailureCode': 'ACCESS_DENIED'|'NO_SUCH_BUCKET'|'INTERNAL_FAILURE',
                            'S3Location': {
                                'Path': 'string',
                                'BucketName': 'string'
                            },
                            'DeliveryTime': datetime(2015, 1, 1),
                            'DownloadUrl': 'string'
                        }
                    },
                ],

            }
          **Response Structure**

          - *(dict) --*

            - **BusinessReportSchedules** *(list) --*

              The schedule of the reports.

              - *(dict) --*

                The schedule of the usage report.

                - **ScheduleArn** *(string) --*

                  The ARN of the business report schedule.

                - **ScheduleName** *(string) --*

                  The name identifier of the schedule.

                - **S3BucketName** *(string) --*

                  The S3 bucket name of the output reports.

                - **S3KeyPrefix** *(string) --*

                  The S3 key where the report is delivered.

                - **Format** *(string) --*

                  The format of the generated report (individual CSV files or zipped files of
                  individual files).

                - **ContentRange** *(dict) --*

                  The content range of the reports.

                  - **Interval** *(string) --*

                    The interval of the content range.

                - **Recurrence** *(dict) --*

                  The recurrence of the reports.

                  - **StartDate** *(string) --*

                    The start date.

                - **LastBusinessReport** *(dict) --*

                  The details of the last business report delivery for a specified time interval.

                  - **Status** *(string) --*

                    The status of the report generation execution (RUNNING, SUCCEEDED, or FAILED).

                  - **FailureCode** *(string) --*

                    The failure code.

                  - **S3Location** *(dict) --*

                    The S3 location of the output reports.

                    - **Path** *(string) --*

                      The path of the business report.

                    - **BucketName** *(string) --*

                      The S3 bucket name of the output reports.

                  - **DeliveryTime** *(datetime) --*

                    The time of report delivery.

                  - **DownloadUrl** *(string) --*

                    The download link where a user can download the report.
        """


class ListConferenceProvidersPaginator(Boto3Paginator):
    """
    Paginator for `list_conference_providers`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: ListConferenceProvidersPaginatePaginationConfigTypeDef = None
    ) -> ListConferenceProvidersPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`AlexaForBusiness.Client.list_conference_providers`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/alexaforbusiness-2017-11-09/ListConferenceProviders>`_

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
                'ConferenceProviders': [
                    {
                        'Arn': 'string',
                        'Name': 'string',
                        'Type':
                        'CHIME'|'BLUEJEANS'|'FUZE'|'GOOGLE_HANGOUTS'|'POLYCOM'
                        |'RINGCENTRAL'|'SKYPE_FOR_BUSINESS'|'WEBEX'|'ZOOM'|'CUSTOM',
                        'IPDialIn': {
                            'Endpoint': 'string',
                            'CommsProtocol': 'SIP'|'SIPS'|'H323'
                        },
                        'PSTNDialIn': {
                            'CountryCode': 'string',
                            'PhoneNumber': 'string',
                            'OneClickIdDelay': 'string',
                            'OneClickPinDelay': 'string'
                        },
                        'MeetingSetting': {
                            'RequirePin': 'YES'|'NO'|'OPTIONAL'
                        }
                    },
                ],

            }
          **Response Structure**

          - *(dict) --*

            - **ConferenceProviders** *(list) --*

              The conference providers.

              - *(dict) --*

                An entity that provides a conferencing solution. Alexa for Business acts as the
                voice interface and mediator that connects users to their preferred conference
                provider. Examples of conference providers include Amazon Chime, Zoom, Cisco, and
                Polycom.

                - **Arn** *(string) --*

                  The ARN of the newly created conference provider.

                - **Name** *(string) --*

                  The name of the conference provider.

                - **Type** *(string) --*

                  The type of conference providers.

                - **IPDialIn** *(dict) --*

                  The IP endpoint and protocol for calling.

                  - **Endpoint** *(string) --*

                    The IP address.

                  - **CommsProtocol** *(string) --*

                    The protocol, including SIP, SIPS, and H323.

                - **PSTNDialIn** *(dict) --*

                  The information for PSTN conferencing.

                  - **CountryCode** *(string) --*

                    The zip code.

                  - **PhoneNumber** *(string) --*

                    The phone number to call to join the conference.

                  - **OneClickIdDelay** *(string) --*

                    The delay duration before Alexa enters the conference ID with dual-tone
                    multi-frequency (DTMF). Each number on the dial pad corresponds to a DTMF tone,
                    which is how we send data over the telephone network.

                  - **OneClickPinDelay** *(string) --*

                    The delay duration before Alexa enters the conference pin with dual-tone
                    multi-frequency (DTMF). Each number on the dial pad corresponds to a DTMF tone,
                    which is how we send data over the telephone network.

                - **MeetingSetting** *(dict) --*

                  The meeting settings for the conference provider.

                  - **RequirePin** *(string) --*

                    The values that indicate whether the pin is always required.
        """


class ListDeviceEventsPaginator(Boto3Paginator):
    """
    Paginator for `list_device_events`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        DeviceArn: str,
        EventType: Literal["CONNECTION_STATUS", "DEVICE_STATUS"] = None,
        PaginationConfig: ListDeviceEventsPaginatePaginationConfigTypeDef = None,
    ) -> ListDeviceEventsPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`AlexaForBusiness.Client.list_device_events`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/alexaforbusiness-2017-11-09/ListDeviceEvents>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              DeviceArn='string',
              EventType='CONNECTION_STATUS'|'DEVICE_STATUS',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type DeviceArn: string
        :param DeviceArn: **[REQUIRED]**

          The ARN of a device.

        :type EventType: string
        :param EventType:

          The event type to filter device events. If EventType isn't specified, this returns a list
          of all device events in reverse chronological order. If EventType is specified, this
          returns a list of device events for that EventType in reverse chronological order.

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
                'DeviceEvents': [
                    {
                        'Type': 'CONNECTION_STATUS'|'DEVICE_STATUS',
                        'Value': 'string',
                        'Timestamp': datetime(2015, 1, 1)
                    },
                ],

            }
          **Response Structure**

          - *(dict) --*

            - **DeviceEvents** *(list) --*

              The device events requested for the device ARN.

              - *(dict) --*

                The list of device events.

                - **Type** *(string) --*

                  The type of device event.

                - **Value** *(string) --*

                  The value of the event.

                - **Timestamp** *(datetime) --*

                  The time (in epoch) when the event occurred.
        """


class ListSkillsPaginator(Boto3Paginator):
    """
    Paginator for `list_skills`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        SkillGroupArn: str = None,
        EnablementType: Literal["ENABLED", "PENDING"] = None,
        SkillType: Literal["PUBLIC", "PRIVATE", "ALL"] = None,
        PaginationConfig: ListSkillsPaginatePaginationConfigTypeDef = None,
    ) -> ListSkillsPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`AlexaForBusiness.Client.list_skills`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/alexaforbusiness-2017-11-09/ListSkills>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              SkillGroupArn='string',
              EnablementType='ENABLED'|'PENDING',
              SkillType='PUBLIC'|'PRIVATE'|'ALL',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type SkillGroupArn: string
        :param SkillGroupArn:

          The ARN of the skill group for which to list enabled skills.

        :type EnablementType: string
        :param EnablementType:

          Whether the skill is enabled under the user's account.

        :type SkillType: string
        :param SkillType:

          Whether the skill is publicly available or is a private skill.

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
                'SkillSummaries': [
                    {
                        'SkillId': 'string',
                        'SkillName': 'string',
                        'SupportsLinking': True|False,
                        'EnablementType': 'ENABLED'|'PENDING',
                        'SkillType': 'PUBLIC'|'PRIVATE'
                    },
                ],

            }
          **Response Structure**

          - *(dict) --*

            - **SkillSummaries** *(list) --*

              The list of enabled skills requested. Required.

              - *(dict) --*

                The summary of skills.

                - **SkillId** *(string) --*

                  The ARN of the skill summary.

                - **SkillName** *(string) --*

                  The name of the skill.

                - **SupportsLinking** *(boolean) --*

                  Linking support for a skill.

                - **EnablementType** *(string) --*

                  Whether the skill is enabled under the user's account, or if it requires linking
                  to be used.

                - **SkillType** *(string) --*

                  Whether the skill is publicly available or is a private skill.
        """


class ListSkillsStoreCategoriesPaginator(Boto3Paginator):
    """
    Paginator for `list_skills_store_categories`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: ListSkillsStoreCategoriesPaginatePaginationConfigTypeDef = None
    ) -> ListSkillsStoreCategoriesPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`AlexaForBusiness.Client.list_skills_store_categories`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/alexaforbusiness-2017-11-09/ListSkillsStoreCategories>`_

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
                'CategoryList': [
                    {
                        'CategoryId': 123,
                        'CategoryName': 'string'
                    },
                ],

            }
          **Response Structure**

          - *(dict) --*

            - **CategoryList** *(list) --*

              The list of categories.

              - *(dict) --*

                The skill store category that is shown. Alexa skills are assigned a specific skill
                category during creation, such as News, Social, and Sports.

                - **CategoryId** *(integer) --*

                  The ID of the skill store category.

                - **CategoryName** *(string) --*

                  The name of the skill store category.
        """


class ListSkillsStoreSkillsByCategoryPaginator(Boto3Paginator):
    """
    Paginator for `list_skills_store_skills_by_category`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        CategoryId: int,
        PaginationConfig: ListSkillsStoreSkillsByCategoryPaginatePaginationConfigTypeDef = None,
    ) -> ListSkillsStoreSkillsByCategoryPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`AlexaForBusiness.Client.list_skills_store_skills_by_category`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/alexaforbusiness-2017-11-09/ListSkillsStoreSkillsByCategory>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              CategoryId=123,
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type CategoryId: integer
        :param CategoryId: **[REQUIRED]**

          The category ID for which the skills are being retrieved from the skill store.

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
                'SkillsStoreSkills': [
                    {
                        'SkillId': 'string',
                        'SkillName': 'string',
                        'ShortDescription': 'string',
                        'IconUrl': 'string',
                        'SampleUtterances': [
                            'string',
                        ],
                        'SkillDetails': {
                            'ProductDescription': 'string',
                            'InvocationPhrase': 'string',
                            'ReleaseDate': 'string',
                            'EndUserLicenseAgreement': 'string',
                            'GenericKeywords': [
                                'string',
                            ],
                            'BulletPoints': [
                                'string',
                            ],
                            'NewInThisVersionBulletPoints': [
                                'string',
                            ],
                            'SkillTypes': [
                                'string',
                            ],
                            'Reviews': {
                                'string': 'string'
                            },
                            'DeveloperInfo': {
                                'DeveloperName': 'string',
                                'PrivacyPolicy': 'string',
                                'Email': 'string',
                                'Url': 'string'
                            }
                        },
                        'SupportsLinking': True|False
                    },
                ],

            }
          **Response Structure**

          - *(dict) --*

            - **SkillsStoreSkills** *(list) --*

              The skill store skills.

              - *(dict) --*

                The detailed information about an Alexa skill.

                - **SkillId** *(string) --*

                  The ARN of the skill.

                - **SkillName** *(string) --*

                  The name of the skill.

                - **ShortDescription** *(string) --*

                  Short description about the skill.

                - **IconUrl** *(string) --*

                  The URL where the skill icon resides.

                - **SampleUtterances** *(list) --*

                  Sample utterances that interact with the skill.

                  - *(string) --*

                - **SkillDetails** *(dict) --*

                  Information about the skill.

                  - **ProductDescription** *(string) --*

                    The description of the product.

                  - **InvocationPhrase** *(string) --*

                    The phrase used to trigger the skill.

                  - **ReleaseDate** *(string) --*

                    The date when the skill was released.

                  - **EndUserLicenseAgreement** *(string) --*

                    The URL of the end user license agreement.

                  - **GenericKeywords** *(list) --*

                    The generic keywords associated with the skill that can be used to find a skill.

                    - *(string) --*

                  - **BulletPoints** *(list) --*

                    The details about what the skill supports organized as bullet points.

                    - *(string) --*

                  - **NewInThisVersionBulletPoints** *(list) --*

                    The updates added in bullet points.

                    - *(string) --*

                  - **SkillTypes** *(list) --*

                    The types of skills.

                    - *(string) --*

                  - **Reviews** *(dict) --*

                    The list of reviews for the skill, including Key and Value pair.

                    - *(string) --*

                      - *(string) --*

                  - **DeveloperInfo** *(dict) --*

                    The details about the developer that published the skill.

                    - **DeveloperName** *(string) --*

                      The name of the developer.

                    - **PrivacyPolicy** *(string) --*

                      The URL of the privacy policy.

                    - **Email** *(string) --*

                      The email of the developer.

                    - **Url** *(string) --*

                      The website of the developer.

                - **SupportsLinking** *(boolean) --*

                  Linking support for a skill.
        """


class ListSmartHomeAppliancesPaginator(Boto3Paginator):
    """
    Paginator for `list_smart_home_appliances`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        RoomArn: str,
        PaginationConfig: ListSmartHomeAppliancesPaginatePaginationConfigTypeDef = None,
    ) -> ListSmartHomeAppliancesPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`AlexaForBusiness.Client.list_smart_home_appliances`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/alexaforbusiness-2017-11-09/ListSmartHomeAppliances>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              RoomArn='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type RoomArn: string
        :param RoomArn: **[REQUIRED]**

          The room that the appliances are associated with.

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
                'SmartHomeAppliances': [
                    {
                        'FriendlyName': 'string',
                        'Description': 'string',
                        'ManufacturerName': 'string'
                    },
                ],

            }
          **Response Structure**

          - *(dict) --*

            - **SmartHomeAppliances** *(list) --*

              The smart home appliances.

              - *(dict) --*

                A smart home appliance that can connect to a central system. Any domestic device can
                be a smart appliance.

                - **FriendlyName** *(string) --*

                  The friendly name of the smart home appliance.

                - **Description** *(string) --*

                  The description of the smart home appliance.

                - **ManufacturerName** *(string) --*

                  The name of the manufacturer of the smart home appliance.
        """


class ListTagsPaginator(Boto3Paginator):
    """
    Paginator for `list_tags`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, Arn: str, PaginationConfig: ListTagsPaginatePaginationConfigTypeDef = None
    ) -> ListTagsPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`AlexaForBusiness.Client.list_tags`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/alexaforbusiness-2017-11-09/ListTags>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              Arn='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type Arn: string
        :param Arn: **[REQUIRED]**

          The ARN of the specified resource for which to list tags.

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
                'Tags': [
                    {
                        'Key': 'string',
                        'Value': 'string'
                    },
                ],

            }
          **Response Structure**

          - *(dict) --*

            - **Tags** *(list) --*

              The tags requested for the specified resource.

              - *(dict) --*

                A key-value pair that can be associated with a resource.

                - **Key** *(string) --*

                  The key of a tag. Tag keys are case-sensitive.

                - **Value** *(string) --*

                  The value of a tag. Tag values are case sensitive and can be null.
        """


class SearchDevicesPaginator(Boto3Paginator):
    """
    Paginator for `search_devices`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Filters: List[SearchDevicesPaginateFiltersTypeDef] = None,
        SortCriteria: List[SearchDevicesPaginateSortCriteriaTypeDef] = None,
        PaginationConfig: SearchDevicesPaginatePaginationConfigTypeDef = None,
    ) -> SearchDevicesPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`AlexaForBusiness.Client.search_devices`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/alexaforbusiness-2017-11-09/SearchDevices>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              Filters=[
                  {
                      'Key': 'string',
                      'Values': [
                          'string',
                      ]
                  },
              ],
              SortCriteria=[
                  {
                      'Key': 'string',
                      'Value': 'ASC'|'DESC'
                  },
              ],
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type Filters: list
        :param Filters:

          The filters to use to list a specified set of devices. Supported filter keys are
          DeviceName, DeviceStatus, DeviceStatusDetailCode, RoomName, DeviceType,
          DeviceSerialNumber, UnassociatedOnly, ConnectionStatus (ONLINE and OFFLINE),
          NetworkProfileName, NetworkProfileArn, Feature, and FailureCode.

          - *(dict) --*

            A filter name and value pair that is used to return a more specific list of results.
            Filters can be used to match a set of resources by various criteria.

            - **Key** *(string) --* **[REQUIRED]**

              The key of a filter.

            - **Values** *(list) --* **[REQUIRED]**

              The values of a filter.

              - *(string) --*

        :type SortCriteria: list
        :param SortCriteria:

          The sort order to use in listing the specified set of devices. Supported sort keys are
          DeviceName, DeviceStatus, RoomName, DeviceType, DeviceSerialNumber, ConnectionStatus,
          NetworkProfileName, NetworkProfileArn, Feature, and FailureCode.

          - *(dict) --*

            An object representing a sort criteria.

            - **Key** *(string) --* **[REQUIRED]**

              The sort key of a sort object.

            - **Value** *(string) --* **[REQUIRED]**

              The sort value of a sort object.

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
                'Devices': [
                    {
                        'DeviceArn': 'string',
                        'DeviceSerialNumber': 'string',
                        'DeviceType': 'string',
                        'DeviceName': 'string',
                        'SoftwareVersion': 'string',
                        'MacAddress': 'string',
                        'DeviceStatus': 'READY'|'PENDING'|'WAS_OFFLINE'|'DEREGISTERED'|'FAILED',
                        'NetworkProfileArn': 'string',
                        'NetworkProfileName': 'string',
                        'RoomArn': 'string',
                        'RoomName': 'string',
                        'DeviceStatusInfo': {
                            'DeviceStatusDetails': [
                                {
                                    'Feature':
                                    'BLUETOOTH'|'VOLUME'|'NOTIFICATIONS'
                                    |'LISTS'|'SKILLS'|'NETWORK_PROFILE'
                                    |'SETTINGS'|'ALL',
                                    'Code':
                                    'DEVICE_SOFTWARE_UPDATE_NEEDED'
                                    |'DEVICE_WAS_OFFLINE'
                                    |'CREDENTIALS_ACCESS_FAILURE'
                                    |'TLS_VERSION_MISMATCH'
                                    |'ASSOCIATION_REJECTION'
                                    |'AUTHENTICATION_FAILURE'
                                    |'DHCP_FAILURE'
                                    |'INTERNET_UNAVAILABLE'
                                    |'DNS_FAILURE'|'UNKNOWN_FAILURE'
                                    |'CERTIFICATE_ISSUING_LIMIT_EXCEEDED'|'INVALID_CERTIFICATE_AUTHORITY'|'NETWORK_PROFILE_NOT_FOUND'|'INVALID_PASSWORD_STATE'
                                    |'PASSWORD_NOT_FOUND'
                                },
                            ],
                            'ConnectionStatus': 'ONLINE'|'OFFLINE'
                        }
                    },
                ],
                'TotalCount': 123
            }
          **Response Structure**

          - *(dict) --*

            - **Devices** *(list) --*

              The devices that meet the specified set of filter criteria, in sort order.

              - *(dict) --*

                Device attributes.

                - **DeviceArn** *(string) --*

                  The ARN of a device.

                - **DeviceSerialNumber** *(string) --*

                  The serial number of a device.

                - **DeviceType** *(string) --*

                  The type of a device.

                - **DeviceName** *(string) --*

                  The name of a device.

                - **SoftwareVersion** *(string) --*

                  The software version of a device.

                - **MacAddress** *(string) --*

                  The MAC address of a device.

                - **DeviceStatus** *(string) --*

                  The status of a device.

                - **NetworkProfileArn** *(string) --*

                  The ARN of the network profile associated with a device.

                - **NetworkProfileName** *(string) --*

                  The name of the network profile associated with a device.

                - **RoomArn** *(string) --*

                  The room ARN associated with a device.

                - **RoomName** *(string) --*

                  The name of the room associated with a device.

                - **DeviceStatusInfo** *(dict) --*

                  Detailed information about a device's status.

                  - **DeviceStatusDetails** *(list) --*

                    One or more device status detail descriptions.

                    - *(dict) --*

                      Details of a device’s status.

                      - **Feature** *(string) --*

                        The list of available features on the device.

                      - **Code** *(string) --*

                        The device status detail code.

                  - **ConnectionStatus** *(string) --*

                    The latest available information about the connection status of a device.

            - **TotalCount** *(integer) --*

              The total number of devices returned.
        """


class SearchProfilesPaginator(Boto3Paginator):
    """
    Paginator for `search_profiles`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Filters: List[SearchProfilesPaginateFiltersTypeDef] = None,
        SortCriteria: List[SearchProfilesPaginateSortCriteriaTypeDef] = None,
        PaginationConfig: SearchProfilesPaginatePaginationConfigTypeDef = None,
    ) -> SearchProfilesPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`AlexaForBusiness.Client.search_profiles`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/alexaforbusiness-2017-11-09/SearchProfiles>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              Filters=[
                  {
                      'Key': 'string',
                      'Values': [
                          'string',
                      ]
                  },
              ],
              SortCriteria=[
                  {
                      'Key': 'string',
                      'Value': 'ASC'|'DESC'
                  },
              ],
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type Filters: list
        :param Filters:

          The filters to use to list a specified set of room profiles. Supported filter keys are
          ProfileName and Address. Required.

          - *(dict) --*

            A filter name and value pair that is used to return a more specific list of results.
            Filters can be used to match a set of resources by various criteria.

            - **Key** *(string) --* **[REQUIRED]**

              The key of a filter.

            - **Values** *(list) --* **[REQUIRED]**

              The values of a filter.

              - *(string) --*

        :type SortCriteria: list
        :param SortCriteria:

          The sort order to use in listing the specified set of room profiles. Supported sort keys
          are ProfileName and Address.

          - *(dict) --*

            An object representing a sort criteria.

            - **Key** *(string) --* **[REQUIRED]**

              The sort key of a sort object.

            - **Value** *(string) --* **[REQUIRED]**

              The sort value of a sort object.

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
                'Profiles': [
                    {
                        'ProfileArn': 'string',
                        'ProfileName': 'string',
                        'IsDefault': True|False,
                        'Address': 'string',
                        'Timezone': 'string',
                        'DistanceUnit': 'METRIC'|'IMPERIAL',
                        'TemperatureUnit': 'FAHRENHEIT'|'CELSIUS',
                        'WakeWord': 'ALEXA'|'AMAZON'|'ECHO'|'COMPUTER',
                        'Locale': 'string'
                    },
                ],
                'TotalCount': 123
            }
          **Response Structure**

          - *(dict) --*

            - **Profiles** *(list) --*

              The profiles that meet the specified set of filter criteria, in sort order.

              - *(dict) --*

                The data of a room profile.

                - **ProfileArn** *(string) --*

                  The ARN of a room profile.

                - **ProfileName** *(string) --*

                  The name of a room profile.

                - **IsDefault** *(boolean) --*

                  Retrieves if the profile data is default or not.

                - **Address** *(string) --*

                  The address of a room profile.

                - **Timezone** *(string) --*

                  The time zone of a room profile.

                - **DistanceUnit** *(string) --*

                  The distance unit of a room profile.

                - **TemperatureUnit** *(string) --*

                  The temperature unit of a room profile.

                - **WakeWord** *(string) --*

                  The wake word of a room profile.

                - **Locale** *(string) --*

                  The locale of a room profile. (This is currently available only to a limited
                  preview audience.)

            - **TotalCount** *(integer) --*

              The total number of room profiles returned.
        """


class SearchRoomsPaginator(Boto3Paginator):
    """
    Paginator for `search_rooms`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Filters: List[SearchRoomsPaginateFiltersTypeDef] = None,
        SortCriteria: List[SearchRoomsPaginateSortCriteriaTypeDef] = None,
        PaginationConfig: SearchRoomsPaginatePaginationConfigTypeDef = None,
    ) -> SearchRoomsPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`AlexaForBusiness.Client.search_rooms`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/alexaforbusiness-2017-11-09/SearchRooms>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              Filters=[
                  {
                      'Key': 'string',
                      'Values': [
                          'string',
                      ]
                  },
              ],
              SortCriteria=[
                  {
                      'Key': 'string',
                      'Value': 'ASC'|'DESC'
                  },
              ],
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type Filters: list
        :param Filters:

          The filters to use to list a specified set of rooms. The supported filter keys are
          RoomName and ProfileName.

          - *(dict) --*

            A filter name and value pair that is used to return a more specific list of results.
            Filters can be used to match a set of resources by various criteria.

            - **Key** *(string) --* **[REQUIRED]**

              The key of a filter.

            - **Values** *(list) --* **[REQUIRED]**

              The values of a filter.

              - *(string) --*

        :type SortCriteria: list
        :param SortCriteria:

          The sort order to use in listing the specified set of rooms. The supported sort keys are
          RoomName and ProfileName.

          - *(dict) --*

            An object representing a sort criteria.

            - **Key** *(string) --* **[REQUIRED]**

              The sort key of a sort object.

            - **Value** *(string) --* **[REQUIRED]**

              The sort value of a sort object.

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
                'Rooms': [
                    {
                        'RoomArn': 'string',
                        'RoomName': 'string',
                        'Description': 'string',
                        'ProviderCalendarId': 'string',
                        'ProfileArn': 'string',
                        'ProfileName': 'string'
                    },
                ],
                'TotalCount': 123
            }
          **Response Structure**

          - *(dict) --*

            - **Rooms** *(list) --*

              The rooms that meet the specified set of filter criteria, in sort order.

              - *(dict) --*

                The data of a room.

                - **RoomArn** *(string) --*

                  The ARN of a room.

                - **RoomName** *(string) --*

                  The name of a room.

                - **Description** *(string) --*

                  The description of a room.

                - **ProviderCalendarId** *(string) --*

                  The provider calendar ARN of a room.

                - **ProfileArn** *(string) --*

                  The profile ARN of a room.

                - **ProfileName** *(string) --*

                  The profile name of a room.

            - **TotalCount** *(integer) --*

              The total number of rooms returned.
        """


class SearchSkillGroupsPaginator(Boto3Paginator):
    """
    Paginator for `search_skill_groups`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Filters: List[SearchSkillGroupsPaginateFiltersTypeDef] = None,
        SortCriteria: List[SearchSkillGroupsPaginateSortCriteriaTypeDef] = None,
        PaginationConfig: SearchSkillGroupsPaginatePaginationConfigTypeDef = None,
    ) -> SearchSkillGroupsPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`AlexaForBusiness.Client.search_skill_groups`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/alexaforbusiness-2017-11-09/SearchSkillGroups>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              Filters=[
                  {
                      'Key': 'string',
                      'Values': [
                          'string',
                      ]
                  },
              ],
              SortCriteria=[
                  {
                      'Key': 'string',
                      'Value': 'ASC'|'DESC'
                  },
              ],
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type Filters: list
        :param Filters:

          The filters to use to list a specified set of skill groups. The supported filter key is
          SkillGroupName.

          - *(dict) --*

            A filter name and value pair that is used to return a more specific list of results.
            Filters can be used to match a set of resources by various criteria.

            - **Key** *(string) --* **[REQUIRED]**

              The key of a filter.

            - **Values** *(list) --* **[REQUIRED]**

              The values of a filter.

              - *(string) --*

        :type SortCriteria: list
        :param SortCriteria:

          The sort order to use in listing the specified set of skill groups. The supported sort key
          is SkillGroupName.

          - *(dict) --*

            An object representing a sort criteria.

            - **Key** *(string) --* **[REQUIRED]**

              The sort key of a sort object.

            - **Value** *(string) --* **[REQUIRED]**

              The sort value of a sort object.

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
                'SkillGroups': [
                    {
                        'SkillGroupArn': 'string',
                        'SkillGroupName': 'string',
                        'Description': 'string'
                    },
                ],
                'TotalCount': 123
            }
          **Response Structure**

          - *(dict) --*

            - **SkillGroups** *(list) --*

              The skill groups that meet the filter criteria, in sort order.

              - *(dict) --*

                The attributes of a skill group.

                - **SkillGroupArn** *(string) --*

                  The skill group ARN of a skill group.

                - **SkillGroupName** *(string) --*

                  The skill group name of a skill group.

                - **Description** *(string) --*

                  The description of a skill group.

            - **TotalCount** *(integer) --*

              The total number of skill groups returned.
        """


class SearchUsersPaginator(Boto3Paginator):
    """
    Paginator for `search_users`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Filters: List[SearchUsersPaginateFiltersTypeDef] = None,
        SortCriteria: List[SearchUsersPaginateSortCriteriaTypeDef] = None,
        PaginationConfig: SearchUsersPaginatePaginationConfigTypeDef = None,
    ) -> SearchUsersPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`AlexaForBusiness.Client.search_users`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/alexaforbusiness-2017-11-09/SearchUsers>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              Filters=[
                  {
                      'Key': 'string',
                      'Values': [
                          'string',
                      ]
                  },
              ],
              SortCriteria=[
                  {
                      'Key': 'string',
                      'Value': 'ASC'|'DESC'
                  },
              ],
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type Filters: list
        :param Filters:

          The filters to use for listing a specific set of users. Required. Supported filter keys
          are UserId, FirstName, LastName, Email, and EnrollmentStatus.

          - *(dict) --*

            A filter name and value pair that is used to return a more specific list of results.
            Filters can be used to match a set of resources by various criteria.

            - **Key** *(string) --* **[REQUIRED]**

              The key of a filter.

            - **Values** *(list) --* **[REQUIRED]**

              The values of a filter.

              - *(string) --*

        :type SortCriteria: list
        :param SortCriteria:

          The sort order to use in listing the filtered set of users. Required. Supported sort keys
          are UserId, FirstName, LastName, Email, and EnrollmentStatus.

          - *(dict) --*

            An object representing a sort criteria.

            - **Key** *(string) --* **[REQUIRED]**

              The sort key of a sort object.

            - **Value** *(string) --* **[REQUIRED]**

              The sort value of a sort object.

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
                'Users': [
                    {
                        'UserArn': 'string',
                        'FirstName': 'string',
                        'LastName': 'string',
                        'Email': 'string',
                        'EnrollmentStatus':
                        'INITIALIZED'|'PENDING'|'REGISTERED'|'DISASSOCIATING'
                        |'DEREGISTERING',
                        'EnrollmentId': 'string'
                    },
                ],
                'TotalCount': 123
            }
          **Response Structure**

          - *(dict) --*

            - **Users** *(list) --*

              The users that meet the specified set of filter criteria, in sort order.

              - *(dict) --*

                Information related to a user.

                - **UserArn** *(string) --*

                  The ARN of a user.

                - **FirstName** *(string) --*

                  The first name of a user.

                - **LastName** *(string) --*

                  The last name of a user.

                - **Email** *(string) --*

                  The email of a user.

                - **EnrollmentStatus** *(string) --*

                  The enrollment status of a user.

                - **EnrollmentId** *(string) --*

                  The enrollment ARN of a user.

            - **TotalCount** *(integer) --*

              The total number of users returned.
        """
