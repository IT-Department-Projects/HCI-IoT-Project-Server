"""
Libraries imported and used for the program
* JSON
* Flask
* Gevent
* Time
* Face Recognition (https://github.com/ageitgey/face_recognition) 
"""
import json
from flask import Flask, request, Response, render_template, abort, url_for, jsonify, redirect
from flask_httpauth import HTTPDigestAuth
from flask_migrate import Migrate
import gevent
import time

import face_recognition
