import pytest


@pytest.fixture
def get_dataset():
    return """
    {
      "id": "cfafbeb1-8037-4d0c-896e-a46fb27ff229",
      "name": "SalesMarketing",
      "addRowsAPIEnabled": false,
      "configuredBy": "john@contoso.com",
      "isRefreshable": true,
      "isEffectiveIdentityRequired": true,
      "isEffectiveIdentityRolesRequired": true,
      "isOnPremGatewayRequired": false
    }
    """


@pytest.fixture
def get_datasets():
    return """
    {
      "value": [
        {
          "id": "cfafbeb1-8037-4d0c-896e-a46fb27ff229",
          "name": "SalesMarketing",
          "addRowsAPIEnabled": false,
          "configuredBy": "john@contoso.com",
          "isRefreshable": true,
          "isEffectiveIdentityRequired": false,
          "isEffectiveIdentityRolesRequired": false,
          "isOnPremGatewayRequired": false
        },
        {
          "id": "cfafbeb1-8037-4d0c-896e-a46fb27ff229",
          "name": "MarketingSales",
          "addRowsAPIEnabled": true,
          "configuredBy": "john@contoso.com",
          "isRefreshable": false,
          "isEffectiveIdentityRequired": false,
          "isEffectiveIdentityRolesRequired": false,
          "isOnPremGatewayRequired": false
        }
      ]
    }
    """


@pytest.fixture
def execute_queries():
    return """
    {
      "results": [
        {
          "tables": [
            {
              "rows": [
                {
                  "MyTable[Year]": 2010,
                  "MyTable[Quarter]": "Q1"
                },
                {
                  "MyTable[Year]": 2010,
                  "MyTable[Quarter]": "Q2"
                },
                {
                  "MyTable[Year]": 2011,
                  "MyTable[Quarter]": "Q1"
                }
              ]
            }
          ]
        }
      ]
}
    """