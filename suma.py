#!/usr/bin/python
# -*- coding: utf-8 -*-


class sumador:

    def parse(self, request, rest):
        listaRest = rest.split("/")
        try:
            numero1 = float(listaRest[1])
            numero2 = float(listaRest[2])
        except ValueError:
            return None
        return (numero1, numero2)

    def process(self, parsedRequest):
        if parsedRequest is not None:
            numero1 = str(parsedRequest[0])
            numero2 = str(parsedRequest[1])
            resultado = str(parsedRequest[0] + parsedRequest[1])
            resultado = numero1 + " + " + numero2 + " = " + resultado

            return ('200 OK', "<html><body><p><h1>" + resultado +
                    "<body text='red'>" +
                    "<body bgcolor='#006400'>"
                    "</h1></p></body></html>")
        else:
            return ("400 Bad Request", "<html>" +
                    "<body><h1>Error de formato: \
                    /suma/numero1/numero2 </h1>" +
                    "<body text='red'>" +
                    "<body bgcolor='#006400'>"
                    "</body></html>")
