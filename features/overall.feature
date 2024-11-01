Feature: Checking the hours, rates, and amounts in Paid side for Overall Report

  Scenario: Verify that the hours, rates and amounts are the correct ones
    Given   Lunch Time
    When    Paid Breaks
    And     Hours
    And     Pay Rate
    And     Hol Hours
    And     Hol Rate
    And     OT Hours
    And     OT Rate
    And     DBLOT Hours
    And     DBLOT Rate
    And     Dollars
    And     Hol Dollars
    And     OT Dollars
    Then    DBLOT Dollars