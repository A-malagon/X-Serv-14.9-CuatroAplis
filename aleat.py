#!/usr/bin/python
# -*- coding: utf-8 -*-

import random


class numeroAleatorio:

    def parse(self, request, rest):
        return None

    def process(self, parsedRequest):
        numeroAleatorio = random.randint(0, 500000000)
        return("HTTP/1.1 200 OK", "<html>"
               "<html><body><h1>Hola</h1>" +
               "<body link='green'>" +
               "<body text='red'>" +
               "<body bgcolor='#87CEFA'>"
               "\r\n" +
               "<a href='" + str(numeroAleatorio) + "'>Dame otra</a>"
               "</body></html>" +
               "\r\n")
