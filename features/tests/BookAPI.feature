# Created by 19732 at 1/20/2022
Feature: verify whether Books are added and deleted using Library API
  # Enter feature description here

  Scenario: verify API functionality
      Given the book details are given
      When Add Book API is executed
      Then book is successfully added

