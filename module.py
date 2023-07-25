from flask import Blueprint, jsonify, request
import requests
from connectionManager import connectionManager

module_bp = Blueprint("module", __name__)


@module_bp.route("/testGet", methods=["GET"])
def get_test():
    mydb = connectionManager('localhost', 'root', 'senha', 'banco')
    query = "select * from tabela where nome = " + request.args.get("name")
    result = mydb.execute_query(query)
    return jsonify(result)


@module_bp.route("/testPost", methods=["POST"])
def get_testPost():
    mydb = connectionManager('localhost', 'root', 'senha', 'banco')
    query = "select * from tabela where nome = '" + \
        request.form.get("name") + "'"
    result = mydb.execute_query(query)
    return jsonify(result)
