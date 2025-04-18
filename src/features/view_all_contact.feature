Feature: Show list of all my friends
# US01 som användare vill jag kunna se en lista över mina vänner, så att jag kontakta mina vänner.
Scenario: Vänlista visas
  Given användaren är på Vänlista sidan " https://forverkliga.se/JavaScript/my-contacts/#/friends "
  Then användare kan se alla vänner på Vänlista sidan

# US02 som användare vill jag kunna ändra information, så att jag kan uppdatera kontakta för mina vänner.

#  """ Lyckad ändring """
Scenario: ändra information med korrekt i båda fälten
  Given användaren ser vänlista som vill ändra information
  When jag klickar på "Ändra"-knappen för den kontakten
  And jag ändra namn eller e-post och klicka på "Spara"
  Then användaren ska se kontaktens uppdateras i listan.
#
#""" Felmeddelande vid tomma fält """
Scenario: ändra information med tomma fält
  Given användaren ser vänlista som vill ändra information2
  When jag klickar på "Ändra"-knappen för den kontakten2
  And jag rederar namn eller e-post
  Then kan inte klicka spara

