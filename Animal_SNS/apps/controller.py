# -*- coding: utf-8 -*-
from flask import Flask, request, render_template, jsonify
from apps import app


@app.route('/')
def index():
    return render_template('front.html')

@app.route('/main')
def main():
    return render_template('main.html')