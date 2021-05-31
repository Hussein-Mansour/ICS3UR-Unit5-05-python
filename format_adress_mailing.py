#!/usr/bin/env python3

# Created by: Hussein Mansour
# Created on: Sun/May30/2021
# This program formats your address to a mailing address


def apartment_question(apartment_no, apartment_yes=None):
    # return the apartment

    full_question = apartment_no
    if (apartment_yes is not None):
        full_question = full_question + " " + apartment_yes[0]
    full_question = full_question + " " + apartment_no

    return full_question


def main():
    # variables
    apartment_yes = None
    apartment_no = ("n" or "no" or "NO" or "N")
    # Introduction
    print("This program formats your address to a mailing address.")

    # Input

    # full name
    full_name = input("Enter your full name: ")
    # apartment question
    question = input("Do you live in an apartment (y/n): ")
    if question.upper() == "Y" or question.upper() == "YES":
        apartment_yes = int(input("Enter your apartment number: "))
    # street number
    street_number = int(input("Enter your street number: "))
    # street name and type
    street_name_type = input(
        "Enter your street name and type (Main St, Express Pkwy ...): ")
    # city name
    city_name = input("Enter your city: ")
    # province
    enter_province = input(
        "Enter your province (as an abbreviation, ex: ON, BC ...): ")
    # postal code
    postal_code = input("Enter your postal code (123 456): ")

    # Output

    # output for full name
    print("\n{0}".format(full_name.upper()))
    # output for question, street number, street name and type
    if (apartment_yes is not None):
        apartment_question(apartment_no, apartment_yes=None)
        print(apartment_yes, "-", street_number, street_name_type.upper())
    else:
        apartment_question(apartment_no)
        print(street_number, street_name_type.upper())
    # output for city name, province, postal code
    print("{0} {1}  {2}".format(
        city_name.upper(), enter_province.upper(), postal_code.upper()))


if __name__ == "__main__":
    main()
