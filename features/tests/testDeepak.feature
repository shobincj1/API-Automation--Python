# Created by 19732 at 2/12/2022
Feature: Listing a book

  # Listing a book
  Scenario: Listing a book using API
    Given endpoint is set
    When User sends a post request
    Then validate the book id

  Scenario Outline: Listing multiple books using API
    Given endpoint is set
    When User sends a post request with <isbn> and <aisle>
    Then validate the book id
    Examples:
    |isbn  |aisle  |
    |4455  |5550065  |
    |7477  |85866  |
    |9596  |96596  |
Scenario: Search the listed Books
    Given Add Book API is executed
    When User searches for added book
    Then User is able to find the search

