
Feature: Söka kontakter
# ""US05 Som användarevill jag kunna söka efter mina vänner på namn eller e-post,
#så att jag kan hitta dem oavsett om jag använder stora eller små bokstäver.

Scenario: Söka efter en kontakt med namn (blandade versaler)
  Given att kontaktlistan är synlig
  When jag skriver "pICARD" i sökfältet
  Then ska kontakten med namnet "Jean-Luc Picard" visas

Scenario: Söka efter en kontakt med e-post (blandade versaler)
  Given att kontaktlistan är synlig2
  When jag skriver "STARFLEET.COM" i sökfältet
  Then ska kontakten med e-post "captain.picard@starfleet.com" visas