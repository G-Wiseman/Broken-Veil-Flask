
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
    query = "Select * from Parties where partyId < 3"
    return queryDbJson(db, query)
    # Returns a list of all parties the authenticated user has access to. This endpoint should only return parties that the user is authorized to access.

# TODO: This function needs work. 
@bp.route("/parties", methods=["Post"])
def createNewParty():
    # Creates a new party owned by the authenticated user. The request body should include the name and any other relevant information about the party.
        return "// Creates a new party owned by the authenticated user. The request body should include the name and any other relevant information about the party."

@bp.route("/parties/<partyID>", methods=['GET'])
def getPartybyId(partyID):
    db = get_db()
    query = "Select * from Parties where partyId= ?;"
    return queryDbJson(db, query, (partyID,))

@bp.route("/parties/<partyID>", methods=['PUT'])
def updatePartybyID(partyID):
    return f"update the party withe ID: {partyID}"

@bp.route("/parties/<partyID>", methods=['DELETE'])
def deletePartybyID(partyID):
    return f"Delete the party with ID: {partyID}"

@bp.route("/parties/<partyID>/characters", methods=["GET"])
def getCharactersbyParty(partyID):
    return f"A JSON with ALL characters that belong to the party ID: {partyID}"

@bp.route("/parties/<partyID>/characters", methods=["POST"])
def updateCharactersbyParty(partyID):
    return f"A JSON with ALL characters that belong to the party ID: {partyID}"

@bp.route("parties/<partyID>/characters/<characterID>", methods=["GET"])
def getCharacterById(partyID, characterID):
    return f"Get the character info related to character{characterID} from {partyID}"

@bp.route("parties/<partyID>/characters/<characterID>", methods=["POST"])
def updateCharacterById(partyID, characterID):
    return f"Update the character info related to character{characterID} from {partyID}"

@bp.route("parties/<partyID>/characters/<characterID>", methods=["DELETE"])
def deleteCharacterById(partyID, characterID):
    return f"Delete the character info related to character{characterID} from {partyID}"