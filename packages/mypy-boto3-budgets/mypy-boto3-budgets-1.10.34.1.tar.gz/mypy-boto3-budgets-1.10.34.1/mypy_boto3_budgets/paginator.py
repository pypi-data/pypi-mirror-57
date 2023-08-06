"Main interface for budgets service Paginators"
from __future__ import annotations

from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_budgets.type_defs import (
    DescribeBudgetsResponseTypeDef,
    DescribeNotificationsForBudgetResponseTypeDef,
    DescribeSubscribersForNotificationResponseTypeDef,
    NotificationTypeDef,
    PaginatorConfigTypeDef,
)


__all__ = (
    "DescribeBudgetsPaginator",
    "DescribeNotificationsForBudgetPaginator",
    "DescribeSubscribersForNotificationPaginator",
)


class DescribeBudgetsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeBudgets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/budgets.html#Budgets.Paginator.DescribeBudgets)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, AccountId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> DescribeBudgetsResponseTypeDef:
        """
        [DescribeBudgets.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/budgets.html#Budgets.Paginator.DescribeBudgets.paginate)
        """


class DescribeNotificationsForBudgetPaginator(Boto3Paginator):
    """
    [Paginator.DescribeNotificationsForBudget documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/budgets.html#Budgets.Paginator.DescribeNotificationsForBudget)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, AccountId: str, BudgetName: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> DescribeNotificationsForBudgetResponseTypeDef:
        """
        [DescribeNotificationsForBudget.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/budgets.html#Budgets.Paginator.DescribeNotificationsForBudget.paginate)
        """


class DescribeSubscribersForNotificationPaginator(Boto3Paginator):
    """
    [Paginator.DescribeSubscribersForNotification documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/budgets.html#Budgets.Paginator.DescribeSubscribersForNotification)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        AccountId: str,
        BudgetName: str,
        Notification: NotificationTypeDef,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> DescribeSubscribersForNotificationResponseTypeDef:
        """
        [DescribeSubscribersForNotification.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/budgets.html#Budgets.Paginator.DescribeSubscribersForNotification.paginate)
        """
