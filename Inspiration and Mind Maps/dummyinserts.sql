-- INSERT statements for Users table
INSERT INTO Users (usernameID, hashedpass)
VALUES ('BobTheWarrior', 'hash123'),
       ('ElvishPrincess', 'secret456'),
       ('WizardMan', 'pass789'),
       ('DwarfKing', 'password1'),
       ('GoblinSlayer', 'securepass');

-- INSERT statements for Parties table
INSERT INTO Parties (partyId, partyName, partyDescription)
VALUES (1, 'The Adventurers', 'A party of brave adventurers on a quest'),
       (2, 'The Misfits', 'A group of unlikely heroes on a mission'),
       (3, 'The Brotherhood', 'A fellowship united in their cause');

-- INSERT statements for Characters table
INSERT INTO Characters (characterId, characterName, party, userOwner, kills, unconcious, deaths, finalKills, damage_dealt, max_damage_dealt, healing_dealt, critical_success, critical_fail)
VALUES (1, 'Grimfang', 1, 'BobTheWarrior', 10, 2, 1, 3, 500, 150, 300, 5, 2),
       (2, 'Galadriel', 1, 'ElvishPrincess', 7, 1, 0, 2, 350, 100, 200, 4, 1),
       (3, 'Merlin', 2, 'WizardMan', 3, 0, 2, 0, 50, 25, 100, 1, 3),
       (4, 'Gimli', 3, 'DwarfKing', 5, 1, 0, 1, 200, 75, 150, 2, 0),
       (5, 'Sneaky Pete', 3, 'GoblinSlayer', 2, 3, 2, 0, 100, 50, 50, 1, 4);

-- INSERT statements for SpecialAttributes table
INSERT INTO SpecialAttributes (characterId, specialAttributeName, specialAttributeValue)
VALUES (1, 'strength', 20),
       (2, 'intelligence', 18),
       (3, 'wisdom', 16),
       (4, 'constitution', 22),
       (5, 'dexterity', 14);

-- INSERT statements for PartyUsers table
INSERT INTO PartyUsers (usernameId, partyId, privilege)
VALUES ('BobTheWarrior', 1, 1),
       ('ElvishPrincess', 1, 2),
       ('WizardMan', 2, 1),
       ('DwarfKing', 3, 1),
       ('GoblinSlayer', 3, 2);
