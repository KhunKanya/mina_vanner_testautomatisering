Feature: Add a new contact
# US03 som användare vill jag lägga till nya kontakter, så jag kan hålla koll på mina vänner

#  """  Lyckad lägg till vänner """
Scenario: Add valid contact
  Given användaren är på kontaktsidan
  When användaren lägger till Kanya Suwannajan med epost
  Then användaren kan ser "Kanya suwannajan" i kontaklista
  And användaren kan ser "kanya.beyon@gmail.com" i kontaklistan

#  """  Försök att lägga till kontakt med saknade fält """
Scenario: Try to add contact with missing fields
  Given användaren är på kontaktsidan2
  And användaren lämnar "Namn" och "E-post" tomma
  When användaren klickar på "Spara"2
  Then användaren kunde inte klickar på "Spara"

