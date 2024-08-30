# -*- coding: utf-8 -*-

import zeep

# Interní zpravodajský systém
class Message(object):
    __module__ = 'skautis'

    def __init__(self, test):
        if test:
            self._client = zeep.Client('https://test-is.skaut.cz/JunakWebservice/Message.asmx?wsdl')
        else:
            self._client = zeep.Client('https://is.skaut.cz/JunakWebservice/Message.asmx?wsdl')

    # Načíst seznam typů příloh zpráv pro editaci šablony zprávy
    def MessageAttachmentTypeAllMultiple(self, ID_Login, ID_MessageType=None):
        return self._client.service.MessageAttachmentTypeAllMultiple({"ID_Login": ID_Login, "ID_MessageType": ID_MessageType})

    # Načíst seznam typů příloh zpráv
    def MessageAttachmentTypeAll(self, ID_Login, ID_MessageType=None):
        return self._client.service.MessageAttachmentTypeAll({"ID_Login": ID_Login, "ID_MessageType": ID_MessageType})

    # Načíst seznam skupin zpráv
    def MessageGroupAll(self, ID_Login, DisplayName=None, ReplyTo=None):
        return self._client.service.MessageGroupAll({"ID_Login": ID_Login, "DisplayName": DisplayName, "ReplyTo": ReplyTo})

    # Smazat skupinu zpráv
    def MessageGroupDelete(self, ID_Login, ID):
        return self._client.service.MessageGroupDelete({"ID_Login": ID_Login, "ID": ID})

    # Načíst detail skupiny zpráv
    def MessageGroupDetail(self, ID_Login, ID):
        return self._client.service.MessageGroupDetail({"ID_Login": ID_Login, "ID": ID})

    # Založit skupinu zpráv
    def MessageGroupInsert(self, ID_Login, ID, DisplayName=None, ReplyTo=None, Footer=None, FooterHtml=None, Note=None):
        return self._client.service.MessageGroupInsert({"ID_Login": ID_Login, "ID": ID, "DisplayName": DisplayName, "ReplyTo": ReplyTo, "Footer": Footer, "FooterHtml": FooterHtml, "Note": Note})

    # Načíst seznam zasílaných skupin zpráv osobě
    def MessageGroupPersonAll(self, ID_Login, ID_Person, ID_MessageGroup):
        return self._client.service.MessageGroupPersonAll({"ID_Login": ID_Login, "ID_Person": ID_Person, "ID_MessageGroup": ID_MessageGroup})

    # Upravit skupinu zpráv
    def MessageGroupUpdate(self, ID_Login, ID, DisplayName=None, ReplyTo=None, Footer=None, FooterHtml=None, Note=None):
        return self._client.service.MessageGroupUpdate({"ID_Login": ID_Login, "ID": ID, "DisplayName": DisplayName, "ReplyTo": ReplyTo, "Footer": Footer, "FooterHtml": FooterHtml, "Note": Note})

    # Načíst detail typu zprávy
    def MessageTypeDetail(self, ID_Login, ID=None):
        return self._client.service.MessageTypeDetail({"ID_Login": ID_Login, "ID": ID})

    # Upravit typ zprávy
    def MessageTypeUpdate(self, ID_Login, ID_MessageGroup, AllwaysEmail, ID=None, DisplayName=None, MessageGroup=None, Procedure=None, Note=None):
        return self._client.service.MessageTypeUpdate({"ID_Login": ID_Login, "ID_MessageGroup": ID_MessageGroup, "AllwaysEmail": AllwaysEmail, "ID": ID, "DisplayName": DisplayName, "MessageGroup": MessageGroup, "Procedure": Procedure, "Note": Note})

    # Smazat či obnovit zprávu
    def MessageUpdateDelete(self, ID_Login, ID, Delete):
        return self._client.service.MessageUpdateDelete({"ID_Login": ID_Login, "ID": ID, "Delete": Delete})

    # Ozančit zprávu jako přečtenou či nepřečtenou
    def MessageUpdateRead(self, ID_Login, ID, IsRead):
        return self._client.service.MessageUpdateRead({"ID_Login": ID_Login, "ID": ID, "IsRead": IsRead})

    # Nastavit příjemci, že byl odeslaný
    def MessageToSent(self, ID_Login, ID, Error=None):
        return self._client.service.MessageToSent({"ID_Login": ID_Login, "ID": ID, "Error": Error})

    # Načíst seznam webových zpráv přihlášeného uživatele
    def MessageAllWeb(self, ID_Login, ID_MessageGroup, IsRead, HasAttachments, IsActive, DateCreateFrom, DateCreateTo, Top, ID_MessageType=None, DisplayName=None):
        return self._client.service.MessageAllWeb({"ID_Login": ID_Login, "ID_MessageGroup": ID_MessageGroup, "IsRead": IsRead, "HasAttachments": HasAttachments, "IsActive": IsActive, "DateCreateFrom": DateCreateFrom, "DateCreateTo": DateCreateTo, "Top": Top, "ID_MessageType": ID_MessageType, "DisplayName": DisplayName})

    # Načíst seznam e-mailů k odeslání
    def MessageAll(self, ID_Login, InstanceKey=None):
        return self._client.service.MessageAll({"ID_Login": ID_Login, "InstanceKey": InstanceKey})

    # Načíst seznam příloh zprávy
    def MessageAttachmentAll(self, ID_Login, ID, ID_Message, IsHtmlImage):
        return self._client.service.MessageAttachmentAll({"ID_Login": ID_Login, "ID": ID, "ID_Message": ID_Message, "IsHtmlImage": IsHtmlImage})

    # Načíst detail zprávy (zpráva se zavoláním této funkce automaticky nastaví jako přečtená)
    def MessageDetail(self, ID_Login, ID):
        return self._client.service.MessageDetail({"ID_Login": ID_Login, "ID": ID})

    # Načíst nastavení zpráv přihlášené osoby
    def MessageMediumPersonAll(self, ID_Login, ID_Person, ID_MessageMedium=None):
        return self._client.service.MessageMediumPersonAll({"ID_Login": ID_Login, "ID_Person": ID_Person, "ID_MessageMedium": ID_MessageMedium})

    # Upravit nastavení zpráv
    def MessageMediumPersonUpdate(self, ID_Login, ID_Person, Subscribe, AllGroups, ID_MessageMedium=None, ID_MessageGroupArray=None):
        return self._client.service.MessageMediumPersonUpdate({"ID_Login": ID_Login, "ID_Person": ID_Person, "Subscribe": Subscribe, "AllGroups": AllGroups, "ID_MessageMedium": ID_MessageMedium, "ID_MessageGroupArray": ID_MessageGroupArray})

    # Načíst seznam šablon zpráv
    def MessageTemplateAll(self, ID_Login, ID_MessageType=None, ID_MessageMedium=None, DisplayName=None):
        return self._client.service.MessageTemplateAll({"ID_Login": ID_Login, "ID_MessageType": ID_MessageType, "ID_MessageMedium": ID_MessageMedium, "DisplayName": DisplayName})

    # Načíst detail šablony zprávy
    def MessageTemplateDetail(self, ID_Login, ID):
        return self._client.service.MessageTemplateDetail({"ID_Login": ID_Login, "ID": ID})

    # Upravit šablonu zprávy
    def MessageTemplateUpdate(self, ID_Login, ID, IsAttachmentVisible, ID_MessageType=None, MessageType=None, ID_MessageMedium=None, MessageMedium=None, DisplayName=None, Body=None):
        return self._client.service.MessageTemplateUpdate({"ID_Login": ID_Login, "ID": ID, "IsAttachmentVisible": IsAttachmentVisible, "ID_MessageType": ID_MessageType, "MessageType": MessageType, "ID_MessageMedium": ID_MessageMedium, "MessageMedium": MessageMedium, "DisplayName": DisplayName, "Body": Body})

    # Načíst seznam příjemců zprávy
    def MessageToAll(self, ID_Login, ID_Message):
        return self._client.service.MessageToAll({"ID_Login": ID_Login, "ID_Message": ID_Message})

    # Načíst seznam typů zpráv
    def MessageTypeAll(self, ID_Login, ID_MessageGroup, DisplayName=None, Key=None):
        return self._client.service.MessageTypeAll({"ID_Login": ID_Login, "ID_MessageGroup": ID_MessageGroup, "DisplayName": DisplayName, "Key": Key})

    # Upravit zprávu
    def MessageUpdate(self, ID_Login, ID, ID_MessageState=None):
        return self._client.service.MessageUpdate({"ID_Login": ID_Login, "ID": ID, "ID_MessageState": ID_MessageState})

    # Načíst seznam proměnných v šablonách zpráv
    def MessageVariableAll(self, ID_Login, DisplayName=None, ID_MessageType=None):
        return self._client.service.MessageVariableAll({"ID_Login": ID_Login, "DisplayName": DisplayName, "ID_MessageType": ID_MessageType})

