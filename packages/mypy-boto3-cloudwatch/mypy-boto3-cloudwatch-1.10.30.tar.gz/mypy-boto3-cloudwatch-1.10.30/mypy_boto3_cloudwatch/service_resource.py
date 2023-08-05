"Main interface for cloudwatch service ServiceResource"
from __future__ import annotations

from datetime import datetime
from typing import Any, List
from boto3.resources.base import ServiceResource as Boto3ServiceResource
from boto3.resources.collection import ResourceCollection
from mypy_boto3.type_defs import Literal

# pylint: disable=import-self
import mypy_boto3_cloudwatch.service_resource as service_resource_scope
from mypy_boto3_cloudwatch.type_defs import (
    AlarmDescribeHistoryResponseTypeDef,
    AlarmsFilterDimensionsTypeDef,
    MetricGetStatisticsDimensionsTypeDef,
    MetricGetStatisticsResponseTypeDef,
    MetricPutAlarmDimensionsTypeDef,
    MetricPutAlarmMetricsTypeDef,
    MetricPutAlarmTagsTypeDef,
    MetricsFilterDimensionsTypeDef,
)


__all__ = (
    "ServiceResource",
    "Alarm",
    "Metric",
    "ServiceResourceAlarmsCollection",
    "ServiceResourceMetricsCollection",
    "MetricAlarmsCollection",
)


class ServiceResource(Boto3ServiceResource):
    alarms: service_resource_scope.ServiceResourceAlarmsCollection
    metrics: service_resource_scope.ServiceResourceMetricsCollection

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def Alarm(self, name: str) -> service_resource_scope.Alarm:
        """
        Creates a Alarm resource.::

          alarm = cloudwatch.Alarm('name')

        :type name: string
        :param name: The Alarm's name identifier. This **must** be set.

        :rtype: :py:class:`CloudWatch.Alarm`
        :returns: A Alarm resource
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def Metric(self, namespace: str, name: str) -> service_resource_scope.Metric:
        """
        Creates a Metric resource.::

          metric = cloudwatch.Metric('namespace','name')

        :type namespace: string
        :param namespace: The Metric's namespace identifier. This **must** be set.
        :type name: string
        :param name: The Metric's name identifier. This **must** be set.

        :rtype: :py:class:`CloudWatch.Metric`
        :returns: A Metric resource
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_available_subresources(self) -> List[str]:
        """
        Returns a list of all the available sub-resources for this
        Resource.

        :returns: A list containing the name of each sub-resource for this
            resource
        :rtype: list of str
        """


class Alarm(Boto3ServiceResource):
    alarm_name: str
    alarm_arn: str
    alarm_description: str
    alarm_configuration_updated_timestamp: datetime
    actions_enabled: bool
    ok_actions: List[Any]
    alarm_actions: List[Any]
    insufficient_data_actions: List[Any]
    state_value: str
    state_reason: str
    state_reason_data: str
    state_updated_timestamp: datetime
    metric_name: str
    namespace: str
    statistic: str
    extended_statistic: str
    dimensions: List[Any]
    period: int
    unit: str
    evaluation_periods: int
    datapoints_to_alarm: int
    threshold: float
    comparison_operator: str
    treat_missing_data: str
    evaluate_low_sample_count_percentile: str
    metrics: List[Any]
    threshold_metric_id: str
    name: str

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete(self, *args: Any, **kwargs: Any) -> None:
        """
        Deletes the specified alarms. You can delete up to 50 alarms in one operation. In the event
        of an error, no alarms are deleted.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/monitoring-2010-08-01/DeleteAlarms>`_

        **Request Syntax**
        ::

          response = alarm.delete()

        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_history(
        self,
        HistoryItemType: Literal["ConfigurationUpdate", "StateUpdate", "Action"] = None,
        StartDate: datetime = None,
        EndDate: datetime = None,
        MaxRecords: int = None,
        NextToken: str = None,
    ) -> AlarmDescribeHistoryResponseTypeDef:
        """
        Retrieves the history for the specified alarm. You can filter the results by date range or
        item type. If an alarm name is not specified, the histories for all alarms are returned.

        CloudWatch retains the history of an alarm even if you delete the alarm.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/monitoring-2010-08-01/DescribeAlarmHistory>`_

        **Request Syntax**
        ::

          response = alarm.describe_history(
              HistoryItemType='ConfigurationUpdate'|'StateUpdate'|'Action',
              StartDate=datetime(2015, 1, 1),
              EndDate=datetime(2015, 1, 1),
              MaxRecords=123,
              NextToken='string'
          )
        :type HistoryItemType: string
        :param HistoryItemType:

          The type of alarm histories to retrieve.

        :type StartDate: datetime
        :param StartDate:

          The starting date to retrieve alarm history.

        :type EndDate: datetime
        :param EndDate:

          The ending date to retrieve alarm history.

        :type MaxRecords: integer
        :param MaxRecords:

          The maximum number of alarm history records to retrieve.

        :type NextToken: string
        :param NextToken:

          The token returned by a previous call to indicate that there is more data available.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'AlarmHistoryItems': [
                    {
                        'AlarmName': 'string',
                        'Timestamp': datetime(2015, 1, 1),
                        'HistoryItemType': 'ConfigurationUpdate'|'StateUpdate'|'Action',
                        'HistorySummary': 'string',
                        'HistoryData': 'string'
                    },
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **AlarmHistoryItems** *(list) --*

              The alarm histories, in JSON format.

              - *(dict) --*

                Represents the history of a specific alarm.

                - **AlarmName** *(string) --*

                  The descriptive name for the alarm.

                - **Timestamp** *(datetime) --*

                  The time stamp for the alarm history item.

                - **HistoryItemType** *(string) --*

                  The type of alarm history item.

                - **HistorySummary** *(string) --*

                  A summary of the alarm history, in text format.

                - **HistoryData** *(string) --*

                  Data about the alarm, in JSON format.

            - **NextToken** *(string) --*

              The token that marks the start of the next batch of returned results.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def disable_actions(self, *args: Any, **kwargs: Any) -> None:
        """
        Disables the actions for the specified alarms. When an alarm's actions are disabled, the
        alarm actions do not execute when the alarm state changes.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/monitoring-2010-08-01/DisableAlarmActions>`_

        **Request Syntax**
        ::

          response = alarm.disable_actions()

        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def enable_actions(self, *args: Any, **kwargs: Any) -> None:
        """
        Enables the actions for the specified alarms.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/monitoring-2010-08-01/EnableAlarmActions>`_

        **Request Syntax**
        ::

          response = alarm.enable_actions()

        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_available_subresources(self) -> List[str]:
        """
        Returns a list of all the available sub-resources for this
        Resource.

        :returns: A list containing the name of each sub-resource for this
            resource
        :rtype: list of str
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def load(self, *args: Any, **kwargs: Any) -> None:
        """
        Calls :py:meth:`CloudWatch.Client.describe_alarms` to update the attributes of the Alarm
        resource. Note that the load and reload methods are the same method and can be used
        interchangeably.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/monitoring-2010-08-01/None>`_

        **Request Syntax**

        ::

          alarm.load()
        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def reload(self, *args: Any, **kwargs: Any) -> None:
        """
        Calls :py:meth:`CloudWatch.Client.describe_alarms` to update the attributes of the Alarm
        resource. Note that the load and reload methods are the same method and can be used
        interchangeably.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/monitoring-2010-08-01/None>`_

        **Request Syntax**

        ::

          alarm.load()
        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def set_state(
        self,
        StateValue: Literal["OK", "ALARM", "INSUFFICIENT_DATA"],
        StateReason: str,
        StateReasonData: str = None,
    ) -> None:
        """
        Temporarily sets the state of an alarm for testing purposes. When the updated state differs
        from the previous value, the action configured for the appropriate state is invoked. For
        example, if your alarm is configured to send an Amazon SNS message when an alarm is
        triggered, temporarily changing the alarm state to ``ALARM`` sends an SNS message. The alarm
        returns to its actual state (often within seconds). Because the alarm state change happens
        quickly, it is typically only visible in the alarm's **History** tab in the Amazon
        CloudWatch console or through  DescribeAlarmHistory .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/monitoring-2010-08-01/SetAlarmState>`_

        **Request Syntax**
        ::

          response = alarm.set_state(
              StateValue='OK'|'ALARM'|'INSUFFICIENT_DATA',
              StateReason='string',
              StateReasonData='string'
          )
        :type StateValue: string
        :param StateValue: **[REQUIRED]**

          The value of the state.

        :type StateReason: string
        :param StateReason: **[REQUIRED]**

          The reason that this alarm is set to this specific state, in text format.

        :type StateReasonData: string
        :param StateReasonData:

          The reason that this alarm is set to this specific state, in JSON format.

        :returns: None
        """


class Metric(Boto3ServiceResource):
    metric_name: str
    dimensions: List[Any]
    namespace: str
    name: str
    alarms: service_resource_scope.MetricAlarmsCollection

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_available_subresources(self) -> List[str]:
        """
        Returns a list of all the available sub-resources for this
        Resource.

        :returns: A list containing the name of each sub-resource for this
            resource
        :rtype: list of str
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_statistics(
        self,
        StartTime: datetime,
        EndTime: datetime,
        Period: int,
        Dimensions: List[MetricGetStatisticsDimensionsTypeDef] = None,
        Statistics: List[Literal["SampleCount", "Average", "Sum", "Minimum", "Maximum"]] = None,
        ExtendedStatistics: List[str] = None,
        Unit: Literal[
            "Seconds",
            "Microseconds",
            "Milliseconds",
            "Bytes",
            "Kilobytes",
            "Megabytes",
            "Gigabytes",
            "Terabytes",
            "Bits",
            "Kilobits",
            "Megabits",
            "Gigabits",
            "Terabits",
            "Percent",
            "Count",
            "Bytes/Second",
            "Kilobytes/Second",
            "Megabytes/Second",
            "Gigabytes/Second",
            "Terabytes/Second",
            "Bits/Second",
            "Kilobits/Second",
            "Megabits/Second",
            "Gigabits/Second",
            "Terabits/Second",
            "Count/Second",
            "None",
        ] = None,
    ) -> MetricGetStatisticsResponseTypeDef:
        """
        Gets statistics for the specified metric.

        The maximum number of data points returned from a single call is 1,440. If you request more
        than 1,440 data points, CloudWatch returns an error. To reduce the number of data points,
        you can narrow the specified time range and make multiple requests across adjacent time
        ranges, or you can increase the specified period. Data points are not returned in
        chronological order.

        CloudWatch aggregates data points based on the length of the period that you specify. For
        example, if you request statistics with a one-hour period, CloudWatch aggregates all data
        points with time stamps that fall within each one-hour period. Therefore, the number of
        values aggregated by CloudWatch is larger than the number of data points returned.

        CloudWatch needs raw data points to calculate percentile statistics. If you publish data
        using a statistic set instead, you can only retrieve percentile statistics for this data if
        one of the following conditions is true:

        * The SampleCount value of the statistic set is 1.

        * The Min and the Max values of the statistic set are equal.

        Percentile statistics are not available for metrics when any of the metric values are
        negative numbers.

        Amazon CloudWatch retains metric data as follows:

        * Data points with a period of less than 60 seconds are available for 3 hours. These data
        points are high-resolution metrics and are available only for custom metrics that have been
        defined with a ``StorageResolution`` of 1.

        * Data points with a period of 60 seconds (1-minute) are available for 15 days.

        * Data points with a period of 300 seconds (5-minute) are available for 63 days.

        * Data points with a period of 3600 seconds (1 hour) are available for 455 days (15 months).

        Data points that are initially published with a shorter period are aggregated together for
        long-term storage. For example, if you collect data using a period of 1 minute, the data
        remains available for 15 days with 1-minute resolution. After 15 days, this data is still
        available, but is aggregated and retrievable only with a resolution of 5 minutes. After 63
        days, the data is further aggregated and is available with a resolution of 1 hour.

        CloudWatch started retaining 5-minute and 1-hour metric data as of July 9, 2016.

        For information about metrics and dimensions supported by AWS services, see the `Amazon
        CloudWatch Metrics and Dimensions Reference
        <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CW_Support_For_AWS.html>`__
        in the *Amazon CloudWatch User Guide* .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/monitoring-2010-08-01/GetMetricStatistics>`_

        **Request Syntax**
        ::

          response = metric.get_statistics(
              Dimensions=[
                  {
                      'Name': 'string',
                      'Value': 'string'
                  },
              ],
              StartTime=datetime(2015, 1, 1),
              EndTime=datetime(2015, 1, 1),
              Period=123,
              Statistics=[
                  'SampleCount'|'Average'|'Sum'|'Minimum'|'Maximum',
              ],
              ExtendedStatistics=[
                  'string',
              ],
              Unit=
                  'Seconds'|'Microseconds'|'Milliseconds'|'Bytes'|'Kilobytes'|'Megabytes'
                  |'Gigabytes'|'Terabytes'|'Bits'|'Kilobits'|'Megabits'|'Gigabits'|'Terabits'
                  |'Percent'|'Count'|'Bytes/Second'|'Kilobytes/Second'|'Megabytes/Second'
                  |'Gigabytes/Second'|'Terabytes/Second'|'Bits/Second'|'Kilobits/Second'
                  |'Megabits/Second'|'Gigabits/Second'|'Terabits/Second'|'Count/Second'|'None'
          )
        :type Dimensions: list
        :param Dimensions:

          The dimensions. If the metric contains multiple dimensions, you must include a value for
          each dimension. CloudWatch treats each unique combination of dimensions as a separate
          metric. If a specific combination of dimensions was not published, you can't retrieve
          statistics for it. You must specify the same dimensions that were used when the metrics
          were created. For an example, see `Dimension Combinations
          <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.html#dimension-combinations>`__
          in the *Amazon CloudWatch User Guide* . For more information about specifying dimensions,
          see `Publishing Metrics
          <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/publishingMetrics.html>`__
          in the *Amazon CloudWatch User Guide* .

          - *(dict) --*

            Expands the identity of a metric.

            - **Name** *(string) --* **[REQUIRED]**

              The name of the dimension.

            - **Value** *(string) --* **[REQUIRED]**

              The value representing the dimension measurement.

        :type StartTime: datetime
        :param StartTime: **[REQUIRED]**

          The time stamp that determines the first data point to return. Start times are evaluated
          relative to the time that CloudWatch receives the request.

          The value specified is inclusive; results include data points with the specified time
          stamp. In a raw HTTP query, the time stamp must be in ISO 8601 UTC format (for example,
          2016-10-03T23:00:00Z).

          CloudWatch rounds the specified time stamp as follows:

          * Start time less than 15 days ago - Round down to the nearest whole minute. For example,
          12:32:34 is rounded down to 12:32:00.

          * Start time between 15 and 63 days ago - Round down to the nearest 5-minute clock
          interval. For example, 12:32:34 is rounded down to 12:30:00.

          * Start time greater than 63 days ago - Round down to the nearest 1-hour clock interval.
          For example, 12:32:34 is rounded down to 12:00:00.

          If you set ``Period`` to 5, 10, or 30, the start time of your request is rounded down to
          the nearest time that corresponds to even 5-, 10-, or 30-second divisions of a minute. For
          example, if you make a query at (HH:mm:ss) 01:05:23 for the previous 10-second period, the
          start time of your request is rounded down and you receive data from 01:05:10 to 01:05:20.
          If you make a query at 15:07:17 for the previous 5 minutes of data, using a period of 5
          seconds, you receive data timestamped between 15:02:15 and 15:07:15.

        :type EndTime: datetime
        :param EndTime: **[REQUIRED]**

          The time stamp that determines the last data point to return.

          The value specified is exclusive; results include data points up to the specified time
          stamp. In a raw HTTP query, the time stamp must be in ISO 8601 UTC format (for example,
          2016-10-10T23:00:00Z).

        :type Period: integer
        :param Period: **[REQUIRED]**

          The granularity, in seconds, of the returned data points. For metrics with regular
          resolution, a period can be as short as one minute (60 seconds) and must be a multiple of
          60. For high-resolution metrics that are collected at intervals of less than one minute,
          the period can be 1, 5, 10, 30, 60, or any multiple of 60. High-resolution metrics are
          those metrics stored by a ``PutMetricData`` call that includes a ``StorageResolution`` of
          1 second.

          If the ``StartTime`` parameter specifies a time stamp that is greater than 3 hours ago,
          you must specify the period as follows or no data points in that time range is returned:

          * Start time between 3 hours and 15 days ago - Use a multiple of 60 seconds (1 minute).

          * Start time between 15 and 63 days ago - Use a multiple of 300 seconds (5 minutes).

          * Start time greater than 63 days ago - Use a multiple of 3600 seconds (1 hour).

        :type Statistics: list
        :param Statistics:

          The metric statistics, other than percentile. For percentile statistics, use
          ``ExtendedStatistics`` . When calling ``GetMetricStatistics`` , you must specify either
          ``Statistics`` or ``ExtendedStatistics`` , but not both.

          - *(string) --*

        :type ExtendedStatistics: list
        :param ExtendedStatistics:

          The percentile statistics. Specify values between p0.0 and p100. When calling
          ``GetMetricStatistics`` , you must specify either ``Statistics`` or ``ExtendedStatistics``
          , but not both. Percentile statistics are not available for metrics when any of the metric
          values are negative numbers.

          - *(string) --*

        :type Unit: string
        :param Unit:

          The unit for a given metric. If you omit ``Unit`` , all data that was collected with any
          unit is returned, along with the corresponding units that were specified when the data was
          reported to CloudWatch. If you specify a unit, the operation returns only data data that
          was collected with that unit specified. If you specify a unit that does not match the data
          collected, the results of the operation are null. CloudWatch does not perform unit
          conversions.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Label': 'string',
                'Datapoints': [
                    {
                        'Timestamp': datetime(2015, 1, 1),
                        'SampleCount': 123.0,
                        'Average': 123.0,
                        'Sum': 123.0,
                        'Minimum': 123.0,
                        'Maximum': 123.0,
                        'Unit':
                        'Seconds'|'Microseconds'|'Milliseconds'|'Bytes'|'Kilobytes'
                        |'Megabytes'|'Gigabytes'|'Terabytes'|'Bits'|'Kilobits'
                        |'Megabits'|'Gigabits'|'Terabits'|'Percent'|'Count'
                        |'Bytes/Second'|'Kilobytes/Second'|'Megabytes/Second'
                        |'Gigabytes/Second'|'Terabytes/Second'|'Bits/Second'
                        |'Kilobits/Second'|'Megabits/Second'|'Gigabits/Second'
                        |'Terabits/Second'|'Count/Second'|'None',
                        'ExtendedStatistics': {
                            'string': 123.0
                        }
                    },
                ]
            }
          **Response Structure**

          - *(dict) --*

            - **Label** *(string) --*

              A label for the specified metric.

            - **Datapoints** *(list) --*

              The data points for the specified metric.

              - *(dict) --*

                Encapsulates the statistical data that CloudWatch computes from metric data.

                - **Timestamp** *(datetime) --*

                  The time stamp used for the data point.

                - **SampleCount** *(float) --*

                  The number of metric values that contributed to the aggregate value of this data
                  point.

                - **Average** *(float) --*

                  The average of the metric values that correspond to the data point.

                - **Sum** *(float) --*

                  The sum of the metric values for the data point.

                - **Minimum** *(float) --*

                  The minimum metric value for the data point.

                - **Maximum** *(float) --*

                  The maximum metric value for the data point.

                - **Unit** *(string) --*

                  The standard unit for the data point.

                - **ExtendedStatistics** *(dict) --*

                  The percentile statistic for the data point.

                  - *(string) --*

                    - *(float) --*
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def load(self, *args: Any, **kwargs: Any) -> None:
        """
        Calls :py:meth:`CloudWatch.Client.list_metrics` to update the attributes of the Metric
        resource. Note that the load and reload methods are the same method and can be used
        interchangeably.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/monitoring-2010-08-01/None>`_

        **Request Syntax**

        ::

          metric.load()
        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def put_alarm(
        self,
        AlarmName: str,
        EvaluationPeriods: int,
        ComparisonOperator: Literal[
            "GreaterThanOrEqualToThreshold",
            "GreaterThanThreshold",
            "LessThanThreshold",
            "LessThanOrEqualToThreshold",
            "LessThanLowerOrGreaterThanUpperThreshold",
            "LessThanLowerThreshold",
            "GreaterThanUpperThreshold",
        ],
        AlarmDescription: str = None,
        ActionsEnabled: bool = None,
        OKActions: List[str] = None,
        AlarmActions: List[str] = None,
        InsufficientDataActions: List[str] = None,
        Statistic: Literal["SampleCount", "Average", "Sum", "Minimum", "Maximum"] = None,
        ExtendedStatistic: str = None,
        Dimensions: List[MetricPutAlarmDimensionsTypeDef] = None,
        Period: int = None,
        Unit: Literal[
            "Seconds",
            "Microseconds",
            "Milliseconds",
            "Bytes",
            "Kilobytes",
            "Megabytes",
            "Gigabytes",
            "Terabytes",
            "Bits",
            "Kilobits",
            "Megabits",
            "Gigabits",
            "Terabits",
            "Percent",
            "Count",
            "Bytes/Second",
            "Kilobytes/Second",
            "Megabytes/Second",
            "Gigabytes/Second",
            "Terabytes/Second",
            "Bits/Second",
            "Kilobits/Second",
            "Megabits/Second",
            "Gigabits/Second",
            "Terabits/Second",
            "Count/Second",
            "None",
        ] = None,
        DatapointsToAlarm: int = None,
        Threshold: float = None,
        TreatMissingData: str = None,
        EvaluateLowSampleCountPercentile: str = None,
        Metrics: List[MetricPutAlarmMetricsTypeDef] = None,
        Tags: List[MetricPutAlarmTagsTypeDef] = None,
        ThresholdMetricId: str = None,
    ) -> service_resource_scope.Alarm:
        """
        Creates or updates an alarm and associates it with the specified metric, metric math
        expression, or anomaly detection model.

        Alarms based on anomaly detection models cannot have Auto Scaling actions.

        When this operation creates an alarm, the alarm state is immediately set to
        ``INSUFFICIENT_DATA`` . The alarm is then evaluated and its state is set appropriately. Any
        actions associated with the new state are then executed.

        When you update an existing alarm, its state is left unchanged, but the update completely
        overwrites the previous configuration of the alarm.

        If you are an IAM user, you must have Amazon EC2 permissions for some alarm operations:

        * ``iam:CreateServiceLinkedRole`` for all alarms with EC2 actions

        * ``ec2:DescribeInstanceStatus`` and ``ec2:DescribeInstances`` for all alarms on EC2
        instance status metrics

        * ``ec2:StopInstances`` for alarms with stop actions

        * ``ec2:TerminateInstances`` for alarms with terminate actions

        * No specific permissions are needed for alarms with recover actions

        If you have read/write permissions for Amazon CloudWatch but not for Amazon EC2, you can
        still create an alarm, but the stop or terminate actions are not performed. However, if you
        are later granted the required permissions, the alarm actions that you created earlier are
        performed.

        If you are using an IAM role (for example, an EC2 instance profile), you cannot stop or
        terminate the instance using alarm actions. However, you can still see the alarm state and
        perform any other actions such as Amazon SNS notifications or Auto Scaling policies.

        If you are using temporary security credentials granted using AWS STS, you cannot stop or
        terminate an EC2 instance using alarm actions.

        The first time you create an alarm in the AWS Management Console, the CLI, or by using the
        PutMetricAlarm API, CloudWatch creates the necessary service-linked role for you. The
        service-linked role is called ``AWSServiceRoleForCloudWatchEvents`` . For more information,
        see `AWS service-linked role
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_terms-and-concepts.html#iam-term-service-linked-role>`__
        .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/monitoring-2010-08-01/PutMetricAlarm>`_

        **Request Syntax**
        ::

          alarm = metric.put_alarm(
              AlarmName='string',
              AlarmDescription='string',
              ActionsEnabled=True|False,
              OKActions=[
                  'string',
              ],
              AlarmActions=[
                  'string',
              ],
              InsufficientDataActions=[
                  'string',
              ],
              Statistic='SampleCount'|'Average'|'Sum'|'Minimum'|'Maximum',
              ExtendedStatistic='string',
              Dimensions=[
                  {
                      'Name': 'string',
                      'Value': 'string'
                  },
              ],
              Period=123,
              Unit=
                  'Seconds'|'Microseconds'|'Milliseconds'|'Bytes'|'Kilobytes'|'Megabytes'
                  |'Gigabytes'|'Terabytes'|'Bits'|'Kilobits'|'Megabits'|'Gigabits'|'Terabits'
                  |'Percent'|'Count'|'Bytes/Second'|'Kilobytes/Second'|'Megabytes/Second'
                  |'Gigabytes/Second'|'Terabytes/Second'|'Bits/Second'|'Kilobits/Second'
                  |'Megabits/Second'|'Gigabits/Second'|'Terabits/Second'|'Count/Second'|'None',
              EvaluationPeriods=123,
              DatapointsToAlarm=123,
              Threshold=123.0,
              ComparisonOperator=
                  'GreaterThanOrEqualToThreshold'|'GreaterThanThreshold'|'LessThanThreshold'
                  |'LessThanOrEqualToThreshold'|'LessThanLowerOrGreaterThanUpperThreshold'
                  |'LessThanLowerThreshold'|'GreaterThanUpperThreshold',
              TreatMissingData='string',
              EvaluateLowSampleCountPercentile='string',
              Metrics=[
                  {
                      'Id': 'string',
                      'MetricStat': {
                          'Metric': {
                              'Namespace': 'string',
                              'MetricName': 'string',
                              'Dimensions': [
                                  {
                                      'Name': 'string',
                                      'Value': 'string'
                                  },
                              ]
                          },
                          'Period': 123,
                          'Stat': 'string',
                          'Unit':
                          'Seconds'|'Microseconds'|'Milliseconds'|'Bytes'
                          |'Kilobytes'|'Megabytes'|'Gigabytes'|'Terabytes'|'Bits'
                          |'Kilobits'|'Megabits'|'Gigabits'|'Terabits'|'Percent'
                          |'Count'|'Bytes/Second'|'Kilobytes/Second'
                          |'Megabytes/Second'|'Gigabytes/Second'
                          |'Terabytes/Second'|'Bits/Second'|'Kilobits/Second'
                          |'Megabits/Second'|'Gigabits/Second'|'Terabits/Second'
                          |'Count/Second'|'None'
                      },
                      'Expression': 'string',
                      'Label': 'string',
                      'ReturnData': True|False,
                      'Period': 123
                  },
              ],
              Tags=[
                  {
                      'Key': 'string',
                      'Value': 'string'
                  },
              ],
              ThresholdMetricId='string'
          )
        :type AlarmName: string
        :param AlarmName: **[REQUIRED]**

          The name for the alarm. This name must be unique within your AWS account.

        :type AlarmDescription: string
        :param AlarmDescription:

          The description for the alarm.

        :type ActionsEnabled: boolean
        :param ActionsEnabled:

          Indicates whether actions should be executed during any changes to the alarm state. The
          default is ``TRUE`` .

        :type OKActions: list
        :param OKActions:

          The actions to execute when this alarm transitions to an ``OK`` state from any other
          state. Each action is specified as an Amazon Resource Name (ARN).

          Valid Values: ``arn:aws:automate:*region* :ec2:stop`` | ``arn:aws:automate:*region*
          :ec2:terminate`` | ``arn:aws:automate:*region* :ec2:recover`` |
          ``arn:aws:automate:*region* :ec2:reboot`` | ``arn:aws:sns:*region* :*account-id*
          :*sns-topic-name* `` | ``arn:aws:autoscaling:*region* :*account-id*
          :scalingPolicy:*policy-id* autoScalingGroupName/*group-friendly-name*
          :policyName/*policy-friendly-name* ``

          Valid Values (for use with IAM roles): ``arn:aws:swf:*region* :*account-id*
          :action/actions/AWS_EC2.InstanceId.Stop/1.0`` | ``arn:aws:swf:*region* :*account-id*
          :action/actions/AWS_EC2.InstanceId.Terminate/1.0``
          | ``arn:aws:swf:*region* :*account-id*
          :action/actions/AWS_EC2.InstanceId.Reboot/1.0``

          - *(string) --*

        :type AlarmActions: list
        :param AlarmActions:

          The actions to execute when this alarm transitions to the ``ALARM`` state from any other
          state. Each action is specified as an Amazon Resource Name (ARN).

          Valid Values: ``arn:aws:automate:*region* :ec2:stop`` | ``arn:aws:automate:*region*
          :ec2:terminate`` | ``arn:aws:automate:*region* :ec2:recover`` |
          ``arn:aws:automate:*region* :ec2:reboot`` | ``arn:aws:sns:*region* :*account-id*
          :*sns-topic-name* `` | ``arn:aws:autoscaling:*region* :*account-id*
          :scalingPolicy:*policy-id* autoScalingGroupName/*group-friendly-name*
          :policyName/*policy-friendly-name* ``

          Valid Values (for use with IAM roles): ``arn:aws:swf:*region* :*account-id*
          :action/actions/AWS_EC2.InstanceId.Stop/1.0`` | ``arn:aws:swf:*region* :*account-id*
          :action/actions/AWS_EC2.InstanceId.Terminate/1.0``
          | ``arn:aws:swf:*region* :*account-id*
          :action/actions/AWS_EC2.InstanceId.Reboot/1.0``

          - *(string) --*

        :type InsufficientDataActions: list
        :param InsufficientDataActions:

          The actions to execute when this alarm transitions to the ``INSUFFICIENT_DATA`` state from
          any other state. Each action is specified as an Amazon Resource Name (ARN).

          Valid Values: ``arn:aws:automate:*region* :ec2:stop`` | ``arn:aws:automate:*region*
          :ec2:terminate`` | ``arn:aws:automate:*region* :ec2:recover`` |
          ``arn:aws:automate:*region* :ec2:reboot`` | ``arn:aws:sns:*region* :*account-id*
          :*sns-topic-name* `` | ``arn:aws:autoscaling:*region* :*account-id*
          :scalingPolicy:*policy-id* autoScalingGroupName/*group-friendly-name*
          :policyName/*policy-friendly-name* ``

          Valid Values (for use with IAM roles): ``>arn:aws:swf:*region* :*account-id*
          :action/actions/AWS_EC2.InstanceId.Stop/1.0`` | ``arn:aws:swf:*region* :*account-id*
          :action/actions/AWS_EC2.InstanceId.Terminate/1.0``
          | ``arn:aws:swf:*region* :*account-id*
          :action/actions/AWS_EC2.InstanceId.Reboot/1.0``

          - *(string) --*

        :type Statistic: string
        :param Statistic:

          The statistic for the metric specified in ``MetricName`` , other than percentile. For
          percentile statistics, use ``ExtendedStatistic`` . When you call ``PutMetricAlarm`` and
          specify a ``MetricName`` , you must specify either ``Statistic`` or ``ExtendedStatistic,``
          but not both.

        :type ExtendedStatistic: string
        :param ExtendedStatistic:

          The percentile statistic for the metric specified in ``MetricName`` . Specify a value
          between p0.0 and p100. When you call ``PutMetricAlarm`` and specify a ``MetricName`` , you
          must specify either ``Statistic`` or ``ExtendedStatistic,`` but not both.

        :type Dimensions: list
        :param Dimensions:

          The dimensions for the metric specified in ``MetricName`` .

          - *(dict) --*

            Expands the identity of a metric.

            - **Name** *(string) --* **[REQUIRED]**

              The name of the dimension.

            - **Value** *(string) --* **[REQUIRED]**

              The value representing the dimension measurement.

        :type Period: integer
        :param Period:

          The length, in seconds, used each time the metric specified in ``MetricName`` is
          evaluated. Valid values are 10, 30, and any multiple of 60.

           ``Period`` is required for alarms based on static thresholds. If you are creating an
           alarm based on a metric math expression, you specify the period for each metric within
           the objects in the ``Metrics`` array.

          Be sure to specify 10 or 30 only for metrics that are stored by a ``PutMetricData`` call
          with a ``StorageResolution`` of 1. If you specify a period of 10 or 30 for a metric that
          does not have sub-minute resolution, the alarm still attempts to gather data at the period
          rate that you specify. In this case, it does not receive data for the attempts that do not
          correspond to a one-minute data resolution, and the alarm may often lapse into
          INSUFFICENT_DATA status. Specifying 10 or 30 also sets this alarm as a high-resolution
          alarm, which has a higher charge than other alarms. For more information about pricing,
          see `Amazon CloudWatch Pricing <https://aws.amazon.com/cloudwatch/pricing/>`__ .

          An alarm's total current evaluation period can be no longer than one day, so ``Period``
          multiplied by ``EvaluationPeriods`` cannot be more than 86,400 seconds.

        :type Unit: string
        :param Unit:

          The unit of measure for the statistic. For example, the units for the Amazon EC2 NetworkIn
          metric are Bytes because NetworkIn tracks the number of bytes that an instance receives on
          all network interfaces. You can also specify a unit when you create a custom metric. Units
          help provide conceptual meaning to your data. Metric data points that specify a unit of
          measure, such as Percent, are aggregated separately.

          If you don't specify ``Unit`` , CloudWatch retrieves all unit types that have been
          published for the metric and attempts to evaluate the alarm. Usually metrics are published
          with only one unit, so the alarm will work as intended.

          However, if the metric is published with multiple types of units and you don't specify a
          unit, the alarm's behavior is not defined and will behave un-predictably.

          We recommend omitting ``Unit`` so that you don't inadvertently specify an incorrect unit
          that is not published for this metric. Doing so causes the alarm to be stuck in the
          ``INSUFFICIENT DATA`` state.

        :type EvaluationPeriods: integer
        :param EvaluationPeriods: **[REQUIRED]**

          The number of periods over which data is compared to the specified threshold. If you are
          setting an alarm that requires that a number of consecutive data points be breaching to
          trigger the alarm, this value specifies that number. If you are setting an "M out of N"
          alarm, this value is the N.

          An alarm's total current evaluation period can be no longer than one day, so this number
          multiplied by ``Period`` cannot be more than 86,400 seconds.

        :type DatapointsToAlarm: integer
        :param DatapointsToAlarm:

          The number of data points that must be breaching to trigger the alarm. This is used only
          if you are setting an "M out of N" alarm. In that case, this value is the M. For more
          information, see `Evaluating an Alarm
          <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html#alarm-evaluation>`__
          in the *Amazon CloudWatch User Guide* .

        :type Threshold: float
        :param Threshold:

          The value against which the specified statistic is compared.

          This parameter is required for alarms based on static thresholds, but should not be used
          for alarms based on anomaly detection models.

        :type ComparisonOperator: string
        :param ComparisonOperator: **[REQUIRED]**

          The arithmetic operation to use when comparing the specified statistic and threshold. The
          specified statistic value is used as the first operand.

          The values ``LessThanLowerOrGreaterThanUpperThreshold`` , ``LessThanLowerThreshold`` , and
          ``GreaterThanUpperThreshold`` are used only for alarms based on anomaly detection models.

        :type TreatMissingData: string
        :param TreatMissingData:

          Sets how this alarm is to handle missing data points. If ``TreatMissingData`` is omitted,
          the default behavior of ``missing`` is used. For more information, see `Configuring How
          CloudWatch Alarms Treats Missing Data
          <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html#alarms-and-missing-data>`__
          .

          Valid Values: ``breaching | notBreaching | ignore | missing``

        :type EvaluateLowSampleCountPercentile: string
        :param EvaluateLowSampleCountPercentile:

          Used only for alarms based on percentiles. If you specify ``ignore`` , the alarm state
          does not change during periods with too few data points to be statistically significant.
          If you specify ``evaluate`` or omit this parameter, the alarm is always evaluated and
          possibly changes state no matter how many data points are available. For more information,
          see `Percentile-Based CloudWatch Alarms and Low Data Samples
          <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html#percentiles-with-low-samples>`__
          .

          Valid Values: ``evaluate | ignore``

        :type Metrics: list
        :param Metrics:

          An array of ``MetricDataQuery`` structures that enable you to create an alarm based on the
          result of a metric math expression. For each ``PutMetricAlarm`` operation, you must
          specify either ``MetricName`` or a ``Metrics`` array.

          Each item in the ``Metrics`` array either retrieves a metric or performs a math
          expression.

          One item in the ``Metrics`` array is the expression that the alarm watches. You designate
          this expression by setting ``ReturnValue`` to true for this object in the array. For more
          information, see  MetricDataQuery .

          If you use the ``Metrics`` parameter, you cannot include the ``MetricName`` ,
          ``Dimensions`` , ``Period`` , ``Namespace`` , ``Statistic`` , or ``ExtendedStatistic``
          parameters of ``PutMetricAlarm`` in the same operation. Instead, you retrieve the metrics
          you are using in your math expression as part of the ``Metrics`` array.

          - *(dict) --*

            This structure is used in both ``GetMetricData`` and ``PutMetricAlarm`` . The supported
            use of this structure is different for those two operations.

            When used in ``GetMetricData`` , it indicates the metric data to return, and whether
            this call is just retrieving a batch set of data for one metric, or is performing a math
            expression on metric data. A single ``GetMetricData`` call can include up to 100
            ``MetricDataQuery`` structures.

            When used in ``PutMetricAlarm`` , it enables you to create an alarm based on a metric
            math expression. Each ``MetricDataQuery`` in the array specifies either a metric to
            retrieve, or a math expression to be performed on retrieved metrics. A single
            ``PutMetricAlarm`` call can include up to 20 ``MetricDataQuery`` structures in the
            array. The 20 structures can include as many as 10 structures that contain a
            ``MetricStat`` parameter to retrieve a metric, and as many as 10 structures that contain
            the ``Expression`` parameter to perform a math expression. Of those ``Expression``
            structures, one must have ``True`` as the value for ``ReturnData`` . The result of this
            expression is the value the alarm watches.

            Any expression used in a ``PutMetricAlarm`` operation must return a single time series.
            For more information, see `Metric Math Syntax and Functions
            <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/using-metric-math.html#metric-math-syntax>`__
            in the *Amazon CloudWatch User Guide* .

            Some of the parameters of this structure also have different uses whether you are using
            this structure in a ``GetMetricData`` operation or a ``PutMetricAlarm`` operation. These
            differences are explained in the following parameter list.

            - **Id** *(string) --* **[REQUIRED]**

              A short name used to tie this object to the results in the response. This name must be
              unique within a single call to ``GetMetricData`` . If you are performing math
              expressions on this set of data, this name represents that data and can serve as a
              variable in the mathematical expression. The valid characters are letters, numbers,
              and underscore. The first character must be a lowercase letter.

            - **MetricStat** *(dict) --*

              The metric to be returned, along with statistics, period, and units. Use this
              parameter only if this object is retrieving a metric and not performing a math
              expression on returned data.

              Within one MetricDataQuery object, you must specify either ``Expression`` or
              ``MetricStat`` but not both.

              - **Metric** *(dict) --* **[REQUIRED]**

                The metric to return, including the metric name, namespace, and dimensions.

                - **Namespace** *(string) --*

                  The namespace of the metric.

                - **MetricName** *(string) --*

                  The name of the metric. This is a required field.

                - **Dimensions** *(list) --*

                  The dimensions for the metric.

                  - *(dict) --*

                    Expands the identity of a metric.

                    - **Name** *(string) --* **[REQUIRED]**

                      The name of the dimension.

                    - **Value** *(string) --* **[REQUIRED]**

                      The value representing the dimension measurement.

              - **Period** *(integer) --* **[REQUIRED]**

                The granularity, in seconds, of the returned data points. For metrics with regular
                resolution, a period can be as short as one minute (60 seconds) and must be a
                multiple of 60. For high-resolution metrics that are collected at intervals of less
                than one minute, the period can be 1, 5, 10, 30, 60, or any multiple of 60.
                High-resolution metrics are those metrics stored by a ``PutMetricData`` call that
                includes a ``StorageResolution`` of 1 second.

                If the ``StartTime`` parameter specifies a time stamp that is greater than 3 hours
                ago, you must specify the period as follows or no data points in that time range is
                returned:

                * Start time between 3 hours and 15 days ago - Use a multiple of 60 seconds (1
                minute).

                * Start time between 15 and 63 days ago - Use a multiple of 300 seconds (5 minutes).

                * Start time greater than 63 days ago - Use a multiple of 3600 seconds (1 hour).

              - **Stat** *(string) --* **[REQUIRED]**

                The statistic to return. It can include any CloudWatch statistic or extended
                statistic.

              - **Unit** *(string) --*

                When you are using a ``Put`` operation, this defines what unit you want to use when
                storing the metric.

                In a ``Get`` operation, if you omit ``Unit`` then all data that was collected with
                any unit is returned, along with the corresponding units that were specified when
                the data was reported to CloudWatch. If you specify a unit, the operation returns
                only data data that was collected with that unit specified. If you specify a unit
                that does not match the data collected, the results of the operation are null.
                CloudWatch does not perform unit conversions.

            - **Expression** *(string) --*

              The math expression to be performed on the returned data, if this object is performing
              a math expression. This expression can use the ``Id`` of the other metrics to refer to
              those metrics, and can also use the ``Id`` of other expressions to use the result of
              those expressions. For more information about metric math expressions, see `Metric
              Math Syntax and Functions
              <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/using-metric-math.html#metric-math-syntax>`__
              in the *Amazon CloudWatch User Guide* .

              Within each MetricDataQuery object, you must specify either ``Expression`` or
              ``MetricStat`` but not both.

            - **Label** *(string) --*

              A human-readable label for this metric or expression. This is especially useful if
              this is an expression, so that you know what the value represents. If the metric or
              expression is shown in a CloudWatch dashboard widget, the label is shown. If Label is
              omitted, CloudWatch generates a default.

            - **ReturnData** *(boolean) --*

              When used in ``GetMetricData`` , this option indicates whether to return the
              timestamps and raw data values of this metric. If you are performing this call just to
              do math expressions and do not also need the raw data returned, you can specify
              ``False`` . If you omit this, the default of ``True`` is used.

              When used in ``PutMetricAlarm`` , specify ``True`` for the one expression result to
              use as the alarm. For all other metrics and expressions in the same ``PutMetricAlarm``
              operation, specify ``ReturnData`` as False.

            - **Period** *(integer) --*

              The granularity, in seconds, of the returned data points. For metrics with regular
              resolution, a period can be as short as one minute (60 seconds) and must be a multiple
              of 60. For high-resolution metrics that are collected at intervals of less than one
              minute, the period can be 1, 5, 10, 30, 60, or any multiple of 60. High-resolution
              metrics are those metrics stored by a ``PutMetricData`` operation that includes a
              ``StorageResolution of 1 second`` .

              If you are performing a ``GetMetricData`` operation, use this field only if you are
              specifying an ``Expression`` . Do not use this field when you are specifying a
              ``MetricStat`` in a ``GetMetricData`` operation.

        :type Tags: list
        :param Tags:

          A list of key-value pairs to associate with the alarm. You can associate as many as 50
          tags with an alarm.

          Tags can help you organize and categorize your resources. You can also use them to scope
          user permissions, by granting a user permission to access or change only resources with
          certain tag values.

          - *(dict) --*

            A key-value pair associated with a CloudWatch resource.

            - **Key** *(string) --* **[REQUIRED]**

              A string that you can use to assign a value. The combination of tag keys and values
              can help you organize and categorize your resources.

            - **Value** *(string) --* **[REQUIRED]**

              The value for the specified tag key.

        :type ThresholdMetricId: string
        :param ThresholdMetricId:

          If this is an alarm based on an anomaly detection model, make this value match the ID of
          the ``ANOMALY_DETECTION_BAND`` function.

          For an example of how to use this parameter, see the **Anomaly Detection Model Alarm**
          example on this page.

          If your alarm uses this parameter, it cannot have Auto Scaling actions.

        :rtype: :py:class:`cloudwatch.Alarm`
        :returns: Alarm resource
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def put_data(self, *args: Any, **kwargs: Any) -> None:
        """
        Publishes metric data points to Amazon CloudWatch. CloudWatch associates the data points
        with the specified metric. If the specified metric does not exist, CloudWatch creates the
        metric. When CloudWatch creates a metric, it can take up to fifteen minutes for the metric
        to appear in calls to  ListMetrics .

        You can publish either individual data points in the ``Value`` field, or arrays of values
        and the number of times each value occurred during the period by using the ``Values`` and
        ``Counts`` fields in the ``MetricDatum`` structure. Using the ``Values`` and ``Counts``
        method enables you to publish up to 150 values per metric with one ``PutMetricData``
        request, and supports retrieving percentile statistics on this data.

        Each ``PutMetricData`` request is limited to 40 KB in size for HTTP POST requests. You can
        send a payload compressed by gzip. Each request is also limited to no more than 20 different
        metrics.

        Although the ``Value`` parameter accepts numbers of type ``Double`` , CloudWatch rejects
        values that are either too small or too large. Values must be in the range of -2^360 to
        2^360. In addition, special values (for example, NaN, +Infinity, -Infinity) are not
        supported.

        You can use up to 10 dimensions per metric to further clarify what data the metric collects.
        Each dimension consists of a Name and Value pair. For more information about specifying
        dimensions, see `Publishing Metrics
        <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/publishingMetrics.html>`__
        in the *Amazon CloudWatch User Guide* .

        Data points with time stamps from 24 hours ago or longer can take at least 48 hours to
        become available for  GetMetricData or  GetMetricStatistics from the time they are
        submitted.

        CloudWatch needs raw data points to calculate percentile statistics. If you publish data
        using a statistic set instead, you can only retrieve percentile statistics for this data if
        one of the following conditions is true:

        * The ``SampleCount`` value of the statistic set is 1 and ``Min`` , ``Max`` , and ``Sum``
        are all equal.

        * The ``Min`` and ``Max`` are equal, and ``Sum`` is equal to ``Min`` multiplied by
        ``SampleCount`` .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/monitoring-2010-08-01/PutMetricData>`_

        **Request Syntax**
        ::

          response = metric.put_data()

        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def reload(self, *args: Any, **kwargs: Any) -> None:
        """
        Calls :py:meth:`CloudWatch.Client.list_metrics` to update the attributes of the Metric
        resource. Note that the load and reload methods are the same method and can be used
        interchangeably.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/monitoring-2010-08-01/None>`_

        **Request Syntax**

        ::

          metric.load()
        :returns: None
        """


class ServiceResourceAlarmsCollection(ResourceCollection):
    """
    A group of resources. See :py:class:`Action`.

    :type name: string
    :param name: The name of the collection
    :type definition: dict
    :param definition: The JSON definition
    :type resource_defs: dict
    :param resource_defs: All resources defined in the service
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def all(self) -> List[service_resource_scope.Alarm]:
        """
        Creates an iterable of all Alarm resources in the collection.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/monitoring-2010-08-01/DescribeAlarms>`_

        **Request Syntax**
        ::

          alarm_iterator = cloudwatch.alarms.all()

        :rtype: list(:py:class:`cloudwatch.Alarm`)
        :returns: A list of Alarm resources
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete(self, *args: Any, **kwargs: Any) -> None:
        """
        Deletes the specified alarms. You can delete up to 50 alarms in one operation. In the event
        of an error, no alarms are deleted.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/monitoring-2010-08-01/DeleteAlarms>`_

        **Request Syntax**
        ::

          response = cloudwatch.alarms.delete()

        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def disable_actions(self, *args: Any, **kwargs: Any) -> None:
        """
        Disables the actions for the specified alarms. When an alarm's actions are disabled, the
        alarm actions do not execute when the alarm state changes.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/monitoring-2010-08-01/DisableAlarmActions>`_

        **Request Syntax**
        ::

          response = cloudwatch.alarms.disable_actions()

        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def enable_actions(self, *args: Any, **kwargs: Any) -> None:
        """
        Enables the actions for the specified alarms.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/monitoring-2010-08-01/EnableAlarmActions>`_

        **Request Syntax**
        ::

          response = cloudwatch.alarms.enable_actions()

        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def filter(
        self,
        AlarmNames: List[str] = None,
        AlarmNamePrefix: str = None,
        StateValue: Literal["OK", "ALARM", "INSUFFICIENT_DATA"] = None,
        ActionPrefix: str = None,
        MaxRecords: int = None,
        NextToken: str = None,
    ) -> List[service_resource_scope.Alarm]:
        """
        Creates an iterable of all Alarm resources in the collection filtered by kwargs passed to
        method.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/monitoring-2010-08-01/DescribeAlarms>`_

        **Request Syntax**
        ::

          alarm_iterator = cloudwatch.alarms.filter(
              AlarmNames=[
                  'string',
              ],
              AlarmNamePrefix='string',
              StateValue='OK'|'ALARM'|'INSUFFICIENT_DATA',
              ActionPrefix='string',
              MaxRecords=123,
              NextToken='string'
          )
        :type AlarmNames: list
        :param AlarmNames:

          The names of the alarms.

          - *(string) --*

        :type AlarmNamePrefix: string
        :param AlarmNamePrefix:

          The alarm name prefix. If this parameter is specified, you cannot specify ``AlarmNames`` .

        :type StateValue: string
        :param StateValue:

          The state value to be used in matching alarms.

        :type ActionPrefix: string
        :param ActionPrefix:

          The action name prefix.

        :type MaxRecords: integer
        :param MaxRecords:

          The maximum number of alarm descriptions to retrieve.

        :type NextToken: string
        :param NextToken:

          The token returned by a previous call to indicate that there is more data available.

        :rtype: list(:py:class:`cloudwatch.Alarm`)
        :returns: A list of Alarm resources
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def iterator(self, **kwargs: Any) -> ResourceCollection:
        """
        Get a resource collection iterator from this manager.

        :rtype: :py:class:`ResourceCollection`
        :return: An iterable representing the collection of resources
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def limit(self, count: int) -> List[service_resource_scope.Alarm]:
        """
        Creates an iterable up to a specified amount of Alarm resources in the collection.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/monitoring-2010-08-01/DescribeAlarms>`_

        **Request Syntax**
        ::

          alarm_iterator = cloudwatch.alarms.limit(
              count=123
          )
        :type count: integer
        :param count: The limit to the number of resources in the iterable.

        :rtype: list(:py:class:`cloudwatch.Alarm`)
        :returns: A list of Alarm resources
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def page_size(self, count: int) -> List[service_resource_scope.Alarm]:
        """
        Creates an iterable of all Alarm resources in the collection, but limits the number of items
        returned by each service call by the specified amount.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/monitoring-2010-08-01/DescribeAlarms>`_

        **Request Syntax**
        ::

          alarm_iterator = cloudwatch.alarms.page_size(
              count=123
          )
        :type count: integer
        :param count: The number of items returned by each service call

        :rtype: list(:py:class:`cloudwatch.Alarm`)
        :returns: A list of Alarm resources
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def pages(self) -> List[Boto3ServiceResource]:
        """
        A generator which yields pages of resource instances after
        doing the appropriate service operation calls and handling
        any pagination on your behalf. Non-paginated calls will
        return a single page of items.

        Page size, item limit, and filter parameters are applied
        if they have previously been set.

            >>> bucket = s3.Bucket('boto3')
            >>> for page in bucket.objects.pages():
            ...     for obj in page:
            ...         print(obj.key)
            'key1'
            'key2'

        :rtype: list(:py:class:`~boto3.resources.base.ServiceResource`)
        :return: List of resource instances
        """


class ServiceResourceMetricsCollection(ResourceCollection):
    """
    A group of resources. See :py:class:`Action`.

    :type name: string
    :param name: The name of the collection
    :type definition: dict
    :param definition: The JSON definition
    :type resource_defs: dict
    :param resource_defs: All resources defined in the service
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def all(self) -> List[service_resource_scope.Metric]:
        """
        Creates an iterable of all Metric resources in the collection.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/monitoring-2010-08-01/ListMetrics>`_

        **Request Syntax**
        ::

          metric_iterator = cloudwatch.metrics.all()

        :rtype: list(:py:class:`cloudwatch.Metric`)
        :returns: A list of Metric resources
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def filter(
        self,
        Namespace: str = None,
        MetricName: str = None,
        Dimensions: List[MetricsFilterDimensionsTypeDef] = None,
        NextToken: str = None,
    ) -> List[service_resource_scope.Metric]:
        """
        Creates an iterable of all Metric resources in the collection filtered by kwargs passed to
        method.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/monitoring-2010-08-01/ListMetrics>`_

        **Request Syntax**
        ::

          metric_iterator = cloudwatch.metrics.filter(
              Namespace='string',
              MetricName='string',
              Dimensions=[
                  {
                      'Name': 'string',
                      'Value': 'string'
                  },
              ],
              NextToken='string'
          )
        :type Namespace: string
        :param Namespace:

          The namespace to filter against.

        :type MetricName: string
        :param MetricName:

          The name of the metric to filter against.

        :type Dimensions: list
        :param Dimensions:

          The dimensions to filter against.

          - *(dict) --*

            Represents filters for a dimension.

            - **Name** *(string) --* **[REQUIRED]**

              The dimension name to be matched.

            - **Value** *(string) --*

              The value of the dimension to be matched.

        :type NextToken: string
        :param NextToken:

          The token returned by a previous call to indicate that there is more data available.

        :rtype: list(:py:class:`cloudwatch.Metric`)
        :returns: A list of Metric resources
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def iterator(self, **kwargs: Any) -> ResourceCollection:
        """
        Get a resource collection iterator from this manager.

        :rtype: :py:class:`ResourceCollection`
        :return: An iterable representing the collection of resources
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def limit(self, count: int) -> List[service_resource_scope.Metric]:
        """
        Creates an iterable up to a specified amount of Metric resources in the collection.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/monitoring-2010-08-01/ListMetrics>`_

        **Request Syntax**
        ::

          metric_iterator = cloudwatch.metrics.limit(
              count=123
          )
        :type count: integer
        :param count: The limit to the number of resources in the iterable.

        :rtype: list(:py:class:`cloudwatch.Metric`)
        :returns: A list of Metric resources
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def page_size(self, count: int) -> List[service_resource_scope.Metric]:
        """
        Creates an iterable of all Metric resources in the collection, but limits the number of
        items returned by each service call by the specified amount.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/monitoring-2010-08-01/ListMetrics>`_

        **Request Syntax**
        ::

          metric_iterator = cloudwatch.metrics.page_size(
              count=123
          )
        :type count: integer
        :param count: The number of items returned by each service call

        :rtype: list(:py:class:`cloudwatch.Metric`)
        :returns: A list of Metric resources
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def pages(self) -> List[Boto3ServiceResource]:
        """
        A generator which yields pages of resource instances after
        doing the appropriate service operation calls and handling
        any pagination on your behalf. Non-paginated calls will
        return a single page of items.

        Page size, item limit, and filter parameters are applied
        if they have previously been set.

            >>> bucket = s3.Bucket('boto3')
            >>> for page in bucket.objects.pages():
            ...     for obj in page:
            ...         print(obj.key)
            'key1'
            'key2'

        :rtype: list(:py:class:`~boto3.resources.base.ServiceResource`)
        :return: List of resource instances
        """


class MetricAlarmsCollection(ResourceCollection):
    """
    A group of resources. See :py:class:`Action`.

    :type name: string
    :param name: The name of the collection
    :type definition: dict
    :param definition: The JSON definition
    :type resource_defs: dict
    :param resource_defs: All resources defined in the service
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def all(self) -> List[service_resource_scope.Alarm]:
        """
        Creates an iterable of all Alarm resources in the collection.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/monitoring-2010-08-01/DescribeAlarmsForMetric>`_

        **Request Syntax**
        ::

          alarm_iterator = metric.alarms.all()

        :rtype: list(:py:class:`cloudwatch.Alarm`)
        :returns: A list of Alarm resources
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete(self, *args: Any, **kwargs: Any) -> None:
        """
        Deletes the specified alarms. You can delete up to 50 alarms in one operation. In the event
        of an error, no alarms are deleted.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/monitoring-2010-08-01/DeleteAlarms>`_

        **Request Syntax**
        ::

          response = metric.alarms.delete()

        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def disable_actions(self, *args: Any, **kwargs: Any) -> None:
        """
        Disables the actions for the specified alarms. When an alarm's actions are disabled, the
        alarm actions do not execute when the alarm state changes.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/monitoring-2010-08-01/DisableAlarmActions>`_

        **Request Syntax**
        ::

          response = metric.alarms.disable_actions()

        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def enable_actions(self, *args: Any, **kwargs: Any) -> None:
        """
        Enables the actions for the specified alarms.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/monitoring-2010-08-01/EnableAlarmActions>`_

        **Request Syntax**
        ::

          response = metric.alarms.enable_actions()

        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def filter(
        self,
        Statistic: Literal["SampleCount", "Average", "Sum", "Minimum", "Maximum"] = None,
        ExtendedStatistic: str = None,
        Dimensions: List[AlarmsFilterDimensionsTypeDef] = None,
        Period: int = None,
        Unit: Literal[
            "Seconds",
            "Microseconds",
            "Milliseconds",
            "Bytes",
            "Kilobytes",
            "Megabytes",
            "Gigabytes",
            "Terabytes",
            "Bits",
            "Kilobits",
            "Megabits",
            "Gigabits",
            "Terabits",
            "Percent",
            "Count",
            "Bytes/Second",
            "Kilobytes/Second",
            "Megabytes/Second",
            "Gigabytes/Second",
            "Terabytes/Second",
            "Bits/Second",
            "Kilobits/Second",
            "Megabits/Second",
            "Gigabits/Second",
            "Terabits/Second",
            "Count/Second",
            "None",
        ] = None,
    ) -> List[service_resource_scope.Alarm]:
        """
        Creates an iterable of all Alarm resources in the collection filtered by kwargs passed to
        method.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/monitoring-2010-08-01/DescribeAlarmsForMetric>`_

        **Request Syntax**
        ::

          alarm_iterator = metric.alarms.filter(
              Statistic='SampleCount'|'Average'|'Sum'|'Minimum'|'Maximum',
              ExtendedStatistic='string',
              Dimensions=[
                  {
                      'Name': 'string',
                      'Value': 'string'
                  },
              ],
              Period=123,
              Unit=
                  'Seconds'|'Microseconds'|'Milliseconds'|'Bytes'|'Kilobytes'|'Megabytes'
                  |'Gigabytes'|'Terabytes'|'Bits'|'Kilobits'|'Megabits'|'Gigabits'|'Terabits'
                  |'Percent'|'Count'|'Bytes/Second'|'Kilobytes/Second'|'Megabytes/Second'
                  |'Gigabytes/Second'|'Terabytes/Second'|'Bits/Second'|'Kilobits/Second'
                  |'Megabits/Second'|'Gigabits/Second'|'Terabits/Second'|'Count/Second'|'None'
          )
        :type Statistic: string
        :param Statistic:

          The statistic for the metric, other than percentiles. For percentile statistics, use
          ``ExtendedStatistics`` .

        :type ExtendedStatistic: string
        :param ExtendedStatistic:

          The percentile statistic for the metric. Specify a value between p0.0 and p100.

        :type Dimensions: list
        :param Dimensions:

          The dimensions associated with the metric. If the metric has any associated dimensions,
          you must specify them in order for the call to succeed.

          - *(dict) --*

            Expands the identity of a metric.

            - **Name** *(string) --* **[REQUIRED]**

              The name of the dimension.

            - **Value** *(string) --* **[REQUIRED]**

              The value representing the dimension measurement.

        :type Period: integer
        :param Period:

          The period, in seconds, over which the statistic is applied.

        :type Unit: string
        :param Unit:

          The unit for the metric.

        :rtype: list(:py:class:`cloudwatch.Alarm`)
        :returns: A list of Alarm resources
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def iterator(self, **kwargs: Any) -> ResourceCollection:
        """
        Get a resource collection iterator from this manager.

        :rtype: :py:class:`ResourceCollection`
        :return: An iterable representing the collection of resources
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def limit(self, count: int) -> List[service_resource_scope.Alarm]:
        """
        Creates an iterable up to a specified amount of Alarm resources in the collection.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/monitoring-2010-08-01/DescribeAlarmsForMetric>`_

        **Request Syntax**
        ::

          alarm_iterator = metric.alarms.limit(
              count=123
          )
        :type count: integer
        :param count: The limit to the number of resources in the iterable.

        :rtype: list(:py:class:`cloudwatch.Alarm`)
        :returns: A list of Alarm resources
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def page_size(self, count: int) -> List[service_resource_scope.Alarm]:
        """
        Creates an iterable of all Alarm resources in the collection, but limits the number of items
        returned by each service call by the specified amount.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/monitoring-2010-08-01/DescribeAlarmsForMetric>`_

        **Request Syntax**
        ::

          alarm_iterator = metric.alarms.page_size(
              count=123
          )
        :type count: integer
        :param count: The number of items returned by each service call

        :rtype: list(:py:class:`cloudwatch.Alarm`)
        :returns: A list of Alarm resources
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def pages(self) -> List[Boto3ServiceResource]:
        """
        A generator which yields pages of resource instances after
        doing the appropriate service operation calls and handling
        any pagination on your behalf. Non-paginated calls will
        return a single page of items.

        Page size, item limit, and filter parameters are applied
        if they have previously been set.

            >>> bucket = s3.Bucket('boto3')
            >>> for page in bucket.objects.pages():
            ...     for obj in page:
            ...         print(obj.key)
            'key1'
            'key2'

        :rtype: list(:py:class:`~boto3.resources.base.ServiceResource`)
        :return: List of resource instances
        """
