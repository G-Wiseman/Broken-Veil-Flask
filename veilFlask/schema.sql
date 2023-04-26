DROP TABLE IF EXISTS Characters;
DROP TABLE IF EXISTS Users;
DROP TABLE IF EXISTS Parties;
DROP TABLE IF EXISTS SpecialAttributes;
DROP TABLE IF EXISTS PartyUsers;



CREATE TABLE Users(
    usernameID VARCHAR(30) Unique primary key, 
    hashedpass VARCHAR(256)
    -- What other info should I gather? Email? 
    -- Discord account? 
    -- Profile Picture? 
);

CREATE Table Parties(
    partyId Integer Primary key, 
    partyName Varchar(60), 
    partyDescription VARCHAR(1000)
);


-- self._kills = 0
-- self._unconc = 0
-- self._deaths = 0
-- self._final_kills = 0
-- self._max_damage_dealt = 0
-- self._healing_dealt = 0
-- self._crit_success = 0
-- self._crit_fail = 0

CREATE TABLE Characters (
    characterId Integer primary key AUTOINCREMENT,
    characterName VARCHAR(30),
    party Integer, 
    userOwner Integer,
    -- Do I want any info on character < Bio / Age / Race / PhotoUrl / etc. > ??? 
    kills Integer,
    unconcious Integer,
    deaths Integer, 
    finalKills Integer,
    damage_dealt Integer,
    max_damage_dealt Integer,
    healing_dealt Integer,
    critical_success Integer, 
    critical_fail Integer,
    Foreign Key (party) REFERENCES Party(partyId), 
    Foreign Key (userOwner) REFERENCES Users(UsernameID)

);

CREATE TABLE SpecialAttributes(
    characterId Integer, 
    specialAttributeName Varchar(30), 
    specialAttributeValue Integer, 
    Foreign Key characterId REFERENCES Characters(characterId),
    Primary Key (characterId, specialAttributeName)
);

CREATE TABLE PartyUsers(
    usernameId Integer, 
    partyId Integer, 
    privilege Integer,
    Foreign Key UsernameID REFERENCES Users(usernameID),
    Foreign Key partyId REFERENCES Parties(partyId),
    Primary Key (usernameId, partyId)
    -- Do I want any fun things like "Title?, Status?, sessions played?"
    -- I'm not actually sure that sessions played would be a good fit for this 
);

