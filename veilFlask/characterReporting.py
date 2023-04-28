
import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
import json
from veilFlask.db import get_db, queryDbJson


bp = Blueprint('gameinfo', __name__, url_prefix='/gameinfo')

@bp.route("/parties", methods=["GET"])
def getParties():
    db = get_db()
    # Check that the user actually has access to view this party. 
    query = "Select * from Parties"
    return queryDbJson(db, query)
    # Returns a list of all parties the authenticated user has access to. This endpoint should only return parties that the user is authorized to access.

# TODO: This function isn't done yet.  
@bp.route("/parties", methods=["Post"])
def createNewParty():
    # Creates a new party owned by the authenticated user. The request body should include the name and any other relevant information about the party.
        return "// Creates a new party owned by the authenticated user. The request body should include the name and any other relevant information about the party."

@bp.route("/parties/<partyID>", methods=['GET'])
def getPartybyId(partyID):
    db = get_db()
    # TODO: Figure out if the user is actually allowed to access this partyId
    query = "Select * from Parties where partyId= ?;"
    return queryDbJson(db, query, (partyID,))

#TODO: This function isn't done yet.
@bp.route("/parties/<partyID>", methods=['PUT'])
def updatePartybyID(partyID):
    return f"update the party withe ID: {partyID}"


# Todo: Finish function
@bp.route("/parties/<partyID>", methods=['DELETE'])
def deletePartybyID(partyID):
    return f"Delete the party with ID: {partyID}"

@bp.route("/parties/<partyID>/characters", methods=["GET"])
def getCharactersbyParty(partyID):
    # TODO: Need to check that they actually belong to this partyId
    db = get_db()
    query = "select characters.* from parties join characters using (partyId) where partyId = ?;"
    return queryDbJson(db, query, (partyID,))
     
# TODO: 
@bp.route("/parties/<partyID>/characters", methods=["POST"])
def updateCharactersbyParty(partyID):
    return f"A JSON with ALL characters that belong to the party ID: {partyID}"

@bp.route("parties/<partyID>/characters/<characterID>", methods=["GET"])
def getCharacterById(partyID, characterID):
    # TODO: Check that they actually have the permissions to view this partyId
    db = get_db()
    query = "select  characters.* from parties join characters using (partyId) where partyId = ? and characterId=?;"
    return queryDbJson(db, query, (partyID, characterID))

# TODO: 
@bp.route("parties/<partyID>/characters/<characterID>", methods=["POST"])
def updateCharacterById(partyID, characterID):
    return f"Update the character info related to character{characterID} from {partyID}"


# TODO: FINISH THE FUNCTION
@bp.route("parties/<partyID>/characters/<characterID>", methods=["DELETE"])
def deleteCharacterById(partyID, characterID):
    # TODO: NEED TO AUTHENTICATE that they are actually have the priviledge to delete this character
    # Priviledges sufficient would be : - Character Owner OR - party moderator (priviledge high enough
    db = get_db()
